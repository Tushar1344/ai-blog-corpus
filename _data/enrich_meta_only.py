#!/usr/bin/env python3
"""Single-threaded date enrichment with broader year range + retry for stubborn URLs."""
import csv
import time
from pathlib import Path
from enrich_dates_robust import fetch, extract_date

DATA = Path(__file__).parent

def get_date_broader(url):
    """Broader retry with many years; pick earliest valid extracted date."""
    candidates = []
    years = ("2020", "2021", "2022", "2023", "2024", "2019", "2018")
    for yr in years:
        wb = f"https://web.archive.org/web/{yr}/{url}"
        html = fetch(wb)
        if not html or len(html) < 10000:
            continue
        date = extract_date(html)
        if date:
            # Filter out stub dates (2026 footer only)
            if date >= "2026-01":
                continue
            candidates.append(date)
        time.sleep(0.3)
    if candidates:
        return min(candidates)
    return ""

def main():
    path = DATA / "master.csv"
    rows = list(csv.DictReader(open(path)))
    missing = [r for r in rows if r.get("in_scope") == "TRUE" and r.get("dropped_in_v2") == "FALSE"
               and not r.get("publish_date")]
    print(f"Missing dates (all companies): {len(missing)}")

    results = {}
    for i, r in enumerate(missing):
        try:
            date = get_date_broader(r["url"])
            if date:
                results[r["id"]] = date
        except Exception:
            pass
        if (i + 1) % 10 == 0:
            print(f"  {i+1}/{len(missing)} | found: {len(results)}")
        time.sleep(0.5)

    print(f"\nRecovered {len(results)}/{len(missing)} Meta dates")

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
    main()
