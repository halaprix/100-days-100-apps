# Day 088 — RestoreCover

Date: 2026-10-24
Status: idea-only

## One-line pitch

A local-first rehearsal app that checks whether a named substitute operator can follow an existing backup-restore runbook without coaching from the sole backup administrator, and exports the blockers before that administrator goes on leave.

## Research brief

- **Decision:** retain one narrow software hypothesis or create a project only if the scoring and dimension gates pass.
- **Target customer:** a small infrastructure team where one person operates backups and another already-authorized technician provides leave coverage.
- **Geography:** English-speaking IT teams; no jurisdiction-specific compliance claims.
- **Substitutes:** native backup verification, recovery orchestration, Hudu processes, and an ordinary runbook plus a timed second-person exercise.
- **Horizon:** a 1–3 day prototype, only after baseline validation.
- **Must-answer question:** does a dedicated rehearsal interface reveal handoff blockers materially faster than an existing process template?
- **Evidence bar:** fetched public reports and original vendor documentation; no inferred willingness to pay, invented interviews, or market-size estimates.
- **Creative constraint:** automate the annoying thing, not the backup engine. Make the handoff test reproducible rather than building another monitoring dashboard.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Fresh public community thread, discovered through RSS and read through HTML extraction | [Backup/recovery admins, October 23](https://www.reddit.com/r/sysadmin/comments/1xdtamz/any_other_backuprecovery_admins_here/) | The author asks about inadequate recovery resources and clarifies that the backup team is effectively one person. This supports operational concentration risk, not demand for this particular app. |
| First-person public comment in the same thread | [Sole Commvault operator](https://www.reddit.com/r/sysadmin/comments/1xdtamz/comment/19rk1py1vyvls/) | A commenter reports responsibility for 1,100 VMs, recovery testing mainly during actual production restores, and SLAs slipping when away or assigned to other projects. These are self-reported claims, not independently measured results. |
| Public counterexample in the same thread | [Delegate recovery procedures](https://www.reddit.com/r/sysadmin/comments/1xdtamz/comment/19rk17rcj1s3l/) | Another operator says a well-run process can be managed by one person and recommends role-based delegation. This is negative evidence against a generic staffing app and motivates testing the substitute operator instead. |
| Original vendor documentation | [Veeam recovery verification report](https://helpcenter.veeam.com/docs/one/userguide/surebackup_jobs_overview.html?ver=13) | Native reporting already records successful, warning, failed, and never-run verification, including test details. A green-job dashboard or basic verification report is not a wedge. |
| Original vendor documentation | [Hudu Processes](https://support.hudu.com/hc/en-us/articles/9143382484759-Processes) | Reusable templates, separate runs, assignments, status, and technician step notes already exist. A checklist clone is not a wedge. |
| Original vendor documentation | [Cutover runbook examples](https://cutover.com/blog/runbook-examples-it-disaster-recovery-cloud-migration-and-technology-implementation) | Recovery runbooks already include prerequisites, permissions, owners, completion confirmation, audit trails, and ongoing review. Recovery orchestration is not an empty category. |

**Evidence strength:** repeated concentration/verification pain within one fresh discussion, plus strong substitute documentation. Multiple comments in one thread are not independent customer discovery. There is no payment, pilot, or recurring adoption evidence. The uncoached-handoff product is our hypothesis, not a tool request made by the source author.

## Shortlist and wedge-first gate

These checks precede the winner's scoring. Rejected ideas receive no numerical score; easy implementation cannot rescue a failed gate.

### 1. RestoreCover — narrowed and retained for validation

**Specific user → existing substitute → why substitute fails → narrow wedge → distribution path → reason now**

Sole backup operator arranging leave coverage → Hudu process run or existing recovery runbook plus native verification → technical verification does not by itself demonstrate that the substitute operator can locate the procedure, obtain already-approved access, and interpret the result without coaching; whether existing runbook tooling makes this awkward remains unproven → a no-integration, two-role rehearsal with explicit blocked steps and coaching-needed events → a worked leave-coverage exercise for backup operators, searchable around backup-admin handover, offered through relevant vendor/community discussions only with approval → fresh reports of SLA slippage during absence, not a new deadline or regulatory change.

- **Direct competitors:** [Cutover](https://cutover.com/blog/runbook-examples-it-disaster-recovery-cloud-migration-and-technology-implementation), plus native recovery-runbook capabilities such as [Commvault AD forest recovery](https://documentation.commvault.com/saas/runbooks_for_active_directory_forest_recovery.html). The Commvault document is workload-specific; do not generalize it to every restore operation.
- **Indirect substitutes:** Hudu process runs; an existing wiki procedure, ticket, and stopwatch.
- **Status quo/pain:** contact the sole specialist during leave or accept delayed recovery. The fresh SLA report passes the incident-risk test, but does not quantify weekly handoff work.
- **Gate result:** retain only the small second-operator exercise. Reject a general DR platform, staffing dashboard, or new runbook repository. First-user access remains unverified, so Distribution cannot reach 4/5.
- **Kill condition:** a Hudu template or ordinary runbook records the same useful blockers with equal or lower setup and review time.

### 2. BackupScopeDiff — rejected before scoring

**Specific user → existing substitute → why substitute fails → narrow wedge → distribution path → reason now**

Backup operator reviewing environment changes → native protected-workload reports and Bocada asset auditing → alleged missing inventory comparison is contradicted by fetched documentation → no defensible generic CSV-reconciliation wedge → backup-coverage search content reaches the audience but not an unmet job → the thread author's report of backups breaking after change supplies urgency, not differentiation.

- **Direct competitors:** [Veeam Protected VMs](https://helpcenter.veeam.com/docs/one/userguide/protected_vms.html?ver=13) identifies missing/outdated restore points; [Bocada Asset Protection](https://www.bocada.com/product/asset-protection/) joins inventory, including CSV, against backup activity and distributes owner-specific reports.
- **Indirect substitute:** spreadsheet join or native export/script.
- **Status quo:** run the existing report and correct exclusions; broken protection is serious, but already addressed by these substitutes.
- **Kill condition triggered:** the proposed differentiating comparison is explicitly sold already. Offline operation alone does not prove a painful gap.

### 3. StockReturnReplay — rejected before scoring

**Specific user → existing substitute → why substitute fails → narrow wedge → distribution path → reason now**

Small warehouse team replacing an Airtable workflow → paid inventory app or internal-tool platform → custom software reportedly double-counted returns → hypothetical returns replay fixture → internal-tool implementers would be a specific audience, but no repeatable access or recurring test-maintenance pain was established → one fresh build-versus-buy account, not proof of demand for a new tester.

- **Signal:** [The startup internal tool trap](https://www.reddit.com/r/sysadmin/comments/1xe23nu/the_startup_internal_tool_trap/), fetched in full after RSS discovery.
- **Direct substitute:** [Jet Admin](https://www.jetadmin.io/), which the author has chosen to try on top of Airtable. Its own page advertises apps on existing data and governance. It is not evidence that inventory correctness is automatically solved.
- **Indirect substitutes:** keep the working paid inventory system; write ordinary integration tests; reconcile sample returns manually.
- **Status quo:** the previous company returned to paid software. Do not interpret that satisfactory retreat as willingness to buy another layer.
- **Kill condition triggered:** no validated recurring replay-test problem or first-user channel; the post's substantial product recommendation also makes it weak independent demand evidence. Reject an all-in-one inventory replacement and the speculative fixture package.

### 4. ChangeContextLink — rejected before scoring

**Specific user → existing substitute → why substitute fails → narrow wedge → distribution path → reason now**

Windows operations and security teams investigating account-deletion alerts → change ticket and security incident context → thread reports context disputes, but does not establish a missing integration → a change-to-alert annotation would duplicate existing workflow infrastructure unless a specific mapping failure is proven → enterprise security integrations require access and trust not available here → fresh team friction, not a platform shift.

- **Signal:** [Security-team context dispute](https://www.reddit.com/r/sysadmin/comments/1xdsriq/incompetent_security_teams_make_the_job_a_drag/). The author says a standard change existed; comments dispute the framing. Do not claim undocumented changes or security incompetence as established root cause.
- **Direct/adjacent competitor:** [ServiceNow Microsoft Sentinel integration](https://store.servicenow.com/store/app/8feeab2e1b646a50a85b16db234bcb2c), search-result evidence only, advertises incident synchronization and alert/entity context. This is adjacent evidence, not proof it maps approved changes automatically. The documentation URL returned only a loading shell.
- **Indirect substitutes:** link the approved change ticket, preserve host/account scope, and share context with the analyst.
- **Status quo:** manual cross-reference; real interruption risk, but no measured repetitive workflow or narrow integration gap was established.
- **Kill condition triggered:** unclear incremental value, privileged integrations, and no concrete first-user access. No alert suppression or automatic dismissal belongs in this idea.

## Problem

Backup availability, tested recoverability, and a substitute person's ability to execute a recovery are different facts. A team can have a documented procedure and still depend on one person's interpretation or access knowledge. The fresh discussion supports this single-person dependency as a risk; it does not prove that new software beats a well-run rehearsal.

The product must not promise to fix staffing, storage capacity, missing backups, or recovery infrastructure. It would only make one handoff exercise easier to run and review.

## Target user

A small infrastructure team with an existing backup product, an existing restore procedure, and an already-designated substitute technician. Start with one non-production file-restore scenario, not a forest recovery or enterprise cyber-recovery plan. Exclude teams that already run adequate second-operator exercises in Hudu or Cutover.

## MVP scope

A local browser app with a small local persistence layer and explicit JSON export:

1. Import a deliberately small exercise definition: scenario, pseudonymous roles, ordered steps, access prerequisites, safe test destination, acceptance checks, and stop conditions.
2. Offer a substitute-operator view that records `not-started`, `blocked`, `completed`, and `coaching-needed`; require an explanation for a blocker rather than silently treating a checkbox as proof.
3. Record operator-entered exercise timestamps and evidence references, including when the primary operator intervened. These are attestations, not independently verified execution telemetry.
4. Export a review showing unresolved access/runbook gaps, coaching events, and which acceptance checks were actually observed. Preserve interrupted exercises as incomplete.
5. Keep `tabletop`, `access-check`, and `test-restore` modes separate. A tabletop pass must never be labeled a successful restore, demonstrated RTO, or compliance certification.

**Non-goals and safety:** no production agents, backup API credentials, password/key storage, automated role grants, scripts, restore commands, backup deletion, or automatic remediation. Store references to approved secret-management procedures, not secret values. Actual restores remain outside the app and need the team's own authorization, isolated target, and cleanup procedure. Local reports may still contain sensitive operational metadata; exclude them from public repositories and inspect exports before sharing.

**Feasibility boundary:** a small manual rehearsal recorder is plausible in 1–3 days. Reliable vendor integrations, execution validation, and a security-assured recovery platform are not.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Cutover collaborative recovery runbooks | Already supports human tasks, prerequisites, owners, completion checks, and audit history. Do not claim these as novel features. |
| Native adjacent substitute | Commvault AD forest recovery runbooks | Already combines automated recovery/configuration tasks and manual validation steps. This workload-specific capability raises the comparison bar rather than proving universal coverage. |
| Indirect substitute | Hudu Processes and Process Runs | Templates, assignments, statuses, and step notes can likely host the exercise. This is the primary small-team baseline to beat. |
| Technical verification substitute | Veeam SureBackup and Recovery Verification Overview | Tests and reports backup recoverability; use it for its actual job, rather than replace it with human checkboxes. It does not itself establish an uncoached staff handoff. |
| Status quo | Existing wiki procedure, approved access, ticket notes, and a stopwatch | Cheap and potentially sufficient. If it works well, publish an exercise template instead of an app. |

No current price comparison was verified. There is no basis for a cheaper-than-incumbent pricing claim or market-size claim.

## Wedge

The only retained hypothesis is **lower-friction, local, uncoached substitute-operator rehearsal around an existing procedure**, not better backup monitoring or unique checklist mechanics. A useful demo would expose a blocked access prerequisite while native technical verification remains green.

That contrast illustrates two different questions; it is not proof the app adds value over Hudu or Cutover. The comparison gap remains unvalidated, so competitive wedge/timing scores below the repo-creation gate. No urgent regulatory clock was found.

## Kill condition

Reject the app and keep only a reusable exercise template if any of these holds:

- Two baseline exercises using an ordinary runbook or Hudu capture the same consequential blockers with equal or lower combined setup/review time.
- Three relevant operators report that current delegation and rehearsal practices already work well, or that the real blocker is staffing/authority the app cannot change.
- Reviewers need stored credentials, privileged integrations, or production automation before the recorder is useful.
- The design confuses attestation with execution proof, or a tabletop result with demonstrated recovery.

To justify a build, require a repeatable baseline comparison, at least one independently participating team with a real handoff need, and a concrete repeatable way to reach similar teams. These criteria are proposed validation gates, not completed research.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Absence-related SLA slippage and concentrated recovery knowledge create incident risk; frequency and demand for a new recorder remain unknown. |
| Feasibility | 4/5 | A constrained local manual exercise is small; trustworthy integrations and execution proof are explicitly excluded. |
| Demo potential | 4/5 | One green technical verification beside a substitute operator's blocked step makes the distinction visible. No demo was built in this run. |
| Distribution | 3/5 | Specific backup-operator communities exist and a handover exercise is useful content, but no repeatable access or adoption path is validated. |
| Competitive wedge / timing | 2/5 | Hudu, Cutover, and native runbooks are strong substitutes. Local rehearsal packaging is a testable hypothesis, not a demonstrated gap. |
| Total | 17/25 | Below 18/25; both Distribution and wedge gates also fail. |

## Decision

**Idea-only; no dedicated project repo created.** RestoreCover is the best retained validation hypothesis from this shortlist, not a validated product or a recommendation to replace existing recovery tools. BackupScopeDiff, StockReturnReplay, and ChangeContextLink are rejected before scoring.

The evidence supports testing whether human handoffs break, not building another backup dashboard. The app recommendation changes only if a baseline exercise proves useful incremental value and a concrete first-user channel emerges.

## Next build step

Before an app scaffold, make one commit-sized synthetic exercise fixture and a baseline comparison protocol. Include five cases: missing approved access, ambiguous restore target, coaching required, stale procedure, and a genuinely successful uncoached test exercise. Compare the same cases in Hudu or a plain runbook plus ticket notes. Treat synthetic fixtures as tool-validation examples, not customer evidence or proof of production recoverability.

## Source access caveats

- The canonical read-only Reddit helper returned JSON HTTP 403 with RSS fallback for r/sysadmin and r/SideProject. RSS scores and comment counts are unavailable; its zero values were not treated as engagement data.
- For r/selfhosted and r/webdev the helper reported JSON/RSS unavailable with HTTP 429. A later small r/sysadmin listing also returned HTTP 429, and helper retries stopped.
- Date-constrained Reddit web searches returned no results. Separate HTML extraction of r/selfhosted/new and r/webdev/new succeeded, as did selected Reddit permalinks. The backup thread's actual fetched comments, not RSS metadata, support the handoff discussion above. Broader scans also found document-recovery and iPhone-backup questions; neither was used as evidence for workplace leave coverage.
- X authentication status and the cheap identity read worked, but the small search returned HTTP 401 Unauthorized. No OAuth2 token was configured, no authentication was changed, and a public X web-search fallback returned no results. There is no X validation in this brief.
- The Commvault cleanroom link found by search resolved to a 404 page; no capability claim relies on it. ServiceNow documentation produced a loading shell, so the adjacent integration description is explicitly search-result-only.
- Vendor pages establish advertised capabilities, not independently tested product behavior. No social writes, outreach, interviews, or production recovery tests occurred.
