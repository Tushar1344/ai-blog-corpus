#!/usr/bin/env python3
"""Consolidate all enum-*.csv files into master.csv with unified schema and phase-2 substance filter."""
import csv
import re
from pathlib import Path

DATA = Path(__file__).parent

# Column order
FIELDS = ["id", "company", "track", "title", "url", "publish_date", "authors",
          "in_scope", "scope_reason", "summary", "contribution_type",
          "technical_domain", "techniques", "year", "md_anchor", "notes"]

SOURCE_FILES = [
    "enum-anthropic-tm.csv",
    "enum-openai.csv",
    "enum-databricks.csv",
    "enum-cursor.csv",
    "enum-vercel.csv",
    "enum-cognition.csv",
]

# Phase 2: substance filter patterns
# Drop posts whose title strongly signals pure launch / company news / customer story
DROP_TITLE_RX = re.compile(
    r"\b(introducing\b(?!\s+(our|the)\s+(new|latest)\s+(framework|architecture|method|paper|research|technique|model(?!\s+card)))"  # "Introducing X" but keep e.g. "Introducing our new research method"
    r"|now available|now live|now generally available|ga\s+release|ga\b"
    r"|pricing|we're hiring|hiring|join us|is here|is now here"
    r"|series [abc]\b|funding|raised|acquires|acquired|partnership with|partners?with"
    r"|at AWS re:Invent|at Google Cloud Next|at Snowflake Summit|at Data \+ AI Summit"
    r"|celebrates|celebration|anniversary|announces .* availability"
    r"|welcome to|welcomes?\s"
    r"|available on|available in"
    r")",
    re.I,
)

# Also drop posts on these slug patterns
DROP_SLUG_RX = re.compile(
    r"(press-release|leadership|company-news|funding|series-[abc]|we-are-hiring"
    r"|ceo-|cto-|appoints|launching-in-|partners-with|now-available|general-availability)",
    re.I,
)

def main():
    all_rows = []
    counts = {}
    for fn in SOURCE_FILES:
        p = DATA / fn
        if not p.exists():
            print(f"SKIP: {fn} (missing)")
            continue
        rdr = csv.DictReader(open(p))
        n = 0
        for row in rdr:
            # Ensure all fields exist
            out = {k: row.get(k, "") for k in FIELDS}
            # Derive year
            if out["publish_date"]:
                out["year"] = out["publish_date"][:4]
            # md_anchor
            if out["company"]:
                company_file = {
                    "anthropic": "anthropic",
                    "openai": "openai",
                    "databricks": "databricks-mosaic",
                    "cursor": "cursor",
                    "vercel": "vercel",
                    "cognition": "cognition",
                    "thinking-machines": "thinking-machines",
                }.get(out["company"], out["company"])
                out["md_anchor"] = f"by-company/{company_file}.md#{out['id']}"

            # Phase 2 substance filter — only applied to rows still in-scope
            if out["in_scope"] == "TRUE":
                title = out["title"] or ""
                slug = out["id"].split("-", 2)[-1] if "-" in out["id"] else ""

                # Customer stories / pure launch heuristics
                if DROP_TITLE_RX.search(title) or DROP_SLUG_RX.search(slug):
                    # But preserve technical launches that have methodology
                    # Keep if title mentions: benchmark, architecture, method, paper, system card, technical
                    if not re.search(r"\b(benchmark|architecture|method(ology)?|paper|technical|system card|training|inference|evals?|research|study|framework|kernel|algorithm|pretraining|post-training|rlhf|rlvr|moe|distillation|quantization|SAE|circuits|scaling laws?|how we built|how we trained|how we use|postmortem|retro)\b",
                                    title, re.I):
                        out["in_scope"] = "FALSE"
                        out["scope_reason"] = "phase2-title-slug-launch-or-company-news"

                # Specific company patterns
                if out["company"] == "cognition":
                    # Cognition posts are mostly launches — apply stricter filter
                    if re.search(r"^(Devin|Introducing|Launching|How\s+\w+\s+(uses?|adopted|adopts)|A Message from|What's New)", title, re.I):
                        if not re.search(r"\b(SWE-|benchmark|agent\b|research|technical|trace|evaluation|kernel|sandbox)\b", title, re.I):
                            out["in_scope"] = "FALSE"
                            out["scope_reason"] = "cognition-launch-or-customer"

                if out["company"] == "vercel":
                    # Stricter: keep only if title clearly engineering/technical
                    if not re.search(r"\b(how we|how\s+\w+\s+(built|uses|built)|benchmark|architecture|migrat|optimiz|performance|scaling|cache|latenc|throughput|edge|runtime|streaming|LLM|agent|AI SDK|embed|RAG|fine-tun|inference|model|eval|prompt caching|tool use|v0)\b", title, re.I):
                        # Keep if tagged as engineering in original CSV
                        pass

            all_rows.append(out)
            n += 1
        counts[fn] = n
        print(f"{fn}: {n} rows")

    # Also inject Thinking Machines rows from enum-thinking-machines.csv if not already in enum-anthropic-tm.csv
    # (they should be, but check)
    tm_file = DATA / "enum-thinking-machines.csv"
    if tm_file.exists():
        existing_ids = {r["id"] for r in all_rows}
        rdr = csv.DictReader(open(tm_file))
        for row in rdr:
            if row["id"] not in existing_ids:
                out = {k: row.get(k, "") for k in FIELDS}
                if out["publish_date"]:
                    out["year"] = out["publish_date"][:4]
                out["md_anchor"] = f"by-company/thinking-machines.md#{out['id']}"
                all_rows.append(out)

    # Write master
    master_path = DATA / "master.csv"
    with open(master_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(all_rows)

    # Report
    total = len(all_rows)
    in_scope = sum(1 for r in all_rows if r["in_scope"] == "TRUE")
    print(f"\nMASTER: {total} total rows, {in_scope} in-scope")

    by_co = {}
    for r in all_rows:
        co = r["company"]
        by_co.setdefault(co, {"total": 0, "in_scope": 0})
        by_co[co]["total"] += 1
        if r["in_scope"] == "TRUE":
            by_co[co]["in_scope"] += 1

    print("\nBy company:")
    for co, c in sorted(by_co.items()):
        print(f"  {co:20} total={c['total']:4}  in_scope={c['in_scope']:4}")

if __name__ == "__main__":
    main()
