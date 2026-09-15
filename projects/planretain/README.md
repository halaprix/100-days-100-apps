# PlanRetain

A local, read-only export inventory and archive-readiness packet for Project
Online teams before the September 30, 2026 retirement.

## Problem

A Project Online PMO has a short window to preserve projects, custom fields,
resources, workflow dependencies, reports, and related handoff evidence before
retirement. Migration vendors move data, while Microsoft guidance leaves the
choice dependent on each environment's size, customizations, code, add-ons, and
integrations. A late spreadsheet inventory does not show whether the exported
set is complete enough to restore, audit, or hand to a migration partner.

## Target user

A Microsoft 365 PMO administrator or project-operations lead still using Project
Online / Project Web App with custom fields, reporting, integrations, or a mix
of active and historical projects.

## MVP

- Accept only user-supplied Project Online CSV exports and an optional small
  YAML manifest; do not authenticate, call Microsoft APIs, or modify data.
- Inventory projects, tasks, resources, custom-field columns, dates, and
  supplied integration/report references.
- Classify archive coverage as `covered`, `manual-review`, or `not-proven`;
  missing exports are never inferred as safe.
- Emit deterministic Markdown and JSON archive-readiness packets with an
  export/restore test checklist.
- Redact source values and local file paths from reports by default.

## Non-goals

- Not a Project Online-to-Planner/Dataverse migration engine or a replacement
  for an implementation partner.
- Not a credentialed tenant scanner, backup service, or document repository.
- Not an automated proof that a future platform preserves Project Online
  semantics.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Microsoft Learn | https://learn.microsoft.com/en-us/projectonline/project-online | Microsoft marks Project Online for retirement on September 30, 2026. |
| Microsoft Support | https://support.microsoft.com/en-us/project/project-for-the-web-and-project-online | Microsoft says a direct move to the replacement depends on environment complexity, customization, size, add-ons, custom code, and integrations. |
| Microsoft Q&A | https://learn.microsoft.com/en-us/answers/questions/5840689/migrating-from-project-online | A current migration response recommends inventory, a representative pilot, and exporting/archiving before retirement. |
| Project Data migration | https://projectdata.io/migration | A commercial migration tool moves Project Online data/configuration to Dataverse, showing both demand and the stronger migration substitute. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Microsoft guidance and project/migration services | Useful for choosing a target and moving data, but not a local, export-first archive-completeness receipt. |
| Direct competitor | Project Data PDS Migration | An established migration tool; PlanRetain must not compete on transfer automation. |
| Indirect substitute | CSV exports, Excel, SharePoint folders, and a consultant checklist | Teams can make an inventory manually, but repeated export coverage and restore evidence are difficult to maintain. |
| Status quo | Delay inventory until a migration project begins | The deadline turns a missing historical export into a recovery, audit, or delivery risk. |

## Wedge

PlanRetain makes one narrow decision reviewable: whether the exports supplied
for a Project Online environment are enough to preserve the facts needed for a
migration, audit, or historical handoff. It stays local, uses no tenant
credentials, and does not promise a one-click migration. First users can be
reached through exact retirement searches, Microsoft Project community threads,
and PMO/migration-partner content.

## Status

`v0.1.0-alpha.0` — local scaffold and specification only. No remote configured.
