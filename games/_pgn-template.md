# The Game Entry Template

The nightly routine (`routine-prompt.md`) creates a DRAFT entry for every
rated game in `games/logs/`, with moves, link, opening and (once Lichess has
analysed it) the numbers. **My job is only the human part**, right after the
review in `training/post-game-review.md`.

---

## What I fill in on each draft

Find the entry (newest file in `games/logs/`, newest game at the top) and
replace the placeholders:

```markdown
- Tea: yes/no · Before chess: <what I was doing> · Focus (1–5): N

**Lesson — Leak #N** (or "no leak" / "Candidate A–D").

Move NN: I played `___`. Better was `___`. Eval ___ → ___ (my point of view).
One or two sentences: what search was I running when I played it?

**The ONE thing to fix:** ____________________
```

Then, in `games/game-log.md`, change that game's Leak cell from `*pending*`
or the `(auto)` label to my own label, e.g. `**#1**`, `*clean*`, `cand. A`.

---

## If I need a PGN by hand

1. Open the game on lichess.org.
2. Click **Share & export** (the tab row under the board).
3. In the **PGN** section click **Download**.
4. Save it into `games/pgn/` named `game-NN-opponentname.pgn` (zero-padded
   number, lowercase, hyphens).

---

## What to screenshot for Claude (if not using a link)

A Lichess link is best — Claude can pull everything from it. Otherwise:

1. **The summary panel** — accuracy, blunders, ACPL, phases for BOTH players,
   with my username and colour circle visible. Non-negotiable.
2. **The whole eval graph.**
3. **The move list** around each flagged mistake.
4. **The result line** (`1-0` / `0-1` and the plain-English text).
