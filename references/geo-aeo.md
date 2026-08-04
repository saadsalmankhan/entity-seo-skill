# GEO & AEO — AI search and answer engines

**GEO** (Generative Engine Optimization) targets AI-powered search/answer surfaces
(Perplexity, ChatGPT Search, Google AI Overviews, Gemini) that synthesize answers
from multiple sources and cite them. **AEO** (Answer Engine Optimization) targets
featured snippets, People Also Ask, and voice search. Both build on the entity
graph in `references/on-site.md` — do this **after** the JSON-LD entity graph and
identity block are in place, since GEO/AEO signals depend on Google already
recognizing `{ENTITY}` as a single, disambiguated entity.

## GEO: make the entity citable by AI engines

**E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)**
- About page states real credentials/experience in the entity's own words, not a
  stock bio.
- Every article names its author and links to `{DOMAIN}/about` via the JSON-LD
  `author` → central `@id` (already required in on-site.md's entity graph).
- Trust signals visible on-site where genuine: testimonials, press mentions,
  certifications, awards. Never fabricate these.
- Contact info (email, and phone/address if applicable) is easy to find.

**Content AI engines can cite**
- Lead each substantive page with the core claim/answer in the **first 1–2
  sentences** — AI synthesis tools weight the top of the page heavily.
- Include specific facts, numbers, and first-hand outcomes (a case study with real
  metrics beats a generic explainer) — see Phase 4 "Content" in `SKILL.md`.
- Cite external authoritative sources where relevant; original data or a clearly
  stated point of view is what gets an AI engine to prefer citing this entity over
  a generic aggregator.
- Keep the entity's name and role stated consistently near the top of every page —
  vague phrasing gives AI engines nothing to anchor the entity to.

**Technical GEO**
- HTTPS everywhere (baseline trust signal).
- No JavaScript-only rendering for primary content — AI crawlers, like classic
  crawlers, need real text in the initial HTML/SSR output.
- `robots.txt` doesn't block known AI crawlers (e.g. `GPTBot`, `PerplexityBot`,
  `Google-Extended`) unless the entity has a deliberate reason to opt out.

## AEO: make the entity extractable as a direct answer

**Featured-snippet-ready formatting**
- Under a question-phrased heading ("What does `{ENTITY}` do?", "How did
  `{ENTITY}` get into `{TOPIC}`?"), answer in a tight 40–60 word paragraph
  immediately below — no throat-clearing first.
- Include a clear "X is..." definition sentence on the about page — the
  single highest-yield sentence for both snippets and AI summaries.
- Turn any step-by-step or comparison content into an actual numbered list or
  table — snippet engines extract structured markup far more reliably than prose.

**Structured answer schema**
- Add `FAQPage` JSON-LD for genuine Q&A content (real questions the entity is
  actually asked — don't invent filler questions just to get the schema type).
- Add `HowTo` JSON-LD for genuine step-by-step content.
- `SpeakableSpecification` on the 1–2 sections best suited to being read aloud
  (the definition sentence, the direct-answer paragraph) if voice/assistant
  surfaces matter for this entity.

**Voice search phrasing**
- Natural, conversational phrasing in headings and direct-answer paragraphs —
  write for "how do I..." / "who is..." spoken queries, not keyword fragments.
- Cover the actual long-tail questions people ask about the entity (check "People
  also ask" for the name query, and recurring questions from real
  conversations/interviews) as their own headings.

## Validate
- Google Rich Results Test for `FAQPage`/`HowTo`/`Speakable`, same as the entity
  JSON-LD.
- Read the rendered page as an AI engine would: does the first screen alone answer
  "who is `{ENTITY}` and what do they do"? If not, that's the highest-leverage GEO
  fix before anything else here.
- Search Console → **Enhancements** shows valid/invalid counts for any FAQ/HowTo
  markup added — fix invalid items immediately (bad schema is worse than none).
- There's no free official API for AI-Overview or assistant citations. Treat "does
  an AI search cite `{ENTITY}`" as a manual, periodic check (ask ChatGPT Search /
  Perplexity / Gemini the name query yourself) — never scrape or automate this.

## Don't
- Don't add `FAQPage`/`HowTo` schema around content that doesn't genuinely exist as
  Q&A/steps — Google and AI engines can tell, and mismatched schema is a
  trust-eroding contradiction like any other (see guardrails in `SKILL.md`).
- Don't chase every AEO tactic on every page; prioritize the about page and the
  entity's 2–3 highest-traffic content pages first.
