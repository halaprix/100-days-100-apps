# SPEC — DavSync Doctor

## User story

As a self-hoster with Radicale/Baïkal and Apple Contacts sync failures, I want a safe local diagnostic command so that I can identify whether the problem is discovery, auth encoding, collection visibility, permissions, vCard data, TLS/proxy behavior, or sync tokens before posting a support request.

## Core flow

1. User runs `davsync-doctor check https://dav.example.test --username USER`.
2. CLI prompts for a password or app password without echoing it.
3. CLI performs read-mostly CardDAV checks in the same order an Apple client depends on:
   - `/.well-known/carddav` redirect and TLS status.
   - `current-user-principal` PROPFIND.
   - `addressbook-home-set` PROPFIND.
   - address book collection listing.
   - OPTIONS capability check.
   - sample `addressbook-query` REPORT.
   - optional sample vCard validation from a local file.
4. CLI maps failures to plain-language fixes and links to public docs.
5. CLI writes a redacted Markdown/JSON report for sharing.

## Data model

```text
CheckResult
- id: stable check id
- title: human-readable check name
- severity: pass | warn | fail | skipped
- evidence: redacted HTTP status, DAV property, or parser result
- explanation: why it matters for Apple Contacts
- suggested_fix: one actionable next step

Report
- target_summary: scheme, port, server type if detectable, redacted host
- client_profile: selected client assumptions, e.g. iOS/macOS native CardDAV
- results: CheckResult[]
- redactions: fields removed or masked
```

## Technical approach

- Language: Python initially, because HTTP/WebDAV XML parsing and packaging are straightforward.
- CLI: `typer` or `argparse` for a small install footprint.
- HTTP: `httpx` with explicit custom methods for PROPFIND and REPORT.
- XML: standard-library `xml.etree.ElementTree`; no need for a full DAV client in the MVP.
- vCard validation: start with syntax checks for UID, FN/N, VERSION, and line folding; add stricter checks later.
- Privacy: secrets are never logged; hostnames, usernames, contact names, emails, phone numbers, and Authorization headers are redacted in reports by default.

## Validation plan

- Unit-test XML parsing and redaction with fixture responses.
- Run against a local Radicale container with known-good config.
- Add fixtures for common failure cases: missing well-known redirect, encoded username mismatch, no addressbook-home-set, read-only collection, malformed vCard, stale ETag/sync-token.
- Validate wedge by posting the redacted report format to Radicale/GitHub-style issue templates manually, not by automating social posting.

## Milestones

- v0.1.0-alpha.0 — repo scaffold.
- v0.1.0-alpha.1 — CLI skeleton and local Radicale fixture.
- v0.2.0-alpha.1 — first real diagnostic report with redaction tests.
