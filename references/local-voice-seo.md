# Local SEO & voice search

Optional phase — apply only where it genuinely fits. Local SEO is built for
**location-bound service businesses** (a firm with a physical office, a service
area, or clients who search "near me"). A remote individual or a globally-served
brand should usually **skip Google Business Profile and location pages entirely**
and only take the voice-search half below. Don't create a GBP listing or
location page that doesn't correspond to a real, physical service presence —
that's the same "fabricated profile" problem as a fake `sameAs` link.

## Does this apply?
- **Organization with a physical/local presence** (office, service area, walk-in
  clients): apply both Local SEO and Voice SEO below.
- **Individual or remote-first brand** (consultant working with clients anywhere):
  apply Voice SEO only. State the home location plainly once (identity block,
  `homeLocation` in schema) — that's sufficient; don't build location-specific
  pages you can't back with a real regional presence.

## Local SEO (organizations with a real local presence)
- **Google Business Profile** is the single biggest lever: claim/verify it,
  pick the correct primary category, add hours, photos, and keep it updated.
  Genuine customer reviews compound over time — never buy or incentivize fake ones.
- **NAP consistency**: Name, Address, Phone identical across the site, GBP, and
  every directory. Inconsistency actively suppresses local ranking.
- **Location-specific pages** — one per real service area, not one per keyword
  you'd like to rank for (e.g. "IT Consulting in Austin"), with genuine local
  detail (testimonials from that region, local case studies), not a templated
  city-swap page.
- **Local backlinks**: sponsor or speak at local events, guest-post on regional
  industry sites, partner with local organizations — earn the link, don't buy it.
- **Local keywords**: work the real place name into titles, headers, and body
  copy naturally ("fintech consultant in Lahore," not keyword-stuffed repetition).

## Voice search (applies broadly — individuals and organizations)
Voice queries are longer, conversational, and question-shaped. This builds
directly on the AEO work in `references/geo-aeo.md` — the same direct-answer
content serves both.
- **Long-tail, conversational keywords**: target the way someone would actually
  ask a voice assistant ("what's the ROI of a CRM for a 10-person startup"), not
  the clipped keyword-fragment version.
- **Q&A structure**: question-phrased heading, then a tight **40–60 word** direct
  answer immediately below — the range voice assistants most often read aloud.
- **`SpeakableSpecification` schema** on the 1–2 sections best suited to being
  read aloud (the entity's definition sentence, a key FAQ answer).
- **Page speed and mobile**: voice results skew mobile/on-the-go; a slow page is
  a ranking penalty here specifically, on top of the general UX cost.
- **Test on real assistants**: ask Siri, Google Assistant, and Alexa the target
  questions yourself, periodically. There's no API for this — it's a manual
  spot-check, same caveat as the AI-citation check in `references/geo-aeo.md`.
- **Audio as an extension** (optional, low priority): a short self-intro clip or
  podcast appearance gives voice/audio surfaces something to draw on. Nice-to-have,
  not a blocker.

## Individual vs organization, side by side
| | Individual / remote | Organization with local presence |
|---|---|---|
| Google Business Profile | Skip | Claim, verify, keep current |
| Location pages | Skip — one clear location line is enough | One per genuine service area |
| Local backlinks | Not a priority | Sponsor/guest-post locally |
| Voice search (Q&A, Speakable, 40–60 word answers) | Apply | Apply |
| Voice-assistant spot-checks | Apply | Apply |
