#!/usr/bin/env python3
"""Generate v2 markdown library with by-focus-area/ as canonical.

Directory layout (v2):
  by-focus-area/        — CANONICAL entries (full detail, one per post)
  by-company/           — cross-reference index (one line per post, linking to focus-area anchor)
  by-contribution-type/ — cross-reference
  by-year/              — cross-reference
  by-technique/         — cross-reference
"""
import csv
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent
DATA = Path(__file__).parent

COMPANY_TITLES = {
    "anthropic": "Anthropic",
    "openai": "OpenAI",
    "databricks": "Databricks Mosaic AI",
    "cursor": "Cursor",
    "vercel": "Vercel",
    "cognition": "Cognition",
    "thinking-machines": "Thinking Machines",
    "google-research": "Google Research",
    "deepmind": "Google DeepMind",
    "meta-fair": "Meta AI / FAIR",
    "huggingface": "Hugging Face",
    "ai2": "Allen Institute for AI",
    "deepseek": "DeepSeek",
    "sakana": "Sakana AI",
    "qwen": "Qwen (Alibaba)",
    "mistral": "Mistral AI",
    "ai21": "AI21 Labs",
    "langchain": "LangChain",
    "moonshot": "Moonshot (Kimi)",
}
COMPANY_FILES = {k: k.replace("_", "-") + ".md" for k in COMPANY_TITLES}

FOCUS_AREAS_ORDER = [
    "pretraining-and-architecture",
    "post-training-and-fine-tuning",
    "alignment-and-safety",
    "interpretability",
    "evals-and-benchmarks",
    "quantization-and-efficiency",
    "agentic-systems",
    "harness-and-context-engineering",
]
FOCUS_AREA_TITLES = {
    "pretraining-and-architecture": "Pretraining & Architecture",
    "post-training-and-fine-tuning": "Post-training & Fine-tuning",
    "alignment-and-safety": "Alignment & Safety",
    "interpretability": "Interpretability",
    "evals-and-benchmarks": "Evaluations & Benchmarks",
    "quantization-and-efficiency": "Quantization & Efficiency",
    "agentic-systems": "Agentic Systems",
    "harness-and-context-engineering": "Harness & Context Engineering",
}
FOCUS_AREA_DESC = {
    "pretraining-and-architecture": "MoE, SSMs, hybrids, scaling laws, new attention variants, data mixes, tokenizers, curriculum, foundation models.",
    "post-training-and-fine-tuning": "RLHF, RLAIF, RLVR, DPO, SFT, LoRA, on-policy distillation, reward modeling, preference optimization.",
    "alignment-and-safety": "Constitutional methods, responsible scaling policies, red-teaming, jailbreaking, sandbagging, alignment faking, safeguards, threat models, system cards.",
    "interpretability": "Sparse autoencoders (SAEs), circuits, steering, probing, dictionary learning, feature viz, monosemanticity.",
    "evals-and-benchmarks": "New eval suites, benchmark analyses, eval methodology (SWE-bench, Tau-Bench, BrowseComp, GPQA, HELM, etc.).",
    "quantization-and-efficiency": "FP8/INT8 training, post-training quantization, distillation for size, parameter-efficient methods (LoRA/PEFT).",
    "agentic-systems": "Agents, tool use, multi-agent, computer use, coding agents, agent benchmarks, agent traces, autonomous workflows.",
    "harness-and-context-engineering": "Agent scaffolding, context engineering, long-running harnesses, prompt caching strategy, agent skills, MCP integrations.",
}

def norm_fname(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") + ".md"

def build_full_entry(row):
    """Build a full canonical entry for by-focus-area/*.md"""
    title = row["title"] or row["id"]
    url = row["url"]
    date = row["publish_date"] or "_date unknown_"
    authors = row["authors"] or ""
    company = COMPANY_TITLES.get(row["company"], row["company"])
    track = row["track"]
    techs = row["techniques"]
    contrib = row["contribution_type"] or "_(uncategorized)_"

    lines = [
        f"### {title}",
        "",
        f"- **ID:** `{row['id']}`",
        f"- **Company:** {company}",
        f"- **Link:** {url}",
        f"- **Date:** {date}",
    ]
    if authors:
        lines.append(f"- **Authors:** {authors}")
    lines.append(f"- **Track:** {track}")
    lines.append(f"- **Contribution type:** {contrib}")
    # Signal line
    sig_o = row.get("signal_overall", "")
    sig_l = row.get("signal_learning", "")
    sig_n = row.get("signal_novelty", "")
    sig_a = row.get("signal_actionability", "")
    sig_p = row.get("signal_priority", "")
    if sig_o:
        lines.append(f"- **Signal:** {sig_o} — L={sig_l}/N={sig_n}/A={sig_a} (priority {sig_p})")
    if techs:
        lines.append(f"- **Techniques:** {techs.replace('|', ', ')}")
    lines.append("")
    if row["summary"]:
        lines.append("**Summary:**")
        lines.append("")
        for b in row["summary"].split(";"):
            b = b.strip()
            if b:
                lines.append(f"- {b}")
        lines.append("")
    else:
        lines.append("_Summary pending — see link for details._")
        lines.append("")
    return "\n".join(lines) + "\n"

def generate_focus_area_files(rows):
    """Write by-focus-area/*.md as canonical. Group by subcategory as H2."""
    # Import from sibling module
    import sys
    sys.path.insert(0, str(DATA))
    from assign_subcategory import SUB_TITLES, SUB_ORDER

    (ROOT / "by-focus-area").mkdir(exist_ok=True)
    by_fa = defaultdict(list)
    for r in rows:
        if not r["focus_area"]:
            continue
        by_fa[r["focus_area"]].append(r)

    for fa in FOCUS_AREAS_ORDER:
        entries = by_fa.get(fa, [])
        fname = fa + ".md"
        out = ROOT / "by-focus-area" / fname
        title = FOCUS_AREA_TITLES[fa]
        desc = FOCUS_AREA_DESC[fa]
        lines = [f"# {title}", "", desc, "", f"**Post count:** {len(entries)}", ""]
        by_co = defaultdict(int)
        for e in entries:
            by_co[e["company"]] += 1
        lines.append("**Contributors:**")
        lines.append("")
        for co, c in sorted(by_co.items(), key=lambda x: -x[1]):
            lines.append(f"- {COMPANY_TITLES.get(co, co)}: {c}")
        lines.append("")

        # Group by subcategory
        by_sub = defaultdict(list)
        for e in entries:
            by_sub[e.get("subcategory", "")].append(e)

        # Subcategory table of contents
        sub_order = SUB_ORDER.get(fa, []) + [""]
        lines.append("**Subcategories:**")
        lines.append("")
        for sub in sub_order:
            count = len(by_sub.get(sub, []))
            if count == 0:
                continue
            sub_title = SUB_TITLES.get(sub, sub or "Uncategorized")
            anchor = sub or "uncategorized"
            lines.append(f"- [{sub_title}](#{anchor}) ({count})")
        lines.append("")
        lines.append("---")
        lines.append("")

        # Write each subcategory as H2
        for sub in sub_order:
            sub_entries = by_sub.get(sub, [])
            if not sub_entries:
                continue
            sub_entries.sort(key=lambda r: r["publish_date"] or "0000-00-00", reverse=True)
            sub_title = SUB_TITLES.get(sub, sub or "Uncategorized")
            anchor = sub or "uncategorized"
            lines.append(f'## <a id="{anchor}"></a>{sub_title}')
            lines.append("")
            lines.append(f"_{len(sub_entries)} posts_")
            lines.append("")
            for e in sub_entries:
                lines.append(build_full_entry(e))
        out.write_text("\n".join(lines))
        print(f"Wrote {out} ({len(entries)} entries in {sum(1 for s in by_sub if by_sub[s])} subcategories)")

def generate_subcategory_files(rows):
    """Write by-subcategory/{subcategory}.md — flat folder, one file per subcategory."""
    import sys
    sys.path.insert(0, str(DATA))
    from assign_subcategory import SUB_TITLES

    out_dir = ROOT / "by-subcategory"
    out_dir.mkdir(exist_ok=True)
    # Clean stale
    for old in out_dir.glob("*.md"):
        old.unlink()

    by_sub = defaultdict(list)
    for r in rows:
        sub = r.get("subcategory", "")
        if not sub:
            continue
        by_sub[sub].append(r)

    for sub, entries in sorted(by_sub.items(), key=lambda x: -len(x[1])):
        entries.sort(key=lambda r: r["publish_date"] or "0000-00-00", reverse=True)
        fname = sub + ".md"
        out = out_dir / fname
        title = SUB_TITLES.get(sub, sub)
        fa = entries[0]["focus_area"] if entries else ""
        lines = [f"# {title}", ""]
        lines.append(f"**Post count:** {len(entries)}  |  **Focus area:** {FOCUS_AREA_TITLES.get(fa, fa)} ([canonical](../by-focus-area/{fa}.md#{sub}))")
        lines.append("")
        lines.append("| Date | Company | Title | ID |")
        lines.append("|---|---|---|---|")
        for e in entries:
            t = (e["title"] or e["id"]).replace("|", "\\|")
            co = COMPANY_TITLES.get(e["company"], e["company"])
            lines.append(f"| {e['publish_date'] or '?'} | {co} | [{t}](../by-focus-area/{fa}.md#{e['id']}) | `{e['id']}` |")
        out.write_text("\n".join(lines) + "\n")
    print(f"Wrote {len(by_sub)} files to by-subcategory/")

def generate_company_files(rows):
    """Write by-company/*.md as cross-reference (one-line entries linking to focus-area anchors)."""
    (ROOT / "by-company").mkdir(exist_ok=True)
    by_co = defaultdict(list)
    for r in rows:
        if not r["focus_area"]:
            continue
        by_co[r["company"]].append(r)

    for co, entries in by_co.items():
        entries.sort(key=lambda r: r["publish_date"] or "0000-00-00", reverse=True)
        out = ROOT / "by-company" / COMPANY_FILES[co]
        title = COMPANY_TITLES[co]
        lines = [f"# {title}", ""]
        lines.append(f"**In-scope posts:** {len(entries)}")
        lines.append("")
        lines.append("Cross-reference index. Canonical entries live in `../by-focus-area/`.")
        lines.append("")
        # Group by focus_area
        by_fa = defaultdict(list)
        for e in entries:
            by_fa[e["focus_area"]].append(e)

        for fa in FOCUS_AREAS_ORDER:
            sub = by_fa.get(fa, [])
            if not sub:
                continue
            lines.append(f"## {FOCUS_AREA_TITLES[fa]} ({len(sub)})")
            lines.append("")
            lines.append("| Date | Title | ID |")
            lines.append("|---|---|---|")
            for e in sub:
                t = (e["title"] or e["id"]).replace("|", "\\|")
                lines.append(f"| {e['publish_date'] or '?'} | [{t}](../by-focus-area/{fa}.md#{e['id']}) | `{e['id']}` |")
            lines.append("")
        out.write_text("\n".join(lines))

    print(f"Wrote {len(by_co)} company cross-ref files")

def generate_country_files(rows):
    """Write by-country/*.md — one file per country, grouped by focus area."""
    out_dir = ROOT / "by-country"
    out_dir.mkdir(exist_ok=True)
    for old in out_dir.glob("*.md"):
        old.unlink()

    by_country = defaultdict(list)
    for r in rows:
        c = r.get("country", "")
        if c:
            by_country[c].append(r)

    for country, entries in sorted(by_country.items(), key=lambda x: -len(x[1])):
        entries.sort(key=lambda r: r["publish_date"] or "0000-00-00", reverse=True)
        fname = norm_fname(country)
        out = out_dir / fname
        # Count by company within country
        by_co = defaultdict(int)
        for e in entries:
            by_co[e["company"]] += 1
        # Group by focus area
        by_fa = defaultdict(list)
        for e in entries:
            by_fa[e["focus_area"]].append(e)

        lines = [f"# {country}", ""]
        lines.append(f"**Total in-scope posts:** {len(entries)}")
        lines.append("")
        lines.append("**Contributing organizations:**")
        lines.append("")
        for co, c in sorted(by_co.items(), key=lambda x: -x[1]):
            lines.append(f"- {COMPANY_TITLES.get(co, co)}: {c}")
        lines.append("")
        lines.append("---")
        lines.append("")
        for fa in FOCUS_AREAS_ORDER:
            sub = by_fa.get(fa, [])
            if not sub:
                continue
            lines.append(f"## {FOCUS_AREA_TITLES[fa]} ({len(sub)})")
            lines.append("")
            lines.append("| Date | Company | Title | ID |")
            lines.append("|---|---|---|---|")
            for e in sub:
                t = (e["title"] or e["id"]).replace("|", "\\|")
                co = COMPANY_TITLES.get(e["company"], e["company"])
                lines.append(f"| {e['publish_date'] or '?'} | {co} | [{t}](../by-focus-area/{fa}.md#{e['id']}) | `{e['id']}` |")
            lines.append("")
        out.write_text("\n".join(lines))
    print(f"Wrote {len(by_country)} country files to by-country/")

def generate_axis_files(rows, axis_col, out_dir, title_prefix, is_multi=False):
    """Generic cross-ref generator (same as v1)."""
    (ROOT / out_dir).mkdir(exist_ok=True)
    # Delete old files first to remove stale content
    for old in (ROOT / out_dir).glob("*.md"):
        old.unlink()
    by_val = defaultdict(list)
    for r in rows:
        if not r["focus_area"]:
            continue
        v = r.get(axis_col, "")
        if not v:
            continue
        splits = v.split("|") if is_multi else [v]
        for s in splits:
            s = s.strip()
            if s:
                by_val[s].append(r)

    for v, entries in by_val.items():
        entries.sort(key=lambda r: r["publish_date"] or "0000-00-00", reverse=True)
        fname = norm_fname(v)
        out = ROOT / out_dir / fname
        lines = [f"# {title_prefix}: {v}", "", f"**Post count:** {len(entries)}", ""]
        lines.append("| Date | Company | Title | ID |")
        lines.append("|---|---|---|---|")
        for e in entries:
            t = (e["title"] or e["id"]).replace("|", "\\|")
            co = COMPANY_TITLES.get(e["company"], e["company"])
            fa = e["focus_area"]
            lines.append(f"| {e['publish_date'] or '?'} | {co} | [{t}](../by-focus-area/{fa}.md#{e['id']}) | `{e['id']}` |")
        out.write_text("\n".join(lines) + "\n")
    print(f"Wrote {len(by_val)} files to {out_dir}/")

def generate_index(rows):
    """Write index.md — master cross-cutting overview."""
    in_scope = [r for r in rows if r["focus_area"]]
    out = ROOT / "index.md"

    by_co = defaultdict(int)
    by_year = defaultdict(int)
    by_fa = defaultdict(int)
    for r in in_scope:
        by_co[r["company"]] += 1
        if r["year"]:
            by_year[r["year"]] += 1
        by_fa[r["focus_area"]] += 1

    lines = [
        "# AI Blog Corpus v2 — Index",
        "",
        f"**{len(in_scope)} in-scope posts** across {len(by_co)} companies, categorized by focus area as the primary axis.",
        "",
        "## By focus area (canonical)",
        "",
        "| Focus area | Posts | File |",
        "|---|---|---|",
    ]
    for fa in FOCUS_AREAS_ORDER:
        c = by_fa.get(fa, 0)
        lines.append(f"| {FOCUS_AREA_TITLES[fa]} | {c} | [{fa}.md](by-focus-area/{fa}.md) |")
    lines.append("")

    lines.append("## By company")
    lines.append("")
    lines.append("| Company | Posts | File |")
    lines.append("|---|---|---|")
    for co in sorted(by_co, key=lambda k: -by_co[k]):
        lines.append(f"| {COMPANY_TITLES[co]} | {by_co[co]} | [{COMPANY_FILES[co]}](by-company/{COMPANY_FILES[co]}) |")
    lines.append("")

    # Subcategories
    import sys
    sys.path.insert(0, str(DATA))
    from assign_subcategory import SUB_TITLES, SUB_ORDER

    lines.append("## By subcategory (nested under focus area)")
    lines.append("")
    by_sub = defaultdict(int)
    by_sub_fa = {}
    for r in in_scope:
        sub = r.get("subcategory", "")
        if sub:
            by_sub[sub] += 1
            by_sub_fa[sub] = r["focus_area"]
    for fa in FOCUS_AREAS_ORDER:
        fa_subs = [s for s in SUB_ORDER.get(fa, []) if by_sub.get(s, 0) > 0]
        if not fa_subs:
            continue
        lines.append(f"### {FOCUS_AREA_TITLES[fa]}")
        lines.append("")
        for s in fa_subs:
            n = by_sub.get(s, 0)
            title = SUB_TITLES.get(s, s)
            lines.append(f"- [{title}](by-subcategory/{s}.md) ({n})")
        lines.append("")

    lines.append("## By year")
    lines.append("")
    for yr in sorted(by_year):
        lines.append(f"- [{yr}](by-year/{yr}.md) ({by_year[yr]})")
    lines.append("")

    lines.append("## Links")
    lines.append("")
    lines.append("- **Master Sheet:** https://docs.google.com/spreadsheets/d/1td1T6wCEnw4EeG05I_hH1dK1aNkLR5HJZZ-4jr-Du9A/edit")
    lines.append("- **Synthesis Doc:** regenerated from `_data/synthesis.md`")
    out.write_text("\n".join(lines))
    print(f"Wrote {out}")

def main():
    # Clean old by-technical-domain if it exists (retired in v2)
    old_td = ROOT / "by-technical-domain"
    if old_td.exists():
        import shutil
        shutil.rmtree(old_td)
        print(f"Retired {old_td}")

    rows = list(csv.DictReader(open(DATA / "master.csv")))
    in_scope = [r for r in rows if r["in_scope"] == "TRUE" and r.get("dropped_in_v2") == "FALSE" and r.get("focus_area")]
    print(f"In-scope v2: {len(in_scope)}")

    generate_focus_area_files(in_scope)
    generate_subcategory_files(in_scope)
    generate_company_files(in_scope)
    generate_country_files(in_scope)
    generate_axis_files(in_scope, "contribution_type", "by-contribution-type", "Contribution type")
    generate_axis_files(in_scope, "year", "by-year", "Year")
    generate_axis_files(in_scope, "techniques", "by-technique", "Technique", is_multi=True)
    generate_index(rows)

if __name__ == "__main__":
    main()
