#!/usr/bin/env python3
"""Check whether Google's Knowledge Graph recognizes each entity on the map.

Uses the official Knowledge Graph Search API (free, API key, no scraping).
For each entity name it prints the top Knowledge Graph matches with their
types, description and URL, and flags whether any match points at one of the
entity's own domains. That is the signal that Google has tied the name to you
rather than to a namesake.

Setup (one time, free):
  - In a Google Cloud project, enable "Knowledge Graph Search API".
  - Create an API key (APIs & Services -> Credentials); restrict it to that API.
  - Keep it out of git: export it from a chmod-600 env file.

Env:
  KG_API_KEY    API key                                             (required)
  KG_QUERIES    comma-separated entity names, e.g. "Jane Doe,Acme Labs,Acme Contrast Checker"
                                                                    (required)
  KG_DOMAINS    comma-separated domains that count as "yours", e.g.
                "example.org,acmelabs.example"                      (optional)
  KG_LIMIT      matches per query (default 5)

Not in the Knowledge Graph yet is normal for new people, products and small
companies. Track it over months, not days. The API only shows entities Google
has already consolidated; it cannot be influenced directly, only by the on-site
and off-site work in this skill.
"""

import json
import os
import sys
import urllib.parse
import urllib.request

API = "https://kgsearch.googleapis.com/v1/entities:search"


def env_list(name: str) -> list[str]:
    return [x.strip() for x in os.environ.get(name, "").split(",") if x.strip()]


def search(query: str, key: str, limit: int) -> list[dict]:
    params = urllib.parse.urlencode({"query": query, "key": key, "limit": limit})
    with urllib.request.urlopen(f"{API}?{params}", timeout=20) as resp:
        data = json.load(resp)
    return data.get("itemListElement", [])


def main() -> int:
    key = os.environ.get("KG_API_KEY")
    queries = env_list("KG_QUERIES")
    if not key or not queries:
        print("Set KG_API_KEY and KG_QUERIES (see the docstring).", file=sys.stderr)
        return 2
    domains = [d.lower() for d in env_list("KG_DOMAINS")]
    limit = int(os.environ.get("KG_LIMIT", "5"))

    for q in queries:
        print(f"\n== {q}")
        try:
            items = search(q, key, limit)
        except Exception as e:  # network/API errors: report and keep going
            print(f"   error: {e}")
            continue
        if not items:
            print("   not in the Knowledge Graph (yet)")
            continue
        mine = False
        for it in items:
            r = it.get("result", {})
            url = r.get("url") or r.get("detailedDescription", {}).get("url", "")
            types = ",".join(t for t in r.get("@type", []) if t != "Thing")
            is_mine = bool(url) and any(d in url.lower() for d in domains)
            mine |= is_mine
            flag = "  <- yours" if is_mine else ""
            desc = r.get("description", "")
            print(f"   {it.get('resultScore', 0):>8.1f}  {r.get('name', '?')} [{types}] {desc} {url}{flag}")
        if domains and not mine:
            print("   none of these point at your domains: the name still resolves to someone/something else")
    return 0


if __name__ == "__main__":
    sys.exit(main())
