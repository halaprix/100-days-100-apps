# ReportChain

Read-only Microsoft 365 org-mailing-list planner for manager-based distribution lists.

## Problem

Microsoft 365 admins get recurring requests like “email this manager and all direct reports” or “make a distribution list for everyone under this VP.” Native dynamic group and dynamic distribution list workflows are possible in narrow cases, but the exact rule syntax, Exchange distinguished-name requirements, nesting limits, and preview behavior are easy to get wrong.

The painful part is not sending one email. It is safely turning an org chart into a repeatable, auditable group plan without accidentally mailing the wrong people or maintaining static lists by hand.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1v4128g/distribution_list_for_direct_reports/ | Fresh admin request asking for an elegant way to email a boss plus direct reports; dynamic groups did not expose the expected manager property in the UI. |
| Microsoft Graph docs | https://learn.microsoft.com/en-us/graph/api/user-list-directreports?view=graph-rest-1.0 | Graph exposes `directReports`, but the API explicitly returns only direct reports for the selected user, not the whole reporting chain. |
| Microsoft Q&A | https://learn.microsoft.com/en-us/answers/questions/1368556/i-want-to-create-a-dynamic-distribution-group-for | Microsoft moderator says a full VP-to-leaf dynamic distribution group using direct-reports query was not directly possible and suggests nested/manual workarounds. |
| Cayosoft | https://www.cayosoft.com/blog/manager-based-groups-microsoft-365/ | Enterprise product added manager-based Microsoft 365 group rules in 2026, validating demand but targeting a broader admin-suite buyer. |
| ManageEngine | https://www.manageengine.com/microsoft-365-management-reporting/kb/how-to-get-manager-list-in-microsoft-365.html | Documents the manual portal and Graph PowerShell route; portal export is limited and PowerShell is the fallback. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Cayosoft Administrator | Handles manager-based Microsoft 365 groups with hierarchy depth and scheduling, but it is an enterprise admin platform rather than a small read-only planner. |
| Direct competitor | AdminDroid / ManageEngine M365 Manager Plus | Strong reporting suites for managers/direct reports; broader reporting and governance products, not a narrow command-packet generator. |
| Indirect substitute | Microsoft Graph PowerShell + Exchange Online PowerShell | Flexible but error-prone; admins must discover direct-report traversal, ExODS distinguished names, recipient filters, previews, and nested-list strategy themselves. |
| Status quo | Static DLs, cc-ing manager plus a hand-maintained staff list, or ad-hoc scripts | Fast for one request, but drifts when org charts change and creates embarrassing or risky recipient mistakes. |

## Wedge

ReportChain is not another Microsoft 365 reporting suite. It is a small, read-only preflight CLI that turns one manager UPN into a preview packet: direct reports, optional reporting tree, missing-manager warnings, candidate dynamic distribution group commands, and a plain-English explanation of what Microsoft 365 can and cannot automate.

The first wedge is “safe before write”: no tenant mutation by default, synthetic fixtures for demos, and copy/pasteable command packets for admins who are not ready to buy a full suite.

## Target user

Small-company Microsoft 365 admins, MSP technicians, and overloaded sysadmins asked to maintain manager/team distribution lists without a dedicated identity-governance suite.

## MVP

- `reportchain preview --manager <upn> --users users.csv` to compute direct reports and recursive reporting trees from exported or fixture data.
- `reportchain packet --manager <upn>` to emit Exchange Online / Graph PowerShell command packets with preview commands before create/update commands.
- Warnings for missing managers, disabled users, guest users, recursion loops, stale static members, and cases where native dynamic groups cannot express the requested shape.
- Synthetic fixture dataset and deterministic Markdown/JSON output for a screenshot-friendly demo.

## Non-goals

- No tenant writes in v0.1.
- No credential storage.
- No full identity-governance dashboard.
- No replacement for Cayosoft, AdminDroid, ManageEngine, Entra, or Exchange admin centers.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
