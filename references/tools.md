# Tools

Everything the core workflow needs is free. The paid tools below are optional
accelerants for high-volume sites — skip them entirely while a site is still
low-traffic (under ~50 impressions/month in Search Console); at that scale
they mostly report noise, and the free tools already cover the workflow.

## Free, already load-bearing in this skill
- **Google Search Console** — ground truth for rank, impressions, indexing, and
  FAQ/HowTo schema validity (`references/measurement.md`). Use this before
  reaching for anything paid.
- **`scripts/gsc_rank.py`** — this skill's own free daily rank check via the
  official GSC API. No SERP scraping, no billing.
- **A SERP API free tier** (e.g. SerpApi, ~100 searches/month recurring) — the
  only remaining legitimate way to check real Google positions for queries the
  site gets zero impressions on (see `references/measurement.md`). Google
  deprecated Programmable Search Engine's "entire web" mode and no longer
  honors `num=100`, so budget ~2 paginated fetches per keyword and run weekly.
- **Google Rich Results Test** — validates `Person`/`FAQPage`/`HowTo`/`Speakable`
  JSON-LD before and after shipping (`references/on-site.md`).
- **Google's Structured Data Markup Helper** — a point-and-click way to generate
  starter FAQ/HowTo schema if writing JSON-LD by hand isn't an option.
- **AnswerThePublic** (free tier) — surfaces real question-phrased searches
  people make around a name or topic. Use this to find **genuine** FAQ
  questions instead of inventing them — the guardrail in `SKILL.md` against
  filler questions.
- **A grammar checker** (Grammarly free tier, or any equivalent) — the
  grammar/spelling pass now required by the content-quality check in
  `references/on-site.md`.
- **PageSpeed Insights** — free page-speed check; relevant to voice search
  ranking specifically (`references/local-voice-seo.md`), not just general UX.
- **Siri / Google Assistant / Alexa** (whatever's on hand) — the only way to
  spot-check voice-assistant answers; there's no API for this.

## Paid, optional once volume justifies them
- **SEMrush / Ahrefs** — keyword and competitor research, featured-snippet
  rank tracking at scale. Worth it once there's enough query volume that
  manual GSC review becomes tedious.
- **Moz Local / BrightLocal** — NAP-consistency and local-ranking tracking
  across directories. Organizations with a real local presence only
  (`references/local-voice-seo.md`) — skip for individuals/remote brands.
- **Merkle's Schema Markup Generator** — a more full-featured alternative to
  Google's own markup helper for product/organization schema.
- **Dialogflow** — for building an actual conversational/voice interface, not
  for optimizing existing content. Only relevant if the entity is building a
  chatbot or voice app, which is out of scope for most of this skill.

## Don't
Don't buy a paid tool to replace a step the free tools already do (GSC replaces
most of what a paid rank tracker offers at this scale). Don't use any tool,
free or paid, to scrape SERPs or automate CAPTCHA-gated lookups — see the
guardrails in `SKILL.md`.
