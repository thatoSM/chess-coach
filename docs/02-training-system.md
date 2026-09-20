# Training System

The whole system exists to close one gap: **I find forcing moves when told
they're there, and miss them when nobody tells me** — especially when I'm
already winning (`docs/03`, Leak #1).

---

## What changed, and why

The original system was **Scan A** (checks, captures, threats before every
move) and **Scan B** (what does their move attack?). Later came the board
card "Sweep" (their loose pieces, my loose pieces, every move).

The data killed the every-move versions. At ~15 seconds per move, a full scan
on every move isn't sustainable, and 190 games after the Sweep was introduced
my move quality hadn't improved (`docs/08-what-the-data-says.md`). My errors
concentrate in one situation — **winning positions** — so the scan now fires
on **triggers**, not on every move.

The names "Scan A" and "Scan B" still appear in old game entries. Today they
map to:

| Old name | Now |
|---|---|
| Scan A (my move) | **Trigger 1** on the board card: when winning, mate → every check → every capture |
| Scan B (their move) | **Trigger 3**: "what does their move attack?" |

---

## The active routine

| Piece | What | Where |
|---|---|---|
| In the game | Four triggers + hard rules | `training/board-card.md` |
| Before playing | Board only on screen; notepad ready | `training/board-card.md` |
| Puzzles | Normal difficulty, slow, mate-first themes | `training/puzzle-routine.md` |
| Openings | Drill the Caro-Kann / Slav lines | `training/drill-trainer.md` |
| After every game | Local-engine review, one lesson, log it | `training/post-game-review.md` |
| Every ~50 games | Re-run the Leak #1 scan, update the trend | `SETUP.md` Part D |

---

## Tools that still hold (use when there's time)

**Counting.** Before a capture on a contested square: how many attackers,
how many defenders, and in what order do the pieces trade? If attackers ≤
defenders, the capture usually loses material.

**Loose pieces (LPDO).** Which pieces — mine and theirs — are undefended?
Tactics land on loose pieces. Mine are what I'm about to lose; theirs are
where my tactic lives.

**The planning question (quiet positions only).** When nothing forcing is on
the board: *"What is the position asking me, and what is my laziest piece?"*
Improve that piece by one move.

---

## Study order when I'm not playing

Set by me, in this order. Nothing moves onto the board card until the gate in
`docs/07-principles-reference.md` is met.

1. **Endgames** — king activity, opposition, rule of the square, pawn
   endgames (also the third puzzle theme).
2. **Puzzles** with the slow method.
3. **Prophylaxis** — what does my opponent want to do next?
4. **Pawn structure** — which pawn to attack, which breaks are mine.
5. **Candidate discipline** — list candidates before calculating any one.

**No heavy opening study until ~1800.**

---

## The one-line version

**When I'm winning: mate, every check, every capture — out loud — before I
touch a piece.**
