# SPEC — RedirectLedger

## User story

As a developer migrating a large static site to WordPress, I want a reviewable mapping from every important legacy URL to a verified staging destination, so that I can approve 301 rules before cutover rather than discover lost routes after launch.

## Core flow

1. Point the CLI at a local legacy HTML tree and import a staging CSV containing URLs and optional title, H1, and canonical metadata.
2. Build an inventory of legacy routes, titles, headings, canonical tags, and selected inbound-link counts.
3. Generate explainable candidate matches: exact pathname, normalized slug, canonical, title/H1 similarity, or no candidate.
4. Require a human decision for all non-exact candidates; record the reviewer decision and reason in a portable mapping file.
5. Verify approved routes against the staging target list and emit a Markdown/HTML cutover ledger plus selected redirect-format exports.

## Features

- `inventory` command for local static HTML.
- `candidates` command that writes JSON/YAML with match evidence and confidence categories.
- `review` command that renders unresolved rows for manual approval.
- `verify` command for duplicate sources, loops, missing targets, and targets marked non-2xx by an imported crawl.
- `export` command for nginx, Apache, Cloudflare Bulk Redirect CSV, and WordPress redirect-plugin CSV.

## Data model

```text
LegacyRoute
  source_path, title, h1, canonical, inbound_count

StagingRoute
  destination_url, title, h1, canonical, status_code

MappingDecision
  source_path, destination_url, match_kind, evidence, status,
  reviewer_note
```

`status` is one of `exact`, `needs-review`, `approved`, `rejected`, or `retired`. Secrets, crawl cookies, response bodies, and credentials are out of scope.

## Technical approach

Use a portable CLI with deterministic parsing and local files only. The initial implementation should parse HTML from disk, accept a minimal CSV schema, and make matching rules transparent. A later adapter may import a Screaming Frog crawl export, but no crawler integration is required for the first runnable slice.

## Validation plan

- Fixture set: legacy pages with exact matches, slug changes, ambiguous candidates, intentionally retired pages, duplicate destinations, and a redirect-loop attempt.
- Unit tests assert that exact matches are automatic while fuzzy matches remain `needs-review`.
- Snapshot tests assert all export formats contain only `approved` mappings.
- Wedge validation: compare the generated ledger with a Screaming Frog list-mode audit and a WordPress redirect-plugin import for three migration fixtures. Continue only if reviewers find pre-cutover unresolved/ambiguous reporting saves material review time.
- Safety validation: prove no command makes network writes, reads credentials, or deploys rules.

## Milestones

- `v0.1.0-alpha.0` — repository scaffold and specification.
- `v0.1.0-alpha.1` — local inventory plus fixture data.
- `v0.2.0-alpha.1` — candidate matcher, reviewer file, verifier, and one export format.
- `v0.3.0-alpha.1` — multi-format export and cutover report demo.