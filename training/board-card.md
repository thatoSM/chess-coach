# BOARD CARD — keep this open while playing

_Built from Stockfish analysis of games 100–147: 34 games, 120 errors of 2+ pawns._

---

## THE SWEEP — every move, no exceptions

**Two passes. Three seconds. This is LOOKING, not thinking.**

### PASS 1 — THEIR pieces (do this FIRST)
Go piece by piece across their side of the board. For each one:

> **Is it defended?**

Any piece of theirs that I attack and nothing defends → **TAKE IT.**

> Missed 11 times in 34 games. Cost: **8,499cp.** Average **772cp each** —
> the most expensive single error type I make.

### PASS 2 — MY pieces
Go piece by piece across my side. For each one:

> **Is it attacked? Is it defended?**

Attacked and undefended → deal with it before anything else.
Move it, defend it, or take something bigger.

> Missed 23 times in 34 games. Cost: **11,963cp.**

**62% of my games contain a Pass 1 or Pass 2 miss.
That is six pawns per game given away for free.**

---

## THEN the forcing scan

0. **MATE** — is there a mate? in one? in two?
1. **CHECKS** — every check I have. Does any of them mate?
2. **CAPTURES** — every capture I have.
3. **THREATS** — anything undefended? any fork?

> Missed checks: 20 instances, **13,042cp**.
> Biggest: G107 m14 `Bxf6+` (−2635), G104 m23 `Qxd3+` (−1678).

---

## AFTER THEY MOVE — one question first

> **What does their move ATTACK?**

Trace the line the piece just opened. Then run THE SWEEP.

---

## SAY IT OUT LOUD

Silent thinking degrades when I'm tired. Speech doesn't.

**"Their loose pieces. My loose pieces. Mate, checks, captures."**

Four seconds. Every move. Especially when the position looks quiet,
and **especially when I'm already winning.**

---

## HARD RULES — no thinking required

- Piece attacked → **count its safe squares BEFORE reacting.**
  Two or more safe squares = not a crisis. Carry on with the scan.
- Bishop on b5/c4 attacked by a pawn → **taking the knight is the DEFAULT.**
  Retreating is the move I must justify out loud. "Bishops are better"
  is not a justification.
- As Black facing `Bc4` with pawns on b7/a7 → **`b5`.**
  If he takes, look for `Nd4` hitting queen and bishop.
- Recapture near my king with a **PIECE**, not a pawn.
- Endgame with few pieces → **the mate check matters MOST here**, not least.
- Before any retreat → **can I trade this piece instead?**
- Before any trade → **what is their piece defending?**

---

## WAYWARD QUEEN — `1.e4 e5 2.Qh5`

Three losses to this. Engine-verified answer:

```
2... Nc6   3. Bc4  g6!   (not Qe7 — it blocks my bishop)
4. Qf3 Nf6  and I'm already better
```

Any time his bishop sits on c4 → **`b5`.**
If `Bxb5??` → **`Nd4!`** forks the queen and hits the loose bishop. −3.46.

---

## WHAT I AM NOT MISSING

Stockfish says only 20% of my big errors involved a fork,
and 59% had a **quiet** best move.

**I am not losing games to missed forks and pins.
I am losing them to pieces standing undefended in plain sight.**

Stop training tactics I can already solve. Run the sweep.
