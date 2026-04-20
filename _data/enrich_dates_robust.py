#!/usr/bin/env python3
"""Robust date enrichment — multi-source extraction: meta tags, JSON-LD, <time>, then text dates."""
import csv
import re
import json
import urllib.parse
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from datetime import datetime

DATA = Path(__file__).parent
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

MONTHS = {
    "jan": 1, "january": 1, "feb": 2, "february": 2, "mar": 3, "march": 3,
    "apr": 4, "april": 4, "may": 5, "jun": 6, "june": 6, "jul": 7, "july": 7,
    "aug": 8, "august": 8, "sep": 9, "sept": 9, "september": 9, "oct": 10, "october": 10,
    "nov": 11, "november": 11, "dec": 12, "december": 12,
}

def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", errors="ignore")
    except Exception:
        return None

def cdx_earliest(url, status="200"):
    """Get earliest Wayback snapshot timestamp for a URL."""
    encoded = urllib.parse.quote(url, safe='')
    cdx = f"https://web.archive.org/cdx/search/cdx?url={encoded}&output=json&limit=1&filter=statuscode:{status}"
    text = fetch(cdx)
    if not text:
        return None
    try:
        data = json.loads(text)
        if len(data) > 1:
            return data[1][1]  # YYYYMMDDhhmmss
    except Exception:
        pass
    return None

def extract_date(html):
    if not html:
        return ""

    # 1. OpenGraph / article meta
    m = re.search(r'property=["\']article:published_time["\']\s+content=["\']([^"\']+)', html)
    if m:
        return m.group(1)[:10]
    m = re.search(r'content=["\']([^"\']+)["\']\s+property=["\']article:published_time', html)
    if m:
        return m.group(1)[:10]

    # 2. Meta datePublished / publishedTime
    m = re.search(r'(?:itemprop|name|property)=["\'](?:datePublished|publishedTime|publish_date|pubdate)["\'][^>]+content=["\']([^"\']+)', html, re.I)
    if m:
        return m.group(1)[:10]

    # 3. JSON-LD datePublished
    for m in re.finditer(r'"datePublished"\s*:\s*"([^"]+)"', html):
        return m.group(1)[:10]

    # 4. <time datetime=...>
    m = re.search(r'<time[^>]+datetime=["\'](\d{4}-\d{2}-\d{2})', html)
    if m:
        return m.group(1)

    # 5. Find H1, then earliest date AFTER it within 80KB window
    h1_pos = 0
    m1 = re.search(r'<h1\b', html)
    if m1:
        h1_pos = m1.start()
    window = html[h1_pos:h1_pos + 80000] if h1_pos else html[:80000]

    # "Published on Oct 17, 2023" / "March 14, 2023"
    m = re.search(r'(?:Published(?:\s+on)?|Posted(?:\s+on)?|Date[^a-z])[^<>]{0,30}?(' +
                  r'Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]{0,8}\s+(\d{1,2}),?\s+(\d{4})',
                  window, re.I)
    if m:
        mo, day, yr = m.group(1), int(m.group(2)), int(m.group(3))
        if 2010 <= yr <= 2027:
            mn = MONTHS[mo.lower()[:3]]
            return f"{yr:04d}-{mn:02d}-{day:02d}"

    # 6. First "Month DD, YYYY" in window after H1
    m = re.search(r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+(\d{1,2}),?\s+(\d{4})\b',
                  window, re.I)
    if m:
        mo, day, yr = m.group(1), int(m.group(2)), int(m.group(3))
        if 2010 <= yr <= 2027:
            mn = MONTHS[mo.lower()[:3]]
            return f"{yr:04d}-{mn:02d}-{day:02d}"

    # 7. DD Month YYYY format
    m = re.search(r'\b(\d{1,2})\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})\b', window, re.I)
    if m:
        day = int(m.group(1)); mo = m.group(2).lower(); yr = int(m.group(3))
        if 2010 <= yr <= 2027:
            mn = MONTHS[mo[:3]]
            return f"{yr:04d}-{mn:02d}-{day:02d}"

    return ""

def get_date_for_url(original_url):
    """Try multiple strategies to get a publish date for a URL."""
    # Strategy 1: direct fetch first (when it works, usually best quality)
    html = fetch(original_url)
    if html and len(html) > 5000:
        date = extract_date(html)
        if date:
            return date, "direct"

    # Strategy 2: Wayback fetch. Prefer substantial HTML (>10KB).
    # Try multiple years, keep the EARLIEST date extracted (likely the real publish date)
    candidates = []
    for yr in ("2023", "2024", "2022", "2025", "2021"):
        wb = f"https://web.archive.org/web/{yr}/{original_url}"
        html = fetch(wb)
        if not html or len(html) < 10000:
            continue
        date = extract_date(html)
        if date:
            candidates.append((date, f"wayback-extract-{yr}"))

    if candidates:
        # Pick the earliest date among candidates (most likely the real publish date)
        candidates.sort()
        return candidates[0]

    # Strategy 3: CDX earliest snapshot (as approx publish date)
    ts = cdx_earliest(original_url)
    if ts and len(ts) >= 8:
        return f"{ts[:4]}-{ts[4:6]}-{ts[6:8]}", "cdx-earliest"

    return "", ""

def main():
    path = DATA / "master.csv"
    rows = list(csv.DictReader(open(path)))
    missing = [r for r in rows if r.get("in_scope") == "TRUE" and r.get("dropped_in_v2") == "FALSE" and not r.get("publish_date")]
    print(f"Missing dates: {len(missing)}")

    results = {}
    methods = {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        futures = {ex.submit(get_date_for_url, r["url"]): r for r in missing}
        done = 0
        for f in as_completed(futures):
            row = futures[f]
            try:
                date, method = f.result()
                if date:
                    results[row["id"]] = date
                    methods[row["id"]] = method
            except Exception as e:
                pass
            done += 1
            if done % 30 == 0:
                print(f"  {done}/{len(missing)} | found: {len(results)}")

    print(f"\nRecovered {len(results)}/{len(missing)} ({100*len(results)//len(missing) if missing else 0}%)")
    # By method breakdown
    from collections import Counter
    method_counts = Counter(methods.values())
    for k, v in method_counts.most_common():
        print(f"  {k:25} {v}")

    # Merge into master.csv
    for r in rows:
        if r["id"] in results:
            r["publish_date"] = results[r["id"]]
            r["year"] = results[r["id"]][:4]

    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)
    print("Wrote master.csv")

    # Report by company
    coverage = Counter()
    for r in rows:
        if r.get("in_scope") == "TRUE" and r.get("dropped_in_v2") == "FALSE":
            if r["publish_date"]:
                coverage[("with", r["company"])] += 1
            else:
                coverage[("without", r["company"])] += 1
    cos = sorted(set(c for _, c in coverage))
    print("\nBy company (with date / missing):")
    for co in cos:
        w = coverage.get(("with", co), 0)
        wo = coverage.get(("without", co), 0)
        total = w + wo
        pct = 100 * w // total if total else 0
        print(f"  {co:25} {w}/{total} ({pct}%)")

if __name__ == "__main__":
    main()
