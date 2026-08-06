# SPEC — RelayTrace

## User story

As a self-hosted mail admin using a forwarding relay, I want to verify that the
relay preserves original envelope-recipient evidence for catch-all aliases, so
that I can trust routing and spam-source tracing before changing MX records or
provider setup.

## Core flow

1. User writes a probe plan with domain, expected aliases, and accepted header
   names.
2. User sends test mail through their relay manually or uses synthetic fixtures.
3. User saves raw RFC822 messages into a local folder.
4. `relaytrace check` parses headers, maps observed recipients to expected
   aliases, and emits a markdown packet plus machine-readable JSON.
5. The packet flags preserved, missing, ambiguous, overwritten, and untested
   recipient evidence.

## Data model

```yaml
relay:
  name: example-forwarder
  accepted_headers:
    - X-Envelope
    - X-Original-To
    - Delivered-To
probes:
  - id: catchall-token-1
    expected_recipient: token1@example.test
    expected_route: spam-source-tagging
  - id: catchall-token-2
    expected_recipient: token2@example.test
    expected_route: default-catchall
```

JSON summary fields:

- `plan_id`
- `message_count`
- `probes[]`
  - `id`
  - `expected_recipient`
  - `observed_headers[]`
  - `status`: `preserved | missing | ambiguous | overwritten | untested`
  - `notes[]`

## Technical approach

- Python 3.11 CLI using the standard-library `email` parser for scaffold MVP.
- Optional YAML dependency can be introduced later; v0 can accept JSON or a tiny
  YAML subset to avoid dependency setup friction.
- Deterministic, offline-only parser first. Live SMTP sending is delayed until
  users confirm the header-packet workflow is valuable.
- Output files:
  - `relaytrace-report.md`
  - `relaytrace-summary.json`

## Validation plan

- Unit fixtures for preserved, stripped, ambiguous, and overwritten headers.
- Golden markdown output for a synthetic catch-all relay plan.
- Manual review against Swaks/MXToolbox/Postfix docs to keep wording honest:
  RelayTrace complements generic SMTP/header tools; it does not claim to replace
  server-health or deliverability diagnostics.
- Early validation question: does the packet surface a relay assumption that a
  self-hosted mail user would check before changing provider/MX setup?

## Milestones

- v0.1.0-alpha.0 — repo scaffold and public-safe spec.
- v0.1.0-alpha.1 — offline fixture parser and markdown/json report.
- v0.2.0-alpha.1 — optional live probe sender using local credentials only.
