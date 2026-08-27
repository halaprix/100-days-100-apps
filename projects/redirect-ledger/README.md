# RedirectLedger

A local-first cutover mapper for static HTML sites moving to WordPress: inventory legacy pages, match them to a staging crawl, and produce a human-approved 301 redirect ledger before DNS changes.

## Problem

A site owner moving a large static site to a CMS has to preserve high-value URLs while changing templates and information architecture. A fresh public `r/webdev` report describes a 2,000–3,000-page HTML site whose owner wants to move to WordPress without destroying SEO or domain rating. Manual spreadsheets and post-cutover crawling turn a pre-launch mapping job into an error-prone, hours-long exercise; missed routes can cost search traffic and create public 404s.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Community report | https://www.reddit.com/r/webdev/comments/1vz3em2/best_ways_to_move_large_static_html_site_over_to/ | An August 27, 2026 post asks how to move a 2,000–3,000-page static HTML site to WordPress while preserving SEO and domain rating. |
| Vendor documentation | https://www.screamingfrog.co.uk/seo-spider/tutorials/audit-redirects/ | Screaming Frog documents that 301 redirects preserve indexing/link signals and that migration auditing is difficult at scale. |
| Direct competitor | https://wp301.com/ | WP301 positions itself as an in-WordPress migration mapping and redirect-management tool. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Screaming Frog SEO Spider | Strong crawler and redirect auditor; it verifies a supplied URL list but does not make a local legacy-tree-to-staging candidate ledger the primary workflow. |
| Direct competitor | WP301 and WordPress redirect plugins | Can map or import redirects inside WordPress; they compete directly and make the category crowded. RedirectLedger must stay focused on pre-cutover evidence, not another redirect manager. |
| Indirect substitute | Spreadsheet, CMS export, manual `curl`, and agency migration work | Flexible but laborious; matching decisions, ambiguity, and review ownership are dispersed across files and messages. |
| Status quo | Launch, then crawl 404s and redirect chains under SEO pressure | Detects failure after visitors and crawlers have already encountered it. |

## Wedge

RedirectLedger does not deploy redirects or replace a WordPress plugin. It creates a deterministic, local review artifact before cutover: candidate matches use pathname, title, canonical, and heading signals; every non-exact route is explicitly approved, rejected, or left unresolved; outputs target Apache, nginx, Cloudflare, or plugin-import formats. The first distribution path is migration-specific search content and reproducible examples attached to WordPress/static-site migration discussions.

## Target user

A freelance web developer, small agency, or technically capable site owner migrating a static HTML site with hundreds or thousands of indexed URLs to a WordPress staging site.

## MVP

- Crawl a local legacy HTML directory and import a CSV of staging URLs plus optional title/H1/canonical fields.
- Propose exact and explainable candidate matches; never silently approve fuzzy matches.
- Render a reviewable HTML/Markdown ledger for approved, ambiguous, unmatched, and intentionally retired routes.
- Export approved 301 rules for nginx, Apache, Cloudflare Bulk Redirect CSV, and WordPress redirect-plugin CSV formats.
- Verify an approved mapping file for duplicate sources, redirect loops, missing destinations, and non-2xx staging targets.

## Non-goals

- No WordPress credentials, automatic plugin installation, DNS changes, or redirect deployment.
- No AI-generated redirect decisions in the first release.
- No promise to preserve rankings; the product verifies route coverage, not search-engine outcomes.

## Status

`v0.1.0-alpha.0` — local scaffold and specification only. The commercial wedge needs validation against existing mapping tools before implementation expands.