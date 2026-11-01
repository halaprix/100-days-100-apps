# Day 096 — DriveBoundary

Date: 2026-11-01
Status: idea-only

## One-line pitch

A local, offline migration-preflight app that joins Google Drive parent-tree and orphan-preview exports with a migration's declared source roots, separating out-of-scope items from unresolved acquisition before an operator stages files or runs another incremental migration.

## Market research brief

- **Decision:** retain a bounded software hypothesis or create a project; reject another general migration engine or orphan-collection script.
- **Target customer:** small migration consultancies handling Google Workspace-to-Microsoft 365 projects across many user accounts.
- **Geography:** global; no jurisdiction-specific compliance claim.
- **Category/substitutes:** GAM exports and orphan preview, migration-provider discovery/settings, and a prepared reconciliation worksheet.
- **Time horizon:** a possible 1–3 day offline prototype after validation, not a production migration product.
- **Must-answer questions:** can source-boundary review avoid unnecessary staging; does it improve on GAM preview plus a worksheet; is the job distinct enough from the existing ScopeCarry hypothesis to deserve a separate app?
- **Evidence bar:** full firsthand report for pain, original tooling documentation for existing capabilities, explicit unknowns for acquisition and provider behavior. No invented interviews, market size, time savings or willingness to pay.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Fresh public community report, 2026-11-01 00:26 UTC; discovered through RSS, full post and visible comments retrieved | [r/sysadmin: Google workspace migration to M355 using Avepoint — dealing with orphan files](https://www.reddit.com/r/sysadmin/comments/1xkpmhm/google_workspace_migration_to_m355_using_avepoint/) | The author reports using GAM to move orphan files into a parent folder before an incremental migration, calls running scripts across thousands of users slow/time-consuming, and separately asks about files under “my computer.” This is one reported project, not a verified general AvePoint limitation. The source title literally says `M355`; the intended destination appears to be Microsoft 365. A visible comment recommends CloudM. |
| Original native-tool documentation; strong counterevidence | [GAM: Users — Drive — Orphans](https://github.com/GAM-team/GAM/wiki/Users-Drive-Orphans) | Already has `collect orphans` with `preview` CSV output, target-folder selection and optional shortcuts. Changing parents may affect other users' access; shortcut collection is not the same operation. This kills a generic orphan finder, previewer or recovery wrapper. No commands were executed against an account. |
| Original inventory documentation; strong substitute | [GAM: Users — Drive Files Display](https://github.com/GAM-team/GAM/wiki/Users-Drive-Files-Display#display-file-list) | Already supports file lists, parent trees and selectors. Its `orphans` selector describes owned items whose parentage does not lead to My Drive, not simply every row with an empty or absent `parents` field. The proposed app must preserve that distinction. |
| Original migration-provider settings; strongest competitor evidence | [CloudM: Google Workspace — Source Settings](https://support.cloudm.io/hc/en-us/articles/14390765633436-Google-Workspace-Source-Settings) | Documents `Migrate orphaned folders` for folders with no parents, says orphaned files are always migrated, and warns of extra requests. Also documents non-owned-folder handling and duplication risks when changing the listed-user setting between runs. A replacement migration engine has no established wedge. These are CloudM's documented semantics, not independently reproduced outcomes or AvePoint behavior. |
| Original provider discovery documentation | [CloudM: Environment Scan](https://support.cloudm.io/hc/en-us/articles/14852712955932-Environment-Scan) | Already exports file/permission/skip/error reports, supports source/batch scans, user concurrency controls, retrying failed users and scan history. Its FAQ describes Google scans as covering users' MyDrive; scan data is not an independent proof of every possible source location. The scan requires a correctly assigned licence. |
| Original platform API documentation | [Google Drive: files.list](https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list) and [File resource](https://developers.google.com/workspace/drive/api/reference/rest/v3/files) | Defines file identity/parent metadata, pagination, corpus selection and `incompleteSearch`. A graph assembled from incomplete, filtered or differently privileged acquisitions cannot establish that a file has no parent or that a migration has complete coverage. |

**Evidence confidence:** moderate for the pain in one current migration project; high for the cited tools' documented capabilities; low for incremental app demand. No second independent customer report was established in this run. Technical documentation corroborates the shape of the problem and the strength of substitutes, not repeated buyer demand. The author's “my computer” wording does not establish which data was cloud-backed, locally available, API-visible or supported by a particular migration route.

## Shortlist and wedge-first gate — before scoring

Constraint: **Nothing new except glue** — reconcile existing exports rather than replace working infrastructure. Three software ideas were evaluated; only the narrowed first hypothesis survives for scoring. Rejected candidates receive no decorative scores.

### 1. DriveBoundary — narrowed and retained for validation

**Specific user → existing substitute → why substitute fails → narrow wedge → distribution path → reason now**

Workspace-to-M365 migration consultant reviewing thousands of accounts → GAM orphan-preview/parent-tree CSV, provider scans and a prepared worksheet → the source reports slow corrective staging, but inadequacy of the existing review workflow is not yet demonstrated → join source identities, declared migration roots and acquisition limits into a minimal per-user boundary review before staging, without moving anything → a worked “GAM orphan preview versus My Drive migration scope” example for migration engineers, with a maintainer-reviewed export recipe as a possible channel; no channel access secured → a fresh project report exposes a concrete pre-incremental decision, not a new platform deadline.

- **Direct competitors:** GAM already previews/collects orphans; CloudM already handles orphaned files/folders and supplies discovery reports. The recommended alternative in the thread is substantive counterevidence, not an invitation to rebuild it.
- **Indirect substitute:** GAM exports joined in Power Query or a short script, with a worksheet listing user, source file ID, known root, proposed handling and unresolved evidence.
- **Status quo:** use the provider's supported discovery/configuration, preview GAM staging, ask vendor support, or switch migration tooling. The author's successful GAM workaround is real substitute evidence even though its scale is inconvenient.
- **Pain test:** the source explicitly describes time-consuming work across thousands of users; missing expected business files can block migration acceptance. Neither a measured weekly time loss nor actual permanent data loss is established.
- **Gate result:** reject generic recovery and faster-scanner claims; retain only cross-export source-boundary triage as a testable hypothesis. No verified feature-absence claim against incumbents.
- **Kill condition:** the native preview/exports plus a prepared worksheet make the same decisions just as quickly, or an incremental improvement to ScopeCarry is sufficient.

### 2. BackupPing — rejected before scoring

**Specific user → existing substitute → why substitute fails → narrow wedge → distribution path → reason now**

Self-hoster backing up books with rclone and cron → a working shell script plus Healthchecks.io, ntfy or systemd failure handling → notifications are missing from the author's setup, not from available products → a proposed copy-paste failure/late-job recipe, not a distinct app → rclone backup setup examples and the existing help thread, with no acquired distribution channel → a fresh question about an already-working backup.

- **Signal:** [r/selfhosted: Best method for selective backups?](https://www.reddit.com/r/selfhosted/comments/1xkuvdz/best_method_for_selective_backups/), 2026-11-01 05:18 UTC. Full post and visible comments retrieved. The author explicitly says the script works and currently checks logs. Visible replies recommend healthcheck-style pings, ntfy and systemd timers; one reply stresses separate restore tests.
- **Direct competitor:** [Healthchecks.io documentation](https://healthchecks.io/docs/) already describes scheduled pings, missed-run alerts, start/failure signals and backup monitoring. Its [shell integration guide](https://healthchecks.io/docs/bash/) is a native recipe baseline, not an unfilled product category.
- **Indirect substitute:** shell exit-code handling plus existing notification tools; systemd logging and failure units. **Status quo:** keep the working script and inspect logs.
- **Why reject:** missing configuration is not a defensible product gap. A success ping also does not verify a restore. No evidence supports replacing the selective backup workflow or adding another dashboard.
- **Kill condition:** an existing heartbeat service plus a short script satisfies the request. Fired.

### 3. RunAnchor — rejected before scoring

**Specific user → existing substitute → why substitute fails → narrow wedge → distribution path → reason now**

Linux operator running rsync/checksum jobs over SSH without wanting terminal-multiplexer shortcuts → tmux, screen, Pueue or systemd-run → tmux's interaction model is disliked, but task-centric alternatives already exist → hypothetical simpler start/status/log/stop CLI → an exact long-running-SSH-jobs setup guide, with no access advantage → a fresh tool request, not a platform breakage.

- **Signal:** [r/selfhosted: Simple way to manage long-running SSH jobs without learning tmux or new keybindings?](https://www.reddit.com/r/selfhosted/comments/1xkqhwi/simple_way_to_manage_longrunning_ssh_jobs_without/). Full post and visible comments retrieved; the page displayed approximately seven hours old during the run. The request includes disconnecting, later checking logs/exit status, listing and stopping jobs. Comments recommend native alternatives, including systemd user services and lingering.
- **Direct competitor:** [Pueue](https://github.com/Nukesor/pueue) already documents terminal-independent task control, persisted logs/queue, status, stopping tasks and copied working-directory/environment context. This is the proposed job, not merely an adjacent product.
- **Native substitute:** [systemd-run](https://www.freedesktop.org/software/systemd/man/latest/systemd-run.html), systemctl and journalctl. The manual distinguishes service/scope modes, clean versus inherited environments, retained post-exit state and the user-manager lifetime when lingering is disabled. Do not promise every `--user` job survives the last logout without checking that context.
- **Indirect substitute:** tmux/screen or a small shell recipe. **Status quo:** learn a few shortcuts or use an existing task manager.
- **Why reject:** a preference for less UI does not establish recurring operational loss, and Pueue already supplies the narrow task-centric interface. A new wrapper would mostly duplicate it.
- **Kill condition:** established tools already deliver the requested workflow with no demonstrated narrow gap. Fired.

## Problem

A migration can follow selected roots while the customer thinks it covers an entire account. A consultant then has to decide whether a suspicious file is genuinely outside the planned traversal, reachable through a different root, represented by a shortcut, or merely absent from an incomplete acquisition. Reparenting first and asking questions later can change source access and create more migration work.

The fresh report demonstrates corrective staging and concern about scale. It does not demonstrate that AvePoint universally cannot migrate these classes, that CloudM fails them, or that thousands of users actually contain problematic items. Those claims must not be smuggled into the product rationale.

## Target user

A migration engineer who already has authorized, redacted source inventories and provider reports and needs to review affected account/file identities before an approved incremental migration. Not an end-user backup app, an automated tenant administrator, a general Google Drive cleanup utility or a replacement migration platform.

## MVP scope

Proposed only; **no app implementation, project repo or scaffold was created**. A Python standard-library CLI with local HTML/CSV output is a plausible bounded prototype after the native-tool comparison.

1. Import a declared source-root manifest, source file/parent-tree metadata, a GAM orphan-preview export and an optional provider scan export. Start with one documented export version; require an explicit schema mapping rather than guessing column meanings.
2. Track acquisition identity, account/corpus, selected fields/filters, collection time, pagination outcome and errors. An export without such context remains `coverage unknown`; the offline tool does not make upstream collection permissionless.
3. Join by account and stable source file ID. Keep duplicate names, conflicting snapshots, source changes and missing columns explicit. Deduplicate repeated observations without erasing which account could see an item.
4. Classify only what the inputs support: `reachable from declared root`, `outside declared traversal`, `parent unresolved`, `GAM orphan-preview candidate`, `shortcut — target coverage unverified`, and `acquisition incomplete`. These labels are observations within a declared acquisition, not assertions of migration success or loss.
5. Preserve root identities and imported selector semantics. A root can legitimately have no parent. A missing parent row may mean a filtered/unauthorized acquisition. Do not equate GAM's parentage-based orphan definition with CloudM's no-parent folder setting. Cycles, inaccessible parent chains and absent roots stay unresolved.
6. Produce the smallest per-user review batch with source IDs, reason, evidence provenance and an operator decision field. Do not claim to reduce API calls or acquisition time; these inputs have already been collected.
7. Treat “Computers” or other special source areas as unknown unless an explicit acquired root and route-specific scope are provided. Do not infer this location from a name or empty parent list. Highlight unsupported source areas as acquisition questions, not certified missing migrations.

**Non-goals:** invoke GAM, collect tenant data, alter parents/owners/ACLs, create shortcuts, run incrementals, execute generated commands, retrieve document contents, verify destination content equality, certify complete migration, or guarantee support for a special Drive source area. Escape imported strings in HTML and neutralize spreadsheet-formula cells in CSV exports. Real inventories stay local and are not public fixtures.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct/native operational substitute | [GAM orphan collection with preview](https://github.com/GAM-team/GAM/wiki/Users-Drive-Orphans) | Already offers the key discovery/preview/collection workflow. Distinguish previews from mutation and shortcuts from actual reparenting. A read-only preview alone is not a wedge. |
| Direct migration-platform substitute | [CloudM source settings](https://support.cloudm.io/hc/en-us/articles/14390765633436-Google-Workspace-Source-Settings) and [Environment Scan](https://support.cloudm.io/hc/en-us/articles/14852712955932-Environment-Scan) | Already covers substantive orphan handling, scans, retries and reports. The app would have to add cross-export interpretation; it must not claim these features are absent. Current pricing was not established; no price-led wedge is credited. |
| Existing provider/status quo | AvePoint plus the operator's GAM staging and incremental rerun | Named in the source, not independently reproduced. Current route/version/configuration and complete AvePoint support documentation were not established; the report is not a product-wide capability verdict. |
| Indirect substitute | Prepared Power Query worksheet or a short source-graph script | Can already join IDs, roots, preview output and unresolved acquisition notes. This prepared baseline, not an empty spreadsheet, must be beaten. |
| Internal substitute | [Day 092 — ScopeCarry](./2026-10-28-scopecarry.md) | Existing research hypothesis for original-scope exceptions across reruns. DriveBoundary is limited to pre-staging source reachability, not destination reconciliation or cross-rerun acceptance. If this is only an input adapter, extend ScopeCarry rather than create a second app. |
| Status quo | Supported provider configuration, GAM preview and vendor support | May be entirely sufficient. Changing platform is a real buyer choice; a new app must not make that sensible option look unavailable. |

## Wedge

The concrete hypothesis is **source-boundary interpretation before staging**: preserve different definitions of an orphan, show what the declared traversal actually establishes, and separate an unresolved parent from a supported out-of-scope conclusion. This is narrower than another migration dashboard or a faster GAM runner.

The advantage is unvalidated. GAM already exports the facts, CloudM already implements important migration behavior, and a prepared worksheet may close the remaining gap. Distribution is **3/5**, not 4: there is a named migration-engineer audience and a specific technical-example route, but no repeatable access, maintainer agreement or evidence that operators would adopt a separate tool. No replies, posts or outreach were performed.

## Kill condition

Stop the standalone app or fold it into the existing research if any of these holds:

- GAM `collect orphans ... preview`, parent-tree exports and a prepared worksheet give the same decisions with equivalent review time.
- Provider-native discovery/configuration resolves the pain without manual staging; CloudM's documented orphan support makes this a serious possibility, not a hypothetical future threat.
- The proposal cannot distinguish missing fields, absent roots, incomplete pagination and permission failures without false completeness.
- Two qualified migration operators cannot demonstrate recurring source-boundary review work or meaningful acceptance risk beyond this single report.
- Real “Computers” acquisition cannot be scoped honestly for the selected route; remove that feature rather than invent coverage.
- The entire useful contribution is an export recipe or a ScopeCarry input adapter. Prefer that smaller outcome.

## Scoring

Assigned after the competitor/substitute and wedge-first gates, only to the narrowed source-boundary hypothesis.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Fresh report explicitly describes slow corrective work at account scale; omitted expected files can block acceptance. Recurrence and measured savings are not established. |
| Feasibility | 4/5 | Offline joins and bounded parent traversal are plausible in 1–3 days. Reliable live acquisition and special-root coverage are deliberately excluded. |
| Demo potential | 4/5 | A fixture can clearly separate a true known-root boundary, an unresolved parent and a shortcut without a misleading all-files-migrated badge. |
| Distribution | 3/5 | Specific migration-engineer audience and exact technical-content route, but no proven repeatable acquisition path. Below the required 4/5. |
| Competitive wedge / timing | 2/5 | GAM preview and CloudM capabilities strongly constrain the gap; one fresh project is not a platform deadline or validated demand. Below the required 3/5. |
| Total | 17/25 | Below 18/25; both dimension gates also fail. |

## Decision

**Winner: DriveBoundary. Status: idea-only. No dedicated project repo created.**

This is the best retained research hypothesis in today's sample, **not a build recommendation**. The generic orphan collector, backup heartbeat app and detached-job runner were rejected because substitutes already do the substantive jobs. The weakest dimension is competitive wedge/timing at **2/5**.

What the evidence supports: inspect source-boundary decisions before applying corrective staging. What remains uncertain: recurring demand, added review value, route-specific source coverage and whether this deserves a separate app at all. A measured native-baseline advantage and operator confirmation would change the recommendation; otherwise publish a recipe or extend ScopeCarry. Validation is tracked in Beads `apps-9s9`; the daily run is `apps-iwl`.

## Next build step

Prepare one commit-sized, redacted fixture and benchmark protocol, before any project creation: a declared My Drive root, an owned chain outside it, an absent parent record, a known root with no parent, a shortcut, duplicate names, a permission failure, incomplete pagination and an explicitly unknown special-root acquisition. Compare manual decisions using GAM preview/parent-tree exports plus a prepared worksheet with the proposed joined view. Require no false completeness, no dropped unresolved cases and a proposed target of at least 30% less review time for two qualified migration operators. This is a future acceptance criterion, not an observed result. Prefer an adapter to ScopeCarry if the experiment shows no separate product boundary.

## Source access caveats

- The canonical Reddit `find` probe returned five r/sysadmin posts through **RSS after JSON HTTP 403**; r/selfhosted and r/webdev initially reported JSON/RSS unavailable with HTTP 429. A later small r/selfhosted listing succeeded through RSS after JSON HTTP 403. A small r/webdev retry still returned HTTP 429; no tight retry loop followed. RSS scores/comment-count zeroes mean unknown, not no engagement.
- Public HTML extraction subsequently retrieved r/selfhosted, r/webdev and r/androidapps new listings and the selected full Reddit posts with visible comments. This is a separate successful fallback, not a claim that the JSON APIs recovered or that every comment was acquired. Ads and unrelated recommendations were excluded from evidence.
- Reddit-constrained, X-constrained and competitor web searches repeatedly returned empty result sets, including broad queries. Search was degraded for this run; emptiness is not evidence of no competitors. Original known documentation URLs and CloudM's public help-center search API supplied substitute evidence instead. The API's orphan search returned and enumerated 15 articles; only relevant original articles were used.
- X account read succeeded, but search returned **HTTP 401**. Authentication status listed no OAuth2 user, so no interactive login or OAuth2 retry was attempted. **No X demand validation** is claimed.
- The Hudu documentation endpoint failed anti-bot extraction during exploratory research; its public product homepage was accessible, but no Hudu feature-absence inference informed the winner. No paid tenant APIs, private workspaces, account data or production migration commands were accessed.
