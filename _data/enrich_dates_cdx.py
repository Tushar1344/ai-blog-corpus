#!/usr/bin/env python3
"""Get approximate publish_date via earliest Wayback CDX snapshot per URL.
The earliest archive date is usually within days-weeks of publication."""
import csv
import json
import urllib.request
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

DATA = Path(__file__).parent
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", errors="ignore")
    except Exception:
        return None

def earliest_snapshot(url):
    # sorted by timestamp, limit 1, earliest first
    encoded = urllib.parse.quote(url, safe='')
    cdx_url = f"https://web.archive.org/cdx/search/cdx?url={encoded}&output=json&limit=1&filter=statuscode:200"
    text = fetch(cdx_url)
    if not text:
        return ""
    try:
        data = json.loads(text)
        if len(data) > 1:
            ts = data[1][1]  # YYYYMMDDhhmmss
            if len(ts) >= 8:
                return f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}"
    except Exception:
        return ""
    return ""

def main():
    path = DATA / "master.csv"
    rows = list(csv.DictReader(open(path)))
    missing = [r for r in rows if r.get("in_scope") == "TRUE" and r.get("dropped_in_v2") == "FALSE" and not r.get("publish_date")]
    print(f"Missing dates: {len(missing)}")

    results = {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        futures = {ex.submit(earliest_snapshot, r["url"]): r for r in missing}
        done = 0
        for f in as_completed(futures):
            try:
                d = f.result()
                if d:
                    results[futures[f]["id"]] = d
            except Exception:
                pass
            done += 1
            if done % 30 == 0:
                print(f"  {done}/{len(missing)} | found: {len(results)}")

    print(f"\nFound approx publish dates for {len(results)}/{len(missing)} (via earliest Wayback snapshot)")

    for r in rows:
        if r["id"] in results:
            r["publish_date"] = results[r["id"]]
            r["year"] = results[r["id"]][:4]
            # Note: this is an approximation
            notes = r.get("notes", "")
            r["notes"] = (notes + "; " if notes else "") + "date-from-wayback-cdx-approx"

    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)
    print("Wrote master.csv")

if __name__ == "__main__":
    main()
