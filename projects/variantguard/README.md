# VariantGuard

A local CLI and CI check that proves Cloudflare returns the correct cached
content variant for each `Accept` or `Accept-Language` request before a cache
rule ships.

## Problem

Teams that cache a content-negotiated site behind Cloudflare can serve the
wrong representation after a cache fill: raw Markdown instead of HTML, or the
wrong language. `Vary` at the origin is necessary but Cloudflare's Cache Rules
Vary setting must also be configured. Manual `curl` checks are easy to miss and
usually happen after an embarrassing public incident.

## Target user

A small web/platform team using Cloudflare Cache Rules with an origin that
varies HTML, Markdown, JSON, or locale responses by request header.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Community report | https://www.reddit.com/r/selfhosted/comments/1vxrrm8/cloudflare_ignores_the_vary_header_and_it_took_me/ | A self-hoster reported users receiving raw Markdown after assuming their origin's `Vary: Accept` alone would partition Cloudflare's cache. |
| Cloudflare changelog | https://developers.cloudflare.com/changelog/post/2026-07-02-vary-for-cache-rules/ | On July 2, 2026, Cloudflare added `Vary` support to Cache Rules on all plans, but it must be enabled/configured. |
| Cloudflare documentation | https://developers.cloudflare.com/cache/concepts/vary/ | Cloudflare documents `normalize`, `passthrough`, and `bypass`, plus the interaction between origin `Vary` and Cache Rules. |

## Competitor / substitute check

| Type | Name / substitute | Notes |
|---|---|---|
| Direct competitor | Cloudflare Cache Rules and Cache Trace | Configure or inspect cache behavior, but do not provide a deploy-time matrix proving response-body/variant separation for a chosen endpoint. |
| Indirect substitute | `curl`, browser DevTools, and hand-written integration tests | Flexible but repetitive; they do not normalize header cases or emit a reviewable cache-variant verdict. |
| Status quo | Wait for a cache miss/hit sequence to expose the error | A wrong public representation can remain served until expiry or purge. |

## Wedge

VariantGuard is a narrow, deterministic regression check, not a generic header
scanner or Cloudflare dashboard. It makes the newly configurable Cache Rules
Vary behavior testable from an endpoint and a small request matrix, without
Cloudflare credentials or source upload.

## MVP

- Accept a URL and a YAML/JSON matrix of request-header cases.
- Fetch each case twice, capture cache and content headers, and compare expected
  content type, response fingerprint, and cache status.
- Emit Markdown/JSON evidence and `--fail-on mismatch` for CI.
- Suggest a safe Cache Rules Vary action (`normalize`, `passthrough`, or
  `bypass`) without applying configuration.

## Non-goals

- No Cloudflare API write access or stored credentials.
- No cache-rule auto-remediation.
- No generalized CDN abstraction in the first release.

## Status

`v0.1.0-alpha.0` — local scaffold and specification only.
