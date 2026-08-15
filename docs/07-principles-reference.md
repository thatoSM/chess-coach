# General Principles — Reference

**This file is a reference, not a checklist. It does NOT go on the board card.**

I asked for this after hearing strong players talk about ideas I'd never been
given — king safety, adding attackers, removing defenders — and feeling behind.
This file exists so I stop wondering what I'm missing. It is for reading on a
quiet Sunday, not for consulting mid-game on a 10+5 clock.

`training/board-card.md` stays short on purpose. The card is what I can actually
execute under a clock. This file is the map of the territory.

> **The gate:** nothing moves from this file onto the board card until three
> consecutive analysed games contain **zero moves losing more than 200cp** to a
> hanging piece or a missed check. See `docs/05-coaching-principles.md` #10 —
> adding is easier than fixing and feels like progress while being none.

---

## How to read the "when it matters" tags

Rough bands. They're not exact and they overlap, but the ordering is real: the
lower items are worth more rating per hour of study at my level than the higher
ones.

| Tag | Meaning |
|---|---|
| **NOW** | Already costing me rated games. Some are already in my files. |
| **SOON** | Starts paying off around 1200–1500. |
| **LATER** | Around 1500–1800. |
| **MUCH LATER** | 1800+. Interesting, not urgent. |

**Column "In my repo?"** tells me whether this is genuinely new information or
something I already have written down and am not executing. Be honest about
which is which — most of the NOW items are the second kind.

---

# 1. King safety

The thing I asked about first. Most of it I already have.

| # | Principle | When | In my repo? |
|---|---|---|---|
| 1.1 | **Castle by move 10.** Both colours, every game. | NOW | Yes — board card, Hard rules |
| 1.2 | **A king in the centre after the queens come off is fine; a king in the centre with queens on is a target.** The danger is proportional to how much heavy material is left. | NOW | New |
| 1.3 | **Recapture near my king with a piece, not a pawn.** Pawn recaptures near the king open lines at my own king. | NOW | Yes — board card |
| 1.4 | **Don't move the three pawns in front of my castled king without a reason.** Each one is a permanent hole. | NOW | New |
| 1.5 | **The luft exception:** one of `h3`/`h6` or `g3`/`g6` to give the king an escape square is usually worth it, to avoid back-rank mate. | NOW | New |
| 1.6 | **Count attackers vs defenders around my king,** not just on individual squares. If they have three pieces aimed at my king and I have one defending, I'm losing whether or not I can see the tactic yet. | SOON | New |
| 1.7 | **Opposite-side castling means a pawn race.** Whoever's attack lands first wins. Don't play slow moves in these positions. | LATER | New |
| 1.8 | **In the endgame the king is a strong piece.** Activate it. Opposite of everything above — the rule flips once the queens and most pieces are gone. | NOW | New |

**Honest note on this section:** in the Panov game I analysed, my king was safe
for all 28 moves and my opponent's king ended on a7. King safety was the part I
got *right*. It was not the reason that game was nearly lost.

---

# 2. Piece safety and material

**This is where my rating currently lives.** Everything in this section is
already in `docs/02-training-system.md` or on the board card. Nothing here is new.
It is listed so I can see how much of what I "don't know" I already have.

| # | Principle | When | In my repo? |
|---|---|---|---|
| 2.1 | **Before releasing a move: name the destination square, count who attacks it.** Attackers > defenders → reject the move. | NOW | Yes — "Counting" |
| 2.2 | **After every opponent move: what did that move attack?** | NOW | Yes — Scan B |
| 2.3 | **After every opponent move: what did that move stop defending?** | NOW | Yes — Scan B |
| 2.4 | **LPDO — loose pieces drop off.** Scan both sides for undefended pieces every position. Mine are what I'm about to lose. Theirs are where my tactic is. | NOW | Yes — LPDO |
| 2.5 | **Before any capture on a contested square, count the whole sequence** — attackers, defenders, and the *order* they come off. | NOW | Yes — "Counting" |
| 2.6 | **Something of mine is attacked? Before saving it, ask whether something bigger is available.** | NOW | Yes — Leak #3 fix |
| 2.7 | **A piece that is defended is not therefore safe.** It's safe if the exchange sequence comes out even or better. Those are different questions. | NOW | New |
| 2.8 | **Rough values:** pawn 1, knight 3, bishop 3, rook 5, queen 9. Rook for knight/bishop is "the exchange," worth about 1.5–2. | NOW | Implied |

---

# 3. The attack-and-defend layer

This is what Magnus was talking about. It is the layer *above* section 2 —
none of it works if the piece I'm adding is itself hanging.

| # | Principle | When | In my repo? |
|---|---|---|---|
| 3.1 | **Add an attacker.** Square defended once, attacked once? Bring a second attacker before capturing. | SOON | Partly — inverse of Counting |
| 3.2 | **Remove the defender.** If the piece I want is guarded, capture the guard, chase it, or pin it first. | SOON | **New** |
| 3.3 | **Overload / deflection.** If one piece is doing two defensive jobs, attack one job — the other collapses. | SOON | **New** |
| 3.4 | **Decoy.** Force a piece (often the king) onto a square where a tactic works. | SOON | New |
| 3.5 | **Interference / blocking.** Cut the line between a defender and what it defends. | LATER | New |
| 3.6 | **Fork.** One piece attacks two targets. Knights and pawns are the classic forkers. Needs a loose piece or the king to land on. | NOW | Partly — Scan A #3 |
| 3.7 | **Pin.** A piece can't move because something more valuable is behind it. Absolute pin = against the king, the piece literally cannot move. | NOW | New |
| 3.8 | **Attack a pinned piece with a pawn.** A pinned piece can't run, so hitting it with something cheap usually wins it. | SOON | New |
| 3.9 | **Skewer.** The reverse of a pin — valuable piece in front, it moves, I take what's behind. | SOON | New |
| 3.10 | **Discovered attack.** Move one piece, uncover an attack from the piece behind it. **Discovered check is the most powerful move in chess** — the moving piece can go anywhere, including somewhere it "shouldn't" be able to. | SOON | New |
| 3.11 | **Double check.** Only the king can move. Nothing can block or capture. | SOON | New |
| 3.12 | **Zwischenzug / in-between move.** Before recapturing, check whether I have a check or a bigger threat first. Recapturing is not obligatory. | SOON | Related to Leak #1 |
| 3.13 | **Trapped piece.** A piece with no safe squares can be hunted with pawns even if it isn't currently attacked. | SOON | New |
| 3.14 | **Back-rank mate.** A castled king with three unmoved pawns and no escape square is a permanent tactical target for both sides. | NOW | New |
| 3.15 | **Every tactic needs a target:** a loose piece, an overloaded defender, an exposed king, or two pieces on a line. **If I can't name the target, the tactic isn't there.** | SOON | Related to LPDO |

**Puzzle themes to select on Lichess for this section:** Remove the Defender,
Deflection, Overloading, Discovered Attack, Pin, Skewer, Back Rank.
Keep difficulty on **Normal**, not Harder — see `training/puzzle-routine.md`.

---

# 4. Development and piece activity

| # | Principle | When | In my repo? |
|---|---|---|---|
| 4.1 | **Develop knights and bishops before the queen and rooks.** | NOW | Yes — `docs/04-openings.md` |
| 4.2 | **Don't move the same piece twice in the opening without a concrete reason.** | NOW | Implied |
| 4.3 | **Don't bring the queen out early.** She gets chased and I lose tempo. (Also: when *they* do it, that's my Scan B "unusual move" trigger.) | NOW | Yes — Scan B #4 |
| 4.4 | **Develop toward the centre.** A knight on the rim controls half as many squares. | NOW | New |
| 4.5 | **Connect the rooks** — finish development, then put rooks on open or soon-to-open files. | SOON | New |
| 4.6 | **Rooks belong on open files; doubled rooks on an open file are a battering ram.** | SOON | New |
| 4.7 | **Rooks belong on the 7th rank** (2nd for Black) — they attack pawns and cut the king off. | SOON | New |
| 4.8 | **Improve my worst-placed piece.** When there's nothing forcing, ask: *what is the position asking me, and what is my laziest piece?* | NOW | Yes — planning question |
| 4.9 | **A bishop pair in an open position is worth about half a pawn extra.** Don't trade one off casually. | LATER | New |
| 4.10 | **Knights want closed positions and outposts; bishops want open diagonals.** Trade toward the structure that suits my pieces. | LATER | New |
| 4.11 | **An outpost** is a square in enemy territory that can't be attacked by a pawn. A knight on one is worth more than a knight. | LATER | New |
| 4.12 | **A piece's job determines its value, not the piece-value table.** Already learnt this one: `Bxc6` over `Ba4` because `Ba4` releases the c6 knight's grip on d4. | NOW | Yes — logged |

---

# 5. Pawn structure

Pawns are the only pieces that can't go backwards. Every pawn move is permanent.

| # | Principle | When | In my repo? |
|---|---|---|---|
| 5.1 | **Doubled pawns** — two of mine on the same file. Usually a weakness; sometimes fine because they open a file for my rook. | SOON | New |
| 5.2 | **Isolated pawn** — no friendly pawn on either neighbouring file. Weak in the endgame, but gives active piece play in the middlegame. | SOON | New |
| 5.3 | **Backward pawn** — can't advance, can't be defended by a pawn. A long-term target, especially on a half-open file. | LATER | New |
| 5.4 | **Passed pawn** — no enemy pawn can stop it. **Push passed pawns.** In the endgame they decide games. | SOON | New |
| 5.5 | **Rooks belong behind passed pawns** — mine and theirs. | LATER | New |
| 5.6 | **Pawn chains point in a direction. Attack the base**, not the head. | LATER | New |
| 5.7 | **A pawn majority on one wing means a future passed pawn there.** That's the plan. | LATER | New |
| 5.8 | **Don't create weaknesses to win a pawn** unless I can hold the pawn. | SOON | Related to gambit rule |

---

# 6. Attacking the enemy king

| # | Principle | When | In my repo? |
|---|---|---|---|
| 6.1 | **Attack where I have more pieces.** Count my attackers vs their defenders in that sector first. | SOON | New |
| 6.2 | **Bring the last piece.** Attacks fail because one piece stayed home. Before sacrificing, ask which of my pieces is not yet participating. | SOON | Related to idle-piece pattern |
| 6.3 | **Open a line to the king before sacrificing on it** — a sacrifice into a closed position just loses material. | LATER | New |
| 6.4 | **Don't start a wing attack while the centre is open** — the counterblow in the centre is faster. | LATER | New |
| 6.5 | **A king dragged into the open loses even with extra material.** Exactly what happened to my opponent in the Panov game: `Bxf7+`, `Be6+`, `Bf4+` pulled his king to a7 while he was a queen up. | NOW | New |
| 6.6 | **Checks are not automatically good.** A check that achieves nothing loses a tempo and often wastes the position. Look for the check *first* (Scan A) — then decide whether to play it. | NOW | Refinement of Scan A |

---

# 7. Defence and prophylaxis

| # | Principle | When | In my repo? |
|---|---|---|---|
| 7.1 | **Ask what they want to do, before deciding what I want to do.** | NOW | Yes — Scan B |
| 7.2 | **Meet a wing attack with a break in the centre.** | LATER | New |
| 7.3 | **When defending, trade attackers.** Every piece traded weakens their attack disproportionately. | SOON | New |
| 7.4 | **When winning big, trade — especially queens.** Simplify. Don't keep it complicated. | NOW | Yes — board card |
| 7.5 | **When losing, avoid trades and keep the position messy.** Opponents crack. | NOW | Related to "never resign" |
| 7.6 | **The best defence is often a counter-threat**, not a passive defensive move. | LATER | New |
| 7.7 | **Never resign.** Endgame is my best phase; opponents at my level crack constantly. Game 8 ended in mate on move 67. | NOW | Yes — board card |

---

# 8. Trading rules

| # | Principle | When | In my repo? |
|---|---|---|---|
| 8.1 | **Ahead in material → trade pieces, keep pawns.** | NOW | Yes — board card |
| 8.2 | **Behind in material → avoid trades, keep complications.** | NOW | Implied |
| 8.3 | **Trade my bad piece for their good piece.** | SOON | New |
| 8.4 | **Don't trade a defender of my king.** | SOON | New |
| 8.5 | **Cramped position → trade to get room.** | LATER | New |
| 8.6 | **A trade is never "even" just because the values match.** Ask what each piece was doing. | NOW | Yes — logged, `Bxc6` rule |

---

# 9. Endgame fundamentals

My strongest phase by score, but the phase breakdown says ~38% of my centipawn
loss happens here. Both things are true.

| # | Principle | When | In my repo? |
|---|---|---|---|
| 9.1 | **Activate the king.** In the endgame it's a fighting piece worth about four pawns. | NOW | New |
| 9.2 | **Push passed pawns; create one if I can.** | NOW | New |
| 9.3 | **Opposition** in king-and-pawn endings — kings facing each other with one square between; whoever does *not* have to move wins the square. | NOW | New — puzzle theme already selected |
| 9.4 | **The square of the pawn** — a quick way to see if a lone king can catch a runner. | NOW | New |
| 9.5 | **Rook endings: rook behind the passer, and the Lucena and Philidor positions.** These two positions decide a large share of rook endings. | SOON | New |
| 9.6 | **Basic mates I must be able to do without thinking:** K+Q, K+R, K+two bishops. | NOW | Assumed |
| 9.7 | **K+B+N mate and K+B vs K+N** — real but rare. Don't spend time here yet. | MUCH LATER | New |

---

# 10. Practical and clock

| # | Principle | When | In my repo? |
|---|---|---|---|
| 10.1 | **Spend time at the moment the position changes character** — a capture, a check, an unusual move — not on quiet moves. | NOW | New |
| 10.2 | **Errors take longer than clean moves.** My data: ~14s median on errors vs ~7s on clean moves. **More time is not the fix — structured search is.** | NOW | Yes — logged finding |
| 10.3 | **Most of my damage happens in winning positions (+1.5 to +4)** — 3.4× the error rate of level positions. Treat "winning" as a danger flag, not a rest. | NOW | Yes — logged finding |
| 10.4 | **The size of my single worst move predicts the result** better than my average accuracy. Median worst move: ~326cp in wins, ~793cp in losses. | NOW | Yes — logged finding |
| 10.5 | **High accuracy can hide the leak.** I have missed forced mates in games scored 97–99%. | NOW | Yes — logged finding |
| 10.6 | **Don't play rated chess after a long gaming session, or late at night.** (Flagged as UNVERIFIED against my own data — see Leak #5. Keep as a preference, not a finding.) | NOW | Yes — Leak #5, unverified |

---

# 11. What the strong-player advice actually is

The rules Magnus and other GMs talk about publicly are almost all from sections
3, 4, 5 and 6 above. That's not an accident. They're talking to an audience for
whom section 2 — piece safety — is already automatic and therefore not worth
mentioning.

**The order is:**

1. Don't hang pieces, and take what they hang. (Section 2)
2. Get the king safe and the pieces out. (Sections 1 and 4)
3. Then the attack-and-defend layer. (Section 3)
4. Then structure and long-term planning. (Sections 5 and 6)

Watching level-4 content while leaking at level 1 feels like education. It isn't.
It's the specific feeling that produced this file.

---

# 12. The honest summary

Counting the table rows: about **75 principles**. Roughly **20 of them** were
already written in `docs/02-training-system.md`, `docs/04-openings.md` or
`training/board-card.md` before this file existed. Those 20 are also the ones
tagged NOW.

**So the gap was never the principles. It was the execution of the ones I had.**

Evidence, from my own repo:

- Puzzle rating above game rating — in a puzzle, someone else tells me the
  tactic exists. I solve it. The knowledge is there.
- The one-move-late pattern, three times: `Nxf3+` (G5, one move late),
  `Rf2+` (G8, four moves late), `Bc5+` (Panov game, one move late). The move was
  never missing.
- Missed mate in one vs esteesAmin, move 29. No principle fixes that.
- Panov game moves 9 and 22: two pieces placed on attacked squares, 9.77 pawns
  lost. The rule that catches both — Counting — was already on the board card.

---

## The one thing this file does not change

> **Before releasing any move: name the destination square, count who attacks it.**
> Attackers > defenders → reject the move, pick another candidate.

That is still the whole job. This file goes in a drawer until the gate at the
top is cleared.

---

> **CONFIRM:** the "when it matters" rating bands are my coach's rough estimate,
> not measured against my games. Treat the ordering as reliable and the specific
> numbers as approximate. The "In my repo?" column was checked against
> `docs/02`, `docs/04`, `docs/05` and `training/board-card.md` at time of
> writing — recheck it if those files change.
