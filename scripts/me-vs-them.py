import re, pathlib
from statistics import mean

def to_cp(t):
    return (1000 if int(t[1:]) > 0 else -1000) if t.startswith("#") else int(round(float(t)*100))

mine, theirs, closer = [], [], 0
for f in sorted(pathlib.Path("games/pgn").glob("*.pgn")):
    text = f.read_text(encoding="utf-8", errors="replace")
    w = re.search(r'\[White "([^"]+)"\]', text)
    evals = re.findall(r'\[%eval ([^\]]+)\]', text)
    if not w or len(evals) < 20:
        continue
    cps = [to_cp(e.strip()) for e in evals]
    im_white = w.group(1).lower() == "thatosm"
    a, b = [], []
    for i in range(len(cps)):
        before = cps[i-1] if i > 0 else 20
        white_moved = (i % 2 == 0)
        loss = (before - cps[i]) if white_moved else (cps[i] - before)
        loss = min(max(loss, 0), 1000)
        (a if white_moved == im_white else b).append(loss)
    if a and b:
        mine.append(mean(a)); theirs.append(mean(b))
        if mean(a) < mean(b): closer += 1

print(f"Games: {len(mine)}")
print(f"My mean ACPL:       {mean(mine):.1f}")
print(f"Opponent mean ACPL: {mean(theirs):.1f}")
print(f"Games where I was the more accurate player: {closer}/{len(mine)}")