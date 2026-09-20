"""My rated rapid results by colour and opening family, against Elo expectation.

"Score" is points per game (win 1, draw 0.5). "Expected" is what the rating
difference predicted. "Diff" = Score - Expected, in percentage points: positive
means I did better than my rating said I should.

Small samples lie. Treat any family with fewer than 20 games as a hint only.

Usage (PowerShell, from the repo root, venv active):
    python scripts/opening-results.py
    python scripts/opening-results.py --since 2026-09-15
    python scripts/opening-results.py --since 2026-09-15 --family Caro-Kann
"""

import argparse
import collections
import datetime as dt
import json
import urllib.request

USER = "thatosm"


def fetch(since: str) -> list:
    start = dt.datetime.strptime(since, "%Y-%m-%d").replace(tzinfo=dt.timezone.utc)
    url = (
        "https://lichess.org/api/games/user/ThatoSM"
        f"?since={int(start.timestamp() * 1000)}&rated=true&perfType=rapid"
        "&opening=true&moves=false"
    )
    req = urllib.request.Request(
        url, headers={"Accept": "application/x-ndjson", "User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=300) as resp:
        return [json.loads(l) for l in resp.read().decode("utf-8").splitlines() if l.strip()]


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--since", default="2026-07-20", help="YYYY-MM-DD, UTC")
    ap.add_argument("--family", default="", help="only openings containing this text")
    ap.add_argument("--min-games", type=int, default=3)
    args = ap.parse_args()

    rows = collections.defaultdict(lambda: {"n": 0, "w": 0, "d": 0, "l": 0,
                                            "score": 0.0, "exp": 0.0})
    for g in fetch(args.since):
        white = g["players"]["white"]
        black = g["players"]["black"]
        me_white = white.get("user", {}).get("id") == USER
        me, opp = (white, black) if me_white else (black, white)
        if "rating" not in me or "rating" not in opp:
            continue
        name = g.get("opening", {}).get("name", "Unknown")
        if args.family and args.family.lower() not in name.lower():
            continue
        family = name if args.family else name.split(":")[0]
        winner = g.get("winner")
        pts = 0.5 if winner is None else (1.0 if (winner == "white") == me_white else 0.0)
        r = rows[("White" if me_white else "Black", family)]
        r["n"] += 1
        r["w" if pts == 1 else "d" if pts == 0.5 else "l"] += 1
        r["score"] += pts
        r["exp"] += 1 / (1 + 10 ** ((opp["rating"] - me["rating"]) / 400))

    print(f"{'Colour':6} {'Opening':45} {'N':>4} {'W-D-L':>9} {'Score':>6} {'Exp':>6} {'Diff':>6}")
    for (colour, family), r in sorted(rows.items(), key=lambda kv: (kv[0][0], -kv[1]["n"])):
        if r["n"] < args.min_games:
            continue
        score = 100 * r["score"] / r["n"]
        exp = 100 * r["exp"] / r["n"]
        wdl = f"{r['w']}-{r['d']}-{r['l']}"
        print(f"{colour:6} {family[:45]:45} {r['n']:>4} {wdl:>9} {score:>5.0f}% "
              f"{exp:>5.0f}% {score - exp:>+5.0f}")


if __name__ == "__main__":
    main()
