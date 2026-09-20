# Thato's Chess Coaching Project

The full coaching system for my chess (Lichess: **ThatoSM**, 10+5 rapid).
It's packed into `repomix-output.xml` and uploaded to the **Chess** Claude
Project, so every chat starts knowing my games, my leaks and how I want to be
coached. Current numbers: [STATS.md](STATS.md). Goal: **1800+**.

## The single most important fact about my chess

**I lose games from winning positions.** Of my last 786 rated rapid games,
665 reached +1.00 or better — and in **58%** of those I then missed a mate,
check or capture that kept the win. It's the same in wins (56%) and losses
(60%): I win the ones where the opponent gives it back.

The move is almost never missing from my chess. I've played the exact move I
missed a move or two later, again and again. **The search is missing from my
routine.** Details: `docs/03-my-recurring-mistakes.md`.

The fix in use: **when I'm winning — mate, every check, every capture — out
loud, before I touch a piece** (`training/board-card.md`).

## How to use this project (for Claude)

When I paste a game (screenshot, PGN or Lichess link) and ask for analysis:

1. **Read `docs/06-reading-an-analysis.md` FIRST.** Confirm my colour and
   which way the eval sign runs before saying anything about the game.
2. Read the accuracy / blunder / ACPL / phase numbers for **both players**
   before commenting on individual moves.
3. Classify the game against `docs/03-my-recurring-mistakes.md` and **name
   the leak by number** (it's usually #1). Candidates stay unnumbered.
4. Blunder-brawl (jagged eval) or outplayed (smooth decline)? Different
   feedback.
5. Be honest in both directions — no praise for a win full of the usual
   blunders, no invented struggle.
6. If I raise a theory about sleep, food, gaming, time of day etc., check
   `docs/08-what-the-data-says.md` first — it's probably been tested.
7. End with the **ONE** thing to fix.

Full detail: `docs/05-coaching-principles.md`.

## File index

| File | What it holds |
|---|---|
| `SETUP.md` | Project setup, the daily loop, committing, running the scripts |
| `routine-prompt.md` | The nightly Lichess sync automation |
| `STATS.md` | Auto-generated ratings and counts — never edit by hand |
| `docs/01-player-profile.md` | Where my chess is, with numbers |
| `docs/02-training-system.md` | How the pieces of training fit together, and what was retired |
| `docs/03-my-recurring-mistakes.md` | **The core file** — every leak and candidate, with evidence |
| `docs/04-openings.md` | Repertoire: Italian as White, Caro-Kann / Slav as Black |
| `docs/05-coaching-principles.md` | How I want to be coached |
| `docs/06-reading-an-analysis.md` | Reading Lichess analysis (screen and API) without misreading it |
| `docs/07-principles-reference.md` | General chess principles — reference, NOT for mid-game |
| `docs/08-what-the-data-says.md` | Every hypothesis tested and every fix tried, with results |
| `training/board-card.md` | The triggers I keep open WHILE playing |
| `training/puzzle-routine.md` | How I do puzzles |
| `training/drill-trainer.md` | My drill trainer artifact and the rules for editing it |
| `training/post-game-review.md` | The review I do after every game |
| `training/wellbeing-and-schedule.md` | The rules I keep, the ones retired, the tea experiment |
| `games/game-log.md` | One row per game, newest first — **the Leak column is the point** |
| `games/logs/` | Full game entries, 40 per file |
| `games/pgn/` | Raw `.pgn` exports |
| `games/leak-scan/` | Auto Leak #1 classification and evidence for every rated rapid game |
| `games/_pgn-template.md` | How to export a PGN + the entry template |
| `scripts/leak-scan.py` | Re-runs the Leak #1 scan (needs Stockfish) |
| `scripts/apply-leak-column.py` | Fills `*pending*` Leak cells from the scan |
| `scripts/opening-results.py` | Results by opening and colour vs rating expectation |

## A standing warning

Three claims in this repo's history were **the opponent's moves recorded as
mine** (Leak #4 and two table rows, now removed). Before repeating any claim
about a specific move, check it against the game with a legal-move generator.
