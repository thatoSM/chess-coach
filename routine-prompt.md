This is a personal chess-training repo. My Lichess username is ThatoSM.

IMPORTANT — always send a `User-Agent` header on every curl request to
lichess.org (e.g. `-A "Mozilla/5.0"` or `-H 'User-Agent: Mozilla/5.0'`).
Without one, `lichess.org/api/games/user/{username}` returns a bare 404
`{"error":"Not found"}` even though the endpoint is fine — this cost a full
night's sync before the cause was found. Every curl example below already
includes it; keep it on any curl command you add.

REPO STRUCTURE — read this first, it governs every part below:

- `games/game-log.md` is an INDEX ONLY. It is a markdown table, newest game at
  the top, with columns: `| # | Date | Result | Colour | Opponent | Leak |`. It
  contains NO game IDs, NO links, NO analysis. Never write full entries here.
- `games/logs/games-001-040.md`, `games-041-080.md`, etc. hold the FULL entries,
  40 games per file, newest-first within each file. All links, moves, and
  analysis live here.
- `docs/` is off limits. Never edit anything in it.
- `README.md`, `training/`, and every `**Lesson —` and `**The ONE thing to
  fix:**` block are HUMAN-WRITTEN. Never edit them. Numbers that change go in
  STATS.md (Part 5), which is regenerated wholesale every night.

Your job tonight has FOUR parts: (1) sync any new finished games as DRAFT
entries, (2) backfill real computer-analysis data into existing draft entries
that are now analysed on Lichess, (3) backfill my Elo into old entry headings
that don't have it yet, and (4) remove any zero-move games that slipped in.

=== PART 1 — SYNC NEW GAMES ===

STEP 1 — Find what's already logged.
Read EVERY file in `games/logs/` and extract every Lichess game ID already
referenced (lines like `Link: https://lichess.org/XXXXXXXX` — the 8-char ID
after the slash). Separately, read `games/game-log.md` and note the highest game
number in the table's `#` column. Do NOT look for game IDs in
`games/game-log.md` — it does not contain any.

STEP 2 — Find new games.
Query the Lichess API for my recent finished games, e.g.:
`curl -s -A "Mozilla/5.0" 'https://lichess.org/api/games/user/ThatoSM?max=30&rated=true&opening=true' -H 'Accept: application/x-ndjson'`
If more than 30 games might be missing (e.g. after a gap), increase `max` so
nothing is missed. If this endpoint errors or 404s transiently, retry once after
a short pause before giving up on this part — don't let it block Parts 2/3.
This returns one JSON object per line with fields including `id`, `status`,
`players.white`, `players.black`, `winner`, `createdAt`. Filter out anything not
finished (skip `status` of `started`/`aborted`/`created`/`noStart`).
Also skip any game where the `rated` field is `false`. Casual games are
practice games and must never enter the log, the PGN folder, or STATS.md.
Compare the
`id`s against the set from Step 1 — any ID not already present is new.

STEP 3 — Process each new game, oldest to newest (so numbering stays sequential).

For each new game ID:

(a) Export its PGN:
`curl -s -A "Mozilla/5.0" 'https://lichess.org/game/export/GAMEID?evals=true&clocks=false' -H 'Accept: application/x-chess-pgn'`
Also fetch the JSON form (`Accept: application/json`) and check the `moves`
field — if it is empty or has zero half-moves, SKIP this game entirely: do not
create a PGN file, a log entry, or an index row. Never log a game with no moves
played.

(b) Read the PGN headers: `[White "..."]`, `[Black "..."]`, `[Result "..."]`,
`[Termination "..."]`, `[WhiteElo "..."]`, `[BlackElo "..."]`. Determine my
colour: if the White tag matches ThatoSM (case-insensitive), I played White,
otherwise Black. The opponent is whichever username is NOT ThatoSM.
Also read `[UTCDate "..."]` and `[UTCTime "..."]`. Convert to Africa/Johannesburg
(UTC+2) — if adding 2 hours pushes past 23:59, roll the date forward one day.

(c) Assign the next sequential number: (highest game number from Step 1) + 1,
incrementing for each subsequent new game this run. Save the PGN to
`games/pgn/game-NN-opponentname.pgn` (NN zero-padded to 2 digits, opponent
username lowercased with non-alphanumeric characters replaced by hyphens) —
match the exact naming style of existing files in `games/pgn/`.

(d) Choose the destination detail file. Find the highest-numbered file in
`games/logs/`. If it already contains 40 `## Game` entries, create the next file
in sequence (`games-041-080.md`, then `games-081-120.md`, and so on) with this
header, and use it instead:

    # Games NNN–NNN — full entries

    Detail file. The scannable index is `games/game-log.md`.

    ---

When you create a new detail file, also append the PREVIOUS detail file's path
to `.repomixignore` on its own line (e.g. `games/logs/games-001-040.md`). This
keeps the packed bundle lean. Never add the current detail file.

(e) Prepend the full entry to the TOP of the entries in that detail file —
immediately after the header/`---` divider, before the current topmost
`## Game N` heading. Follow `docs/06-reading-an-analysis.md`: state my colour and
eval-sign direction FIRST. Use this structure:

    ## Game NN — RESULT · COLOUR (MyElo if present) vs Opponent (OpponentElo if present) · how it ended

    - Colour: I played [White/Black]. Eval direction: [positive/NEGATIVE] evals are my advantage.
    - Link: https://lichess.org/GAMEID
    - Played: YYYY-MM-DD HH:MM SAST
    - Mode: [Rated/Unrated] · [clock in minutes]+[increment in seconds]
    - Date: YYYY/MM/DD
    - PGN: `games/pgn/game-NN-opponentname.pgn`
    - Moves:
      ```
      <the full mainline movetext from the PGN, both players, all moves, one line>
      ```
    - Result: [from Termination tag / Result tag, in plain English]
    - **Me: [NOT YET ANALYSED] accuracy · blunders · mistakes · inaccuracies · ACPL.**
    - **Opponent: [NOT YET ANALYSED]**

    **Lesson — [DRAFT: needs review, no leak number assigned yet].**

    [DRAFT — fill in after reviewing the game with computer analysis.]

    **The ONE thing to fix:** [DRAFT — not yet determined]

    ---

(f) Add ONE row to the top of the table in `games/game-log.md`, immediately
below the `|---|---|---|---|---|---|` separator row:

    | NN | YYYY-MM-DD | RESULT | COLOUR | Opponent (Elo) | *pending* |

The Date column is the SAST date only (no time) — the same date computed in
step (b).

RESULT is WIN/LOSS/DRAW from MY perspective — derive correctly, don't guess.
Do NOT invent accuracy percentages, blunder counts, ACPL, or a leak number for a
brand-new game — that gets filled in later via Part 2 and by me. Do NOT edit
`docs/03-my-recurring-mistakes.md` or any "through-line" section — those require
real human analysis.

Mode and Date come straight from the PGN: read `[Event "..."]` (contains
"rated" or "casual" — Unrated for "casual", Rated for "rated"; for team-battle
or other events without that wording, fall back to whether `[WhiteRatingDiff
"..."]` is present) and `[TimeControl "SEC+INC"]` (SEC/60 minutes if evenly
divisible, else `SECs`, e.g. `600+5` → `10+5`). Date is the same
Africa/Johannesburg-converted date already used for `Played`, reformatted with
slashes (`YYYY/MM/DD`).

=== PART 2 — BACKFILL COMPUTER ANALYSIS ===

I regularly click 'Request Computer Analysis' on lichess.org after my games, but
it isn't instant, so entries often sit as drafts for a day or more before Lichess
finishes analysing them. Every night, re-check ALL existing draft entries across
ALL detail files, not just new ones.

STEP 1 — Search EVERY file in `games/logs/` for entries still containing the
literal text `[NOT YET ANALYSED]`. For each, extract its Lichess game ID from its
`Link:` line, and remember which file it lives in so you write the update back to
the right one.

STEP 2 — For each such game ID, query:
`curl -s -A "Mozilla/5.0" 'https://lichess.org/game/export/GAMEID?evals=true' -H 'Accept: application/json'`
and check whether the response's top-level `analysis` array is present AND
`players.white.analysis` / `players.black.analysis` objects are present (both
must exist — that means Lichess has finished analysing it). If not present yet,
skip this game and leave its placeholder untouched — do not fabricate numbers.

STEP 3 — For each game that IS now analysed, replace its placeholder block in its
own detail file with real data pulled directly from the JSON (never invent or
estimate anything):

- Determine my colour from `players.white.user.id`/`players.black.user.id`
  matching `thatosm` (case-insensitive).
- Read `players.<mycolor>.analysis` → `{inaccuracy, mistake, blunder, acpl}` and
  the same for the opponent's colour.
- Read `division.middle` and `division.end` (ply numbers) if present — convert
  ply to an approximate move number via `(ply+1)//2`.
- Walk the `analysis` array (index i = ply i, 0-indexed; i even = White's move,
  i odd = Black's move; move number = i//2 + 1). The `moves` field
  (space-separated SAN) gives the move played at each ply: `moves.split()[i]`.
  For any array entry containing a `judgment` key, record: move number, side
  (White/Black → map to Me/Opponent using my colour), the played move, the
  judgment name (Inaccuracy/Mistake/Blunder), the suggested best move (first word
  of the entry's `variation` field, already in SAN), and eval before→after
  (format `eval` as centipawns/100 with a sign, e.g. `181` → `+1.81`; format
  `mate` as `#N`; "before" is the previous array entry's eval/mate, or "start"
  for the first move).

Replace the placeholder lines (`- **Me: [NOT YET ANALYSED]...**` and
`- **Opponent: [NOT YET ANALYSED]**`) with:

    - **Me: N blunders · N mistakes · N inaccuracies · N ACPL.** (accuracy % isn't exposed by Lichess's API — read it off the Link above)
    - **Opponent: N blunders · N mistakes · N inaccuracies · N ACPL.**
    - Phases (Lichess division): opening ends ~move X, endgame starts ~move Y.

    **Computer analysis — flagged moves (from Lichess):**

    | Move | Side | Played | Eval before → after | Judgment | Best |
    |---|---|---|---|---|---|
    ... rows for every flagged move, both players, in move order ...

(Omit the Phases line if division data is missing. Omit the table entirely if
there are zero flagged moves.)

Do NOT touch the `**Lesson —` section, the leak number, `**The ONE thing to
fix:**`, or the row in `games/game-log.md` — those stay as human-review
placeholders. Do NOT touch `docs/`.

=== PART 3 — BACKFILL MY ELO INTO OLD HEADINGS ===

Older entries were logged before headings included my Elo, so their heading
still reads `## Game NN — RESULT · COLOUR vs Opponent (OpponentElo if
present) · how it ended` with nothing in parentheses after COLOUR.

STEP 1 — Search EVERY file in `games/logs/` for `## Game NN —` headings where
COLOUR (`White` or `Black`) is NOT immediately followed by `(`. Those are the
ones missing my Elo.

STEP 2 — For each such entry, read its own `- PGN:` line to find its local
PGN file (e.g. `games/pgn/game-NN-opponentname.pgn`) — no need to hit the
Lichess API, the file is already saved locally. Read that file's `[WhiteElo
"..."]` or `[BlackElo "..."]` tag, matching the colour stated in the entry's
`- Colour: I played [White/Black].` line.

STEP 3 — If that Elo tag has a real value (not empty or `?`), edit the
heading in place to insert it right after COLOUR, e.g. change `· White vs
Opponent (959) ·` to `· White (1523) vs Opponent (959) ·`. If the tag is
missing or `?`, leave that heading untouched. Don't touch anything else in
the entry.

=== PART 4 — REMOVE ZERO-MOVE GAMES ===

For every game currently logged in any `games/logs/` file (via its `Link:` game
ID), fetch the JSON export and check the `moves` field. If a game has zero moves
played, it should never have been logged. Remove all three traces of it:

1. Delete the entire `## Game N — ...` entry block from its detail file (from
   its heading down to and including the following `---` divider).
2. Delete its corresponding PGN file from `games/pgn/`.
3. Delete its row from the table in `games/game-log.md`.

Do NOT renumber the remaining games — just remove the bad entry and leave a gap
in the numbering. This should be rare; most nights there will be nothing to
remove here.

=== PART 5 — REGENERATE STATS.md ===

Run this every night. It is purely mechanical — never write interpretation,
narrative, or analysis into this file.

STEP 1 — Fetch both endpoints:
  curl -s -A "Mozilla/5.0" 'https://lichess.org/api/user/ThatoSM/perf/rapid'
  curl -s -A "Mozilla/5.0" 'https://lichess.org/api/user/ThatoSM'

If either errors or 404s, retry once after a short pause. If it still fails,
LEAVE THE EXISTING STATS.md UNTOUCHED and carry on — never write partial or
guessed values.

STEP 2 — Overwrite STATS.md at the repo root with exactly this shape, filling
every value from the JSON. Round ratings to whole numbers. Convert ISO
timestamps to plain dates. Convert stat.count.seconds to days and hours.

    # Lichess Stats — auto-generated

    > Generated by `routine-prompt.md`. Do not edit by hand — changes will be
    > overwritten. Interpretation lives in `docs/01-player-profile.md`.

    _Last generated: YYYY-MM-DD HH:MM UTC_

    ## Ratings
    | Perf | Rating | Games | Provisional |
    ... one row per entry in perfs, from /api/user/ThatoSM ...

    ## Rapid
    | Metric | Value |
    |---|---|
    | Rating | perf.glicko.rating |
    | Rating deviation | perf.glicko.deviation |
    | Progress (last 12) | perf.progress |
    | Rank | rank |
    | Percentile | percentile |
    | Highest | stat.highest.int (stat.highest.at) |
    | Lowest | stat.lowest.int (stat.lowest.at) |
    | Total games | stat.count.all (stat.count.rated rated) |
    | W / D / L | stat.count.win / draw / loss |
    | Average opponent | stat.count.opAvg |
    | Disconnects | stat.count.disconnects |
    | Time played | stat.count.seconds as Xd Yh |
    | Current win streak | stat.resultStreak.win.cur.v |
    | Longest win streak | stat.resultStreak.win.max.v (from → to dates) |
    | Current loss streak | stat.resultStreak.loss.cur.v |
    | Longest loss streak | stat.resultStreak.loss.max.v (from → to dates) |

    ## Logged coverage
    | Metric | Value |
    |---|---|
    | Rapid games played | perf.nb |
    | Games logged in this repo | <count of ## Game entries across games/logs/> |
    | Coverage | percentage |

STEP 3 — Compute the colour split by reading the table in games/game-log.md
ONLY. Count WIN/LOSS/DRAW per colour and append:

    ## Results by colour (logged games only)
    | Colour | W–L–D | Score |

Do NOT compute this from the Lichess API — the API doesn't expose my colour
cheaply, and game-log.md is the authoritative record here.

HARD LIMITS ON THIS PART:
- STATS.md is the ONLY file you may write in Part 5.
- Never edit README.md, docs/, training/, or any file in games/.
- Never write a sentence of analysis, a leak number, or a "what this means"
  line into STATS.md. Numbers and tables only.
- If a field is missing from the JSON, write "—". Never estimate.

=== COMMIT AND PUSH ===

If you made ANY changes (new games, backfilled analysis, backfilled old
headings with my Elo, and/or removed zero-move games): stage everything
changed, commit with a clear message describing what happened, and push
straight to `origin main`. Never open a pull request, never push to a side
branch. If nothing changed at all, skip committing entirely.

After committing and pushing, run `npx repomix` in the repo root.
