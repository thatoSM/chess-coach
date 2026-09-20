# My Openings

**Rule: no heavy opening study until ~1800.** Rating at my level is decided in
the middlegame and endgame. The repertoire exists to get me to a playable
middlegame on a routine, low-clock path — not to win games by itself.

The lines below are drilled in my trainer (see `training/drill-trainer.md`).
If this file and the trainer ever disagree, the trainer's validated lines win
and this file gets corrected.

---

## As White — 1.e4, Italian

1. `e4` 2. `Nf3` 3. `Bc4`, then `d3`, `Nc3`, castle **by move 10**.

The idea is fast, safe development: both knights, both bishops, king castled,
then play the middlegame.

**Against non-1...e5 replies** (Sicilian, Scandinavian, Pirc, French,
Caro-Kann, anything odd): play `d4` early and develop normally. Against the
Sicilian specifically, `2.d4` has been my best practical result
(see `docs/08-what-the-data-says.md`); the Bowdler `2.Bc4` has been my worst.

**The danger here is Leak #2 (opening autopilot).** When the opponent's move
is not the one I expected, ask one question before continuing the script:
**"what did that move stop defending?"**

---

## As Black — the ...c6 / ...d5 system

One structure against everything: pawns on c6 and d5, light-squared bishop out
to f5 or g4 **before** `...e6`, then `...e6`, `...Nf6` / `...Nd7`, castle, and
break with `...c5` or `...e5`.

### Against 1.e4 — Caro-Kann (`1...c6`, then `2...d5` almost always)

`2...d5` is played even against early queen moves (`Qh5`, `Qf3`, `Qe2`). Only
a quick forcing-move check first.

**Classical** — `3.Nc3` or `3.Nd2` `dxe4 4.Nxe4 Bf5 5.Ng3 Bg6 6.h4 h6 7.Nf3 Nd7
8.h5 Bh7 9.Bd3 Bxd3 10.Qxd3 e6`
- `11.Bd2 Ngf6 12.O-O-O Be7 13.Kb1 O-O`
- `11.Bf4 Qa5+` → `12.Bd2 Qc7` or `12.c3 Ngf6`
- Plan: castle, then free the position with `...c5` (aimed at a queenside
  king) or `...e5`. Answer `h4` with `...h6` so the bishop keeps h7.
- Trap to know: **4...Bf5, not 4...Nd7** — after `4...Nd7 5.Qe2 Ngf6?? 6.Nd6#`.

**Advance** — `3.e5 Bf5`
- `4.Nf3 e6 5.Be2 c5` → `6.O-O Nc6 7.c3 cxd4 8.cxd4 Nge7` or
  `6.Be3 cxd4 7.Nxd4 Ne7`
- `4.g4 Bd7`
- `4.Nc3 e6 5.g4 Bg6 6.Nge2 c5`
- Plan: attack d4, the **base** of the chain, with `...c5`, `...Nc6`, `...Qb6`.
  Don't attack on the kingside. The g8 knight goes via e7 (f6 is covered by e5).

**Exchange** — `3.exd5 cxd5 4.Bd3 Nc6 5.c3 Nf6 6.Bf4 Bg4 7.Qb3 Qd7`
- Plan: king safe first (White aims at h7), then the **minority attack**
  against c3: **`...a6` FIRST** (b5 is hit by `Bd3` and `Qb3`), then `...b5`,
  `...b4`, rooks to the c-file.

**Panov** — `3.exd5 cxd5 4.c4 Nf6 5.Nc3 e6 6.Nf3 Be7`
- Plan: knight blockades d5 in front of the isolated d4 pawn; trade pieces.
  If White plays `c5`, break with `...b6`.

**Two Knights** — `2.Nc3 d5 3.Nf3 Bg4` (**not** `3...dxe4`)
- Plan: bishop pair given up for a solid position; `...e6`, `...Nf6`, castle.

**Fantasy** — `3.f3 e6`
- Plan: hit d4 with `...c5` and `...Qb6`; develop `...Ne7`, `...Nbd7`.

### Against 1.d4 — `1...d5`

- **Slav** vs `2.c4`: `2...c6`. Bishop to f5 before `...e6`. If `Qb3` hits b7,
  answer `...Qb6`.
- **London**: `...Nf6`, `...c5`, `...Nc6`, `...e6`, `...Bd6` (trade White's
  f4 bishop), `...Qb6` idea hitting b2.
- **Jobava** (`Nc3` + `Bf4`): `...e6`; meet `Nb5` with `...Na6` (guards c7).
- **Colle**: `...Bf5` early, before White's `Bd3` can oppose it.
- **Blackmar-Diemer**: take both pawns (`...dxe4`, `...exf3`), then `...Bg4`,
  develop, castle. Don't grab more.

### Against anything else

- `1.c4` / `1.Nc3`: `1...c6` — transposes to a Caro-Kann or Slav.
- Everything else: `1...d5` and the same setup.

---

## How to meet a gambit (any gambit)

1. Take the pawn once if it's safe.
2. Give it back the moment holding it costs development.
3. Finish developing, castle, trade pieces. A traded-down gambit is just a
   pawn down.

---

## History (why the repertoire changed)

- Until September 2026 I played `1...e5` as Black (Italian / Four Knights
  structures), with the Queen's Gambit Declined approved but never integrated.
- I switched to the Caro-Kann and Slav to get a **routine** structure that
  saves clock for the middlegame and endgame, and one system that works
  against every first move.
- The old `1...e5` material (Wayward Queen answer `2...Nc6 3.Bc4 g6`, the
  Evans Gambit notes) no longer applies as Black and has been removed.

---

## The honest caveat

The opening is my most-scripted phase, so it is where Leak #2 lives. The
repertoire is not the problem — **playing it without looking is.** Every move
here is still subject to the forcing-move check.
