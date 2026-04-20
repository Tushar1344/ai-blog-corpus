#!/usr/bin/env python3
"""Add `country` column to master.csv and backfill all existing companies."""
import csv
from pathlib import Path

DATA = Path(__file__).parent

COMPANY_COUNTRY = {
    # Existing
    "anthropic": "USA",
    "openai": "USA",
    "databricks": "USA",
    "cursor": "USA",
    "vercel": "USA",
    "cognition": "USA",
    "thinking-machines": "USA",
    "google-research": "USA",
    "deepmind": "UK",            # London HQ, Google-owned
    "meta-fair": "USA",
    "huggingface": "France",     # Paris HQ, Franco-American (NYC + Paris)
    "ai2": "USA",
    "deepseek": "China",
    # Tier 2 (new)
    "sakana": "Japan",
    "qwen": "China",
    "mistral": "France",
    "ai21": "Israel",
    "langchain": "USA",
    "moonshot": "China",
}

def main():
    path = DATA / "master.csv"
    rows = list(csv.DictReader(open(path)))
    fields = list(rows[0].keys())
    if "country" not in fields:
        # Place right after company
        fields.insert(fields.index("company") + 1, "country")

    for r in rows:
        r.setdefault("country", "")
        if not r["country"]:
            r["country"] = COMPANY_COUNTRY.get(r["company"], "")

    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    c = Counter(r["country"] for r in rows if r.get("in_scope") == "TRUE" and r.get("dropped_in_v2") == "FALSE")
    print(f"Added country column. Distribution:")
    for k, v in c.most_common():
        print(f"  {k:10} {v}")

if __name__ == "__main__":
    main()
