# Day 061 — VariantGuard

Date: 2026-08-25
Status: repo-created

## One-line pitch

A local CLI and CI check that proves Cloudflare returns the correct cached
content variant for each `Accept` or `Accept-Language` request before a Cache
Rule ships.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Community report (Reddit RSS fallback) | https://www.reddit.com/r/selfhosted/comments/1vxrrm8/cloudflare_ignores_the_vary_header_and_it_took_me/ | On August 25, a self-hoster described serving raw Markdown to visitors after assuming the origin's `Vary: Accept` alone would partition Cloudflare's cache. |
| Original platform changelog | https://developers.cloudflare.com/changelog/post/2026-07-02-vary-for-cache-rules/ | On July 2, Cloudflare added origin `Vary` support to Cache Rules on all plans; the cache rule must enable/configure it. |
| Original platform documentation | https://developers.cloudflare.com/cache/concepts/vary/ | The docs define `normalize`, `passthrough`, and `bypass`, and say that an origin `Vary` response and Cache Rules configuration jointly control cache selection. |
| HTTP reference | https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Vary | `Vary` identifies request fields that influenced a response so caches can store separate representations. |

## Source access caveats

- Reddit's public JSON endpoint was blocked with its theme-beta response. The
  read-only tool used its public RSS fallback for fresh `r/selfhosted`,
  `r/sysadmin`, and `r/SaaS` posts; scores and comment counts are unavailable.
  `r/webdev` and `r/LocalLLaMA` hit `429` and were not retried.
- `xurl whoami` succeeded, but `xurl search` returned `401 Unauthorized`; X
  search was unavailable and no X signal is claimed.
- The winner is supported by one fresh community report plus original
  Cloudflare documentation and changelog, not a claim of broad Reddit/X
  consensus.

## Problem

A content-negotiated origin can return HTML, Markdown, JSON, or locale-specific
content for the same URL. If a team enables edge caching but misses the
Cloudflare Cache Rules `Vary` configuration, one cached representation can be
served to the wrong request. The resulting public bug is hard to reproduce:
it depends on cache-fill order, often appears after deployment, and may persist
until expiry or purge.

This passes the status-quo pain test. The fallback is repeated manual `curl`
and browser checks or waiting for an incident; a wrong representation can cause
public embarrassment, break API consumers, and consume hours of debugging.

## Target user

A small web or platform team using Cloudflare Cache Rules with an origin that
varies HTML, Markdown, JSON, or locale responses by `Accept` or
`Accept-Language`.

## Shortlist and wedge-first gate

| Candidate | Wedge-first gate | Outcome |
|---|---|---|
| VariantGuard | Cloudflare Cache Rules maintainers with content-negotiated endpoints → Cache Rules/Cache Trace plus `curl` → configuration visibility and one-off headers do not prove two cached request variants remain separate → local request-matrix regression packet → Cloudflare community threads, changelog searches, and a reusable GitHub Action → Vary support became configurable in Cache Rules on July 2, 2026 | **Selected**; narrow job, clear defect, and a concrete pre-deploy channel. |
| QuarantineScope | Microsoft 365 admins seeing internal mail quarantined → Defender Explorer/message trace/service health → strong vendor tooling already owns investigation and remediation → incident receipt → M365 admin communities → fresh quarantine report | Rejected before scoring: an incident-only wrapper adds little beyond existing Defender and service-health views. |
| CloudSync Sentry | Entra Cloud Sync operators → Microsoft service health and Sync Health → the reported issue is an upstream outage, not a missing local workflow → status digest → Entra admin communities → August outage report | Rejected before scoring: vendor status and Sync Health are the appropriate system of record; no durable wedge. |
| MailAuth Hand-off | MSPs helping customers fix SPF/DKIM/DMARC → DMARC analyzers, DNS checkers, and documentation → established tools already generate actionable diagnostics → hand-off packet → MSP communities → fresh sysadmin complaint | Rejected before scoring: useful pain but a crowded diagnostics category with no specific advantage. |

## MVP scope

- Accept a URL and a local YAML/JSON matrix of request-header cases.
- Fetch each case twice; record `Vary`, `Content-Type`, `CF-Cache-Status`,
  `Age`, a privacy-safe body fingerprint, and response status.
- Compare expected representation/content type and flag collision or unstable
  cache behavior.
- Emit Markdown/JSON evidence and support `--fail-on mismatch` in CI.
- Suggest, but never apply, a safe Cache Rules action: `normalize`,
  `passthrough`, or `bypass`.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Cloudflare Cache Rules and Cache Trace | They configure or inspect cache behavior but do not produce a deploy-time response-body/variant matrix for a chosen endpoint. |
| Direct competitor | Generic cache-header checkers | They report one URL's headers/cache status, not a repeatable multi-request semantic-variant regression check. |
| Indirect substitute | `curl`, browser DevTools, hand-written integration tests | Flexible but repeated, easy to omit, and typically do not normalize request cases or render a reviewable verdict. |
| Status quo | Wait for cache hit/miss order to expose the mismatch | The error can affect public users and persist until a purge; debugging happens under pressure. |

## Wedge

VariantGuard is deliberately not a generic CDN dashboard or header linter. It
is a local, deterministic check for the small but high-consequence gap between
an origin's `Vary` response and Cloudflare's newly configurable Cache Rules
behavior. It requires no Cloudflare token, never changes a rule, and makes a
pre-deploy proof artifact from a tiny request matrix.

## Kill condition

Reject or narrow if Cloudflare Cache Trace adds a public CI/export mode that
proves response-body separation across an arbitrary header matrix, or if five
relevant Cache Rules maintainers report that a two-case `curl` check reliably
catches the defect in under five minutes and would not run in review/CI.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Wrong cached representations can break clients or publicly display incorrect content; the manual workaround can consume hours. |
| Feasibility | 5/5 | A local CLI can make deterministic HTTP requests, fingerprint bodies, compare cases, and render reports in 1–3 days. |
| Demo potential | 5/5 | A fixture can visibly fail with identical fingerprints, then pass after cache-variant separation. |
| Distribution | 4/5 | The July Cache Rules feature, Cloudflare community/support searches, public GitHub code search, and a reusable GitHub Action form a concrete, repeatable first-user path. |
| Competitive wedge / timing | 4/5 | Cloudflare has strong configuration/inspection tools, but no identified deploy-time request-matrix regression check; the July Vary release gives a timely, narrow wedge. |
| Total | 22/25 | Clears the repository threshold and both dimension gates. |

## Decision

**Repo created locally.** The dedicated local scaffold and its public-safe
master snapshot are [`projects/variantguard`](../projects/variantguard). No
dedicated GitHub remote was created or claimed. The weakest dimension is
usefulness (4/5): the pain is severe for affected sites but applies to a narrow
subset of Cloudflare users.

## Next build step

Implement a fixture origin that serves HTML/Markdown and locale variants, then
build the two-pass request-matrix CLI that emits a failing collision report and
a passing separation report.
