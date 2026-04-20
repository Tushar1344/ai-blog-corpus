#!/usr/bin/env python3
"""Merge hs_results_N.csv files (summaries + signal refinements) into master.csv."""
import csv
from pathlib import Path
from collections import Counter

DATA = Path(__file__).parent

def main():
    updates = {}
    for i in range(4):
        p = DATA / f"hs_results_{i}.csv"
        if not p.exists():
            print(f"MISSING: {p}")
            continue
        for r in csv.DictReader(open(p)):
            rid = (r.get("id") or "").strip()
            if not rid:
                continue
            updates[rid] = {
                "summary": (r.get("summary") or "").strip(),
                "new_L": (r.get("new_signal_learning") or "").strip(),
                "new_N": (r.get("new_signal_novelty") or "").strip(),
                "new_A": (r.get("new_signal_actionability") or "").strip(),
                "refined_sub": (r.get("refined_subcategory") or "").strip(),
            }
    print(f"Loaded {len(updates)} updates")

    path = DATA / "master.csv"
    rows = list(csv.DictReader(open(path)))
    fields = list(rows[0].keys())

    n_summary = 0
    n_sig_l = n_sig_n = n_sig_a = 0
    n_sub = 0
    n_fail = 0
    for r in rows:
        u = updates.get(r["id"])
        if not u:
            continue
        if u["summary"]:
            if u["summary"] == "content-fetch-failed":
                n_fail += 1
            else:
                r["summary"] = u["summary"]
                n_summary += 1
        if u["new_L"] in ("H", "M", "L") and u["new_L"] != r.get("signal_learning"):
            r["signal_learning"] = u["new_L"]
            n_sig_l += 1
        if u["new_N"] in ("H", "M", "L") and u["new_N"] != r.get("signal_novelty"):
            r["signal_novelty"] = u["new_N"]
            n_sig_n += 1
        if u["new_A"] in ("H", "M", "L") and u["new_A"] != r.get("signal_actionability"):
            r["signal_actionability"] = u["new_A"]
            n_sig_a += 1
        if u["refined_sub"] and u["refined_sub"] != r.get("subcategory"):
            r["subcategory"] = u["refined_sub"]
            n_sub += 1

    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)

    print(f"  summaries added:           {n_summary}")
    print(f"  content-fetch-failed:      {n_fail}")
    print(f"  learning revised:          {n_sig_l}")
    print(f"  novelty revised:           {n_sig_n}")
    print(f"  actionability revised:     {n_sig_a}")
    print(f"  subcategory refined:       {n_sub}")

if __name__ == "__main__":
    main()
