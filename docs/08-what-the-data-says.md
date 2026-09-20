# What The Data Says — tested claims and tried fixes

One ledger for every hypothesis I've tested and every intervention I've tried,
with the result. **Read this before proposing a new theory about why I play
well or badly** — it has probably been tested already.

Rules for this file:

- A row records what was measured, on how many games, and the result. No
  row without a sample size.
- "No signal" means the data didn't support the claim. It doesn't mean the
  claim is impossible — it means acting on it isn't justified.
- Numbers come from chat analyses in the Chess Claude Project using the
  Lichess API, python-chess and Stockfish. The date is when the test ran.

---

## 1. The core diagnosis

| Finding | Evidence |
|---|---|
| **Leak #1 is the dominant lever.** | Auto-scan of every rated rapid game since July 2026 — see `docs/03`, "The numbers" section, and `games/leak-scan/`. |
| Damage concentrates in **winning** positions. | Error rate per move is **3.4×** higher at +1.5 to +4 than in level positions (138 games, Aug 12). 55% of large middlegame errors come from positions already better than +1.5 (194 games, Aug 25). |
| Wins are not clean. | Two-thirds of wins contain a 300cp+ error; 40% contain a 500cp+ one (194 games, Aug 25). Wins account for 45.8% of all centipawns thrown away (211 games, Aug 25). |
| The size of the **single worst move** decides games. | Median worst move 326cp in wins vs 793cp in losses (40 games, Aug 13); 302 vs 664 (108 games, Aug 12). ACPL lower than the opponent's predicted the result in 15 of 15 games (Aug 9). |
| I usually out-play my opponent on average. | More accurate than the opponent in 63 of 94 analysed games, by 12 ACPL on average (Aug 7). Losses come from one catastrophic move inside a better-played game. |
| **Level positions are my strongest bucket.** | Lowest damage rate and fastest thinking (138 games, Aug 12). The "I don't know what to do in quiet positions" hypothesis was not supported. |
| Middlegame is the worst phase — and always has been. | 99.5 ACPL, 41% of all damage. Stable across the whole logged period; the "it's got worse recently" feeling failed a permutation test (194 games, Aug 25). |
| Endgame is not where I collapse. | Entering an endgame at +2.0 or better converts 77%, the same as the middlegame's 76% (108 games, Aug 12). Endgame cp/move improved 73.5 → 60.6 (Aug 25). But see the endgame-conversion candidate in `docs/03`. |
| Leak #1 predates any chess study. | In my first 54 rapid games (15–24 Jan 2025, record 11–42–1), missed mates and forcing moves were already there (Sep 11). |
| Lichess accuracy hides Leak #1. | 98–99% accuracy games have contained missed forced mates; accuracy barely drops when the position was already winning (Aug 10, Sep 5, Sep 7). |

## 2. The puzzle-to-rapid gap

My puzzle rating runs ~320–400 points above my rapid rating (1518 vs 1186
now). **That size of gap is fairly typical on Lichess**, so it is not unique
proof of anything on its own (Aug 7). What IS specific to me is the
one-move-late pattern in `docs/03`: I play the move I missed a move or two
later. That shows the move was in my chess and the search was not.

## 3. State hypotheses — all tested, none showed a signal

| Hypothesis | Test | Result |
|---|---|---|
| Fatigue / time of day | Score and accuracy vs start time (Aug 15) | No signal (p = 0.84 score, p = 0.47 accuracy). |
| Time of day, full split | 436 games by SAST hour (Sep 19) | Morning 54% vs evening 47%, but adjacent hours swing 34% ↔ 61%. Noise. |
| Late-night rapid | 191 timestamped games (Aug 10) | Zero games started after 23:00; only nine 21:00–22:59. Claim unsupported. |
| Sleep | Session-by-session (Sep 3, Aug 7) | The worse-sleep session produced the better accuracy. 8 h sleep once came before worse play than 6 h. |
| Diet | Last three days vs baseline (Aug 7) | Those were my best days by ~18 ACPL. No diet effect visible. |
| League of Legends before chess | Aug 7 | No usable signal; League timestamps were never joined to games. |
| Device (phone vs PC) | Sep 4 | **Untestable** — no device field exists in any logged game. |
| Room lighting | Sep 7 | Clock time is not a proxy for lighting in my room; not testable from game data. |
| Bathroom breaks | Sep 7 | One game can't test it. Plausible mechanism (removing a distraction), no data. |
| Repeat opponents | 400 games (Aug 18) | Accuracy 0.7 points *lower* vs repeat opponents, p = 0.58. No effect. |
| Tilt after losses | Aug 7 | Error rate after two straight losses 0.117 vs 0.113 otherwise. No tilt effect. |
| Session length | Aug 7 | Games 13+ of a session were my **best** band (63% score). |

**Why these keep failing:** 75–85% of my performance variance happens
**within a single day**, not between days (Aug 7, Aug 13). My best and worst
games are hours apart, same sleep, same food, same device. Anything that
changes once per day can explain at most the remaining ~20%.

**Standing pattern:** new state hypotheses tend to appear right after a
concrete tactical fix is prescribed. They feel productive and defer the harder
work. When one appears, check this table first.

### Open experiment — tea

I'm logging tea (1 cup of Trinco, ~1 hour before) yes/no per game. **Pre-set
rule:** compare after 20+ games each side, using score vs rating expectation
and my worst-move size, not just win rate. Given the within-day variance above,
expect no clear result; a difference under ~10 percentage points on 20 games
each is noise.

## 4. Interventions — what was tried and what happened

| Intervention | Result | Status |
|---|---|---|
| Scan A on **every** move (checks, captures, threats) | Couldn't be sustained at ~15 s per move | Replaced by narrow triggers |
| Board card "Sweep" (Pass 1 / Pass 2 on every move) | 190 games after introduction: ACPL, worst-move median and middlegame cp/move all **worsened**. The rating climb in that period was not attributable to it (Aug 25) | **Retired** |
| Stop after two losses | Tilt not measurable (see above) | **Retired** |
| Volume cap (3 games/day) | Games 13+ were my best | **Retired** |
| Puzzles on Harder | 14% solve rate = guessing | Switched to **Normal** (74%) |
| Narrow trigger: after winning material / at +3 or better, name every check, then every capture | Matches where the errors concentrate | **Active** — see `training/board-card.md` |
| Notepad for "found it, lost it" | 42 cases in 150 games of blundering the best move then playing it within 3 moves; the move before a blunder takes 8.9 s median vs 6.2 s (Sep 7) | **Active** — re-measure after 40 games against the 10.1% baseline |
| Nothing on screen but the board | Moves over 20 s had 18–22% error rate vs 7–8% under 20 s, and long thinks weren't following opponent threats — distraction, not calculation (Aug 18) | **Active** |
| Recapture rule | `13.Qxd4` instead of `Nxd4` allowed a queen fork (Sep 3) | **Active** — name what their most active piece hits after each recapture |

## 5. Colour and opening results

| Finding | Evidence |
|---|---|
| **White is my stronger colour.** | 56.8% as White, +5.5 pp vs Elo expectation (427 games, Sep 11). Logged: White 56.7%, Black 49.3% (445 games). The old "Black 70.8%" claim came from 47 games and is dead. |
| Non-`1...e5` replies as White are not a crisis. | Gap is ~6.5 points on n = 82, not the old 30-point gap from n = 8 (Aug 31). |
| As White vs the Sicilian | 5–3–1 overall; Bowdler `2.Bc4` 1–2–1, `2.d4` 3–0 (Sep 16). Tiny samples. |
| As Black vs the Queen's Gambit (pre-Slav) | 5–3; all three losses came after an early `...dxc4` (Sep 16). Tiny sample; the Slav's `...dxc4` after `...c6` and `a4` is a different, main-line structure. |
| Clock is not my problem. | Won on time 36 times, lost on time 5 (Aug 31). |
| No two games share even 8 opening moves. | 427 games (Sep 11). Opening-sequence statistics at depth are impossible; only opening families can be compared. |
| Caro-Kann / Slav | Too new to judge. Re-run `scripts/opening-results.py` after 30+ games. |

## 6. Rating arc

| Point | Rapid |
|---|---|
| First rated games, Jan 2025 | 1500 provisional → 795 |
| Low, 25 May 2026 | 601 |
| Early-August peak, after a 12-game win streak | 1117 |
| All-time high, 20 Sep 2026 | **1186** |

Current numbers: `STATS.md` (regenerated nightly).
