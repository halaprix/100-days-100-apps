# DeskPatch

A signed self-service Windows updater for locked-down analyst desktops, starting with Power BI Desktop.

## Problem

Small IT teams sometimes lack a clean endpoint-management path: no Intune/AD control, blocked Microsoft Store, users without local admin rights, and analyst desktop tools that still need frequent updates. The bad choices are manual admin sessions across many machines or scripts that embed privileged credentials.

DeskPatch exists to test a narrower pattern: one trusted local service, signed update manifests, pinned installer hashes, and auditable non-admin update requests.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1ue0u06/installation_automation_for_pbi_wo_admin/ | IT operator has 200+ users, no AD control, blocked Store, recurring Power BI updates, and concern about exposing admin credentials in automation. |
| Microsoft Download Center | https://www.microsoft.com/en-us/download/details.aspx?id=58494 | Power BI Desktop is distributed as a large standalone EXE; fetched page showed version `2.155.756.0`, published `6/10/2026`, file `PBIDesktopSetup_x64.exe`, size `644.7 MB`. |
| Microsoft Learn | https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-latest-update-archive | Microsoft maintains monthly Power BI Desktop update history and current release cadence. |
| Public Power BI discussions | https://www.reddit.com/r/PowerBI/comments/jnfwh2/powerbi_desktop_automatic_updates_without_the/ | Users discuss updating Power BI without Microsoft Store; Chocolatey can help but still needs elevated execution. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Microsoft Intune / Company Portal | Best answer for managed fleets, but unavailable to the source user. |
| Direct competitor | PDQ Deploy, Action1, ManageEngine Endpoint Central, NinjaOne | Mature deployment/patch tools; much broader than the Power BI-first wedge. |
| Direct competitor | Admin By Request / endpoint privilege managers | Proper broad privilege governance; DeskPatch starts as a smaller allowlisted updater. |
| Indirect substitute | Chocolatey / winget / PSADT scripts | Packaging helps, but an elevated execution channel is still required. |
| Status quo | Manual admin sessions or unsafe scripts | Slow at 200+ endpoints or risky if credentials are embedded. |

## Wedge

DeskPatch is not a generic patch manager and not a way to run arbitrary installers as admin. The wedge is a deliberately small, auditable updater for a short list of approved analyst tools, starting with Power BI Desktop.

The core trust boundary is simple:

1. An admin installs a local Windows service once.
2. Admins publish signed manifests with installer URL, version, hash, silent command, expiry, and approver.
3. Non-admin users can run only approved manifests whose signatures and hashes verify.
4. Every action is logged locally for audit.

## Target user

Small IT teams, MSP operators, and helpdesk staff responsible for Windows analyst workstations where endpoint management is absent, blocked, or too heavy for the immediate job.

## MVP

- Windows service skeleton that exposes one local update endpoint.
- Signed JSON update manifest format.
- SHA-256 installer verification before execution.
- CLI/tray proof-of-concept for requesting an approved update.
- Power BI Desktop recipe with metadata fields for current installer version and silent command.
- Local audit log for request, approval manifest, result, and installer hash.

## Non-goals

- No stored admin passwords.
- No arbitrary command execution.
- No generic remote monitoring in v0.1.
- No replacement for Intune/PDQ/Admin By Request where those are already deployed.
- No policy bypass: an admin must install the trusted service and approve manifests.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
