# Thato's Chess Coaching Project

This repository holds the full coaching system for improving my chess. It is
designed to be uploaded to a **Claude Project** so that every new conversation
starts already knowing my playing patterns, my recurring mistakes, and the
training system I'm working through — without me having to re-explain any of it.

_Numbers last verified against my Lichess profile on **2 August 2026**._

## Who I am (chess context)

- Lichess username: **ThatoSM** (South Africa, member since 24 Nov 2024)
- Format I play: **10+5 Rapid**
- Rating: **1026 rapid** — an all-time high, set 2 Aug 2026. Low of **601** on
  25 May 2026. That is **+425 in roughly ten weeks.**
- Puzzle rating: **~1491** (was a stale ~610 before I trained properly)
- Colour repertoire: **1.e4 as White, 1...e5 as Black**, Italian-style development
- I learnt fundamentals via Duolingo starting May 2026, then moved to real
  coaching and Lichess puzzle training.

## The single most important fact about my chess

**My puzzle rating (~1491) is now roughly 465 points HIGHER than my game
rating (1026).**

That gap has **widened**, not closed — it was ~135 points at Game 10. My tactics
are not the bottleneck and never were. I can SEE the moves. I've now proved it
**four times**, every one verified against the PGN:

- **Game 5:** missed `Nxf3+` on move 11, played it on move 12.
- **Game 8:** missed `Rf2+` on move 29, played it on move 33.
- **Game 34:** missed `Ra8#` — mate in one — on move 28, played `Ra8+` on move 29.
- **Game 42:** missed `Nxe5` on move 10, played it on move 11 and resigned.

The move was always in my chess. The **search** was missing from my routine.

In a puzzle, someone tells me "there's something here." In a game, nobody does.
So I have to tell myself, every move. That is what Scan A is for
(`docs/02-training-system.md`).

## How to use this project (for Claude)

When I paste a game (screenshot or PGN) and ask for analysis:

1. **Read `docs/06-reading-an-analysis.md` FIRST.** Confirm which colour I
   played and which way the eval sign runs BEFORE saying anything about the
   game. This has been got wrong twice. It is the most common failure mode.
2. Read `docs/03-my-recurring-mistakes.md` and check whether the new game shows
   the **same leak again** (it usually does). Name it explicitly by number.
3. Read the accuracy / blunder / phase numbers FIRST, before commenting on
   individual moves — the phase scores tell the real story.
4. Distinguish **"lost a blunder-brawl"** (jagged eval graph) from **"got
   outplayed"** (smooth decline). They need different feedback.
5. Be honest. Don't just congratulate wins — my wins often contain the same
   blunders as my losses, they just went unpunished. Equally, don't invent a
   struggle that didn't happen. Tell me what the numbers actually say.
6. End by telling me the ONE thing to fix, not five.

Full detail on how I want to be coached: `docs/05-coaching-principles.md`.

## File index

| File | What it holds |
|---|---|
| `SETUP.md` | Build the Claude Project + create the GitHub repo, step by step |
| `routine-prompt.md` | The nightly sync/backfill automation prompt |
| `docs/01-player-profile.md` | Full snapshot of where my chess is, with numbers |
| `docs/02-training-system.md` | The scans, counting, LPDO, the planning question |
| `docs/03-my-recurring-mistakes.md` | **The core file** — every leak, with examples |
| `docs/04-openings.md` | My White and Black repertoire + how to meet gambits |
| `docs/05-coaching-principles.md` | How I want to be coached |
| `docs/06-reading-an-analysis.md` | How to read a Lichess analysis without misreading it |
| `games/game-log.md` | Scannable index — one row per game, newest first |
| `games/logs/` | Full entries, 40 games per file |
| `games/_pgn-template.md` | How to export a PGN + a template to fill in |
| `games/pgn/` | Raw `.pgn` exports, one file per game |
| `training/puzzle-routine.md` | Exactly how I do Lichess puzzles |
| `training/board-card.md` | The one-screen checklist I keep open WHILE playing |
| `training/wellbeing-and-schedule.md` | Chess-first rule, gaming drain, day structure |

## The current frontier (as of 2 Aug 2026, Game 48 logged)

**I am on a 10-game winning streak — my longest ever — and at my all-time high
rating, both as of today.** For contrast, my longest losing streak is 24 games
(Jan 2025). The trajectory is real.

**And the leak is still live.** The six analysed wins in the streak contain the
same errors as my losses, verified against the PGNs:

- **Game 44 (WIN):** `Qf4+` available on moves 25, 26 AND 27, each time from a
  forced mate in 2. Missed all three. Then missed **`Qg3#` — mate in one — on
  move 30.** Won anyway because the opponent blundered nine times to my seven.
- **Game 47 (WIN):** 2 blunders, 0 mistakes, 0 inaccuracies — statistically my
  cleanest game in the set. Both blunders were the same missed capture,
  `Nxe3`, two moves running, each throwing away a winning position.
- **Game 48 (WIN):** missed `Qg4+` on move 19 (+0.59 → +8.49), played it on
  move 22.

**A low blunder count is not evidence the leak is gone.** Game 47 proves it.

**Colour split (47 played games):** Black **17–7–0 (70.8%)**, White
**11–10–2 (52.2%)**. Black is decisively my stronger colour.

**As White, the Italian is not the problem — not getting to play it is.**
When Black answers `1...e5`: 8–5–1 (61%). When Black plays anything else:
**2–5–1 (31%)**. The two most recent White losses (41, 42) were both
Scandinavians. Sample is small — collect more before changing anything.

**No repertoire changes.** See `docs/05-coaching-principles.md` principle 10.

The next rating points come from one place: running Scan A, in the right order —
**mate → checks → captures** — before every move, especially the quiet-looking
ones and especially when I'm already winning.

## A standing warning

Three claims in this repo turned out to be **the opponent's moves recorded as
mine** — the retracted Leak #4, and the unverified `Qe2`/`Rxf2` row. Before
repeating any claim about a specific move, check it against the PGN in
`games/pgn/`. Only cite rows from the VERIFIED table in
`docs/03-my-recurring-mistakes.md`.
