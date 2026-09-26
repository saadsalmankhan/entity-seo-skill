# Polished report (Word + PDF)

An agency-style, color-coded scorecard — for a baseline snapshot or a progress
update — that the entity can keep or hand to a stakeholder. Optional: skip it for
routine checks. This is a deliverable, not a step in the core loop.

## When to generate one
- After the first **`audit`** — a baseline before any changes ship.
- After each **iterate** cycle — re-score the same dimensions so the new
  report shows delta against the last one. Keep old reports; don't overwrite them.

## Score what this skill actually did
Seven dimensions, each scored 1–10 (1–3 critical, 4–5 below average, 6–7 decent
foundation needing specific fixes, 8–9 strong, 10 exemplary), plus one non-scored
real-data section. The first two are the core of entity SEO; list them first.

1. **Entity map & relationship coverage.** Does `entities.yaml` exist, has the
   owner confirmed it, and does every entity have a home page? Score = share of
   relationship rows that are *stated*, *encoded*, *confirmed off-site* and
   *answered* correctly (the four `audit` checks). Show the table.
2. **Reinforcement.** Walk `references/reinforcement.md`: do titles, meta
   descriptions, bylines, author boxes, image alt text, video descriptions and
   profiles state the relationships, in wording close to the statement library,
   without stuffing?
3. **JSON-LD entity graph.** Every entity is a node with its own `@id`; every
   relationship references a node by `@id`; no dangling references; articles
   declare `about`/`mentions`.
4. **On-site SEO.** Walk `references/on-site.md`: titles, meta descriptions,
   heading hierarchy, URL structure, canonicals, sitemap/robots, image SEO,
   OG/Twitter cards, PDF consistency, content quality.
5. **GEO (AI search readiness).** Walk the GEO half of `references/geo-aeo.md`:
   E-E-A-T, AI-citable structure, extractable relationship sentences, AI-crawler
   access.
6. **AEO (answer & voice readiness).** Walk the AEO half of
   `references/geo-aeo.md`: snippet formatting, FAQ/HowTo/Speakable validity
   (cross-check Search Console → Enhancements), voice phrasing.
7. **Off-site authority.** Walk `references/off-site.md`: URL fields, structured
   relationship fields, and whether the other end confirms each relationship.
   Score = coverage × correctness, not link count.

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
1. Cover: `{ENTITY}`, "Entity SEO Report", date, the seven scores as a color-coded
   strip.
2. Executive summary: 3–5 sentences — which relationships search engines and AI
   assistants get right or wrong, current position for the name query, and the
   single highest-leverage next move.
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
