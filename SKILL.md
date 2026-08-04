---
name: entity-seo
description: Rank a person or brand at the top for their own name, with full-site SEO, GEO (AI/generative search), and AEO (answer engines & voice) technique coverage along the way. Use when someone owns a matching domain but is outranked by same-name entities (a business, a celebrity, hundreds of namesakes), the site is new and low-authority, or they want a broader SEO/GEO/AEO tune-up while fixing the name-ranking problem. Walks through diagnosis, on-site SEO (titles, meta/headings/URLs, canonicals, a JSON-LD entity graph, sitemap/robots, image SEO), GEO & AEO (E-E-A-T, AI-citable content, featured-snippet formatting, FAQ/HowTo/Speakable schema, voice search), off-site authority (profile links and backlinks), first-hand content, free Google Search Console rank measurement with a daily automation, and an optional agency-style Word/PDF report with color-coded scores. Works for individuals and organizations. Triggers on requests like "rank me for my name", "I'm not the top result for my own name", "improve my personal/brand SEO", "why does another Saad Salman outrank me", "track my Google rank", "audit my site for SEO/GEO/AEO".
---

# Entity SEO — rank a person or brand for their own name

The goal is winning the **exact-name query**. The blocker is usually **entity
ambiguity + authority**, not discovery: the site is (or soon will be) indexed, but
other entities share the name, or the site is too new to be trusted yet.

## Guardrails (state these to the user early, and never break them)

- **No guarantees.** You cannot promise position #1. Rankings vary by user,
  location, and device, and changes take **days to weeks** to show after indexing.
- **Legitimate tactics only.** Never scrape Google SERPs, bypass/solve CAPTCHAs,
  buy backlinks, spam directories, or create fake profiles. These violate ToS and
  backfire.
- **Only real, owned profiles** go in `sameAs` and off-site links.
- **Truth and consistency.** Every published claim (site, résumé/PDF, schema, every
  profile) must be accurate and match. Contradictions confuse the entity.
- **Secrets are secrets.** API keys and service-account keys: chmod 600, never
  committed, never printed.

## Workflow

Run these phases in order. Do on-site first (fast, high-certainty); the durable
wins come from off-site authority and content.

### 1. Diagnose
1. Search the name incognito. Note **who outranks the site and why** (established
   business, Wikipedia/IMDb entity, LinkedIn, namesakes).
2. Check indexing: `site:{DOMAIN}`. Inspect the homepage, about page, and any
   indexed PDFs (résumés, brochures) — stale PDFs are a common contradiction.
3. Classify the gap: *discovery* (not indexed) vs *ambiguity/authority* (indexed
   but buried). Most sites are the latter.
4. Inventory every existing public surface (LinkedIn, GitHub, company page,
   university, press, résumé) — these are consolidation targets for later.

### 2. On-site: SEO, GEO & AEO
Read `references/on-site.md` and `references/geo-aeo.md`, and apply both. Summary:
- Titles: `{ENTITY} | {ROLE} — {Specialties}`; unique per-page titles/descriptions;
  use **absolute** titles if a title template would double-suffix the name.
- Meta descriptions, heading hierarchy, URL structure, OG/Twitter cards — see
  on-site.md's "Meta, headings & URL fundamentals".
- **Per-page canonicals** — never one canonical in the root layout (it leaks to
  every page).
- About/company `<h1>` contains the full name; add a labelled identity block; put
  name+role in the first paragraph.
- A single JSON-LD `@graph`: `WebSite` + `Person`/`Organization` site-wide,
  `ProfilePage`/`AboutPage` on the about page, `Article`/`BlogPosting` author →
  central `@id` on every post. See the examples in the reference.
- `sitemap.xml` + `robots.txt` (don't block known AI crawlers without reason).
- Image SEO: descriptive filename + alt, same photo/logo everywhere, referenced in
  schema `image`.
- Fix indexed PDFs at the **same URL** (update text **and** metadata).
- **GEO**: E-E-A-T signals, lead-with-the-answer content structure, AI-crawlable
  rendering — see geo-aeo.md.
- **AEO**: question-phrased headings with direct-answer paragraphs, `FAQPage`/
  `HowTo`/`Speakable` schema where genuine content supports it — see geo-aeo.md.

Deliverable: a deployable patch. Verify with a build and by inspecting the
rendered `<title>`, canonical, and JSON-LD (including any FAQ/HowTo schema added).

### 3. Off-site authority
Read `references/off-site.md`. Produce a personalized checklist and draft what you
can (READMEs, republish canonicals). Core move: put `{DOMAIN}` in the
**machine-readable URL field** of every real profile — not just bio prose.

### 4. Content
Publish substantive, first-hand articles/case studies in the entity's field. Each
is another indexed page reinforcing "{ENTITY} = {TOPIC}" and wins long-tail queries.
Author bio links the name → `/about`. No generic AI summaries — real decisions,
numbers, outcomes.

### 5. Measure & automate
Read `references/measurement.md`. Set up Google Search Console, submit the sitemap,
request indexing on key pages, and stand up the daily rank check
(`scripts/gsc_rank.py` — the free, accurate GSC API version). Watch **average
position** for the name query trend toward 1 over 2–4 weeks. Check Search Console →
Enhancements for FAQ/HowTo schema validity if Phase 2's AEO work added any.

Optional deliverable: if the entity wants something to keep or hand to a
stakeholder, read `references/reporting.md` and generate a color-coded Word/PDF
scorecard — once as a baseline after Phase 1, and again after each Iterate cycle
to show delta.

### 6. Iterate
Weekly: review average position and indexed-page count. If on-site is done and rank
is stuck, the lever is **more off-site authority and more content** — not more
on-site tweaks.

## Individual vs organization

- **Individual:** schema `Person`; off-site = LinkedIn, GitHub, Wellfound,
  Crunchbase (person), university/alumni, podcasts.
- **Organization:** schema `Organization`/`LocalBusiness`; off-site = **Google
  Business Profile** (biggest lever for local/physical presence), industry
  directories, press/PR, Crunchbase (company), review sites; watch NAP consistency
  and reviews. See the org column in each reference file.
