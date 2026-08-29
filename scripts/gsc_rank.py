#!/usr/bin/env python3
"""Daily Google Search Console rank check for an entity's name queries.

Reads a service-account key and queries the Search Analytics API for a Search
Console *Domain* property, then prints a short rank report. Free, official, and
ToS-compliant — no SERP scraping.

What the report contains and why:
  - Tracked-query table — exact-match positions for the queries you list.
  - Query breakdown — every query GSC recorded, auto-bucketed (exact name /
    name + platform / name + role / name + location / name + other / partial /
    non-name) with impression-weighted average position per bucket. Separates
    the bare-name fight from the name+modifier queries you can actually win.
  - Country split for the name query — GSC's blended average hides huge geo
    differences (position 9 at home can average out to 70 globally).
  - Pages getting impressions — catches activity from long-tail queries Google
    anonymizes (they never appear as query rows but do appear per-page).
  - Totals + anonymized gap + trend vs the prior 28 days — for a new site,
    impressions move before position does; trend the impressions.

Setup (see references/measurement.md):
  - Enable the Search Console API on a Google Cloud project (no billing needed).
  - Create a service account (no IAM role) + a JSON key.
  - In Search Console, add the service-account email as a Restricted user.

Config via environment variables:
  GSC_KEY_PATH        path to the service-account JSON key          (required)
  GSC_SITE            property id, e.g. "sc-domain:example.org"     (required)
  GSC_QUERIES         comma-separated queries to track exactly      (required)
  GSC_NAME            the entity name for bucketing (defaults to the
                      first entry of GSC_QUERIES)
  GSC_ROLE_WORDS      extra role words for bucketing, comma-separated
  GSC_LOCATION_WORDS  extra location words for bucketing, comma-separated

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
NAME = os.environ.get("GSC_NAME", QUERIES[0] if QUERIES else "").lower()
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]


def _env_words(var):
    return {w.strip().lower() for w in os.environ.get(var, "").split(",") if w.strip()}


PLATFORM_WORDS = {"linkedin", "github", "twitter", "x", "instagram", "facebook",
                  "youtube", "medium", "reddit", "tiktok"}
ROLE_WORDS = {"engineer", "developer", "designer", "manager", "consultant",
              "founder", "resume", "cv"} | _env_words("GSC_ROLE_WORDS")
LOCATION_WORDS = _env_words("GSC_LOCATION_WORDS")
GROUP_ORDER = ["exact name", "name + platform", "name + role", "name + location",
               "name + other", "partial name", "non-name"]


def classify_query(q):
    if q == NAME:
        return "exact name"
    if NAME and NAME in q:
        extra = set(q.replace(NAME, " ").split())
        if extra & PLATFORM_WORDS:
            return "name + platform"
        if extra & ROLE_WORDS:
            return "name + role"
        if extra & LOCATION_WORDS:
            return "name + location"
        return "name + other"
    if NAME and set(q.split()) & set(NAME.split()):
        return "partial name"
    return "non-name"


def get_token():
    creds = service_account.Credentials.from_service_account_file(KEY_PATH, scopes=SCOPES)
    creds.refresh(Request())
    return creds.token


def query(token, start, end, dimensions):
    url = (
        "https://searchconsole.googleapis.com/webmasters/v3/sites/"
        + urllib.parse.quote(SITE, safe="")
        + "/searchAnalytics/query"
    )
    body = json.dumps({
        "startDate": start, "endDate": end,
        "dimensions": dimensions, "rowLimit": 25000,
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
    prev_end = start - dt.timedelta(days=1)
    prev_start = prev_end - dt.timedelta(days=27)
    s, e = start.isoformat(), end.isoformat()

    data = query(token, s, e, ["query"])
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

    # Bucket every recorded query by modifier type, weighted by impressions
    groups = {}
    for r in rows:
        groups.setdefault(classify_query(r["keys"][0].lower()), []).append(r)
    print("\nQuery breakdown (weighted by impressions):")
    print("| Group | Queries | Impressions | Clicks | Avg position |")
    print("|---|---|---|---|---|")
    for g in GROUP_ORDER:
        rs = groups.get(g)
        if not rs:
            continue
        impr = sum(int(r["impressions"]) for r in rs)
        clicks = sum(int(r["clicks"]) for r in rs)
        wpos = sum(r["position"] * r["impressions"] for r in rs) / impr if impr else 0
        print(f"| {g} | {len(rs)} | {impr} | {clicks} | {wpos:.1f} |")

    # Country split for the name query — the blended average hides geo differences
    if NAME:
        qc = query(token, s, e, ["query", "country"]).get("rows", [])
        name_by_country = [r for r in qc if r["keys"][0].lower() == NAME]
        if name_by_country:
            parts = [f"{r['keys'][1].upper()} pos {r['position']:.1f} ({int(r['impressions'])} impr)"
                     for r in sorted(name_by_country, key=lambda r: r["impressions"], reverse=True)]
            print(f"\n\"{NAME}\" by country: " + "; ".join(parts))

    top = sorted(rows, key=lambda r: r["impressions"], reverse=True)[:5]
    print("\nTop queries by impressions:")
    for r in top:
        print(f"  - {r['keys'][0]}  (pos {r['position']:.1f}, {int(r['impressions'])} impr)")

    # Page-level impressions catch activity from queries GSC anonymizes
    pages = query(token, s, e, ["page"]).get("rows", [])
    if pages:
        print("\nPages getting impressions:")
        for r in sorted(pages, key=lambda r: r["impressions"], reverse=True)[:6]:
            print(f"  - {r['keys'][0]}  (pos {r['position']:.1f}, "
                  f"{int(r['impressions'])} impr, {int(r['clicks'])} clicks)")

    # Totals, anonymized-query gap, and trend vs the prior 28 days
    tot_rows = query(token, s, e, []).get("rows", [])
    prev_rows = query(token, prev_start.isoformat(), prev_end.isoformat(), []).get("rows", [])
    if tot_rows:
        tot = tot_rows[0]
        visible = sum(int(r["impressions"]) for r in rows)
        hidden = int(tot["impressions"]) - visible
        line = (f"\nTotals: {int(tot['impressions'])} impressions, {int(tot['clicks'])} clicks, "
                f"avg pos {tot['position']:.1f}")
        if prev_rows:
            prev = prev_rows[0]
            delta = int(tot["impressions"]) - int(prev["impressions"])
            line += f" ({'+' if delta >= 0 else ''}{delta} impressions vs prior 28d)"
        print(line)
        if hidden > 0:
            print(f"  ({hidden} impressions from long-tail queries Google anonymizes — "
                  f"see the pages list above for where they landed)")

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
