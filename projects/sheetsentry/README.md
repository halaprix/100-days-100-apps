# SheetSentry

SheetSentry is a local-first guardrail for sites, demos, and AI agents that depend on Google Sheets-as-API endpoints.

## Problem

Small builders often use Google Sheets as a lightweight CMS, FAQ, directory, prototype backend, or MCP-readable data source. The failure mode is ugly: a free-cap, permission, quota, schema, tab-name, or cache issue can make a production page or agent connector return empty data with little warning.

## Target user

Indie builders, agencies, and developer advocates shipping small public pages or agent demos backed by SheetDB, Sheety, OpenSheet, PasteSheet, Apps Script, or a public Google Sheet endpoint.

## MVP

- `sheetsentry init` creates a local manifest for one or more sheet-backed endpoints.
- `sheetsentry check` probes status, JSON shape, required columns, cache age, row count, empty-response risk, and read-only MCP endpoint metadata.
- `sheetsentry snapshot` writes a static fallback JSON bundle that can be served if the live endpoint fails.
- `sheetsentry report` exports a Markdown runbook with the exact failure, likely cause, and provider-specific fix links.

## Non-goals

- Not a Google Sheets API host.
- Not a replacement for SheetDB, Sheety, OpenSheet, PasteSheet, or Apps Script.
- Not a write path for agents.
- Not a general-purpose uptime monitor.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/SideProject | https://www.reddit.com/r/SideProject/comments/1utcnod/i_turned_a_google_sheet_into_a_live_rest_api_mcp/ | Fresh builder reports a sheet-to-API service cap caused a page to go blank, then built a pasted-URL REST API plus MCP server. |
| SheetDB | https://sheetdb.io/ | Existing product category: turn Google Sheets into JSON APIs for apps, CRMs, websites, and tools. |
| Sheety | https://sheety.co/ | Existing product category: spreadsheet-backed REST APIs for prototypes, websites, apps, and CMS use cases. |
| OpenSheet | https://github.com/benborgers/opensheet | Open-source hosted sheet-to-JSON API reports 1.5B hits/month, validating large usage of sheet-backed endpoints. |
| PasteSheet guide | https://pastesheet.com/guides/google-sheets-mcp | Timely MCP angle: pasted Sheet URL becomes a read-only REST API and MCP server. |

## Current status

v0.1.0-alpha.0 — scaffold/spec only.
