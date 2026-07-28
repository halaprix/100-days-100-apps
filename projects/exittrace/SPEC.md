# SPEC — ExitTrace

## User story

As a web developer or SEO consultant working on a sensitive support site, I want a local report of browser-visible trace risks, so that I can preserve discoverability and accessibility without exposing at-risk users through page titles, URLs, referrers, history, or broken quick-exit flows.

## Core flow

1. Run `exittrace audit --local fixtures/survivor-site --sensitive-map fixtures/sensitive.yml`.
2. ExitTrace crawls pages from a local build, sitemap, or live URL.
3. It extracts safe page facts: URL, path segments, title, headings, canonical URL, links, referrer policy, quick-exit links, and safety-content links.
4. It compares those facts to a sensitive-term map and built-in rules.
5. It writes `exittrace-report.md` and `exittrace-report.csv`.
6. The consultant/web team reviews the findings and applies safer wording or implementation fixes.

## Data model

```text
PageTrace
- source_url
- normalized_path
- title
- h1
- canonical_url
- referrer_policy
- outbound_links[]
- quick_exit_links[]
- safety_links[]
- sensitive_matches[]

SensitiveMatch
- location: title | path | heading | link_text | referrer | canonical
- term
- severity
- evidence
- suggested_action

QuickExitFinding
- has_exit_control
- exit_target
- rel_noreferrer
- loading_overlay_hint
- safety_content_linked
- history_warning_present

AuditReport
- generated_at
- crawl_source
- pages[]
- findings[]
- caveats[]
- source_links[]
```

## Technical approach

- Start as a Python CLI with no mandatory network calls for local/static audits.
- Use `httpx` and `beautifulsoup4` or stdlib HTML parsing for the first crawler.
- Keep sensitive vocabulary in a user-supplied YAML file so teams can tune wording by context.
- Bundle conservative rules for browser-visible trace surfaces, not definitive safety claims.
- Export Markdown first for human handoff, then CSV for issue tracking.
- Include public-source links in every caveat section.

## Validation plan

- Fixture tests for unsafe and safer titles, URL slugs, headings, canonical URLs, and outbound links.
- Golden-file tests for Markdown and CSV reports.
- Rule tests for quick-exit link detection and `rel="noreferrer"` checks.
- Public-safety tests to ensure fixture reports contain no real survivor-service domains, private IPs, secrets, or local filesystem paths.
- Wedge validation: publish one synthetic before/after report and ask webdev/nonprofit-tech readers which checks are missing.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and spec.
- v0.1.0-alpha.1 — local fixture crawler plus title/path/heading checks.
- v0.1.0-alpha.2 — quick-exit/referrer/safety-content checks.
- v0.2.0-alpha.1 — live URL crawl, CSV export, and sample before/after report.
