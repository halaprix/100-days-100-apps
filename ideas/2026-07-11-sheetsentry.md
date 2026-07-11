# Day 023 — SheetSentry

Date: 2026-07-11
Status: repo-created

## One-line pitch

SheetSentry is a local-first CLI that checks Google-Sheets-as-API and Google-Sheets-as-MCP endpoints before a quota, permission, schema, cache, or provider-limit failure blanks a public page or breaks an AI agent demo.

## Source access caveat

Reddit public JSON returned the known `theme-beta` HTTP 403 block, so the run used the reddit-readonly RSS fallback for r/SideProject, r/SaaS, and r/sysadmin. Several configured subreddits returned RSS HTTP 429 and were treated as unavailable rather than retried in a loop. Reddit thread fetches also returned HTTP 403, so comment context was unavailable. X `whoami` worked, but X search returned HTTP 401 Unauthorized, so X did not contribute usable search evidence.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/SideProject | https://www.reddit.com/r/SideProject/comments/1utcnod/i_turned_a_google_sheet_into_a_live_rest_api_mcp/ | Fresh builder says a sheet-to-API service free cap made a public page go blank, then built a pasted-URL REST API plus MCP server. |
| SheetDB | https://sheetdb.io/ | Established category: turn Google Sheets into JSON APIs for CRMs, websites, applications, and tools. |
| Sheety | https://sheety.co/ | Established category: spreadsheet-backed REST APIs for prototypes, websites, apps, and CMS use cases. |
| OpenSheet | https://github.com/benborgers/opensheet | Open-source hosted Google-Sheet-to-JSON API reports 1.5B hits/month, showing large usage of sheet-backed endpoints. |
| PasteSheet guide | https://pastesheet.com/guides/google-sheets-mcp | Timely MCP angle: pasted Google Sheet URL becomes a read-only REST API and MCP server for Claude/Cursor/ChatGPT-style clients. |

## Problem

Small builders use Google Sheets as a lightweight CMS, prototype backend, FAQ store, directory, launch-page database, and now agent-readable MCP data source. The setup is attractive because the editor is familiar and the endpoint can be created quickly.

The operational failure mode is weak: if the sheet permissions change, the tab is renamed, a required column disappears, the provider returns HTML/login/error content, the free cap is hit, or the cache serves stale/empty data, the consuming site or AI agent can silently show blank data. That clears the status-quo pain test because it can publicly break a launch page or demo and cost more than 30 minutes of debugging each time it happens.

## Target user

Indie builders, agencies, developer advocates, and small SaaS teams shipping public pages or AI-agent demos backed by SheetDB, Sheety, OpenSheet, PasteSheet, Apps Script, or a public Google Sheet endpoint.

## Shortlist gate

| Candidate | Wedge-first line | Decision |
|---|---|---|
| SheetSentry | Indie builder using Google Sheets as a tiny backend or MCP data source → SheetDB/Sheety/OpenSheet/PasteSheet plus generic uptime monitors → existing providers expose the endpoint but do not preflight sheet-specific blank-page causes or produce a static fallback → read-only local CLI that checks schema/permissions/provider errors and writes last-known-good JSON → long-tail SEO around sheet-to-API failures, GitHub examples, r/SideProject/MCP replies → fresh Reddit post reports a free-cap blank page and MCP timing is current. | Winner; clears repo gate. |
| ConsentGap | UK SaaS founder losing GA4 visibility after cookie consent changes → GA4 Consent Mode, server-side GTM, Plausible, Fathom, Matomo, agency guides → analytics tools are crowded and several privacy-first substitutes already solve the reporting job → only a tiny “GA4 consent-mode sanity check” wedge remains → UK SaaS/privacy SEO and replies → fresh r/SaaS post asks for cookieless tracking workaround. | Idea-only; crowded analytics category and wedge is too small for repo creation. |
| SheetAudit Lite | Excel-heavy operator with messy workbooks → Excel Inquire, Spreadsheet Compare, PerfectXL, FormulaDesk, Sheetguard-style tools → direct spreadsheet auditing competitors are mature → possible wedge would need a very narrow “pre-upload audit for clients” channel → finance/ops communities → fresh r/SideProject post asks Excel users to test a spreadsheet auditing tool. | Rejected; incumbents already target broken formulas/inconsistent data. |
| VisaPlanLint | Digital nomad planning future stays → Nomad Tracker, ExpatPass, TravelDays, official Schengen calculators, spreadsheets → apps already cover Schengen/tax residency/day tracking and data maintenance is heavy → only possible wedge is local deterministic itinerary linting, not broad visa advice → digital-nomad SEO/communities → fresh r/SideProject post validates forward-planning pain. | Idea-only; crowded and data-liability risk. |
| BackupChoice Matrix | Sysadmin comparing Veeam alternatives → vendor comparisons, Gartner-style reviews, MSP consultants, spreadsheets → decision support is useful but broad and procurement-heavy → narrow wedge would be restore-drill evidence capture, not generic comparison → r/sysadmin/search → fresh r/sysadmin post asks for real-world backup reliability and overhead. | Idea-only; needs sharper first-user proof. |

## MVP scope

- `sheetsentry init` creates a local `sheetsentry.yaml` manifest for one or more sheet-backed endpoints, expected provider, required columns, minimum rows, optional MCP URL, and snapshot path.
- `sheetsentry check` fetches endpoints without secrets and validates HTTP status, content type, parseable JSON, row count, required columns, empty required fields, response size, and common sheet-specific failure signatures.
- `sheetsentry snapshot` writes a last-known-good static JSON fallback bundle and metadata.
- `sheetsentry report` exports Markdown/JSON with severity, likely cause, evidence, and provider-specific fix links.
- Fixtures cover healthy endpoint, empty array, HTML login page, missing column, provider cap/error body, stale snapshot, and malformed MCP metadata.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | SheetDB, Sheety, PasteSheet, OpenSheet | They create or host sheet-backed APIs/MCP endpoints. SheetSentry is not another host; it validates and snapshots endpoints from those services before public failure. |
| Direct competitor | Generic uptime/API monitors such as UptimeRobot, Better Stack, Postman monitors | They can detect HTTP downtime or generic assertions, but they do not know sheet-specific failure modes like renamed tabs, missing columns, empty row arrays, provider caps, stale sheet cache, or MCP tool metadata mismatch. |
| Indirect substitute | Manual browser refreshes, curl scripts, Playwright smoke tests, Apps Script, spreadsheets/checklists | Works for careful developers, but tends to be ad hoc and misses last-known-good fallback generation and provider-specific diagnosis. |
| Status quo | Ship the endpoint, notice blank UI/agent failure after a user or demo hits it, then inspect provider dashboard, sheet permissions, and JSON manually | Publicly embarrassing, launch-blocking, and can burn debugging time because failures often return “valid” but empty or wrong-shaped data. |

## Wedge

SheetSentry wins by avoiding the crowded “turn Sheets into an API” lane. The wedge is a provider-agnostic, local, read-only preflight and fallback layer for builders who already chose a sheet-backed endpoint. A 1–3 day MVP can be useful because it only needs deterministic probes, fixtures, and a static fallback bundle — no OAuth, no hosting platform, no write path, and no private sheet access.

## Kill condition

Kill or narrow the idea if target users say their sheet-backed pages are noncritical prototypes where blank data is tolerable, or if generic API monitors with JSON assertions already catch the provider-cap, missing-column, empty-array, and MCP metadata failures with less setup. Also kill any MVP scope that requires private Google credentials or storing provider API keys.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | The source signal includes a public blank-page failure from a sheet API cap; the problem can break pages, demos, and agent connectors. |
| Feasibility | 4/5 | A deterministic TypeScript CLI with fixtures, probes, schema checks, snapshots, and reports is buildable in 1–3 days. |
| Demo potential | 4/5 | Easy to show: broken sheet endpoint → red report → static fallback JSON → green check. |
| Distribution | 4/5 | Concrete channels: long-tail “SheetDB/Sheety/OpenSheet/PasteSheet blank page” searches, MCP Google Sheets guides, GitHub examples, and helpful replies in builder/MCP threads. |
| Competitive wedge / timing | 4/5 | Existing providers validate demand but leave a narrow operations gap; the new MCP use case makes read-only sheet endpoint reliability more timely. |
| Total | 20/25 | Clears repo threshold and both dimension gates. |

## Decision

Create the dedicated repo because SheetSentry scored 20/25, Distribution is 4/5, and Competitive wedge / timing is 4/5.

Repo: https://github.com/halaprix/sheetsentry

## Next build step

Implement `sheetsentry check` with fixture-backed detectors for empty array, HTML/login response, missing required column, provider cap/error body, stale snapshot, and malformed MCP tool metadata.
