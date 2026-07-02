# Day 014 — HeaderPass

Date: 2026-07-02
Status: repo-created
Repo: https://github.com/halaprix/headerpass

## One-line pitch

Local-first diagnostics for self-hosted apps that break behind Cloudflare Access, tunnels, and non-browser clients.

## Source access caveats

- Reddit public JSON returned `HTTP 403 theme-beta`; r/selfhosted and r/LocalLLaMA evidence came through the reddit-readonly RSS fallback, so scores/comment counts are unavailable and treated as meaningless.
- Reddit thread/comment fetches also returned `HTTP 403`, so this brief uses post titles/snippets plus public competitor/docs pages.
- X/Twitter `whoami` worked, but X search returned `401 Unauthorized`; no X evidence was used.
- Web search had spotty `site:reddit.com` coverage, so competitor validation used original docs and public GitHub issues where possible.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1ul29ev/how_can_i_set_http_header_for_cloudflare_tunnels/ | Fresh self-hoster wants headers/rules for Cloudflare Tunnels so Immich/OpenCloud apps can work away from home without weakening access controls. |
| GitHub issue | https://github.com/blinkospace/blinko/issues/1005 | Blinko user says web UI works behind Cloudflare Access, but the mobile app cannot pass `CF-Access-Client-Id` / `CF-Access-Client-Secret` headers and is blocked. |
| Cloudflare docs | https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/ | Cloudflare Access supports service-token auth through request headers, including service-token policy setup and request headers. |
| Cloudflare docs | https://developers.cloudflare.com/cloudflare-one/access-controls/troubleshooting/ | Access failures can look like CORS, cookies, sessions, login loops, or policy errors, making origin-vs-auth diagnosis noisy. |
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1ul8o50/question_regarding_ipv6_change/ | Another fresh self-hoster hit remote-access fragility when ISP IPv6 changes affected exposed Docker services. |
| Tailscale docs | https://tailscale.com/docs/reference/tailscale-cli/serve | Tailscale Serve/Funnel is a credible alternative access path, but it changes the access model rather than diagnosing Cloudflare header/auth failures. |

## Problem

Self-hosters increasingly put private apps behind Cloudflare Access, Cloudflare Tunnel, Tailscale, Nginx Proxy Manager, or similar layers. Browser access may work, but mobile apps, desktop sync clients, CLI clients, and APIs often fail because they cannot complete browser-oriented auth, cannot attach service-token headers, lose cookies/JWTs on retry, hit CORS/session issues, or route through the wrong origin/SNI/host-header path.

The current troubleshooting path is scattered: forum snippets, dashboard guesses, ad-hoc `curl`, app-specific GitHub issues, and risky bypass hostnames. This can waste hours and can push users toward disabling security.

## Target user

Self-hosters running apps such as Immich, OpenCloud, Blinko, Home Assistant, Jellyfin, and similar tools behind Cloudflare Access/Tunnel or a reverse proxy, especially when a non-browser client fails while the browser UI works.

## MVP scope

- CLI: `headerpass check <url> --client mobile-api|sync-daemon|browser`.
- Probe browser-like and API-client-like request paths with redirects, cookies, status codes, TLS metadata, and header-presence checks.
- Classify failures: Cloudflare Access auth, missing service token, CORS/cookie/session, origin TLS/SNI, tunnel routing, DNS/IP drift, or app-level rejection.
- Export a redacted markdown runbook with copyable checks and safe next steps.
- Never store or print secret header values; only show header names, redacted examples, and hashes/presence indicators.

## Shortlist and wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| HeaderPass | Self-hosters with protected mobile/API clients → Cloudflare docs, Tailscale, Nginx/Caddy snippets, ad-hoc `curl` → those explain pieces but do not classify one user's browser-vs-mobile failure safely → local redacted probe/runbook for Cloudflare Access headers and tunnel/proxy failure classes → r/selfhosted + app GitHub issues + searchable runbooks → Cloudflare Access + mobile/self-hosted apps keep colliding now. | Winner; narrow enough, status-quo pain creates security risk, and distribution has concrete threads. |
| CronBrief | Self-hosters with several cron/systemd scripts → Healthchecks.io, Cronitor, Uptime Kuma, Airflow-lite projects → hosted monitors catch misses but not local dependency/log/resource explanations → read-only local cron/systemd inventory that emits failure briefs → r/selfhosted posts about lightweight cron alternatives → recurring script sprawl. | Good pain but direct/indirect competition is strong; narrower wedge needed. |
| QuantPick | Local LLM deployers choosing AWQ/GPTQ/GGUF/FP8 → vLLM docs, LLM Compressor, blog benchmarks, community CLIs → docs list support but not per-user hardware/quality tradeoff → small benchmark harness for one model/hardware budget → r/LocalLLaMA benchmark threads → quant formats keep changing. | Rejected for today: source post already described a similar CLI; crowded benchmark space. |
| SchemaRetry Kit | LLM app developers with flaky structured output → Instructor, Outlines, PydanticAI, LangChain retry parsers → generic retries hide validation-specific repair details → tiny validator-error feedback adapter with fixtures → Python/LLM dev communities → structured output remains a common failure mode. | Rejected for today: useful but crowded library category and distribution weaker than HeaderPass. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Cloudflare Access / Tunnel docs | Official and necessary, but not a local diagnostic harness for a specific app/client/tunnel path. Docs explain service tokens and troubleshooting categories; users still map them manually to their setup. |
| Direct competitor | Tailscale Serve/Funnel | Strong alternative for private/public service access, but it changes the access model rather than diagnosing Cloudflare Access service-token/header problems. |
| Direct competitor | App-specific custom-header support | Best long-term fix inside each app, shown by the Blinko issue, but coverage is fragmented and per-app. HeaderPass can generate the evidence/runbook app maintainers need. |
| Indirect substitute | Nginx Proxy Manager, Caddy, cloudflared YAML, ad-hoc `curl`, forum snippets | Useful primitives, but users must manually reason about headers, cookies, redirects, CORS, SNI, service-token policy, and origin failures. |
| Status quo | Disable Access, add an unprotected bypass hostname, expose ports, or keep trial-and-error debugging | Security-risky and time-consuming; one wrong bypass can expose private services. |

## Wedge

HeaderPass wins only by staying narrow: it is not another tunnel, proxy, auth provider, or hosted dashboard. It is a local-first diagnostic for one painful situation: "browser works, non-browser client fails behind Cloudflare Access/tunnel/proxy." The output is a redacted runbook users can paste into GitHub issues or forum replies without leaking secrets.

The wedge is strongest where app maintainers need proof that custom headers or Access-friendly behavior are required. That creates a distribution path through r/selfhosted troubleshooting threads and app-specific GitHub issues, not generic Product Hunt traffic.

## Kill condition

Reject or narrow if app-level custom-header support becomes common enough that users no longer need diagnostics, or if a mature Cloudflare/Tailscale tool ships a local client-mode probe with redacted runbook export. Also kill if early users mostly want automatic Cloudflare account mutation; that would expand scope into secrets and permissions too early.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Breakage can waste hours and tempts users to weaken access controls; fresh Reddit and GitHub issue evidence shows real non-browser-client pain. |
| Feasibility | 4/5 | A 1-3 day MVP can probe HTTP behavior, classify common cases, and export a redacted runbook without cloud API writes. |
| Demo potential | 4/5 | Easy terminal demo: one failing protected URL fixture, classified cause, before/after `curl` checks, redacted markdown output. |
| Distribution | 4/5 | Specific r/selfhosted and app-maintainer issue channels exist; distribution can be via public troubleshooting runbooks and replies, not broad launch spam. |
| Competitive wedge / timing | 3/5 | Incumbents are strong infrastructure tools, but they do not own the local non-browser-client diagnostic/runbook layer. |
| Total | 19/25 | Clears repo threshold and gates. |

## Decision

Create the dedicated repo because HeaderPass scored 19/25, Distribution is 4/5, and Competitive wedge / timing is 3/5.

Repo created and scaffold pushed: https://github.com/halaprix/headerpass

## Next build step

Implement the first CLI skeleton: `headerpass check <url>` with HTTP probe modes, redaction tests, and fixture scenarios for Cloudflare Access login, missing service-token headers, and origin/TLS mismatch.
