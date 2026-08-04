# Polished report (Word + PDF)

An agency-style, color-coded scorecard — for a baseline snapshot or a progress
update — that the entity can keep or hand to a stakeholder. Optional: skip it for
routine checks. This is a deliverable, not a step in the core loop.

## When to generate one
- End of **Phase 1 (Diagnose)** — a baseline before any changes ship.
- End of a **Phase 6 (Iterate)** cycle — re-score the same dimensions so the new
  report shows delta against the last one. Keep old reports; don't overwrite them.

## Score what this skill actually did
Six dimensions, each scored 1–10 (1–3 critical, 4–5 below average, 6–7 decent
foundation needing specific fixes, 8–9 strong, 10 exemplary), plus one non-scored
real-data section:

1. **On-site SEO** — walk `references/on-site.md`: titles, meta descriptions,
   heading hierarchy, URL structure, canonicals, `<h1>`/identity block,
   sitemap/robots, image SEO, OG/Twitter cards, PDF consistency.
2. **GEO (AI search readiness)** — walk the GEO half of `references/geo-aeo.md`:
   E-E-A-T signals, AI-citable content structure (answer up top, specific facts,
   original point of view), technical crawlability for AI bots.
3. **AEO (answer & voice readiness)** — walk the AEO half of
   `references/geo-aeo.md`: featured-snippet formatting, FAQ/HowTo/Speakable
   schema validity (cross-check Search Console → Enhancements), voice-search
   phrasing.
4. **JSON-LD entity graph** — does it actually resolve to one `@id` referenced
   consistently site-wide? This is the backbone the other dimensions lean on.
5. **Off-site authority** — walk `references/off-site.md`: for each profile, is
   `{DOMAIN}` in the machine-readable URL field, not just bio prose? Score =
   coverage × correctness, not link count.
6. **Content & consolidation** — how many first-hand, substantive pages exist
   reinforcing "{ENTITY} = {TOPIC}", each properly authored (JSON-LD `author` →
   central `@id`)?

Plus **search rank** — not scored 1–10, it's real numbers: pull straight from
`scripts/gsc_rank.py` — average position trend for the name quer(y/ies),
impressions, clicks, over the available window. This is the one thing a generic
site-audit tool can't produce, because it needs the entity's own Search Console
access — make it the report's centerpiece, not an afterthought.

## Design system
Color-code every score cell: green `#16A34A` (8–10), amber `#D97706` (5–7), red
`#DC2626` (1–4). Keep it simple — a title page, a scores table, one section per
dimension with specific findings (cite the actual title tag, the actual missing
canonical, the actual profile that's missing the URL field), and a closing
rank-trend table pulled straight from the GSC script's output.

State the guardrails from `SKILL.md` somewhere visible (footer or intro) — **no
ranking guarantee**, changes take days to weeks. Don't brand the report with anyone
else's name; it's the entity's own report.

## Build it
Use the `docx` skill to generate the `.docx` (it handles the DOCX mechanics —
tables, shading, headers/footers — correctly; don't hand-roll XML). Suggested
structure:
1. Cover: `{ENTITY}`, "Entity SEO Report", date, the six scores as a color-coded
   strip.
2. Executive summary: 3–5 sentences — current position for the name query, what's
   driving it, the single highest-leverage next move.
3. One section per dimension with a findings table (Signal | Finding | Status) —
   every row backed by something actually observed, not boilerplate.
4. Rank trend: a table (and, if this is a follow-up report, a simple before/after
   comparison) straight from `gsc_rank.py`'s output.
5. Next steps: 2–3 concrete, prioritized actions.

Convert to PDF (e.g. `soffice --headless --convert-to pdf`) if the tooling is
available; otherwise deliver the `.docx` alone — don't block the report on PDF
conversion.

## Don't
- Don't run this for every diagnose pass — it's for a baseline and periodic
  checkpoints, not every session.
- Don't pad scores or findings to look more thorough; a short, accurate report
  beats a long generic one.
- Don't fabricate what wasn't checked (Core Web Vitals, backlink profile,
  competitor sites) — name the dimensions this skill actually assesses and stop
  there.
