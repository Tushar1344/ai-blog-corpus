#!/usr/bin/env python3
"""Enrich OpenAI CSV by fetching each post page and extracting title, publish date, authors."""
import csv
import re
import time
import json
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from html import unescape

UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
DATA = Path(__file__).parent

def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return None

def extract_meta(html):
    if not html:
        return ("", "", "")
    title = ""
    date = ""
    authors = ""

    m = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)', html)
    if m:
        title = unescape(m.group(1)).strip()
    else:
        m = re.search(r'<title>([^<]+)</title>', html)
        if m:
            title = unescape(m.group(1)).strip()
    title = re.sub(r'\s*\|\s*OpenAI\s*$', '', title)

    m = re.search(r'<meta[^>]+property=["\']article:published_time["\'][^>]+content=["\']([^"\']+)', html)
    if m:
        date = m.group(1)[:10]
    else:
        # Fallback: JSON-LD
        for m in re.finditer(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>([^<]+)</script>', html, re.DOTALL):
            try:
                data = json.loads(m.group(1).strip())
                if isinstance(data, list):
                    for d in data:
                        if d.get("datePublished"):
                            date = d["datePublished"][:10]
                            break
                elif isinstance(data, dict):
                    if data.get("datePublished"):
                        date = data["datePublished"][:10]
                    elif data.get("@graph"):
                        for d in data["@graph"]:
                            if isinstance(d, dict) and d.get("datePublished"):
                                date = d["datePublished"][:10]
                                break
                if date:
                    break
            except Exception:
                continue

    # Authors: JSON-LD often has this
    if not authors:
        for m in re.finditer(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>([^<]+)</script>', html, re.DOTALL):
            try:
                data = json.loads(m.group(1).strip())
                blocks = data if isinstance(data, list) else [data]
                for d in blocks:
                    if isinstance(d, dict):
                        if d.get("@graph"):
                            blocks.extend(d["@graph"])
                        auth = d.get("author")
                        if auth:
                            if isinstance(auth, list):
                                names = [a.get("name", "") if isinstance(a, dict) else str(a) for a in auth]
                            elif isinstance(auth, dict):
                                names = [auth.get("name", "")]
                            else:
                                names = [str(auth)]
                            authors = "|".join(n for n in names if n)
                            if authors:
                                break
                if authors:
                    break
            except Exception:
                continue

    # Meta author fallback
    if not authors:
        m = re.search(r'<meta[^>]+name=["\']author["\'][^>]+content=["\']([^"\']+)', html)
        if m:
            authors = m.group(1).strip()

    return (title, date, authors)

def enrich_one(row):
    html = fetch(row["url"])
    title, date, authors = extract_meta(html)
    if title:
        row["title"] = title
    if date:
        row["publish_date"] = date
    if authors:
        row["authors"] = authors
    return row

def main():
    in_path = DATA / "enum-openai.csv"
    rows = list(csv.DictReader(open(in_path)))
    print(f"Enriching {len(rows)} OpenAI rows with 10 concurrent workers...")

    with ThreadPoolExecutor(max_workers=10) as ex:
        futures = {ex.submit(enrich_one, r): r for r in rows}
        enriched = []
        done = 0
        for f in as_completed(futures):
            try:
                enriched.append(f.result())
            except Exception as e:
                enriched.append(futures[f])
            done += 1
            if done % 20 == 0:
                print(f"  {done}/{len(rows)}")

    # Write back
    # Preserve original order by id
    order = {r["id"]: i for i, r in enumerate(rows)}
    enriched.sort(key=lambda r: order.get(r["id"], 9999))

    fieldnames = ["id", "company", "track", "title", "url", "publish_date", "authors", "in_scope", "scope_reason"]
    with open(in_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(enriched)

    # Report
    with_title = sum(1 for r in enriched if r.get("title"))
    with_date = sum(1 for r in enriched if r.get("publish_date"))
    with_authors = sum(1 for r in enriched if r.get("authors"))
    dates = [r["publish_date"] for r in enriched if r["publish_date"]]
    print(f"\nResults:")
    print(f"  total: {len(enriched)}")
    print(f"  with title: {with_title}")
    print(f"  with date: {with_date}")
    print(f"  with authors: {with_authors}")
    if dates:
        print(f"  date range: {min(dates)} → {max(dates)}")

if __name__ == "__main__":
    main()
