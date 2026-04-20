#!/usr/bin/env python3
"""Recompute signal_overall + signal_priority from existing L/N/A values.
Does NOT re-assign L/N/A — preserves agent-refined judgments."""
import csv
from pathlib import Path

DATA = Path(__file__).parent

def main():
    path = DATA / "master.csv"
    rows = list(csv.DictReader(open(path)))
    fields = list(rows[0].keys())

    scored = 0
    for r in rows:
        if r.get("in_scope") != "TRUE" or r.get("dropped_in_v2") == "TRUE":
            continue
        l = r.get("signal_learning", "")
        n = r.get("signal_novelty", "")
        a = r.get("signal_actionability", "")
        if l not in ("H","M","L") or n not in ("H","M","L") or a not in ("H","M","L"):
            continue

        letters = [l, n, a]
        nH = letters.count("H")
        nL = letters.count("L")
        if nH >= 2:
            overall = "H"
        elif nH == 1 and nL == 0:
            overall = "H"
        elif nH == 1 and nL >= 1:
            overall = "M"
        elif nL >= 2 and nH == 0:
            overall = "L"
        else:
            overall = "M"

        wL = {"H": 3, "M": 2, "L": 1}
        priority = round(wL[n] * 1.2 + wL[l] * 1.1 + wL[a] * 1.0, 1)

        r["signal_overall"] = overall
        r["signal_priority"] = f"{priority}"
        scored += 1

    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    in_scope = [r for r in rows if r.get("in_scope") == "TRUE" and r.get("dropped_in_v2") == "FALSE"]
    print(f"Recomputed {scored} overall/priority values\n")
    print("signal_overall distribution:")
    for k, v in Counter(r["signal_overall"] for r in in_scope).most_common():
        print(f"  {k}: {v} ({100*v/len(in_scope):.0f}%)")

    # High-signal by company
    print("\nHigh-signal by company:")
    h_by_co = Counter(r["company"] for r in in_scope if r["signal_overall"] == "H")
    total_by_co = Counter(r["company"] for r in in_scope)
    for co, c in h_by_co.most_common():
        pct = 100 * c / total_by_co[co] if total_by_co[co] else 0
        print(f"  {co:25} {c}/{total_by_co[co]} ({pct:.0f}% high-signal)")

if __name__ == "__main__":
    main()
