#!/usr/bin/env python3
"""Merge results_N.csv files from reclassification agents back into master.csv.

Each results row: id, new_focus_area (blank=unchanged), new_subcategory, summary
"""
import csv
from pathlib import Path

DATA = Path(__file__).parent

def main():
    # Load all results
    updates = {}
    for i in range(4):
        p = DATA / f"results_{i}.csv"
        if not p.exists():
            print(f"MISSING: {p}")
            continue
        for r in csv.DictReader(open(p)):
            post_id = r.get("id", "").strip()
            if not post_id:
                continue
            updates[post_id] = {
                "new_focus_area": (r.get("new_focus_area") or "").strip(),
                "new_subcategory": (r.get("new_subcategory") or "").strip(),
                "summary": (r.get("summary") or "").strip(),
            }
    print(f"Loaded {len(updates)} updates")

    # Load master, apply
    master_path = DATA / "master.csv"
    rows = list(csv.DictReader(open(master_path)))
    fields = list(rows[0].keys())

    reclassified_fa = 0
    reclassified_sub = 0
    with_summary = 0
    for r in rows:
        u = updates.get(r["id"])
        if not u:
            continue
        if u["new_focus_area"] and u["new_focus_area"] != r["focus_area"]:
            r["focus_area"] = u["new_focus_area"]
            reclassified_fa += 1
        if u["new_subcategory"] and u["new_subcategory"] != r["subcategory"]:
            r["subcategory"] = u["new_subcategory"]
            reclassified_sub += 1
        if u["summary"]:
            r["summary"] = u["summary"]
            with_summary += 1

    with open(master_path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)

    print(f"  focus_area reassigned: {reclassified_fa}")
    print(f"  subcategory changed:   {reclassified_sub}")
    print(f"  summaries added:       {with_summary}")
    print(f"Wrote master.csv")

if __name__ == "__main__":
    main()
