# Player Profile

A factual snapshot. Update the numbers whenever they move meaningfully.

## Identity

- **Lichess:** ThatoSM
- **Format:** 10+5 Rapid (10 minutes each, +5 seconds per move)
- **Colours:** 1.e4 as White, 1...e5 as Black. Italian-style development.

## Ratings

| Metric | Value | Note |
|---|---|---|
| Rapid rating | **~940** | Low of ~601 in May 2026, 947 in July 2026 |
| Puzzle rating | **~1116** | Was a stale ~610 before I trained properly |
| Games played | ~537 | |
| Puzzles solved (original count) | 31 | **This was the whole diagnosis** |

> **CONFIRM:** update the games/puzzles counts — these are from the Game 1
> profile snapshot and are now out of date.

## The key insight

**Puzzle rating (1116) > game rating (940).**

I am rated ~180 points stronger at finding tactics when someone tells me a
tactic exists than I am at finding them unprompted. That gap IS my rating
ceiling. Closing it doesn't require learning anything new — it requires a
routine (Scan A, see `docs/02-training-system.md`).

Game 8 is the cleanest proof of this ever recorded: I missed `Rf2+` on move 29,
then played `Rf2+` on move 33. Identical move, identical idea, four moves
apart. Nothing was learned in between. I simply searched the second time.

## Phase scores (where my accuracy lives)

Historical pattern across games 1–7:

| Phase | Typical | Verdict |
|---|---|---|
| Opening | 75–86% | Historically my **weakest** — autopilot (Leak #2) |
| Middlegame | 75–99% | Highly variable — depends entirely on whether I scan |
| Endgame | **91–100%** | Consistently my **strongest**, by a wide margin |

**Game 8 changed this picture.** Opening 86%, Middlegame **75%**, Endgame 91%.
For the first time the middlegame was the worst phase, and both errors in it
were missed forcing moves.

**Current reading:** opening autopilot is improving. Middlegame scanning is now
the priority.

## Strengths (genuine, evidence-backed)

- **Endgame technique.** 91–100% across games. In Game 8 I converted a large
  advantage from move 35 to checkmate on move 67 without a wobble, including
  promoting a pawn. Long conversions do not shake me.
- **Structure.** I know my opening setup cold and reach playable middlegames.
  Game 2 I reproduced the Italian setup independently and it was textbook.
- **Defence.** Game 2: defended accurately for 20 straight moves under pressure
  and emerged a piece up.
- **I don't tilt into resignation.** I play games out.

## Weaknesses (in priority order)

1. **Leak #1 — quiet move instead of a forcing move.** Everything else is
   downstream of this. See `docs/03-my-recurring-mistakes.md`.
2. **Middlegame accuracy** — currently my worst phase.
3. **Opening autopilot** — improving, not solved.
4. **Playing tired** — a state problem, fully within my control.

## History

- **Jan 2025:** 24-game losing streak. The "no practice" era. Behind me.
- **May 2026:** Learnt fundamentals via Duolingo. Rating ~601.
- **May–Jul 2026:** Real coaching + Lichess puzzle training. Rating 601 → 947,
  puzzles ~610 → ~1116.
