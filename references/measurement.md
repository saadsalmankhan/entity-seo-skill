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
- **Query breakdown**: every recorded query is auto-bucketed (exact name /
  name + platform / name + role / name + location / name + other / partial /
  non-name) with an impression-weighted average position per bucket. At low
  volume, single-query rows are noise; buckets make the exact-name fight vs
  the winnable name+modifier queries legible at a glance.
- **Country split** for the name query (`dimensions=["query","country"]`):
  GSC's headline average blends all countries and can hide a page-1 position
  at home behind a global position of 70+.
- **Page dimension + totals**: Google anonymizes rare long-tail queries — they
  never appear as query rows but their impressions DO appear per-page and in
  the no-dimension totals. Reporting `totals − visible query impressions`
  surfaces that hidden activity; the per-page list shows where it landed.
- **Trend vs the prior 28 days**: on a new site, impressions move before
  position does — trend the impressions, not just the rank.

### Reading GSC numbers honestly
- **Average position is survivor-biased**: it averages only the times the site
  actually appeared. One appearance at position 8 out of thousands of searches
  prints as "position 8". Read position together with impressions.
- **A missing query row ≠ position 100.** It means zero impressions — GSC
  cannot see queries where the site never surfaced at all.

## Real-SERP spot checks (what GSC can't see)
GSC only reports queries where the site got an impression, so it can't answer
"where do I rank for X?" when the site doesn't surface for X at all. Options,
as of late 2026:
- **Google's Programmable Search Engine "search the entire web" mode is
  deprecated** for new engines — the old free official way to approximate full
  Google results via the Custom Search JSON API is gone.
- **Google no longer honors `num=100`**: any SERP fetch returns ~10 results per
  page. Rank checks must paginate (2 pages ≈ top 20) and should report
  "beyond page 2" as `>20`, not a fake `>100`.
- **Don't scrape google.com directly** — bot detection blocks it almost
  immediately and it's against ToS. Use a SERP API (SerpApi has a recurring
  free tier of ~100 searches/month; Serper/DataForSEO are cheap paid options)
  and budget it: ~10 keywords × 2 pages weekly ≈ 80 searches/month.
- **Scan for every owned property** (personal site, GitHub, product domains) —
  a name+project query often ranks the GitHub repo or product site before the
  personal site, and that still wins the SERP for the entity.
- **Scout before you track**: spend a few API calls checking candidate
  queries. A thin SERP (Google returns only a handful of results) signals weak
  competition — those name+modifier and niche-project queries are usually the
  winnable ones, while two-word head terms are owned by aggregators.

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

## Relationship checks (is the map being understood?)
Rank for the name is one number. Entity SEO is working when search engines and
AI assistants answer **relationship questions** correctly. Two checks:

**Knowledge Graph (official, free).** `scripts/kg_check.py` queries Google's
Knowledge Graph Search API for each entity on the map and flags whether a match
points at the entity's own domains:
```bash
export KG_API_KEY=...            # from a chmod-600 env file, never committed
export KG_QUERIES="Jane Doe,Acme Labs,Acme Contrast Checker"
export KG_DOMAINS="example.org,acmelabs.example"
python3 scripts/kg_check.py
```
"Not in the Knowledge Graph yet" is normal for new people, products and small
companies. Trend it over months. The API can't be influenced directly; it
reflects the on-site and off-site work.

**Relationship questions (manual).** Ask each `relationship_questions` entry in
`entities.yaml` ("Who founded Acme Labs?", "Who makes the Acme Contrast
Checker?") in Google and 1–2 AI assistants (ChatGPT Search, Perplexity, Gemini).
Log answer / correct? / source cited, per date. A wrong or missing answer points
at the exact line that needs more support (on-site statement, schema, off-site
confirmation or content). Never scrape or automate these; ask them yourself.

## GEO/AEO signal checks
- Search Console → **Enhancements** shows valid/invalid counts for any FAQ/HowTo
  markup added by the `site` action (`references/geo-aeo.md`) — fix invalid items
  immediately.
- There's no free official API for AI-Overview or assistant citations. Treat
  whether an AI search cites `{ENTITY}` as a manual, periodic spot-check (ask
  ChatGPT Search / Perplexity / Gemini the name query yourself), not something to
  automate or scrape.

## What "working" looks like
- **Week 1:** little movement — Google is still recrawling. Don't refresh Google
  manually; it tells you nothing.
- **Weeks 2–4:** impressions rise, average position settles and drops. This is where
  the entity fixes show up.
- Check **weekly**, not hourly.
- If rank stalls after on-site is complete, the answer is more **off-site
  confirmation of the relationships and more content that demonstrates them**,
  not more on-site tweaks.

## Monitoring cadence
- **Weekly**: review the rank-check output (average position trend for
  `{ENTITY}` and the name + company/product queries); skim Search Console
  impressions/clicks for anything new.
- **Monthly**: content-quality audit against `references/on-site.md`'s checklist
  (word count, grammar, does each page still directly answer its target
  question) on every key page; spot-check the target voice/AI queries on
  whatever assistants are on hand (`references/local-voice-seo.md`), logging
  any change from the last check.
- **Monthly (relationships)**: ask the `relationship_questions` from
  `entities.yaml` in Google and 1–2 AI assistants and log the answers; run
  `scripts/kg_check.py`.
- **Quarterly**: re-read `entities.yaml` with the owner: new products, role
  changes or a rebrand go in first, then re-run `audit`. Re-run the off-site checklist (`references/off-site.md`) to
  confirm every profile link still resolves and nothing has drifted; revisit
  the FAQ question set — are these still real questions people ask, or has the
  entity landscape shifted (new namesakes, a role change)?
