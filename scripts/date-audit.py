import pathlib, re
from collections import Counter

HEADING = re.compile(r"^## Game (\d+) ", re.M)
DATE = re.compile(r"^- Date: (\d{4}/\d{2}/\d{2})", re.M)

counts = Counter()
pairs = []
for f in sorted(pathlib.Path("games/logs").glob("games-*.md")):
    text = f.read_text(encoding="utf-8", errors="replace")
    starts = [(m.start(), int(m.group(1))) for m in HEADING.finditer(text)]
    for i, (pos, num) in enumerate(starts):
        end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
        d = DATE.search(text[pos:end])
        if d:
            counts[d.group(1)] += 1
            pairs.append((num, d.group(1)))

print("Games per date (most common first):")
for day, c in counts.most_common(15):
    print(f"  {day}   {c}")

print("\nGame number vs date (every 10th game):")
for num, day in sorted(pairs)[::10]:
    print(f"  game-{num:<4} {day}")
