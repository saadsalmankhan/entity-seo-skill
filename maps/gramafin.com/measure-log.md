# gramafin.com: measurement log

Search checks use a general web search engine (US index), not Google: they're
directional only. Google Search Console is the real number once it's connected
(see `references/measurement.md`).

## 2026-11-14: baseline (fixes NOT live yet)
State: the `site` branches in gramafin and personal-website are unmerged. Live
gramafin.com still has the one-word title, no JSON-LD, and help on app.gramafin.com.
saadsalman.org still says "Web, Android, iOS" and links the private repo.

| Query | Expect | Result | Correct? |
|---|---|---|---|
| Gramafin | gramafin.com | Not found. Results are chemicals and drugs (Gramine, Grafalon, Grafino) | ✗ |
| Who built Gramafin? | Saad Salman | Not found. Unrelated "Gram…" companies | ✗ |
| Gramafin app Pakistan net worth | gramafin.com | Not found. Other PK fintechs (NayaPay, TAG, Savyour) | ✗ |
| Net worth tracker app Pakistan PKR free | Gramafin | Not listed. PaisaMax (pre-launch), FinHisaab, Hysab Kytab, global apps | ✗ |
| Is there an API for MUFAP mutual fund NAVs? | Pakistan Mutual Funds API | Not listed. Apify MUFAP scrapers and CapitalStake take the spot | ✗ |

GSC: not connected. Knowledge Graph API: no key.

Takeaways:
- Zero visibility for the brand name, which is expected for a site with no
  structured data, a one-word title and no outside mentions. Deploying the
  `site` fixes is the first lever.
- The MUFAP API question is winnable: the competitors are generic scraper
  listings. Listing the API where developers look (Apify/RapidAPI-style
  directories, awesome-lists, the npm README) is a `reinforce` task.
- A pre-launch competitor (PaisaMax) is already being picked up for "free PKR
  net worth tracker". The category is getting crowded.
