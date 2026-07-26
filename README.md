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

## Use it as a Claude skill

Clone into your Claude skills directory:

```bash
git clone https://github.com/<owner>/entity-seo-skill.git ~/.claude/skills/entity-seo
```

Then in Claude Code / Claude, ask something like *"help me rank #1 for my name"* or
*"why does another <name> outrank me — fix my SEO"*, and the skill guides the work.

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

## License

MIT — see [LICENSE](LICENSE). Use it, fork it, improve it.
