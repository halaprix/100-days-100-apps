# Day 026 — PortLease

Date: 2026-07-14
Status: repo-created

## One-line pitch

A read-only UPnP/NAT-PMP exposure reporter for self-hosters who need to know which LAN device silently opened an internet-facing port.

## Source access note

The bundled `reddit-readonly` script was not available in this environment, so I used the documented Reddit RSS/public web fallback path. Reddit RSS worked for r/selfhosted and r/sysadmin but returned `HTTP 429` for several other configured subreddits, so I kept requests small and used web extraction on specific public Reddit permalinks. X/Twitter `whoami` worked, but `xurl search` returned `401 Unauthorized`; no X search evidence was used.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS/web fallback — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1uvy3tu/psa_upnp_and_ugreen_nas/ | Fresh homelab security scare: a UGREEN NAS allegedly opened HTTP, HTTPS, and SSH to the public internet via UPnP while the owner believed only Tailscale was exposed. |
| Reddit RSS/web fallback — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1uvy3tu/psa_upnp_and_ugreen_nas/ | Commenters repeated “disable UPnP” advice, while another commenter noted surprise that device-side UPnP was still actively used. |
| OpenWrt Wiki | https://openwrt.org/docs/guide-user/firewall/upnp/upnp_setup?s[]=0 | OpenWrt documents that UPnP lets programs automatically configure router port forwarding and carries security risk because mappings can be created without user intervention. |
| MiniUPnP project | https://github.com/miniupnp/miniupnp | Existing low-level tools can query/manage UPnP IGD mappings, but they are not packaged as a homelab-friendly owner/risk/evidence report. |
| Reddit RSS/web fallback — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1uw0b9l/us_company_opening_an_eu_office_gdpr/ | Separate strong candidate: US company opening an EU office is overwhelmed by GDPR data-residency mapping; confirms today’s feed had multiple compliance/security pain signals. |
| Reddit RSS/web fallback — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1uvxko7/microsoft_purview_encryption_sensitivity_labels/ | Separate candidate: Purview sensitivity-label encryption breaks automation and partner collaboration when systems are not MIP-aware. |

## Shortlist and wedge-first gate

1. **PortLease** — Read-only UPnP/NAT-PMP lease explainer for self-hosted NAS owners.
   - Specific user → existing substitute → why substitute fails → narrow wedge → distribution path → reason now
   - New/intermediate self-hoster with NAS/Tailscale/reverse proxy → router UI, `upnpc`, nmap, external port scanners, Reddit advice → router UI and raw tools show fragments but not “which device requested what, how risky is it, and what evidence can I share?” → read-only lease inventory plus owner hints, risk flags, and Markdown report → r/selfhosted/r/HomeNetworking support replies plus search content for “UPnP NAS exposed SSH”/UGREEN/Tailscale confusion → fresh UGREEN NAS scare and recurring UPnP security advice.
   - Gate: **passes**. Narrow enough to avoid generic security-scanner territory.

2. **ResidencyMap Sprint** — GDPR data-residency map packet for US companies opening an EU office.
   - Small IT team doing first EU expansion → OneTrust/BigID/Purview, consultants, spreadsheets → enterprise privacy tools are heavyweight and the sysadmin still needs a first-pass system/process/subprocessor map → local questionnaire plus data-flow/ROPA starter packet → r/sysadmin and high-intent GDPR residency search content → fresh r/sysadmin thread says legal wants every EU personal-data system, processing region, backup location, and subprocessor.
   - Gate: passes, but overlaps with recent compliance packet bets (NIS2 EvidencePack, TenantRoute) and sits in a crowded GRC/data-mapping market.

3. **LabelFlow Preflight** — Purview sensitivity-label automation compatibility checker.
   - M365 admin rolling out encrypted labels → Purview docs, SDK examples, manual pilot files → MIP-unaware search/backup/DLP/automation silently breaks when encryption expands → checklist-driven dry-run matrix and service-account permission packet → r/sysadmin/M365 admin content and exact Purview search queries → fresh thread names SDK, super-user rights, guest sharing, and MIP-unaware systems as failure points.
   - Gate: passes as a narrow M365 admin tool, but would need careful Microsoft-doc validation and likely tenant/API access later.

4. **FamilyCache** — Local-only music push/cache coordinator for iPhones.
   - Family leaving Apple Music → Navidrome/Subsonic apps, VLC over SMB, manual downloads → existing apps solve library access but “push to each iPhone only when home” is awkward → LAN-only cache manifest and Shortcut/app handoff → r/selfhosted music-library threads → fresh post asks for exactly this before reinventing with Shortcuts.
   - Gate: rejected for winner; iOS background/download restrictions make the MVP less reliable, and the status quo is tolerable with Navidrome players.

5. **H200Yield** — Profit/risk calculator for accidental H200 owners deciding resell vs rent capacity.
   - Person with high-end GPUs → spreadsheets, eBay, Vast.ai/RunPod/Vultr pricing pages → user has uncertainty on electricity, demand, marketplace risk, and amortization → local ROI model with public pricing assumptions → LocalLLaMA/selfhosted GPU threads → fresh selfhosted post asks whether to resell two H200s or self-host LLM capacity.
   - Gate: rejected for winner; expensive but uncommon scenario, and the wedge is closer to a calculator/content page than a repeatable app bet.

## Problem

Self-hosters often think their attack surface is limited to the ports they manually forwarded. UPnP/NAT-PMP breaks that assumption: any LAN device or app can ask the gateway to create a public port mapping. When something goes wrong, the user has to piece together router logs, Pi-hole/DNS clues, SSH logs, vendor remote-access behavior, Tailscale assumptions, and external scanners.

The painful part is provenance. “Port 22 is open” is not enough. The user needs to know which gateway accepted the lease, which internal host owns it, whether the lease is long-lived, whether the description is trustworthy, whether this is likely a NAS/admin surface, and what evidence to capture before changing settings.

## Target user

- New or intermediate homelabber running NAS devices, media servers, game servers, Tailscale, or reverse proxies.
- Self-hosters who want a local before/after report when disabling UPnP.
- Small MSP/helpdesk operators diagnosing consumer-router exposure without installing a cloud scanner.

## MVP scope

- Cross-platform CLI, initially Linux/macOS.
- Discover UPnP IGD and NAT-PMP gateways on the current LAN.
- Query active mappings without adding, deleting, refreshing, or extending leases.
- Display external port, protocol, internal host/port, description, gateway, and lease duration.
- Enrich internal hosts with safe local hints: ARP/MAC vendor, reverse DNS, mDNS hostname, and optional user labels.
- Risk-classify common exposures: SSH, NAS/admin web UI ports, RDP/VNC, blank descriptions, unknown owners, long-lived leases.
- Export Markdown and JSON reports with synthetic sample data for demos.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Router admin UI / OpenWrt LuCI UPnP status | Useful when present, but vendor-specific and usually not shaped as an incident/evidence report with owner enrichment. |
| Direct competitor | `miniupnpc`, `upnpc`, NAT-PMP utilities | Can query mappings, but output is raw and assumes networking comfort; no homelab-specific risk language or report workflow. |
| Direct competitor | Fing, router security apps, ISP apps | Often cloud/mobile/vendor-specific inventory tools; not a local-first UPnP lease provenance reporter. |
| Indirect substitute | Nmap, GRC ShieldsUP, canyouseeme, external scans | Prove external reachability but do not explain which LAN device requested the mapping. |
| Indirect substitute | Pi-hole/router/SSH log spelunking | Works after the fact for skilled users; slow, manual, and hard to share safely. |
| Status quo | Disable UPnP after a scare and ask Reddit what happened | Reactive; may remove evidence before the owner understands which device opened what. |

## Wedge

PortLease is deliberately narrow: it is not a generic vulnerability scanner and it does not auto-fix router settings. It only answers “what public leases exist, who likely requested them, and how risky do they look?” for self-hosted NAS and home-lab networks.

That wedge matters because existing tools either show raw mappings, scan from outside, or require router/vendor-specific screens. A 1–3 day MVP can win attention by producing a clean, public-safe Markdown report from one command and by being easy to recommend in UPnP/NAS/Tailscale support threads.

## Kill condition

Kill or narrow if live read-only discovery is unreliable across common consumer routers, if `upnpc -l` plus a short tutorial is enough for the target users, or if the product drifts into generic vulnerability scanning/autofix. The product must stay local-first, read-only, and lease-provenance focused.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 5/5 | Silent public exposure creates real security risk and public embarrassment; the workaround is stressful log spelunking after an incident. |
| Feasibility | 4/5 | Protocol/tooling exists, but router diversity and NAT-PMP/PCP coverage need careful fixture/live validation. |
| Demo potential | 5/5 | A synthetic UGREEN-style fixture can produce a clear before/after terminal table and Markdown report. |
| Distribution | 4/5 | Specific communities and queries exist: r/selfhosted, r/HomeNetworking, NAS forums, UPnP/Tailscale/UGREEN support threads. |
| Competitive wedge / timing | 4/5 | Existing tools are low-level or vendor-specific; fresh evidence shows UPnP surprises are still happening in 2026. |
| Total | 22/25 | Strong build candidate; clears repo threshold and both dimension gates. |

## Decision

Create a dedicated repo: `halaprix/portlease`.

Status: repo-created; scaffold pushed and tagged `v0.1.0-alpha.0`.

Weakest dimensions: feasibility, distribution, and competitive wedge/timing are tied at 4/5. The main risk is router compatibility; the MVP should prove one common path first and keep reports honest about uncertainty.

## Next build step

Build the parser/risk engine against synthetic UPnP/NAT-PMP fixtures, then add one live read-only gateway query path and a Markdown report matching the UGREEN-style scenario.
