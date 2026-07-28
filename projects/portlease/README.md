# PortLease

Read-only UPnP/NAT-PMP exposure reports for self-hosters who need to know which LAN device opened an internet-facing port before the next NAS scare.

## Problem

Home-lab and small-office users often believe they have no public services exposed because they did not create any manual port forwards. UPnP/NAT-PMP changes that: a LAN device can ask the router to create a temporary or persistent public mapping without the user noticing.

A fresh self-hosted report described a UGREEN NAS exposing HTTP, HTTPS, and SSH through UPnP, followed by port-scan noise and router DoS logs. The owner had Tailscale and local DNS, thought remote access was disabled, and only discovered the exposure after manually correlating Pi-hole, router, and SSH logs.

PortLease is the narrow tool for that moment: enumerate router leases, identify likely owners, flag risky mappings, and export a plain-language incident/evidence packet without changing router settings.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS/web fallback — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1uvy3tu/psa_upnp_and_ugreen_nas/ | Fresh homelab security scare: a NAS apparently opened SSH/HTTP/HTTPS to the internet via UPnP while the owner believed only Tailscale was exposed. |
| Reddit RSS/web fallback — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1uvy3tu/psa_upnp_and_ugreen_nas/ | Comments show repeated advice to disable UPnP and confusion that device-side UPnP is still actively used. |
| OpenWrt Wiki | https://openwrt.org/docs/guide-user/firewall/upnp/upnp_setup?s[]=0 | OpenWrt documents that UPnP lets programs automatically configure port forwarding and carries security risk because mappings can be created without user intervention. |
| MiniUPnP project | https://github.com/miniupnp/miniupnp | Existing low-level tooling can query and manage UPnP IGD mappings, but it is developer/operator oriented rather than a homelab incident report. |
| UpGuard explainer | https://www.upguard.com/blog/what-is-upnp | Public security guidance still treats UPnP exposure as relevant in 2026, not a solved historical issue. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Router admin UI / OpenWrt LuCI UPnP status | Shows mappings on some routers, but varies by vendor and rarely explains owner, risk, or evidence steps. |
| Direct competitor | `miniupnpc`, `upnpc`, NAT-PMP utilities | Powerful low-level tools for querying mappings; not packaged as a safe diagnostic report for non-network specialists. |
| Direct competitor | Fing, router security apps, ISP apps | Often network-inventory oriented, cloud/mobile-heavy, or vendor-specific; not focused on local-first UPnP lease provenance. |
| Indirect substitute | Nmap, external port scanners, GRC ShieldsUP / canyouseeme | Can prove an exposed port, but not which LAN device requested the mapping or when it appeared. |
| Status quo | Disable UPnP after a scare, inspect router logs by hand, ask Reddit | Reactive and error-prone; users often cannot produce a clear before/after report or identify the requesting device. |

## Wedge

PortLease is not a generic vulnerability scanner and does not auto-fix router configuration. It is a read-only UPnP/NAT-PMP lease explainer for self-hosted NAS and homelab owners:

- query discovered Internet Gateway Devices,
- list active mappings with lease duration, protocol, external port, internal host, and description,
- enrich internal hosts with local hints from ARP, mDNS, DHCP exports, and optional user-supplied labels,
- flag risky mappings such as SSH, admin panels, NAS web UI, RDP/VNC, and wildcard long-lived leases,
- generate a Markdown report suitable for a support thread or personal incident log.

The first-user path is concrete: self-hosted and home-networking communities already discuss UPnP scares, UGREEN/NAS remote-access behavior, Tailscale confusion, and router log interpretation.

## Target user

- New or intermediate homelabber running NAS devices, media servers, game servers, Tailscale, or reverse proxies.
- Self-hosters who want a local report before and after disabling UPnP.
- Small MSP/helpdesk operator diagnosing consumer-router exposure for a client without installing a cloud scanner.

## MVP

- Cross-platform CLI, initially Linux/macOS.
- Discover UPnP IGD and NAT-PMP gateways on the LAN.
- Dump active mappings in a table.
- Risk-classify common ports and long-lived mappings.
- Resolve internal IPs to MAC/vendor and optional hostname labels where available.
- Export a Markdown report with evidence, risk flags, and manual next steps.
- Include synthetic sample outputs for demos and tests.

## Non-goals

- No automatic router changes in v0.
- No credentialed router login or scraping vendor admin pages.
- No internet-wide scanning.
- No cloud service, account system, or telemetry.
- No claim that the tool proves compromise or replaces a security assessment.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
