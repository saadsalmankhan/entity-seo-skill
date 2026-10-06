# entity-seo

A reusable **Claude skill** (and plain playbook) for **entity SEO**: helping
Google and AI-powered search understand who you are, what your company, brand
and products are, and **how they all relate to each other**.

Your name is an entity. Your brand is an entity. Your company, if its name is
different, is another. Every product and service you sell is one, and so is an
idea, a method or a slogan. Entity SEO is mapping those entities, writing down
*why* each relationship between them exists, and then reinforcing those
relationships everywhere you publish: the JSON-LD graph, entity pages, titles,
profiles, articles, images and video. Ranking for your own name against
namesakes is one of the results it measures. It isn't the whole job.

Full-site **SEO, GEO (AI/generative search), and AEO (answer engines & voice)**
technique coverage is built in, and it's legitimate tactics only.

## How it works

The skill is split into **actions** that all read and update one saved map,
`entities.yaml`, so your schema, profile copy and articles describe the same
relationships:

| Action | What it does |
|---|---|
| `map` | List your entities, draw the relationships with a one-line *why*, write the statement library. You confirm it. |
| `audit` | For each relationship: is it stated on-site, encoded in schema, confirmed off-site, answered correctly by Google/AI? |
| `site` | On-site fixes: multi-entity JSON-LD graph, a page per entity, titles, internal links, plus technical SEO/GEO/AEO |
| `reinforce` | Ready-to-paste copy for every profile, bio, listing and video description |
| `content` | First-hand articles that demonstrate the relationships |
| `measure` | Google Search Console rank, Knowledge Graph check, relationship questions to AI assistants |
| `report` | Optional color-coded Word/PDF scorecard |

Run `/entity-seo` with no argument and it picks the next action from where you
are; name an action to run just that one (`/entity-seo audit`).

## What's inside

| File | What it covers |
|---|---|
| [`SKILL.md`](SKILL.md) | The skill: definition, guardrails, the actions and how the next one is chosen |
| [`references/entity-map.md`](references/entity-map.md) | Inventory entities, draw relationships with a *why*, give each entity a home, write the statement library, diagnose against the map |
| [`references/reinforcement.md`](references/reinforcement.md) | Per-surface checklist: site, profiles, articles, images, video, comments, press, without stuffing |
| [`references/on-site.md`](references/on-site.md) | Entity pages, the multi-entity JSON-LD graph (Person, Organization, Brand, Product, Service, DefinedTerm, articles with `about`/`mentions`), titles, canonicals, sitemap/robots, image SEO, content quality |
| [`references/geo-aeo.md`](references/geo-aeo.md) | GEO (E-E-A-T, AI-citable content, crawlability), query intent including relationship queries, AEO (snippets and answer formatting, a status table of which answer markup still works, voice) |
| [`references/off-site.md`](references/off-site.md) | Profiles and authority, with relationships confirmed from both ends |
| [`references/local-voice-seo.md`](references/local-voice-seo.md) | Local SEO for organizations with a real physical/service-area presence, voice search for everyone |
| [`references/measurement.md`](references/measurement.md) | GSC setup, daily rank automation, Knowledge Graph and relationship checks, monitoring cadence |
| [`references/reporting.md`](references/reporting.md) | Optional scored report, led by entity-map and relationship coverage |
| [`references/tools.md`](references/tools.md) | Free-first tool list |
| [`references/worked-example.md`](references/worked-example.md) | A real run on saadsalman.org: the map, the gaps, the code changes |
| [`templates/entities.yaml`](templates/entities.yaml) | The entity-map template every action reads |
| [`scripts/gsc_rank.py`](scripts/gsc_rank.py) | Free, official GSC API rank check (no SERP scraping) |
| [`scripts/kg_check.py`](scripts/kg_check.py) | Free, official Knowledge Graph Search API check per entity |

Works for **individuals** (map centred on a `Person`) and **organizations**
(centred on an `Organization`, with brands, founders, products and locations).

## Install it as a Claude skill

Clone into your Claude skills directory (the folder name becomes the skill name):

```bash
git clone https://github.com/saadsalmankhan/entity-seo-skill.git ~/.claude/skills/entity-seo
```

- **Personal** (just you): `~/.claude/skills/entity-seo/`
- **Per-project / shared with a team**: `<repo>/.claude/skills/entity-seo/` and commit it.

Restart Claude Code (or reload) so it picks up the new skill.

## How to call it

1. **Let it auto-trigger.** Describe the goal:
   > "Do entity SEO for me and my company."
   > "Google doesn't connect me to the product I built."
   > "Another <name> outranks me on Google."
   > "Audit my site for SEO, GEO and AEO and give me a scored report."
2. **Invoke it by name.** `/entity-seo` (it picks the next action) or
   `/entity-seo map`, `/entity-seo audit`, etc.
3. **Just read it.** It's plain Markdown; `SKILL.md` + `references/` work as a
   standalone playbook.

It starts by asking for your name, domain and existing profiles, drafts the
entity map from what's already public, and asks you to confirm it before
changing anything.

## Use the scripts standalone

```bash
pip install google-auth
export GSC_KEY_PATH=/secure/path/sa-key.json
export GSC_SITE=sc-domain:example.org
export GSC_QUERIES="jane doe,jane doe designer,jane doe portfolio"
python3 scripts/gsc_rank.py
```

```bash
export KG_API_KEY=...   # Knowledge Graph Search API key, kept out of git
export KG_QUERIES="jane doe,acme labs,acme contrast checker"
export KG_DOMAINS="example.org"
python3 scripts/kg_check.py
```

See [`references/measurement.md`](references/measurement.md) for the one-time
(free, no-billing) setup of both APIs.

## Ground rules (baked into the skill)

- **No guarantees** of position #1; rankings vary by user/location and take weeks.
- **Legitimate tactics only** — no SERP scraping, no CAPTCHA solving, no bought
  links, no fake profiles.
- **Only true relationships**: no invented partnerships, products or awards.
- **Truth & consistency** across site, résumé, schema, and every profile.
- **No stuffing**: reinforce relationships where they fit naturally.
- **Secrets stay secret** (keys `chmod 600`, never committed).

## Built by

Created by [Saad Salman](https://saadsalman.org) — a fintech product manager in
Lahore. This is the entity-SEO playbook used on
[saadsalman.org](https://saadsalman.org); see the
[worked example](references/worked-example.md) and the skill's page at
[saadsalman.org/projects/entity-seo](https://saadsalman.org/projects/entity-seo). If it's useful, a star helps others find it.

## License

MIT — see [LICENSE](LICENSE). Use it, fork it, improve it.
