import re, pathlib
from collections import Counter

counts = Counter()
pairs = []
for f in sorted(pathlib.Path("games/pgn").glob("*.pgn")):
    text = f.read_text(encoding="utf-8", errors="replace")
    d = re.search(r'\[UTCDate "([\d.]+)"\]', text)
    n = re.search(r'game-(\d+)', f.name)
    if d:
        counts[d.group(1)] += 1
        if n:
            pairs.append((int(n.group(1)), d.group(1)))

print("Games per UTCDate (most common first):")
for day, c in counts.most_common(15):
    print(f"  {day}   {c}")

print("\nGame number vs date (every 10th file):")
for num, day in sorted(pairs)[::10]:
    print(f"  game-{num:<4} {day}")