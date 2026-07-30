# Game Log

Every analysed game, newest at the top, with the ONE lesson from each.

**Before adding an entry, read `docs/06-reading-an-analysis.md`.** Two entries
in this file have had to be rewritten because the colour and eval sign weren't
checked first.

Each entry is deliberately short. The *lesson* lives here; the *game* lives in
the link and the PGN. If I can't remember a game, I open the link — I don't
need a longer write-up.

---

## Game 10 — WIN · Black vs esteesAmin (1059) · White resigned

- Link: https://lichess.org/Wy1M8OYQ
- PGN: *not yet exported*
- Rating: 972 → 980 · State: [CONFIRM]
- **Me: 79% accuracy · 4 BLUNDERS · 1 mistake · 1 inaccuracy · 49 ACPL.**
  Phases: **Opening 95** / Middlegame 73 / Endgame 100.
- **Opponent: 59% · 3 blunders · 1 mistake · 3 inaccuracies · 79 ACPL.**
  Phases: Opening 94 / Middlegame 47 / Endgame 100.
- Jagged graph — a **blunder-brawl**. I won because White blundered worse, not
  because I controlled the game. The opposite of Game 9.

**Lesson — Leak #1, new shape: scan ORDER.**

Move 29: White played `29.Nxd6??`, making checkmate unavoidable for me.
`29...Qxg2#` was **mate in one.** I played `29...Nxd1??`, capturing a rook.
Lichess: "Lost forced checkmate sequence." #-1 → -6.5. Won anyway five moves
later.

Every prior instance of Leak #1 was *quiet move instead of forcing move*. This
was **capture instead of mate**. I did run a forcing search — I ran it in the
wrong order. Second missed forced mate in the log (first was `27...Qg3+` vs
RafaEspejo).

**Secondary:** the other three blunders (`25...Rxa4`, `27...Qg5`, `28...Nxe3`)
all sit in one five-move sharp stretch. Same root — moving fast, taking the
loud option.

**Strength: 95% opening — my best in the log by a distance.** Castled by move
5, handled White's `a3`/`b4` sideline without following a script. The opening
was my weakest phase in every prior game. First real evidence it's moving.

**The ONE thing to fix:** mate → checks → captures, in that order. A free rook
stays free; the mate might not.

---

## Game 9 — WIN · White vs water-dragon562 (1112) · Black resigned

- Link: https://lichess.org/SL1lenaL
- PGN: `games/pgn/game-09-water-dragon562.pgn`
- Rating: 965 → 972 · State: [CONFIRM]
- **Me: 93% accuracy · 0 blunders · 1 mistake · 0 inaccuracies · 15 ACPL.**
  Phases: Opening 80 / **Middlegame 100** / **Endgame 100**.
- **Opponent: 77% · 1 blunder · 1 mistake · 1 inaccuracy · 63 ACPL.**
  Phases: Opening 57 / Middlegame 96 / Endgame 96.
- **The best set of numbers in the log**, against an opponent 147 points above me.

**Lesson — the scan working, and one opening lapse.**

Move 7 `Bg5` pinned the f6 knight to the queen. Opponent played `8...Nxd5??` —
moving a pinned piece — and I answered **instantly with `9.Bxd8`, winning the
queen.** That is the exact pattern from my mistakes table. I saw it and took
it, then converted +5.4 → +12.3 over fourteen moves without a slip.

**The one miss — move 3.** I played `3.Bc4?`; `3.Nxe5` was there (+1.8 → +0.3).
Opponent had played `2...Bc5?` instead of `2...Nc6` — and the c6 knight is the
*only* defender of e5. The moment they developed the bishop instead, **e5 was
hanging**, and I played my Italian script move. **Leak #2 feeding Leak #1.**

**The ONE thing to fix:** when the opponent's opening move isn't the one I
expected, ask "what did that move stop defending?"

---

## Game 8 — WIN · Black vs Clotilde78891 · 67...Qb7# (checkmate)

- Link: https://lichess.org/Q5KjLCNz
- PGN: `games/pgn/game-08-clotilde78891.pgn`
- Eval direction: I was **Black**, so **negative** evals are my advantage.
- Best/worst eval: -11 / +0.1
- **Me: 90% accuracy · 1 blunder · 2 mistakes · 5 inaccuracies · 27 ACPL.**
  Phases: Opening 86 / **Middlegame 75** / Endgame 91.
- **Opponent: 85% · 2 blunders · 5 mistakes · 7 inaccuracies · 43 ACPL.**
  Phases: Opening 75 / Middlegame 69 / Endgame 86.
- **I outplayed them on every metric.** Never worse than equal at any point.

**Lesson — Leak #1, again.**

Move 29: I played `g5??`, a quiet pawn move. `Rf2+` — a **check** — was best.
-2.3 → +0.1. My only blunder in the game, and it gave away the whole advantage.

**The tell:** on **move 33 I played `Rf2+`** — the exact move I'd missed four
moves earlier. Nothing learned in between; the opponent handed the chance back
with `33.h4?`. *(Verified against the PGN: `Rf2+` was legal on move 29.)*

I SEE the move. I don't SEARCH for it.

**Secondary:** `26...fxe4?!` also handed back an edge (-1.0 → 0.0). Both errors
were in the middlegame — 75%, my weakest phase, a first.

**Strength:** the conversion. From `35.b3??` (-6.3) I ground -6 to -11 without a
wobble, promoted on move 52 (`a1=Q`), mated on move 67.

**⚠️ WARNING:** this game was misread TWICE — first as a loss, then as a heroic
comeback from a "dead-lost -10 position." Neither happened. The negative evals
were MY advantage as Black, and the "drifting rooks" (`Rg3`/`Re3`/`Rg5`) were
the OPPONENT'S moves.

*(Original analysis covered moves 26–67 from screenshots; the PGN now covers all 67.)*

---

## Game 7 — WIN · White vs Rinat2312 (1015)

- Link: https://lichess.org/2vLzuzL2
- PGN: *not yet exported*
- **82% accuracy, 1 blunder. Won at +8.5.**

**Lesson — opening autopilot (Leak #2).** Opponent hung a piece with `Nxe4??`
on move 5; I played `6.d3??` (my script) instead of `6.Nxe4` (free piece),
+3.4 → -0.8. Recovered in the middlegame with a run of checks/captures and won.
Same theme: quiet script move over a forcing capture.

---

## Game 6 — WIN · White vs AaranyaRameshwaran (894) · 30.Qxg5# (checkmate)

- Link: https://lichess.org/Uo8erzXG
- PGN: `games/pgn/game-06-aaranyarameshwaran.pgn`
- **92% accuracy, 0 blunders, 99% middlegame, 100% endgame.**

**Lesson — the redemption / proof the scan works.** Same day as Game 5's loss,
one game later. Took the free piece when the opponent blundered (`12.Qxd4`),
then drove a clean all-checks-and-captures mating sequence (moves 22–30). Both
halves of the scan demonstrated to myself in one afternoon: Game 5 skipped it
(57%), Game 6 ran it (92%).

---

## Game 5 — LOSS · Black vs sarinafaragh (995)

- Link: https://lichess.org/cZmwOEVK
- PGN: `games/pgn/game-05-sarinafaragh.pgn`
- **57% accuracy, 6 blunders. Jagged brawl. FRESH game, NOT tired.**

**Lesson — Leak #1, decisive, and the one-move-late pattern's first instance.**

Move 11: I played `O-O??`; `Nxf3+` — a check-AND-capture — was there. -1.6 → +1.6.

**And on move 12 I played `Nxf3+`.** *(Verified against the PGN.)* Same shape as
Game 8: I found the move ONE MOVE LATE, after the advantage had gone. This game
predates Game 8 and shows the identical thing. See the through-line below.

Being a FRESH game proved the cause was "didn't run the scan," not fatigue.
Lost a coin-flip brawl (opponent 56%) by blundering one more time than they did.

**Opening note:** opponent opened `2.Qh5` — a Scholar's Mate attempt. I answered
`3...Qe7`, which is exactly what `docs/04-openings.md` says NOT to do (it blocks
my own f8 bishop). `3...g6` or developing was available. I then spent move 5
undoing it with `Qd8`. **Two tempi lost to the wrong gambit answer.**

---

## Game 4 — WIN · Black vs RafaEspejo (904) · on time

- Link: https://lichess.org/qh94Xx2g
- PGN: `games/pgn/game-04-rafaespejo.pgn`
- **82% accuracy, 3 blunders. Blunder-trading brawl.**

**Lesson — won despite playing worse.** Was winning (-4.7), then blundered it
back, including missing a **FORCED MATE on move 27** (`Qg3+`; I played `Be6`).
*(Verified: `Qg3+` was legal.)* Won only because the opponent blundered more.
When winning big, SIMPLIFY and trade.

---

## Game 3 — WIN · White vs i_am_a_knight (834) · 34.Qd7# (checkmate)

- Link: https://lichess.org/YUdbsaKK
- PGN: `games/pgn/game-03-i-am-a-knight.pgn`
- **Opponent never castled; made 4 pawn moves in the opening.**

**Lesson — watched from the winning side WHY the opening principles exist.** His
king ran and got mated on move 34. My leak here: **castled on move 16** (too
late). **Castle by move 10.**

> **CORRECTION:** this entry previously also claimed I "missed a free bishop on
> f2 (`Rxf2` available, played `Qe2`)." **The PGN does not contain either move.**
> I never played `Qe2` in this game — or in any logged game. See the note in
> `docs/03-my-recurring-mistakes.md`.

---

## Game 2 — WIN · Black vs behnazpiroozkia (993) · on time

- Link: https://lichess.org/EL99vlEU
- PGN: `games/pgn/game-02-behnazpiroozkia.pgn`
- **Textbook opening (matched the Italian setup independently).**

**Lesson — recapture with a PIECE near my king, not a pawn.** Move 11 `gxf6`
shredded my king's pawn shield; `Qxf6` was available and keeps the pawns. Then
defended 20 moves accurately and came out a piece up. One bad decision, then
correct defence.

---

## Game 1 — profile snapshot (Lichess stats)

- Rating climb 601 (May) → 947 (Jul). The 24-game losing streak was Jan 2025,
  the "no practice" era. Puzzle count was 31 (!) vs 537 games: the original
  diagnosis. **The training ratio was the whole problem.**

---

## The through-line

**Strong structure, and a single sight/discipline leak (#1) that recurs until
the scan becomes automatic.**

- **Leak #1 is verified in 6 of the 9 played games** (4, 5, 7, 8, 9, 10). It is
  the whole ballgame.
- **The one-move-late pattern is now DOUBLE-CONFIRMED.** Game 5: missed
  `Nxf3+` on move 11, played it on move 12. Game 8: missed `Rf2+` on move 29,
  played it on move 33. Both verified against the PGN. This is the strongest
  evidence in the entire repo that the move is never missing from my chess —
  only the search is.
- **Endgame is consistently strong** (91–100%, and 100% in both of the last two
  games). A genuine weapon.
- **Opening is genuinely improving.** 57% → 80% → **95%** across games 7, 9, 10.
  It is no longer automatically my weakest phase.
- **Middlegame is now the phase to watch** (75%, 73% in my two worst recent
  showings; 100% in my best).
- The leak has NOT "moved to position." That reading came from a misread game
  and has been retracted.
