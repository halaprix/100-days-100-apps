# Day 038 — SplitPath

Date: 2026-07-27
Status: repo-created

## One-line pitch

Read-only split-DNS and private reverse-proxy diagnostics for self-hosters using Caddy or Nginx Proxy Manager with Tailscale, NetBird, or similar overlays.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1v7qstp/how_to_access_caddy_reverseproxied_services_over/ | Fresh post: a self-hoster with Cloudflare DNS and Caddy wants NetBird access to reverse-proxied services without exposing Docker ports or public services. |
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1v7j4gg/can_i_get_domains_to_resolve_without_hosting_my/ | Fresh post: a self-hoster using Cloudflare, Nginx Proxy Manager, and Tailscale asks whether they must run their own DNS server for private domains to resolve. |
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1v7ssql/what_tools_do_you_use_to_monitor_packet_loss/ | Fresh post: self-hosters still ask for practical network diagnostics between locations, reinforcing appetite for small self-hosted troubleshooting tools. |
| Tailscale docs | https://tailscale.com/kb/1054/dns | Tailscale supports restricted nameservers / split DNS, but docs note resolver ordering and OS behavior can vary. |
| NetBird docs | https://docs.netbird.io/how-to/manage-dns-in-your-network | NetBird exposes nameservers, match domains, search domains, and a local resolver, creating another failure surface for private names. |
| Caddy docs | https://caddyserver.com/docs/caddyfile/directives/reverse_proxy | Caddy reverse proxying supports host/upstream/TLS behavior that must line up with DNS and overlay routing. |

## Problem

Self-hosters want friendly `service.example.com` hostnames to work both at home and over a private overlay network without exposing services publicly. The failure is rarely one setting: public DNS, local DNS rewrites, MagicDNS or NetBird DNS, client OS resolver behavior, Caddy/NPM host matching, TLS/SNI, and overlay routing all interact.

The current workaround is forum archaeology plus trial-and-error changes to DNS/proxy/router settings. That can waste hours and creates security risk when users make private apps publicly reachable just to make names resolve.

## Target user

Homelab and self-hosted operators using Caddy or Nginx Proxy Manager with Cloudflare-managed domains and Tailscale, NetBird, WireGuard, or similar overlay networks.

## MVP scope

- `splitpath probe service.example.com --lan-ip <expected-private-ip> --overlay-dns <optional-resolver-ip>`.
- Capture public DNS answers, OS resolver answers, optional overlay resolver answers, TCP/TLS reachability, and basic HTTP status/header metadata.
- Classify the likely failure: missing split DNS, public-only DNS, proxy bind mismatch, TLS/SNI mismatch, or client resolver bypass.
- Emit a public-safe markdown/JSON diagnostic packet with private details redacted by default.
- Include fixture demos for Caddy + Tailscale and Caddy + NetBird.

## Shortlist wedge-first gate

1. **SplitPath** — Self-hosters with Caddy/NPM + Tailscale/NetBird → docs plus `dig`/`curl` and forum threads → tools do not connect DNS, overlay resolver, proxy, and TLS path in one public-safe packet → read-only split-DNS/reverse-proxy diagnostic CLI → r/selfhosted plus Tailscale/NetBird/Caddy search content and support replies → fresh repeated private-hostname confusion across NetBird and Tailscale posts.
2. **PacketLoss Lens** — Self-hosters monitoring links between locations → SmokePing, Uptime Kuma, PingPlotter → incumbents already cover latency/loss well, setup friction is the main pain → maybe a config generator, but monitoring is crowded → r/selfhosted replies/search → fresh post, but weak wedge. Rejected before final scoring.
3. **TinyApp Vault** — Web developers building tiny personal apps → localStorage/IndexedDB, PouchDB, RxDB, Supabase/Firebase/Turso → existing local-first/sync libraries are strong and the use case often tolerates manual export → one-file JSON backup library could be neat but not clearly urgent → webdev content/search → fresh post, but category is crowded and status-quo pain is uneven. Held as idea-only.
4. **InstaHook Packet** — Web developers debugging Instagram Messaging webhooks → Meta docs, webhook.site, ngrok, Pipedream, Hookdeck → platform role/test-user/subscription state is hard to inspect, but many checks need app credentials and current Meta access → public-safe checklist/packet could help but evidence is one thread → webdev/Stack Overflow searches → fresh stuck post. Held as idea-only.
5. **ShopCert Guard** — Shopify operators putting Cloudflare in front of a store → Shopify/Cloudflare docs and generic DNS/SSL checkers → public post says the underlying platform issue was fixed, so the immediate pain may be declining → ACME challenge/path checker could demo well but wedge is narrow → Shopify/Cloudflare SEO → timely change, but kill condition partially triggered. Rejected.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Tailscale DNS / MagicDNS documentation | Strong first-party docs for tailnet names, DNS settings, and split DNS. They do not produce a local, shareable packet covering public DNS, OS resolver behavior, reverse-proxy reachability, and TLS/SNI together. |
| Direct competitor | NetBird DNS management documentation | NetBird documents nameservers, match domains, search domains, and local resolver behavior. It does not diagnose mixed Cloudflare + Caddy/NPM + overlay setups from the user's client. |
| Direct competitor | Caddy / Nginx Proxy Manager docs | Explain reverse proxy behavior, but not whether DNS or overlay routing is sending the client to the intended proxy path. |
| Indirect substitute | Pi-hole, AdGuard Home, dnsmasq, Unbound, `/etc/hosts` | These can implement local DNS fixes, but the user still has to know that DNS is the failing layer. |
| Indirect substitute | `dig`, `nslookup`, `curl`, `openssl s_client`, browser tests | Powerful but fragmented; some OS/browser resolver paths diverge from CLI tools. |
| Status quo | Ask Reddit, copy split-DNS snippets, or expose the service publicly | Wastes time and can create security risk by making private services reachable from the public internet. |

## Wedge

SplitPath is not another DNS server, VPN, reverse proxy, or hosted monitoring tool. It is a read-only diagnostic packet generator for one narrow job: explain why a private hostname resolves/reaches differently across public DNS, local resolver, overlay DNS, reverse proxy, and TLS/SNI. That wedge is small enough for a 1-3 day CLI MVP and concrete enough for repeatable distribution via self-hosted support threads and search pages around "Caddy Tailscale split DNS", "NetBird Caddy private domain", and "Nginx Proxy Manager Tailscale domain resolves".

## Kill condition

Reject or narrow if Tailscale/NetBird first-party CLI tools already provide a comparable public-safe end-to-end packet, or if support-thread validation shows users only need a single documented DNS rewrite rather than repeated diagnostics.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | The workaround can waste hours and wrong fixes can expose private services. Pain is strong in self-hosted support contexts, though not every user hits it weekly. |
| Feasibility | 4/5 | A read-only Python CLI can probe DNS/TCP/TLS/HTTP with fixtures in 1-3 days. Cross-platform resolver behavior is the main edge case. |
| Demo potential | 4/5 | Before/after diagnostic packet is easy to show in terminal, markdown, and a short GIF. |
| Distribution | 4/5 | Specific communities and queries exist: r/selfhosted, Caddy/NPM, Tailscale, NetBird, Cloudflare private-domain troubleshooting. Distribution is reply/search driven, not generic Product Hunt. |
| Competitive wedge / timing | 4/5 | Fresh posts show confusion around NetBird/Tailscale private DNS; first-party docs exist but do not package mixed-stack diagnosis. |
| Total | 20/25 | Clears repo threshold and both gates. |

## Decision

Create the dedicated project repo: https://github.com/halaprix/splitpath

Status is `repo-created`: local scaffold was created, committed, pushed to GitHub, and tagged `v0.1.0-alpha.0`.

Weakest dimension: distribution is solid but still support/search driven rather than built-in sharing.

## Next build step

Implement `splitpath probe` fixture mode with deterministic sample outputs for Caddy + Tailscale and Caddy + NetBird, then add classification-rule tests before touching real network probes.

## Research access note

Reddit JSON was blocked by `HTTP 403 theme-beta`; the run used the reddit-readonly RSS fallback for r/selfhosted and hit `HTTP 429` for several other subreddit feeds. X search was unavailable with `401 Unauthorized`, although `xurl whoami` worked. Web search returned empty for targeted Reddit queries, so competitor validation used fetched first-party docs pages.
