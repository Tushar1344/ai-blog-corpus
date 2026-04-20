#!/usr/bin/env python3
"""Upload master.csv to the Google Sheet."""
import csv
import json
import subprocess
import urllib.request
from pathlib import Path

DATA = Path(__file__).parent
SHEET_ID = "1td1T6wCEnw4EeG05I_hH1dK1aNkLR5HJZZ-4jr-Du9A"

def get_token():
    r = subprocess.run(["python3",
        "/Users/tushar.madan/.claude/plugins/cache/fe-vibe/fe-google-tools/1.1.1/skills/google-auth/resources/google_auth.py",
        "token"], capture_output=True, text=True)
    return r.stdout.strip()

def main():
    rows = list(csv.reader(open(DATA / "master.csv")))
    print(f"Uploading {len(rows)} rows (incl header)...")

    # Sort in-scope first, then by company, then by publish_date desc
    header = rows[0]
    body = rows[1:]
    def sort_key(r):
        in_scope = r[7] == "TRUE"
        company = r[1]
        date = r[5] or "0000-00-00"
        return (not in_scope, company, date)
    # Invert date for desc
    body.sort(key=lambda r: (not (r[7] == "TRUE"), r[1], r[5]), reverse=False)
    body.sort(key=lambda r: r[5] or "0000-00-00", reverse=True)
    body.sort(key=lambda r: (not (r[7] == "TRUE"), r[1]))

    final = [header] + body

    token = get_token()
    # Batch update in chunks of 1000 rows
    BATCH = 500
    total = len(final)
    for i in range(0, total, BATCH):
        chunk = final[i:i+BATCH]
        start_row = i + 1
        end_row = i + len(chunk)
        rng = f"master!A{start_row}:Y{end_row}"
        payload = {"values": chunk}
        req = urllib.request.Request(
            f"https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}/values/{rng}?valueInputOption=RAW",
            data=json.dumps(payload).encode("utf-8"),
            method="PUT",
            headers={
                "Authorization": f"Bearer {token}",
                "x-goog-user-project": "gcp-sandbox-field-eng",
                "Content-Type": "application/json",
            })
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                body_resp = json.loads(resp.read().decode())
                print(f"  rows {start_row}-{end_row}: updated {body_resp.get('updatedCells', 0)} cells")
        except Exception as e:
            print(f"  rows {start_row}-{end_row}: FAIL {e}")

    print(f"\nSheet URL: https://docs.google.com/spreadsheets/d/{SHEET_ID}/edit")

if __name__ == "__main__":
    main()
