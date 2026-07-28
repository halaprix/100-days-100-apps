# SplitPath

Read-only split-DNS and private reverse-proxy diagnostics for self-hosters using Caddy or Nginx Proxy Manager with Tailscale, NetBird, or similar overlay networks.

## Problem

Self-hosters often want the same friendly hostnames to work at home and over a private overlay network without exposing services publicly. The failure mode is confusing: public DNS, local resolver rules, MagicDNS or NetBird DNS, Caddy/NPM host matching, TLS, and client OS resolver behavior all interact. The status quo is forum archaeology plus trial-and-error DNS changes that can accidentally expose services or break access for other clients.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1v7qstp/how_to_access_caddy_reverseproxied_services_over/ | A self-hoster with Cloudflare-managed DNS and Caddy wants NetBird access to reverse-proxied services without exposing Docker ports or public services. |
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1v7j4gg/can_i_get_domains_to_resolve_without_hosting_my/ | A self-hoster using Cloudflare, Nginx Proxy Manager, and Tailscale asks whether they must run their own DNS server for domains to resolve privately. |
| Tailscale docs | https://tailscale.com/kb/1054/dns | Tailscale supports split DNS with restricted nameservers, but resolver ordering and OS behavior can be non-obvious. |
| NetBird docs | https://docs.netbird.io/how-to/manage-dns-in-your-network | NetBird has nameservers, match domains, search domains, and a local resolver, creating another config surface for private names. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Tailscale DNS / MagicDNS docs | Strong docs for tailnet names and split DNS, but not a local packet that tests public DNS, OS resolver behavior, overlay DNS, and reverse-proxy reachability together. |
| Direct competitor | NetBird DNS management docs | Covers match domains and custom zones, but does not diagnose a mixed Cloudflare + Caddy/NPM + overlay setup from the user's machine. |
| Indirect substitute | Pi-hole, AdGuard Home, dnsmasq, Unbound, local `/etc/hosts` | Can solve the routing, but require the user to know which resolver path is failing first. |
| Indirect substitute | `dig`, `nslookup`, `curl`, browser tests, forum threads | Powerful but fragmented; macOS and browser behavior can diverge from CLI resolver tools. |
| Status quo | Trial-and-error DNS rewrites or exposing services publicly | Wastes time and can create security risk by pushing private apps onto public DNS/proxy paths. |

## Wedge

SplitPath is not another DNS server, VPN, or reverse proxy. It is a read-only diagnostic CLI that produces a shareable safety packet: what public DNS returns, what the OS resolver returns, what a specified overlay resolver returns, whether the hostname reaches the intended reverse proxy, and which minimal config family likely fixes it. The wedge is narrow enough for a 1-3 day MVP and easy to distribute through self-hosted/Tailscale/NetBird/Caddy troubleshooting searches.

## Target user

Self-hosters and homelab operators who use Caddy or Nginx Proxy Manager with Tailscale, NetBird, WireGuard, or similar overlays, and who want private hostnames to work without public exposure.

## MVP

- `splitpath probe service.example.com --lan-ip <ip> --overlay-dns <ip>` runs read-only DNS and HTTP/TLS checks.
- Compare public DNS, OS resolver output, optional overlay resolver output, and direct reverse-proxy reachability.
- Emit a markdown/JSON diagnostic packet with likely failure class: public-only DNS, missing split DNS, wrong reverse-proxy bind, TLS/SNI mismatch, or client resolver bypass.
- Include fixture-based examples for Caddy + Tailscale and Caddy + NetBird.

## Non-goals

- No automatic firewall, router, DNS, Cloudflare, Tailscale, NetBird, or Caddy mutation in the MVP.
- No credential collection.
- No hosted monitoring service.
- No claim to replace full DNS or VPN documentation.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
