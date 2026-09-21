# Drill Trainer

**Link:** https://claude.ai/artifact/4i7JVkmA59fRvHEbdcGJDN

A single HTML page (chess.js 0.10.3 from cdnjs). Progress is saved in the
browser, per device. The trainer is the source of truth for my opening lines;
`docs/04-openings.md` describes them in words.

---

## The four modes

1. **Openings.** I play Black; White picks from the lines I've ticked.
   - One dot per variation: green = clean last time, red = mistake or hint.
   - Red variations come first, and the last variation never repeats.
   - A line gets a checkmark only when every dot is green.
   - A "Why" note appears after each of my moves.
2. **Squares.** Tap the named square. 30 seconds. "As White" and "As Black"
   board views.
3. **Key squares.** 40 positions: plans, targets, traps, and moments from my
   own games (RtsF7naM, 8QSDOF75). Tap the answer square, then read the
   explanation.
4. **Lessons.** Spaced-repetition flashcards (36 built in) from game reviews.
   Intervals: 1, 3, 7, 14, 30 days.

## What's in it

- 15 line groups, 189 sequences: Classical, Advance, Exchange, Panov, Two
  Knights, Fantasy, other 2nd moves, 2.Nf3/2.Nc3 then exd5, early queen
  (vs 1.e4); Slav, London, Colle, Blackmar-Diemer, other 1.d4 d5 systems
  (vs 1.d4); other first moves.
- 314 move notes, one per Black position. The original 148 were audited
  against their positions (notes 30, 32 and 137 were rewritten). The 166
  added in the coverage rebuild were written against their positions.
- Every Black move is Stockfish-checked (depth 17-18): none is more than
  0.30 pawns worse than the engine's best, so none is a mistake.
- The London covers White taking on c5 in every move order: 4.dxc5 e6
  (5.b4 a5), 4.c3 Nc6 5.dxc5 e5!, the Nf3 orders, and dxc5 after Nd2 e6.
- Coverage: lines were added for every White move that leaves the drill
  in at least 2 of every 1,000 Lichess rapid games at 900-1500 (sample:
  477k games from the August database). If I always play the drill move,
  White leaves the drill before the line ends in about 41 games in 100,
  down from 91. What's left is mostly moves seen in 1-2 games.
- 5 Leak #1 positions (Y3Kv4gW3, NrqqHy6s, jXbD9Hx4, Ioxb2Pab and
  CvarQfXV) and 4 no-calculation positions: rule of the square, king to
  the sixth, rook behind the passer, Blackburne Shilling.
- 4 "Their reply" positions (85TRwipG, hD2iTRzR, 2jB6uoec, gT0ifqcr):
  the opponent's punishing check or capture right after my mistake.

## Rules for editing it (for Claude)

1. **Update the same artifact link.** Never create a new one.
2. **Notes are keyed by move sequence.** `NOTES` is an object: the key is
   the move sequence that first reaches a Black position, the value is the
   note. Order no longer matters, so new sequences go in the group they
   belong to. Every Black position must have exactly one note, and a
   headless run must confirm none is missing (the page does not warn). Positions are keyed the way chess.js 0.10.3
   writes FENs (the en-passant square is always written after a two-square
   pawn move), so a transposition that ends with a pawn's double step is a
   different position and needs its own note.
3. A position must never have two different Black replies across lines.
4. **Validate before publishing:** every line and every key-square position
   through chess.js; every Black position has a note; then a headless run
   that plays every variation of every group to the end with the book
   moves and confirms zero mistakes, zero stuck runs and a note on every
   Black move.
5. Moments from my games go into Key squares with the game ID in the
   question text.
6. A note is not validated by chess.js. Check what it CLAIMS against the
   position: is that square occupied, is that piece actually blocked,
   can that knight actually go there?
7. Key-square positions are stored as FENs and outlive the 200-game
   window. Never swap a position because its game was trimmed.
8. New Black moves must be Stockfish-checked and within about 0.30 pawns
   of the best move. Prefer the move that fits the repertoire's system
   (bishop out before ...e6, ...c5 against d4, Bb5+ answered by ...Bd7)
   when it is that close.

## Fixed

The Lessons card "What do you check before EVERY move?" and the on-screen
tip in Openings mode both still taught the retired every-move scan. Both
now teach the triggers: the card is Trigger 1 (mate -> checks -> captures,
when winning), the tip is Trigger 3 (what does their move attack?).
