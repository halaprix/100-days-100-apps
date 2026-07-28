# HeaderPass

Local-first diagnostics for self-hosted apps that break behind Cloudflare Access, tunnels, and non-browser clients.

## Problem

Self-hosters often protect apps with Cloudflare Access or tunnel/proxy layers, then discover that mobile clients, desktop apps, sync daemons, or API consumers fail because they cannot complete browser-oriented auth, send the required headers, or survive tunnel/origin edge cases.

The risky workaround is to weaken protection, expose a second hostname, paste one-off proxy snippets, or keep debugging by trial and error.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1ul29ev/how_can_i_set_http_header_for_cloudflare_tunnels/ | Fresh self-hoster asks how to set headers/rules for Cloudflare Tunnels so mobile apps can access Immich/OpenCloud while away from home. |
| GitHub issue | https://github.com/blinkospace/blinko/issues/1005 | Blinko user reports the web UI works behind Cloudflare Access, but the mobile app cannot send `CF-Access-Client-Id` / `CF-Access-Client-Secret` headers. |
| Cloudflare docs | https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/ | Cloudflare Access supports service-token auth via request headers, but setup spans tokens, policies, and app behavior. |
| Cloudflare docs | https://developers.cloudflare.com/cloudflare-one/access-controls/troubleshooting/ | Access failures include CORS, cookie/session, login-loop, and policy issues that are hard to distinguish from origin failures. |
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1ul8o50/question_regarding_ipv6_change/ | Another fresh self-hoster hits remote-access fragility when ISP IPv6 changes break exposed Docker services. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Cloudflare Access / Tunnel docs and dashboard | Official source of truth, but not a local test harness for a specific app/client/tunnel chain. |
| Direct competitor | Tailscale Serve/Funnel | Solves a different access model; useful alternative, not a Cloudflare Access header/policy debugger. |
| Indirect substitute | Nginx Proxy Manager, Caddy, ad-hoc `curl` commands, forum snippets | Can route traffic, but leaves users to reason manually about headers, cookies, service tokens, CORS, and mobile-client behavior. |
| Status quo | Disable Access, create an unprotected bypass hostname, or keep pasting config from threads | Fast but risky; can leak private services or create inconsistent app behavior. |

## Wedge

HeaderPass does not try to replace Cloudflare, Tailscale, or reverse proxies. It is a small local diagnostic and runbook generator for one painful slice: "will this non-browser client reach this protected self-hosted app, and which auth/header/proxy rule is missing?"

That narrow scope is demoable, privacy-preserving, and distributable through concrete r/selfhosted and app-specific issue threads where users already ask for custom-header and tunnel fixes.

## Target user

Self-hosters running apps such as Immich, OpenCloud, Blinko, Home Assistant, Jellyfin, and similar services behind Cloudflare Access, Cloudflare Tunnel, Nginx Proxy Manager, Caddy, or Tailscale.

## MVP

- CLI that accepts a target URL, expected client type, and optional local config files.
- Probes browser-like and API-client-like requests and classifies failures: Access auth, missing service token, CORS/cookie, origin TLS/SNI, tunnel routing, DNS/IP drift, or app-level rejection.
- Emits a redacted markdown runbook with safe next steps and copyable `curl` checks.
- Never stores or prints secret header values; it only records header presence, hash prefixes, and redacted examples.

## Non-goals

- Not a hosted proxy, tunnel provider, or secret vault.
- Not an automatic Cloudflare account mutator in the MVP.
- Not a bypass tool for third-party services.
- Not a replacement for Cloudflare, Tailscale, Caddy, or Nginx Proxy Manager.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
