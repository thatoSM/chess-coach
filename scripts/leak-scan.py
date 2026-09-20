"""Classify every rated rapid game for Leak #1 and write the evidence files.

Leak #1 (see docs/03-my-recurring-mistakes.md): from a winning position I play
a move that throws a large part of the advantage away, while the engine's best
move was FORCING (a mate, a check, or a capture) and I did not play it.

Method
------
1. Pull my rated rapid games from the Lichess API (evals included).
2. Candidate move: I was at least +1.00 before the move (my point of view)
   and the move dropped the evaluation by 1.50 or more. Mates count as
   +/-10.00. Games Lichess has not analysed are screened with Stockfish
   instead of Lichess evals.
3. Each candidate is re-checked with Stockfish at --depth. It only counts as
   Leak #1 if Stockfish's best move is a mate, a check or a capture, and I
   played something else. Quiet best moves are reported separately, not as
   Leak #1.
4. Each instance gets one type, in scan order: missed mate in 1, missed forced
   mate, missed check, missed capture. "Scan order" is flagged when the move I
   played was itself a check or capture (right idea, wrong forcing move).

Outputs (in --out):
    leak-by-game.md    one row per game: Lichess ID, colour, result, label
    leak1-evidence.md  every verified instance with move, best move, swing
    leak-by-game.json  the same per-game labels, read by apply-leak-column.py
    leak1-evidence.json  instances as data, for later analysis

Usage (PowerShell, from the repo root, venv active):
    python scripts/leak-scan.py --stockfish "C:\\path\\to\\stockfish.exe"
    python scripts/leak-scan.py --stockfish stockfish --since 2026-07-20
"""

import argparse
import datetime as dt
import json
import pathlib
import sys
import time
import urllib.request

import chess
import chess.engine

USER = "thatosm"
CAP = 10.0            # mate scores are capped at +/-10 pawns
WIN_THRESHOLD = 1.00  # "winning" = at least +1.00 for me before the move
DROP_THRESHOLD = 1.50 # a candidate move loses at least 1.50


def fetch_games(since: str) -> list:
    """Download rated rapid games with evals since the given YYYY-MM-DD date."""
    start = dt.datetime.strptime(since, "%Y-%m-%d").replace(tzinfo=dt.timezone.utc)
    url = (
        "https://lichess.org/api/games/user/ThatoSM"
        f"?since={int(start.timestamp() * 1000)}&rated=true&perfType=rapid"
        "&evals=true&accuracy=true&opening=true&division=true"
    )
    req = urllib.request.Request(
        url,
        headers={"Accept": "application/x-ndjson", "User-Agent": "Mozilla/5.0"},
    )
    with urllib.request.urlopen(req, timeout=300) as resp:
        lines = resp.read().decode("utf-8").splitlines()
    games = [json.loads(line) for line in lines if line.strip()]
    games.sort(key=lambda g: g["createdAt"])
    return games


def my_colour(game: dict) -> chess.Color:
    white_id = game["players"]["white"].get("user", {}).get("id", "")
    return chess.WHITE if white_id == USER else chess.BLACK


def pawns_from_lichess(node: dict) -> float:
    """Lichess analysis node -> pawns from White's point of view, capped."""
    if "mate" in node:
        return CAP if node["mate"] > 0 else -CAP
    return max(-CAP, min(CAP, node.get("eval", 0) / 100))


def pawns_from_engine(score: chess.engine.PovScore) -> float:
    white = score.white()
    if white.is_mate():
        return CAP if white.mate() > 0 else -CAP
    return max(-CAP, min(CAP, white.score() / 100))


def white_evals(game: dict, board_moves: list, engine, screen_depth: int) -> list:
    """Eval after every ply, White's point of view. Index i = after ply i."""
    if "analysis" in game and len(game["analysis"]) >= len(board_moves):
        return [pawns_from_lichess(n) for n in game["analysis"][: len(board_moves)]]
    board = chess.Board()
    out = []
    for move in board_moves:
        board.push(move)
        if board.is_game_over():
            out.append(0.0 if not board.is_checkmate()
                       else (CAP if board.turn == chess.BLACK else -CAP))
            continue
        info = engine.analyse(board, chess.engine.Limit(depth=screen_depth))
        out.append(pawns_from_engine(info["score"]))
    return out


def classify(board: chess.Board, played: chess.Move, engine, depth: int):
    """Return (type, best_san, scan_order) if Leak #1, else ('quiet', best_san, False)."""
    info = engine.analyse(board, chess.engine.Limit(depth=depth))
    best = info["pv"][0]
    best_san = board.san(best)
    if best == played:
        return None
    score = info["score"].pov(board.turn)
    forcing_played = board.gives_check(played) or board.is_capture(played)
    if score.is_mate() and score.mate() > 0:
        kind = "missed mate in 1" if score.mate() == 1 else "missed forced mate"
    elif board.gives_check(best):
        kind = "missed check"
    elif board.is_capture(best):
        kind = "missed capture"
    else:
        return ("quiet", best_san, False)
    return (kind, best_san, forcing_played)


def ply_anchor(move: int, colour: str) -> int:
    """Lichess URLs jump to a ply (half-move), not a move number."""
    return (move - 1) * 2 + (1 if colour == "White" else 2)


def fmt(x: float) -> str:
    if x >= CAP:
        return "mate"
    if x <= -CAP:
        return "-mate"
    return f"{x:+.2f}"


def scan(games: list, engine, depth: int, screen_depth: int):
    per_game, evidence, quiet = [], [], []
    for n, game in enumerate(games, 1):
        if not game.get("moves"):
            continue
        me = my_colour(game)
        board = chess.Board()
        moves = []
        for san in game["moves"].split():
            moves.append(board.push_san(san))
        evals = white_evals(game, moves, engine, screen_depth)
        sign = 1 if me == chess.WHITE else -1
        board = chess.Board()
        reached_win = False
        hits = []
        prev = 0.2 * sign  # start position, roughly level
        for ply, move in enumerate(moves):
            after = evals[ply] * sign
            if board.turn == me:
                before = prev
                if before >= WIN_THRESHOLD:
                    reached_win = True
                if before >= WIN_THRESHOLD and before - after >= DROP_THRESHOLD:
                    result = classify(board, move, engine, depth)
                    if result:
                        kind, best_san, scan_order = result
                        row = {
                            "id": game["id"], "move": ply // 2 + 1,
                            "colour": "White" if me == chess.WHITE else "Black",
                            "played": board.san(move), "best": best_san,
                            "before": fmt(before), "after": fmt(after),
                            "type": kind, "scan_order": scan_order,
                        }
                        (quiet if kind == "quiet" else hits).append(row)
            board.push(move)
            prev = after
        winner = game.get("winner")
        result = "DRAW" if winner is None else (
            "WIN" if (winner == "white") == (me == chess.WHITE) else "LOSS")
        if hits:
            label = f"#1 x{len(hits)}"
        elif reached_win:
            label = "clean"
        else:
            label = "no winning position"
        per_game.append({
            "id": game["id"],
            "date": dt.datetime.fromtimestamp(game["createdAt"] / 1000,
                                              dt.timezone.utc).strftime("%Y-%m-%d"),
            "colour": "White" if me == chess.WHITE else "Black",
            "result": result,
            "opening": game.get("opening", {}).get("name", "?"),
            "reached_win": reached_win,
            "label": label,
            "analysed_by": "lichess" if "analysis" in game else "stockfish",
        })
        evidence.extend(hits)
        if n % 50 == 0:
            print(f"  {n}/{len(games)} games scanned", file=sys.stderr)
    return per_game, evidence, quiet


def write_outputs(out: pathlib.Path, per_game, evidence, quiet, depth: int):
    out.mkdir(parents=True, exist_ok=True)
    (out / "leak-by-game.json").write_text(json.dumps(per_game, indent=1))

    won = [g for g in per_game if g["reached_win"]]
    leaky = [g for g in won if g["label"].startswith("#1")]
    by_result = {}
    for r in ("WIN", "LOSS", "DRAW"):
        pool = [g for g in won if g["result"] == r]
        hit = [g for g in pool if g["label"].startswith("#1")]
        by_result[r] = (len(hit), len(pool))
    types = {}
    for e in evidence:
        types[e["type"]] = types.get(e["type"], 0) + 1
    scan_order = sum(e["scan_order"] for e in evidence)

    lines = [
        "# Leak #1 by game — auto-classified",
        "",
        "> Generated by `scripts/leak-scan.py`. Do not edit by hand. Human review",
        "> of any row goes in the game's entry in `games/logs/`, and the human",
        "> label in `games/game-log.md` always wins over this file.",
        "",
        f"Stockfish verification depth: {depth}. Games scanned: {len(per_game)}.",
        "",
        "## Headline",
        "",
        f"- Games that reached a winning position (+1.00 or better): **{len(won)}**",
        f"- Of those, games with at least one Leak #1 instance: **{len(leaky)}**"
        f" ({100 * len(leaky) / max(1, len(won)):.1f}%)",
    ]
    for r, (h, p) in by_result.items():
        if p:
            lines.append(f"- {r}: {h} of {p} ({100 * h / p:.0f}%)")
    lines += [
        f"- Instances: **{len(evidence)}** — " + ", ".join(
            f"{v} {k}" for k, v in sorted(types.items(), key=lambda kv: -kv[1])),
        f"- Scan-order instances (I played a check or capture, but the wrong one): {scan_order}",
        f"- Candidates rejected because the best move was quiet: {len(quiet)}",
        "",
        "## Per game (oldest first)",
        "",
        "| Date | Lichess | Colour | Result | Opening | Leak | Evals |",
        "|---|---|---|---|---|---|---|",
    ]
    for g in per_game:
        lines.append(
            f"| {g['date']} | [{g['id']}](https://lichess.org/{g['id']}) | {g['colour']} "
            f"| {g['result']} | {g['opening']} | {g['label']} | {g['analysed_by']} |")
    (out / "leak-by-game.md").write_text("\n".join(lines) + "\n")

    ev = [
        "# Leak #1 — verified instances",
        "",
        "> Generated by `scripts/leak-scan.py`. Evals are from MY point of view",
        "> (positive = good for me, whichever colour I played). Every best move was",
        "> legal in that exact position and checked by Stockfish.",
        ">",
        "> A \"missed forced mate\" can start with a quiet move: mate comes first in",
        "> the scan order, whatever the first move of the mate looks like.",
        "",
        "| Lichess | Move | Colour | I played | Best | Swing | Type | Scan order? |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for e in evidence:
        ev.append(
            f"| [{e['id']}](https://lichess.org/{e['id']}#{ply_anchor(e['move'], e['colour'])}) | {e['move']} "
            f"| {e['colour']} | `{e['played']}` | `{e['best']}` | {e['before']} → {e['after']} "
            f"| {e['type']} | {'yes' if e['scan_order'] else ''} |")
    ev += [
        "",
        "## Rejected candidates — best move was QUIET (not Leak #1)",
        "",
        "Big drops from winning positions where the engine's best move was not",
        "forcing — usually a piece left hanging or a threat ignored. Kept for",
        "human review; not numbered.",
        "",
        "| Lichess | Move | I played | Best | Swing |",
        "|---|---|---|---|---|",
    ]
    for q in quiet:
        ev.append(f"| [{q['id']}](https://lichess.org/{q['id']}#{ply_anchor(q['move'], q['colour'])}) | {q['move']} "
                  f"| `{q['played']}` | `{q['best']}` | {q['before']} → {q['after']} |")
    (out / "leak1-evidence.md").write_text("\n".join(ev) + "\n")
    (out / "leak1-evidence.json").write_text(json.dumps(
        {"leak1": evidence, "quiet": quiet}, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--stockfish", required=True, help="path to the Stockfish binary")
    ap.add_argument("--since", default="2026-07-20", help="YYYY-MM-DD, UTC")
    ap.add_argument("--depth", type=int, default=14, help="verification depth")
    ap.add_argument("--screen-depth", type=int, default=10,
                    help="depth used to evaluate games Lichess has not analysed")
    ap.add_argument("--out", default="games/leak-scan", help="output folder")
    args = ap.parse_args()

    print("Fetching games from Lichess...", file=sys.stderr)
    games = fetch_games(args.since)
    print(f"  {len(games)} rated rapid games", file=sys.stderr)
    t0 = time.time()
    with chess.engine.SimpleEngine.popen_uci(args.stockfish) as engine:
        per_game, evidence, quiet = scan(games, engine, args.depth, args.screen_depth)
    write_outputs(pathlib.Path(args.out), per_game, evidence, quiet, args.depth)
    print(f"Done in {time.time() - t0:.0f}s -> {args.out}/", file=sys.stderr)


if __name__ == "__main__":
    main()
