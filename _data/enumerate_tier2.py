#!/usr/bin/env python3
"""Tier 2 enumeration: Sakana, Qwen, Mistral, AI21, LangChain, Moonshot.

Writes per-source CSVs into _data/enum-{company}.csv
"""
import csv
import json
import re
import subprocess
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from datetime import datetime
from html import unescape

DATA = Path(__file__).parent
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'

FIELDS = ["id", "company", "country", "track", "title", "url", "publish_date", "authors", "in_scope", "scope_reason"]
NS_SM = "{http://www.sitemaps.org/schemas/sitemap/0.9}"

def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", errors="ignore")
    except Exception:
        return None

def extract_title_date(html):
    if not html:
        return "", ""
    title = ""
    date = ""
    # Prefer <title> (usually the specific post title); fall back to og:title
    m = re.search(r'<title>([^<]+)</title>', html)
    if m:
        title = unescape(m.group(1)).strip()
    # If <title> looks like a brand-only string (short, matches brand pattern), try og:title
    brand_only = re.match(r'^(Sakana AI|Mistral AI|Mistral|AI21 Labs?|LangChain( Blog)?|Qwen|Moonshot( AI)?|Blog)\s*$', title, re.I)
    if brand_only or not title:
        m2 = re.search(r'<meta[^>]+property=["\']og:title["\'][^>]+content=["\']([^"\']+)', html)
        if m2:
            t2 = unescape(m2.group(1)).strip()
            if t2 and not re.match(r'^(Sakana AI|Mistral AI|Mistral|AI21 Labs?|LangChain|Qwen|Moonshot( AI)?|Blog)\s*$', t2, re.I):
                title = t2
    # Strip common suffixes
    title = re.sub(r'\s*[|·•\-–—]\s*(Sakana AI|Qwen|Mistral|Mistral AI|AI21 Labs|AI21|LangChain|Moonshot|blog)\s*$', '', title, flags=re.I)

    m = re.search(r'property=["\']article:published_time["\'][^>]+content=["\']([^"\']+)', html)
    if m:
        date = m.group(1)[:10]
    else:
        m = re.search(r'itemprop=["\']datePublished["\'][^>]+content=["\']([^"\']+)', html)
        if m:
            date = m.group(1)[:10]
        else:
            m = re.search(r'<time[^>]+datetime=["\'](\d{4}-\d{2}-\d{2})', html)
            if m:
                date = m.group(1)
            else:
                # text date near H1
                mh = re.search(r'<h1\b', html)
                head = html[mh.start():mh.start()+80000] if mh else html[:80000]
                months = {m: i+1 for i, m in enumerate(["January","February","March","April","May","June","July","August","September","October","November","December"])}
                m = re.search(r'\b(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+(\d{1,2}),?\s+(\d{4})\b', head)
                if m:
                    mo_str = m.group(1).lower()
                    mn = {
                        "jan":1,"feb":2,"mar":3,"apr":4,"may":5,"jun":6,
                        "jul":7,"aug":8,"sep":9,"oct":10,"nov":11,"dec":12
                    }[mo_str[:3]]
                    date = f"{int(m.group(3)):04d}-{mn:02d}-{int(m.group(2)):02d}"
    return title, date

def write_csv(path, rows):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)

# ---------------- Sakana ----------------
def enum_sakana():
    html = fetch("https://sakana.ai/blog/")
    if not html:
        html = (DATA.parent / "_tmp_sakana.html").read_text() if (DATA.parent / "_tmp_sakana.html").exists() else ""
    # Extract all /{slug}/ links from the blog index
    slugs = sorted(set(re.findall(r'href="/([a-z][a-z0-9-]+)/"', html)))
    # Exclude known navigation slugs
    exclude = {"blog", "ja", "en", "news", "about", "careers", "contact", "team",
               "imprint", "privacy", "terms", "research", "products", "landing"}
    slugs = [s for s in slugs if s not in exclude and not s.endswith('-jp')]

    rows = []
    for s in slugs:
        url = f"https://sakana.ai/{s}/"
        post_html = fetch(url)
        title, date = extract_title_date(post_html)
        # Fallback title
        if not title:
            title = s.replace("-", " ").title()
        rows.append({
            "id": f"sk-r-{s}",
            "company": "sakana",
            "country": "Japan",
            "track": "research",
            "title": title,
            "url": url,
            "publish_date": date,
            "authors": "",
            "in_scope": "TRUE",
            "scope_reason": "",
        })
    return rows

# ---------------- Qwen ----------------
def enum_qwen():
    sm = fetch("https://qwenlm.github.io/en/sitemap.xml")
    if not sm:
        return []
    try:
        root = ET.fromstring(sm)
    except Exception:
        return []
    rows = []
    for url in root.findall(f"{NS_SM}url"):
        loc = url.findtext(f"{NS_SM}loc", "")
        if not loc or "/blog/" not in loc:
            continue
        lastmod = url.findtext(f"{NS_SM}lastmod", "")
        slug = loc.rstrip("/").split("/blog/")[-1].split("/")[0]
        if not slug:
            continue
        post_html = fetch(loc)
        title, date = extract_title_date(post_html)
        if not date and lastmod:
            date = lastmod[:10]
        if not title:
            title = slug.replace("-", " ").title()
        rows.append({
            "id": f"qw-r-{slug}",
            "company": "qwen",
            "country": "China",
            "track": "research",
            "title": title,
            "url": loc,
            "publish_date": date,
            "authors": "Qwen Team",
            "in_scope": "TRUE",
            "scope_reason": "",
        })
    return rows

# ---------------- Mistral (via Wayback CDX) ----------------
def enum_mistral():
    cdx = fetch("https://web.archive.org/cdx/search/cdx?url=mistral.ai/news/*&output=json&collapse=urlkey&filter=statuscode:200&limit=3000")
    if not cdx:
        return []
    try:
        data = json.loads(cdx)
    except Exception:
        return []
    h = data[0]
    slugs = set()
    for row in data[1:]:
        url = row[h.index("original")]
        m = re.search(r"/news/([a-z0-9][a-z0-9-]+)/?$", url)
        if m:
            slugs.add(m.group(1))
    rows = []
    for s in sorted(slugs):
        url = f"https://mistral.ai/news/{s}/"
        # Try Wayback fetch for title/date
        wb = fetch(f"https://web.archive.org/web/2024/{url}") or fetch(f"https://web.archive.org/web/2025/{url}")
        title, date = extract_title_date(wb)
        if not title:
            title = s.replace("-", " ").title()
        rows.append({
            "id": f"mt-r-{s}",
            "company": "mistral",
            "country": "France",
            "track": "research",
            "title": title,
            "url": url,
            "publish_date": date,
            "authors": "Mistral AI",
            "in_scope": "TRUE",
            "scope_reason": "",
        })
    return rows

# ---------------- AI21 (via Wayback CDX) ----------------
def enum_ai21():
    cdx = fetch("https://web.archive.org/cdx/search/cdx?url=ai21.com/blog/*&output=json&collapse=urlkey&filter=statuscode:200&limit=3000")
    if not cdx:
        return []
    try:
        data = json.loads(cdx)
    except Exception:
        return []
    h = data[0]
    slugs = set()
    for row in data[1:]:
        url = row[h.index("original")]
        m = re.search(r"/blog/([a-z0-9][a-z0-9-]+)/?$", url)
        if m:
            slugs.add(m.group(1))
    rows = []
    for s in sorted(slugs):
        url = f"https://www.ai21.com/blog/{s}/"
        wb = fetch(f"https://web.archive.org/web/2024/{url}") or fetch(f"https://web.archive.org/web/2025/{url}")
        title, date = extract_title_date(wb)
        if not title:
            title = s.replace("-", " ").title()
        rows.append({
            "id": f"a21-r-{s}",
            "company": "ai21",
            "country": "Israel",
            "track": "research",
            "title": title,
            "url": url,
            "publish_date": date,
            "authors": "AI21 Labs",
            "in_scope": "TRUE",
            "scope_reason": "",
        })
    return rows

# ---------------- LangChain ----------------
def enum_langchain():
    sm = fetch("https://www.langchain.com/sitemap.xml")
    if not sm:
        return []
    locs = re.findall(r"<loc>(https://www\.langchain\.com/blog/[^<]+)</loc>", sm)
    rows = []
    for url in locs:
        slug = url.rstrip("/").split("/blog/")[-1]
        html = fetch(url)
        title, date = extract_title_date(html)
        if not title:
            title = slug.replace("-", " ").title()
        rows.append({
            "id": f"lc-r-{slug}",
            "company": "langchain",
            "country": "USA",
            "track": "research",
            "title": title,
            "url": url,
            "publish_date": date,
            "authors": "LangChain",
            "in_scope": "TRUE",
            "scope_reason": "",
        })
    return rows

# ---------------- Moonshot ----------------
def enum_moonshot():
    r = subprocess.run(["gh", "api", "/users/MoonshotAI/repos?per_page=100",
                        "--jq", ".[] | {name, description, default_branch, created_at}"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return []
    repos = [json.loads(line) for line in r.stdout.strip().split("\n") if line]

    INCLUDE = re.compile(r"^(kimi|moonlight|mo(d|b)a|mura|memory)", re.I)
    EXCLUDE = {"awesome-llms", "kimi-chat", ".github"}

    rows = []
    for repo in repos:
        name = repo["name"]
        lname = name.lower()
        if lname in EXCLUDE:
            continue
        if not INCLUDE.match(lname):
            continue
        branch = repo.get("default_branch", "main")
        readme_url = f"https://raw.githubusercontent.com/MoonshotAI/{name}/{branch}/README.md"
        readme = fetch(readme_url)
        title = name
        pub = (repo.get("created_at") or "")[:10]
        if readme:
            m = re.search(r"^#\s+(.+?)\s*$", readme, re.MULTILINE)
            if m:
                title = m.group(1).strip().split("|")[0].strip()[:200]
        rows.append({
            "id": f"mn-r-{lname}",
            "company": "moonshot",
            "country": "China",
            "track": "research",
            "title": title,
            "url": f"https://github.com/MoonshotAI/{name}",
            "publish_date": pub,
            "authors": "Moonshot AI",
            "in_scope": "TRUE",
            "scope_reason": "",
        })
    return rows

# ---------------- Concurrent runner ----------------
def run_with_concurrent_enrich(rows, enrich_url_fn, max_workers=6):
    # Used by enumerators if they pass post URLs needing fetch
    pass

def main():
    import sys
    which = sys.argv[1] if len(sys.argv) > 1 else "all"

    jobs = [
        ("sakana", enum_sakana),
        ("qwen", enum_qwen),
        ("mistral", enum_mistral),
        ("ai21", enum_ai21),
        ("langchain", enum_langchain),
        ("moonshot", enum_moonshot),
    ]
    for name, fn in jobs:
        if which != "all" and which != name:
            continue
        print(f"\n=== {name} ===")
        rows = fn()
        print(f"  enumerated {len(rows)}")
        with_date = sum(1 for r in rows if r.get("publish_date"))
        print(f"  with date: {with_date}")
        out = DATA / f"enum-{name}.csv"
        write_csv(out, rows)
        print(f"  wrote {out}")

if __name__ == "__main__":
    main()
