import requests, json
from datetime import datetime, timezone, timedelta

SAST = timezone(timedelta(hours=2))
url = "https://lichess.org/api/games/user/ThatoSM"
params = {"perfType": "rapid", "rated": "true", "analysed": "true",
          "evals": "true", "accuracy": "true", "max": 400}
r = requests.get(url, params=params,
                 headers={"Accept": "application/x-ndjson"}, stream=True)

early, late = [], []
for line in r.iter_lines():
    if not line:
        continue
    g = json.loads(line)
    me = "white" if g["players"]["white"].get("user", {}).get("name","").lower() == "thatosm" else "black"
    acpl = g["players"][me].get("analysis", {}).get("acpl")
    if acpl is None:
        continue
    hour = datetime.fromtimestamp(g["createdAt"]/1000, SAST).hour
    (late if (hour >= 21 or hour < 3) else early).append(acpl)

def report(name, xs):
    print(f"{name}: n={len(xs)}  mean ACPL={sum(xs)/len(xs):.1f}" if xs else f"{name}: n=0")

report("Before 21:00", early)
report("21:00-03:00", late)