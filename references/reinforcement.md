# Reinforcement — entity SEO around everything you publish

Entity SEO isn't a separate campaign that runs next to the rest of your marketing.
It sits around all of it. Every profile, article, post, title, description, image,
and video either confirms the lines on the entity map (`references/entity-map.md`)
or misses the chance to. This file is the per-surface checklist.

The rule for every surface: **name the entity and, where it fits naturally, the
related entity and the relationship.** "Jane Doe" alone is brand consistency.
"Jane Doe, founder of Acme Labs" is entity SEO.

## Don't stuff it
Same as brand mentions: reinforce where it belongs, skip where it doesn't. A
relationship mention should read like something a person would write anyway. If
it reads like an SEO insertion, cut it. Consistency matters, but readers come
first, and forced mentions are exactly what search and AI engines learn to ignore.

## Per-surface checklist

### Your own site
- **Titles:** the entity plus its most important relationship where space allows.
  `Acme Contrast Checker by Acme Labs | WCAG Contrast Tool`;
  `Jane Doe | Founder of Acme Labs — Accessibility Design`.
- **Meta descriptions:** pull from the statement library; mention at least one
  related entity.
- **Entity pages:** each entity's home page (see entity-map.md §4) states its key
  relationships in the first paragraph *and* links to the related entities' pages.
  Internal links are the on-site version of the lines on your map.
- **Author boxes / bylines:** "Jane Doe is the founder of Acme Labs…" linking to
  `/about`, not just a name.
- **Footer:** legal company name, brand, founder or parent, as applicable. It's
  on every page, so it quietly confirms the brand ↔ company line.
- **JSON-LD:** each relationship in visible text is also encoded in the graph
  (see `references/on-site.md`). Schema reinforces what the page says. It never
  claims something the page doesn't.

### Profiles (every one you build)
- Bio or "about" field uses the statement-library one-liner for that entity.
- Structured fields carry the relationships: LinkedIn *Experience* → the company
  page (not free-text), company page → founder listed, Crunchbase person ↔
  organization linked, GitHub org ↔ personal account, app-store listing → the
  company as publisher/developer.
- Each profile links to the entity's canonical page (the machine-readable URL
  field, per `references/off-site.md`).

### Articles and posts (every platform)
- Author line names the person and the relationship relevant to the topic
  ("Jane Doe, founder of Acme Labs"), on your own site *and* on guest posts,
  Medium, LinkedIn articles, and newsletters.
- When a piece discusses a product, method, or idea you own, name it with its
  related entity the first time ("the Contrast-First Method, which I developed
  at Acme Labs") and link to its canonical page.
- In JSON-LD, use `about` and `mentions` pointing at the entity `@id`s the article
  covers, as well as `author`.
- Social posts: not every post. Do it when the post is about the product, the
  company, or the idea.

### Images
- Filenames: `jane-doe-founder-acme-labs.jpg`, `acme-contrast-checker-screenshot.png`.
- Alt text describes what's in the image and names the entities in it: "Jane Doe
  presenting the Acme Contrast Checker at A11yConf 2026".
- Captions do the same where captions exist.
- Consistent visual identity (same headshot, same logo) across all surfaces.

### Video and audio
- Title and description name the people and entities involved and how they're
  related ("Jane Doe, founder of Acme Labs, demos the Contrast-First Method").
- Say it out loud too: transcripts and auto-captions are indexed, so a spoken
  introduction ("I'm Jane Doe, I founded Acme Labs") reinforces the line.
- Upload transcripts/captions rather than relying on auto-generated ones.
- Podcast guest intros and show notes: send the host the one-liner and the link.

### Comments and community
- Sometimes, not always. A signature or a relevant mention when it adds context
  ("we ran into this building the Acme Checker") is fine. Dropping the brand into
  every reply is spam.

### Press, partners, directories
- Give journalists, event organizers, and partners the statement-library
  one-liner and the canonical link, so third-party mentions repeat the
  relationship in the same wording.
- Directory and marketplace listings name the company behind the brand/product.

## Consistency, applied to relationships
Consistency isn't only spelling the brand name the same everywhere. It means the
**same relationships** are stated everywhere:
- The founder's name, the company's name, and the brand's name co-occur the same
  way across surfaces.
- No surface contradicts the map (an old bio calling Jane "co-founder" when the
  map says "founder"; a listing naming the old company as publisher).
- When a relationship changes (new role, acquisition, rename), update the map
  first, then work through this checklist. Stale relationships are contradictions,
  exactly like stale PDFs.

## Quick audit
For a given surface, ask:
1. Which entity is this surface about?
2. Which of its lines on the map should this surface confirm?
3. Does the visible text confirm them, in wording close to the statement library?
4. Does the machine-readable layer (structured fields, schema, links) confirm
   them too?
5. Would a reader find the mention natural? If not, remove it.
