#!/usr/bin/env python3
"""Generate must-read.md — top posts ranked by signal priority, broken down by focus area.

Also generates by-signal/{high,medium,low}.md — flat indexes for each overall signal tier.
"""
import csv
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).parent.parent
DATA = Path(__file__).parent

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
COMPANY_TITLES = {
    "anthropic": "Anthropic", "openai": "OpenAI", "databricks": "Databricks Mosaic",
    "cursor": "Cursor", "vercel": "Vercel", "cognition": "Cognition",
    "thinking-machines": "Thinking Machines", "google-research": "Google Research",
    "deepmind": "DeepMind", "meta-fair": "Meta FAIR", "huggingface": "Hugging Face",
    "ai2": "AI2", "deepseek": "DeepSeek", "sakana": "Sakana AI",
    "qwen": "Qwen", "mistral": "Mistral", "ai21": "AI21 Labs",
    "langchain": "LangChain", "moonshot": "Moonshot (Kimi)",
}

def load_rows():
    return [r for r in csv.DictReader(open(DATA / "master.csv"))
            if r.get("in_scope") == "TRUE" and r.get("dropped_in_v2") == "FALSE"]

def render_entry(r, include_summary=True):
    title = r["title"] or r["id"]
    url = r["url"]
    date = r["publish_date"] or "?"
    co = COMPANY_TITLES.get(r["company"], r["company"])
    country = r.get("country", "")
    fa = r.get("focus_area", "")
    sub = r.get("subcategory", "")
    sig = f"L={r['signal_learning']}/N={r['signal_novelty']}/A={r['signal_actionability']}"
    priority = r.get("signal_priority", "")
    lines = [
        f"### {title}",
        "",
        f"- **Company:** {co} ({country}) · **Focus:** {fa} / {sub} · **Date:** {date}",
        f"- **Signal:** {r['signal_overall']} — {sig} (priority {priority})",
        f"- **Link:** {url}",
    ]
    if include_summary and r.get("summary"):
        lines.append("")
        lines.append("**Summary:**")
        lines.append("")
        for b in r["summary"].split(";"):
            b = b.strip()
            if b:
                lines.append(f"- {b}")
    lines.append("")
    return "\n".join(lines)

def generate_must_read(rows):
    """Top-50 overall + top-15 per focus area."""
    out = ROOT / "must-read.md"
    in_scope = [r for r in rows if r["signal_overall"] == "H"]
    in_scope.sort(key=lambda r: -float(r.get("signal_priority") or 0))

    lines = [
        "# Must-read corpus",
        "",
        "Posts ranked by combined signal on three dimensions: **learning** (teaches fundamentals), **novelty** (new methods/findings), **actionability** (applicable techniques).",
        "",
        "Score = 1.2 × novelty + 1.1 × learning + 1.0 × actionability, each H=3/M=2/L=1.",
        "",
        "Filter the [Sheet](https://docs.google.com/spreadsheets/d/1td1T6wCEnw4EeG05I_hH1dK1aNkLR5HJZZ-4jr-Du9A/edit) by `signal_overall=H` for live slicing.",
        "",
        f"**{len(in_scope)} H-signal posts** (out of 1360 in-scope).",
        "",
        "## Top 50 overall",
        "",
        "| Rank | Signal | Priority | Company | Title |",
        "|---|---|---|---|---|",
    ]
    for i, r in enumerate(in_scope[:50], 1):
        title = (r["title"] or r["id"]).replace("|", "\\|")
        anchor_fa = r["focus_area"]
        lines.append(
            f"| {i} | L={r['signal_learning']}/N={r['signal_novelty']}/A={r['signal_actionability']} "
            f"| {r['signal_priority']} "
            f"| {COMPANY_TITLES.get(r['company'], r['company'])} "
            f"| [{title}](by-focus-area/{anchor_fa}.md#{r['id']}) |"
        )
    lines.append("")

    # Per focus area
    by_fa = defaultdict(list)
    for r in in_scope:
        by_fa[r["focus_area"]].append(r)

    for fa in FOCUS_AREAS_ORDER:
        entries = by_fa.get(fa, [])
        if not entries:
            continue
        lines.append(f"## {FOCUS_AREA_TITLES[fa]} — top picks ({len(entries)} H-signal total)")
        lines.append("")
        lines.append("| Signal | Priority | Company | Country | Date | Title |")
        lines.append("|---|---|---|---|---|---|")
        for r in entries[:15]:
            title = (r["title"] or r["id"]).replace("|", "\\|")
            anchor = f"by-focus-area/{fa}.md#{r['id']}"
            lines.append(
                f"| L={r['signal_learning']}/N={r['signal_novelty']}/A={r['signal_actionability']} "
                f"| {r['signal_priority']} "
                f"| {COMPANY_TITLES.get(r['company'], r['company'])} "
                f"| {r.get('country', '')} "
                f"| {r.get('publish_date', '')} "
                f"| [{title}]({anchor}) |"
            )
        lines.append("")

    out.write_text("\n".join(lines))
    print(f"Wrote {out} (top {min(50, len(in_scope))} overall + per-area breakdowns)")

def generate_by_signal(rows):
    """Flat by-signal/{high,medium,low}.md files."""
    out_dir = ROOT / "by-signal"
    out_dir.mkdir(exist_ok=True)
    for old in out_dir.glob("*.md"):
        old.unlink()

    buckets = defaultdict(list)
    for r in rows:
        s = r["signal_overall"]
        if s:
            buckets[s].append(r)

    for sig in ["H", "M", "L"]:
        entries = buckets.get(sig, [])
        entries.sort(key=lambda r: (-float(r.get("signal_priority") or 0), r.get("publish_date") or ""))
        name = {"H": "high", "M": "medium", "L": "low"}[sig]
        out = out_dir / f"{name}-signal.md"
        title = {"H": "High-signal posts", "M": "Medium-signal posts", "L": "Low-signal posts"}[sig]
        desc = {
            "H": "Must-read — posts scoring high on at least two of: learning, novelty, actionability.",
            "M": "Worth reading if you care about the topic — middle tier.",
            "L": "Likely low signal (product announcements, customer stories, reruns). Skim or skip unless you're completionist.",
        }[sig]
        lines = [
            f"# {title}",
            "",
            desc,
            "",
            f"**Count:** {len(entries)}",
            "",
            "| Priority | Signal | Company | Country | Date | Focus area | Title |",
            "|---|---|---|---|---|---|---|",
        ]
        for r in entries:
            title_txt = (r["title"] or r["id"]).replace("|", "\\|")
            anchor = f"../by-focus-area/{r['focus_area']}.md#{r['id']}"
            lines.append(
                f"| {r.get('signal_priority', '')} "
                f"| L={r['signal_learning']}/N={r['signal_novelty']}/A={r['signal_actionability']} "
                f"| {COMPANY_TITLES.get(r['company'], r['company'])} "
                f"| {r.get('country', '')} "
                f"| {r.get('publish_date', '')} "
                f"| {r.get('focus_area', '')} "
                f"| [{title_txt}]({anchor}) |"
            )
        out.write_text("\n".join(lines) + "\n")
    print(f"Wrote by-signal/ (3 files: high/medium/low)")

def main():
    rows = load_rows()
    print(f"Loaded {len(rows)} in-scope posts")
    generate_must_read(rows)
    generate_by_signal(rows)

if __name__ == "__main__":
    main()
