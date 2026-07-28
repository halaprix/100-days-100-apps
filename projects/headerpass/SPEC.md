# SPEC — HeaderPass

## User story

As a self-hoster protecting apps behind Cloudflare Access or a tunnel/proxy chain, I want a local diagnostic that tells me why a non-browser client cannot connect, so that I can fix access without exposing a private service or leaking tokens.

## Core flow

1. User runs `headerpass check https://app.example.test --client mobile-api`.
2. CLI performs safe probes that mimic browser and non-browser access patterns.
3. User can optionally provide redacted config paths or environment names for tunnel/proxy context.
4. HeaderPass classifies the failure and prints a concise explanation.
5. HeaderPass writes a public-safe runbook with copyable checks and redacted config hints.

## MVP feature list

- URL probe runner with browser-like and API-client-like modes.
- Cloudflare Access detector: login page, 401/403, service-token header requirements, Access cookie/JWT hints.
- Reverse-proxy/tunnel detector for common symptoms: wrong host header, TLS/SNI mismatch, CORS, redirect loop, DNS/IP drift, origin unreachable.
- Redaction layer for tokens, hostnames optionally marked private, cookies, and Authorization headers.
- Markdown runbook export for sharing in issues/forums without secrets.

## Data model

```text
ProbeTarget
- url
- client_mode: browser | mobile-api | sync-daemon | generic-http
- expected_status
- headers_present: list of header names only

ProbeResult
- request_kind
- status_code
- redirect_chain_summary
- detected_platform: cloudflare-access | cloudflare-tunnel | tailscale | reverse-proxy | unknown
- failure_class
- evidence: redacted snippets only

Runbook
- summary
- likely_cause
- safe_checks
- suggested_fix
- risk_notes
```

## Technical approach

- Language: Python CLI first; package with `uv`/`pipx` later.
- HTTP probing: `httpx` with redirects, cookie jar, TLS metadata, and timeout controls.
- Redaction: denylist sensitive headers and token-like values before any output.
- Config parsing: start with optional cloudflared YAML, Caddyfile, and Nginx Proxy Manager exported snippets if supplied manually.
- No cloud account API writes in the MVP.

## Validation plan

- Reproduce three fixture scenarios locally: Cloudflare Access login page, missing service-token headers, and origin/TLS mismatch.
- Verify redaction by snapshot tests that include fake secrets and cookies.
- Compare generated runbooks against official Cloudflare Access service-token and troubleshooting docs.
- Share a public-safe sample runbook in r/selfhosted-style format and check whether the explanation is understandable without private details.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and evidence-backed spec.
- v0.1.0-alpha.1 — CLI skeleton with HTTP probes and redaction tests.
- v0.2.0-alpha.1 — fixture-based demo for Cloudflare Access and tunnel failures.
