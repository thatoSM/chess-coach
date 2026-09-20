# Post-Game Review

I review **every game right after playing it.** One lesson per game. My own
mistakes first.

I use the **local browser Stockfish** on the Lichess analysis board, because
Lichess's server analysis has a daily limit. The nightly routine and
`scripts/leak-scan.py` both cope with games that have no server analysis.

---

## The review, step by step

1. When the game ends, click **Analysis board** (under the board on
   lichess.org, or the menu button → Analysis board on mobile).
2. Turn on the local engine: click the **engine toggle** (the switch next to
   the evaluation number at the top of the move list). The engine runs on my
   own computer — no daily limit.
3. **Confirm my colour and the eval direction first**
   (`docs/06-reading-an-analysis.md`): as Black, negative = good for me.
4. Step through the game with the **→** arrow key. Watch the eval number.
5. Stop at every move of **mine** where the eval swung by about 1.5 or more
   against me. For each one:
   - What did I play?
   - What does the engine's top line (the first line under the eval) start
     with?
   - Was that a **mate, a check or a capture**? If yes, and I was winning,
     it's **Leak #1**.
6. Only after my own mistakes, look at my opponent's biggest one — did I
   punish it?
7. Pick **one lesson.** Not three.
8. If the lesson is a position worth drilling, write it as a Lessons card in
   the trainer (`training/drill-trainer.md`) or ask Claude to add it to Key
   squares.

## Log it

In the game's entry in `games/logs/` (the nightly routine creates the
draft), fill in:

- The lesson, with move number, what I played, what was better, eval swing.
- Leak number (or "none" / candidate letter).
- Opening, tea yes/no, what I did before chess, focus 1–5.
- The ONE thing to fix.

Then replace the `(auto)` label in `games/game-log.md` with my own label if
I disagree with it.

## Every ~50 games

Re-run the Leak #1 scan and add a row to the trend table in `docs/03`
(`SETUP.md`, Part D).
