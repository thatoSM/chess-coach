import pathlib, re
from datetime import date
from statistics import mean

TODAY = date.today()

HEADING = re.compile(r"^## Game (\d+) ", re.M)
ENTRY_DATE = re.compile(r"^- Date: (\d{4})/(\d{2})/(\d{2})", re.M)
ME_ACPL = re.compile(r"^- \*\*Me: .*? (\d+) ACPL\.\*\*", re.M)

rows = []
for f in sorted(pathlib.Path("games/logs").glob("games-*.md")):
    text = f.read_text(encoding="utf-8", errors="replace")
    starts = [(m.start(), int(m.group(1))) for m in HEADING.finditer(text)]
    for i, (pos, num) in enumerate(starts):
        if num == 1:
            continue
        end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
        ent = text[pos:end]
        d, me = ENTRY_DATE.search(ent), ME_ACPL.search(ent)
        if not d or not me:
            continue
        played = date(int(d.group(1)), int(d.group(2)), int(d.group(3)))
        rows.append(((TODAY - played).days, int(me.group(1)), f"game-{num}"))

recent = [(a, n) for ago, a, n in rows if 0 <= ago <= 3]
before = [a for ago, a, n in rows if ago > 3]

print(f"Games with Lichess analysis: {len(rows)}\n")
print(f"Last 3 days: n={len(recent)}")
for a, n in sorted(recent, key=lambda x: -x[0]):
    print(f"   {n:<40} ACPL {a:.0f}")
print(f"\nBaseline (older): n={len(before)}  mean ACPL={mean(before):.1f}" if before else "")
if recent:
    print(f"Last 3 days mean ACPL={mean([a for a, n in recent]):.1f}")
