import re, pathlib
from collections import Counter

folder = pathlib.Path("games/pgn")
files = sorted(folder.glob("*.pgn"))

has_time, no_time, has_eval = 0, 0, 0
hours = Counter()

for f in files:
    text = f.read_text(encoding="utf-8", errors="replace")
    t = re.search(r'\[UTCTime "(\d{2}):', text)
    d = re.search(r'\[UTCDate "(\d{4})\.', text)
    if t and d:
        has_time += 1
        sast = (int(t.group(1)) + 2) % 24   # UTC -> Johannesburg
        hours[sast] += 1
    else:
        no_time += 1
    if "%eval" in text:
        has_eval += 1

print(f"PGN files found:        {len(files)}")
print(f"  with UTCDate+UTCTime: {has_time}")
print(f"  without timestamps:   {no_time}")
print(f"  with engine evals:    {has_eval}")

late = sum(v for k, v in hours.items() if k >= 21 or k < 3)
print(f"\nTimestamped games starting 21:00-03:00 SAST: {late}")
print("Hour histogram (SAST):")
for h in range(24):
    if hours[h]:
        print(f"  {h:02d}:00  {'#' * hours[h]}  ({hours[h]})")