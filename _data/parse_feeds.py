#!/usr/bin/env python3
"""Parse downloaded sitemaps/RSS/HTML and emit per-source CSVs."""
import re
import csv
import xml.etree.ElementTree as ET
from html import unescape
from pathlib import Path
from datetime import datetime

DATA = Path(__file__).parent

NS_SM = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
NS_ATOM = "{http://www.w3.org/2005/Atom}"

def write_csv(path, rows):
    with open(path, "w", newline="") as f:
        w = csv.writer(f, quoting=csv.QUOTE_MINIMAL)
        w.writerow(["id", "company", "track", "title", "url", "publish_date", "authors", "in_scope", "scope_reason"])
        for r in rows:
            w.writerow(r)

def slug_from_url(url, prefixes):
    for p in prefixes:
        if p in url:
            rest = url.split(p, 1)[1].strip("/")
            return rest.split("/")[0].split("?")[0]
    return url.rstrip("/").split("/")[-1]

# ---------------- Anthropic ----------------
def parse_anthropic():
    tree = ET.parse(DATA / "anthropic_sitemap.xml")
    root = tree.getroot()
    rows = []
    for url in root.findall(f"{NS_SM}url"):
        loc = url.findtext(f"{NS_SM}loc", "")
        if "/research/" in loc and not loc.endswith("/research"):
            slug = slug_from_url(loc, ["/research/"])
            if slug and not slug.startswith("team"):
                rows.append([
                    f"ant-r-{slug}", "anthropic", "research", "", loc, "", "", "TRUE", ""
                ])
        elif "/engineering/" in loc and not loc.endswith("/engineering"):
            slug = slug_from_url(loc, ["/engineering/"])
            if slug:
                rows.append([
                    f"ant-e-{slug}", "anthropic", "engineering", "", loc, "", "", "TRUE", ""
                ])
    write_csv(DATA / "enum-anthropic.csv", rows)
    return len(rows)

# ---------------- OpenAI ----------------
def parse_openai():
    rows = []
    seen = set()
    # Engineering first so it wins on dedup
    for sitemap, track, tprefix in [
        ("openai_eng.xml", "engineering", "oai-e-"),
        ("openai_pub.xml", "research", "oai-r-"),
    ]:
        tree = ET.parse(DATA / sitemap)
        root = tree.getroot()
        for url in root.findall(f"{NS_SM}url"):
            loc = url.findtext(f"{NS_SM}loc", "")
            if "/index/" in loc:
                slug = slug_from_url(loc, ["/index/"])
                if slug and slug not in seen:
                    seen.add(slug)
                    rows.append([f"{tprefix}{slug}", "openai", track, "", loc, "", "", "TRUE", ""])
    write_csv(DATA / "enum-openai.csv", rows)
    return len(rows)

# ---------------- Thinking Machines ----------------
def parse_tm():
    tree = ET.parse(DATA / "tm_rss.xml")
    root = tree.getroot()
    # RSS not Atom
    channel = root.find("channel")
    rows = []
    if channel is None:
        return 0
    for item in channel.findall("item"):
        link = item.findtext("link", "").strip()
        title = unescape(item.findtext("title", "").strip())
        pub = item.findtext("pubDate", "").strip()
        date = ""
        if pub:
            for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z"):
                try:
                    date = datetime.strptime(pub, fmt).strftime("%Y-%m-%d")
                    break
                except Exception:
                    pass
        author = item.findtext("{http://purl.org/dc/elements/1.1/}creator", "") or item.findtext("author", "")
        slug = link.rstrip("/").split("/")[-1]
        rows.append([f"tm-r-{slug}", "thinking-machines", "research", title, link, date, author, "TRUE", ""])
    write_csv(DATA / "enum-thinking-machines.csv", rows)
    return len(rows)

# ---------------- Cognition ----------------
def parse_cognition():
    tree = ET.parse(DATA / "cognition_rss.xml")
    root = tree.getroot()
    channel = root.find("channel")
    rows = []
    if channel is None:
        return 0
    for item in channel.findall("item"):
        link = item.findtext("link", "").strip()
        title = unescape(item.findtext("title", "").strip())
        pub = item.findtext("pubDate", "").strip()
        date = ""
        if pub:
            for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S GMT"):
                try:
                    date = datetime.strptime(pub, fmt).strftime("%Y-%m-%d")
                    break
                except Exception:
                    pass
        author = item.findtext("{http://purl.org/dc/elements/1.1/}creator", "") or item.findtext("author", "")
        slug = link.rstrip("/").split("/")[-1]
        # default in-scope TRUE; will be refined in Phase 2 per-post substance check
        rows.append([f"cog-r-{slug}", "cognition", "research", title, link, date, author, "TRUE", ""])
    write_csv(DATA / "enum-cognition.csv", rows)
    return len(rows)

# ---------------- Vercel ----------------
def parse_vercel():
    tree = ET.parse(DATA / "vercel_atom.xml")
    root = tree.getroot()
    rows = []
    AI_RX = re.compile(r"\b(ai|llm|agent|agents|gpt|embed|embedding|rag|v0|ai-sdk|chatbot|inference|prompt|copilot|generative|model|fine-tun|eval|mcp)\b", re.I)
    for entry in root.findall(f"{NS_ATOM}entry"):
        link_el = entry.find(f"{NS_ATOM}link")
        link = link_el.get("href") if link_el is not None else ""
        title = unescape(entry.findtext(f"{NS_ATOM}title", "").strip())
        pub = entry.findtext(f"{NS_ATOM}published", "") or entry.findtext(f"{NS_ATOM}updated", "")
        date = pub[:10] if pub else ""
        authors = "|".join(a.findtext(f"{NS_ATOM}name", "") for a in entry.findall(f"{NS_ATOM}author"))
        # Only blog/{slug}, not changelog
        if "/blog/" not in link or "/changelog/" in link:
            continue
        slug = link.rstrip("/").split("/blog/")[-1].split("/")[0]
        if not slug:
            continue
        # Heuristic: AI/engineering-related
        is_ai = bool(AI_RX.search(title) or AI_RX.search(slug.replace("-", " ")))
        if is_ai:
            rows.append([f"vcl-e-{slug}", "vercel", "engineering", title, link, date, authors, "TRUE", ""])
        else:
            rows.append([f"vcl-e-{slug}", "vercel", "engineering", title, link, date, authors, "FALSE", "not-ai-engineering"])
    write_csv(DATA / "enum-vercel.csv", rows)
    return len(rows)

# ---------------- Cursor ----------------
def parse_cursor():
    rows = []
    # Cursor blog HTML is SSR'd. Extract /blog/{slug} links and titles.
    for fn, track_guess in [("cursor_blog.html", "all"), ("cursor_research.html", "research")]:
        html = (DATA / fn).read_text(errors="ignore")
        # Find all post links: /blog/{slug} — but not /blog/topic/, /blog/page/, etc.
        found = re.findall(r'href="(/blog/[a-z0-9-]+)"[^>]*>([^<]*)', html)
        # Also match JSON-ish structures for post cards (next.js often has __NEXT_DATA__)
        next_data = re.search(r'<script id="__NEXT_DATA__" type="application/json">(.+?)</script>', html)
        if next_data:
            # Extract slugs and titles from JSON
            raw = next_data.group(1)
            # Look for patterns like "slug":"xxx" next to "title":"yyy"
            posts_rx = re.findall(r'"slug":"([^"]+)"[^}]*?"title":"([^"]+)"[^}]*?"date":"([^"]+)"', raw)
            posts_rx += re.findall(r'"slug":"([^"]+)"[^}]*?"date":"([^"]+)"[^}]*?"title":"([^"]+)"', raw)
        # Fallback
        seen_slugs = set()
        for href, text in found:
            slug = href.split("/blog/")[1].strip("/")
            if slug in ("topic", "page") or "/" in slug:
                continue
            if slug in seen_slugs:
                continue
            seen_slugs.add(slug)
            title = text.strip() or slug.replace("-", " ").title()
            track = "research" if track_guess == "research" else "engineering"
            # For the "all" pass, we'll fix track later
            rows.append([f"cur-r-{slug}" if track == "research" else f"cur-e-{slug}",
                         "cursor", track, title, f"https://cursor.com/blog/{slug}", "", "", "TRUE" if track_guess == "research" else "FALSE", ""])
    # Dedupe by slug, prefer research-tagged
    by_slug = {}
    for r in rows:
        slug = r[4].rstrip("/").split("/")[-1]
        if slug not in by_slug or (r[2] == "research"):
            by_slug[slug] = r
    # If not tagged research, mark in_scope=FALSE for now (product-default)
    final = []
    for slug, r in by_slug.items():
        if r[2] != "research":
            r[7] = "FALSE"
            r[8] = "unclassified-cursor-blog"
        final.append(r)
    write_csv(DATA / "enum-cursor.csv", final)
    return len(final)

# ---------------- Databricks (RSS only, limited) ----------------
def parse_databricks_rss():
    """Fallback RSS parse — only returns 10 most recent. Full enumeration needs Playwright."""
    tree = ET.parse(DATA / "dbx_feed.xml")
    root = tree.getroot()
    channel = root.find("channel")
    rows = []
    if channel is None:
        return 0
    for item in channel.findall("item"):
        link = item.findtext("link", "").strip()
        title = unescape(item.findtext("title", "").strip())
        pub = item.findtext("pubDate", "").strip()
        date = ""
        if pub:
            for fmt in ("%a, %d %b %Y %H:%M:%S %z", "%a, %d %b %Y %H:%M:%S %Z", "%a, %d %b %Y %H:%M:%S GMT"):
                try:
                    date = datetime.strptime(pub, fmt).strftime("%Y-%m-%d")
                    break
                except Exception:
                    pass
        author = item.findtext("{http://purl.org/dc/elements/1.1/}creator", "") or item.findtext("author", "")
        slug = link.rstrip("/").split("/")[-1]
        # Category check
        cats = [c.text.lower() if c.text else "" for c in item.findall("category")]
        is_ai = any("ai" in c or "mosaic" in c or "research" in c or "generative" in c for c in cats)
        rows.append([f"dbx-r-{slug}", "databricks", "research", title, link, date, author, "TRUE" if is_ai else "FALSE", "" if is_ai else "rss-non-ai-category"])
    write_csv(DATA / "enum-databricks-rss-only.csv", rows)
    return len(rows)

if __name__ == "__main__":
    counts = {
        "anthropic": parse_anthropic(),
        "openai": parse_openai(),
        "thinking-machines": parse_tm(),
        "cognition": parse_cognition(),
        "vercel": parse_vercel(),
        "cursor": parse_cursor(),
        "databricks-rss-only": parse_databricks_rss(),
    }
    for k, v in counts.items():
        print(f"{k}: {v} rows")
