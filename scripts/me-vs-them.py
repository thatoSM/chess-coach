import pathlib, re
from statistics import mean

HEADING = re.compile(r"^## Game (\d+) ", re.M)
ME_ACPL = re.compile(r"^- \*\*Me: .*? (\d+) ACPL\.\*\*", re.M)
OPP_ACPL = re.compile(r"^- \*\*Opponent: .*? (\d+) ACPL\.\*\*", re.M)

mine, theirs, closer = [], [], 0
for f in sorted(pathlib.Path("games/logs").glob("games-*.md")):
    text = f.read_text(encoding="utf-8", errors="replace")
    starts = [(m.start(), int(m.group(1))) for m in HEADING.finditer(text)]
    for i, (pos, num) in enumerate(starts):
        if num == 1:
            continue
        end = starts[i + 1][0] if i + 1 < len(starts) else len(text)
        ent = text[pos:end]
        me, opp = ME_ACPL.search(ent), OPP_ACPL.search(ent)
        if not me or not opp:
            continue
        my_acpl, opp_acpl = int(me.group(1)), int(opp.group(1))
        mine.append(my_acpl)
        theirs.append(opp_acpl)
        if my_acpl < opp_acpl:
            closer += 1

print(f"Games: {len(mine)}")
print(f"My mean ACPL:       {mean(mine):.1f}")
print(f"Opponent mean ACPL: {mean(theirs):.1f}")
print(f"Games where I was the more accurate player: {closer}/{len(mine)}")
