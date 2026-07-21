# Day 032 — WinSvcBeacon

Date: 2026-07-21
Status: repo-created

## One-line pitch

A tiny Windows-first bridge that turns selected Windows Service checks into Uptime Kuma push monitors and a redacted handoff packet.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS fallback — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1v2arq7/statusmonitor_for_windows_services/ | Fresh post asks for a simple way to monitor whether Windows Services are running, ideally like Uptime Kuma. |
| Reddit RSS fallback — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1v2axmg/hpe_nimble_cannot_enable_multiprotocol_iscsi_on/ | Adjacent fresh sysadmin signal: infrastructure admins are blocked by vendor-specific state and need safe preflight diagnostics before changes. |
| Reddit RSS fallback — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1v28b72/recommendations_for_file_sharing/ | Adjacent self-hosted operations signal: users avoid exposing sensitive apps and ask for safer, narrower operational bridges instead of bigger platforms. |
| GitHub search result | https://github.com/jmclaren7/uptime-kuma-push | Existing PowerShell push script shows demand for Windows/internal-network checks with Uptime Kuma, but not a complete service-discovery and packet workflow. |
| Uptime Kuma public site | https://uptimekuma.co/ | Validates the chosen status-page/monitoring target: a popular self-hosted monitoring tool rather than a new dashboard. |
| Prometheus windows_exporter | https://github.com/prometheus-community/windows_exporter | Mature Windows service metrics exist, but require a Prometheus-style monitoring stack rather than a tiny Uptime Kuma bridge. |
| Icinga Windows monitoring | https://icinga.com/solutions/windows-monitoring/ | Mature Windows monitoring also exists in Icinga; the opportunity must stay narrower and lighter. |

Source access notes: Reddit public JSON endpoints returned `HTTP 403 theme-beta`; the reddit-readonly script used public RSS fallback where available. Some subreddit RSS feeds returned `HTTP 429`, so no retry loop was used. Reddit thread/comment fetches returned 403 and were not used. X `whoami` worked for read access, but X search returned `401 Unauthorized`, so X search was not used as evidence. Competitor validation used public web search results and product/docs pages.

## Shortlist and wedge gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| WinSvcBeacon | Windows-heavy small-team sysadmins already using or considering Uptime Kuma → full monitoring stacks, Uptime Kuma push scripts, PowerShell plus Task Scheduler → full stacks are too heavy and scripts lack service discovery, dry-run validation, uninstall notes, and redacted handoff output → fixture-first CLI that generates a reviewed Windows Service check plan, PowerShell push script, scheduled-task command, and Markdown packet → r/sysadmin, r/UptimeKuma, GitHub/search content for "Uptime Kuma Windows service monitor" and support-thread reply strategy → fresh r/sysadmin request asks for exactly simple Windows Service monitoring in an Uptime Kuma shape. | Winner; clears repo threshold as a narrow bridge, not a generic monitoring dashboard. |
| NimbleCutoverGuard | Storage admins migrating HPE Nimble/Alletra with Hyper-V/SCVMM history → HPE docs/support, Microsoft VMM docs, vendor tickets, manual CLI/PowerShell checks → substitutes are authoritative but do not provide a quick offline preflight from pasted sanitized outputs → parser for Nimble/SCVMM SMI-S dependency evidence before enabling iSCSI multiprotocol → r/sysadmin, HPE/SCVMM search queries, consultant handoff packets → fresh post shows a real blocked migration. | Held/rejected for today: strong pain, but too vendor-specific and MVP depends on proprietary command output examples. |
| PaperlessShareBridge | Paperless-ngx self-hosters who keep the app VPN-only → ProjectSend, Nextcloud, SFTPGo, presigned object storage, temporary reverse proxy exposure → substitutes work but require duplicating files or exposing more surface than desired → local helper that stages explicit expiring outbound shares from selected documents without exposing Paperless itself → r/selfhosted/Paperless content and privacy-oriented file-sharing searches → fresh post asks how to share files while keeping Paperless private. | Rejected for today: direct substitutes are strong and the safe integration boundary needs more validation. |
| HybridSOC2Packet | On-prem/hybrid sysadmins facing SOC 2 → Vanta, Drata, auditors, spreadsheets, screenshots → compliance tools skew cloud-first, but evidence capture is procedural and crowded → offline evidence packet checklist for physical/environmental/on-prem completeness → r/sysadmin, SOC 2/on-prem search, MSP/auditor content → fresh post says cloud-first tools ignore hybrid/on-prem evidence. | Rejected: useful but overlaps prior NIS2 EvidencePack and crowded compliance tooling. |
| LaunchGapReview | Indie product builders before launch → QA consultants, Playwright tests, privacy scanners, manual reviews → automated tests miss copy/privacy/build/version issues → checklist-runner for launch review packets → r/SideProject and indie launch content → fresh post lists failures found in indie launches. | Rejected: crowded launch/security review category and distribution would be generic. |

## Problem

The source request is deliberately small: "I want a simple way to monitor if Windows Services are running, like Uptime Kuma." That is a real operations gap for teams that do not want a full monitoring platform just to know whether IIS, a backup agent, print spooler, database service, or line-of-business daemon is running.

The current workaround is either too big or too fragile:

- deploy PRTG/Icinga/Nagios/Zabbix/Prometheus for a handful of service checks,
- copy a PowerShell push script without discovery, dry-run, or uninstall notes,
- use Task Scheduler and hope the right service names, intervals, and secrets were wired correctly,
- ask Reddit again when the monitor goes stale or a teammate inherits it.

The status-quo pain is enough because misconfigured service monitoring creates false confidence, can hide downtime, and wastes recurring admin time when scripts are copied host-by-host without a standard handoff packet.

## Target user

- Small-company sysadmins with Windows servers and lightweight self-hosted monitoring.
- MSP/helpdesk operators who maintain a few Windows services for clients but do not want to deploy a full metrics stack.
- Homelab and small-office admins already running Uptime Kuma.

## MVP scope

- Python CLI with fixture-backed demo first: `winsvc-beacon plan --fixture examples/windows-services.json --config services.yml`.
- `services.yml` maps Windows service names to expected states and Uptime Kuma push URL environment variable names.
- Dry-run planner that flags missing services, display-name/name mismatches, stopped services, and redacted push URL handling.
- `emit-powershell` command that generates an auditable PowerShell script and Task Scheduler registration command.
- `packet` command that exports Markdown with service mapping, schedule, dry-run results, redacted push URL placeholders, and rollback/uninstall notes.
- No credential storage, remote host control, service restart/remediation, or generic metrics dashboard in v0.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | PRTG, Icinga, Nagios, Zabbix, Prometheus windows_exporter | Mature and more complete for Windows monitoring. Overkill when the user wants Uptime Kuma-shaped checks for a few Windows Services. |
| Direct competitor | Uptime Kuma plus existing push-monitor scripts | Uptime Kuma supplies the status UI and push pattern; scripts show demand but leave discovery, validation, install/uninstall, and handoff as manual glue. |
| Indirect substitute | PowerShell `Get-Service`, Task Scheduler, RMM tools, email alerts | Experienced admins can build the pieces. The failure mode is fragile copied glue with no dry-run packet or teammate handoff. |
| Status quo | Ask r/sysadmin, copy a script, or deploy a full monitoring stack | Wastes setup time and can create false confidence if service names, schedules, or push URLs are wrong. |

## Wedge

WinSvcBeacon can still work because it refuses to become another monitoring dashboard. It is a narrow bridge for one job: make selected Windows Services visible in Uptime Kuma safely and repeatably.

Why the wedge is credible:

- it targets admins already choosing lightweight Uptime Kuma rather than selling a new status UI,
- it turns ad-hoc PowerShell into a reviewed plan, generated script, scheduled-task command, and rollback notes,
- dry-run and fixture mode make the demo public-safe and easy to understand,
- redacted Markdown packets are naturally shareable in support threads and handoffs,
- distribution can be focused on exact search/support phrases instead of generic launch channels.

## Kill condition

Kill or narrow if Uptime Kuma ships first-party Windows Service monitors with service discovery, installer/uninstaller, scheduled execution, push-secret handling, dry-run validation, and packet-style handoff output. Also kill any scope that turns into a generic metrics dashboard, stores real push URLs, or auto-remediates/restarts services before the read-only bridge proves value.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Service monitoring avoids silent downtime and false confidence; pain is concrete but not always urgent for every small team. |
| Feasibility | 5/5 | A fixture-first Python CLI plus generated PowerShell and Markdown packet is buildable in 1–3 days. |
| Demo potential | 4/5 | A demo can show healthy/stopped/missing services, redacted push URLs, and generated Task Scheduler instructions in one terminal recording. |
| Distribution | 4/5 | Specific channels and queries exist: r/sysadmin, r/UptimeKuma, GitHub searches, and support-thread replies for "monitor Windows Services with Uptime Kuma". |
| Competitive wedge / timing | 3/5 | Existing monitoring tools are strong, so the wedge must stay narrow: Uptime Kuma bridge, dry-run validation, and handoff packet. |
| Total | 20/25 | Clears repo threshold and both dimension gates. |

## Decision

Create `halaprix/winsvc-beacon` as a dedicated project repo: https://github.com/halaprix/winsvc-beacon. The idea scores 20/25, Distribution is 4/5, and Competitive wedge/timing is 3/5. Repo status is `repo-created`: scaffold pushed to GitHub and tagged `v0.1.0-alpha.1` after fixing the scaffold CI smoke check.

## Next build step

Implement fixture-backed `winsvc-beacon plan` and `winsvc-beacon packet` commands with one healthy service, one stopped service, one missing service, and redacted Uptime Kuma push URL placeholders.
