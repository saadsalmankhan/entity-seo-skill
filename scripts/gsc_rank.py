#!/usr/bin/env python3
"""Daily Google Search Console rank check for an entity's name queries.

Reads a service-account key and queries the Search Analytics API for a Search
Console *Domain* property, then prints a short rank report. Free, official, and
ToS-compliant — no SERP scraping.

Setup (see references/measurement.md):
  - Enable the Search Console API on a Google Cloud project (no billing needed).
  - Create a service account (no IAM role) + a JSON key.
  - In Search Console, add the service-account email as a Restricted user.

Config via environment variables:
  GSC_KEY_PATH   path to the service-account JSON key   (required)
  GSC_SITE       property id, e.g. "sc-domain:example.org"   (required)
  GSC_QUERIES    comma-separated name queries to track   (required)

The key is a secret: this script never prints it.

Requires: pip install google-auth
"""
import datetime as dt
import json
import os
import sys
import urllib.parse
import urllib.request

from google.oauth2 import service_account
from google.auth.transport.requests import Request

KEY_PATH = os.environ.get("GSC_KEY_PATH")
SITE = os.environ.get("GSC_SITE")  # e.g. "sc-domain:example.org"
QUERIES = [q.strip() for q in os.environ.get("GSC_QUERIES", "").split(",") if q.strip()]
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]


def get_token():
    creds = service_account.Credentials.from_service_account_file(KEY_PATH, scopes=SCOPES)
    creds.refresh(Request())
    return creds.token


def query(token, start, end):
    url = (
        "https://searchconsole.googleapis.com/webmasters/v3/sites/"
        + urllib.parse.quote(SITE, safe="")
        + "/searchAnalytics/query"
    )
    body = json.dumps({
        "startDate": start, "endDate": end,
        "dimensions": ["query"], "rowLimit": 25000,
    }).encode()
    req = urllib.request.Request(
        url, data=body,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())


def main():
    if not (KEY_PATH and SITE and QUERIES):
        print("Set GSC_KEY_PATH, GSC_SITE, and GSC_QUERIES environment variables.",
              file=sys.stderr)
        sys.exit(2)

    token = get_token()
    end = dt.date.today() - dt.timedelta(days=2)     # GSC data lags ~2 days
    start = end - dt.timedelta(days=27)              # 28-day window
    data = query(token, start.isoformat(), end.isoformat())
    rows = data.get("rows", [])
    by_query = {r["keys"][0].lower(): r for r in rows}

    print(f"# Search Console rank — {dt.date.today().isoformat()}")
    print(f"Window: {start} to {end} (28 days, ~2-day GSC lag)\n")

    if not rows:
        print("No data yet. Search Console has not recorded impressions for this "
              "property in the window. Normal for a newly verified property or a "
              "site Google has not re-crawled yet — check again in a few days.")
        return

    print("| Query | Avg position | Impressions | Clicks |")
    print("|---|---|---|---|")
    for q in QUERIES:
        r = by_query.get(q.lower())
        if r:
            print(f"| {q} | {r['position']:.1f} | {int(r['impressions'])} | {int(r['clicks'])} |")
        else:
            print(f"| {q} | not showing (0 impressions) | 0 | 0 |")

    top = sorted(rows, key=lambda r: r["impressions"], reverse=True)[:5]
    print("\nTop queries by impressions:")
    for r in top:
        print(f"  - {r['keys'][0]}  (pos {r['position']:.1f}, {int(r['impressions'])} impr)")

    primary = by_query.get(QUERIES[0].lower())
    if primary:
        p = primary["position"]
        state = "#1 already 🎉" if p < 1.5 else f"~position {p:.1f} — {'close' if p < 5 else 'climbing'}"
        print(f"\nTakeaway: for \"{QUERIES[0]}\", you're at {state}.")
    else:
        print(f"\nTakeaway: \"{QUERIES[0]}\" has no impressions yet in this window.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa
        print(f"ERROR: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
