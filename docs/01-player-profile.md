# Player Profile

A factual snapshot. Update the numbers whenever they move meaningfully.

_Last updated: after Game 10 vs esteesAmin._

## Identity

- **Lichess:** ThatoSM
- **Format:** 10+5 Rapid (10 minutes each, +5 seconds per move)
- **Colours:** 1.e4 as White, 1...e5 as Black. Italian-style development.

## Ratings

| Metric | Value | Note |
|---|---|---|
| Rapid rating | **980** | Low of ~601 in May 2026. Climb: 947 → 965 → 972 → 980 |
| Puzzle rating | **~1116** | Was a stale ~610 before I trained properly |
| Games played | ~537 | **CONFIRM:** from the Game 1 snapshot, now out of date |
| Puzzles solved (original count) | 31 | **This was the whole diagnosis** |

> **CONFIRM:** update the games/puzzles counts.

## The key insight

**Puzzle rating (1116) > game rating (980).**

I am rated ~135 points stronger at finding tactics when someone tells me a
tactic exists than I am at finding them unprompted. That gap IS my rating
ceiling. Closing it doesn't require learning anything new — it requires a
routine (Scan A, see `docs/02-training-system.md`).

**This is now proven twice, both verified against the PGN:**

- **Game 5, move 11:** played `O-O`. `Nxf3+` was legal. **Played `Nxf3+` on
  move 12** — one move late, after the eval had already flipped.
- **Game 8, move 29:** played `g5`. `Rf2+` was legal. **Played `Rf2+` on move
  33** — four moves late, once the opponent handed the chance back.

Same move, same idea, nothing learned in between. I simply searched the second
time. The move is never missing from my chess. The search is missing from my
routine.

## Phase scores (where my accuracy lives)

Recorded phase scores, most recent first:

| Game | Opening | Middlegame | Endgame | Accuracy | Blunders |
|---|---|---|---|---|---|
| 10 vs esteesAmin | **95** | 73 | **100** | 79% | 4 |
| 9 vs water-dragon562 | 80 | **100** | **100** | 93% | 0 |
| 8 vs Clotilde78891 | 86 | 75 | 91 | 90% | 1 |
| 7 vs Rinat2312 | 57 | — | — | 82% | 1 |
| 6 vs AaranyaRameshwaran | — | 99 | 100 | 92% | 0 |
| 5 vs sarinafaragh | — | — | — | 57% | 6 |

**Opening — no longer my weak phase.** 57% → 86% → 80% → **95%**. Game 10 is my
best opening score in the log. The old reading ("historically my weakest,
autopilot") is out of date; Leak #2 has surfaced twice in ten games and not at
all in the last one.

**Middlegame — now the phase to watch.** The most volatile number I have: 73%
and 75% in my two loosest games, 99% and 100% in my two cleanest. It tracks
one thing only — whether I ran the scan. It is not a knowledge gap.

**Endgame — consistently my strongest, by a wide margin.** 91–100%, and 100% in
each of the last two games. A genuine weapon.

**Current reading:** the opening has been fixed by attention, not study — which
is evidence the same fix works on the middlegame. That is now the priority.

## Strengths (genuine, evidence-backed)

- **Endgame technique.** 91–100% across games. Game 8: converted a large
  advantage from move 35 to checkmate on move 67 without a wobble, including
  promoting a pawn. Long conversions do not shake me.
- **Punishing opponent errors when I'm looking.** Game 9: opponent moved a
  pinned piece on move 8, I played `9.Bxd8` and won the queen instantly — the
  exact pattern I'd previously missed. Then converted +5.4 → +12.3 flawlessly.
- **Playing up.** Game 9's 93% / 0 blunders came against an opponent rated 147
  points above me. My best game is against my strongest opposition.
- **Structure.** I know my opening setup cold and reach playable middlegames.
  Game 2: reproduced the Italian setup independently, textbook.
- **Defence.** Game 2: defended accurately for 20 straight moves under pressure
  and emerged a piece up.
- **I don't tilt into resignation.** I play games out — and it wins games.
  Games 4, 8 and 10 were all won after I'd given away a winning position.

## Weaknesses (in priority order)

1. **Leak #1 — forcing moves not searched for, or searched in the wrong order.**
   Everything else is downstream of this. Verified in 6 of 9 played games. Two
   missed forced mates. See `docs/03-my-recurring-mistakes.md`.
2. **Middlegame accuracy** — my most variable phase, and now my worst.
3. **Speed in sharp positions.** Game 10's other three blunders all fell inside
   one five-move stretch. When the position gets loud I move faster, not slower.
4. **Opening autopilot** — improving markedly. No longer top-tier priority.
5. **Playing tired** — a state problem, fully within my control.

## History

- **Jan 2025:** 24-game losing streak. The "no practice" era. Behind me.
- **May 2026:** Learnt fundamentals via Duolingo. Rating ~601.
- **May–Jul 2026:** Real coaching + Lichess puzzle training. Rating 601 → 980,
  puzzles ~610 → ~1116.
