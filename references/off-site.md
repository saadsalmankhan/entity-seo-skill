# Off-site authority

Once on-site is done, this is the real lever. Google ranks established entities
above newcomers because other trusted sites vouch for them. Build the legitimate
equivalent. **A handful of genuine, relevant references beat hundreds of junk links.**

## The core moves
1. Put `{DOMAIN}` (or the entity's own home page) in the **machine-readable URL
   field** of every real profile, not just buried in bio prose. Those fields are
   what search engines and the profile platforms actually expose and link.
2. Make each profile **confirm relationships, not just the name.** Use the
   structured fields that link entities: LinkedIn *Experience* linked to the
   real company page (not free text), a company page listing its founder,
   Crunchbase person ↔ organization, an app-store listing naming the developer,
   a GitHub repo README naming its maker. Bios use the statement-library one-liner
   from `entities.yaml`.
3. **Confirm from both ends.** A relationship stated only by you is weak; the
   same relationship stated by the other entity's own profile is strong. For
   every line on the map, ask where the *other* end confirms it: the company
   page lists the founder, the product site says who built it, the employer's
   team page lists the person.

## Relationship checklist (run per row of the map)
For each relationship in `entities.yaml`:
- Which off-site surfaces should state it? (LinkedIn, company page, Crunchbase,
  product site/README, app store, press, directory listing, conference bio)
- Does at least one **independent** source state it?
- Does the other entity's own profile state it back?
- Is the wording consistent with the statement library?
Anything missing becomes a line on the `reinforce` checklist for the owner.

## Individual checklist
- **LinkedIn** → Contact info → *Website* field (and add the site to Featured).
  Strongest signal, since LinkedIn already ranks for the name.
- **GitHub** → profile *Website* field; create a profile README repo
  (`{username}/{username}`) that links to the site; pin repos that link back.
- **Wellfound / AngelList** → *Website* field in Social Profiles; write a specific
  "what I'm looking for" that names the exact role (specific > generic).
- **Crunchbase** → claim or create a person profile tied to the employer; add the
  website. (Many Crunchbase outbound links are `nofollow`, but the page itself
  ranks for the name and consolidates the entity.)
- **University / alumni page** — `.edu` links carry weight; email the alumni/PR
  office to be featured with a link.
- **Company / team page**, **conference / podcast / association bios** — same photo,
  same one-line bio, link to the site.
- **Medium / dev.to** → republish an article with a **canonical link** back to the
  original on `{DOMAIN}` (backlink + audience, no duplicate-content penalty).

## Organization checklist
- **Google Business Profile** — for any local/physical presence this is often the
  single biggest lever: verified listing, correct primary category, complete NAP,
  photos, and genuine reviews.
- **Industry directories** relevant to the sector (not generic link farms).
- **Press / PR** — real coverage that links the brand name to the site.
- **Crunchbase (company)**, **LinkedIn Company Page**, **G2/Capterra/Trustpilot**
  or equivalent review sites for the category.
- **Wikidata / Wikipedia** — only if genuinely notable; do not self-promote into them.
- **NAP consistency** — identical Name, Address, Phone everywhere; inconsistency
  actively hurts local ranking.

## Avoid
Purchased backlinks, mass/automated directory submissions, private blog networks,
and empty or fabricated profiles created only to pad `sameAs`. Google discounts or
penalizes these.

## How to verify a profile is done right
- It names the entity **and** the related entities it should (employer,
  company, products), in structured fields where the platform has them.
- The site link is the **bare canonical** form (`https://{DOMAIN}`), not an old or
  `www`/redirecting variant.
- The name, role, and photo match the site and schema exactly.
- Where possible, the profile is public and indexable (so it ranks for the name and
  crowds out same-name entities).
