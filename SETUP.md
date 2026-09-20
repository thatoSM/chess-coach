# Setup Guide

Written first-timer style, for Windows PowerShell in VS Code. The repo lives
at `C:\Users\Ryzen 5 PC\projects\chess-coach`.

- **Part A** — the Claude Project
- **Part B** — committing and pushing
- **Part C** — Python and Stockfish, for the scripts (once)
- **Part D** — re-running the Leak #1 scan (every ~50 games)
- **Part E** — the daily loop
- **Part F** — the nightly routine

---

## Part A — The Claude Project

The Project is called **Chess**. Its knowledge is one file:
`repomix-output.xml`, a packed copy of this repo.

**Custom instructions** (Project → Instructions), paste exactly:

> You are my chess coach. Before analysing any game I paste, read
> `docs/06-reading-an-analysis.md` and confirm which colour I played and
> which way the eval sign runs — this has been misread twice, so do it
> every time. Then read `docs/03-my-recurring-mistakes.md` and
> `docs/05-coaching-principles.md`. Name which numbered leak the game shows.
> Read the accuracy and phase numbers before commenting on individual moves.
> Be honest — don't congratulate a win that contained the same blunders as
> my losses, and don't invent a struggle that didn't happen. End with ONE
> thing to fix, not five.

**Refreshing the Project after any change** (this is the step that actually
affects coaching — Git and Claude don't talk to each other):

1. In VS Code, open the terminal: **Ctrl + `** (backtick, under Escape).
2. Make sure you're in the repo:
   ```powershell
   cd "C:\Users\Ryzen 5 PC\projects\chess-coach"
   ```
3. Rebuild the bundle:
   ```powershell
   npx repomix
   ```
   It prints a summary and writes `repomix-output.xml` in the repo folder.
4. On claude.ai, open the **Chess** Project → Project knowledge.
5. Delete the old `repomix-output.xml` (the **⋯** or bin icon on the file).
6. Drag the new `repomix-output.xml` from File Explorer into the knowledge
   panel.

---

## Part B — Committing and pushing

After any change:

```powershell
cd "C:\Users\Ryzen 5 PC\projects\chess-coach"
git pull
git add .
git commit -m "Describe what changed"
git push
```

- `git pull` first, because the nightly routine pushes from the cloud. If you
  skip it, `git push` is rejected with "Updates were rejected"; run
  `git pull`, then `git push` again.
- Commit messages describe the change. **No dates or day numbers in them.**

---

## Part C — Python and Stockfish (once)

### C1. Python

1. Check Python is installed:
   ```powershell
   python --version
   ```
   Anything 3.10 or newer is fine. If it says "not recognized", install it
   from https://www.python.org/downloads/ and **tick "Add python.exe to
   PATH"** on the first installer screen, then close and reopen VS Code.
2. Create the virtual environment in the repo (once):
   ```powershell
   cd "C:\Users\Ryzen 5 PC\projects\chess-coach"
   python -m venv venv
   ```
3. Activate it (every new terminal):
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   The prompt now starts with `(venv)`. If PowerShell says running scripts
   is disabled, run this once, answer **Y**, then activate again:
   ```powershell
   Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
   ```
4. Install the chess library:
   ```powershell
   pip install chess
   ```

`venv/` is in `.gitignore`, so it never gets committed.

### C2. Stockfish

1. Go to https://stockfishchess.org/download/ → **Windows**.
2. Download the **x86-64-avx2** build (right for a Ryzen 5).
3. Open the downloaded `.zip` → **Extract all** → extract to `C:\tools\`.
4. In File Explorer, open `C:\tools\stockfish\` and find the `.exe` (named
   like `stockfish-windows-x86-64-avx2.exe`). Right-click it → **Copy as
   path**. That quoted path is your `--stockfish` value below.

---

## Part D — Re-running the Leak #1 scan (every ~50 games)

1. Open the terminal, go to the repo, activate the venv:
   ```powershell
   cd "C:\Users\Ryzen 5 PC\projects\chess-coach"
   .\venv\Scripts\Activate.ps1
   ```
2. Run the scan (paste your own Stockfish path from C2):
   ```powershell
   python scripts/leak-scan.py --stockfish "C:\tools\stockfish\stockfish-windows-x86-64-avx2.exe"
   ```
   It prints progress every 50 games and takes a few minutes. It overwrites
   the four files in `games/leak-scan/`.
3. Preview the Leak column update, then apply it:
   ```powershell
   python scripts/apply-leak-column.py --dry-run
   python scripts/apply-leak-column.py
   ```
   Only `*pending*` cells change. My own labels are never touched.
4. Open `games/leak-scan/leak-by-game.md`. Copy the Headline numbers into
   the **Trend** table in `docs/03-my-recurring-mistakes.md` as a new row.
5. Commit and push (Part B), then refresh the Project (Part A).

Opening results, any time:
```powershell
python scripts/opening-results.py --since 2026-09-15 --family Caro-Kann
```

---

## Part E — The daily loop

1. Play, with the board card open (`training/board-card.md`).
2. After each game: review with the local engine and log the human fields
   (`training/post-game-review.md`).
3. The nightly routine syncs games, fills in the Lichess numbers, commits
   and pushes.
4. Next session: `git pull`, then refresh the Project (Part A) before asking
   Claude about recent games.

---

## Part F — The nightly routine

- Runs as a Claude Code scheduled routine (trigger
  `trig_01GXQNmE1LNhre48LCwwiGSs`), 19:00 UTC / 21:00 SAST.
- Its instructions are `routine-prompt.md`. It edits only `games/` (not
  `games/leak-scan/`), `STATS.md` and `.repomixignore`.
- To check it's still running:
  ```powershell
  git pull
  git log -5 --oneline
  ```
  Recent commits from the routine should appear. If the newest routine
  commit is days old, open Claude Code and check the routine.

---

## Security note

Never paste a password, personal access token or API key into a chat with
Claude. If one leaks, delete it at GitHub → **Settings → Developer settings
→ Personal access tokens**.
