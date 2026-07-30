# Game Log

Every analysed game, newest at the top, with the ONE lesson from each. New games
get added here so the pattern stays visible over time.

Format: result · colour · opponent · accuracy/blunders · the lesson.

**Before adding an entry, read `docs/06-reading-an-analysis.md`.** Two entries
in this file have had to be rewritten because the colour and eval sign weren't
checked first.

---

## Game 8 — WIN · Black vs Clotilde78891 · 67...Qb7# (checkmate)

- **Me: 90% accuracy · 1 blunder · 2 mistakes · 5 inaccuracies · 27 ACPL.**
  Phases: Opening 86 / **Middlegame 75** / Endgame 91.
- **Opponent: 85% · 2 blunders · 5 mistakes · 7 inaccuracies · 43 ACPL.**
  Phases: Opening 75 / Middlegame 69 / Endgame 86.
- **I outplayed them on every single metric.** I was never worse than equal at
  any point. Peak advantage roughly -11. (I was Black; negative = my advantage.)

**Lesson — Leak #1, again.**

Move 29: I played `g5??`, a quiet pawn move. `Rf2+` — a **check** — was best.
Eval went -2.3 → +0.1. That single move gave away my entire advantage and was
my only blunder in the game.

**The tell that makes this the most useful game in the log:** on **move 33 I
played `Rf2+`.** The exact move I'd missed four moves earlier. Nothing was
learned in between; the opponent simply handed the chance back with `33.h4?`.

I SEE the move. I don't SEARCH for it.

**Secondary:** `26...fxe4?!` also handed back an edge (-1.0 → 0.0). Both of my
errors were in the middlegame, which at 75% was my weakest phase — a first.

**Strength:** the conversion. From White's `35.b3??` (-6.3) I ground the
position from -6 to -11 without a wobble, promoted on move 52 (`a1=Q`), and
mated on move 67. Endgame 91%.

**⚠️ WARNING FOR FUTURE ANALYSIS:** this game was misread TWICE — first as a
loss, then as a heroic comeback from a "dead-lost -10 position." Neither
happened. The negative evals were my advantage as Black, and the "drifting
rooks with no plan" attributed to me (`Rg3`/`Re3`/`Rg5`) were the OPPONENT'S
moves. Always confirm colour → result line → eval direction → move column,
before analysing.

*(Analysis covered moves 26–67 from screenshots; moves 1–25 not reviewed.)*

---

## Game 7 — WIN · White vs Rinat2312 (1015)
- **82% accuracy, 1 blunder. Won at +8.5.**
- Lesson: **opening autopilot (Leak #2).** Opponent hung a piece with `Nxe4??`
  on move 5; I played `6.d3??` (my script) instead of `6.Nxe4` (free piece),
  dropping +3.4 → -0.8. Recovered in the middlegame with a run of
  checks/captures and won. Same theme: quiet script move over a forcing
  capture. Opening was my weakest phase.

## Game 6 — WIN · White vs AaranyaRameshwaran (894)
- **92% accuracy, 0 blunders, 99% middlegame, 100% endgame. Checkmate.**
- Lesson: **the redemption / proof the scan works.** Same day as Game 5's loss,
  one game later. Took the free piece when the opponent blundered (`Qxd4`),
  then drove a clean all-checks-and-captures mating sequence (moves 22–30).
  Demonstrated both halves of the scan to myself in one afternoon: Game 5
  skipped it (57%), Game 6 ran it (92%).

## Game 5 — LOSS · Black vs sarinafaragh (995)
- **57% accuracy, 6 blunders. Jagged brawl. Fresh game, NOT tired.**
- Lesson: **Leak #1, decisive.** Move 11 `O-O??` instead of `Nxf3+` (a
  check-AND-capture) flipped eval -1.6 → +1.6. Being a FRESH game proved the
  cause was "didn't run the scan," not fatigue. Lost a coin-flip brawl
  (opponent 56% accuracy) by blundering one more time than they did.

## Game 4 — WIN · Black vs RafaEspejo (904), on time
- **82% accuracy, 3 blunders. Blunder-trading brawl.**
- Lesson: **won despite playing worse.** Was winning (-4.7), then blundered it
  back, including missing a FORCED MATE on move 27 (`Qg3+`; played `Be6`). Won
  only because the opponent blundered more. When winning big, SIMPLIFY and
  trade — don't keep it complicated.

## Game 3 — WIN · White vs i_am_a_knight (834), checkmate
- **Opponent never castled; made 4 pawn moves in the opening.**
- Lesson: watched from the winning side WHY the opening principles exist. His
  king ran 8 times and got mated on move 34. My leak here: castled on move 16
  (too late) and missed a free bishop on f2 for a move (`Rxf2` available,
  played `Qe2`). **Castle by move 10.**

## Game 2 — WIN · Black vs behnazpiroozkia (993), on time
- **Textbook opening (matched the Italian setup independently).**
- Lesson: **recapture with a PIECE near my king, not a pawn.** Move 11 `gxf6`
  shredded my king's pawn shield; `Qxf6` was available and keeps the pawns.
  Then defended 20 moves accurately and came out a piece up. One bad decision,
  then correct defence.

## Game 1 — profile snapshot (Lichess stats)
- Rating climb 601 (May) → 947 (Jul). The 24-game losing streak was Jan 2025,
  the "no practice" era — behind me. Puzzle count was 31 (!) vs 537 games: the
  original diagnosis. **The training ratio was the whole problem.**

---

## The through-line

**Strong structure, and a single sight/discipline leak (#1) that recurs until
the scan becomes automatic.**

- **Leak #1 appears in 7 of 8 logged games.** It is the whole ballgame.
- **Endgame is consistently strong** (91–100%) and is a genuine weapon — I
  convert long endings cleanly and I don't resign.
- **Opening was historically weakest**, but Game 8's 86% suggests that's
  improving. Middlegame is now the phase to watch.
- The leak has NOT "moved to position." That reading came from a misread game
  and has been retracted. It is still the same forcing-move search, missing.
