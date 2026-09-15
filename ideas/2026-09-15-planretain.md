# Day 081 — PlanRetain

Date: 2026-09-15
Status: repo-created

## One-line pitch

A local, read-only CLI that turns explicit Project Online exports into an
archive-readiness packet before the September 30, 2026 retirement.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Microsoft Learn — Project Online admin documentation | [Project Online Admin Documentation](https://learn.microsoft.com/en-us/projectonline/project-online) | Microsoft flags Project Online for retirement on September 30, 2026.[1] |
| Microsoft Support — product comparison | [Project for the web and Project Online](https://support.microsoft.com/en-us/project/project-for-the-web-and-project-online) | Microsoft says whether a direct move is appropriate depends on an environment's complexity, customizations, size, add-ons, custom code, and integrations.[2] |
| Microsoft Q&A — current migration discussion | [Migrating from Project Online](https://learn.microsoft.com/en-us/answers/questions/5840689/migrating-from-project-online) | The guidance recommends an inventory, representative pilot, and export/archive work before retirement.[3] |
| Microsoft Tech Community | [Data access after Project Online (PWA) retirement](https://techcommunity.microsoft.com/discussions/project/data-access-after-project-online-pwa-retirement/4465629) | A current community discussion highlights uncertainty around access to Project and related SharePoint content after the cutoff.[4] |
| Direct migration substitute | [Project Data PDS Migration](https://projectdata.io/migration) | A commercial migration product moves Project Online data and configuration into Dataverse, proving both demand and a stronger transfer substitute.[5] |

## Problem

A Project Online PMO has only days left to preserve projects, task structures,
resource assignments, custom fields, reports, workflow references, and
migration evidence. Microsoft makes clear that a direct move depends on the
actual environment rather than a one-size-fits-all path. A late Excel inventory
can list files, but it does not state whether the supplied exports cover the
facts needed for a future migration, audit, or historical handoff.

The status quo clears the pain test: a missing or untested historical export can
block a migration decision, weaken an audit/recovery response, or create
expensive consultant rework after the service deadline. The tool is not for a
PMO that has already completed a tested archival and migration program.

## Target user

A Microsoft 365 PMO administrator or project-operations lead still using Project
Online / Project Web App with custom fields, reporting, integrations, or a mix
of active and historical projects.

## MVP scope

- Read only explicit Project Online CSV exports and an optional small YAML
  manifest; never authenticate, call a Microsoft API, or change input files.
- Inventory projects, tasks, resources, assignments, custom-field columns,
  time ranges, and user-supplied integration/report references.
- Classify categories as `covered`, `manual-review`, or `not-proven`; absent
  exports and unknown mappings never become safe by inference.
- Emit deterministic Markdown and JSON packets with a compact export/restore
  test matrix.
- Redact source values and local file paths from reports by default.

## Shortlist and wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| **PlanRetain — selected** | Project Online PMO lead facing retirement → Microsoft guidance, CSV/Excel inventories, migration firms, and PDS Migration → these select/move platforms but do not produce a credential-free receipt that explicit exports cover archive categories and still need a restore test → local export-first archive-readiness packet → exact retirement searches, Microsoft Project community threads, and PMO/migration-partner content → September 30 retirement is imminent. | Pass: time-bounded, >30-minute and audit/migration-risk workflow, concrete channel. |
| **ABM Handoff Packet — rejected** | M&A IT admin with two Apple Business Manager tenants → Apple support, MDM vendor runbooks, spreadsheets, and manual re-enrollment → an inventory could organize a difficult transfer → local cross-tenant device handoff packet → Apple admin/M&A communities → fresh r/sysadmin question reports manual movement → only one fresh report, accessible Apple documentation did not establish a stable technical boundary, and MDM/migration partners may already own the process. | Reject: one source and unproven wedge. |
| **Entra Lifecycle Gap — rejected** | Hybrid-identity admin → Entra Connect, Graph/PowerShell, and account-lifecycle tools → separate AD/Entra expiry policy can leave a confusing sign-in gap → account-state comparison packet → r/sysadmin and M365 admin searches → fresh r/sysadmin reminder → this overlaps the lab's earlier SyncBrake hybrid-identity preflight and needs stronger distinct evidence. | Reject: duplicate territory. |
| **Windows Update Evidence Pack — rejected** | Offline-network Windows administrator → Settings update history, WSUS/SCCM reports, screenshots, and spreadsheets → evidence is incomplete after a UI change → update-history receipt → Windows administration communities → fresh r/sysadmin report → PatchProof already occupies patch-compliance evidence in this lab. | Reject: duplicate territory. |
| **Self-hosted Code Review Agent — rejected** | Forgejo/GitLab maintainer → Proval, hosted review agents, local LLMs, and manual review → generic review automation lacks a unique workflow → self-hosted reviewer → SideProject/dev communities → fresh SideProject launch → crowded code-review/AI-agent category and launch evidence does not prove a new wedge. | Reject: crowded category, no distinct channel. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Microsoft Project Online retirement/migration guidance | Authoritative for the date and replacement choices, but it does not generate an environment-specific, export-coverage receipt.[1][2] |
| Direct competitor | Project Data PDS Migration and migration consultancies | Stronger products/services for moving data and configuration. PlanRetain deliberately does not compete on transfer automation.[5] |
| Indirect substitute | CSV exports, Excel, SharePoint folders, and consultant checklists | Can inventory an estate, but cross-file coverage and restore evidence are rebuilt manually and drift. |
| Status quo | Delay export inventory until a target-platform migration begins | Defers discovery of missing historical data, custom fields, reports, and integration references into the deadline window. |

## Wedge

PlanRetain is not a migration wizard, project-management replacement, or backup
platform. It makes one narrow question reviewable: *do the explicit exports in
hand cover the categories needed to preserve this Project Online environment,
and what still needs a restore test?* The credentials-free, local-first report
has lower trust and procurement friction than tenant-wide migration tooling.

Its concrete first-user path is retirement-specific search content, Microsoft
Project Community / Q&A discussions, and material used by PMO migration partners
when they ask a customer for an inventory. The deadline provides the reason now;
the output is valuable before a team has selected a target platform.

## Kill condition

Stop or narrow PlanRetain if five Project Online PMO/migration practitioners can
assemble a reliable archive-coverage and restore receipt in under 15 minutes
from normal exports, or if an established migration provider offers a free,
equivalent export-first archive-readiness packet. Also stop if useful coverage
requires live tenant credentials rather than the explicit exports.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Retirement creates a real delivery, audit, and historical-record risk for customized PMOs; the affected niche is bounded. |
| Feasibility | 5/5 | A conservative, explicit-input CSV/YAML inventory and deterministic report are a 1–3 day local CLI slice. |
| Demo potential | 5/5 | A mixed fixture set becoming a red/yellow/green archive packet and restore matrix is immediately legible. |
| Distribution | 4/5 | Exact retirement searches, Microsoft Project community/Q&A threads, and PMO/migration-partner inventory content are specific repeatable channels. |
| Competitive wedge / timing | 3/5 | The September 30 deadline is hard and close; migration vendors are strong, so the wedge is deliberately confined to pre-migration archive evidence. |
| Total | 21/25 | Clears the repository threshold and both dimension gates. |

## Decision

**repo-created.** PlanRetain scores **21/25**, with Distribution at **4/5** and
Competitive wedge/timing at **3/5**. A local dedicated scaffold and public-safe
snapshot were created at [`projects/planretain`](../projects/planretain). No
dedicated GitHub remote was created or claimed.

## Next build step

Create synthetic CSV/YAML fixtures for projects, tasks, resources, custom fields,
and missing categories; implement the conservative `covered` / `manual-review` /
`not-proven` coverage report without accepting tenant credentials.

## Source access caveats

Reddit's public JSON endpoint returned the documented `403` theme-beta response
for r/SideProject and r/sysadmin. The read-only tool used the public RSS fallback
and retrieved fresh posts from both. r/SaaS, r/selfhosted, and r/webdev then
returned `429` at both JSON/RSS layers and were not retried. The fresh r/sysadmin
posts informed rejected alternatives only; this selected Project Online bet is
validated by public Microsoft/product sources rather than a claimed Reddit
consensus.

The `xurl` identity probe succeeded, but the default profile had no OAuth2 token
and the read-only search probe returned `401 Unauthorized`; no X signal is used.
Some Microsoft Support/Apple pages returned unavailable or incomplete content to
the extractor, so the brief relies only on the public Microsoft Learn/Q&A/Tech
Community pages and a public competitor page cited above.

## Sources

[1] https://learn.microsoft.com/en-us/projectonline/project-online

[2] https://support.microsoft.com/en-us/project/project-for-the-web-and-project-online

[3] https://learn.microsoft.com/en-us/answers/questions/5840689/migrating-from-project-online

[4] https://techcommunity.microsoft.com/discussions/project/data-access-after-project-online-pwa-retirement/4465629

[5] https://projectdata.io/migration
