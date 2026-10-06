# Worked example: saadsalman.org

A real run of the skill on its author's own site (Next.js + Sanity), to show what
each action produces. The name "Saad Salman" is shared by many people (film,
fabrics, academia, engineering), so the site already did most of the classic
name-ranking work: a central `Person` `@id`, `sameAs`, per-page canonicals, an
about page with a Q&A section, and `llms.txt` with a
disambiguation note. What was missing was the **relationships**.

## map: what the entity map found
Entities:
- **Person:** Saad Salman
- **Employers:** Keep Technologies (current; brand "Keep", not to be confused
  with the unrelated keep.com), Hypefin and i2c (past)
- **Education:** FAST-NUCES
- **Own products:** Gramafin (personal finance app for Pakistan), the Pakistan
  Mutual Funds API (unofficial MUFAP API + MCP server), Rostrum (speaking-club
  app), and the entity-seo skill itself
- **Service:** fintech consulting
- **Shipped work at employers:** Keep Card Program, Keep Travel, and client
  programs at Hypefin and i2c
- **Topics:** card issuing, payments, Pakistani mutual funds

The strongest relationship, with its *why*: "I built the Pakistan Mutual Funds
API **because** Gramafin needed a daily NAV to value mutual fund holdings." It
connects the person to two products and the products to each other, and no
namesake can copy it. It was stated in one paragraph on the about page and
nowhere in schema.

## audit: gaps against the map
| Relationship | Stated | Schema | Gap |
|---|---|---|---|
| Person → works at → Keep | yes | inline, no `@id` | Keep re-declared anonymously on two pages |
| Person → formerly at → Hypefin, i2c | yes | inline, no `@id`; Hypefin had no URL | orgs can't be referenced from elsewhere |
| Keep Card Program → produced by → Keep; Saad led it | yes | `author: Person` | wrong direction: Keep produced it, Saad contributed |
| Keep Card Program → partners → Mastercard, PTC, i2c | yes | none | partner i2c not linked to the i2c employer node |
| Person → built → Pakistan Mutual Funds API | yes | `author` only | no `creator`, no `sameAs` to repos/npm, no link to MUFAP source |
| Gramafin → uses → Pakistan Mutual Funds API | about page only | none | the best *why* sentence was barely stated |
| Person → built → entity-seo skill | no | no | entity missing from the site entirely |
| Articles → about → products | n/a | `author` only | posts didn't say which entities they cover |

## site: what changed
- `Organization` nodes with `@id`s for Keep, Hypefin, i2c and FAST-NU, emitted
  site-wide. `worksFor`, `alumniOf` and the experience-page `OrganizationRole`s
  point at them by `@id`.
- Shipped-project pages: `sourceOrganization` = the employer, `contributor` =
  the person, partners as `mentions` (i2c resolved to its node).
- The Pakistan Mutual Funds API page gained `creator`, `sameAs` (both repos plus
  npm), `isBasedOn` MUFAP, `mentions` Gramafin, and a visible sentence saying it
  was built for Gramafin. Gramafin's node `mentions` the API.
- New `/projects/entity-seo` page for the missing entity, plus a home-page card,
  sitemap entry and `llms.txt` line.
- Blog posts and case studies compute `about` (entities named in title, excerpt
  or tags) and `mentions` (entities named in the body) from a small registry of
  owned entities. The author bio adds a line for the product the post is about.

- Later cleanup: removed `HowTo` markup from two pages and `Speakable` from the
  about page. Neither earns anything in Google any more (see the status table in
  `references/geo-aeo.md`). The visible steps and definition stayed; genuine
  `FAQPage` sections were left alone.

Pattern worth copying: a registry of owned entities (`{ id, name, match }`) in
the structured-data module, used by every article template. A new product gets
added once and every post that names it links to it.

## reinforce: the off-site checklist it produced
- gramafin.com and the npm package README: "by Saad Salman" linking to
  saadsalman.org (the other end of the "built by" line).
- LinkedIn: Experience entries linked to the real company pages, not free text;
  Gramafin, the API and entity-seo added as Projects.
- Keep one spelling of "Hypefin" everywhere; the site and a LinkedIn listing
  disagreed.

## measure: relationship questions
- "Who built Gramafin?" → expect Saad Salman
- "Is there a MUFAP API?" → expect the Pakistan Mutual Funds API, by Saad Salman
- "Saad Salman Keep" → expect the fintech PM, not a namesake
- "Who made the entity-seo skill?" → expect Saad Salman
