"""Fill the *pending* Leak cells in games/game-log.md from the auto scan.

Reads:
    games/logs/*.md                    game number -> Lichess ID (the Link: lines)
    games/pgn/game-NN-*.pgn            fallback for the same mapping ([Site] tag)
    games/leak-scan/leak-by-game.json  labels written by scripts/leak-scan.py

Only cells that still say *pending* are changed. Anything I have labelled by
hand is never touched. Auto labels are marked "(auto)" so they can't be
mistaken for a human review:

    #1 x3 (auto)       three verified Leak #1 instances
    clean (auto)       reached +1.00 or better, no Leak #1 instance
    no win (auto)      never reached +1.00, so Leak #1 couldn't fire

Games the scan didn't cover (casual games, variants, games older than the
scan window) stay *pending*.

Usage (PowerShell, from the repo root, venv active):
    python scripts/apply-leak-column.py --dry-run
    python scripts/apply-leak-column.py
"""

import argparse
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
LOG = ROOT / "games" / "game-log.md"
LOGS = ROOT / "games" / "logs"
PGNS = ROOT / "games" / "pgn"
PGN_NAME = re.compile(r"^game-(\d+)-")
SCAN = ROOT / "games" / "leak-scan" / "leak-by-game.json"

HEADING = re.compile(r"^## Game (\d+) ", re.M)
LINK = re.compile(r"lichess\.org/([A-Za-z0-9]{8})")
ROW = re.compile(r"^\| (\d+) \|(.*)\| \*pending\* \|\s*$")


def number_to_id() -> dict:
    """Map game number -> Lichess ID from every detail file."""
    mapping = {}
    for path in sorted(LOGS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        starts = [(m.start(), int(m.group(1))) for m in HEADING.finditer(text)]
        for i, (pos, num) in enumerate(starts):
            end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
            link = LINK.search(text[pos:end])
            if link:
                mapping[num] = link.group(1)
    # Fallback: the PGN files carry the Lichess link in their [Site] tag.
    for path in PGNS.glob("game-*.pgn"):
        m = PGN_NAME.match(path.name)
        if not m or int(m.group(1)) in mapping:
            continue
        link = LINK.search(path.read_text(encoding="utf-8", errors="ignore"))
        if link:
            mapping[int(m.group(1))] = link.group(1)
    return mapping


def label(row: dict) -> str:
    raw = row["label"]
    if raw.startswith("#1"):
        return f"#1 x{raw.split('x')[1]} (auto)"
    if raw == "clean":
        return "clean (auto)"
    return "no win (auto)"


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--dry-run", action="store_true", help="report, don't write")
    args = ap.parse_args()

    ids = number_to_id()
    scan = {row["id"]: row for row in json.loads(SCAN.read_text(encoding="utf-8"))}

    lines = LOG.read_text(encoding="utf-8").splitlines()
    filled, missing_link, not_scanned = 0, [], []
    for i, line in enumerate(lines):
        m = ROW.match(line)
        if not m:
            continue
        num = int(m.group(1))
        game_id = ids.get(num)
        if not game_id:
            missing_link.append(num)
            continue
        if game_id not in scan:
            not_scanned.append(num)
            continue
        lines[i] = f"| {num} |{m.group(2)}| {label(scan[game_id])} |"
        filled += 1

    print(f"Filled {filled} pending rows.")
    print(f"Still pending, no Lichess link found: {len(missing_link)}")
    print(f"Still pending, not in the scan (casual/variant/too old): {len(not_scanned)}")
    if not_scanned:
        print("  games:", ", ".join(map(str, sorted(not_scanned))))
    if args.dry_run:
        print("Dry run — nothing written.")
        return
    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {LOG.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
