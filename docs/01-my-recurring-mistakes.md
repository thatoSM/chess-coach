# My Recurring Mistakes — THE CORE FILE

Read this first when analysing any new game. My mistakes are astonishingly
consistent. It is almost always the SAME leak wearing a new disguise.

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
| vs sarinafaragh (Black) | `11...O-O` | `11...Nxf3+` | a check-AND-capture; castling flipped eval -1.6 → +1.6 |
| vs Rinat (White) | `6.d3` | `6.Nxe4` | opponent hung a piece; I played my script instead |
| vs Clotilde78891 (Black) | `29...g5` | `29...Rf2+` | a CHECK; threw away -2.3 → +0.1 |

Every single miss was a check or a capture that Scan A would have surfaced. Not
one needed knowledge I don't have. When I get the same position AS A PUZZLE I
solve it instantly. The only difference is that nobody labelled it "White to
play and win" — so I didn't run the search.

### The Clotilde game is the clearest proof yet

Move 29: `Rf2+` was winning. I played `g5??`.
Move 33: I played `Rf2+`.

**I found the move four moves late, once the opponent handed the chance back.**
The move was never missing from my chess. The *search* was missing from my
routine. My puzzle rating (1116) is above my game rating (940) for exactly this
reason: in puzzles, someone else runs the search for me by saying "there's
something here."

**Coaching note:** when a new game shows this leak (it usually will), name it
explicitly as Leak #1 and point to this table. I need to FEEL how consistent it
is — it's not seven problems, it's one problem seven times.

## Leak #2 — opening autopilot

I've memorised my Italian setup so well I play it without looking. e4, Nf3, Nc3,
Bc4, O-O, d3 — I rattle it off. That's exactly when I miss a free piece, because
the opponent did something unusual (grabbed a pawn, brought the queen out) and I
kept playing my script instead of responding to the board.

**Fix:** the opening is NOT exempt from the scan — especially not the opening.
The moment the opponent does anything unexpected, I stop the script and run
Scan A. Early pawn-grabs almost always hang a piece; I've missed that free piece
more than once.

## Leak #3 — triage failure (saving small when I could win big)

Related to Leak #1. When something of mine is attacked, I rush to save it —
even when there's a BIGGER capture available elsewhere. Example: I played
`Nxa5` to save a bishop when `Bxc7` won the queen. I solved the right *kind* of
problem (a piece is attacked) at the wrong *priority*.

**Fix:** when something of mine is attacked, before saving it ask "is there
something BIGGER available?" Deal with the biggest thing on the board first.

## Leak #4 — drifting / no plan (RETRACTED — evidence was a misread)

**This leak is currently unsupported and should not be coached as fact.**

It was written up from Game 8 vs Clotilde78891 on the belief that I had been
squeezed into a lost position (~-10) by aimless piece play. That reading was
wrong twice over:

- I was **Black**, so negative evals were MY advantage. I was never worse than
  roughly equal (+0.1) in that game, and only for about four moves.
- The drifting rooks (`Rg3`, `Re3`, `Rg5`, `Rg1`) and the missed `h3` pin-break
  were **the opponent's moves and the engine's suggestions for the opponent** —
  recorded in this file as mine.

There is no confirmed instance of this leak in my games yet.

**Keep the question** — "what is the position asking me, and what's my laziest
piece?" — it is good practice and it belongs in the training system. But do not
promote it to a documented leak until a game genuinely demonstrates it in MY
moves. If one does, log the game, the move, and the engine line here.

## Leak #5 — playing chess while tired / after gaming

I've traced rating dips to playing late at night after long League/Fortnite
sessions. League specifically drains me most (locked-in matches, heavy working
memory, emotional load). Tired chess = blunder-brawls = lost rating.

**Fix:** chess goes FIRST in a session or not at all. No rated chess after a
long gaming session. If I want chess when tired, do puzzles instead (stoppable,
no rating I care about). NOTE: not every bad game is tired — some of my worst
games have been fresh, and those are pure "didn't run the scan." Distinguish.

## The meta-pattern

Leaks 1, 2, and 3 are all the same root: **I don't run Scan A before
quiet-looking moves.** Leak 5 is a state problem, not a skill problem. Leak 4 is
a placeholder with no evidence behind it.

When coaching me, figure out which of these a game shows — it is almost always
#1. Do not reach for a new, more sophisticated diagnosis just because my
accuracy was high. Game 8 was 90% accuracy and it was still Leak #1.
