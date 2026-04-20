#!/usr/bin/env python3
"""Enrich missing publish_date via Wayback Machine + CDX timestamp extraction."""
import csv
import re
import urllib.request
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

DATA = Path(__file__).parent
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", errors="ignore")
    except Exception:
        return None

def extract_date(html):
    if not html:
        return ""
    # og:article:published_time
    m = re.search(r'article:published_time["\']\s+content=["\']([^"\']+)', html)
    if m:
        return m.group(1)[:10]
    # meta itemprop datePublished
    m = re.search(r'itemprop=["\']datePublished["\']\s+content=["\']([^"\']+)', html)
    if m:
        return m.group(1)[:10]
    # <time datetime=...>
    m = re.search(r'<time[^>]+datetime=["\'](\d{4}-\d{2}-\d{2})', html)
    if m:
        return m.group(1)
    # JSON-LD datePublished
    for m in re.finditer(r'"datePublished"\s*:\s*"([^"]+)"', html):
        return m.group(1)[:10]
    return ""

def get_first_wayback_ts(url):
    """Use CDX API to get earliest snapshot timestamp."""
    cdx = f"https://web.archive.org/cdx/search/cdx?url={urllib.parse.quote(url, safe='')}&limit=1&output=json&filter=statuscode:200"
    try:
        data = json.loads(fetch(cdx) or "[]")
        if data and len(data) > 1:
            ts = data[1][1]  # second row, column 1 = timestamp
            return f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}"
    except Exception:
        pass
    return ""

def enrich_one(row):
    url = row["url"]
    # Try Wayback 2024/2025/2026 snapshots
    for yr in ("2025", "2024", "2026", "2023"):
        html = fetch(f"https://web.archive.org/web/{yr}/{url}")
        date = extract_date(html)
        if date:
            return (row["id"], date)
    # Try CDX earliest snapshot
    import urllib.parse
    date = get_first_wayback_ts(url)
    if date:
        return (row["id"], date)
    return (row["id"], "")

def main():
    path = DATA / "master.csv"
    rows = list(csv.DictReader(open(path)))
    missing = [r for r in rows if r.get("in_scope") == "TRUE" and r.get("dropped_in_v2") == "FALSE" and not r.get("publish_date")]
    print(f"Missing dates: {len(missing)}")

    results = {}
    with ThreadPoolExecutor(max_workers=12) as ex:
        futures = {ex.submit(enrich_one, r): r for r in missing}
        done = 0
        for f in as_completed(futures):
            try:
                rid, d = f.result()
                if d:
                    results[rid] = d
            except Exception:
                pass
            done += 1
            if done % 30 == 0:
                print(f"  {done}/{len(missing)} | found so far: {len(results)}")

    print(f"\nFound dates for {len(results)}/{len(missing)} missing")

    # Merge back
    for r in rows:
        if r["id"] in results:
            r["publish_date"] = results[r["id"]]
            r["year"] = results[r["id"]][:4]

    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)
    print("Wrote master.csv")

if __name__ == "__main__":
    import urllib.parse  # needed for get_first_wayback_ts
    main()
