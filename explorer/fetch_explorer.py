"""Fetch what real Lichess rapid players (1000-1599) play in each drill position.
Reads positions.txt, writes explorer.json. Safe to stop and re-run: it resumes."""
import json, os, time
import requests

TOKEN = os.environ["LICHESS_TOKEN"]
URL = "https://explorer.lichess.ovh/lichess"
PARAMS = {"variant": "standard", "speeds": "rapid", "ratings": "1000,1200,1400", "moves": 12, "topGames": 0, "recentGames": 0}

fens = [l.strip() for l in open("positions.txt", encoding="utf-8") if l.strip()]
out = json.load(open("explorer.json", encoding="utf-8")) if os.path.exists("explorer.json") else {}
todo = [f for f in fens if f not in out]
print(f"{len(out)} done, {len(todo)} to go (about {len(todo) // 60} minutes)")

s = requests.Session()
s.headers["Authorization"] = f"Bearer {TOKEN}"
for i, fen in enumerate(todo, 1):
    while True:
        r = s.get(URL, params={**PARAMS, "fen": fen}, timeout=30)
        if r.status_code == 429:
            print("Rate limited - waiting 60 seconds...")
            time.sleep(60)
            continue
        r.raise_for_status()
        break
    d = r.json()
    out[fen] = {"total": d["white"] + d["draws"] + d["black"],
                "moves": [[m["san"], m["white"] + m["draws"] + m["black"]] for m in d["moves"]]}
    if i % 25 == 0 or i == len(todo):
        with open("explorer.json", "w", encoding="utf-8") as f:
            json.dump(out, f)
        print(f"{i}/{len(todo)} saved")
    time.sleep(1)
print("DONE - send explorer.json to Claude")
