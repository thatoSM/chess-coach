import re, pathlib
from datetime import date
from statistics import mean

TODAY = date(2026, 8, 7)

def to_cp(tok):
    if tok.startswith("#"):
        return 1000 if int(tok[1:]) > 0 else -1000
    return int(round(float(tok) * 100))

rows = []
for f in sorted(pathlib.Path("games/pgn").glob("*.pgn")):
    text = f.read_text(encoding="utf-8", errors="replace")
    d = re.search(r'\[UTCDate "(\d{4})\.(\d{2})\.(\d{2})"\]', text)
    w = re.search(r'\[White "([^"]+)"\]', text)
    if not (d and w):
        continue
    evals = re.findall(r'\[%eval ([^\]]+)\]', text)
    if len(evals) < 20:
        continue
    cps = [to_cp(e.strip()) for e in evals]
    im_white = w.group(1).lower() == "thatosm"
    losses = []
    for i in range(len(cps)):
        if (i % 2 == 0) != im_white:
            continue
        before = cps[i-1] if i > 0 else 20
        loss = (before - cps[i]) if im_white else (cps[i] - before)
        losses.append(min(max(loss, 0), 1000))
    if not losses:
        continue
    g = date(int(d.group(1)), int(d.group(2)), int(d.group(3)))
    rows.append(((TODAY - g).days, mean(losses), f.name))

recent = [(a, n) for ago, a, n in rows if ago <= 3]
before = [a for ago, a, n in rows if ago > 3]

print(f"Games with evals: {len(rows)}\n")
print(f"Last 3 days: n={len(recent)}")
for a, n in sorted(recent, key=lambda x: -x[0]):
    print(f"   {n:<40} ACPL {a:.0f}")
print(f"\nBaseline (older): n={len(before)}  mean ACPL={mean(before):.1f}" if before else "")
if recent:
    print(f"Last 3 days mean ACPL={mean([a for a, n in recent]):.1f}")