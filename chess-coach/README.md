# Thato's Chess Coaching Project

This repository holds the full coaching system for improving my chess. It is
designed to be uploaded to a **Claude Project** so that every new conversation
starts already knowing my playing patterns, my recurring mistakes, and the
training system I'm working through — without me having to re-explain any of it.

## Who I am (chess context)

- Lichess username: **ThatoSM**
- Format I play: **10+5 Rapid**
- Rating: **~940 rapid** (climbed from a low of ~600 in May 2026)
- Puzzle rating: **~1116** (jumped from a stale ~610 once I started training properly)
- Colour repertoire: **1.e4 as White, 1...e5 as Black**, Italian-style development
- I learnt fundamentals via Duolingo starting May 2026, then moved to real
  coaching and Lichess puzzle training.

## The single most important fact about my chess

**My puzzle rating (1116) is now HIGHER than my game rating (940).**

My tactics are not the bottleneck. I can SEE the moves — I proved it in Game 8,
where I missed `Rf2+` on move 29 and then played that exact move on move 33.
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

## The current frontier (as of Game 8 vs Clotilde78891)

Leak #1 is still the leak. In Game 8 I played 90% accuracy and outplayed my
opponent on every single metric — but my one blunder was the same old shape: a
quiet pawn move (`29...g5??`) when a check (`Rf2+`) was winning. I played that
exact check four moves later, once the opponent handed the chance back.

Endgame remains my strongest phase (91% here, clean conversion to mate on move
67). **Middlegame (75%) is now my weakest phase**, and both of my middlegame
errors in Game 8 were Leak #1 in flavour, not positional drift.

The next rating points come from one place: running Scan A before quiet moves.
