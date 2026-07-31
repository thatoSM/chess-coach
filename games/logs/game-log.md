# Game Index

One line per game. This file stays scannable no matter how many games I play —
**the leak column is the point.** Reading it down the page is how I see the same
mistake repeating.

Full entries live in `games/logs/`. Aggregate evidence lives in
`docs/03-my-recurring-mistakes.md`, which is **never split**.

**Before adding an entry, read `docs/06-reading-an-analysis.md`** and confirm
colour and eval direction first.

| # | Result | Colour | Opponent (rating) | Leak | Detail |
|---|---|---|---|---|---|
| 15 | LOSS | Black | rafffaelll2022 (1024) | *pending* | [001-030](logs/games-001-030.md) |
| 14 | LOSS | White | rafffaelll2022 (1018) | *pending* | [001-030](logs/games-001-030.md) |
| 13 | WIN | Black | samerhatam (947) | *pending* | [001-030](logs/games-001-030.md) |
| 12 | WIN | White | MarcoxNew (1009) | *pending* | [001-030](logs/games-001-030.md) |
| 11 | LOSS | Black | yahto19 (1061) | *pending* | [001-030](logs/games-001-030.md) |
| 10 | WIN | Black | esteesAmin (1059) | **#1** (scan order) | [001-030](logs/games-001-030.md) |
| 9 | WIN | White | water-dragon562 (1112) | **#2** → #1 | [001-030](logs/games-001-030.md) |
| 8 | WIN | Black | Clotilde78891 | **#1** | [001-030](logs/games-001-030.md) |
| 7 | WIN | White | Rinat2312 (1015) | **#2** | [001-030](logs/games-001-030.md) |
| 6 | WIN | White | AaranyaRameshwaran (894) | *clean* | [001-030](logs/games-001-030.md) |
| 5 | LOSS | Black | sarinafaragh (995) | **#1** | [001-030](logs/games-001-030.md) |
| 4 | WIN | Black | RafaEspejo (904) | **#1** | [001-030](logs/games-001-030.md) |
| 3 | WIN | White | i_am_a_knight (834) | castled late | [001-030](logs/games-001-030.md) |
| 2 | WIN | Black | behnazpiroozkia (993) | recapture | [001-030](logs/games-001-030.md) |
| 1 | — | — | *profile snapshot* | — | [001-030](logs/games-001-030.md) |

---

## Rollover rule

When game 31 is played, create `games/logs/games-031-060.md` and point new index
rows at it. **Never renumber. Never move an existing entry between files.**

## Why it's split this way

Splitting the detail by 30s keeps any single file readable. Keeping the index
whole keeps the pattern visible — five `#1`s stacked in one column say more than
five write-ups scattered across two files ever could.
