# Player Profile

A factual snapshot. Live numbers are in `STATS.md` (regenerated nightly);
this file holds the interpretation. Numbers below were pulled from the
Lichess API on 20 September 2026.

## Identity

- **Lichess:** ThatoSM — South Africa, account since Nov 2024, first rated
  game Jan 2025.
- **Format:** 10+5 Rapid.
- **Repertoire:** 1.e4 Italian as White. As Black, the Caro-Kann vs 1.e4 and
  `1...d5` / Slav vs 1.d4 (switched from `1...e5` in September 2026). See
  `docs/04-openings.md`.
- **Goal:** 1800+ rapid. No heavy opening study until ~1800.

## Ratings

| Metric | Value | Note |
|---|---|---|
| **Rapid** | **1186** | All-time high, set 20 Sep 2026. RD 45. Better than ~30% of rapid players. |
| Puzzles | 1518 | ~330 above rapid — fairly typical on Lichess (`docs/08`) |
| Classical | 1155? | Provisional, 17 games |
| Blitz | 1025? | Provisional, 14 games |

## Arc

| Point | Rapid |
|---|---|
| First 54 games, 15–24 Jan 2025 | 1500 provisional → 795 (11–42–1) |
| Gap until May 2026 | — |
| Low, 25 May 2026 | 601 |
| Early-August peak, after a 12-game win streak | 1117 |
| Now | 1186 |

## Results by colour (rated rapid, 20 Jul – 20 Sep 2026)

| Colour | Games | W–L–D | Score |
|---|---|---|---|
| **White** | 381 | 210–155–16 | **57.2%** |
| Black | 405 | 187–201–17 | 48.3% |

White is my stronger colour, and the gap held in September (58.2% vs 45.3%).
The old "Black 70.8%" figure came from 47 games and is dead. Black's weakness
is part of why the Black repertoire changed; whether the Caro-Kann / Slav
helps needs 30+ games before judging (`scripts/opening-results.py`).

## Phases

- **Middlegame is my worst phase** — 41% of all damage, and it has been
  stable across the whole logged period.
- **Opening is no longer weak.** It was my worst phase in the first ten games.
- **Endgame conversion is average, not a collapse** — 77% from +2.0, the same
  as the middlegame. Candidate B in `docs/03` tracks the exceptions.

## The key insight

**I lose games in positions I'm winning.** 665 of my last 786 rated rapid
games reached +1.00 or better. In 58% of those I then missed a mate, check or
capture that kept the win (`docs/03`, Leak #1). My error rate per move at
+1.5 to +4 is 3.4× my rate in level positions.

## Strengths (evidence-backed)

- **Out-playing opponents on average.** More accurate than my opponent in 63
  of 94 analysed games.
- **Level positions** — my lowest error rate and fastest thinking.
- **The clock.** Won on time 36 times, lost on time 5.
- **Resilience.** I play games out; I've won from ~-10 by grinding to mate on
  move 67, and many wins came after giving a winning position away.
- **I climb.** 601 → 1186 in four months.

## Weaknesses (priority order)

1. **Leak #1** — forcing moves missed in winning positions, or the wrong
   forcing move played. Everything else is downstream.
2. **Big drops with a quiet best move** (Candidate D) — probably hanging
   pieces. Unreviewed.
3. **Capturing without checking the reply** (Candidate A).
4. **Middlegame accuracy** — my most variable phase.
