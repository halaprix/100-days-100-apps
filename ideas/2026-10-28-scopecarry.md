# Day 092 — ScopeCarry

Date: 2026-10-28
Status: idea-only

## One-line pitch

A local-only migration exception ledger that carries unresolved Google Drive exclusions across Microsoft 365 migration reruns, so a successful task does not silently become an all-data sign-off.

## Research brief

- Decision: choose a small software bet, not another cloud migration engine; create a project only if the score and both dimension gates pass.
- Target customer: a small MSP or independent consultant rescuing a partly completed Google Drive-to-OneDrive/SharePoint migration.
- Geography: English-speaking Microsoft 365/Google Workspace operators; no geography-specific compliance claim.
- Substitute set: Microsoft Migration Manager reports, MigrationWiz, rclone checks, and an Excel exception register.
- Time horizon: a 1–3 day offline CSV prototype, conditional on validation.
- Must-answer questions: do native reports already expose the issue; can exclusions survive a change of task scope; will operators prefer a reusable ledger to an Excel join?
- Evidence bar: original platform documentation plus a fully read current incident and its visible comments. No customer interviews, payments, fixture benchmark, or repeated independent demand were established today.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Public community report, 2026-10-28; discovered through Reddit RSS and then fetched as a full web page | [Google Workspace to Office 365 Migration Hell](https://www.reddit.com/r/sysadmin/comments/1xhdadz/google_workspace_to_office_365_migration_hell/) | Consultant reports spending at least four times quoted hours, repeated failures, about 20 excluded folders, and uncertainty about what moved despite a completed user migration. This is an individual report, not measured prevalence. |
| Visible source-author replies; counterevidence | [Same thread and comments](https://www.reddit.com/r/sysadmin/comments/1xhdadz/google_workspace_to_office_365_migration_hell/) | A commenter recommends MigrationWiz; the author says they should have started there and is also considering rclone. The author has not requested or agreed to buy a separate exception ledger. |
| Original Microsoft documentation, updated 2026-09-29 | [Scan and assess Google Drives](https://learn.microsoft.com/en-us/sharepointmigration/mm-google-step2-scan-assess) | Microsoft explicitly says Ready to migrate does not mean every item passed; orphaned files are not scanned or reported. Splitting a drive into subfolder tasks requires separate inventory reconciliation, including root-level files and destination mappings. This establishes a real review job, not an absent native feature. |
| Original Microsoft report schema | [Cloud migration reports and codes](https://learn.microsoft.com/en-us/sharepointmigration/mm-cloud-reports) | Native reports already provide item-level statuses, result codes, task and transaction identifiers, historical ProjectError records, and FilesFiltered/FilesFailed summary counts. Completed statuses 102, 120 and 122 can describe unsupported items that were not transferred. A simple error viewer would duplicate native capability. |
| Original Microsoft documentation; scope/identity constraints | [Migration Manager Google FAQ](https://learn.microsoft.com/en-us/sharepointmigration/mm-faqs-google) | Inaccessible items are excluded; renamed source or destination paths can produce duplicates. Same-name files receive suffixes. File-size totals are not reliable proof of Google-native document coverage. |
| Original substitute documentation | [rclone check](https://rclone.org/commands/rclone_check/) and [Google Drive backend](https://rclone.org/drive/#import-export-of-google-documents) | rclone already checks source/destination without changing them and writes missing/different/error lists. Google documents are exported into chosen formats with appended extensions. A path or checksum comparison alone is not a universal migration-verification method. |
| Original vendor product and pricing pages; marketing claims, not independently tested | [MigrationWiz](https://www.bittitan.com/migrationwiz/) and [pricing](https://www.bittitan.com/pricing-bittitan-migrationwiz/) | Existing migration product covers documents, mapping/filtering, project sharing and action logging. Listed User Migration Bundle is $17.50 per user; Shared Documents is $25 up to 50 GB or $48 up to 100 GB per library. These are different license scopes, not a quote for this incident; they undermine a blanket claim that paid migration software is unaffordable. |
| Original Google API reference | [files.list](https://developers.google.com/workspace/drive/api/reference/rest/v3/files/list) | Pagination, corpora, access scope and incompleteSearch constrain any supplied inventory. A local ledger cannot infer unseen files or prove tenant-wide completeness from a report export. |

## Problem

Repeated exclude-and-retry cycles can turn a migration incident into scope debt: the operator fixes the currently selected task while the client still expects the original drive's content. A later task can complete without resolving earlier exclusions or files outside replacement subfolder tasks.

The painful behavior is visible within one incident: repeated failures, repeated exclusions, and reported paid-time overrun. Independent recurrence across multiple customers remains unverified. The 150 GB share mentioned by the author is not, by itself, proof of violating a documented limit or the cause of the failures. The email-count issue is separate and excluded from this idea.

**Status-quo pain test:** reported lost billable time and blocked delivery clear the material-pain bar. It is not yet established that maintaining the exception register, rather than actually moving the files, consumes enough time to justify a new app.

## Target user

An MSP migration technician who already has native scan/migration CSVs, has changed task scope during troubleshooting, and needs to hand unresolved original-scope exceptions to a colleague or content owner. Not a first-time home user, generic IT dashboard buyer, or enterprise compliance team.

## MVP scope

Constraint: **Nothing new except glue** — reuse native reports; do not build another transfer engine.

1. Import operator-supplied scan and migration TransactionItem.csv files with explicit report type, task identity, transaction/run date, source scope and destination mapping. Import ProjectError and summary exports as additional evidence, not as interchangeable latest-state tables. Interpret statuses by report phase: Microsoft documents scan Status=Skipped as scan complete and ready to migrate, not an excluded or missing item.
2. Load a small operator-approved original-scope inventory and a dated exclusion/disposition CSV. Record how the inventory was acquired, its authorization scope, filters, pagination completion and any known incompleteSearch result. Unknown acquisition coverage stays unknown.
3. Carry exceptions forward across reruns and task splits. Mark them unresolved, explicitly accepted as out of scope, or reported successful in a later mapped run. Preserve original rows and evidence references; never clear an exception merely because a later task says Completed.
4. Require explicit mappings when tasks or names change. Preserve raw paths, case and Unicode. Duplicate names, suffixes, shortcuts, Google-native exports and ambiguous matches require human review; no automatic path-only identity merge.
5. Export a reviewable CSV plus a small static HTML handoff with unresolved items, declared owner decisions and evidence references. Escape HTML and guard CSV formula injection. No upload or telemetry; report contents and filenames remain sensitive even without file bodies.

Boundaries: no authentication or live collection in the first prototype; no copy, delete, retry, permission changes, mailbox migration, automatic source-retirement approval, content-equality certification or permission/version-history certification. Native reported success, independently observed destination presence, and verified content equality are different claims. The prototype only carries the evidence supplied to it.

A bounded parser/demo is feasible in 1–3 days. Reliable cross-provider content reconciliation is not included in that estimate. No prototype or customer-data test was performed in this research run.

## Shortlist — competitor and wedge-first gates before scoring

Three app candidates were considered. The two killed candidates are deliberately not assigned numeric scores.

### 1. ScopeCarry — narrow and retain as today's research winner

**Wedge-first line:** small MSP rescuing a partly completed Google Drive migration → Migration Manager detailed reports plus Excel, MigrationWiz or rclone → native reports explain current and historical errors, but an operator must still reconcile original scope with changed tasks and explicit exclusions → offline carry-forward exception decisions across reruns, without moving data → a worked sample for the exact “completed migration / excluded folders” search problem and opt-in MSP fixture reviews → a fresh costly rescue incident plus current Microsoft guidance explicitly requiring inventory reconciliation.

- Direct competitors/substitutes checked: native Migration Manager reporting and MigrationWiz; both already solve substantial parts of the job.
- Indirect substitutes: Excel/Power Query over the native CSVs and rclone missing-file reports.
- Status quo: keep exports and a manual exception register, consult vendor support, or switch the remaining migration workload to an established product.
- Proposed gap is specific but unproven. Narrow away from transfer, error translation, generic reporting and broad “migration verified” claims.
- Gate result: retain a validation hypothesis, not a build recommendation. Search intent and named communities exist; repeatable acquisition and superiority over a worksheet do not.

### 2. PxeInventory — reject before scoring

Fresh source: [Which servers have PXE enabled?](https://www.reddit.com/r/sysadmin/comments/1xhfqs3/how_do_you_even_find_out_which_of_your_servers/) (2026-10-28); full post and visible comments read.

**Wedge-first line:** mixed-vendor server operator → iDRAC/iLO inventory, Redfish and vendor scripts → a normalized fleet view might require vendor-specific attribute handling, but absence of a workable native solution was not demonstrated → proposed offline BIOS/PXE comparison → server-management documentation and operator examples → fresh inventory question, not a verified new vulnerability advisory.

- Direct/native substitutes: [Dell iDRAC Redfish scripting](https://github.com/dell/iDRAC-Redfish-Scripting) supports BIOS/NIC management and inventory. The thread itself points to LOM and Redfish.
- Indirect substitute: a read-only vendor script plus configuration-management inventory.
- Status quo: query existing management interfaces; do not reboot into BIOS for each machine by default.
- Kill condition fired: a generic security/inventory wrapper without a proven cross-vendor gap or acquisition channel is reject-by-default. The post's CVE-2026-97631 identifier and exploit narrative were not independently verified and are not used as factual timing evidence.
- Result: rejected; no numerical score.

### 3. VoteMute — reject before scoring

Fresh source: [Political spam-text filtering request](https://www.reddit.com/r/androidapps/comments/1xh4kd6/how_to_get_these_fucking_political_spam_texts_off/) (2026-10-27); full post and visible comments read.

**Wedge-first line:** Android user receiving unwanted political SMS → Google Messages spam controls and third-party SMS clients → the author says existing filtering missed these messages → proposed local unknown-sender keyword rule → exact Android keyword-blocking help queries → current unwanted-text complaint, not a verified regulatory exemption.

- Direct substitute: [Fossify Messages](https://github.com/FossifyOrg/Messages); a commenter recommends its keyword block, and the source author explicitly reports testing it from a VoIP number and says it works.
- Indirect substitute: existing spam filters and carrier controls; manual per-number blocking is the disliked status quo.
- Kill condition fired: the requested narrow job already has a source-confirmed working solution. A new SMS app would add default-handler/permission and trust friction rather than a demonstrated advantage. The author's claim about political-text exemptions is not adopted as a legal fact.
- Result: rejected; no numerical score. A help article would be more useful than another app.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct/native | Microsoft Migration Manager | Already exports detailed current results, historical errors, result-code explanations, filtered counts and transaction IDs. Benchmark the proposed carry-forward decisions against these exports, not just the portal badge. |
| Direct/adjacent | BitTitan MigrationWiz | Established document/email migration, filtering/mapping and collaboration. Source author shows interest. This run did not test its reporting or establish that it lacks exception ownership; that is an open competitor question, not an asserted gap. |
| Indirect | rclone check and Drive backend | Native missing/differ/error reporting is a strong zero-new-product baseline. Cross-provider conversion and naming require deliberate mapping; no claim that rclone cannot be configured appropriately. |
| Indirect | Excel or Power Query exception register | Can join run exports and preserve explicit accepted exclusions. Probably sufficient for occasional jobs; the app must beat a reusable worksheet, not an empty spreadsheet. |
| Status quo | Keep current exports, manually track excluded folders, ask support or purchase an established migration tool | No evidence today that an additional application is preferable. Record unresolved client scope rather than treating task success as full migration acceptance. |

## Wedge

The only retained wedge is **original-scope exception continuity** after task changes: “this folder was excluded on the first attempt; what evidence or owner decision resolved it?” It is not “Microsoft has no item reports” or “nobody verifies migrations.”

Microsoft's explicit source-inventory reconciliation guidance makes this a real operator task, while its rich reports and a worksheet make the product opportunity uncertain. This is distinct from yesterday's export-handoff integrity/provenance idea: no forensic packaging or hash wrapper; the decision is migration-scope debt.

## Kill condition

Stop or reduce to a reusable worksheet if any of the following holds:

- Native CSVs plus a prepared Power Query workbook give operators the same carry-forward and sign-off review within ten minutes on the same fixture.
- MigrationWiz or another tool the intended technicians already use supplies sufficient exception ownership/history without an extra product.
- Three opt-in migration operators cannot provide two independent recurring examples of scope debt or identify a meaningful review-time saving; today's single incident is insufficient.
- More than incidental manual identity mapping is needed after renamed/split tasks, so the ledger adds work or falsely clears unresolved items.
- Source inventory acquisition is more costly than the review saved, or operators need trustworthy content/permissions verification rather than this narrower evidence ledger.

Validation target, not measured result: at least 30 minutes saved per migration handoff, no falsely cleared exclusions, and explicit unknowns for incomplete inventories. No claim of savings is made today.

## Scoring

Scores assigned only after the three candidate gates and the substitute review above.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Concrete quoted-hours overrun and delivery uncertainty; willingness to adopt a separate ledger is unproven. |
| Feasibility | 4/5 | Bounded offline CSV ledger is small; identity ambiguity must fail to human review rather than claim full reconciliation. |
| Demo potential | 4/5 | A clearly labeled synthetic example can show a green latest task beside unresolved original-scope exclusions. No such demo was built today. |
| Distribution | 3/5 | Specific MSP/M365 operator audience and an exact problem-query sample strategy, but no demonstrated repeatable access or committed reviewers. A content idea alone is not a 4/5 channel. |
| Competitive wedge / timing | 2/5 | Native reports, a prepared worksheet and MigrationWiz are strong. Cross-rerun decision continuity is a hypothesis, not a verified missing feature. |
| Total | 17/25 | Research winner only; below 18/25 and below both dimension gates. |

## Decision

**idea-only. No dedicated project repo or scaffold created.** Weakest dimension: competitive wedge/timing, 2/5. Distribution is also below the required 4/5. Do not manufacture a build recommendation from a costly but singular incident.

Recommendation: test whether a tiny reusable worksheet suffices before writing a standalone product. Confidence is moderate that the migration-review pain exists and low that this app deserves to exist. A timed comparison and independent operator examples would change the recommendation; a better portal screenshot would not.

## Next build step

Create one clearly synthetic, offline comparison fixture containing original scope, two dated native-format runs, one accepted exclusion, one unresolved excluded folder, a split-task root-file gap and an ambiguous renamed item. Write an expected-disposition CSV and a prepared Power Query/native-report baseline; run a timed operator review before implementing a ledger. Track this validation in Beads. Do not use client exports in public fixtures.

## Source access caveats

- Canonical Reddit find probe used a 48-hour window with six requested posts per subreddit. Public JSON was blocked with HTTP 403; RSS returned six posts each for r/sysadmin and r/androidapps. Their zero score/comment placeholders are unknown engagement, not actual zero engagement.
- r/selfhosted and r/webdev were unavailable in that probe with HTTP 429 reported by the helper's JSON/RSS fallback chain. No tight retries were made. Reddit-constrained web searches for additional migration reports returned no results; independent repeated demand was not established.
- Web extraction successfully retrieved the complete main posts and visible comments for all three shortlisted source threads. This is separate from the blocked public JSON endpoint; no claim to exhaustive comment coverage.
- xurl account lookup succeeded, but the cheap search returned HTTP 401 Unauthorized. No OAuth2 token was listed, so an OAuth2 retry was not useful. X-constrained web search returned no results; no X evidence supports the decision.
- Broader competitor searches also returned several empty result sets; direct original documentation/product URLs were fetched instead. Pricing and vendor capability descriptions were read, not purchased or benchmarked. Microsoft pages exposed their article text despite a generic authorization notice, and label the two Google migration guidance articles as AI-assisted; they are official published guidance, not independent demand evidence.
