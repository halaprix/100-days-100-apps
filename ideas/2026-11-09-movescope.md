# Day 104 — MoveScope

Date: 2026-11-09
Status: idea-only

## One-line pitch

A local-first incident-review app that turns Google Shared Drive move/rename exports into per-file change chains, separating transient churn, observed net changes and unresolved history before an administrator plans any repair.

## Research brief

- **Decision:** retain a narrowly scoped event-triage hypothesis; reject an automatic rollback tool or another backup service.
- **Target customer:** an MSP Google Workspace administrator investigating a sudden multi-folder move/rename incident in a Mac-using client organization.
- **Geography:** English-language Workspace/MSP support communities; no jurisdiction-specific claim.
- **Substitute set:** native Drive audit searches, GAM reports plus a prepared worksheet, and an existing backup provider's snapshot/change view.
- **Time horizon:** a one-to-three-day offline timeline prototype, conditional on a benchmark against those substitutes.
- **Must-answer question:** does grouping repeated changes by stable file ID materially reduce incident-review effort without implying that partial logs can reconstruct or safely restore the entire prior tree?
- **Evidence bar:** one fresh operator incident plus original platform/tool documentation. Repeated independent incidents, measured review time, interviews and willingness to pay are not established. No market-size claim.
- **Creative constraint:** “Nothing new except glue” — leave acquisition and recovery to existing tools; test only the interpretation step.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Fresh original operator report; HTML recovery, about 16 hours old when fetched | [Bulk file move and rename — Google Drive for desktop on macOS update](https://www.reddit.com/r/sysadmin/comments/1xr276j/bulk_file_move_and_rename_google_drive_for/) | An administrator reports 300+ files/folders moved, merged or renamed across Shared Drive project folders, including names changing and changing back within seconds. They already inspected audit logs and contacted support: evidence that native acquisition works, not proof of a missing collector. |
| Original Google platform documentation | [Drive audit event definitions](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/drive) | `move` documents `doc_id`, `source_folder_id` and `destination_folder_id`; `rename` documents `doc_id`, `old_value` and `new_value`. These enable a bounded chain view when fields are actually present. One user action can generate multiple events, including multiple primary events. |
| Original Google native-substitute documentation | [Drive log events](https://support.google.com/a/answer/4579696?hl=en), [activities.list](https://developers.google.com/workspace/admin/reports/v1/reference/activities/list) | Native filtered investigation already exists. Google explicitly says not every activity is logged; edition, privileges, lag and retention matter. Reports are paginated. Timestamp proximity is not completeness or a trustworthy total ordering. |
| Original Google platform context | [Drive for desktop on macOS](https://support.google.com/drive/answer/12178485?hl=en) | Google documents File Provider use and differences from legacy streaming. This does not independently confirm the Reddit author's account of support's diagnosis or prove an OS update caused their incident. |
| Original existing-tool documentation | [GAM reports](https://github.com/GAM-team/GAM/wiki/Reports), [file management](https://github.com/GAM-team/GAM/wiki/Users-Drive-Files-Manage) | GAM already supports Drive activity reports, time/event filters and file-management operations. A prepared GAM export plus worksheet/script is a serious baseline, not an empty spreadsheet. No GAM mutation was executed. |
| Original commercial substitute documentation | [Afi Google Workspace backup](https://afi.ai/docs/gw/) | Afi documents Shared Drive coverage, metadata/permission recovery, backed-up versions and a snapshot-range changes view. Reject generic change reporting or recovery as the claimed gap. A prior backup is a different evidence source from after-the-fact audit exports. |

**Confidence:** medium that the reported incident warrants careful review; low that an additional app is necessary. The fresh report is one organization, not demonstrated recurring market demand. Its audit attribution to a user/client does not establish human intent, root cause, the responsible device or a universally safe mitigation. The reported “merge” is not verified content merging or a documented event primitive.

## Shortlist: competitor and wedge-first gate before scoring

Three software candidates were compared. Only the narrowed survivor is scored; rejected candidates receive no compensating feasibility points.

### 1. MoveScope — narrowed and retained

**Wedge-first line:** MSP administrator triaging a Shared Drive move/rename burst → native Drive investigation, GAM exports plus a worksheet, and backup change views → the source demonstrates repeated transformations across many objects, but not failure of a prepared native workflow; folding per-ID chains may reduce repeated reading → offline event-chain and uncertainty review, not tree rollback → a reproducible sanitized “rename out-and-back plus folder moves” example for exact Workspace/GAM incident questions and invited MSP support discussions → a fresh 300+ item report justifies testing the workflow, not declaring a newly confirmed macOS regression.

- **Direct functional competitors:** native Drive investigation and Afi snapshot changes/recovery for customers with prior backups.
- **Indirect substitutes:** GAM export, a short grouping script and a prepared Power Query/worksheet; Google support and the customer's backup operator.
- **Status quo:** inspect events by file ID, compare relevant inventory/backup evidence and have the responsible administrator decide which changes were unwanted. The source already did part of this successfully.
- **Gate result:** reject automatic inverse replay and generic audit dashboards. Retain only a bounded triage hypothesis; absence of a superior existing report has not been demonstrated.
- **Kill condition:** native/GAM/backup views with a prepared worksheet produce the same accurate review at equal or lower complete effort; then contribute a recipe or adapter instead of a standalone app.

### 2. TunnelSense — rejected before scoring

**Wedge-first line:** Android Tailscale user whose public websites work but tailnet service fails → native app-based split-tunneling settings and official help → the source initially mistook per-app exclusion for a DNS/server problem, but the documented setting solved it → a proposed app-route explainer duplicates a successful checklist → exact Android split-tunneling support questions → today's confusion is a documentation opportunity, not unmet replacement demand.

- **Signal and resolution:** [Tailscale prevents Android phone connection](https://www.reddit.com/r/selfhosted/comments/1xrjg23/tailscale_prevents_android_phone_connection_to_my/). The [author confirms the split-tunneling explanation solved it](https://www.reddit.com/r/selfhosted/comments/1xrjg23/comment/19sd23z9vcev7/).
- **Direct/native substitute:** [Tailscale's Android guide](https://tailscale.com/docs/features/client/android-app-split-tunneling) explicitly documents that checked apps are excluded in the default mode, including both traffic and DNS. MDM inclusion mode is a different configuration.
- **Indirect substitute / status quo:** read the relevant setting/help and check the affected app, rather than changing DNS repeatedly. Another commenter alleges a separate DNS issue; that does not diagnose this resolved case.
- **Kill:** native instructions already solve the actual job. A separate diagnostic app would run in its own context and cannot by itself prove another app's traffic path. No repeated unresolved or costly review workflow established.

### 3. UpgradeScope — rejected before scoring

**Wedge-first line:** Supabase Free organization owner considering Pro while retaining old projects → native organization-based billing guide, multi-project pricing calculator and upcoming invoice → a fresh author reports surprise recurring compute costs, but current native tools already explain and calculate the cross-project effect → a proposed organization-upgrade cost preview duplicates those tools → exact additional-project billing questions → today's complaint supports clearer education, not a fabricated new price change or proof of historical disclosure.

- **Signal:** [Supabase billing/support complaint](https://www.reddit.com/r/webdev/comments/1xrb9gw/supabase_removed_my_billing_complaint_from/), about 10 hours old. The author's spending/support account is not independently audited; no claim about moderation misconduct or entitlement to a refund is adopted.
- **Direct/native competitors:** [billing guide](https://supabase.com/docs/guides/platform/billing-on-supabase), [pricing and multi-project calculator](https://supabase.com/pricing), [cost controls and upcoming invoice](https://supabase.com/docs/guides/platform/cost-control). Paid plans apply to organizations; compute is per project and is excluded from the documented Spend Cap. The pricing page already lets users add projects to its estimate.
- **Indirect substitute / status quo:** inventory existing projects, use that calculator and billing view, and consult the transfer guide if separate organizations are appropriate. This run does not recommend deleting projects or moving them without a separate operational review.
- **Kill:** a new calculator has no demonstrated wedge over the current native calculator. Today's documentation cannot establish what the author saw during an earlier upgrade, and a new app cannot recreate that missing historical evidence. Reject generic cloud-cost dashboards and chargeback automation.

## Problem

During an unexpected rename/move burst, a long event export can mix transient name churn, folder changes, subsequent legitimate edits and incomplete observations. Counting rows or listing the last event is not the same as identifying the objects whose observed state still differs from a chosen reference.

**Status-quo pain test:** disruption to hundreds of shared project objects is a credible operational rework risk, not merely a cosmetic preference. However, the post does not measure downtime, lost revenue or more than 30 minutes of weekly work. The unmet part of the review workflow remains a hypothesis. If a prepared native filter/worksheet is sufficient, reject the app despite the incident's seriousness.

## Target user

A Workspace/MSP incident owner with authorized access to the relevant exports and a responsibility to distinguish observed changes from proposed remediation. Not a consumer recovery utility, general security scanner, backup replacement, forensic authenticator or macOS patch-management product.

## MVP scope

Proposed software only; no prototype or customer data was processed today:

1. A Python CLI producing an escaped, self-contained local HTML report from explicitly supplied Admin Reports API JSON exports. Start with one documented JSON contract; do not claim compatibility with every Admin console CSV or GAM flattening format.
2. Record declared tenant/scope, time window, acquisition time, applied filters, page completion and schema/tool versions. Preserve raw input references and event positions. Missing pagination/provenance remains unknown, even if no continuation token is visible in a flattened export. File hashes establish only file integrity, not origin or completeness.
3. Group by tenant plus stable `doc_id`, preserving individual `events[]` entries. Display observed `rename` old/new values and `move` source/destination IDs verbatim. A title is not identity; a parent title alone cannot identify the folder.
4. Highlight a return to the observed starting name/parent separately from observed net change. Label this as “within supplied evidence,” never “unchanged since before the incident.” Missing predecessors, chain mismatches and unsupported events prevent a confident net summary.
5. Preserve original timestamps, activity qualifiers and event positions. Do not treat `id.uniqueQualifier` as a documented causal sequence number. Equal-time alternatives remain ambiguous unless another source establishes order. Do not collapse all events sharing an activity ID or discard non-primary events blindly.
6. Show relevant add/remove-folder, trash, restore, copy or other unsupported observations as blockers to a simplistic move/rename fold, not as silently ignored history. Keep source-specific identities and limitations; no automatic conflation of different audit APIs.
7. Optionally attach an operator-supplied later metadata inventory with its own capture time. Compare only fields actually acquired. Later legitimate edits, missing/inaccessible objects, absent parents, duplicate titles, folder descendants and cross-drive changes remain explicit review cases. Moving a folder can alter descendant paths without a separate event for every descendant; this is not a complete historical-tree reconstruction.
8. Output an evidence-linked review list, not executable commands, a restoration plan or an “apply” button. No network access, background collector, file content ingestion, production writes, process termination or OS-update hooks in this MVP.

**Privacy and safety:** exports can contain identities, filenames, app identifiers, network information and sensitive project names. Minimize fields, keep reports local, escape untrusted HTML/CSV values and use synthetic public fixtures. Redacted derivatives remain distinct from originals; hashes are not anonymization. Offline import does not eliminate the privileges or edition requirements needed for upstream acquisition. No guarantee of restored content, historical permissions or legal admissibility.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Native functional competitor | [Google Drive audit/investigation](https://support.google.com/a/answer/4579696?hl=en) | Already offers filtered event review. The source administrator already used the audit logs. Benchmark a prepared investigation, not manual scrolling through everything. |
| Commercial competitor / recovery substitute | [Afi Google Workspace backup](https://afi.ai/docs/gw/) | Snapshot-range changes, metadata/permission recovery and versions already exist for backed-up data. Do not invent missing ID preservation or exact incident-reversal behavior without testing. |
| Indirect substitute | [GAM reports](https://github.com/GAM-team/GAM/wiki/Reports) plus a prepared worksheet/grouping script | Existing acquisition and analysis building blocks may be enough. Include export/filter setup in the benchmark. |
| Adjacent operator tooling | [GAM file management](https://github.com/GAM-team/GAM/wiki/Users-Drive-Files-Manage) | Already supplies management primitives; a mutation wrapper is neither novel nor safe as an unattended incident response. |
| Status quo | Native investigation, support and existing backups | May solve this occasional incident better than installing another app. There is no evidence that every affected customer lacks backups. |

## Wedge

The retained hypothesis is **per-object move/rename-chain compression with visible conflicts**, for an administrator who already has incident exports and needs a bounded triage view. It is not collecting more logs, claiming to recover a vanished tree or reversing every operation attributed to a user.

Afi's change view and a short GAM/worksheet workflow substantially weaken the case. No hands-on comparison establishes a product gap. The correct deliverable may be an upstream GAM example or a report template, not another standalone application.

**Distribution hypothesis:** publish one synthetic rename-out-and-back/folder-move example answering exact “Google Shared Drive files moved and renamed” and GAM audit-analysis questions, then seek maintainer-approved placement in Workspace/GAM support resources and invited MSP incident discussions. Those are specific first-user topics, but reliable reach, permissions for placement and repeated adoption are unproven. Distribution stays 3/5; no unsolicited replies, outreach or social writes occurred.

## Kill condition

Reject the standalone app if any holds:

- A prepared native investigation, GAM worksheet/script or existing backup changes view yields equally accurate findings at equal or lower acquisition-plus-review effort.
- Three relevant operators cannot establish recurring review need, or fewer than two show a provisional 30% reduction in total effort with no missed material changes. This is a proposed validation bar, not a measured outcome.
- Useful output requires asserting complete history from partial logs, imposing arbitrary causal order or promising safe inverse replay despite legitimate later changes.
- Required prior-state evidence is usually missing, so most output is unresolved without enough saved effort to justify another tool.
- An existing-tool contribution covers the workflow adequately; favor that narrower product boundary.

## Scoring

Assigned after competitor checks and narrowing, not before.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Hundreds of affected shared project objects justify careful triage. Recurrence and actual operator time are unmeasured. |
| Feasibility | 4/5 | A bounded offline per-ID timeline is plausible in one to three days. Historical tree reconstruction, recovery and live integrations are excluded. |
| Demo potential | 4/5 | Synthetic transient renames, parent moves and conflicting chains make the difference visible. No runnable demo was built today. |
| Distribution | 3/5 | Specific Workspace/GAM/MSP incident channels exist; repeatable access and adoption are not established. |
| Competitive wedge / timing | 2/5 | Fresh incident, but native investigation, GAM and backup change views are strong substitutes. No proven gap or independently confirmed new platform regression. |
| Total | 17/25 | Below threshold; Distribution and competitive-wedge dimension gates also fail. |

## Decision

**Idea-only. No dedicated project repo created.** MoveScope is the strongest retained research hypothesis among three checked candidates, not a validated build opportunity. Weakest dimension: competitive wedge/timing at 2/5; Distribution is 3/5.

The evidence supports testing interpretation effort, not deploying a fix for the reported macOS incident. Support's alleged File Provider diagnosis and quit-before-update advice remain the author's report, not a verified general remediation. The visible comment asserting macOS cannot be managed is not adopted as a platform fact.

## Next build step

If pursued, make one validation-sized fixture commit containing synthetic Admin Reports event exports and expected triage findings: rename out-and-back, chained moves, a folder with descendants, repeated activity entries, equal-time conflicts, missing parent IDs and later legitimate changes. Include a prepared native/GAM worksheet baseline. Time complete acquisition and review with three relevant operators before building a standalone app; contribute an existing-tool example if it is sufficient.

Follow-up is tracked in Beads (`apps-7c4`). No customer outreach, tenant access, restore, update or file mutation was performed.

## Source access caveats

- Canonical `reddit-readonly find` probed r/SideProject, r/SaaS, r/sysadmin, r/selfhosted and r/webdev with small limits. JSON was blocked with HTTP 403/theme-beta for the successful fallback cases; r/SideProject and r/selfhosted returned RSS posts. r/SaaS, r/sysadmin and r/webdev were unavailable with HTTP 429 warnings. A separate small r/androidapps posts probe also returned HTTP 429. No tight retries.
- RSS scores/comment counts were unavailable placeholders, not engagement evidence. The winner's post and visible discussion were recovered through direct public HTML extraction after Reddit-constrained search queries returned no results. r/sysadmin, r/webdev, r/Entrepreneur and r/androidapps listings were readable via HTML. Listing discovery is not full-thread validation; selected posts were fetched separately, and collapsed comments were not exhaustively expanded.
- `xurl whoami` succeeded; read-only search returned HTTP 401 Unauthorized. No OAuth2 user was configured, so no interactive authentication or credential change was attempted. X-constrained web search returned no results; no X validation is claimed.
- General web search also returned no results for a concrete Drive/GAM query. This was not treated as competitor absence. Original vendor/tool documentation was retrieved directly. A guessed Afi route returned 404; its documentation index supplied the actual Google Workspace page. Guessed Drive Activity schema routes and an unrelated asset-doc route returned 404 and were discarded, not used as evidence.
- Documentation capabilities were not hands-on acceptance-tested. This brief distinguishes the fresh community incident from vendor specifications and commercial claims. No independent recurring demand or savings is claimed.

## Repository verification caveat

Fresh repository-wide snapshot verification still fails with `KeyError: 'source_commit'`, already tracked in Beads (`apps-mq0`). No snapshot or verifier code changed today. Daily JSON, brief/index consistency and focused public-safety checks are separate verification; they do not make the repository-wide suite green.
