# WinSvcBeacon

A tiny Windows-first bridge that turns selected Windows Service checks into Uptime Kuma push monitors and a shareable status packet.

## Problem

Small Windows-heavy teams often want the simplicity of Uptime Kuma but need to know whether internal Windows services such as IIS, print spoolers, backup agents, database services, or line-of-business daemons are actually running. The common answer is to install a full monitoring stack or hand-roll a PowerShell script plus Task Scheduler job.

That is workable for experienced admins, but it leaves a lot of room for silent misconfiguration: wrong service names, missing scheduled tasks, no uninstall path, no dry-run output, and no packet to hand to a teammate when a service monitor is flaky.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS fallback — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1v2arq7/statusmonitor_for_windows_services/ | Fresh sysadmin request asks for a simple way to monitor whether Windows Services are running, ideally like Uptime Kuma. |
| GitHub search result | https://github.com/jmclaren7/uptime-kuma-push | Existing PowerShell script shows demand for Uptime Kuma push checks from Windows/internal networks, but it is a script primitive rather than a service-discovery workflow. |
| Uptime Kuma public site | https://uptimekuma.co/ | Uptime Kuma is a popular self-hosted monitoring/status tool, validating the chosen integration target. |
| Prometheus windows_exporter | https://github.com/prometheus-community/windows_exporter | Full metrics exporters can monitor Windows services, but require Prometheus-style infrastructure rather than a tiny status-page bridge. |
| Icinga Windows monitoring | https://icinga.com/solutions/windows-monitoring/ | Mature Windows monitoring exists, but it is broader than the lightweight Uptime Kuma use case in the source request. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | PRTG, Icinga, Nagios, Zabbix, Prometheus windows_exporter | Strong mature options for full monitoring. They are heavier than a small Uptime Kuma push bridge for a few Windows Services. |
| Direct competitor | Uptime Kuma plus push-monitor scripts | Uptime Kuma has the status UI and push model; scripts exist, but service discovery, dry-run validation, installer/uninstaller, and packet export are ad hoc. |
| Indirect substitute | PowerShell `Get-Service`, Task Scheduler, email alerts, RMM tools | Works for experienced admins, but repeated manual glue is easy to misconfigure and hard to hand off. |
| Status quo | Ask r/sysadmin, copy a script, or deploy a full monitoring stack | Either wastes admin time for a small need or overfits a large tool to a simple Windows service check. |

## Wedge

WinSvcBeacon is not trying to beat full observability platforms. Its wedge is a narrow bridge for admins who already like Uptime Kuma and only need reliable Windows Service status checks:

- discovers service display names and canonical service names before monitor creation,
- generates Uptime Kuma push URLs and a PowerShell scheduled task from a reviewed config,
- supports dry-run and local status packet output before writing anything,
- keeps setup understandable enough to paste into a support thread or hand to another admin.

## Target user

- Small-company sysadmins with Windows servers and lightweight self-hosted monitoring.
- MSP/helpdesk operators who maintain a few Windows services for clients but do not want to deploy a full metrics stack.
- Homelab and small-office admins already running Uptime Kuma.

## MVP

- `winsvc-beacon scan` prints selected Windows service names from a fixture first, then real PowerShell later.
- `winsvc-beacon plan --config services.yml` validates service names and planned Kuma push monitors.
- `winsvc-beacon emit-powershell` writes a PowerShell script and Task Scheduler registration command.
- `winsvc-beacon packet` exports Markdown with service mapping, schedule, dry-run output, and rollback notes.

## Non-goals

- Not a general Windows metrics exporter.
- Not a replacement for PRTG, Icinga, Nagios, Zabbix, or Prometheus.
- Not storing Uptime Kuma credentials in v0.
- Not auto-remediating or restarting services in v0.

## Status

v0.1.0-alpha.1 — scaffold/spec only; CI smoke check fixed.
