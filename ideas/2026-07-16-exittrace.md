# Day 028 — ExitTrace

Date: 2026-07-16
Status: repo-created

## One-line pitch

A local crawler and report generator for sensitive support websites that need discoverable SEO content without leaving dangerous page titles, URLs, referrers, history entries, or broken quick-exit flows on a survivor's device.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS fallback — r/webdev | https://www.reddit.com/r/webdev/comments/1uxu9yn/looking_for_a_solution_to_mask_page_titles_for/ | Fresh post from an SEO consultant asks how to keep domestic-abuse support pages discoverable while preventing descriptive titles from appearing in tabs, browser history, and address-bar autocomplete. |
| GOV.UK Design System | https://design-system.service.gov.uk/patterns/exit-a-page-quickly/ | The official pattern says quick-exit flows are for sensitive services, warns that browsing history is not erased, and recommends safety-content pages that explain private browsing and selective history deletion. |
| GOV.UK Design System | https://design-system.service.gov.uk/components/exit-this-page/ | The component guidance says quick exit is for pages that could put someone at risk of abuse or retaliation, and notes known gaps for static information pages. |
| Safety Net Project / NNEDV | https://techsafety.org/seekinghelponline | Survivor safety guidance says online-chat sites may not save messages locally, but the visited website can still appear in browser history and should be removed carefully. |
| Safety Net Project / NNEDV | https://www.techsafety.org/internetbrowserprivacytips | Browser privacy guidance explains that history, cookies, private browsing, and sudden clearing behavior can create safety tradeoffs for monitored users. |
| W3C WCAG 2.2 | https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html | Accessibility guidance requires meaningful page titles, creating a real tension with safety-sensitive, descriptive titles on abuse-support content. |
| Google Chrome Help | https://support.google.com/chrome/answer/95589 | Chrome documents that visited websites are recorded in browser history and can sync across signed-in devices. |

Source access notes: Reddit public JSON and comment-thread endpoints returned `HTTP 403 theme-beta`, so Reddit evidence used the read-only skill's public RSS fallback. Several RSS feeds were also rate-limited. X `whoami` worked, but X search returned `401 Unauthorized`, so X was not used as evidence. Repo files referenced by the public README (`docs/PROCESS.md`, `docs/SCORING.md`, and `sources.yml`) were not present in this checkout; the run followed `AGENTS.md` plus loaded project context.

## Shortlist and wedge gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| ExitTrace | SEO consultant or small charity web developer → WCAG title rules, GOV.UK quick-exit component, private-browsing advice, manual browser testing → substitutes solve pieces but do not produce a page-by-page trace-risk packet for titles, URLs, referrers, history/autocomplete language, and quick-exit content → local crawler with safe-title/slug/referrer/exit-flow checks and Markdown handoff → r/webdev, civic-design, nonprofit-tech, accessibility, and SEO-for-sensitive-services content/replies → fresh r/webdev post exposes the exact SEO-vs-survivor-safety conflict now. | Winner; scored. |
| RDM Escape Plan | Small IT admin team forced off Devolutions Remote Desktop Manager pricing → Royal TS, mRemoteNG, KeePass/RDPMan, spreadsheets, vendor comparisons → substitutes require manual export/feature mapping and credential-storage risk review → migration-readiness checklist from existing RDM inventory to shortlist alternatives → r/sysadmin reply/search around new licensing model → fresh r/sysadmin post names bundle pricing and SQL backend deprecation. | Rejected: painful but crowded remote-connection-manager market; v0 would mostly be a buyer-guide wrapper unless it can parse real RDM exports. |
| Package Slop Sieve | Web developer choosing packages in an AI-generated-library flood → OpenSSF Scorecard, Socket, Snyk, npm trends, GitHub stars/manual audits → substitutes focus security or popularity, not architectural/test-quality triage for a specific job → repo shortlist scorecard with test depth, maintenance shape, examples, and API-fit notes → r/webdev/library-selection content and package-specific searches → fresh r/webdev thread says package filtering now burns serious time. | Held/rejected: real pain, but supply-chain/package scoring is crowded and risks becoming a generic security scanner. |
| Homepage PVE Widget Doctor | Self-hoster debugging Homepage's Proxmox widget 401 while curl succeeds → Homepage docs, Proxmox API docs, forum replies, log spelunking → substitutes require posting redacted configs and guessing token/user realms → offline config/log validator for Homepage + Proxmox API tokens → r/selfhosted, Homepage GitHub issues, Proxmox searches → fresh r/selfhosted post leaked config shape while asking what was missing. | Narrow but lower ceiling; useful as a plugin/issue-answer rather than today's strongest standalone app. |
| Agent Browser Sandbox | Small web-tool builder using AI agents for UI checks → separate browser profiles, Playwright contexts, Docker browsers, manual cookie cleanup → substitutes exist but are not framed as non-leaky agent-review sessions with reset prompts → CLI that launches named disposable profiles with permissions/download isolation → AI-coding and webdev communities → fresh r/webdev post asks whether AI tools should get isolated browser sessions. | Rejected for today: good but close to crowded AI-agent/browser-automation infrastructure; distribution is less concrete than ExitTrace. |

## Problem

Sensitive support sites face a nasty product-design conflict:

- SEO and WCAG push pages toward descriptive titles, headings, and URLs.
- Survivors and other at-risk users may be monitored through browser tabs, history, synced history, address-bar autocomplete, screenshots, or someone looking over their shoulder.
- Quick-exit buttons help only one part of the flow, and official guidance explicitly says browsing history is not erased.
- Small charities, legal-aid teams, and consultants often cannot afford bespoke safety research for every page template.

The status quo is manual review: add a quick-exit button, write a safety page, test a few browsers by hand, and hope titles/slugs/referrers are not exposing the user. That can burn hours per site and still miss synced history, page-title wording, referral paths, or static content pages outside the main service journey.

## Target user

- SEO consultants and web developers working on domestic-abuse, legal-aid, health, whistleblowing, stalking, trafficking, or crisis-support resources.
- Small nonprofit/civic-tech teams that need a practical safety handoff before publishing sensitive pages.
- Accessibility-minded product teams trying to balance descriptive page titles with user safety.

## MVP scope

- Local CLI crawler: `exittrace audit https://example.org --sensitive-map sensitive.yml`.
- Static export/input mode for pre-launch sites: crawl a local build directory or sitemap XML.
- Checks for risky page titles, sensitive URL slugs, breadcrumb/header/title mismatch, referrer leakage, quick-exit presence, safety-content links, `rel="noreferrer"` on exit links, and pages that need noindex or alternate wording review.
- Browser-behavior notes for Chrome/Safari/Firefox history, autocomplete, sync, and private-browsing caveats, with source links.
- Markdown/CSV report with page-by-page findings, severity, evidence snippets, and suggested safer wording patterns.
- Redaction defaults so public demo reports do not expose real survivor-service URLs unless explicitly allowed.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | GOV.UK Exit this page component and Exit a page quickly pattern | Excellent implementation guidance and research-backed pattern, but not an auditor for arbitrary sites, SEO titles, URL slugs, referrers, or browser-history wording. |
| Direct competitor | Accessibility/SEO crawlers such as Lighthouse, Screaming Frog, Sitebulb, and axe | Catch titles, links, accessibility, and SEO issues, but they do not classify survivor-safety trace risk or quick-exit/safety-content completeness. |
| Direct competitor | Domestic-abuse site quick-exit widgets and agency checklists | Useful components/checklists, but usually do not produce repeatable, browser-trace-specific evidence across every sensitive page. |
| Indirect substitute | Manual review in Chrome/Safari/Firefox private and normal sessions | Possible for experts, but slow, inconsistent, and easy to miss synced history, autocomplete wording, referrers, and static content pages. |
| Status quo | Publish descriptive pages with a quick-exit button and a safety note | Better than nothing, but still leaves page titles/URLs/history entries that can expose a monitored user. |

## Wedge

ExitTrace is not a generic SEO, accessibility, or security scanner. It is a narrow safety-design audit for the trace a sensitive page leaves on a user's device and in browser UI:

- crawl pages and classify visible/browser-stored text such as `<title>`, canonical URL, headings, breadcrumbs, and outbound referrers,
- flag pages where safety-sensitive wording appears in places likely to be visible in tabs, history, autocomplete, or synced history,
- verify quick-exit implementation details and whether safety-content pages clearly warn that history is not erased,
- emit a practical report that a consultant can hand to a charity/web team before launch.

The first-user path is concrete: the original r/webdev thread, GOV.UK Design System discussion spaces around quick-exit gaps on flat content, nonprofit/civic-tech web teams, SEO consultants working in sensitive verticals, and search content around "domestic violence website SEO browser history" and "quick exit button does not erase history".

## Kill condition

Reject or narrow if field feedback from survivor-safety organizations says automated trace-risk reports create false confidence, or if existing accessibility/SEO crawlers add first-class quick-exit/history-risk checks that cover titles, slugs, referrers, safety content, and browser caveats in one report.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 5/5 | A bad title, slug, or history entry can create real safety risk, public embarrassment, or harm; the workaround is expert manual review. |
| Feasibility | 4/5 | v0 can be a local crawler plus static rules and Markdown/CSV output; browser-specific history/autocomplete behavior must be caveated rather than overpromised. |
| Demo potential | 4/5 | A synthetic crisis-support site can show unsafe titles/slugs, missing warnings, and a clean before/after report. |
| Distribution | 4/5 | Specific communities and channels exist: r/webdev, civic-design/GOV.UK discussions, nonprofit-tech, accessibility, and SEO consultants in sensitive domains. |
| Competitive wedge / timing | 4/5 | The fresh thread captures a narrow SEO-vs-safety gap; incumbents solve SEO/accessibility/components, not trace-risk packets. |
| Total | 21/25 | Clears repo threshold and both dimension gates. |

## Decision

Create `halaprix/exittrace` as a dedicated project repo. The score clears the 18/25 threshold, Distribution is 4/5, and Competitive wedge/timing is 4/5.

## Next build step

Implement `exittrace audit --local fixtures/survivor-site --sensitive-map fixtures/sensitive.yml` with title/URL/referrer/quick-exit checks and a synthetic Markdown report.
