# Day 102 — CohortTail

Date: 2026-11-07
Status: idea-only

## One-line pitch

A local-first scenario app that shows why a confirmed Wasabi minimum-billing-duration change does not immediately remove old-object billing exposure, keeping pre-change and post-change upload cohorts separate.

## Research brief

- **Decision:** retain a narrowly scoped policy-cutover explanation hypothesis; reject another generic cloud-storage calculator, billing dashboard or backup recommendation engine.
- **Target customer:** an MSP backup operator explaining a confirmed minimum-duration change on an existing Wasabi Pay-Go account to a budget owner.
- **Geography:** English-language infrastructure teams; account-specific terms override public examples. No tax, contractual or compliance advice.
- **Substitute set:** Wasabi Account Control Manager (WACM) usage/invoice exports, Wasabi support, Rack2Cloud's Veeam Immutable Storage Estimator (VISE), and a prepared cohort worksheet.
- **Time horizon:** a one-to-three-day offline scenario MVP only if an existing-tool/worksheet comparison establishes additional value.
- **Must-answer question:** does separating upload cohorts and unresolved history reduce real explanation effort beyond native reports and existing simulation tools?
- **Evidence bar:** one fresh operator question with visible discussion, older independently authored cost questions, current provider documentation and direct competitor documentation. No customer interviews, account exports, measured savings, paid pilots or defensible TAM estimate.
- **Creative constraint:** “Subtract” — remove live collection, automatic retention changes and provider rankings; retain one temporal billing-policy explanation.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Fresh public operator question; discovered through RSS, post and visible comments recovered through HTML | [Immutable cloud storage for enterprise backups](https://www.reddit.com/r/sysadmin/comments/1xpobo6/what_are_you_using_for_immutable_cloud_storage/) | Posted 2026-11-06 at 21:12 UTC. Author compares storage for roughly 250 TB of backups against an annual budget, egress and recovery requirements. This is a real planning question, not proof that the author has a policy-cutover problem or wants another calculator. |
| Visible discussion in the same thread; not independent customers | [Minimum-duration caution](https://www.reddit.com/r/sysadmin/comments/1xpobo6/comment/19s8xed4dlbic/) and [estimation friction](https://www.reddit.com/r/sysadmin/comments/1xpobo6/comment/19s8ulrcivatf/) | Commenters flag minimum storage duration and cost-estimation complexity. Other replies report satisfactory existing backup/storage choices and emphasize defining recovery objectives first. Do not treat this as consensus, independently measured cost or a verified reliability comparison. |
| Older original operator question and vendor reply; historical, not fresh demand | [Wasabi Cost Estimation, January 2022](https://forums.veeam.com/viewtopic.php?f=52&t=78841&start=0) | Operator explicitly asks how to calculate cost with short backup retention and minimum-duration billing. Veeam's reply says the described object-storage path uploads incremental-forever rather than naively uploading each weekly full. Its old dollar rate is not current pricing, and its version-specific behavior is not a universal model. |
| Original provider policy documentation; page states update on 2026-09-14 | [Minimum Storage Duration Policy](https://docs.wasabi.com/docs/how-does-wasabis-minimum-storage-duration-policy-work) | Wasabi explicitly says that a change from 90 to 30 days applies only to objects uploaded after the change; older objects retain their original 90-day policy. It also says the change ends the current billing cycle and starts another, generating an invoice. A documentation revision date does not prove the policy itself is new. |
| Original provider pricing and billing documentation | [Pricing FAQ](https://wasabi.com/pricing/faq) | Distinguishes Timed Active Storage, Timed Deleted Storage, account minimums, Pay-Go and RCS terms. Immutability is a separate protection property. Free egress/API use has policy conditions; no unconditional “free unlimited restores” claim is justified. |
| Native substitute documentation; usage/invoice pages state update on 2026-10-22 | [Usage exports](https://docs.wasabi.com/docs/access-consumption-data), [Control Account utilization](https://docs.wasabi.com/docs/storage-usage-view-control-account), [WACM invoices](https://docs.wasabi.com/docs/invoices) | Native reporting already separates active/deleted storage and supports historical CSV/JSON/Excel exports and calculated invoice lines. Usage rows are end-of-day counters, not object birth/deletion histories or automatically invoice-equivalent accruals. This is strong counterevidence to a dashboard/rebilling product. |
| Direct competitor; original product description and readable app page | [Rack2Cloud VISE](https://www.rack2cloud.com/veeam-immutable-storage-cost-estimator/) and [estimator](https://vise.rack2cloud.com/) | Already offers browser-local day-level retained/billed-capacity simulation, provider minimums, versioned Veeam behavior, scenario comparison and exports. Offline, deterministic and “explains minimum duration” are not differentiators. No custom scenario was executed in this run. |
| Original backup-platform documentation | [Veeam Block Generation](https://helpcenter.veeam.com/docs/vbr/userguide/object_storage_block_generation.html) | Block generation and lock extension can make actual object retention differ from configured backup retention. A backup job schedule alone cannot supply object deletion dates for a correct billing model. |

**Confidence:** medium that storage-cost interpretation can affect consequential purchases; low that policy-cutover explanation deserves a standalone app. Fresh demand is broad provider selection, while the narrower cohort problem is a hypothesis derived from documented semantics. Multiple replies describe working substitutes. No source establishes repeated customer demand for this exact app.

## Shortlist: competitor and wedge-first gate before scoring

Three software candidates were checked. Only the narrowed retained candidate receives a numerical score; rejected candidates are not rescued by easy implementation.

### 1. CohortTail — narrowed and retained

**Wedge-first line:** MSP backup operator explaining a confirmed same-account minimum-duration cutover → WACM usage/invoice exports, support, VISE and a prepared cohort worksheet → those tools already report and model most costs; whether reconstructing old-versus-new cohort assumptions is still burdensome is unverified → a dated scenario that preserves original policy per upload cohort and keeps missing historical ages unknown → a worked “why the bill did not drop immediately after a 90-to-30-day change” example for Veeam/Wasabi operators, shared through relevant maintainer or partner channels only where invited → a fresh cost-planning discussion and explicit current policy text justify validation, not a claim of a newly introduced billing change.

- **Direct competitors:** VISE for scenario modeling; native WACM for observed utilization, export and billing explanation. Neither is dismissed as a simplistic capacity-times-price tool.
- **Indirect substitutes:** a prepared upload-cohort worksheet, account-specific support explanation and a partner's existing quotation process.
- **Status quo:** review provider exports, confirm terms and explain the distinction manually. Financial planning matters, but no measured weekly time burden or erroneous invoice was established.
- **Gate result:** reject generic comparison, reporting and automatic retention optimization. Retain only a policy-effective-date/cohort hypothesis; feature absence in competitors has not been demonstrated, so wedge credit stays low.
- **Kill condition:** native exports plus a worksheet explain the same scenario at equal or less total effort, or an existing estimator can handle it with a small fixture/configuration addition. Prefer that contribution.

### 2. AddOnOverlap — rejected before scoring

**Wedge-first line:** M365 renewal owner reviewing newly bundled capabilities → CoreView duplicated-plan reports, Microsoft's packaging notice and licensing-partner review → a fresh vendor-authored reminder shows renewal questions, not failure of these substitutes → proposed offline add-on-overlap review is already a documented product capability → exact renewal examples for M365 licensing administrators → the July 2026 packaging/pricing rollout is relevant context, not a new November deadline or a defensible gap.

- **Signal:** [M365 price increase: which plans changed](https://www.reddit.com/r/sysadmin/comments/1xpw13k/microsoft_365_price_increase_which_plans_went_up/), posted today. The author explicitly sells licensing help; this is commercially interested timing/context evidence, not an independent customer request.
- **Direct functional competitor:** [CoreView Optimization Center](https://help.coreview.com/en_US/understanding-the-optimization-center) explicitly documents a **Duplicated plans** tab for overlapping service plans, license combinations and management actions.
- **Platform substitute:** [Microsoft's official FAQ](https://www.microsoft.com/en-us/licensing/news/2026-M365-Packaging-Pricing-Updates-FAQ) separates packaging rollout from pricing at renewal and says qualifying SKUs receive features regardless of agreement term. Actual account entitlement and contract cancellation rights still require verification.
- **Indirect substitute / status quo:** native license exports, a prepared renewal worksheet and a licensing partner's review. Removing an assignment is not necessarily cancellation of a purchased subscription or immediate cash savings.
- **Wedge and kill:** overlap detection and a prettier renewal report are insufficient against existing functionality. Reject without an independently observed unmet workflow; do not infer that an apparently overlapping add-on can safely be removed or canceled.

### 3. ArchAccessTrial — rejected before scoring

**Wedge-first line:** small-business IT owner evaluating remote access across Apple Silicon, Windows ARM and x86-64 → BeyondTrust/RustDesk platform documentation, incumbent trials and a test worksheet → the source reports a current supplier's missing native builds, not an industry-wide absence → proposed architecture-and-session trial ledger adds little to a prepared test plan → specific Windows-on-ARM support discussions → a fresh evaluation request, but no demonstrated recurring evaluation burden.

- **Signal:** [Cross-platform remote access for small business](https://www.reddit.com/r/sysadmin/comments/1xpuvn8/goto_crossplatform_remote_access_for_small/), posted today. Visible replies recommend existing products and explicitly distinguish native builds, session roles, sleep/wake and unattended reboot behavior.
- **Direct substitutes:** [BeyondTrust's platform matrix](https://docs.beyondtrust.com/rs/docs/supported-platforms) differentiates customer clients, Jump Clients and representative consoles; [RustDesk's client documentation](https://rustdesk.com/docs/en/client/) covers desktop/mobile clients and explicitly says iOS cannot be remotely controlled. Broad platform support is not independent proof of a native ARM build or successful unattended reboot on a specific release.
- **Indirect substitute / status quo:** trial the actual client/host combinations, record outcomes in an existing acceptance worksheet and choose a supported product. The request is primarily vendor selection; building another remote-access engine is not a one-to-three-day MVP.
- **Wedge and kill:** reject the trial-ledger app unless multiple operators demonstrate repeated evidence-management work that the worksheet cannot handle. No cross-platform session or architecture support was tested; no blanket winner is recommended.

## Problem

Minimum billing duration, backup retention, Object Lock and invoice periods are different clocks. A confirmed account policy change can leave older uploads governed by their original duration. A support explanation that applies the new number to every object can create an unjustified expectation of immediate savings.

This is a real documented semantic boundary, not a proven recurring buying problem. It may need only an example added to an existing worksheet or estimator.

**Status-quo pain test:** the fresh discussion concerns a consequential storage budget and recovery decision, and older questions explicitly show cost-calculation difficulty. That supports a financial-planning risk worth investigating. It does not establish lost money, an incorrect bill, more than 30 minutes per week of work, or that the narrowly proposed app beats the available manual workflow. Do not convert a provider-selection question into evidence that the cohort app is demanded.

## Target user

An authorized MSP backup operator with confirmed account terms, an effective policy-change timestamp, and permission to use sanitized exports or declared planning assumptions. Initial scope is a confirmed minimum-duration change within Pay-Go, not a Pay-Go-to-RCS contract migration. An account without confirmed terms cannot receive a definitive savings forecast.

## MVP scope

Proposed software only; **not implemented, account-tested or invoice-reconciled in this run**:

1. An offline CLI with an escaped HTML scenario view. Accept a small explicit CSV/JSON schema for supplied upload cohorts, bytes, upload date, declared deletion date or interval, effective policy timeline, source/provenance and units. No credentials, live bucket access or arbitrary archive ingestion.
2. Keep an object's original minimum-duration policy when a later policy takes effect. Show separate old-policy and new-policy cohorts; retain unresolved policy-effective times and unknown birth/deletion dates rather than assigning convenient values. A supplied timestamp is not automatically proof of original upload time.
3. Show scenario active storage and remaining minimum-duration billing exposure separately. Timed Deleted Storage is a billing concept, not a recoverable recycle bin. Object Lock/legal holds and backup references can prevent the assumed deletion; an operator-declared deletion scenario is not authorization to perform it.
4. Allow supplied native historical usage exports as **observed end-of-day context**, with a declared account/sub-account scope and export range. Do not infer object ages, actual deletions or a unique cohort history from aggregate counters. Missing days, timezone boundaries, mixed account scopes and units remain explicit uncertainty. With no cohort history, produce only declared scenarios, not an alleged reconstruction of the actual bill.
5. Export assumptions, provenance, policy dates and a sensitivity comparison. Any monetary view requires supplied account-specific rates, units, billing convention and confirmed cycle boundaries; otherwise show capacity-time exposure without an exact-money total. Keep tax, credits, support, account minimum allocation and unrelated services explicitly outside an incomplete model, not silently zero. A policy change can split billing cycles, so calendar-month buckets do not establish invoice totals.

**Boundary:** no bucket/version/object deletion, retention shortening, Object Lock changes, account-plan changes, recovery probes or recommendations to weaken protection to reduce spend. Do not simulate Veeam object lifecycle from weekly-full counts; actual block reuse, generation and lock extension require a separately validated version-specific model, already offered by existing tools. No automatic RTO, restore-throughput or provider-reliability claims. “Lower modeled cost” does not mean an acceptable recovery design. Keep sensitive customer identifiers out of shareable output; local processing alone is not anonymization.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct functional competitor | [Rack2Cloud VISE](https://www.rack2cloud.com/veeam-immutable-storage-cost-estimator/) | Already local, deterministic, day-level and scenario-based, with minimum-duration effects and exports. Its readable page is not a hands-on validation of every scenario; do not claim a missing cutover feature from limited inspection. |
| Native functional substitute | [WACM consumption exports](https://docs.wasabi.com/docs/access-consumption-data) and [invoice views](https://docs.wasabi.com/docs/invoices) | Already supplies active/deleted storage history, export and calculated billing components. Existing native functionality defeats a generic dashboard or rebilling pitch. |
| Authoritative explanation substitute | [Wasabi policy documentation](https://docs.wasabi.com/docs/how-does-wasabis-minimum-storage-duration-policy-work) plus account support | Already states the pre-/post-change object rule and billing-cycle reset. A worked support example may solve the entire problem. |
| Indirect substitute | Prepared cohort worksheet plus native exports | Can apply the same dated rules without another app. Comparison must include acquiring/cleaning inputs and obtaining policy confirmation. |
| Adjacent substitute | Existing backup-provider sizing and quotation process | Version-specific object behavior matters more than a nominal retention multiplier. A storage estimate cannot establish the overall backup solution's price or safety. |
| Status quo | Confirm account terms, read native reports, seek provider/partner support | Plausibly sufficient for an infrequent cutover. Fresh thread replies reporting satisfactory services are counterevidence to replacement demand. |

## Wedge

The only retained hypothesis is **a policy-cutover scenario that preserves upload-cohort rules while visibly refusing to reconstruct unavailable history**. It is not a new provider comparison engine, invoice auditor or backup optimizer.

Offline execution, scenario comparison and active-versus-billed capacity are already available. The narrow cutover explanation might be an existing-tool enhancement rather than a company. Its incremental value must be measured against a prepared worksheet and current native reporting, not against an empty spreadsheet or a simplistic calculator.

**Distribution hypothesis:** publish a worked, explicitly synthetic old/new upload example targeting the exact minimum-duration cutover question; offer a fixture or explanatory contribution to relevant Veeam/Wasabi maintainers or partner educators only where invited. No unsolicited sales replies or DMs. Specific communities and search terms are known, but recurring access/adoption is not demonstrated, so this is 3/5, not 4/5.

## Kill condition

Reject the standalone app if any condition holds:

- WACM exports, account support and a prepared cohort worksheet explain the transition with equal or less complete workflow effort.
- VISE or another existing tool handles the case directly, or can do so with a small fixture/configuration or documentation contribution.
- Three relevant operators cannot supply recurring explanation cases, or fewer than two meet a provisional 30% reduction in acquisition-plus-explanation time with no increase in incorrect savings or invoice claims. This is a proposed validation bar, not a measured result.
- Useful output depends on reconstructing nonexistent object history from end-of-day totals, assuming negotiated terms, treating backup retention as deletion time, or presenting a scenario as invoice verification.
- Operators confirm the documentation/support explanation is sufficient for this infrequent change, or no repeatable first-user channel emerges.

## Scoring

Assigned only after competitor checks and narrowing.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Consequential storage budgeting and repeated historical questions justify investigation; no direct evidence of recurring cutover-app demand or measured losses. |
| Feasibility | 4/5 | A small explicit-cohort scenario view is feasible in one to three days. Exact invoice reconstruction and a Veeam lifecycle engine are excluded; acquisition/schema uncertainty remains. |
| Demo potential | 4/5 | Synthetic old/new cohorts can show why a change does not rewrite historical terms. No runnable demo was built today. |
| Distribution | 3/5 | Exact Veeam/Wasabi operator channels and an example-led strategy exist, but repeatable access or adoption has not been shown. |
| Competitive wedge / timing | 2/5 | Fresh planning question and clear policy semantics; strong native reporting and an existing local simulation tool leave the incremental wedge unvalidated. |
| Total | 17/25 | Below 18/25, with Distribution and competitive-wedge dimension gates also failing. |

## Decision

**Idea-only. No dedicated project repo created.** CohortTail is the strongest retained hypothesis among today's three candidates, not a validated product or a recommendation to migrate storage. Weakest dimension: competitive wedge/timing at 2/5. Distribution is 3/5.

The evidence supports a bounded comparison of explanation workflows. It does not establish an incorrect invoice, automatic eligibility for a shorter minimum duration, recoverability of deleted data, immediate cash savings or a provider-wide reliability problem. An older Veeam community article describes a support-request route to shorter terms; verify current account eligibility instead of treating that historic offer as guaranteed.

The existing index continues at Day 102 without renumbering earlier entries. No scheduling configuration was changed.

## Next build step

If pursued, make one validation-sized fixture commit: an explicitly synthetic pre-/post-policy-change cohort file, an unknown-history variant, and expected output distinguishing scenario exposure from observed native usage. Include a prepared cohort worksheet and compare against WACM reporting, provider explanation and VISE with three relevant operators. Require the time-and-correctness bar before building; prefer an existing-tool fixture or documentation contribution if sufficient. No customer outreach, account access or billing-policy mutation occurred today.

Follow-up is tracked in Beads (`apps-4j1`).

## Source access caveats

- Canonical `reddit-readonly find` requested six recent posts each from r/sysadmin, r/selfhosted and r/webdev within 48 hours. r/sysadmin JSON was blocked with HTTP 403/theme-beta, but RSS returned six posts. RSS score/comment-count placeholders are not engagement evidence.
- The same probe reported r/selfhosted and r/webdev JSON/RSS unavailable with HTTP 429. No tight retries. Reddit-constrained web fallback returned an older selfhosted backup discussion and no fresh webdev result; neither was promoted to fresh evidence.
- Web extraction recovered all three shortlisted Reddit post bodies and visible comments. Collapsed replies were not exhaustively fetched; no claim of complete discussion coverage or measured consensus is made.
- `xurl whoami` succeeded using existing authentication, but read-only search returned HTTP 401 Unauthorized. No OAuth2 user was configured, so no interactive login or credential change was attempted. X-constrained web fallback returned a vendor profile rather than a relevant dated post; no X validation is claimed.
- Wasabi, Veeam, Microsoft, CoreView, RustDesk, BeyondTrust and Rack2Cloud bodies were readable. Competitor capabilities are documentation claims, not hands-on acceptance-test results. The estimator page's illustrative defaults were not adopted as real customer data or validated calculations. Source-access success does not prove feature absence elsewhere.

## Repository verification caveat

The existing repository-wide snapshot verifier still fails with `KeyError: 'source_commit'`, tracked separately in Beads (`apps-mq0`). No snapshot or verifier code changed in this run. Daily brief/index consistency, JSON and focused public-safety checks are verified separately; the repository-wide suite must not be described as green.
