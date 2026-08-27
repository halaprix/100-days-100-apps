# Day 063 — RedirectLedger

Date: 2026-08-27
Status: repo-created

## One-line pitch

A local-first cutover mapper for static HTML sites moving to WordPress: inventory
legacy pages, match them to a staging crawl, and produce a human-approved 301
redirect ledger before DNS changes.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Community report (Reddit RSS discovery; public post page) | https://www.reddit.com/r/webdev/comments/1vz3em2/best_ways_to_move_large_static_html_site_over_to/ | On August 27, a site owner reported a 2,000–3,000-file static HTML site with declining traffic and asked how to move it to WordPress without destroying SEO or domain rating. |
| Vendor documentation | https://www.screamingfrog.co.uk/seo-spider/tutorials/audit-redirects/ | Screaming Frog says 301 redirects preserve indexing/link signals and documents list-mode auditing because migration redirects can become incorrect, chained, or broken at scale. |
| Direct competitor | https://wp301.com/ | WP301 markets in-WordPress migration mapping and redirect management, confirming that mapping/redirect tooling already exists and that the MVP must not be a generic redirect manager. |
| Plugin substitute | https://wordpress.org/plugins/kaan-bulk-redirects/ | Kaan Bulk Redirects supports CSV import/export and redirect management; it is an output target/substitute, not a pre-cutover mapping-review workflow. |

## Source access caveats

- Reddit's public JSON endpoint returned its theme-beta `403`. The read-only
  tool used public RSS fallback for fresh `r/sysadmin` and `r/webdev` probes;
  scores and comment counts are unavailable. `r/selfhosted` then returned RSS
  `429` and was not retried. The selected `r/webdev` post page was fetchable,
  but the comments-thread API still returned `403`.
- `xurl auth status` showed no OAuth 2 token for the default app, and the
  attempted X search returned `401 Unauthorized`. X supplied no signal and no
  X consensus is claimed.
- This is one fresh, concrete community report backed by migration-tool
  documentation and competitor checks. It is not evidence that every static-site
  migration needs a new tool.

## Problem

A large static-site-to-CMS migration turns every indexed legacy path into a
cutover decision. Existing tools can crawl, audit a supplied URL list, or manage
redirects after a mapping exists, but the team still has to build and review the
mapping. A spreadsheet, CMS export, and manual requests make the work hard to
reconcile before launch; a missed high-value route can create public 404s and
lose search traffic.

This passes the status-quo pain test. For hundreds or thousands of routes, the
manual workaround consumes far more than 30 minutes and an error can block a
safe launch or cause a visible commercial loss.

## Target user

A freelance web developer, small agency, or technically capable site owner
migrating a static HTML site with hundreds or thousands of indexed URLs to a
WordPress staging site.

## Shortlist and wedge-first gate

| Candidate | Wedge-first gate | Outcome |
|---|---|---|
| RedirectLedger | Static-site migration developer with hundreds/thousands of URLs → Screaming Frog, WP301/redirect plugins, spreadsheets, and agency work → crawlers audit supplied routes and plugins manage redirects but none is assumed to make a local legacy-tree-to-staging review ledger the primary pre-cutover artifact → explainable candidate matching plus explicit approval/unresolved rows and multi-target exports → migration-specific search content, WordPress/static-site migration threads, and reproducible example repositories → a fresh 2,000–3,000-file migration request exposes the route-mapping pain | **Selected**; severe cutover risk, local MVP, and a concrete audience/channel. |
| ShiftAuth Kit | K-12/retail frontline IT teams → Entra documentation, QR handouts, My Staff, and digital-adoption platforms → pictographic enrollment still fails in one fresh report → device/language-specific enrollment packet → frontline IT communities → Entra QR authentication support | Rejected before scoring: overlaps prior Entra/passkey work and lacks proof it beats Microsoft’s built-in frontline path rather than improving documentation. |
| SystemMap Delta | Admins maintaining system diagrams → D2, Lucid, Backstage, and manually maintained diagrams → diagrams drift, but existing diagram/source-control workflows already cover most of the job → infrastructure-change diff view → sysadmin documentation threads → a fresh D2 discussion | Rejected before scoring: no evidence that the status quo causes a material recurring loss for a sharp first-user segment. |
| MAMP Patch Pulse | Mac web developers hit by a local PHP runtime break → vendor update notes, rollback, Docker, and local logs → one report suggests a same-day disruption, but a global-version detector has weak proof of repeatability → installer/version incident check → MAMP support searches → fresh MAMP breakage report | Rejected before scoring: one incident is not enough evidence and distribution is vague. |
| FormFollow-Up | Small web agencies deciding what follows a form submit → success pages, embedded success state, A/B testing, and CRM forms → conversion choices are contextual rather than a durable missing workflow → post-submit experiment planner → webdev/agency communities → fresh form-success question | Rejected before scoring: crowded optimization tooling and tolerable status quo. |

## MVP scope

- Crawl a local legacy HTML directory and import a CSV of staging URLs plus
  optional title, H1, canonical, and status fields.
- Propose exact and explainable candidate matches from pathname, slug, title,
  heading, and canonical signals; fuzzy matches always require review.
- Render an HTML/Markdown ledger for approved, ambiguous, unmatched, and
  intentionally retired routes.
- Verify duplicate source paths, redirect loops, missing destinations, and
  non-2xx staging targets.
- Export only approved mappings for nginx, Apache, Cloudflare Bulk Redirect CSV,
  and a WordPress redirect-plugin CSV. Never deploy the rules.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Screaming Frog SEO Spider | Strong crawler and redirect auditor. It validates a supplied legacy URL list and reports chains/errors; the proposed gap is building a reviewable local legacy-to-staging candidate ledger before rules exist. |
| Direct competitor | WP301 | Markets migration mapping plus a WordPress redirect manager. It makes the category real and forces a narrower position: external pre-cutover proof, not another in-admin redirect editor. |
| Direct competitor | WordPress bulk redirect plugins | CSV import/export and redirect management solve deployment after mappings exist, but do not prove the input map covers the local legacy tree. |
| Indirect substitute | Spreadsheet, CMS export, manual requests, migration agency | Flexible but manual; source/destination decisions, ambiguity, and review ownership are scattered and easy to lose. |
| Status quo | Cut over, then crawl 404s and redirect chains | Finds problems only after users and search crawlers can encounter them. |

## Wedge

RedirectLedger is not a generic SEO crawler, redirect manager, or AI mapper. It
is a local deterministic pre-cutover proof: it inventories the legacy tree,
shows why each staging candidate was proposed, refuses to auto-approve fuzzy
matches, and emits only human-approved routes in the target platform’s format.
The concrete distribution wedge is content/examples for the exact migration
query, static-site-to-WordPress discussions, and a shareable review artifact
that agencies can use with clients.

## Kill condition

Reject or narrow if WP301 or a maintained WordPress/Screaming Frog workflow can
already create an equally reviewable local legacy-tree-to-staging map with
explicit unresolved/ambiguous rows and multi-target exports, or if three
migration practitioners report that their existing spreadsheet+crawler process
takes under 30 minutes for a 500-route cutover. Also reject any scope that needs
WordPress credentials, a production crawl, automatic deployment, or opaque AI
matching to be useful.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 5/5 | Large migrations create multi-hour mapping work; missed routes can lose traffic and delay a launch. |
| Feasibility | 4/5 | Local HTML/CSV inventory, deterministic matching, reports, and exports fit 1–3 days; high-quality matching needs fixture validation. |
| Demo potential | 5/5 | A fixture can visibly classify exact, ambiguous, retired, and missing routes and render safe redirect exports. |
| Distribution | 4/5 | Exact migration searches, WordPress/static-site communities, migration checklists, and agency-facing example reports are a concrete repeatable path. |
| Competitive wedge / timing | 3/5 | Incumbents are strong, but a local pre-cutover approval ledger is narrower than crawling or redirect management. The gap needs practitioner validation. |
| Total | 21/25 | Clears the repository threshold and both dimension gates. |

## Decision

**Repo created locally.** RedirectLedger scores 21/25 and passes the
Distribution (4/5) and competitive-wedge/timing (3/5) gates. Its dedicated local
scaffold and public-safe snapshot are in
[`projects/redirect-ledger`](../projects/redirect-ledger). No dedicated GitHub
remote was created or claimed. The weakest dimension is competitive
wedge/timing (3/5): WP301, redirect plugins, and crawler workflows already own
much of the category, so the external pre-cutover review artifact must prove
its value.

## Next build step

Implement a synthetic 20-route fixture: local legacy HTML plus staging CSV with
exact, slug-changed, ambiguous, retired, duplicate, and missing routes. Build
the deterministic inventory/candidate report before adding any redirect export.