# My Recurring Mistakes — THE CORE FILE

Read this first when analysing any new game (after confirming colour and eval
sign — see `docs/06-reading-an-analysis.md`).

My mistakes are astonishingly consistent. It is almost always the SAME leak
wearing a new disguise.

---

## Leak #1 — I play a quiet move when a FORCING move wins (my #1 problem)

This is THE pattern. In game after game, a check or capture — often winning
material or even a forced mate — sits on the board, and I play a tidy,
sensible-looking developing move instead. My brain searches for "a good move,"
not "the most forcing move." Those are different searches.

### Documented instances

**Verified against the PGN** (the move I should have played was legal in that
exact position):

| Game | I played | I should have played | What I missed |
|---|---|---|---|
| vs RafaEspejo (Black) | `27...Be6` | `27...Qg3+` | a FORCED MATE |
| vs sarinafaragh (Black) | `11...O-O` | `11...Nxf3+` | check-AND-capture; -1.6 → +1.6 — **and I played `Nxf3+` on move 12** |
| vs Rinat2312 (White) | `6.d3` | `6.Nxe4` | opponent hung a piece; I played my script |
| vs Clotilde78891 (Black) | `29...g5??` | `29...Rf2+` | a CHECK; -2.3 → +0.1 — **and I played `Rf2+` on move 33** |
| vs water-dragon562 (White) | `3.Bc4?` | `3.Nxe5` | `2...Bc5` stopped defending e5; +1.8 → +0.3 |
| vs esteesAmin (Black) | `29...Nxd1??` | `29...Qxg2#` | **MATE IN ONE — I took a rook instead** |

**Unverified — do not cite as evidence:**

| Game | Claimed | Status |
|---|---|---|
| vs behnazpiroozkia | `Qe2` instead of `Rxf2` (free bishop) | **`Qe2` appears in NO logged game of mine.** Same failure mode as the retracted Leak #4 — probably the opponent's move. |
| vs Radmanj | `8...d6` instead of `8...b6` | **No such game exists in the log.** Source unknown. |
| middlegame example | `Rab1` instead of `Bxc7` (wins the queen) | No game attached. Keep only if I can name the game. |

> **CONFIRM:** either find the games behind those three rows and verify them, or
> delete the rows. A leak table with unverifiable entries is how Leak #4 happened.

### The one-move-late pattern — the strongest evidence in this repo

Twice now I have played the exact move I missed, a move or two later, with
nothing learned in between:

- **Game 5, move 11:** played `O-O`. `Nxf3+` was legal. **Played `Nxf3+` on move 12.**
- **Game 8, move 29:** played `g5`. `Rf2+` was legal. **Played `Rf2+` on move 33.**

Both confirmed against the PGN. The move was never missing from my chess. **The
search was missing from my routine.** My puzzle rating being above my game
rating says the same thing — in a puzzle, someone else runs the search for me.

### Scan ORDER — added after Game 10

Game 10 was a new shape. I *did* play a forcing move — I captured a rook. But
mate in one was on the board. I ran the forcing search in the wrong order.

> **Mate → checks → captures. In that order, every time.**
>
> Before I take anything: *"is there a check? does that check mate?"* A free
> rook will still be free one second later. The mate might not.

That is now **two missed forced mates** (RafaEspejo move 27, esteesAmin move 29).

**Coaching note:** when a new game shows this leak (it usually will), name it
explicitly as Leak #1 and point to this table. I need to FEEL how consistent it
is — it's not six problems, it's one problem six times.

---

## Leak #2 — opening autopilot

I've memorised my Italian setup so well I play it without looking. e4, Nf3,
Nc3, Bc4, O-O, d3 — I rattle it off. That's exactly when I miss a free piece,
because the opponent did something unusual and I kept playing my script.

**Two clean instances, both the same shape:**

| Game | Opponent deviated | I played | Free material I walked past |
|---|---|---|---|
| vs Rinat2312 | `5...Nxe4??` | `6.d3` | the knight |
| vs water-dragon562 | `2...Bc5?` (not `Nc6`) | `3.Bc4` | the e5 pawn |

Both times: opponent leaves the main line in the first six moves, I keep playing
the memorised sequence, material walks past.

**Fix:** the opening is NOT exempt from the scan. When the opponent's move isn't
the one I expected, ask one specific question — **"what did that move stop
defending?"** Not a general scan. One question, aimed at the piece that moved.
Both answers above were one move deep.

**Status: genuinely improving.** Opening accuracy 57% (G7) → 80% (G9) → **95%
(G10)**, my best in the log. No longer automatically my worst phase.

---

## Leak #3 — triage failure (saving small when I could win big)

Related to Leak #1. When something of mine is attacked, I rush to save it —
even when there's a BIGGER capture available elsewhere. Example: `Nxa5` to save
a bishop when `Bxc7` won the queen. Right *kind* of problem, wrong *priority*.

**Fix:** when something of mine is attacked, before saving it ask "is there
something BIGGER available?" Deal with the biggest thing on the board first.

> **CONFIRM:** the `Nxa5`/`Bxc7` example has no game attached. Same problem as
> the unverified Leak #1 rows — find the game or drop the example.

---

## Leak #4 — drifting / no plan (UNVERIFIED — evidence retracted)

**This leak was written up from Game 8, and that analysis was wrong.**

The drifting rooks (`Rg3`, `Re3`, `Rg5`, `Rg1`), the `Re1??` on move 9, and the
missed `h3` pin-break were all **the opponent's moves or engine suggestions for
the opponent** — not mine. As Black, those squares aren't even mine to use. The
PGN now in the repo confirms this.

**I still have no confirmed instance of this leak.**

Keep the planning question — "what is the position asking me, and what is my
laziest piece?" — because it's good practice regardless. But **do not treat
Leak #4 as a documented weakness** until a game demonstrates it in MY moves,
verified against the correct colour.

---

## Leak #5 — playing chess while tired / after gaming

I've traced rating dips to playing late at night after long League/Fortnite
sessions. League drains me most (locked-in matches, heavy working memory,
emotional load). Tired chess = blunder-brawls = lost rating.

**Fix:** chess goes FIRST in a session or not at all. No rated chess after a
long gaming session. If I want chess when tired, do puzzles instead.

**NOTE:** not every bad game is a tired game. Game 5 (57%, 6 blunders) was
fresh. Those are pure "didn't run the scan." Distinguish before blaming fatigue,
or I'll fix the wrong thing.

---

## The meta-pattern

- **Leaks 1, 2 and 3 are the same root:** I don't run the forcing search before
  quiet-looking moves — or I run it in the wrong order.
- **Leak 4 is unproven.** Don't reach for it.
- **Leak 5 is a state problem, not a skill problem.**

When coaching me: figure out which of these a game shows. It's almost always one
of these, and **usually #1**. Do not reach for a new, more sophisticated
diagnosis just because my accuracy was high — Game 8 was 90% and was still #1.

**And do not add a row to any table without the game attached.** Three rows in
this file currently can't be traced to a game. That is exactly how Leak #4
became a fake weakness.
