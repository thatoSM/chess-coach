# My Recurring Mistakes — THE CORE FILE

Read this when analysing any new game — **after** confirming colour and eval
sign (`docs/06-reading-an-analysis.md`).

Verification standard: every move claim in this file was checked against the
PGN or the Lichess game with a legal-move generator, with my colour confirmed
first. **No row goes into any table without the game attached.** That rule
exists because Leak #4 was invented from the opponent's moves.

My mistakes are astonishingly consistent. It is almost always the SAME leak
wearing a new disguise.

---

## Leak #1 — I play a quiet move when a FORCING move wins (my #1 problem)

In game after game, a mate, check or capture sits on the board and I play a
tidy, sensible-looking move instead. My brain searches for "a good move," not
"the most forcing move." Those are different searches.

### The numbers — every rated rapid game since July 2026

From `scripts/leak-scan.py` (full output in `games/leak-scan/`), run on all
**786** rated rapid games from 20 July to 20 September 2026:

| Measure | Value |
|---|---|
| Games that reached a winning position (+1.00 or better) | **665** |
| …of those, with at least one Leak #1 instance | **388 (58.3%)** |
| In wins / losses / draws | 56% / 60% / 71% |
| Verified instances | **747** |
| Missed capture / missed check / missed forced mate / missed mate in 1 | 370 / 255 / 91 / 31 |
| Scan-order instances (I played a check or capture — the wrong one) | 254 |

**Read that twice: wins 56%, losses 60%.** Leak #1 is not what separates my
wins from my losses — it's in almost every game where I get ahead. I win the
ones where the opponent gives it back.

An earlier run (September, 446 logged games) found 57.7%. The method
reproduces.

**Trend — this is the baseline every fix gets measured against:**

| Period | Games with Leak #1 / games that reached +1.00 |
|---|---|
| 20–31 Jul | 44 / 67 (65.7%) |
| 1–15 Aug | 124 / 204 (60.8%) |
| 16–31 Aug | 71 / 129 (55.0%) |
| 1–20 Sep | 149 / 265 (56.2%) |

A slow drift down, not a fix. Re-run `scripts/leak-scan.py` every ~50 games
and add a row.

### How the scan decides

A move counts as Leak #1 only if: I was at least +1.00 before it, it dropped
the evaluation by 1.50 or more, Stockfish (depth 14) says the best move was a
mate, a check or a capture, and I played something else. The auto labels in
`games/game-log.md` are marked `(auto)`. My own review overrides them.

### Hand-verified instances (the original table)

| Game | I played | I should have played | What I missed |
|---|---|---|---|
| vs RafaEspejo (Black) | `27...Be6` | `27...Qg3+` | a FORCED MATE |
| vs sarinafaragh (Black) | `11...O-O` | `11...Nxf3+` | check-AND-capture; **and I played `Nxf3+` on move 12** |
| vs Rinat2312 (White) | `6.d3` | `6.Nxe4` | opponent hung a piece; I played my script |
| vs Clotilde78891 (Black) | `29...g5??` | `29...Rf2+` | a CHECK; **and I played `Rf2+` on move 33** |
| vs water-dragon562 (White) | `3.Bc4?` | `3.Nxe5` | `2...Bc5` stopped defending e5 |
| vs esteesAmin (Black) | `29...Nxd1??` | `29...Qxg2#` | **MATE IN ONE — I took a rook instead** |
| Game 34 vs doctorexcal (White) | `28.b5` | `28.Ra8#` | **MATE IN ONE — and I played `Ra8+` on move 29** |
| Game 37 vs pavanraaj (Black) | `28...Qc1+` | `28...Qxf4` | had a forced mate; played the wrong forcing move |
| Game 30 vs AnayAnand2016 (White) | `12.Be3` | `12.Qh5+` | a CHECK at +6.21 |
| Game 23 vs spoof-em-up (White) | `25.Kd3` | `25.Qxc7+` | check-AND-capture of the queen |
| Game 11 vs yahto19 (Black) | `23...Qd1` | `23...Qg3+` | a CHECK |
| Game 21 vs kai-reader (Black) | `9...h6` | `9...Bxd5` | a CAPTURE |
| Game 16 vs GiftmischerPTA (White) | `19.c4`, `20.dxc4`, `21.Nd7` | `Bxf6` | the same capture three moves running |
| Game 15 vs rafffaelll2022 (Black) | `6...Re8`, `7...Nh5` | `Nxg4`, `Bxh3` | two captures during a wild attack |
| Game 44 (WIN) | `25...f5`, `26...Qd2`, `27...f4` | `Qf4+` | forced mate, three moves running; then **`Qg3#` missed on move 30** |
| Game 47 (WIN) | `10...exd4`, `11...Nxd4` | `Nxe3` | the same capture twice, each from a winning position |
| Game 48 (WIN) | `19...fxe5` | `Qg4+` | **played `Qg4+` on move 22** |

The automated scan reproduces Games 34, 37, 44 and 47 exactly.

### The one-move-late pattern — the strongest evidence in this repo

I have played the exact move I missed, a move or two later, with nothing
learned in between:

- **Game 5, move 11:** played `O-O`, `Nxf3+` was legal. Played `Nxf3+` on move 12.
- **Game 8, move 29:** played `g5`, `Rf2+` was legal. Played `Rf2+` on move 33.
- **Game 34, move 28:** played `b5`, **`Ra8#` was mate in one.** Played `Ra8+`
  on move 29, by which point it lost.
- **Game 42, move 10:** played `Bg5`, `Nxe5` was best. Played `Nxe5` on move
  11 and resigned on move 11.
- **Game 48, move 19:** missed `Qg4+`, played it on move 22 (a win).

A later clock study found **42 cases in 150 games** of blundering Stockfish's
best move and then playing that exact move within the next three moves
(September). The move was never missing from my chess. **The search was
missing from my routine.**

### Scan ORDER

> **Mate → checks → captures. In that order.**
>
> Before I take anything: *"is there a check? does that check mate?"* A free
> rook will still be free one second later. The mate might not.

254 of the 747 instances are scan-order errors: I did play a forcing move,
just not the best one — usually a capture when a check or mate was there.

**Coaching note:** when a new game shows this leak (it usually will), name it
as Leak #1 and point here. It's not six problems, it's one problem six times.

---

## Leak #2 — opening autopilot

I play my memorised setup without looking, and miss free material when the
opponent deviates.

| Game | Opponent deviated | I played | Free material I walked past |
|---|---|---|---|
| vs Rinat2312 | `5...Nxe4??` | `6.d3` | the knight |
| vs water-dragon562 | `2...Bc5?` (not `Nc6`) | `3.Bc4` | the e5 pawn |

**Fix:** when the opponent's move isn't the one I expected, ask one question:
**"what did that move stop defending?"**

**Status: improving.** The opening is no longer my weak phase. With the new
Caro-Kann / Slav repertoire the risk is the same: a routine setup played
without looking.

---

## Leak #3 — triage failure (saving small when I could win big)

When something of mine is attacked, I rush to save it even when a bigger
capture is available elsewhere. Right kind of problem, wrong priority.

**Fix:** before saving an attacked piece, ask "is there something BIGGER
available?"

**Evidence status:** the original example (`Nxa5` instead of `Bxc7`) had no
game attached and matches no position in any logged PGN, so it has been
removed. This leak currently has **no attached instance**. Keep it only if a
game demonstrates it.

---

## Leak #4 — drifting / no plan (UNVERIFIED — evidence retracted)

Written up from Game 8, but the drifting rook moves were **the opponent's**.
No confirmed instance in my moves. Keep the planning question ("what is the
position asking me, and what is my laziest piece?") as good practice, but
**do not treat this as a documented weakness.**

## Leak #5 — playing chess after gaming (UNVERIFIED — no evidence found)

Written from assertion. Every related test (late-night play, time of day,
gaming, fatigue) found no signal — see `docs/08-what-the-data-says.md`.
**Do not reach for this leak when analysing a game.**

---

## Candidates — evidence exists, NOT numbered

Numbering is my decision after I've reviewed the positions myself.

### Candidate A — capturing without checking the reply

The reverse of Leak #1: I *make* a forcing move, usually a capture, without
asking what it allows.

| Game | I played | Was best | Swing |
|---|---|---|---|
| 24 vs mlbbhunter (White) | `15.Bxb8` | `15.Bd6` | +9.72 → mate in 2 against me |
| 14 vs rafffaelll2022 (White) | `9.Qxg4` | `9.Nc3` | +5.27 → -5.99 |
| 25 vs Aliyetkin (White) | `24.Rxb1` | `24.Qxe5` | +0.32 → mate in 7 against me |
| 26 vs Aaryav555 (Black) | `27...exd4` | `27...Qe7` | -4.38 → +6.59 (my disadvantage) |
| [z99cXmF7](https://lichess.org/z99cXmF7) (White) | `13.Qxd4` | `13.Nxd4` | recapture with the wrong piece → queen fork, resigned |

Game 21 move 13 (`dxe5` instead of `Rxe5`, into mate in 2) may belong here.
**Five-plus instances. My review pending.**

### Candidate B — failing to convert a winning endgame

- **Game 20 vs minikmustafa (White):** +5.46 at move 19 declining to -3 by
  move 31 across a dozen small errors.
- **Game 41 vs prince202621 (White):** +7.37 at move 35, bled to +1.20 by
  move 42, then `48.Kb3` (+6.01 → -6.63).
- An August analysis of 108 games found five more losses from endgames
  entered at +2.0 or better. The game IDs weren't recorded in the repo —
  re-derive them before counting.

Endgame conversion overall is the same as middlegame conversion (77% vs 76%),
so this may be a long-game problem rather than an endgame one.

### Candidate C — "found it, lost it" (candidate decay)

I identify the right forcing move while calculating, think on, and play
something else. Clock data: the move before a blunder takes a median 8.9 s vs
6.2 s for clean moves. 10.1% of my 300cp+ errors are this shape (September,
150 games). Countermeasure in use: write the candidate down (see
`training/board-card.md`).

### Candidate D — big drops where the best move was QUIET

The Leak #1 scan rejects drops from winning positions where Stockfish's best
move was quiet. There are **886** of them — more than the 747 Leak #1
instances. Most are likely a piece of mine left hanging or a threat ignored.
Listed in `games/leak-scan/leak1-evidence.md` for review. Not a leak until
I've looked at a sample of positions and named the shape.

---

## Removed rows

Deleted after checking every logged PGN, per this file's own rule:

- `Qe2` instead of `Rxf2` (vs behnazpiroozkia) — `Qe2` appears in no game of
  mine from that period. Almost certainly the opponent's move.
- `8...d6` instead of `8...b6` (vs Radmanj) — no such game exists.
- `Rab1` / `Nxa5` instead of `Bxc7` — no game attached; no matching position
  from the period the row was written.

---

## The meta-pattern

- **Leaks 1, 2 and 3 are one root:** I don't run the forcing search before
  quiet-looking moves, or I run it in the wrong order.
- **Leaks 4 and 5 are unverified.** Don't reach for them.
- **Candidates A–D are unnumbered on purpose.**

When coaching me: it's almost always one of these, and **usually #1**. Don't
reach for a new, more sophisticated diagnosis just because my accuracy was
high — Game 8 was 90% and was still #1.
