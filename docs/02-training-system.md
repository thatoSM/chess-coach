# Training System

The whole system exists to close one gap: **I find tactics when told they're
there, and miss them when nobody tells me.** These routines are how I tell
myself.

> **CONFIRM:** this file is reconstructed from how the scans are referenced in
> my other notes. Check the exact wording of Scan A and Scan B against what my
> coach actually gave me and correct anything that's off.

---

## Scan A — my move (the forcing-move search)

**Run before EVERY move. Especially before a move that looks quiet and sensible
— that is exactly when I've historically blundered.**

Ask, in this order:

1. **Checks** — every check I have. Every single one, even the silly-looking ones.
2. **Captures** — every capture I have. Especially captures that are ALSO checks.
3. **Threats** — every move that attacks something undefended or forks two things.

Only if all three come up empty do I get to think about a quiet developing move.

**Why the order matters:** my brain's default search is "what is a good move
here?" That is a *different search* from "what is the most forcing move here?"
and it reliably returns a tidy developing move. Every documented instance of
Leak #1 was a check or a capture sitting on the board.

**The test that proves it works:** when I'm shown the identical position as a
Lichess puzzle, I solve it instantly. Nothing is missing from my chess except
the instruction to look.

## Scan B — their move (the threat check)

**Run immediately after the opponent moves, before I start thinking about my
own plan.**

1. **What does their last move ATTACK?** Trace the line the piece just opened
   or the square it now hits.
2. **What does their last move DEFEND or un-defend?** Moving a piece often
   abandons something.
3. **Do they have a check or capture next move?**
4. **Was that move unusual?** If they deviated from normal play — grabbed a
   pawn, brought the queen out early, moved a piece twice — **stop the script
   immediately** and run Scan A. Unusual moves hang pieces. This is the direct
   antidote to Leak #2.

---

## Counting

Before any capture on a contested square, count:

- How many of my pieces attack the square?
- How many of their pieces defend it?
- What is the **order** of the exchange — do I end up trading a rook for a pawn
  because their defender was worth less than my attacker?

Rule of thumb: if attackers ≤ defenders, the capture usually loses material.
Count the sequence out loud in my head before playing it.

## LPDO — Loose Pieces Drop Off

Every position, both sides: **which pieces are undefended?**

Loose pieces are what make forks, pins, skewers and double attacks possible. A
tactic almost always needs a loose piece to land on. So:

- Scan the board for MY loose pieces → these are what I'm about to lose.
- Scan for THEIR loose pieces → these are where my tactic lives.

Two documented misses were free undefended pieces: `Rxf2` (a free bishop) and
`Nxe4`/`6.Nxe4` (a hung piece in the opening). LPDO would have caught both.

## The planning question (quiet positions)

When Scan A comes up genuinely empty and the position is quiet, don't just
"develop something." Ask:

> **"What is the position asking me, and what is my laziest piece?"**

Then improve the worst-placed piece. A rook doing nothing on g3 is not a plan;
a rook coming to an open file is.

> **NOTE:** this rule is good practice, but be aware it was originally written
> up from a misread game. See Leak #4 in `docs/03-my-recurring-mistakes.md` —
> I do not yet have a confirmed example of positional drift in MY moves.

---

## Daily routine

| When | What | How long |
|---|---|---|
| Start of session | Puzzles — slow, **Normal** difficulty, 60s+ per puzzle | 15–20 min |
| Then | Rated games, **while fresh** | 2–3 games max |
| After a loss | Analyse it. Name the leak. Log it. | 10 min |
| Never | Rated chess after a long gaming session | — |

> **Why Normal, not Harder:** I tested Harder and solved 14%. On Normal it's
> 74%. A 14% solve rate is not calculation training, it's guessing training —
> which is the one thing puzzle practice must not become. Never click a move I
> haven't calculated to the end.

Detail: `training/puzzle-routine.md` and `training/wellbeing-and-schedule.md`.

## The one-line version

**Checks, captures, threats — every move, especially the quiet ones.**

Keep `training/board-card.md` open in a second tab while playing.
