import json, time, urllib.request, urllib.parse, urllib.error
from datetime import datetime, timezone, timedelta

SAST = timezone(timedelta(hours=2))
params = urllib.parse.urlencode({
    "perfType": "rapid", "rated": "true", "analysed": "true",
    "evals": "true", "accuracy": "true", "max": 400
})
url = f"https://lichess.org/api/games/user/ThatoSM?{params}"
req = urllib.request.Request(url, headers={
    "Accept": "application/x-ndjson",
    "User-Agent": "chess-coach-late-night-check"
})

def fetch():
    for attempt in range(4):
        try:
            return urllib.request.urlopen(req).read().decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code == 429:
                wait = 60 * (attempt + 1)
                print(f"Rate limited. Waiting {wait}s, then retrying...")
                time.sleep(wait)
                continue
            raise
    raise SystemExit("Still rate limited after several tries. Try again later.")

body = fetch()

early, late, skipped, total = [], [], 0, 0
for raw in body.splitlines():
    raw = raw.strip()
    if not raw:
        continue
    g = json.loads(raw)
    if "players" not in g:
        print("Unexpected response from Lichess:", g)
        raise SystemExit(1)
    total += 1
    white = g["players"]["white"].get("user", {}).get("name", "").lower()
    me = "white" if white == "thatosm" else "black"
    acpl = g["players"][me].get("analysis", {}).get("acpl")
    if acpl is None:
        skipped += 1
        continue
    hour = datetime.fromtimestamp(g["createdAt"] / 1000, SAST).hour
    (late if (hour >= 21 or hour < 3) else early).append(acpl)

def report(name, xs):
    print(f"{name}: n={len(xs)}  mean ACPL={sum(xs)/len(xs):.1f}" if xs else f"{name}: n=0")

print(f"Games returned: {total}  (no analysis, skipped: {skipped})")
report("Before 21:00", early)
report("21:00-03:00", late)