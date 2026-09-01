# How To Save A Game As PGN + The Log Template

Screenshots work, but PGN is better: it's text, it fits in a repo, and a coach
can replay the whole game instead of the twelve moves that fit on screen.

---

## Part 1 — Export the PGN from Lichess (step by step)

1. Open the finished game on **lichess.org**.
2. Under the board, click the **Analysis board** / **Computer analysis** tab if
   it isn't already open.
3. Look for the tab row: `Computer analysis · Move times · Crosstable ·
   **Share & export**`. Click **Share & export**.
4. Scroll to the **PGN** section. There's a text box containing the whole game.
5. Click **Download** to save the `.pgn` file, or select all the text and copy it.
6. Save it into this repo at `games/pgn/`, named like:
   `game-08-clotilde78891.pgn`
   (zero-padded number, lowercase, hyphens, no spaces — so they sort correctly)
7. Tick **"Include computer analysis"** if the option is offered. That embeds
   the engine evals in the file, which is far more useful.

**Getting the game URL:** it's in the address bar, e.g.
`https://lichess.org/AbCdEfGh`. Paste it into the log entry — it lets any coach
open the full analysis directly.

---

## Part 2 — What to screenshot (if I'm not doing PGN)

Four shots, in this order:

1. **The summary panel** — accuracy, blunders, ACPL, phase scores for BOTH
   players, with my username and colour circle visible. **This one is
   non-negotiable** — it's how the colour gets confirmed.
2. **The eval graph** — the whole thing, not a crop.
3. **The move list around each flagged mistake** — enough context to see the
   column each move is in.
4. **The final result line** — `1-0` / `0-1` and the "Checkmate • X is
   victorious" text.

---

## Part 3 — Log entry template

Copy this into the TOP of `games/game-log.md` and fill it in.

```markdown
## Game N — RESULT · COLOUR vs OPPONENT (rating) · how it ended

- **Me: X% accuracy · N blunders · N mistakes · N inaccuracies · N ACPL.**
  Phases: Opening XX / Middlegame XX / Endgame XX.
- **Opponent: X% · N blunders · N mistakes · N ACPL.**
  Phases: Opening XX / Middlegame XX / Endgame XX.
- Link: https://lichess.org/XXXXXXXX
- Played: YYYY-MM-DD HH:MM SAST
- PGN: `games/pgn/game-NN-opponent.pgn`
- Eval direction: I was [White/Black], so [positive/NEGATIVE] evals are my
  advantage.
- Best/worst eval I reached: ____ / ____

**Lesson — Leak #N.**

Move NN: I played `___`. Better was `___`. Eval ___ → ___.
[One paragraph on why I played the move I did — what search was I running?]

**Secondary:** [any second error worth noting]

**Strength:** [what I did well — be specific, with move numbers]

**State:** fresh / tired / after gaming / late night

**The ONE thing to fix:** ____________________
```

---

## Part 4 — After logging

1. Update `docs/03-my-recurring-mistakes.md` if this game adds a row to a leak
   table.
2. Update the "through-line" section at the bottom of `game-log.md`.
3. Update `README.md`'s "current frontier" section if the picture changed.
4. Commit and push (`SETUP.md`, Part B).
5. **Re-upload the changed files to the Claude Project.** Easy to forget, and
   it's the step that actually affects future coaching.
