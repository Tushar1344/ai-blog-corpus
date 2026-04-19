#!/usr/bin/env python3
"""Enrich OpenAI CSV via Wayback Machine (bypasses Cloudflare)."""
import csv
import re
import time
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
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return None

def title_from_slug(slug):
    return " ".join(w.capitalize() for w in slug.split("-"))

def extract_meta(html, post_url):
    if not html:
        return ("", "", "")
    title = ""
    date = ""
    authors = ""

    # Title - prefer og:title, then <title>
    m = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)', html)
    if m:
        title = unescape(m.group(1)).strip()
    else:
        m = re.search(r'<title>([^<]+)</title>', html)
        if m:
            title = unescape(m.group(1)).strip()
    title = re.sub(r'\s*\|\s*OpenAI\s*$', '', title)
    # Wayback adds prefix like "Internet Archive" — strip it
    title = re.sub(r'^(Wayback Machine|Internet Archive)\s*[-|]\s*', '', title)

    # Publish date — first <time datetime="YYYY-MM-DD"> on the page after <main> or near <h1>
    # Strategy: find the <h1> containing the post title, then nearest <time> AFTER it
    # Fallback: the first <time datetime> on the page
    slug = post_url.rstrip("/").split("/")[-1]

    # Try to find h1-associated time
    m = re.search(r'<h1[^>]*>(.*?)</h1>(.*?)<time[^>]+datetime=["\']([^"\']+)', html, re.DOTALL)
    if m:
        date = m.group(3)[:10]
    else:
        # Try published_time meta
        m = re.search(r'article:published_time["\']\s+content=["\']([^"\']+)', html)
        if m:
            date = m.group(1)[:10]
        else:
            # Fallback: first time element
            m = re.search(r'<time[^>]+datetime=["\']([^"\']+)', html)
            if m:
                date = m.group(1)[:10]

    return (title, date, authors)

def enrich_one(row):
    url = row["url"]
    # Hit Wayback with a year that predates now — "2025" picks the latest snapshot from that year
    wb_url = f"https://web.archive.org/web/2025/{url}"
    html = fetch(wb_url)
    if not html or len(html) < 5000:
        # Retry with different year
        wb_url = f"https://web.archive.org/web/2024/{url}"
        html = fetch(wb_url)
    if not html or len(html) < 5000:
        # Last resort: fall back to direct with UA
        html = fetch(url)
    title, date, authors = extract_meta(html, url)
    # Always ensure title — fallback to slug
    if not title:
        slug = url.rstrip("/").split("/")[-1]
        title = title_from_slug(slug)
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
    print(f"Enriching {len(rows)} OpenAI rows via Wayback with 8 concurrent workers...")

    with ThreadPoolExecutor(max_workers=8) as ex:
        futures = {ex.submit(enrich_one, r): r for r in rows}
        enriched = []
        done = 0
        for f in as_completed(futures):
            try:
                enriched.append(f.result())
            except Exception as e:
                enriched.append(futures[f])
            done += 1
            if done % 10 == 0:
                print(f"  {done}/{len(rows)}")

    # Preserve order
    order = {r["id"]: i for i, r in enumerate(rows)}
    enriched.sort(key=lambda r: order.get(r["id"], 9999))

    fieldnames = ["id", "company", "track", "title", "url", "publish_date", "authors", "in_scope", "scope_reason"]
    with open(in_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(enriched)

    with_title = sum(1 for r in enriched if r.get("title"))
    with_date = sum(1 for r in enriched if r.get("publish_date"))
    dates = [r["publish_date"] for r in enriched if r["publish_date"]]
    print(f"\nResults:")
    print(f"  total: {len(enriched)}")
    print(f"  with title: {with_title}")
    print(f"  with date: {with_date}")
    if dates:
        print(f"  date range: {min(dates)} → {max(dates)}")

if __name__ == "__main__":
    main()
