#!/usr/bin/env python3
"""Tier 1 enumeration: Google Research, Meta AI, Hugging Face, DeepSeek.

Writes:
  enum-google-deepmind.csv  (actually Google Research; DeepMind done separately via Playwright)
  enum-meta-fair.csv
  enum-huggingface.csv
  enum-deepseek.csv
"""
import csv
import re
import json
import urllib.request
import urllib.parse
import subprocess
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from html import unescape
from datetime import datetime

DATA = Path(__file__).parent
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
NS_ATOM = "{http://www.w3.org/2005/Atom}"

FIELDS = ["id", "company", "track", "title", "url", "publish_date", "authors", "in_scope", "scope_reason"]

def fetch(url, timeout=30, referer=None):
    h = {"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"}
    if referer:
        h["Referer"] = referer
    req = urllib.request.Request(url, headers=h)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", errors="ignore")
    except Exception as e:
        return None

def write_csv(path, rows):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)

# ---------------- Google Research ----------------

def enum_google_research():
    rows = []
    years = list(range(2018, 2027))
    for yr in years:
        url = f"https://research.google/blog/{yr}/"
        html = fetch(url)
        if not html:
            continue
        # Links like /blog/{slug}/
        found = re.findall(r'href="/blog/([a-z0-9][a-z0-9-]+)/?"', html)
        found = set(found) - {str(yr), "tagged"}
        for slug in found:
            if slug.startswith("20"):  # skip year links
                continue
            rows.append({
                "id": f"gr-r-{slug}",
                "company": "google-research",
                "track": "research",
                "title": "",
                "url": f"https://research.google/blog/{slug}/",
                "publish_date": "",
                "authors": "",
                "in_scope": "TRUE",
                "scope_reason": "",
            })
    # Dedupe by id
    seen = set()
    uniq = []
    for r in rows:
        if r["id"] not in seen:
            seen.add(r["id"])
            uniq.append(r)
    return uniq

def enrich_google_research(row):
    html = fetch(row["url"])
    if not html:
        return row
    m = re.search(r'<meta[^>]+property="og:title"[^>]+content="([^"]+)"', html)
    if m:
        row["title"] = unescape(m.group(1)).strip()
    else:
        m = re.search(r'<title>([^<]+)</title>', html)
        if m:
            row["title"] = unescape(m.group(1)).strip()
    row["title"] = re.sub(r'\s*[–|-]\s*Google\s+Research\s*$', '', row["title"] or '')
    # Publish date
    m = re.search(r'<meta[^>]+(?:property="article:published_time"|itemprop="datePublished")[^>]+content="([^"]+)"', html)
    if m:
        row["publish_date"] = m.group(1)[:10]
    else:
        m = re.search(r'<time[^>]+datetime="([^"]+)"', html)
        if m:
            row["publish_date"] = m.group(1)[:10]
    # Authors
    ms = re.findall(r'<meta[^>]+name="author"[^>]+content="([^"]+)"', html)
    if ms:
        row["authors"] = "|".join(ms[:6])
    return row

# ---------------- Meta AI (via Wayback slugs + Wayback content fetch) ----------------

def enum_meta():
    slugs = Path(DATA / "meta_slugs.txt").read_text().splitlines()
    rows = []
    for s in slugs:
        if not s:
            continue
        rows.append({
            "id": f"meta-r-{s}",
            "company": "meta-fair",
            "track": "research",
            "title": s.replace("-", " ").strip().title()[:120],
            "url": f"https://ai.meta.com/blog/{s}/",
            "publish_date": "",
            "authors": "",
            "in_scope": "TRUE",
            "scope_reason": "",
        })
    return rows

def enrich_meta(row):
    wb = f"https://web.archive.org/web/2026/{row['url']}"
    html = fetch(wb)
    if not html or len(html) < 5000:
        html = fetch(f"https://web.archive.org/web/2025/{row['url']}")
    if not html:
        return row
    m = re.search(r'<meta[^>]+property="og:title"[^>]+content="([^"]+)"', html)
    if m:
        t = unescape(m.group(1)).strip()
        t = re.sub(r'\s*[|–-]\s*(Meta|Meta AI)\s*$', '', t)
        if t and len(t) > 3:
            row["title"] = t
    # Date
    m = re.search(r'<meta[^>]+(?:property="article:published_time"|itemprop="datePublished")[^>]+content="([^"]+)"', html)
    if m:
        row["publish_date"] = m.group(1)[:10]
    else:
        m = re.search(r'<time[^>]+datetime="(\d{4}-\d{2}-\d{2})', html)
        if m:
            row["publish_date"] = m.group(1)
    return row

# ---------------- Hugging Face ----------------

def enum_huggingface():
    xml_text = (DATA / "hf_feed.xml").read_text()
    root = ET.fromstring(xml_text)
    rows = []
    # Detect format (atom vs rss)
    channel = root.find("channel")
    if channel is not None:
        items = channel.findall("item")
        for it in items:
            link = it.findtext("link", "").strip()
            title = unescape(it.findtext("title", "").strip())
            pub = it.findtext("pubDate", "").strip()
            date = ""
            if pub:
                for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S GMT"):
                    try:
                        date = datetime.strptime(pub, fmt).strftime("%Y-%m-%d")
                        break
                    except Exception:
                        pass
            author = it.findtext("{http://purl.org/dc/elements/1.1/}creator", "").strip() or it.findtext("author", "").strip()
            # Skip community/author posts (pattern /blog/{username}/{slug})
            # Official: /blog/{slug}, community: /blog/{user}/{slug}
            m = re.match(r"https?://huggingface\.co/blog/([^/]+)(?:/([^/]+))?/?$", link)
            if not m:
                continue
            part1, part2 = m.group(1), m.group(2)
            if part2:
                # community/author post — skip
                continue
            slug = part1
            rows.append({
                "id": f"hf-r-{slug}",
                "company": "huggingface",
                "track": "research",
                "title": title,
                "url": link,
                "publish_date": date,
                "authors": author,
                "in_scope": "TRUE",
                "scope_reason": "",
            })
    return rows

# ---------------- DeepSeek ----------------

def enum_deepseek():
    # Get all repos
    r = subprocess.run(["gh", "api", "/users/deepseek-ai/repos?per_page=100",
                        "--jq", ".[] | {name, description, default_branch, created_at}"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        print("gh api failed:", r.stderr[:200])
        return []
    repos = [json.loads(line) for line in r.stdout.strip().split("\n") if line]

    # Filter: keep only model technical-report repos (not infra tools)
    TECHNICAL_REPO_PATTERNS = [
        r"^deepseek-.*$",  # DeepSeek-V3, V2, R1, Coder, etc.
        r"^janus$",
        r"^esft$",
        r"^engram$",
        r"^dreamcraft3d$",
    ]
    # Exclude infra repos
    EXCLUDE = {"3fs", "deepep", "deepgemm", "dualpipe", "eplb", "flashmla", "lplb", "smallpond",
               "awesome-deepseek-coder", "awesome-deepseek-integration", "open-infra-index",
               "nano-vllm", "profile-data"}

    rows = []
    for repo in repos:
        name = repo["name"]
        lname = name.lower()
        if lname in EXCLUDE:
            continue
        if not any(re.match(p, lname) for p in TECHNICAL_REPO_PATTERNS):
            continue
        branch = repo.get("default_branch", "main")
        # Fetch README
        readme_url = f"https://raw.githubusercontent.com/deepseek-ai/{name}/{branch}/README.md"
        readme = fetch(readme_url)
        title = name
        pub = (repo.get("created_at") or "")[:10]
        # Extract first # heading as title
        if readme:
            m = re.search(r"^#\s+(.+?)\s*$", readme, re.MULTILINE)
            if m:
                title = m.group(1).strip().split("|")[0].strip()[:200]
            # Find arXiv link
            arxiv = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", readme)
            if arxiv:
                # Keep GitHub URL as canonical, mention arxiv in scope_reason
                pass
        rows.append({
            "id": f"dsk-r-{lname}",
            "company": "deepseek",
            "track": "research",
            "title": title,
            "url": f"https://github.com/deepseek-ai/{name}",
            "publish_date": pub,
            "authors": "DeepSeek-AI",
            "in_scope": "TRUE",
            "scope_reason": "",
        })
    return rows

# ---------------- Main ----------------

def enrich_concurrent(rows, enrich_fn, label, max_workers=10):
    print(f"  enriching {len(rows)} {label} rows ({max_workers} workers)...")
    with ThreadPoolExecutor(max_workers=max_workers) as ex:
        futures = {ex.submit(enrich_fn, r): r for r in rows}
        done = 0
        for f in as_completed(futures):
            try:
                f.result()
            except Exception:
                pass
            done += 1
            if done % 50 == 0:
                print(f"    {done}/{len(rows)}")

def main():
    print("=== Google Research ===")
    gr = enum_google_research()
    print(f"  enumerated {len(gr)} Google Research posts")
    enrich_concurrent(gr, enrich_google_research, "Google Research", max_workers=10)
    write_csv(DATA / "enum-google-research.csv", gr)

    print("\n=== Hugging Face ===")
    hf = enum_huggingface()
    print(f"  enumerated {len(hf)} HF official posts (community skipped)")
    write_csv(DATA / "enum-huggingface.csv", hf)

    print("\n=== DeepSeek ===")
    ds = enum_deepseek()
    print(f"  enumerated {len(ds)} DeepSeek technical reports")
    write_csv(DATA / "enum-deepseek.csv", ds)

    print("\n=== Meta AI ===")
    meta = enum_meta()
    print(f"  enumerated {len(meta)} Meta AI blog URLs from CDX")
    enrich_concurrent(meta, enrich_meta, "Meta AI", max_workers=8)
    write_csv(DATA / "enum-meta-fair.csv", meta)

    print("\nAll done.")

if __name__ == "__main__":
    main()
