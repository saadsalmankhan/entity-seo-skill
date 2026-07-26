# entity-seo

A reusable **Claude skill** (and plain playbook) for ranking a **person or brand at
the top of Google for their own name** — the legitimate, no-black-hat way.

It's for the common situation where you own the matching domain but you're *not*
the top result for your own name, because other entities share it (a business, a
public figure, hundreds of namesakes) or your site is new and low-authority. The
real problem is **entity ambiguity + authority**, not discovery — and that's fixable.

## What's inside

| File | What it covers |
|---|---|
| [`SKILL.md`](SKILL.md) | The skill: guardrails + a 6-phase workflow (Diagnose → On-site → Off-site → Content → Measure → Iterate) |
| [`references/on-site.md`](references/on-site.md) | Titles, canonicals, identity block, the JSON-LD entity graph, sitemap/robots, image SEO, PDF consistency |
| [`references/off-site.md`](references/off-site.md) | Profile & backlink checklist (LinkedIn, GitHub, Wellfound, Crunchbase, Google Business Profile, …) |
| [`references/measurement.md`](references/measurement.md) | Google Search Console setup + free daily rank automation |
| [`scripts/gsc_rank.py`](scripts/gsc_rank.py) | Free, official GSC API rank-check script (no SERP scraping) |

Works for **individuals** (`Person` schema) and **organizations** (`Organization` /
`LocalBusiness`, Google Business Profile) — the differences are called out throughout.

## Install it as a Claude skill

Clone into your Claude skills directory (the folder name becomes the skill name):

```bash
git clone https://github.com/saadsalmankhan/entity-seo-skill.git ~/.claude/skills/entity-seo
```

- **Personal** (just you): `~/.claude/skills/entity-seo/`
- **Per-project / shared with a team**: `<repo>/.claude/skills/entity-seo/` and commit it.

Restart Claude Code (or reload) so it picks up the new skill.

## How to call it

Three ways, once installed:

1. **Let it auto-trigger.** Just describe the goal and Claude matches the skill's
   `description`:
   > "Help me rank #1 for my name."
   > "Another <name> outranks me on Google — fix my SEO."
   > "Set up daily rank tracking for my site."
2. **Invoke it by name.** In Claude Code, type `/entity-seo`, or say
   *"use the entity-seo skill on my site."*
3. **Just read it.** It's plain Markdown — `SKILL.md` + `references/` work as a
   standalone playbook even without Claude.

The skill then walks the 6 phases (Diagnose → On-site → Off-site → Content →
Measure → Iterate), asking for what it needs (your name, domain, existing profiles).

## Use the rank-check script standalone

```bash
pip install google-auth
export GSC_KEY_PATH=/secure/path/sa-key.json
export GSC_SITE=sc-domain:example.org
export GSC_QUERIES="jane doe,jane doe designer,jane doe portfolio"
python3 scripts/gsc_rank.py
```

See [`references/measurement.md`](references/measurement.md) for the one-time
(free, no-billing) Google Search Console API setup.

## Ground rules (baked into the skill)

- **No guarantees** of position #1; rankings vary by user/location and take weeks.
- **Legitimate tactics only** — no SERP scraping, no CAPTCHA solving, no bought
  links, no fake profiles.
- **Truth & consistency** across site, résumé, schema, and every profile.
- **Secrets stay secret** (keys `chmod 600`, never committed).

## Built by

Created by [Saad Salman](https://saadsalman.org) — a fintech product manager in
Lahore. This is the exact entity-SEO playbook used to build and rank
[saadsalman.org](https://saadsalman.org). If it's useful, a star helps others find it.

## License

MIT — see [LICENSE](LICENSE). Use it, fork it, improve it.
