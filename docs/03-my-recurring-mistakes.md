# My Recurring Mistakes — THE CORE FILE

_Last updated: 2 August 2026, after a full review of all 13 analysed losses and
the games 43–48 winning streak. Every move claim below was verified against the
PGN in `games/pgn/` with a legal-move generator._

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
| Game 34 vs doctorexcal (White) | `28.b5` | `28.Ra8#` | **MATE IN ONE — and I played `Ra8+` on move 29** |
| Game 37 vs pavanraaj (Black) | `28...Qc1+` | `28...Qxf4` | had `#-4`; played the wrong forcing move. `#-4` → +3.20 |
| Game 30 vs AnayAnand2016 (White) | `12.Be3` | `12.Qh5+` | a CHECK at +6.21; quiet bishop move instead. +6.21 → +2.09 |
| Game 23 vs spoof-em-up (White) | `25.Kd3` | `25.Qxc7+` | check-AND-capture of the queen; I moved my king. +1.81 → -8.87 |
| Game 11 vs yahto19 (Black) | `23...Qd1` | `23...Qg3+` | a CHECK, handed a -7.79 position. -7.79 → -2.85 |
| Game 21 vs kai-reader (Black) | `9...h6` | `9...Bxd5` | a CAPTURE; quiet pawn move instead |
| Game 16 vs GiftmischerPTA (White) | `19.c4`, `20.dxc4`, `21.Nd7` | `Bxf6` | **the same capture available three moves running** |
| Game 15 vs rafffaelll2022 (Black) | `6...Re8`, `7...Nh5` | `Nxg4`, `Bxh3` | two captures on offer during a wild attack; played quiet moves |

**Added after the loss review of 2 Aug 2026.** Every row above was checked
against the PGN in `games/pgn/` with a legal-move generator — the suggested move
was legal in that exact position, and the colour was confirmed from the
`Colour:` line of each log entry first.

**Leak #1 is the decisive error in 8 of my 13 analysed losses.**

### It is present in my WINS too — 2 Aug 2026

Verified against the PGNs. These are all games I **won**:

| Game | I played | Was available | Swing |
|---|---|---|---|
| 44 (WIN) | `25...f5` | `Qf4+` | mate in 2 → -6.09 |
| 44 (WIN) | `26...Qd2` | `Qf4+` | mate in 2 → -5.16 |
| 44 (WIN) | `27...f4` | `Qf4+` | mate in 2 → -4.85 |
| 44 (WIN) | `30...f3` | **`Qg3#`** | **mate in one** → +2.85 |
| 48 (WIN) | `19...fxe5` | `Qg4+` | +0.59 → +8.49 — **played `Qg4+` on move 22** |
| 47 (WIN) | `10...exd4` | `Nxe3` | -7.59 → -0.84 |
| 47 (WIN) | `11...Nxd4` | `Nxe3` | -6.92 → -0.11 |

Game 44 is the Game 16 shape inside a win: the same check missed on three
consecutive moves, each time from a forced mate, then mate in one missed three
moves later. I won because the opponent blundered nine times to my seven.

**Game 47 is the warning.** 2 blunders, 0 mistakes, 0 inaccuracies —
statistically my cleanest game in the set. Both blunders were the same missed
capture, two moves running, each throwing away a completely winning position.
**A low blunder count is not evidence the leak is gone.**

**Unverified — do not cite as evidence:**

| Game | Claimed | Status |
|---|---|---|
| vs behnazpiroozkia | `Qe2` instead of `Rxf2` (free bishop) | **`Qe2` appears in NO logged game of mine.** Same failure mode as the retracted Leak #4 — probably the opponent's move. |
| vs Radmanj | `8...d6` instead of `8...b6` | **No such game exists in the log.** Source unknown. |
| middlegame example | `Rab1` instead of `Bxc7` (wins the queen) | No game attached. Keep only if I can name the game. |

> **CONFIRM:** either find the games behind those three rows and verify them, or
> delete the rows. A leak table with unverifiable entries is how Leak #4 happened.

### The one-move-late pattern — the strongest evidence in this repo

**Four times now** I have played the exact move I missed, a move or two later,
with nothing learned in between:

- **Game 5, move 11:** played `O-O`. `Nxf3+` was legal. **Played `Nxf3+` on move 12.**
- **Game 8, move 29:** played `g5`. `Rf2+` was legal. **Played `Rf2+` on move 33.**
- **Game 34, move 28:** played `b5`. **`Ra8#` was legal — mate in one.**
  **Played `Ra8+` on move 29**, by which point it lost: +7.75 → -5.80. Mated
  seven moves later.
- **Game 42, move 10:** played `Bg5` (+1.37 → -0.34). `Nxe5` was best.
  **Played `Nxe5` on move 11** (+0.02 → -4.23) and **resigned on move 11.**
  An eleven-move loss caused by nothing but playing the right move one move late.

A fifth near-instance, in a game I won: **Game 48, move 19** — missed `Qg4+`,
played it on move 22.

All confirmed against the PGN with a legal-move generator. The move was never missing from my chess. **The
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

## Leak #5 — playing chess after gaming (UNVERIFIED — no evidence found)

**Written from assertion, not data. No game was ever attached.**

Measured 7 Aug 2026 across 137 timestamped PGNs in `games/pgn/`:

| Start time (SAST) | Games |
|---|---|
| Before 21:00 | 129 |
| 21:00–22:59 | 8 |
| 23:00–03:00 | **0** |

The claim that late-night rapid is where the blunder-brawls live cannot be
supported. I have never played a rated rapid game at midnight. The 21:00–22:00
tail is 8 games — too few to compute a meaningful accuracy split, so no split
was computed.

**Unresolved:** I can't tell from this whether I never played late, or whether
the "chess goes first" rule prevented it. Either way the diagnosis was never
evidenced.

**Still untested:** the gaming-before-chess half. That needs League timestamps
joined to game timestamps. Not done yet — do not treat it as established.

**Do not reach for this leak when analysing a game** until a game demonstrates
it, the same standard applied to Leak #4.

---

---

## CANDIDATE — capturing without checking the reply (NOT YET NUMBERED)

**Do not treat this as a documented leak. It has evidence but no human review.**

The reverse shape of Leak #1: instead of missing a forcing move, I *make* one —
usually a capture — without asking what it allows. Four instances, all verified
against the PGN:

| Game | I played | Was best | Swing |
|---|---|---|---|
| 24 vs mlbbhunter (White) | `15.Bxb8` | `15.Bd6` | +9.72 → mate in 2 against me |
| 14 vs rafffaelll2022 (White) | `9.Qxg4` | `9.Nc3` | +5.27 → -5.99 |
| 25 vs Aliyetkin (White) | `24.Rxb1` | `24.Qxe5` | +0.32 → mate in 7 against me |
| 26 vs Aaryav555 (Black) | `27...exd4` | `27...Qe7` | -4.38 → +6.59 |

Game 21 move 13 (`dxe5` instead of `Rxe5`, straight into mate in 2) may belong
here too — it also breaks the board card's existing rule, *"recapture near my
king with a PIECE, not a pawn."*

**Four losses is enough to notice. It is not enough to number.** It might be a
genuine sixth leak, or it might be the far side of the same missing habit as
Leak #1. **I review those four positions myself before this becomes a numbered
leak.** That is the Leak #4 lesson.

---

## CANDIDATE — failing to convert a winning endgame (NOT YET NUMBERED)

Two instances of a smooth decline rather than a blunder-brawl:

- **Game 20 vs minikmustafa (White):** 40 ACPL, no catastrophe. +5.46 at move 19
  declining steadily to -3 by move 31 across a dozen small errors. The engine
  wanted quiet improving moves — `Rf1`, `Rg1`, `a4`, `Ke3`.
- **Game 41 vs prince202621 (White):** +7.37 at move 35 bleeding to +1.20 by
  move 42, then `48.Kb3` (+6.01 → -6.63). A 71-move loss.

**Two is not a pattern.** Watch for a third before writing anything down. This
also sits oddly against endgame being my strongest phase — which may mean it's a
*long-game* problem rather than an endgame one.

---

## The meta-pattern

- **Leaks 1, 2 and 3 are the same root:** I don't run the forcing search before
  quiet-looking moves — or I run it in the wrong order.
- **Leak 4 is unproven.** Don't reach for it.
- **Leak 5 is unverified.** Two of five numbered leaks now are.
- **Two candidates are unnumbered on purpose.** Capturing-without-checking (4
  instances) and endgame conversion (2 instances). Evidence exists; human review
  doesn't. They stay unnumbered until I've looked at the positions myself.

When coaching me: figure out which of these a game shows. It's almost always one
of these, and **usually #1**. Do not reach for a new, more sophisticated
diagnosis just because my accuracy was high — Game 8 was 90% and was still #1.

**And do not add a row to any table without the game attached.** Three rows in
this file currently can't be traced to a game. That is exactly how Leak #4
became a fake weakness.
