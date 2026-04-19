#!/usr/bin/env python3
"""Generate by-company/*.md and cross-reference files from master.csv.

First pass: emits entries with titles, links, dates, authors, and heuristic tags.
Summaries will be filled in by Phase 3 summarization agents.
"""
import csv
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent
DATA = Path(__file__).parent

COMPANY_FILES = {
    "anthropic": "anthropic.md",
    "openai": "openai.md",
    "databricks": "databricks-mosaic.md",
    "cursor": "cursor.md",
    "vercel": "vercel.md",
    "cognition": "cognition.md",
    "thinking-machines": "thinking-machines.md",
}
COMPANY_TITLES = {
    "anthropic": "Anthropic",
    "openai": "OpenAI",
    "databricks": "Databricks Mosaic AI",
    "cursor": "Cursor",
    "vercel": "Vercel",
    "cognition": "Cognition",
    "thinking-machines": "Thinking Machines",
}

def slug_to_anchor(post_id):
    return post_id.lower()

def build_entry_stub(row):
    """Build the markdown entry for a post in the canonical by-company file."""
    title = row["title"] or row["id"]
    url = row["url"]
    date = row["publish_date"] or "_date unknown_"
    authors = row["authors"] or ""
    track = row["track"]
    domain = row["technical_domain"]
    contrib = row["contribution_type"]
    techs = row["techniques"]

    lines = [
        f"### {title}",
        "",
        f"- **ID:** `{row['id']}`",
        f"- **Link:** {url}",
        f"- **Date:** {date}",
    ]
    if authors:
        lines.append(f"- **Authors:** {authors}")
    lines.append(f"- **Track:** {track}")
    lines.append(f"- **Domain:** {domain}")
    lines.append(f"- **Contribution type:** {contrib}")
    if techs:
        lines.append(f"- **Techniques:** {techs.replace('|', ', ')}")
    lines.append("")
    if row["summary"]:
        lines.append("**Summary:**")
        lines.append("")
        for bullet in row["summary"].split(";"):
            bullet = bullet.strip()
            if bullet:
                lines.append(f"- {bullet}")
        lines.append("")
    else:
        lines.append("_Summary pending — see link for details._")
        lines.append("")
    return "\n".join(lines) + "\n"

def generate_company_files(rows):
    by_co = defaultdict(lambda: defaultdict(list))
    for r in rows:
        if r["in_scope"] != "TRUE":
            continue
        co = r["company"]
        track = r["track"]
        by_co[co][track].append(r)

    for co, tracks in by_co.items():
        out_file = ROOT / "by-company" / COMPANY_FILES[co]
        title = COMPANY_TITLES[co]
        lines = [f"# {title}", ""]
        # Small provenance note
        company_notes = {
            "anthropic": "Research and Engineering posts from anthropic.com. Canonical summaries live here.",
            "openai": "Research publications and engineering posts from openai.com. Canonical summaries live here.",
            "databricks": "Research and engineering posts from the Mosaic Research team (Databricks). Includes recoverable pre-acquisition MosaicML posts.",
            "cursor": "Research and engineering posts from cursor.com/blog. Changelog excluded.",
            "vercel": "Engineering and AI-applied posts from vercel.com/blog. Changelog excluded.",
            "cognition": "Research and engineering posts from cognition.ai/blog (Devin team). Product launches excluded.",
            "thinking-machines": "Connectionism research from thinkingmachines.ai/blog. News posts excluded.",
        }
        lines.append(company_notes.get(co, ""))
        lines.append("")
        total = sum(len(v) for v in tracks.values())
        lines.append(f"**In-scope post count:** {total}")
        lines.append("")

        for track_name, entries in sorted(tracks.items()):
            entries.sort(key=lambda r: r["publish_date"] or "0000-00-00", reverse=True)
            lines.append(f"## {track_name.title()} ({len(entries)} posts, newest first)")
            lines.append("")
            for e in entries:
                lines.append(build_entry_stub(e))
        out_file.write_text("\n".join(lines))
        print(f"Wrote {out_file} ({total} entries)")

def generate_cross_ref(rows, axis_column, out_dir, title_prefix):
    """Write one file per distinct value of axis_column.

    For multi-value columns (pipe-separated), split into multiple files.
    """
    (ROOT / out_dir).mkdir(parents=True, exist_ok=True)
    by_val = defaultdict(list)
    for r in rows:
        if r["in_scope"] != "TRUE":
            continue
        vals = r[axis_column]
        if not vals:
            continue
        # Multi-value if techniques, single otherwise
        splits = vals.split("|") if axis_column == "techniques" else [vals]
        for v in splits:
            v = v.strip()
            if v:
                by_val[v].append(r)

    for val, entries in sorted(by_val.items()):
        entries.sort(key=lambda r: r["publish_date"] or "0000-00-00", reverse=True)
        fn = re.sub(r"[^a-z0-9]+", "-", val.lower()).strip("-") + ".md"
        out_file = ROOT / out_dir / fn
        lines = [f"# {title_prefix}: {val}", ""]
        lines.append(f"**Post count:** {len(entries)}")
        lines.append("")
        lines.append("| Date | Company | Title | ID |")
        lines.append("|---|---|---|---|")
        for e in entries:
            title = (e["title"] or e["id"]).replace("|", "\\|")
            co = COMPANY_TITLES.get(e["company"], e["company"])
            co_file = COMPANY_FILES.get(e["company"], "unknown.md")
            rel_path = f"../by-company/{co_file}#{e['id']}"
            lines.append(f"| {e['publish_date'] or '?'} | {co} | [{title}]({rel_path}) | `{e['id']}` |")
        out_file.write_text("\n".join(lines) + "\n")
    print(f"Wrote {len(by_val)} files to {out_dir}/")

def generate_index(rows):
    """Write index.md — master cross-cutting overview."""
    out_file = ROOT / "index.md"
    in_scope_rows = [r for r in rows if r["in_scope"] == "TRUE"]
    by_co = defaultdict(int)
    by_year = defaultdict(int)
    for r in in_scope_rows:
        by_co[r["company"]] += 1
        if r["year"]:
            by_year[r["year"]] += 1

    lines = [
        "# AI Blog Corpus — Index",
        "",
        "Master cross-cutting index. For narrative by company, see `by-company/`. For thematic views, see `by-technical-domain/`, `by-contribution-type/`, `by-year/`, `by-technique/`.",
        "",
        f"**In-scope posts:** {len(in_scope_rows)}",
        f"**Total enumerated posts:** {len(rows)}",
        "",
        "## By company",
        "",
        "| Company | In-scope posts | File |",
        "|---|---|---|",
    ]
    for co in sorted(by_co):
        lines.append(f"| {COMPANY_TITLES[co]} | {by_co[co]} | [{COMPANY_FILES[co]}](by-company/{COMPANY_FILES[co]}) |")
    lines.append("")

    lines.append("## By year")
    lines.append("")
    lines.append("| Year | Posts |")
    lines.append("|---|---|")
    for yr in sorted(by_year.keys()):
        lines.append(f"| [{yr}](by-year/{yr}.md) | {by_year[yr]} |")
    lines.append("")

    lines.append("## By technical domain")
    lines.append("")
    by_dom = defaultdict(int)
    for r in in_scope_rows:
        if r["technical_domain"]:
            by_dom[r["technical_domain"]] += 1
    for d, c in sorted(by_dom.items(), key=lambda x: -x[1]):
        fn = re.sub(r"[^a-z0-9]+", "-", d.lower()).strip("-") + ".md"
        lines.append(f"- [{d}](by-technical-domain/{fn}) ({c})")
    lines.append("")

    lines.append("## By contribution type")
    lines.append("")
    by_ct = defaultdict(int)
    for r in in_scope_rows:
        if r["contribution_type"]:
            by_ct[r["contribution_type"]] += 1
    for d, c in sorted(by_ct.items(), key=lambda x: -x[1]):
        fn = re.sub(r"[^a-z0-9]+", "-", d.lower()).strip("-") + ".md"
        lines.append(f"- [{d}](by-contribution-type/{fn}) ({c})")
    lines.append("")

    lines.append("## Top techniques (cross-cutting tags)")
    lines.append("")
    techs = defaultdict(int)
    for r in in_scope_rows:
        for t in r["techniques"].split("|"):
            t = t.strip()
            if t:
                techs[t] += 1
    for t, c in sorted(techs.items(), key=lambda x: -x[1])[:30]:
        fn = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-") + ".md"
        lines.append(f"- [{t}](by-technique/{fn}) ({c})")
    lines.append("")

    lines.append("## Links")
    lines.append("")
    lines.append("- **Master Sheet:** https://docs.google.com/spreadsheets/d/1td1T6wCEnw4EeG05I_hH1dK1aNkLR5HJZZ-4jr-Du9A/edit")
    lines.append("- **Synthesis Doc:** _pending_")

    out_file.write_text("\n".join(lines))
    print(f"Wrote {out_file}")

def main():
    master = DATA / "master.csv"
    rows = list(csv.DictReader(open(master)))
    print(f"Loaded {len(rows)} rows")

    generate_company_files(rows)
    generate_cross_ref(rows, "technical_domain", "by-technical-domain", "Technical domain")
    generate_cross_ref(rows, "contribution_type", "by-contribution-type", "Contribution type")
    generate_cross_ref(rows, "year", "by-year", "Year")
    generate_cross_ref(rows, "techniques", "by-technique", "Technique")
    generate_index(rows)

if __name__ == "__main__":
    main()
