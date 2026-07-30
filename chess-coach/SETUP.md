# Setup Guide

Two things to do with this repo:

- **Part A** — turn it into a Claude Project (do this first, it's the useful bit)
- **Part B** — put it on GitHub via VS Code, from scratch

Both are written first-timer style. Nothing is assumed.

---

## Part A — Create the Claude Project

1. Go to **claude.ai** and sign in.
2. In the left sidebar, click **Projects**.
3. Click **Create project** (top right).
4. Name it **"Chess Coach — Thato"**. Add a short description, e.g.
   "Coaching system, recurring leaks, and game log for ThatoSM (Lichess)."
5. Open the new project. Find the **project knowledge** / **project files**
   area — usually a panel on the right or an **Add content** button.
6. Upload every `.md` file from this repo: `README.md`, `SETUP.md`, everything
   in `docs/`, `games/`, and `training/`. You can select them all and drag them
   in at once. (Skip `.gitignore` and the `games/pgn/` folder — those are for
   GitHub, not for Claude.)
7. In the project's **custom instructions** box, paste this:

   > You are my chess coach. Before analysing any game I paste, read
   > `docs/06-reading-an-analysis.md` and confirm which colour I played and
   > which way the eval sign runs — this has been misread twice, so do it
   > every time. Then read `docs/03-my-recurring-mistakes.md` and
   > `docs/05-coaching-principles.md`. Name which numbered leak the game shows.
   > Read the accuracy and phase numbers before commenting on individual moves.
   > Be honest — don't congratulate a win that contained the same blunders as
   > my losses, and don't invent a struggle that didn't happen. End with ONE
   > thing to fix, not five.

8. Done. Every new chat inside that project now starts knowing my chess.

**Important:** the Claude Project's uploaded files and my chat memory are
separate systems. This repo is the portable, version-controlled source of
truth; the Project is a **snapshot** of it. **When I update these files, I must
re-upload them** or the Project keeps coaching me off an old story.

---

## Part B — Create the Git repo and push to GitHub (from scratch)

### One-time prerequisites

1. Install **Git**: https://git-scm.com/downloads — accept all the defaults.
2. Install **VS Code**: https://code.visualstudio.com
3. Create a **GitHub account** if I don't have one: https://github.com
4. Restart VS Code after installing Git, so it can find it.

### Tell Git who I am (once, ever)

Open VS Code, then open the terminal with **Ctrl + `** (the backtick key, top
left of the keyboard, under Escape). Type these two lines, pressing Enter after
each. Use my real name and the email on my GitHub account:

```powershell
git config --global user.name "Thato"
git config --global user.email "my-github-email@example.com"
```

Nothing will appear to happen. That's correct — it worked.

### Create the repo

1. In VS Code: **File → Open Folder** → select the `chess-coach` folder.
2. Open the **Source Control** panel: click the branch-shaped icon in the far
   left bar, or press **Ctrl + Shift + G**.
3. Click the **Initialize Repository** button. VS Code now lists every file in
   the folder as a change.
4. In the message box at the top of that panel, type:
   `Initial chess coaching system`
5. Click the **✓ Commit** button.
6. If it asks "Would you like to stage all your changes and commit them
   directly?" — click **Yes**.
7. Click **Publish Branch** (it may say **Publish to GitHub**).
8. VS Code opens a browser window asking me to **sign in to GitHub**. Sign in
   and click **Authorize**.
9. VS Code asks whether to publish as **private** or **public**. Choose
   **private** unless I specifically want this public.
10. Confirm the repo name (`chess-coach` is fine). VS Code pushes everything up.

The repo is now on GitHub. Refresh github.com to see it.

### Pushing future changes (every time I update a file)

1. Save the file (**Ctrl + S**).
2. Source Control panel (**Ctrl + Shift + G**).
3. Type a short commit message describing what changed, e.g.
   `Add Game 9 vs <opponent>`.
4. Click **✓ Commit**, then **Yes** if it asks to stage everything.
5. Click **Sync Changes** (the circular-arrows icon) to push to GitHub.
6. **Then re-upload the changed files to the Claude Project** (Part A, step 6).
   Git and Claude do not talk to each other. This step is easy to forget and
   it's the one that matters for coaching.

### The command-line equivalent (if I prefer the terminal)

From inside the folder, in VS Code's terminal (**Ctrl + `**):

```powershell
git add .
git commit -m "Update coaching files"
git push
```

The very first time only, if the repo isn't linked to GitHub yet:

```powershell
git init
git add .
git commit -m "Initial chess coaching system"
git branch -M main
git remote add origin https://github.com/<my-username>/chess-coach.git
git push -u origin main
```

---

## Security note

**Never paste a password, personal access token, or API key into a chat with
Claude.** Enter credentials only in GitHub's own sign-in window or VS Code's
own prompt. If I ever paste a token by accident, go to GitHub →
**Settings → Developer settings → Personal access tokens** and delete it
immediately.
