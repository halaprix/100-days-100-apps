# Day 047 — ForestDrill

Date: 2026-08-05
Status: repo-created

## One-line pitch

A read-only Active Directory backup and recovery-drill packet generator for small IT teams that need to test the plan before AD is actually on fire.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vfts7w/comment_on_my_ad_backup_strategy/ | Fresh admin asks how to create and test an AD backup/recovery process across 20+ DCs, whether an AD-joined backup manager is a risk, whether cold tier is acceptable, and which recovery scenarios/accounts to validate. |
| Reddit search fallback — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/18z536u/best_practice_ad_recovery/ | Historical thread shows recurring uncertainty about safest/fastest AD recovery after ransomware-like events. |
| Microsoft Learn | https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-backing-up-system-state | Microsoft documents system-state backups for domain controllers as part of AD forest recovery. |
| Semperis | https://www.semperis.com/active-directory-forest-recovery/ | Enterprise incumbent frames AD recovery as cyber-first disaster recovery with staged, trusted recovery rather than generic server restore. |
| ManageEngine | https://www.manageengine.com/products/active-directory-audit/ad-backup-recovery-software.html | Another incumbent sells AD backup/recovery as part of a broader auditing/recovery platform, confirming the category is painful but tool-heavy. |

## Problem

Small and mid-market sysadmins often have backup components but not a tested Active Directory recovery story. The plan is spread across backup-product capabilities, system-state coverage, cold storage assumptions, undocumented account dependencies, and unanswered tabletop questions. The risky failure mode is discovering during an outage that the backup manager, storage credentials, DSRM password, system-state data, or isolated-network process depends on the same compromised forest.

Status-quo pain passes the threshold: a real recovery drill can consume hours or days, mistakes create security and business-continuity risk, and the public thread shows admins asking for peer review before they trust the plan.

## Target user

- One-person and small-team Windows/sysadmin shops responsible for AD but without a dedicated identity-resilience product.
- MSP engineers reviewing client AD backup plans before a renewal, ransomware tabletop, or insurance questionnaire.
- IT managers who need a concise leadership/vendor packet without exposing private infrastructure details.

## MVP scope

- `forestdrill plan --answers examples/small-org-ad-backup.yaml`.
- Public-safe YAML fixture for DC count band, hypervisor mix, backup methods, backup management trust boundary, storage tiers, recovery-account categories, and drill scenarios.
- Deterministic rules for system-state coverage, AD-joined backup manager risk, cold-tier recovery-time risk, isolated-network drill gaps, and account-verification gaps.
- Markdown packet export plus JSON summary for tests.
- Synthetic examples only; no AD, Azure, backup-console, credential-store, or network access in v0.

## Shortlist screened before winner

| Candidate | Wedge-first gate | Gate result |
|---|---|---|
| ForestDrill | Small-team AD admins → vendor backup consoles + Microsoft docs + spreadsheets → substitutes do not produce a public-safe tabletop packet or expose backup-plane trust gaps quickly → read-only fixture-to-drill-packet CLI → r/sysadmin/MSP/search content around AD backup recovery → fresh AD backup strategy thread plus ransomware/forest-recovery timing | Winner; gates pass. |
| LinkReceipt | Solo launch founders submitting to startup directories → Ahrefs/Semrush/Screaming Frog plus manual page fetches → generic SEO crawlers require setup and exact competitors like Backlynk/ShipDR already focus on directory backlinks → narrow receipt for live/nofollow/noindex/unpublished status → r/SideProject launch posts and directory-list audiences → fresh post manually checking 34 listings | Rejected for today: direct competitors are too close; wedge needs proof beyond “simpler.” |
| PrintGhost | M365 Universal Print admins → Universal Print portal, Microsoft troubleshooting docs, printer vendor dashboards → cloud status can become stale and native device status may disagree → read-only stale-status reconciliation packet → r/sysadmin and Universal Print search threads → fresh stale waste-toner warning post | Idea-only: useful but narrower source base and distribution likely 3/5. |
| LabelFatigue | M365 security admins rolling out DLP/sensitivity labels → Microsoft Purview, DLP suites, consultants → users over-classify or default-tag when the taxonomy is high-friction → label-fatigue preflight questionnaire/report → r/sysadmin/security admins → fresh DLP fatigue thread | Rejected: crowded DLP/GRC category; wedge is too soft without telemetry or interviews. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Semperis Active Directory Forest Recovery | Strong enterprise platform for automated, malware-aware AD recovery; much more than a lightweight preflight and likely procurement-heavy for small teams. |
| Direct competitor | Quest Recovery Manager for Active Directory / Forest Edition | Mature AD recovery tooling for real restore workflows; not positioned as a fixture-driven plan review for teams already using mixed backup tools. |
| Direct competitor | ManageEngine ADAudit Plus AD backup and recovery | Covers AD backup/recovery operations inside a broader auditing product; not a public-safe tabletop packet generator. |
| Indirect substitute | Microsoft Learn, backup-vendor runbooks, spreadsheets, consultant tabletop notes | Authoritative but fragmented; admins still reconcile system-state coverage, backup-manager trust, cold-tier timing, account access, and isolated-network tests manually. |
| Status quo | Ask peers, read docs, export screenshots, and test whichever restore path seems obvious | Can waste hours per drill and leaves catastrophic gaps until an incident proves the plan wrong. |

## Wedge-first gate

Small-team AD/sysadmin owner → enterprise AD recovery suites, backup-console docs, Microsoft Learn, spreadsheets → substitutes either require procurement/live tooling or remain fragmented and do not expose backup-plane trust gaps in one artifact → fixture-driven, read-only AD recovery drill packet that maps a mixed backup plan to gaps, account checks, and isolated-network scenarios → r/sysadmin/MSP/search content around “AD backup recovery strategy” and “forest recovery test” → fresh thread asks exactly these recovery-plan questions while ransomware/identity-resilience pressure keeps AD recovery timely.

## Wedge

ForestDrill deliberately avoids being a recovery platform. It wins on a lower trust bar and faster setup: a sysadmin can enter public-safe facts in 30 minutes and get a drill packet without installing an agent, granting domain permissions, connecting to a backup console, or buying a cyber-recovery suite.

The wedge is narrow enough for a 1–3 day MVP: turn messy AD backup strategy questions into a deterministic markdown packet covering system-state coverage, backup-platform blast radius, storage-tier restore risk, recovery accounts, isolated-network tests, and vendor questions.

## Kill condition

Reject or narrow if early sysadmin/MSP reviewers say one of these is true:

- their existing backup/recovery product already emits an equivalent tabletop packet without live credentials;
- the packet does not surface a gap they would discuss in a recovery drill;
- users will not enter even synthetic/public-safe backup-plan facts;
- the first requested feature is live AD/backup-console integration before the fixture-driven packet proves useful.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 5/5 | AD recovery failure creates business-continuity and security risk; fresh and historical sysadmin threads show repeated uncertainty. |
| Feasibility | 4/5 | A deterministic YAML-to-markdown CLI is straightforward; the hard part is careful rule wording and public-safety boundaries. |
| Demo potential | 4/5 | A synthetic before/after recovery drill packet is easy to screenshot, though less visually flashy than UI-heavy products. |
| Distribution | 4/5 | Specific communities and search paths exist: r/sysadmin, MSP audiences, AD backup/forest recovery queries, and recovery tabletop content. |
| Competitive wedge / timing | 3/5 | Strong incumbents exist, but they are recovery platforms; the narrow read-only readiness-packet wedge remains credible. |
| Total | 20/25 | Clears repo threshold and both gates. |

## Decision

Create the repo scaffold and consolidate the public-safe snapshot into the master index at [`projects/forestdrill`](../projects/forestdrill).

No dedicated GitHub remote was created for the project during this run; the scaffold/spec snapshot is tracked in the master index repo. Status is `repo-created` because the local project repo and canonical snapshot exist.

Weakest dimension: competitive wedge / timing at 3/5, because Semperis, Quest, ManageEngine, and backup vendors already occupy adjacent recovery territory.

## Next build step

Implement the first runnable CLI slice: parse `examples/small-org-ad-backup.yaml`, evaluate five deterministic checks, and write `forestdrill-packet.md` plus `forestdrill-summary.json`.

## Research access note

Reddit JSON was blocked by `HTTP 403 theme-beta`; the run used the reddit-readonly RSS fallback for r/sysadmin/r/SideProject and `web_search`/`web_extract` for competitor and documentation validation. X search was unavailable with `401 Unauthorized`; no X write actions were attempted.
