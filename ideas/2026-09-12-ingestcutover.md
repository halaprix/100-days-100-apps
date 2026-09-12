# Day 078 — IngestCutover

Date: 2026-09-12
Status: idea-only

## One-line pitch

A local, redaction-first CLI that turns an Azure Monitor HTTP Data Collector API inventory into a DCR/Logs Ingestion cutover packet before the legacy API loses support.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Microsoft Learn — migration guide | [Migrate from the HTTP Data Collector API](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/custom-logs-migrate) | Support for the legacy API ends on September 14, 2026; migration adds DCR/DCE, RBAC, and schema decisions.[1] |
| Microsoft Q&A — operator question | [Retirement notice: transition to DCR-based custom log ingestion](https://learn.microsoft.com/en-us/answers/questions/2129487/retirement-notice-transition-to-dcr-based-custom-l) | An operator asks what must be done and whether the transition needs downtime; the answer recommends identifying resources and parallel validation.[2] |
| Microsoft Learn — ingestion tutorial | [Send data with the Logs Ingestion API](https://learn.microsoft.com/en-us/azure/azure-monitor/logs/tutorial-logs-ingestion-portal) | The replacement flow requires an Entra authentication scheme plus a DCR and, in the portal flow, a DCE.[3] |
| Closest automation substitute | [AzLogDcrIngestPS](https://github.com/KnudsenMorten/AzLogDcrIngestPS) | A maintained PowerShell module already automates DCR/ingestion setup and includes migration material; a new tool must stay strictly on preflight and evidence.[4] |

## Problem

Azure teams that still send custom logs through the HTTP Data Collector API face a support deadline in two days.[1] The replacement is not a URL swap: it introduces identity/RBAC, DCR/DCE choices, custom-table migration, and schema-change behavior.[3] Microsoft explicitly notes that the legacy API used to adapt classic-table schemas automatically whereas the Logs Ingestion API does not.[1]

The tolerable-looking workaround is to read the migration guide, click through each workspace, and collect screenshots before a manual parallel test. That becomes a launch/incident risk when one unlisted classic table, missing role, region mismatch, or unmodelled source field makes the new path reject data. The public Q&A question is historical (December 2024), so it is used for problem language rather than a claim of current community volume.[2]

## Target user

The Azure administrator or platform engineer who owns one to twenty Log Analytics workspaces with custom-log senders and needs a reviewable change packet before the September 14 support cutoff.[1]

## MVP scope

A local CLI that accepts sanitized Azure CLI table-list JSON and optional exported DCR/template JSON. Microsoft documents `Classic` table subtype as the discovery signal for Data Collector API tables; the CLI would treat that as an input fact, not discover a tenant on its own.[1] It:

1. identifies `Classic` custom tables and groups them by workspace;
2. checks a declarative input for DCR, endpoint/region, identity, RBAC, and destination-table coverage;
3. flags schema fields that need an explicit migration decision;
4. emits a redacted Markdown/JSON packet with an inventory, missing prerequisites, parallel-validation plan, rollback note, and copyable read-only Azure CLI queries.

It does not authenticate to Azure, create resources, submit logs, retain exports, or claim that a migration is safe.

## Shortlist and wedge-first gate

| Candidate | Wedge-first line | Competitor / substitute gate | Result |
|---|---|---|---|
| **IngestCutover** | Azure Monitor custom-log owner → Microsoft docs, Portal, ARM/Bicep, and AzLogDcrIngestPS → they configure the target but do not produce one redacted, inventory-to-validation review packet → offline classic-table/DCR/schema preflight → Azure Monitor migration queries, Microsoft Q&A/Stack Overflow answers, and GitHub Action/template search → legacy API support ends September 14, 2026 | Closest direct substitute is AzLogDcrIngestPS; indirect substitutes are the portal, IaC, and consultants. The status quo is a manual inventory and parallel test. Narrowing to evidence, not deployment, leaves a credible gap. | **Advance** — score below. |
| **CopilotPolicySwitch** | Copilot org admin → Copilot policy settings and GitHub’s deprecation notice → native settings already show alternatives and enablement → policy-to-integration impact report → GitHub Community/Copilot admin searches → October 2 model retirements | GitHub’s native admin settings are already the control point, and no source showed a separate repeatable integration-inventory pain. | **Reject before scoring** — native substitute too strong. |
| **StreamArchive Relay** | Twitch creator → manual VOD download/upload or Restream → existing tools already schedule, store, and distribute video → Twitch-only archive receipt → creator communities → no platform deadline | Restream and the fresh SideProject post’s Upcastor cover the same workflow. A “Twitch to YouTube” wedge is not enough. | **Reject before scoring** — crowded, no narrow advantage. |
| **DeskBluetooth Rule** | Mac desk worker → manual Bluetooth control, blueutil, or native automation → existing tools already control paired devices → dock-identity restore policy → Mac automation communities → no timely trigger | The fresh Uncordex project already implements the exact saved-desk reconnect behavior. | **Reject before scoring** — direct implementation already exists. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | [AzLogDcrIngestPS](https://github.com/KnudsenMorten/AzLogDcrIngestPS) | Automates Log Ingestion API/DCR work and has migration resources. It is not evidence-only, so IngestCutover must not compete as a generic deployment wrapper.[4] |
| Direct competitor | Microsoft migration guide and Azure portal | The official route covers how to migrate; it includes discovery commands and setup instructions.[1][3] |
| Indirect substitute | ARM/Bicep/Terraform, bespoke PowerShell, or an Azure consultant | Can build the target resources but leaves each team to prove its original inventory, schema decisions, and validation plan. |
| Status quo | Spreadsheet plus portal screenshots and a manual dual-ingestion test | It can work, but it is slow to review and easy to leave incomplete under a near-term support deadline. |

## Wedge

The wedge is not “automate Azure migration.” It is a no-credential, input-only **review packet** for one specific transition: classic custom tables and HTTP Data Collector API senders to DCR-based ingestion.[1] The demonstration is concrete: drop in sanitized inventory exports, receive a missing-prerequisites matrix and parallel-test checklist. This avoids competing with infrastructure-as-code or a mature ingestion module such as AzLogDcrIngestPS.[4]

## Kill condition

Reject or narrow the bet if a targeted search finds an actively maintained tool that already accepts classic-table/DCR inventory and emits an equivalent preflight packet, or if Azure operators say their existing IaC plan plus Microsoft’s discovery query takes under 30 minutes per workspace. Also reject if the only usable input requires broad tenant credentials or telemetry uploads.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | A missed custom-log transition can blind monitoring or delay a change; the September 14 support deadline makes the work urgent.[1] |
| Feasibility | 4/5 | An input-only CLI can parse fixture exports and generate deterministic Markdown in 1–3 days. Live tenant discovery is deliberately out of scope. |
| Demo potential | 4/5 | A before/after packet with classic tables, missing DCR/RBAC rows, and a parallel-test plan is legible in a short terminal recording. |
| Distribution | 3/5 | Azure Monitor migration searches and existing Q&A/community threads name the audience, but this run did not validate a repeatable owned channel or an active cluster of fresh requests. |
| Competitive wedge / timing | 3/5 | The September 14 support deadline is real and the evidence-packet boundary is sharper than a generic migrator, but Microsoft guidance and AzLogDcrIngestPS are meaningful substitutes. |
| Total | 18/25 | Clears the numeric threshold but fails the Distribution gate (minimum 4/5). |

## Decision

**Idea-only.** Do not create a dedicated repo: the 18/25 total clears the threshold, but Distribution is 3/5, below the required 4/5. The immediate timing is useful, yet the narrow preflight wedge needs proof from active Azure operators before a scaffold is justified.

## Next build step

Run five targeted, read-only searches across Azure Monitor Q&A, Stack Overflow, and GitHub for classic custom-table/DCR migration incidents; create a repo only if they surface recurring packet/review pain not solved by existing IaC or AzLogDcrIngestPS.

## Source access caveats

Reddit’s public JSON endpoint returned HTTP 403 and the `r/SideProject` RSS fallback returned fresh posts; its relevant stream/archive and Bluetooth posts were used only to reject shortlist candidates, not as evidence for IngestCutover. Subsequent `r/sysadmin` and `r/selfhosted` RSS probes returned HTTP 429, so they were not retried. X authentication status showed no OAuth 2 token for the default app, and the read-only search returned HTTP 401. This winner therefore relies on fetchable Microsoft documentation, Microsoft Q&A, and an open GitHub repository; it does not claim Reddit or X validation.

## Sources

[1] https://learn.microsoft.com/en-us/azure/azure-monitor/logs/custom-logs-migrate — Microsoft Learn: migrate the HTTP Data Collector API
[2] https://learn.microsoft.com/en-us/answers/questions/2129487/retirement-notice-transition-to-dcr-based-custom-l — Microsoft Q&A: DCR ingestion transition question
[3] https://learn.microsoft.com/en-us/azure/azure-monitor/logs/tutorial-logs-ingestion-portal — Microsoft Learn: Logs ingestion API tutorial
[4] https://github.com/KnudsenMorten/AzLogDcrIngestPS — AzLogDcrIngestPS repository
