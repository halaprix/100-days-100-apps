# Day 006 — DeskPatch

Date: 2026-06-24
Status: blocked

## One-line pitch

A signed self-service Windows updater for locked-down analyst desktops, starting with Power BI Desktop, so users can apply approved monthly updates without IT storing admin credentials in scripts or touching hundreds of machines.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1ue0u06/installation_automation_for_pbi_wo_admin/ | IT operator has 200+ users, no AD control, blocked Microsoft Store, and recurring Power BI Desktop updates; they considered Python automation but worried about exposing admin credentials. |
| Reddit / r/SaaS | https://www.reddit.com/r/SaaS/comments/1ue524v/best_service_management_software_for_teams/ | Adjacent workflow pain: internal requests scatter across email, Slack, spreadsheets, and meetings until ownership and deadlines are unclear. This reinforces the broader small-team request/update tracking pain. |
| Microsoft Download Center | https://www.microsoft.com/en-us/download/details.aspx?id=58494 | Power BI Desktop is distributed as a large standalone EXE; fetched page showed version `2.155.756.0`, published `6/10/2026`, file `PBIDesktopSetup_x64.exe`, size `644.7 MB`. |
| Microsoft Learn | https://learn.microsoft.com/en-us/power-bi/fundamentals/desktop-latest-update-archive | Microsoft maintains a monthly Power BI Desktop update archive and current-version release cadence; stale Desktop versions can be a real operational drag for analysts. |
| Microsoft Fabric Community / Reddit search | https://community.fabric.microsoft.com/t5/Desktop/Is-local-admin-permission-mandatory-for-installing-Power-BI/td-p/3403331 and https://www.reddit.com/r/PowerBI/comments/jnfwh2/powerbi_desktop_automatic_updates_without_the/ | Public discussions repeat the same constraint: Store is blocked or admin rights are required; Chocolatey/IT deployment helps but still assumes elevated admin flow. |

Research note: Reddit public JSON was blocked by `HTTP 403 theme-beta`; r/SaaS and r/sysadmin posts were collected through the reddit-readonly RSS fallback. Some subreddit RSS calls returned `HTTP 429`, so the run stopped retrying instead of looping. Reddit thread/comment extraction was blocked by the same 403, so only RSS post bodies and public web-search snippets were used. X read auth worked (`whoami`), but X search returned `401 Unauthorized`, so X was not used as evidence.

## Problem

Small IT/helpdesk teams often do not have the clean enterprise deployment story: no Intune/AD control over the relevant devices, Microsoft Store blocked, local admin rights withheld from users, and a monthly desktop app that analysts still need updated. The bad workaround is either manual admin intervention on every workstation or an unsafe script that embeds privileged credentials. That wastes many hours per month and creates a security risk.

The Power BI post is especially sharp because the operator names the scale (`200+ users`), update frequency (`once or twice a month`), and the exact unsafe workaround they want to avoid (storing admin credentials inside a Python application).

## Target user

Small IT teams, MSP operators, and internal helpdesk staff responsible for Windows analyst workstations where:

- Power BI Desktop or similar heavy desktop tools must stay current,
- Microsoft Store / Company Portal / Intune is unavailable or politically blocked,
- users should not receive standing local admin rights,
- the team still needs auditability and an approval trail.

## MVP scope

- A Windows service installed once by an admin as the only trusted elevation point.
- A signed update manifest format: app name, allowed installer hash, version, download URL, silent install command, expiry, and approver.
- A small tray/CLI client that lets a non-admin user request or run only approved updates.
- A local audit log: requester, device, installer hash, version, timestamp, result.
- First built-in recipe: Power BI Desktop standalone EXE update.
- Admin-side manifest generator that fetches the current installer metadata, records SHA-256, and exports a signed JSON manifest.

Non-goals for v0.1: generic remote monitoring, patching every app, storing privileged credentials, bypassing company policy, or replacing Intune/PDQ/Action1 for teams that already have them.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Microsoft Intune / Company Portal | Best answer when the organization controls endpoints and has licensing/admin buy-in. Too heavy or unavailable for the source user's stated constraints. |
| Direct competitor | PDQ Deploy, Action1, ManageEngine Endpoint Central, NinjaOne | Mature endpoint deployment/patch tools. Stronger than a 1-3 day MVP for managed fleets, but overkill when the narrow job is a few approved analyst-tool updates on semi-managed machines. |
| Direct competitor | Admin By Request / Securden / endpoint privilege managers | Proper way to govern admin elevation. Broader and more compliance-oriented; wedge is a tiny allowlisted updater for teams not ready to buy full EPM. |
| Indirect substitute | Chocolatey / winget / PSADT scripts | Useful packaging layer, but still usually needs an elevated execution channel. If implemented by embedding admin creds, it creates the exact risk the source post worries about. |
| Indirect substitute | Manual admin sessions or helpdesk remote control | Works, but burns repeated time and delays analysts every update cycle. |
| Status quo | Users wait for IT or IT ships a risky script | Either slow and expensive at 200+ endpoints, or unsafe because privileged credentials leak into automation. |

## Wedge

**Wedge-first line:** Small IT team updating Power BI Desktop for 200+ locked-down Windows users → Intune/PDQ/Chocolatey/manual admin sessions → unavailable, too broad, or still require elevated execution and credential handling → a single-purpose signed allowlist updater that installs once and only runs approved installer hashes → r/sysadmin, r/PowerBI, MSP communities, and exact SEO queries like “Power BI update without admin rights” → Power BI has fresh monthly releases and locked-down desktops keep colliding with analyst velocity.

DeskPatch should not pretend privilege can be safely created from nothing. The honest wedge is: one-time trusted service install, no stored admin password, only signed manifests and pinned hashes, and a first recipe narrow enough to demo in days.

## Kill condition

Reject or narrow if target users already have Intune, PDQ, Action1, Admin By Request, or another endpoint-management tool deployed and are happy with it. Also reject if the only demanded feature is “run arbitrary installers as admin”; that becomes an unsafe privilege-bypass product, not a narrowly governed updater.

## Shortlist notes

| Candidate | Wedge-first gate result |
|---|---|
| DeskPatch | Winner. Strong pain and scale signal from r/sysadmin; direct competitors are real, but the narrow “Power BI Desktop update without stored admin creds” wedge is specific enough to test. |
| UploadGuard Lite | Node/Express upload validation middleware and test harness for teams relying on Multer MIME checks. Good security pain from r/SaaS and public docs, but crowded with `file-type`, libmagic, blog snippets, and managed upload services; better as a library recipe than a standalone product today. |
| RequestTrace | Lightweight internal-request ownership tracker for small teams drowning in email/Slack/spreadsheets. Rejected/held: Jira Service Management, Freshservice, Desk365, Atomicwork, and countless ITSM tools crowd the category; wedge was not narrow enough. |
| ChangePocket | Tiny change-request approval log for solo sysadmins with one assistant. Useful, but competitor/substitute check shows GitLab issues, Jira, ServiceNow/Freshservice, and ITSM change modules already cover it; distribution is weaker than the Power BI updater niche. |
| DemoFlow | Interactive SaaS demo/pre-call explainer. Rejected by continuity with Day 005: still in the crowded AI demo/video category. |

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 5/5 | Source post names 200+ users, recurring monthly updates, and a security-risk workaround. This clearly passes the status-quo pain test. |
| Feasibility | 3/5 | A safe production updater is non-trivial, but a v0.1 demo can be a signed manifest + Windows service + CLI flow for one installer. |
| Demo potential | 4/5 | Strong before/after: blocked user cannot update Power BI; approved DeskPatch manifest lets them run a pinned installer and produces an audit log. |
| Distribution | 4/5 | Specific communities and search intent exist: r/sysadmin, r/PowerBI, MSP forums, and exact “Power BI without admin / Store blocked” queries. |
| Competitive wedge / timing | 3/5 | Endpoint management is crowded, but the single-app, no-stored-credentials, Power BI-first wedge is sharper than generic patch management. |
| Total | 19/25 | Clears repo-creation threshold and gates. Create a scaffold, but treat security architecture as the first validation task. |

## Decision

Create a dedicated repo scaffold for `deskpatch`. The remote repository exists at https://github.com/halaprix/deskpatch, but pushing the local scaffold was blocked by GitHub `403`, so the project remains blocked until content write access works. This is not a generic patch manager; it is a narrow, auditable self-service updater for locked-down analyst desktops, with Power BI Desktop as the first recipe.

## Next build step

Build a proof-of-safety prototype before UI polish: Windows service accepts only signed manifests, verifies installer SHA-256, runs one Power BI Desktop silent installer command, and writes a tamper-evident audit log. If that cannot be made simple and safe, stop before expanding scope.
