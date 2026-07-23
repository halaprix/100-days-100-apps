# Day 034 — ReportChain

Date: 2026-07-23
Status: repo-created

## One-line pitch

Read-only Microsoft 365 CLI that turns a manager UPN into a safe direct-report / reporting-tree distribution-list preview packet before admins touch Exchange or Entra.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1v4128g/distribution_list_for_direct_reports/ | Fresh admin asked for an elegant way to email a boss plus direct reports; the expected `user.manager` dynamic group property was not available in their UI path, leading to Power Automate / manual-list uncertainty. |
| Microsoft Graph docs | https://learn.microsoft.com/en-us/graph/api/user-list-directreports?view=graph-rest-1.0 | Graph exposes `directReports`, but the docs state it does not return the direct-report chain beyond the specified user. |
| Microsoft Q&A | https://learn.microsoft.com/en-us/answers/questions/1368556/i-want-to-create-a-dynamic-distribution-group-for | Microsoft moderator said a VP-to-leaf dynamic distribution group using a direct-reports query was not directly possible and suggested nested dynamic groups plus a root DL. |
| Microsoft Q&A | https://learn.microsoft.com/en-us/answers/questions/1337169/dynamic-dl-based-on-org-hierarchy | Another admin hit manager-filter / distinguished-name confusion and solved it only after using the mailbox distinguished name. |
| Cayosoft | https://www.cayosoft.com/blog/manager-based-groups-microsoft-365/ | Enterprise admin suite added manager-based Microsoft 365 group rules in 2026, validating that the workflow is common and still operationally annoying. |
| ManageEngine | https://www.manageengine.com/microsoft-365-management-reporting/kb/how-to-get-manager-list-in-microsoft-365.html | Documents the portal and Graph PowerShell path, including the limitation that the Entra admin center does not export all managers in one operation. |

## Problem

Microsoft 365 org charts are useful for communication, rollout targeting, and delegated administration, but native group tooling is split across Entra, Exchange Online, Graph, and PowerShell. A request that sounds simple — “make a list for this manager’s team” — becomes a brittle decision tree:

- direct reports vs full reporting tree,
- Entra dynamic group rule vs Exchange dynamic distribution group recipient filter,
- Exchange distinguished names vs user principal names,
- preview behavior vs actual created group behavior,
- static nested DLs when native dynamic rules cannot express the shape.

The status quo burns admin time and can create public embarrassment or operational risk if stale lists email the wrong people.

## Target user

Small-company Microsoft 365 admins, MSP technicians, and sysadmins who receive manager/team distribution-list requests but do not have a full identity-governance suite.

## MVP scope

- `reportchain preview --manager <upn> --users users.csv` computes direct reports and optional recursive reporting trees from exported or synthetic data.
- `reportchain packet --manager <upn>` emits Markdown/JSON with membership preview, assumptions, warnings, and copy/pasteable Exchange Online / Graph PowerShell command packets.
- Warn on missing manager attributes, disabled users, guest users, recursion loops, stale static members, and unsupported native dynamic-group shapes.
- Ship with synthetic fixtures only, so the demo needs no tenant credentials.

## Shortlist and wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| ReportChain | Microsoft 365 admins/MSPs → Entra/Exchange UI, Graph PowerShell, static DLs, Cayosoft/AdminDroid/ManageEngine → native paths are split, confusing, and broad suites are heavy → read-only CLI packet for manager-based DL decisions before tenant writes → r/sysadmin/M365/PowerShell content and reply strategy around direct-report DL errors → fresh Reddit request plus 2026 enterprise-suite feature validates timing | Pass; scored as winner. |
| Local ID Scan PDF PWA | People asked for scanned ID copies → Adobe Scan, CamScanner, iLovePDF, OS scanner apps → uploads/privacy and physical-size layout friction → browser-local ID-to-PDF with exact card sizing → privacy/local-first SEO and SideProject demo → fresh SideProject build signal | Rejected as daily winner: useful, but crowded scanner/PDF category and distribution is mostly generic SEO. |
| React Router transition testbed | React Router app developers → Framer Motion, View Transitions API, custom route state → route transitions are hard to coordinate and regress visually → fixture-driven transition lifecycle playground for React Router → React Router/animation docs examples and package users → fresh Routeveil SideProject signal | Rejected: dev-tool niche is real but evidence is a maker launch, not a repeated pain thread. |
| Direct-report Power Automate recipe generator | M365 admins → Power Automate, Graph scripts, static lists → automations are hard to permission and maintain → generated flow recipe from manager UPN → M365 admin blog/search path → Reddit request mentioned Power Automate | Narrowed into ReportChain; standalone flow generator is too brittle and likely requires live tenant/write permissions too early. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Cayosoft Administrator | Strong enterprise competitor: supports manager-based groups, hierarchy depth, scoping, and scheduling. Too broad/heavy for a small admin who wants a safe preflight packet. |
| Direct competitor | AdminDroid / ManageEngine M365 Manager Plus | Mature M365 reporting/admin tools with manager/direct-report reports. They validate demand but focus on dashboards/reporting suites rather than a tiny read-only command planner. |
| Native competitor | Microsoft Entra dynamic groups and Exchange Online dynamic distribution groups | Native and cheap when the exact rule is expressible, but the UI/rule syntax/recipient-filter/DN path is confusing and fragmented. |
| Indirect substitute | Graph PowerShell, Exchange Online PowerShell, CSV exports, custom scripts | Flexible and free, but every admin has to rediscover traversal, filtering, preview, and command safety. |
| Status quo | Static distribution lists, nested DLs, cc manager plus staff DL, manual updates | Works for one-off messages but drifts as reporting lines change and can send to the wrong audience. |

## Wedge

ReportChain wins only if it stays narrower than the suites: no dashboard, no governance platform, no default tenant writes. The MVP is a read-only “packet generator” that explains the native option, previews membership from exported data, flags risky org-chart gaps, and emits commands an admin can manually review.

That wedge gives it a plausible 1–3 day MVP: synthetic fixtures, deterministic graph traversal, Markdown/JSON output, and command templates. The first-user path is concrete: answer direct-report DL questions in r/sysadmin / M365 admin communities with a reproducible preview packet and a fixture demo, not a sales page.

## Kill condition

Reject or narrow if Microsoft’s current Entra dynamic direct-report rules plus Exchange dynamic distribution groups can fully handle most manager/team DL requests in the UI without DN/PowerShell confusion, or if admins say a full suite is already mandatory because scheduling/writes/audit are the real buying criteria.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Repeated admin pain; wrong recipient lists are embarrassing and operationally risky. |
| Feasibility | 4/5 | CSV-first traversal and packet generation are straightforward; live Graph and Exchange edge cases should wait. |
| Demo potential | 4/5 | Synthetic org chart → preview tree → warnings → generated command packet is screenshot/GIF-friendly. |
| Distribution | 4/5 | Specific communities and search queries exist: r/sysadmin, M365 admin blogs, PowerShell examples, direct-report DL threads. |
| Competitive wedge / timing | 3/5 | Enterprise competitors are real, but the narrow read-only packet wedge and fresh 2026 product activity keep it viable. |
| Total | 19/25 | Clears repo threshold and dimension gates. |

## Decision

Create the repo. ReportChain clears 18/25 with Distribution 4/5 and Competitive wedge/timing 3/5. Status is `repo-created` because the scaffold was pushed and tagged.

Repo: https://github.com/halaprix/reportchain

## Next build step

Implement `reportchain preview --manager <upn> --users fixtures/users.csv` with synthetic fixture data, recursive tree traversal, cycle detection, disabled/guest warnings, and Markdown output.

## Research access note

Reddit public JSON was blocked; the r/sysadmin evidence came through the `reddit-rss-fallback` layer. Reddit comments fetch for the fresh thread returned HTTP 403, so the brief relies on the RSS snippet plus web-search/documentation validation. X search returned 401 Unauthorized, so X was not used beyond auth probing.
