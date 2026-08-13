# Day 053 — SyncBrake

Date: 2026-08-13
Status: repo-created
Repo: [`projects/syncbrake`](../projects/syncbrake)

## One-line pitch

SyncBrake turns Microsoft Entra Connect pending-export deletes plus break-glass readiness facts into a safe preflight packet before a hybrid identity sync mistake locks an organization out.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vn3inw/entra_connect_sync_appears_to_have/ | Fresh sysadmin post reports an Entra Connect sync issue that appears to have deleted/disabled all users including Global Admins, leaving the team unable to open a Microsoft 365 support ticket from the admin center. |
| Microsoft Learn / Prevent accidental deletes | https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-feature-prevent-accidental-deletes | Microsoft documents the accidental-delete threshold, `stopped-deletion-threshold-exceeded`, event ID 116, pending-export delete inspection, and the risk of disabling the threshold. |
| Microsoft Learn / Staging server and disaster recovery | https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-sync-staging-server | Microsoft recommends staging mode to preview configuration changes and inspecting `csexport` / `CSExportAnalyzer` output before exporting changes to Microsoft Entra ID. |
| Microsoft Learn / Emergency access accounts | https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/security-emergency-access | Microsoft says organizations should create two or more cloud-only emergency access accounts to reduce accidental administrative lockout impact. |
| Microsoft Q&A | https://learn.microsoft.com/en-us/answers/questions/1291854/how-can-a-global-admin-regain-access-after-acciden | Public Q&A shows the support/recovery pattern when the only Global Admin is locked out and recommends Azure Data Protection / emergency access preparation. |

## Problem

Hybrid identity admins can stage a seemingly normal Entra Connect configuration change that silently turns into a mass-delete or mass-disable export. Microsoft provides the raw controls: accidental-delete threshold, staging mode, Synchronization Service Manager, `csexport`, and emergency access guidance. The operational gap is packaging those raw facts into a quick, reviewable go/no-go packet before someone disables a threshold, promotes a staging server, changes OU scope, or discovers too late that all break-glass paths are synchronized, blocked, or untested.

The status quo is painful because the failure mode is not just cleanup work. It can lock administrators out of Microsoft 365, interrupt sign-in, block support-ticket creation, and turn a sync change into an emergency escalation.

## Target user

Small and mid-market Microsoft 365 / hybrid identity admins who run Entra Connect or Entra Cloud Sync without a dedicated identity engineering team, especially teams that make occasional OU-filtering, staging-server, or disaster-recovery changes.

## MVP scope

- Accept exported `CSExportAnalyzer` CSV / sanitized pending-export data and a small YAML checklist for tenant safety facts.
- Classify pending deletes/disables by object type, privileged/admin-looking accounts, synced-vs-cloud-only emergency accounts, and threshold risk.
- Generate a deterministic markdown/HTML preflight packet with blast radius, break-glass checklist, safe next steps, rollback questions, and an explicit go/no-go banner.
- Include fixture-only examples; do not connect to Microsoft Graph, production tenants, domain controllers, or Entra Connect servers in the first slice.
- Redact tenant names, UPNs, domains, hostnames, and support-case details by default.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Microsoft Entra Connect accidental-delete threshold | Critical built-in safety control; blocks exports beyond a threshold, but does not create a stakeholder-readable preflight packet or break-glass readiness summary. |
| Direct competitor | Microsoft Entra Connect staging mode + `csexport` / `CSExportAnalyzer` | Supported way to preview export changes. It produces raw CSV/manual inspection workflows, not a concise go/no-go packet. |
| Direct competitor | Microsoft Entra Connect Health | Monitors sync health and alerts, but the MVP wedge is offline pre-change review from exported data and manual readiness facts. |
| Direct competitor | Enterprise Entra backup/recovery suites and consultants | Stronger for mature teams, but heavier than a local-first packet generator for a one-off risky sync change. |
| Indirect substitute | Excel, PowerShell snippets, internal runbooks, screenshots from Synchronization Service Manager | Flexible, but easy to miss admin accounts, cloud-only break-glass coverage, threshold state, or rollback questions under pressure. |
| Status quo | Promote/disable/export after manual spot checks, then escalate to Microsoft if lockout happens | Fast until it fails; a mass identity mistake can block sign-in and admin-center support access. |

## Wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| SyncBrake | Hybrid identity admins before Entra Connect export/staging changes → accidental-delete threshold, staging mode, `CSExportAnalyzer`, Excel, break-glass docs → raw controls exist but do not combine blast radius and emergency-access readiness into a go/no-go artifact → local-first pending-export packet with redaction and break-glass checklist → r/sysadmin/M365/Entra incident and how-to searches, plus reply strategy on lockout/preflight threads → fresh lockout post and Microsoft docs emphasize the exact safety controls | Winner; strong pain, clear CLI demo, specific distribution, and a narrow wedge above raw Microsoft tooling. |
| PrinterBurst | RDS admins seeing Windows Settings enumerate hundreds of print-server printers → GPO printer settings, Event Viewer, print server inventory, scripts → cause spans discovery, AD publishing, shell enumeration, and RDS profile state → read-only RDS printer-enumeration packet → r/sysadmin/RDS searches and printer troubleshooting posts → fresh Windows Server 2022 RDS printer thread | Held: useful but narrower and less obviously repeatable than identity lockout risk. |
| KioskLatch | Small org admins locking Android tablets without paid MDM → app pinning, restricted users, Fully Kiosk, FreeKiosk, Intune if licensed → free native modes are brittle and MDM is overkill for five shared tablets → ADB-driven kiosk hardening checklist generator → r/sysadmin Android tablet/kiosk searches → fresh no-budget Samsung tablet lockdown thread | Held: crowded with kiosk apps and MDM docs; wedge needs device/version proof. |
| BookingGuestTrace | M365 admins testing Personal Bookings external guest access on iOS → Bookings settings, guest/incognito testing, Microsoft support threads → behavior differs by platform/browser and cached account state → reproducible guest-access test matrix packet → Microsoft Q&A and r/sysadmin Bookings searches → fresh iOS guest-prompt mismatch thread | Idea-only candidate; useful support artifact, but likely too docs/debug-matrix focused. |
| AdWasteReceipt | Indie mobile app builders buying TikTok ads → TikTok Ads Manager metrics, App Store Connect, spreadsheets → views/likes/downloads attribution feels fake or opaque → small campaign receipt reconciler → r/SideProject and app-launch posts → fresh “TikTok ad waste” post | Rejected: crowded analytics/attribution category and weak wedge beyond existing dashboards. |

## Wedge

SyncBrake can win by staying deliberately narrower than identity backup suites and more actionable than Microsoft docs. The first slice does not need tenant access: it converts already-exported, sanitized pending-export data plus a small break-glass checklist into a packet that says “stop, review these deletes/admin risks first” or “safe to proceed with these caveats.” That is valuable during a change window because it reduces public embarrassment, downtime, and lockout risk without requiring another SaaS connection to the tenant.

## Kill condition

Reject or narrow if Microsoft Entra Connect Health or the supported `CSExportAnalyzer` workflow already produces a clear blast-radius plus emergency-access go/no-go packet, or if first users say their existing runbook catches privileged-account deletes and break-glass failure modes in under 10 minutes. Also reject any direction that requires live tenant credentials in the MVP; the wedge is local-first safety, not another privileged cloud integration.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 5/5 | The failure can lock admins out, disrupt sign-in, and block support access; status-quo mistakes are high-cost. |
| Feasibility | 4/5 | A CSV/YAML parser plus deterministic packet renderer and redaction checks is buildable in 1–3 days. |
| Demo potential | 4/5 | Clear demo: sample pending-export CSV in, blast-radius/break-glass packet out with stop/go banner. |
| Distribution | 4/5 | Specific channels exist: r/sysadmin hybrid identity threads, M365/Entra search queries, Microsoft Q&A-style problems, and incident-prevention blog posts. |
| Competitive wedge / timing | 4/5 | Microsoft controls are documented but fragmented; fresh lockout evidence and recent docs make a preflight packet timely. |
| Total | 21/25 | Clears repo threshold and both dimension gates. |

## Decision

Create repo. SyncBrake scored 21/25 with distribution 4/5 and competitive wedge/timing 4/5, so it clears the creation gates. Scaffold/spec snapshot was added under `projects/syncbrake`; no dedicated GitHub remote was created during this local-first run.

## Next build step

Implement `syncbrake packet --export fixtures/pending-export.csv --readiness fixtures/readiness.yml --out packet.md` to render a deterministic sample blast-radius and break-glass readiness packet without connecting to Microsoft services.

## Source access caveats

Reddit public JSON was blocked; r/sysadmin and r/SideProject collection used `reddit-rss-fallback`. r/SaaS and r/selfhosted probes hit `HTTP 429`; no Reddit score/comment counts were used because RSS fallback reports them as zero. X/Twitter `auth status` showed no OAuth2 user and `xurl search` returned `401 Unauthorized`, so no X data was used and no social writes were attempted.
