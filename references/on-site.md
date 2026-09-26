# On-site technical SEO

Placeholders: `{ENTITY}` (name), `{DOMAIN}` (https://example.org), `{ROLE}`,
`{TOPIC}`. Examples use Next.js App Router but the concepts are framework-agnostic.

## Titles & descriptions
- Homepage `<title>`: **`{ENTITY} | {ROLE} — {Specialties}`**. Lead with the name,
  then disambiguate. A vague brand slogan alone is a wasted title.
- Entity pages carry their most important relationship where it fits:
  `Acme Contrast Checker by Acme Labs | WCAG Contrast Tool`,
  `Jane Doe | Founder of Acme Labs`.
- Every page gets a **unique** title and meta description that names the entity.
- If a title template applies a suffix (e.g. `template: "%s | {ENTITY}"`), set page
  titles that already contain the name as **absolute** so you don't get
  `About {ENTITY} | {ENTITY}` double-suffixes:
  ```ts
  export const metadata = { title: { absolute: "About {ENTITY} | {ROLE}" } };
  ```

## Meta, headings & URL fundamentals
- Meta description: unique per page, 150–160 chars, states the entity/topic plainly
  and includes a soft call-to-action. Don't leave it to auto-generation.
- Heading hierarchy: exactly one `<h1>` per page; `<h2>`/`<h3>` follow a logical
  outline, no skipped levels, no keyword-stuffed headings.
- URL structure: short, readable, hyphenated, no query-string cruft for canonical
  content (`/blog/{slug}` not `/blog?id=123`); avoid duplicate/near-duplicate paths.
- Open Graph / Twitter Card: `og:title`, `og:description`, `og:image` (the same
  entity photo/logo used everywhere), `twitter:card=summary_large_image` — controls
  how the entity appears when shared, which is itself a trust/consistency signal.
- Freshness signals: visible "Published"/"Updated" dates on articles; re-date
  evergreen pages (about, services) when materially changed, not on a schedule.

## Content quality (don't skip — schema can't rescue thin content)
A page can have flawless titles, canonicals, and JSON-LD and still be passed over by
AI Overviews and answer engines if the content itself is thin. Treat this as an
active check, not a one-time rule:
- **Word-count every key page** (about, case studies, pillar articles). Flag
  anything under **500 words** (**1500+** for cornerstone/pillar content) as a
  content-quality risk and route it to the `content` action for a rewrite before investing
  further in schema or off-site work on that page — technical SEO and structured
  data cannot compensate for thin content when engines decide what to cite.
- **Proofread for grammar and spelling.** Errors are a low-effort signal to both
  classic ranking and AI synthesis, same as thin content — run a pass (or a
  spell/grammar tool) on every page before publishing or re-publishing.
- **Check for keyword cannibalization** on multi-page sites/orgs: if two pages
  target the same query (e.g. two pages both trying to rank for "{ENTITY} {ROLE}"),
  consolidate or differentiate them — competing pages split authority instead of
  compounding it.

## Canonicals
- Set `alternates.canonical` **per page** (`/`, `/about`, `/blog`, ...).
- **Never** set a single canonical in the root layout — child pages inherit it and
  all point at `/`. This silently de-indexes your inner pages. Common, damaging.

## Headings & identity block
- About/company `<h1>` = the **full name** ("About {ENTITY}"), not "Hi, I'm …".
- First paragraph names the entity and role naturally.
- Add a labelled identity block (parseable by people and machines):
  - **Individual:** Name, Profession, Specialisation, Location, Current company, Education.
  - **Org:** Legal name, Category, HQ / service area, Founded, Leadership, Website.

## Entity pages
Every entity on the map (`references/entity-map.md`) needs one canonical page
that is *about that entity* and hosts its `@id`: `/about` for the person, the
homepage or `/company` for the organization, `/products/{slug}` for each product
or service, `/method/{slug}` for a named idea. The first paragraph states the
entity's key relationships ("Acme Contrast Checker, made by Acme Labs, …") and
links to the related entities' pages. Internal links are the on-site version of
the lines on the map.

## JSON-LD entity graph (the backbone)
The graph is how relationships become machine-readable. Rules:
- **Every entity is its own node with its own `@id`.** Relationships reference
  other nodes by `@id`, never by an anonymous inline object. `"worksFor":
  {"@type":"Organization","name":"Acme"}` creates an unnamed blob nothing else can
  point at. `"worksFor": {"@id": "{DOMAIN}/#org"}` joins the graph.
- **Emit shared nodes site-wide** (Person, Organization/Brand, employers) from the
  root layout, and each page adds its own nodes (a product, an article) that
  reference them. Nodes with the same `@id` on different pages merge.
- **Encode only what the page's visible text says.** Schema reinforces the
  content and never claims more.
- **`sameAs`** only for genuine, owned profiles (or an entity's official
  Wikipedia/Wikidata page). Never invent profiles for schema.

Site-wide graph (root layout): person, company, brand, past employer, school:
```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "WebSite", "@id": "{DOMAIN}/#website", "url": "{DOMAIN}/",
      "name": "{ENTITY}", "publisher": { "@id": "{DOMAIN}/#person" } },
    { "@type": "Person", "@id": "{DOMAIN}/#person", "name": "Jane Doe",
      "url": "{DOMAIN}/about", "image": "{DOMAIN}/jane-doe-founder-acme-labs.jpg",
      "jobTitle": "Founder & CEO", "description": "...",
      "worksFor": { "@id": "{DOMAIN}/#org" },
      "alumniOf": [{ "@id": "{DOMAIN}/#org-school" }, { "@id": "{DOMAIN}/#org-prev" }],
      "knowsAbout": ["Web accessibility", "WCAG"],
      "sameAs": ["https://www.linkedin.com/in/...", "https://github.com/..."] },
    { "@type": "Organization", "@id": "{DOMAIN}/#org", "name": "Acme Labs Ltd.",
      "legalName": "Acme Labs Ltd.", "url": "{DOMAIN}/", "logo": "{DOMAIN}/acme-logo.png",
      "foundingDate": "2019", "founder": { "@id": "{DOMAIN}/#person" },
      "brand": { "@id": "{DOMAIN}/#brand" },
      "sameAs": ["https://www.linkedin.com/company/..."] },
    { "@type": "Brand", "@id": "{DOMAIN}/#brand", "name": "Acme",
      "slogan": "Design for every eye", "logo": "{DOMAIN}/acme-logo.png" },
    { "@type": "Organization", "@id": "{DOMAIN}/#org-prev", "name": "Previous Employer Inc",
      "url": "https://previous.example" },
    { "@type": "CollegeOrUniversity", "@id": "{DOMAIN}/#org-school", "name": "...",
      "url": "https://..." }
  ]
}
```
If brand and company are the same thing, drop the `Brand` node and give the
Organization an `alternateName`. If they differ, keep both: that difference is
exactly what the graph needs to express.

Product / service page: its own node, pointing back at maker and brand:
```json
{ "@type": "SoftwareApplication", "@id": "{DOMAIN}/products/contrast-checker#product",
  "name": "Acme Contrast Checker", "url": "{DOMAIN}/products/contrast-checker",
  "applicationCategory": "DesignApplication", "operatingSystem": "Web",
  "creator": { "@id": "{DOMAIN}/#org" }, "brand": { "@id": "{DOMAIN}/#brand" },
  "sameAs": ["https://github.com/acme/contrast-checker"],
  "offers": { "@type": "Offer", "price": 0, "priceCurrency": "USD" } }
```
```json
{ "@type": "Service", "@id": "{DOMAIN}/services/audits#service",
  "name": "Accessibility Audits", "serviceType": "Accessibility consulting",
  "provider": { "@id": "{DOMAIN}/#org" }, "areaServed": ["US", "CA"] }
```
Use `Product` (with `brand`/`manufacturer`) for physical goods, `Book`,
`Course` etc. where they fit. A product built by an individual uses
`creator: {"@id": ".../#person"}`.

Named idea / method: a `DefinedTerm`, credited to its creator:
```json
{ "@type": "DefinedTerm", "@id": "{DOMAIN}/method/contrast-first#term",
  "name": "The Contrast-First Method", "description": "...",
  "url": "{DOMAIN}/method/contrast-first",
  "inDefinedTermSet": { "@type": "DefinedTermSet", "name": "Acme design methods" },
  "subjectOf": { "@type": "CreativeWork", "creator": { "@id": "{DOMAIN}/#person" },
    "url": "{DOMAIN}/method/contrast-first" } }
```

Work done *at* an employer or *for* a client: credit the organization, not
just the person:
```json
{ "@type": "CreativeWork", "@id": "{DOMAIN}/work/card-program#project",
  "name": "Card program launch", "sourceOrganization": { "@id": "{DOMAIN}/#org-prev" },
  "contributor": { "@id": "{DOMAIN}/#person" },
  "mentions": [{ "@type": "Organization", "name": "Mastercard" }] }
```

Articles: author, plus the entities the article is about:
```json
{ "@type": "BlogPosting", "headline": "...", "datePublished": "...",
  "author": { "@id": "{DOMAIN}/#person" }, "publisher": { "@id": "{DOMAIN}/#org" },
  "about": [{ "@id": "{DOMAIN}/products/contrast-checker#product" }],
  "mentions": [{ "@id": "{DOMAIN}/method/contrast-first#term" }],
  "mainEntityOfPage": "{DOMAIN}/blog/slug" }
```
Implementation tip: keep a small registry of owned entities (`{ id, name,
match }`) in the structured-data module and let every article template derive
`about` (entities named in the title/excerpt/tags) and `mentions` (named in the
body). A new product is added once and every post that names it links to it.
See `references/worked-example.md`.

Render escaped so JSON can't break out of the tag:
```tsx
<script type="application/ld+json"
  dangerouslySetInnerHTML={{ __html: JSON.stringify(data).replace(/</g, "\\u003c") }} />
```
Validate with Google's Rich Results Test / Schema Markup Validator, then check the
graph itself: **every `{"@id": ...}` reference must resolve to a node emitted on
that page** (site-wide nodes included). A dangling `@id` is a relationship that
points at nothing.

## Sitemap & robots
- Emit `sitemap.xml` with static routes + every post/case study. Wrap CMS calls in
  try/catch so a build never fails when the CMS is unreachable.
- `robots.txt`: allow all, point to the sitemap, disallow admin/studio/api paths.
- These are prerequisites for submitting the sitemap in Search Console.

## Image SEO
- Rename the primary image: `{entity}-{role}.jpg` (or `{brand}-logo.png`).
- Descriptive `alt`: "{ENTITY}, {ROLE} in {LOCATION}".
- Reference it in the entity's schema `image`/`logo`.
- Use the **same** recognizable photo/logo across the site and every profile.

## Consistency (NAP for people/brands)
Name, role, location, links **and relationships** must be identical across the
site, résumé/PDF, and every off-site profile. The same founder, company, brand and
product names co-occur the same way everywhere (see `references/reinforcement.md`). If Google has indexed a PDF with an old URL or stale
title, update it **at the same URL** (preserves accrued authority) — fix both the
visible text and the PDF metadata (Title/Author/Subject/Keywords).
