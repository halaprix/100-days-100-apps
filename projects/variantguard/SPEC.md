# SPEC — VariantGuard

## User story

As a web/platform engineer using Cloudflare Cache Rules, I want a deterministic
request matrix that verifies negotiated variants stay distinct after cache
fills, so that I can catch a misconfigured `Vary` rule before users receive the
wrong representation.

## Core flow

1. The user supplies a public URL and a local case file with request headers and
   expected content types or body markers.
2. VariantGuard warms and repeats each case, records response headers and a
   privacy-safe body fingerprint, then compares results.
3. It renders a Markdown/JSON packet with mismatches and a suggested Cache Rules
   action; CI exits nonzero for a configured severity.

## Feature list

- CLI: `variantguard check <url> --cases cases.yml`.
- Header-case parser for `Accept` and `Accept-Language`.
- Two-pass fetches with response status, `Vary`, `Content-Type`, `CF-Cache-Status`,
  `Age`, and SHA-256 body fingerprints.
- Expected-variant assertions and mismatch classification.
- Report renderer and CI-friendly exit codes.
- Documentation-only suggestions for Cache Rules Vary actions.

## Data model

```text
Case: name, request_headers, expected_content_type?, expected_body_marker?
Observation: case, pass, response_headers, body_sha256, body_bytes, timestamp
Finding: severity, rule_id, affected_cases, explanation, suggested_action
Report: target_url, cases, observations, findings
```

Reports never include full response bodies or authorization headers.

## Technical approach

Implement a Python CLI using the standard library for HTTP and hashing. Keep
case files local. Default to redacting query values from output and rejecting
URLs with embedded credentials. Use fixtures with a local test server for
reproducible variant and cache-header behavior.

## Validation plan

- Unit-test header-case parsing, redaction, fingerprints, and mismatch rules.
- Integration-test a fixture origin that returns HTML/Markdown and locale
  variants from `Accept` / `Accept-Language`.
- Demonstrate a failing same-fingerprint case and a passing split-variant case.
- Interview five Cloudflare Cache Rules users from public community threads or
  repositories; proceed only if at least three would run the check in CI or
  pre-deploy review.

## Milestones

- `v0.1.0-alpha.0` — repository scaffold and product specification.
- `v0.1.0-alpha.1` — case parser, fixture origin, and terminal report.
- `v0.2.0-alpha.1` — Markdown/JSON packet and CI exit mode.
- `v0.3.0-alpha.1` — validate the wedge with five target users.
