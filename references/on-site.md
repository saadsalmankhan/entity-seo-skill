# On-site technical SEO

Placeholders: `{ENTITY}` (name), `{DOMAIN}` (https://example.org), `{ROLE}`,
`{TOPIC}`. Examples use Next.js App Router but the concepts are framework-agnostic.

## Titles & descriptions
- Homepage `<title>`: **`{ENTITY} | {ROLE} — {Specialties}`**. Lead with the name,
  then disambiguate. A vague brand slogan alone is a wasted title.
- Every page gets a **unique** title and meta description that names the entity.
- If a title template applies a suffix (e.g. `template: "%s | {ENTITY}"`), set page
  titles that already contain the name as **absolute** so you don't get
  `About {ENTITY} | {ENTITY}` double-suffixes:
  ```ts
  export const metadata = { title: { absolute: "About {ENTITY} | {ROLE}" } };
  ```

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

## JSON-LD entity graph (the backbone)
Emit one `@graph` and reference a single central `@id` from every page so Google
consolidates everything into ONE entity.

Person (individual):
```json
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "WebSite", "@id": "{DOMAIN}/#website", "url": "{DOMAIN}/",
      "name": "{ENTITY}", "alternateName": "{ENTITY} — {ROLE}",
      "publisher": { "@id": "{DOMAIN}/#person" } },
    { "@type": "ProfilePage", "@id": "{DOMAIN}/about/#profile",
      "url": "{DOMAIN}/about", "mainEntity": { "@id": "{DOMAIN}/#person" },
      "isPartOf": { "@id": "{DOMAIN}/#website" } },
    { "@type": "Person", "@id": "{DOMAIN}/#person", "name": "{ENTITY}",
      "url": "{DOMAIN}/", "image": "{DOMAIN}/{entity}-{role}.jpg",
      "jobTitle": "{ROLE}", "description": "...",
      "worksFor": { "@type": "Organization", "name": "..." },
      "alumniOf": { "@type": "CollegeOrUniversity", "name": "..." },
      "knowsAbout": ["{TOPIC}", "..."],
      "sameAs": ["https://linkedin.com/in/...", "https://github.com/..."] }
  ]
}
```

Organization (brand) — swap the `Person` node for:
```json
{ "@type": "Organization", "@id": "{DOMAIN}/#org", "name": "{ENTITY}",
  "legalName": "...", "url": "{DOMAIN}/", "logo": "{DOMAIN}/logo.png",
  "foundingDate": "YYYY", "sameAs": ["..."],
  "contactPoint": { "@type": "ContactPoint", "contactType": "customer support",
    "email": "..." } }
```
Use `LocalBusiness` (with `address`, `geo`, `openingHours`) for a physical/local
business.

Every article/post/case study references the entity as author:
```json
{ "@type": "BlogPosting", "headline": "...", "datePublished": "...",
  "author": { "@id": "{DOMAIN}/#person" }, "publisher": { "@id": "{DOMAIN}/#person" },
  "mainEntityOfPage": "{DOMAIN}/blog/slug" }
```

`sameAs` = **only genuine, owned profiles**. Never invent profiles for schema.

Render escaped so JSON can't break out of the tag:
```tsx
<script type="application/ld+json"
  dangerouslySetInnerHTML={{ __html: JSON.stringify(data).replace(/</g, "\\u003c") }} />
```
Validate with Google's Rich Results Test / Schema Markup Validator.

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
Name, role, location, and links must be **identical** across the site, résumé/PDF,
and every off-site profile. If Google has indexed a PDF with an old URL or stale
title, update it **at the same URL** (preserves accrued authority) — fix both the
visible text and the PDF metadata (Title/Author/Subject/Keywords).
