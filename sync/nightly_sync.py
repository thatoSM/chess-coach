"""Nightly Lichess sync for the chess-coach repo.

Does the same six parts as routine-prompt.md, as plain code, so it can run
on GitHub Actions without using any Claude usage:
  1. add new finished rated games as DRAFT entries
  2. backfill Lichess server analysis into draft entries (or mark them after 7 days)
  3. backfill my Elo into old headings
  4. remove zero-move games
  5. trim to the 200 most recent games (Game 1 always stays)
  6. regenerate STATS.md

Run from the repo root:  python sync/nightly_sync.py
Exit code 0 always unless something unexpected crashes; prints a summary line
that the workflow uses as the commit message.
"""

import io
import json
import re
import sys
import time
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

import chess
import chess.pgn

USER = "ThatoSM"
UA = {"User-Agent": "Mozilla/5.0"}
KEEP = 200
SAST = timezone(timedelta(hours=2))
ROOT = Path(".")
LOGS = ROOT / "games" / "logs"
PGN_DIR = ROOT / "games" / "pgn"
INDEX = ROOT / "games" / "game-log.md"
STATS = ROOT / "STATS.md"
RMIGNORE = ROOT / ".repomixignore"

NOT_YET = "[NOT YET ANALYSED]"
NO_SERVER = ("- **No Lichess server analysis.** Reviewed with the local engine. "
             "The auto Leak label comes from `scripts/leak-scan.py`.")

summary = []


# ---------- HTTP ----------

def http(url, accept="application/json", data=None):
    """GET (or POST if data) with User-Agent; one retry after a pause."""
    for attempt in range(2):
        try:
            headers = dict(UA, Accept=accept)
            if data is not None:
                headers["Content-Type"] = "text/plain"
            req = urllib.request.Request(url, data=data, headers=headers)
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read().decode("utf-8")
        except Exception as e:  # noqa: BLE001
            if attempt == 0:
                time.sleep(5)
            else:
                print(f"WARN request failed: {url} ({e})", file=sys.stderr)
                return None


def ndjson(text):
    return [json.loads(line) for line in (text or "").splitlines() if line.strip()]


# ---------- repo helpers ----------

def log_files():
    return sorted(LOGS.glob("games-*.md"))


def logged_ids():
    ids = set()
    for f in log_files():
        ids.update(re.findall(r"Link: https://lichess\.org/([A-Za-z0-9]{8})", f.read_text(encoding="utf-8")))
    return ids


def highest_number():
    nums = [int(m) for m in re.findall(r"^\| (\d+) \|", INDEX.read_text(encoding="utf-8"), re.M)]
    return max(nums) if nums else 0


def detail_file_for(n):
    lo = (n - 1) // 40 * 40 + 1
    hi = lo + 39
    return LOGS / f"games-{lo:03d}-{hi:03d}.md"


def slug(name):
    return re.sub(r"[^a-z0-9]", "-", name.lower())


def fmt_eval(e):
    if e is None:
        return "start"
    if "mate" in e:
        return f"#{e['mate']}"
    if "eval" in e:
        return f"{e['eval'] / 100:+.2f}"
    return "?"


def my_colour(g):
    return "white" if g["players"]["white"].get("user", {}).get("id") == USER.lower() else "black"


# ---------- part 1: new games ----------

def ending_text(g, board, last_san, n_plies):
    """(heading tail, Result-line sentence)"""
    status, winner = g["status"], g.get("winner")
    loser = {"white": "Black", "black": "White"}.get(winner, "")
    win_c = (winner or "").capitalize()
    if status == "mate":
        move_no = (n_plies + 1) // 2
        dots = "." if n_plies % 2 == 1 else "..."
        return f"{move_no}{dots}{last_san} (checkmate)", f"Checkmate on move {move_no} ({last_san})."
    if status == "resign":
        return f"{loser} resigned", f"{loser} resigned."
    if status == "outoftime":
        if winner:
            return "on time", f"{win_c} won on time."
        return "draw on time (insufficient material)", "Draw: time ran out with insufficient mating material."
    if status == "timeout":
        return f"{loser} left the game", f"{loser} left the game; {win_c} wins."
    if status == "stalemate":
        return "draw by stalemate", "Draw by stalemate."
    if status in ("draw", "insufficientMaterialClaim"):
        if board.is_insufficient_material() or status == "insufficientMaterialClaim":
            return "draw by insufficient material", "Draw by insufficient material."
        if board.can_claim_threefold_repetition() or board.is_repetition(3):
            return "draw by repetition", "Draw by repetition."
        if board.can_claim_fifty_moves():
            return "draw by fifty-move rule", "Draw by fifty-move rule."
        return "draw agreed", "Draw agreed."
    return status, f"Game ended: {status}."


def movetext(pgn_text):
    body = pgn_text.split("\n\n", 1)[1] if "\n\n" in pgn_text else ""
    body = re.sub(r"\{[^}]*\}", "", body)          # eval comments
    body = re.sub(r"\$\d+", "", body)               # NAGs
    body = re.sub(r"\(\s*[^()]*\)", "", body)       # simple variations
    body = re.sub(r"\d+\.\.\.", "", body)           # "12..." continuation numbers
    return " ".join(body.split())


def part1():
    known = logged_ids()
    text = http(f"https://lichess.org/api/games/user/{USER}?max=60&rated=true&opening=true"
                "&evals=true&accuracy=true&division=true&clocks=false&pgnInJson=true",
                accept="application/x-ndjson")
    if text is None:
        summary.append("Part 1 skipped (Lichess error)")
        return
    games = [g for g in ndjson(text)
             if g.get("rated") and g["id"] not in known
             and g["status"] not in ("started", "aborted", "created", "noStart")]
    games.sort(key=lambda g: g["createdAt"])
    n = highest_number()
    added = []
    for g in games:
        sans = (g.get("moves") or "").split()
        if not sans:
            continue
        n += 1
        pgn_text = g["pgn"].strip() + "\n\n\n"
        hdr = dict(re.findall(r'^\[(\w+) "(.*)"\]$', pgn_text, re.M))
        me = my_colour(g)
        opp = "black" if me == "white" else "white"
        my_name = me.capitalize()
        opp_name = g["players"][opp].get("user", {}).get("name") or hdr.get(opp.capitalize(), "?")
        my_elo = hdr.get(f"{my_name}Elo", "")
        opp_elo = hdr.get(f"{opp.capitalize()}Elo", "")
        my_elo_s = f" ({my_elo})" if my_elo and my_elo != "?" else ""
        opp_elo_s = f" ({opp_elo})" if opp_elo and opp_elo != "?" else ""

        winner = g.get("winner")
        result = "DRAW" if not winner else ("WIN" if winner == me else "LOSS")

        board = chess.Board()
        last_san = ""
        for s in sans:
            last_san = s
            board.push_san(s)
        tail, result_line = ending_text(g, board, last_san, len(sans))

        utc = datetime.strptime(hdr["UTCDate"] + " " + hdr["UTCTime"], "%Y.%m.%d %H:%M:%S").replace(tzinfo=timezone.utc)
        local = utc.astimezone(SAST)
        tc = hdr.get("TimeControl", "-")
        if "+" in tc:
            sec, inc = tc.split("+")
            sec = int(sec)
            tc_s = f"{sec // 60}+{inc}" if sec % 60 == 0 else f"{sec}s+{inc}"
        else:
            tc_s = tc
        event = hdr.get("Event", "").lower()
        if "casual" in event:
            mode = "Unrated"
        elif "rated" in event:
            mode = "Rated"
        else:
            mode = "Rated" if f"{my_name}RatingDiff" in hdr else "Unrated"
        eval_dir = "positive evals are my advantage." if me == "white" else "NEGATIVE evals are my advantage."

        pgn_name = f"game-{n:02d}-{slug(opp_name)}.pgn"
        (PGN_DIR / pgn_name).write_text(pgn_text, encoding="utf-8")

        entry = (
            f"## Game {n} — {result} · {my_name}{my_elo_s} vs {opp_name}{opp_elo_s} · {tail}\n\n"
            f"- Colour: I played {my_name}. Eval direction: {eval_dir}\n"
            f"- Link: https://lichess.org/{g['id']}\n"
            f"- Played: {local:%Y-%m-%d %H:%M} SAST\n"
            f"- Mode: {mode} · {tc_s}\n"
            f"- Date: {local:%Y/%m/%d}\n"
            f"- PGN: `games/pgn/{pgn_name}`\n"
            f"- Opening: {g.get('opening', {}).get('name', '—')}\n"
            f"- Moves:\n  ```\n  {movetext(pgn_text)}\n  ```\n"
            f"- Result: {result_line}\n"
            f"- **Me: {NOT_YET} accuracy · blunders · mistakes · inaccuracies · ACPL.**\n"
            f"- **Opponent: {NOT_YET}**\n\n"
            f"- Tea: [ ] · Before chess: [ ] · Focus (1–5): [ ]\n\n"
            f"**Lesson — [DRAFT: needs review, no leak number assigned yet].**\n\n"
            f"[DRAFT — fill in after reviewing the game with computer analysis.]\n\n"
            f"**The ONE thing to fix:** [DRAFT — not yet determined]\n\n---\n"
        )
        df = detail_file_for(n)
        if not df.exists():
            lo, hi = df.stem.split("-")[1:]
            df.write_text(f"# Games {lo}–{hi} — full entries\n\nDetail file. The scannable index is "
                          f"`games/game-log.md`.\n\n---\n", encoding="utf-8")
            prev = [f for f in log_files() if f != df and int(f.stem.split("-")[1]) < int(lo)]
            if prev:
                p = prev[-1] if len(prev) == 1 else max(prev, key=lambda f: int(f.stem.split("-")[1]))
                line = f"games/logs/{p.name}"
                ign = RMIGNORE.read_text(encoding="utf-8") if RMIGNORE.exists() else ""
                if line not in ign.splitlines():
                    RMIGNORE.write_text(ign.rstrip("\n") + "\n" + line + "\n", encoding="utf-8")
        body = df.read_text(encoding="utf-8")
        i = body.find("\n## Game ")
        if i == -1:
            body = body.rstrip("\n") + "\n" + entry
        else:
            body = body[: i + 1] + entry + body[i + 1:]
        df.write_text(body, encoding="utf-8")

        idx = INDEX.read_text(encoding="utf-8")
        row = f"| {n} | {result} | {my_name} | {opp_name}{opp_elo_s} | *pending* |\n"
        idx = idx.replace("|---|---|---|---|---|\n", "|---|---|---|---|---|\n" + row, 1)
        INDEX.write_text(idx, encoding="utf-8")
        added.append(n)
    if added:
        summary.append(f"games {added[0]}-{added[-1]}" if len(added) > 1 else f"game {added[0]}")


# ---------- part 2: backfill analysis ----------

ENTRY_RE = re.compile(r"^## Game (\d+) —.*?(?=^## Game |\Z)", re.M | re.S)


def analysis_block(g):
    me = my_colour(g)
    opp = "black" if me == "white" else "white"

    def line(who, c):
        a = g["players"][c]["analysis"]
        acc = f"{a['accuracy']}%" if "accuracy" in a else "—"
        return (f"- **{who}: {acc} accuracy · {a.get('blunder', 0)} blunders · {a.get('mistake', 0)} mistakes · "
                f"{a.get('inaccuracy', 0)} inaccuracies · {a.get('acpl', '—')} ACPL.**")

    out = [line("Me", me), line("Opponent", opp)]
    div = g.get("division") or {}
    if "middle" in div or "end" in div:
        parts = []
        if "middle" in div:
            parts.append(f"opening ends ~move {(div['middle'] + 1) // 2}")
        if "end" in div:
            parts.append(f"endgame starts ~move {(div['end'] + 1) // 2}")
        out.append(f"- Phases (Lichess division): {', '.join(parts)}.")
    sans = g["moves"].split()
    rows = []
    for i, e in enumerate(g["analysis"]):
        if "judgment" not in e or i >= len(sans):
            continue
        side_c = "white" if i % 2 == 0 else "black"
        who = "Me" if side_c == me else "Opponent"
        before = fmt_eval(g["analysis"][i - 1]) if i > 0 else "start"
        best = (e.get("variation") or "").split()
        rows.append(f"| {i // 2 + 1} | {who} ({side_c.capitalize()}) | `{sans[i]}` | {before} → {fmt_eval(e)} | "
                    f"{e['judgment']['name']} | `{best[0] if best else '—'}` |")
    text = "\n".join(out)
    if rows:
        text += ("\n\n**Computer analysis — flagged moves (from Lichess):**\n\n"
                 "| Move | Side | Played | Eval before → after | Judgment | Best |\n"
                 "|---|---|---|---|---|---|\n" + "\n".join(rows))
    return text


PLACEHOLDER_RE = re.compile(r"^- \*\*Me: \[NOT YET ANALYSED\].*\n- \*\*Opponent: \[NOT YET ANALYSED\]\*\*", re.M)


def part2():
    drafts = {}  # id -> (file, old)
    stale = 0
    now = datetime.now(SAST)
    for f in log_files():
        body = f.read_text(encoding="utf-8")
        changed = False
        for m in ENTRY_RE.finditer(body):
            ent = m.group(0)
            if NOT_YET not in ent:
                continue
            gid = re.search(r"Link: https://lichess\.org/([A-Za-z0-9]{8})", ent)
            played = re.search(r"Played: (\d{4}-\d{2}-\d{2} \d{2}:\d{2})", ent)
            if played and now - datetime.strptime(played.group(1), "%Y-%m-%d %H:%M").replace(tzinfo=SAST) > timedelta(days=7):
                body = body.replace(ent, PLACEHOLDER_RE.sub(NO_SERVER, ent, count=1), 1)
                changed = True
                stale += 1
            elif gid:
                drafts[gid.group(1)] = f
        if changed:
            f.write_text(body, encoding="utf-8")
    filled = 0
    if drafts:
        text = http("https://lichess.org/api/games/export/_ids?evals=true&accuracy=true&division=true&opening=true",
                    accept="application/x-ndjson", data=",".join(drafts).encode())
        for g in ndjson(text):
            if not g.get("analysis") or "analysis" not in g["players"]["white"] or "analysis" not in g["players"]["black"]:
                continue
            f = drafts[g["id"]]
            body = f.read_text(encoding="utf-8")
            for m in ENTRY_RE.finditer(body):
                ent = m.group(0)
                if f"lichess.org/{g['id']}" in ent and NOT_YET in ent:
                    new = PLACEHOLDER_RE.sub(lambda _: analysis_block(g), ent, count=1)
                    body = body.replace(ent, new, 1)
                    filled += 1
                    break
            f.write_text(body, encoding="utf-8")
    if filled or stale:
        summary.append(f"backfill analysis ({filled} analysed, {stale} marked local-engine)")


# ---------- part 3: Elo in old headings ----------

def part3():
    fixed = 0
    for f in log_files():
        body = f.read_text(encoding="utf-8")
        orig = body
        for m in ENTRY_RE.finditer(orig):
            ent = m.group(0)
            head = ent.split("\n", 1)[0]
            hm = re.match(r"^(## Game \d+ — \S+ · )(White|Black)( vs .*)$", head)
            pm = re.search(r"- PGN: `([^`]+)`", ent)
            if not hm or not pm or not Path(pm.group(1)).exists():
                continue
            elo = re.search(rf'^\[{hm.group(2)}Elo "([^"]*)"\]', Path(pm.group(1)).read_text(encoding="utf-8"), re.M)
            if elo and elo.group(1) not in ("", "?"):
                body = body.replace(head, f"{hm.group(1)}{hm.group(2)} ({elo.group(1)}){hm.group(3)}", 1)
                fixed += 1
        if body != orig:
            f.write_text(body, encoding="utf-8")
    if fixed:
        summary.append(f"Elo added to {fixed} headings")


# ---------- parts 4 + 5: remove games ----------

def remove_game(n):
    for f in log_files():
        body = f.read_text(encoding="utf-8")
        m = re.search(rf"^## Game {n} —.*?^---\n", body, re.M | re.S)
        if m:
            pm = re.search(r"- PGN: `([^`]+)`", m.group(0))
            if pm and Path(pm.group(1)).exists():
                Path(pm.group(1)).unlink()
            body = body[: m.start()] + body[m.end():]
            f.write_text(body, encoding="utf-8")
            if not re.search(r"^## (Game |The through-line)", body, re.M):
                f.unlink()
                if RMIGNORE.exists():
                    lines = [l for l in RMIGNORE.read_text(encoding="utf-8").splitlines() if l != f"games/logs/{f.name}"]
                    RMIGNORE.write_text("\n".join(lines) + "\n", encoding="utf-8")
            break
    for p in PGN_DIR.glob(f"game-{n:02d}-*.pgn"):
        p.unlink()
    idx = INDEX.read_text(encoding="utf-8")
    INDEX.write_text(re.sub(rf"^\| {n} \|.*\n", "", idx, flags=re.M), encoding="utf-8")


def part4():
    # A saved PGN with no moves = a zero-move game (cheaper than 200 API calls).
    removed = []
    for p in PGN_DIR.glob("game-*.pgn"):
        game = chess.pgn.read_game(io.StringIO(p.read_text(encoding="utf-8")))
        if game is not None and game.next() is None:
            removed.append(int(p.name.split("-")[1]))
    for n in removed:
        if n != 1:
            remove_game(n)
    if removed:
        summary.append(f"removed zero-move games {removed}")


def part5():
    cutoff = highest_number() - KEEP
    if cutoff <= 0:
        return
    nums = sorted({int(x) for x in re.findall(r"^\| (\d+) \|", INDEX.read_text(encoding="utf-8"), re.M)})
    for f in log_files():
        nums += [int(x) for x in re.findall(r"^## Game (\d+) —", f.read_text(encoding="utf-8"), re.M)]
    old = sorted({n for n in nums if 1 < n <= cutoff})
    for n in old:
        remove_game(n)
    if old:
        summary.append(f"trim to 200 (removed {len(old)})")


# ---------- part 6: STATS.md ----------

def d(iso):
    return iso[:10] if iso else "—"


def part6():
    perf_t = http(f"https://lichess.org/api/user/{USER}/perf/rapid")
    user_t = http(f"https://lichess.org/api/user/{USER}")
    if not perf_t or not user_t:
        summary.append("STATS.md left as is (Lichess error)")
        return
    P, U = json.loads(perf_t), json.loads(user_t)
    g = P.get("perf", {}).get("glicko", {})
    s = P.get("stat", {})
    c = s.get("count", {})
    rs = s.get("resultStreak", {})

    def get(o, *ks):
        for k in ks:
            if not isinstance(o, dict) or k not in o:
                return "—"
            o = o[k]
        return o

    def rnd(x):
        return round(x) if isinstance(x, (int, float)) else "—"

    secs = c.get("seconds")
    played = f"{secs // 86400}d {secs % 86400 // 3600}h" if isinstance(secs, int) else "—"
    names = {"ultraBullet": "UltraBullet", "bullet": "Bullet", "blitz": "Blitz", "rapid": "Rapid",
             "classical": "Classical", "correspondence": "Correspondence", "puzzle": "Puzzle"}
    rows = []
    for k, v in U.get("perfs", {}).items():
        if "rating" not in v:
            continue
        rows.append(f"| {names.get(k, k[:1].upper() + k[1:])} | {rnd(v['rating'])} | {v.get('games', '—')} | "
                    f"{'Yes' if v.get('prov') else 'No'} |")

    def streak(kind):
        m = rs.get(kind, {}).get("max", {})
        if not m:
            return "—"
        span = f" ({d(get(m, 'from', 'at'))} → {d(get(m, 'to', 'at'))})" if m.get("from") else ""
        return f"{m.get('v', '—')}{span}"

    logged = sum(len(re.findall(r"^## Game \d+ —", f.read_text(encoding="utf-8"), re.M)) for f in log_files())
    nb = P.get("perf", {}).get("nb")
    cov = f"{logged / nb * 100:.1f}%" if nb else "—"

    wld = {"White": [0, 0, 0], "Black": [0, 0, 0]}
    for res, col in re.findall(r"^\| \d+ \| (WIN|LOSS|DRAW) \| (White|Black) \|", INDEX.read_text(encoding="utf-8"), re.M):
        wld[col][{"WIN": 0, "LOSS": 1, "DRAW": 2}[res]] += 1
    colour_rows = []
    for col, (w, l, dr) in wld.items():
        tot = w + l + dr
        pts = w + dr / 2
        pts_s = f"{pts:g}"
        pct = f"{pts / tot * 100:.1f}%" if tot else "—"
        colour_rows.append(f"| {col} | {w}–{l}–{dr} | {pts_s}/{tot} ({pct}) |")

    STATS.write_text(f"""# Lichess Stats — auto-generated

> Generated by `routine-prompt.md`. Do not edit by hand — changes will be
> overwritten. Interpretation lives in `docs/01-player-profile.md`.

_Last generated: {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC_

## Ratings
| Perf | Rating | Games | Provisional |
|---|---|---|---|
{chr(10).join(rows)}

## Rapid
| Metric | Value |
|---|---|
| Rating | {rnd(g.get('rating'))} |
| Rating deviation | {rnd(g.get('deviation'))} |
| Progress (last 12) | {get(P, 'perf', 'progress')} |
| Rank | {P.get('rank', '—')} |
| Percentile | {P.get('percentile', '—')} |
| Highest | {get(s, 'highest', 'int')} ({d(get(s, 'highest', 'at'))}) |
| Lowest | {get(s, 'lowest', 'int')} ({d(get(s, 'lowest', 'at'))}) |
| Total games | {c.get('all', '—')} ({c.get('rated', '—')} rated) |
| W / D / L | {c.get('win', '—')} / {c.get('draw', '—')} / {c.get('loss', '—')} |
| Average opponent | {c.get('opAvg', '—')} |
| Disconnects | {c.get('disconnects', '—')} |
| Time played | {played} |
| Current win streak | {get(rs, 'win', 'cur', 'v')} |
| Longest win streak | {streak('win')} |
| Current loss streak | {get(rs, 'loss', 'cur', 'v')} |
| Longest loss streak | {streak('loss')} |

## Logged coverage
| Metric | Value |
|---|---|
| Rapid games played | {nb if nb is not None else '—'} |
| Games logged in this repo | {logged} |
| Coverage | {cov} |

## Results by colour (logged games only)
| Colour | W–L–D | Score |
|---|---|---|
{chr(10).join(colour_rows)}
""", encoding="utf-8")


if __name__ == "__main__":
    part1()
    part2()
    part3()
    part4()
    part5()
    part6()
    msg = "Nightly sync: " + (", ".join(summary) if summary else "stats refresh")
    print(msg)
