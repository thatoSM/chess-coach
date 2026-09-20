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
3. **Key squares.** 27 positions: plans, targets, traps, and moments from my
   own games (RtsF7naM, 8QSDOF75). Tap the answer square, then read the
   explanation.
4. **Lessons.** Spaced-repetition flashcards (28 built in) plus my own cards
   from game reviews. Intervals: 1, 3, 7, 14, 30 days.

## What's in it

- 13 line groups, 52 sequences: Classical, Advance, Exchange, Panov, Two
  Knights, Fantasy, other 2nd moves, early queen (vs 1.e4); Slav, London,
  Colle, Blackmar-Diemer (vs 1.d4); other first moves.
- 148 move notes, one per first-seen Black position.

## Rules for editing it (for Claude)

1. **Update the same artifact link.** Never create a new one.
2. **Notes are matched to positions by first-seen order.** New lines go only
   at the **end** of `LINES`, and their notes at the **end** of `NOTES`.
   Inserting in the middle shifts every later note onto the wrong move.
3. A position must never have two different Black replies across lines.
4. **Validate before publishing:** every line and every key-square position
   through chess.js; note count must equal the number of first-seen Black
   positions; then a headless test of the page.
5. Moments from my games go into Key squares with the game ID in the
   question text.

## Known issue to fix (my call)

The Lessons card "What do you check before EVERY move?" answers "checks,
captures and threats." My documented fix is **mate → checks → captures**,
as a trigger when winning, not on every move (`training/board-card.md`).
