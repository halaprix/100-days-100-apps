# ForestDrill

A read-only Active Directory backup and recovery-drill packet generator for small IT teams that need to test the plan before AD is actually on fire.

## Problem

Small and mid-market sysadmins know Active Directory recovery is critical, but the plan often lives across backup-console screenshots, vendor docs, cold-storage guesses, and unanswered questions like: is the backup platform joined to the same AD, do we have system-state coverage, which account still works in an isolated forest drill, and what exactly should be tested?

ForestDrill turns a public-safe questionnaire and optional CSV fixtures into a recovery drill packet: coverage gaps, blast-radius risks, isolated-network test scenarios, account-verification checklist, storage-tier caveats, and open questions for the next tabletop.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vfts7w/comment_on_my_ad_backup_strategy/ | Fresh admin post asks how to create and test an AD backup/recovery process across 20+ DCs, whether an AD-joined backup manager is a risk, whether cold tier is acceptable, and which recovery scenarios/accounts to validate. |
| Reddit search fallback — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/18z536u/best_practice_ad_recovery/ | Historical thread shows recurring uncertainty about safest/fastest AD recovery after ransomware-like events. |
| Microsoft Learn | https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/forest-recovery-guide/ad-forest-recovery-backing-up-system-state | Microsoft documents system-state backups for domain controllers as part of AD forest recovery. |
| Semperis | https://www.semperis.com/active-directory-forest-recovery/ | Enterprise incumbent positions AD recovery as a cyber-resilience problem with staged, trusted recovery rather than generic server restore. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Semperis Active Directory Forest Recovery | Strong enterprise platform for automated, malware-aware AD recovery; overkill for teams that first need a public-safe drill packet before a purchase or tabletop. |
| Direct competitor | Quest Recovery Manager for Active Directory / Forest Edition | Mature AD recovery tooling focused on real restore workflows; not a lightweight preflight for documenting gaps in an existing mixed backup plan. |
| Direct competitor | ManageEngine ADAudit Plus AD backup and recovery | Handles AD backup/recovery operations inside a broader auditing product; not focused on offline plan review for small teams using Dell, Veeam, Azure Blob, scripts, or mixed tooling. |
| Indirect substitute | Microsoft Learn, vendor runbooks, spreadsheets, consultant tabletop notes | Authoritative but fragmented; admins still reconcile backup manager trust, system-state coverage, cold-tier restore timing, account credentials, and isolated-network tests manually. |
| Status quo | Ask r/sysadmin, read docs, export backup-console screenshots, then test whatever seems obvious | Wastes hours per drill and can leave catastrophic gaps until an incident proves the plan was wrong. |

## Wedge

ForestDrill is not an AD recovery product. It is a 30-minute readiness packet for teams that already have backup tools but do not yet have a testable recovery story:

- fixture-driven and read-only in v0;
- no domain credentials, tenant IDs, backup-console secrets, or live environment access;
- not connecting to Active Directory, Azure, or backup consoles in v0;
- maps public Microsoft recovery concepts into a concrete drill checklist;
- highlights backup blast-radius risks such as AD-joined backup management;
- outputs markdown/JSON that can be used in a change advisory, tabletop, or vendor call.

## Target user

- One-person and small-team Windows/sysadmin shops responsible for AD but without a dedicated identity-resilience product.
- MSP engineers reviewing client AD backup plans before a renewal, ransomware tabletop, or insurance questionnaire.
- IT managers who need a concise artifact for leadership without exposing private infrastructure details.

## MVP

- `forestdrill plan --answers examples/small-org-ad-backup.yaml`.
- YAML fixture schema for domain-controller count, backup methods, management-plane trust, storage tiers, recovery accounts, and drill scenarios.
- Deterministic rule engine for system-state coverage, backup-console blast radius, cold-tier restore risk, isolated-network tests, and account-validation gaps.
- Markdown packet export plus JSON summary for tests.

## Non-goals

- Not connecting to Active Directory, Azure, Dell Avamar, Veeam, or any backup console in v0.
- Not performing backups or restores.
- Not guaranteeing recoverability or replacing vendor support.
- Not storing real domain names, hostnames, tenant IDs, IPs, account names, or screenshots.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
