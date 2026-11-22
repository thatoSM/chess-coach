import pathlib, re
from collections import Counter

HEADING = re.compile(r"^## Game (\d+) ", re.M)
PLAYED_HOUR = re.compile(r"^- Played: \d{4}-\d{2}-\d{2} (\d{2}):\d{2} SAST", re.M)
ANALYSED = re.compile(r"^- \*\*Me: \d", re.M)

has_time, no_time, has_eval, total = 0, 0, 0, 0
hours = Counter()

for f in sorted(pathlib.Path("games/logs").glob("games-*.md")):
    text = f.read_text(encoding="utf-8", errors="replace")
    starts = [(m.start(), int(m.group(1))) for m in HEADING.finditer(text)]
    for i, (pos, num) in enumerate(starts):
        if num == 1:
            continue
        end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
        ent = text[pos:end]
        total += 1
        t = PLAYED_HOUR.search(ent)
        if t:
            has_time += 1
            hours[int(t.group(1))] += 1
        else:
            no_time += 1
        if ANALYSED.search(ent):
            has_eval += 1

print(f"Games found:             {total}")
print(f"  with a Played time:   {has_time}")
print(f"  without a timestamp:  {no_time}")
print(f"  with Lichess analysis: {has_eval}")

late = sum(v for k, v in hours.items() if k >= 21 or k < 3)
print(f"\nGames starting 21:00-03:00 SAST: {late}")
print("Hour histogram (SAST):")
for h in range(24):
    if hours[h]:
        print(f"  {h:02d}:00  {'#' * hours[h]}  ({hours[h]})")
