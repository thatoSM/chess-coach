# How To Read A Lichess Analysis Without Misreading It

**Read this before analysing any game I paste. Every time. No exceptions.**

Game 8 was misread twice — first as a loss, then as a "heroic comeback from a
dead-lost position." Both wrong, both from the same root cause: not establishing
which colour I was before reading the eval numbers. This file exists so it
doesn't happen a third time.

---

## The eval sign rule

Lichess evaluations are **always from White's point of view.**

| Eval | Meaning |
|---|---|
| `+3.0` | **White** is winning by about three pawns |
| `-3.0` | **Black** is winning by about three pawns |
| `#3` | **White** mates in 3 |
| `#-3` | **Black** mates in 3 |

So:

- **When I play White:** positive = good for me.
- **When I play Black:** **negative = good for me.**

**A big negative number in one of my Black games is me WINNING, not losing.**
This is the exact mistake that produced a fictional comeback story in my game
log.

---

## The mandatory checklist

Work through these in order before writing a single word of analysis:

1. **Which colour did I play?**
   On the Lichess analysis panel, my username `ThatoSM` appears next to either
   a white circle (○ = White) or a black circle (● = Black). Find it. Say it
   out loud.

2. **What does the result line say?**
   At the bottom of the move list: `1-0` (White won), `0-1` (Black won), or
   `1/2-1/2` (draw), plus a plain-English line like "Checkmate • Black is
   victorious." **Trust this line over any inference from the eval graph.**

3. **Now, and only now, set the eval direction.**
   "I was Black, so negative evals are my advantage."

4. **Which column are the moves in?**
   In the move list, the left column is White's moves and the right column is
   Black's. A move in the wrong column belongs to my opponent. Engine
   suggestions ("Rg3 was best") also belong to whoever was to move — check
   which side that was before attributing it to me.

5. **Whose mistake is flagged?**
   "Blunder. Bd1 was best." attaches to the move directly above it. Check the
   column.

6. **Read the summary panel numbers for BOTH players**, then compare.

Only after all six do I get to talk about the chess.

---

## The specific traps

### Trap 1 — the eval graph shape
The graph is shaded from White's perspective too. A line plunging downward in
one of my Black games means I'm taking over. Don't read "line goes down" as
"things went badly for Thato."

### Trap 2 — attributing the opponent's moves to me
As Black my rooks live on the 8th rank; as White they live on the 1st. If the
"drifting" moves being blamed on me are `Rg3`, `Re3`, `Rg1` and I was Black,
those are White's rooks. This is precisely what went wrong in the first Game 8
write-up: an entire new "leak" was invented out of the opponent's play.

**Quick sanity check:** does the move even make sense for my colour?

### Trap 3 — a big eval swing that isn't mine
A mistake flag sitting between two of my moves might belong to the opponent.
Check the column before adding a row to the Leak #1 table.

### Trap 4 — partial screenshots
If I only send moves 26 onward, **say so**, and don't make claims about moves
1–25. State clearly what the analysis does and doesn't cover.

---

## What "good" looks like

> "You played Black (● next to ThatoSM). Result line says 0-1, checkmate,
> Black is victorious — so you won. That means negative evals are your
> advantage throughout. Your best moment was about -11; your worst was +0.1
> after move 29. You were never worse than equal in this game."

That's the opening of a correct analysis. Colour, result, sign direction, range
— then the chess.
