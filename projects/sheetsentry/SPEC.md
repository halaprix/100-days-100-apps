# SheetSentry SPEC

## User story

As a builder using Google Sheets as a lightweight backend, I want a local check that tells me whether my sheet-backed endpoint will return usable data before I ship or demo, so a quota, permission, schema, or cache failure does not blank my page or break my AI agent.

## MVP features

1. `sheetsentry init`
   - Create `sheetsentry.yaml` with endpoints, provider type, required columns, minimum rows, expected content type, optional MCP metadata URL, and snapshot path.
2. `sheetsentry check`
   - Fetch each endpoint with timeout and no secrets.
   - Validate HTTP status, content type, parseable JSON, row count, required columns, empty values in required fields, and response size.
   - Detect common sheet-backed failure signatures: HTML login page, Google permission error, empty array, provider free-cap message, renamed/missing tab, stale cache marker, and malformed MCP tool metadata.
3. `sheetsentry snapshot`
   - Save last-known-good JSON plus metadata to `dist/sheetsentry/<name>.json`.
   - Emit a tiny browser fallback snippet for static sites.
4. `sheetsentry report`
   - Produce Markdown and JSON reports with severity, likely cause, evidence, and provider-specific fix links.

## Data model

```yaml
version: 1
endpoints:
  - name: faq
    provider: opensheet
    url: https://opensheet.elk.sh/example/Sheet1
    required_columns: [question, answer]
    min_rows: 3
    mcp_url: null
    snapshot: dist/sheetsentry/faq.json
```

## Build plan

- Language: TypeScript CLI on Node.js 22+.
- CLI: `tsx` during development, packaged with `bin` entry.
- Validation: `zod` for manifest and response checks.
- Tests: fixtures for healthy, empty array, HTML login page, missing column, stale snapshot, and provider error body.

## Validation plan

- Unit-test every detector with static fixtures.
- Run `sheetsentry check` against mock fixture server in CI.
- Demo with one intentionally broken fixture and one healthy public-style fixture.

## Privacy and security

- Public/read-only endpoints only in MVP.
- Do not ask for OAuth tokens, service account JSON, cookies, or provider API keys.
- Redact query strings in reports by default.
