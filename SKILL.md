---
name: entity-seo
description: Entity SEO for a person or brand. Maps every entity (person, brand, legal company, each product and service, ideas and slogans), writes down why each relationship exists, then reinforces those relationships everywhere (a multi-entity JSON-LD graph, entity pages, titles, profiles, articles, images, video) so search engines and AI assistants learn who built what and who works where. Split into actions (map, audit, site, reinforce, content, measure, report) sharing one entities.yaml; with no argument it picks the next step. Includes on-site SEO, GEO, AEO, local SEO, off-site authority, free Search Console rank and Knowledge Graph checks, and an optional scored report. For individuals and organizations. Triggers on "do entity SEO for me", "map my entities", "Google doesn't connect me to my company/product", "rank me for my name", "another person with my name outranks me", "audit my site for SEO/GEO/AEO", "track my Google rank".
---

# Entity SEO

Entity SEO means helping Google and AI-powered search understand **your entities
and the relationships between them**. It isn't only ranking for your name.

Your personal name is an entity. So is your brand name. So is your company name,
if it differs from the brand. Each product or service you sell is one, and so is
an idea or a slogan. If search engines can't tell how those connect (who founded
what, which company makes which product, who is behind which idea), you haven't
started entity SEO yet.

The test: draw every entity as a node and a line between each related pair. Can
you explain why you drew each line? When you can, you understand your entities.
Content and schema then exist to **reinforce the reason each line is there**.

Entity SEO isn't a separate campaign. It sits around everything else you do:
every profile, article, post, title, description, image and video either confirms
the lines on the map or misses the chance to. Rank for the exact name is one
result you measure (see `references/measurement.md`). It isn't the goal itself.

## Guardrails (state these early and never break them)

- **No guarantees.** You can't promise a Knowledge Panel or position #1. Results vary
  by user, location and device, and take **days to weeks** after indexing.
- **Only true relationships.** Every line on the map must survive a fact-check. No
  invented partnerships, awards, "as seen in", products or frameworks.
- **Legitimate tactics only.** Never scrape Google SERPs, bypass CAPTCHAs, buy
  links, spam directories or create fake profiles.
- **Only real, owned profiles** go in `sameAs` and off-site links.
- **Consistency.** The site, résumé/PDF, schema and every profile must describe the
  same entities and the same relationships. Contradictions confuse the graph.
- **Don't stuff it.** Reinforce relationships where they belong, the way a person
  would naturally write them. Skip the places where they don't fit.
- **Secrets are secrets.** API keys and service-account keys: `chmod 600`, never
  committed, never printed.

## How it runs: actions around one saved map

Entity SEO can't be done in one call. Some steps need the owner's judgment
(which relationships are true), some happen off the site (only the owner can edit
their LinkedIn), and results only show weeks later. So the skill is split into
actions. They all read and update **one file, `entities.yaml`**, kept in the
project (template: `templates/entities.yaml`). That shared file is what keeps
the schema, profile copy and articles describing the same relationships.

| Action | What it does | Reads | Output |
|---|---|---|---|
| `map` | Inventory entities, draw relationships with a one-line *why*, write the statement library. **Owner confirms.** | site, profiles, owner | `entities.yaml` + diagram |
| `audit` | Check each relationship: stated on-site? encoded in schema? confirmed off-site? answered correctly by search/AI? | `entities.yaml`, site, web | gap list, ranked |
| `site` | On-site fixes: multi-entity JSON-LD graph, a page per entity, titles/meta, internal links, image alt, plus technical SEO/GEO/AEO | `entities.yaml`, codebase | code patch, verified |
| `reinforce` | Draft copy for every off-site surface: profiles, bios, company page, listings, video descriptions | `entities.yaml` | copy-paste checklist for the owner |
| `content` | Plan/draft first-hand articles that demonstrate the relationships | `entities.yaml`, gaps | briefs or drafts |
| `measure` | GSC rank, Knowledge Graph check, relationship questions to AI assistants | `entities.yaml` | trend log |
| `report` | Optional color-coded Word/PDF scorecard | all of the above | `.docx`/`.pdf` |

**With no argument** (`/entity-seo`), pick the next step from the project's state:
no `entities.yaml` → `map`; map exists but no audit, or it's older than the
last site change → `audit`; open on-site gaps → `site`; open off-site gaps →
`reinforce`; site and profiles done → `content`, then `measure` on the cadence in
`references/measurement.md`. Say which action you picked and why, then run it.
The owner can always name an action explicitly (`/entity-seo audit`).

## Actions in detail

### map
Read `references/entity-map.md` and follow it:
1. Inventory entities from what already exists: the site (about page, product
   pages, footer, existing JSON-LD), résumé/PDF, LinkedIn, GitHub, company page.
2. Draw the relationship table: from, relationship, to, **why** (one plain
   sentence), schema property.
3. Give each entity a home: one canonical URL that is its `@id`.
4. Write the statement library: one-liners that name an entity **and** a related
   entity.
5. **Show the map to the owner and get it confirmed** before any later action
   uses it. Don't guess relationships into schema.

Individual vs organization: an individual's map centres on the Person
(employer, past employers, education, own products, topics). An organization's
map centres on the Organization (brand, founders, products/services, parent or
subsidiaries, locations). Both apply the same method.

### audit
For every relationship row, record four checks (see entity-map.md §6):
*stated* in visible text, *encoded* in JSON-LD with `@id` links, *confirmed*
off-site by an independent source, *answered* correctly when asked as a question
in Google and 1–2 AI assistants. Also run the classic diagnosis:
- incognito name search: who outranks the site, and why
- `site:{DOMAIN}` indexing check, plus stale indexed PDFs
- word count on key pages (flag under 500 words, or under 1500 for cornerstone pages)

Rank gaps by leverage. Broken person ↔ company ↔ product chains come first.

### site
Read `references/on-site.md` (the multi-entity graph, entity pages, titles,
canonicals, sitemap/robots, image SEO, content quality) and `references/geo-aeo.md`
(E-E-A-T, AI-citable content, query intent, answer formatting, and the
status table of which answer markup still earns anything). For local
businesses, read `references/local-voice-seo.md` too. Key moves:
- Every entity gets a node with its own `@id`; relationships reference other
  nodes by `@id`, never anonymous inline objects.
- Articles declare `about`/`mentions` for the entities they cover, as well as
  `author`.
- Visible text states each relationship the schema claims. Schema never claims
  what the page doesn't say.
Deliverable: a deployable patch. Verify with a build and by inspecting the
rendered JSON-LD (every `@id` reference resolves to a node in the graph).

### reinforce
Read `references/reinforcement.md` (per-surface checklist) and
`references/off-site.md` (profiles and authority). Produce a checklist per
surface with the exact copy from the statement library, and name which
relationships each surface should confirm. Include the other end of each
relationship too: the company page listing the founder, the app-store listing
naming the developer, the product README linking the maker. Draft what can be
drafted, such as READMEs and republish canonicals. The owner applies the rest.

### content
Publish substantive, first-hand pages that *demonstrate* relationships: case
studies of work done at an employer, build logs for a product, the story behind a
method. Each page names its entities, links to their home pages and declares
`about`/`mentions`. Every entity without a real page gets one here. No generic AI
summaries: real decisions, numbers and outcomes.

### measure
Read `references/measurement.md`: GSC setup and the daily rank check
(`scripts/gsc_rank.py`), the Knowledge Graph check (`scripts/kg_check.py`), and
**relationship questions** ("who founded X", "who makes Y", "what is Z") asked in
Google and AI assistants, logged against the map. A wrong or missing answer
points at the line that needs more support.

### report (optional)
Read `references/reporting.md`. Produce a baseline after the first `audit`,
then re-score after each iterate cycle to show the change.

## Iterate
Follow the weekly/monthly/quarterly cadence in `references/measurement.md`. When
something changes (new product, role change, rebrand), **update `entities.yaml`
first**, then re-run `audit` and let the gaps drive the next actions. If on-site
work is done and results are stuck, the lever is more off-site confirmation and
more content that demonstrates the relationships. More on-site tweaks won't help.

A worked example (saadsalman.org) is in `references/worked-example.md`. Tool
recommendations (free first, paid only once volume justifies it) are in
`references/tools.md`.
