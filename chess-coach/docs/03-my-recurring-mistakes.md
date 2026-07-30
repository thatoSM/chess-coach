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

### Documented instances (all the same leak):

| Game | I played | I should have played | What I missed |
|---|---|---|---|
| vs behnazpiroozkia (Black) | `Qe2` | `Rxf2` | a free bishop sitting undefended |
| middlegame example | `Rab1` | `Bxc7` | winning the opponent's QUEEN on an open diagonal |
| vs Radmanj (Black) | `8...d6` | `8...b6` | gave back a winning material edge by opening lines |
| vs RafaEspejo (Black) | `27...Be6` | `27...Qg3+` | a FORCED MATE |
| vs sarinafaragh (Black) | `11...O-O` | `11...Nxf3+` | a check-AND-capture; eval flipped -1.6 → +1.6 |
| vs Rinat (White) | `6.d3` | `6.Nxe4` | opponent hung a piece; I played my script instead |
| **vs Clotilde78891 (Black)** | **`29...g5??`** | **`29...Rf2+`** | **a CHECK; eval -2.3 → +0.1 — and I played `Rf2+` four moves later** |

Every single miss was a check or a capture that Scan A would have surfaced. Not
one needed knowledge I don't have. When I get the same position AS A PUZZLE I
solve it instantly. The only difference is that nobody labelled it "White to
play and win" — so I didn't run the search.

**The Clotilde game is the definitive proof.** I missed `Rf2+` on move 29 and
played `Rf2+` on move 33. Same move, same idea, four moves apart, with nothing
learned in between. The move was never missing from my chess. **The search was
missing from my routine.**

**Coaching note:** when a new game shows this leak (it usually will), name it
explicitly as Leak #1 and point to this table. I need to FEEL how consistent it
is — it's not seven problems, it's one problem seven times.

---

## Leak #2 — opening autopilot

I've memorised my Italian setup so well I play it without looking. e4, Nf3,
Nc3, Bc4, O-O, d3 — I rattle it off. That's exactly when I miss a free piece,
because the opponent did something unusual (grabbed a pawn, brought the queen
out) and I kept playing my script instead of responding to the board.

**Fix:** the opening is NOT exempt from the scan — especially not the opening.
The moment the opponent does anything unexpected, stop the script and run
Scan A. Early pawn-grabs almost always hang a piece; I've missed that free
piece more than once.

**Status:** improving. Game 8 opening accuracy was 86%, my best recorded. Don't
declare it fixed yet, but it's no longer automatically my worst phase.

---

## Leak #3 — triage failure (saving small when I could win big)

Related to Leak #1. When something of mine is attacked, I rush to save it —
even when there's a BIGGER capture available elsewhere. Example: I played
`Nxa5` to save a bishop when `Bxc7` won the queen. I solved the right *kind* of
problem (a piece is attacked) at the wrong *priority*.

**Fix:** when something of mine is attacked, before saving it ask "is there
something BIGGER available?" Deal with the biggest thing on the board first.

---

## Leak #4 — drifting / no plan (UNVERIFIED — evidence retracted)

**This leak was written up from Game 8, and that analysis was wrong.**

The drifting rooks (`Rg3`, `Re3`, `Rg5`, `Rg1`), the `Re1??` on move 9, and the
missed `h3` pin-break were all **the opponent's moves or engine suggestions for
the opponent** — not mine. As Black, those squares aren't even mine to use.

**I currently have no confirmed instance of this leak.**

Keep the planning question — "what is the position asking me, and what is my
laziest piece?" — because it's good practice regardless. But **do not treat
Leak #4 as a documented weakness** until a game demonstrates it in MY moves,
verified against the correct colour.

If a future game does show it, rewrite this section with the real evidence.

---

## Leak #5 — playing chess while tired / after gaming

I've traced rating dips to playing late at night after long League/Fortnite
sessions. League specifically drains me most (locked-in matches, heavy working
memory, emotional load). Tired chess = blunder-brawls = lost rating.

**Fix:** chess goes FIRST in a session or not at all. No rated chess after a
long gaming session. If I want chess when tired, do puzzles instead (stoppable,
no rating I care about).

**NOTE:** not every bad game is a tired game. Some of my worst games have been
fresh — Game 5 (57%, 6 blunders) was a fresh game. Those are pure "didn't run
the scan." Distinguish before blaming fatigue, or I'll fix the wrong thing.

---

## The meta-pattern

- **Leaks 1, 2 and 3 are the same root:** I don't run Scan A before
  quiet-looking moves.
- **Leak 4 is unproven.** Don't reach for it.
- **Leak 5 is a state problem, not a skill problem.**

When coaching me: figure out which of these a game shows. It's almost always
one of these, and **usually #1**.
