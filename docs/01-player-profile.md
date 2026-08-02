# Player Profile

A factual snapshot. Update the numbers whenever they move meaningfully.

_Last updated: **2 August 2026**, from the Lichess profile and Rapid stats page.
Game log current to Game 48._

## Identity

- **Lichess:** ThatoSM — South Africa, member since 24 Nov 2024
- **Format:** 10+5 Rapid (10 minutes each, +5 seconds per move)
- **Colours:** 1.e4 as White, 1...e5 as Black. Italian-style development.

## Ratings

| Metric | Value | Note |
|---|---|---|
| **Rapid** | **1026** | All-time high, set 2 Aug 2026. Rank 265,844. Better than 18.1% of Rapid players. Progression over last 12 games: **+50** |
| Rating deviation | 45.00 | Still settling — expect swings |
| **Puzzles** | **~1491** | Was a stale ~610 before I trained properly. **CONFIRM:** read off a cropped screenshot |
| Blitz | 1114? | Provisional — only 9 games |
| Classical | 1091? | Provisional — only 12 games |
| Bullet / Antichess | — | 2 games each. Not a format I play |

## Rapid career numbers

| Metric | Value |
|---|---|
| Total games | 640 (615 rated, 96%) |
| Victories | 300 (47%) |
| Draws | 39 (6%) |
| Defeats | 301 (47%) |
| Disconnections | 13 (2%) |
| Average opponent | **841.92** |
| Time spent playing | 4 days, 6 hours |
| Highest rating | **1026** — 2 Aug 2026 |
| Lowest rating | **601** — 25 May 2026 |
| Longest winning streak | **10 games** — 1 Aug 2026 → 2 Aug 2026 (**current**) |
| Longest losing streak | 24 games — 17 Jan 2025 → 19 Jan 2025 |

**Read the average opponent figure carefully.** 841.92 is the average across all
640 games, most of them from the pre-training era. My recent opposition sits in
the 900–1050 band. The lifetime 47/47 win/loss split is a record of who I *was*,
not who I am now.

**601 → 1026 in about ten weeks** (25 May → 2 Aug 2026). The 24-game losing
streak and the 10-game winning streak are the two ends of that same climb.

> **CONFIRM:** the sidebar shows 616 Rapid games while the stats page shows 640
> total / 615 rated. Minor discrepancy — probably unrated games and a game
> finishing between screenshots. Not worth chasing.

**Coverage note:** the repo logs **48 games**. That is roughly **8%** of my
Rapid games. Every conclusion in `docs/03` rests on that 8%, and it is a
*recent, analysed* 8% — but it is not the full record.

## The key insight

**Puzzle rating (~1491) > game rating (1026), by roughly 465 points.**

**That gap has widened, not closed.** It was ~135 points at Game 10. I am now
rated far stronger at finding tactics when someone tells me a tactic exists than
at finding them unprompted. That gap IS my rating ceiling. Closing it doesn't
require learning anything new — it requires a routine (Scan A, see
`docs/02-training-system.md`).

**This is now proven four times, every one verified against the PGN:**

- **Game 5, move 11:** played `O-O`. `Nxf3+` was legal. **Played `Nxf3+` on
  move 12** — one move late, after the eval had already flipped.
- **Game 8, move 29:** played `g5`. `Rf2+` was legal. **Played `Rf2+` on move
  33** — four moves late, once the opponent handed the chance back.
- **Game 34, move 28:** played `b5`. **`Ra8#` was legal — mate in one.**
  **Played `Ra8+` on move 29**, one move late, by which point it lost.
- **Game 42, move 10:** played `Bg5`. `Nxe5` was best. **Played `Nxe5` on move
  11**, one move late, and resigned on the spot. An eleven-move loss.

Same move, same idea, nothing learned in between. I simply searched the second
time. The move is never missing from my chess. The search is missing from my
routine.

## Results by colour (47 played games)

| Colour | W–L–D | Score |
|---|---|---|
| **Black** | 17–7–0 | **70.8%** |
| White | 11–10–2 | 52.2% |

Black is decisively my stronger colour, and it holds in the recent stretch too
(Black 5–1 across games 39–48; White 2–2).

**As White, split by whether I got my opening:**

| Situation | W–L–D | Score |
|---|---|---|
| Black played `1...e5` | 8–5–1 | 61% |
| Black played anything else | 2–5–1 | **31%** |

The Italian isn't the problem. Games where I never get to play it are. Both of
my two most recent White losses (41, 42) were Scandinavians. **Eight games is
too small a sample to rebuild a repertoire on — collect more first.**

**As Black, split by opponent's opening:**

| Situation | W–L | Score |
|---|---|---|
| vs Italian / Four Knights Italian | 3–3 | 50% |
| vs everything else | 13–4 | 76% |

But two of the three Italian losses (Games 21, 26) were **winning positions
given away by Leak #1**, not opening problems. A different third move saves
neither.

## Phase scores (where my accuracy lives)

| Game | Opening | Middlegame | Endgame | Accuracy | Blunders |
|---|---|---|---|---|---|
| 10 vs esteesAmin | **95** | 73 | **100** | 79% | 4 |
| 9 vs water-dragon562 | 80 | **100** | **100** | 93% | 0 |
| 8 vs Clotilde78891 | 86 | 75 | 91 | 90% | 1 |
| 7 vs Rinat2312 | 57 | — | — | 82% | 1 |
| 6 vs AaranyaRameshwaran | — | 99 | 100 | 92% | 0 |
| 5 vs sarinafaragh | — | — | — | 57% | 6 |

> **CONFIRM:** this table stops at Game 10 because Lichess's API doesn't expose
> accuracy %. Games 11–48 have blunder/mistake/ACPL counts and phase *divisions*
> in `games/logs/`, but not phase accuracy. Either backfill these by hand from
> the game links or accept that this table is a historical snapshot.

**Opening — no longer my weak phase.** 57% → 86% → 80% → **95%** across games
7–10.

**Middlegame — the phase to watch.** The most volatile number I have. It tracks
one thing only: whether I ran the scan. It is not a knowledge gap.

**Endgame — consistently my strongest.** 91–100%. A genuine weapon. Game 41 is
the one counter-example: +6.01 at move 48, thrown away with `Kb3`.

## Strengths (genuine, evidence-backed)

- **Endgame technique.** 91–100% across games. Game 8: converted a large
  advantage from move 35 to checkmate on move 67 without a wobble. Game 45:
  converted a 70-move win ending in `Nc6#`. Long conversions do not shake me.
- **Punishing opponent errors when I'm looking.** Game 9: opponent moved a
  pinned piece on move 8, I played `9.Bxd8` and won the queen instantly.
- **Playing up.** Game 9's 93% / 0 blunders came against an opponent rated 147
  points above me. My best game is against my strongest opposition.
- **Structure.** I know my opening setup cold and reach playable middlegames.
- **Defence.** Game 2: defended accurately for 20 straight moves under pressure
  and emerged a piece up.
- **I don't tilt into resignation.** I play games out — and it wins games.
  Games 4, 8, 10, 44 and 48 were all won after I'd given away a winning position.
- **I climb.** 601 → 1026 in ten weeks, off a 24-game losing streak.

## Weaknesses (in priority order)

1. **Leak #1 — forcing moves not searched for, or searched in the wrong order.**
   Everything else is downstream of this. It is the decisive error in **8 of my
   13 analysed losses** — and it is present in the current 10-game winning
   streak too. Four one-move-late instances now verified. See
   `docs/03-my-recurring-mistakes.md`.
2. **Capturing without checking the reply.** The reverse shape: I grab material
   in a winning position and get mated. Games 24 (`Bxb8` at +9.72), 14 (`Qxg4`
   at +5.27), 25 (`Rxb1`), 26 (`exd4` at -4.38). **Four instances — enough to
   look at, not yet enough to number.** Do not add it to the leak list until
   I've reviewed those four positions myself.
3. **Middlegame accuracy** — my most variable phase.
4. **Converting winning endgames.** Games 20 and 41: smooth declines from +5.46
   and +7.37. Two instances. Watch for a third.
5. **Opening autopilot (Leak #2)** — improving markedly. Not top-tier priority.
6. **Playing tired (Leak #5)** — a state problem, fully within my control.

## History

- **Nov 2024:** joined Lichess.
- **Jan 2025:** 24-game losing streak. The "no practice" era. Behind me.
- **May 2026:** learnt fundamentals via Duolingo. Rating bottomed at **601** on
  25 May.
- **May–Aug 2026:** real coaching + Lichess puzzle training. Rating **601 →
  1026**, puzzles **~610 → ~1491**.
- **1–2 Aug 2026:** 10-game winning streak, all-time high rating.
