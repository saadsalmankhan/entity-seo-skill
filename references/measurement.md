# Measurement & automation

## Google Search Console (ground truth)
1. Add a **Domain** property (covers www/non-www/http/https at once) → verify with
   the DNS **TXT** record it gives you. Leave the record in place permanently.
2. Submit `sitemap.xml` (type just `sitemap.xml` in the Sitemaps box).
3. **URL-inspect + Request indexing** the homepage, about page, and any updated
   PDFs so new titles/schema get recrawled sooner. (It's a nudge, not instant.)
4. Confirm Google's chosen canonical matches yours; confirm no page is `noindex`.
5. Monitor: **Performance → filter Query = "{ENTITY}" → Average position** (trend it
   toward 1), plus impressions, clicks, and Indexing → Pages count.

## Daily rank automation

Two legitimate data sources:
- **WebSearch/API proxy** — zero setup, but approximate and often region-locked
  (e.g. a US-only index that won't match a local SERP). Fine as a directional signal.
- **GSC Search Analytics API** — the accurate number. **Free, no Cloud billing
  required.** Recommended.

### GSC API setup (one time, ~10 min, free)
1. Create a Google Cloud project → enable the **Search Console API**.
2. Create a **service account**. **No IAM role needed** — skip the "grant access to
   project" step.
3. Create a **JSON key** for it; download and store it locked down (`chmod 600`),
   never in git.
4. In Search Console → Settings → **Users and permissions → Add user** → paste the
   service-account email → permission **Restricted** (enough for read-only Search
   Analytics). Propagation can take ~1 minute — a `403` immediately after adding is
   normal; retry shortly.

### The script
`scripts/gsc_rank.py` queries the Search Analytics API and prints a short report.
Key implementation notes baked in:
- Auth via the service-account key + scope `webmasters.readonly`.
- Property id for a Domain property is `sc-domain:{DOMAIN}` (URL-encode the `:`).
- Query `dimensions=["query"]` over a ~28-day window **ending ~2 days ago** (GSC
  data lags ~2 days), then pull each target query's `position`/`impressions`/`clicks`.
- Handle the empty-`rows` case: a newly verified property returns no rows → report
  "No data yet" instead of crashing.

Configure via environment variables:
```bash
export GSC_KEY_PATH=/secure/path/sa-key.json
export GSC_SITE=sc-domain:example.org
export GSC_QUERIES="jane doe,jane doe designer,jane doe portfolio"
python3 scripts/gsc_rank.py
```

### Schedule it
Run it daily on whatever scheduler you use (cron, a Claude Code scheduled task, a
CI cron, etc.). Optionally email the report through an existing transactional
sender (Resend/SMTP) — read the key from the environment, never hardcode it.

## What "working" looks like
- **Week 1:** little movement — Google is still recrawling. Don't refresh Google
  manually; it tells you nothing.
- **Weeks 2–4:** impressions rise, average position settles and drops. This is where
  the entity fixes show up.
- Check **weekly**, not hourly.
- If rank stalls after on-site is complete, the answer is more **off-site authority
  and content**, not more on-site tweaks.
