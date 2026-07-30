# Thato's Chess Coaching Project

This repository holds the full coaching system for improving my chess. It is
designed to be uploaded to a **Claude Project** so that every new conversation
starts already knowing my playing patterns, my recurring mistakes, and the
training system I'm working through — without me having to re-explain any of it.

## Who I am (chess context)

- Lichess username: **ThatoSM**
- Format I play: **10+5 Rapid**
- Rating: **980 rapid** (climbed from a low of ~600 in May 2026)
- Puzzle rating: **~1116** (jumped from a stale ~610 once I started training properly)
- Colour repertoire: **1.e4 as White, 1...e5 as Black**, Italian-style development
- I learnt fundamentals via Duolingo starting May 2026, then moved to real
  coaching and Lichess puzzle training.

## The single most important fact about my chess

**My puzzle rating (1116) is now HIGHER than my game rating (980).**

My tactics are not the bottleneck. I can SEE the moves — and I've now proved it
TWICE, both verified against the PGN:

- **Game 5:** missed `Nxf3+` on move 11, played it on move 12.
- **Game 8:** missed `Rf2+` on move 29, played it on move 33.

The move was always in my chess. The **search** was missing from my routine.

The gap between puzzle rating and game rating is the whole diagnosis: in a
puzzle, someone tells me "there's something here." In a game, nobody does. So
I have to tell myself, every move. That is what Scan A is for
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
| `docs/01-player-profile.md` | Full snapshot of where my chess is, with numbers |
| `docs/02-training-system.md` | The scans, counting, LPDO, the planning question |
| `docs/03-my-recurring-mistakes.md` | **The core file** — every leak, with examples |
| `docs/04-openings.md` | My White and Black repertoire + how to meet gambits |
| `docs/05-coaching-principles.md` | How I want to be coached |
| `docs/06-reading-an-analysis.md` | How to read a Lichess analysis without misreading it |
| `games/game-log.md` | Every analysed game, with the lesson from each |
| `games/_pgn-template.md` | How to export a PGN + a template to fill in |
| `games/pgn/` | Raw `.pgn` exports, one file per game |
| `training/puzzle-routine.md` | Exactly how I do Lichess puzzles |
| `training/board-card.md` | The one-screen checklist I keep open WHILE playing |
| `training/wellbeing-and-schedule.md` | Chess-first rule, gaming drain, day structure |

## The current frontier (as of Game 10 vs esteesAmin)

**Leak #1 is still the leak, but it has changed shape.** In Game 10 I found a
forcing move — I captured a rook — while `29...Qxg2#` was mate in one. That's
not a failure to search; it's searching in the wrong ORDER. It's also the second
forced mate I've missed.

> **Mate → checks → captures. In that order, every time.**

**The opening is no longer my weak phase.** 57% → 86% → 80% → **95%** across
games 7 to 10. Game 10 is my best opening score in the log. That's the first
leak in this repo to visibly close, and it closed through attention, not study —
which is the best evidence I have that the same fix works elsewhere.

**Middlegame is now the phase to watch** (73%, 75% in my two loosest games; 99%,
100% in my two cleanest). It tracks one thing: whether I ran the scan.

**Endgame remains a genuine weapon** — 91–100%, and 100% in each of the last two
games.

**Best game so far:** Game 9. 93% accuracy, zero blunders, 15 ACPL, 100% in both
middlegame and endgame, against an opponent 147 points above me.

The next rating points come from one place: running Scan A, in the right order,
before every move — especially the quiet-looking ones.

## A standing warning

Three claims in this repo turned out to be **the opponent's moves recorded as
mine** — the retracted Leak #4, and the unverified `Qe2`/`Rxf2` row. Before
repeating any claim about a specific move, check it against the PGN in
`games/pgn/`. Only cite rows from the VERIFIED table in
`docs/03-my-recurring-mistakes.md`.
