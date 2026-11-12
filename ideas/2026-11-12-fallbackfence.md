# Day 106 — FallbackFence

Date: 2026-11-12
Status: idea-only

## One-line pitch

A local CLI that compares a proposed BIOS-password fallback-version window with the fleet's last reported states before an endpoint engineer publishes the next ConfigJon Intune remediation package.

## Research brief

- **Decision:** retain one narrow software hypothesis or create a project only if the evidence and dimension gates justify it.
- **Target customer:** endpoint engineers already operating versioned ConfigJon BIOS-password remediations on Dell/HP Windows devices; not every BIOS administrator.
- **Geography:** no geographic dependency; English-language technical distribution first.
- **Substitutes:** native Intune exports, ConfigJon scripts/reporting, OEM management and a prepared PowerShell/Excel join.
- **Time horizon:** a 1–3 day offline comparison MVP, not a new firmware agent or credential vault.
- **Must answer:** is deciding which old versions to retain repeatedly difficult after using the existing reports? Can an offline comparison reduce total preparation and review effort without claiming it verifies credentials?
- **Evidence bar:** original documentation plus public operator requests; no invented interviews, fleet measurements or willingness to pay.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Fresh public operator request, 2026-11-12; discovered through RSS, full post and visible replies retrieved through web extraction | [Dell/HP centralized BIOS passwords](https://www.reddit.com/r/sysadmin/comments/1xu6ysr/centralized_bios_password_management_and/) | Requests unique passwords, MECM deployment, encrypted storage, periodic rotation, reporting and handling offline/failed rotations without losing existing credentials. Replies identify HP Sure Admin and Dell Intune integration: strong counterevidence to building another general manager. The author does **not** say they use ConfigJon or request this proposed preflight. |
| Older public operator discussion, 2022-12-06; historical corroboration, not fresh validation | [BIOS Passwords?](https://www.reddit.com/r/sysadmin/comments/zealck/bios_passwords/) | Asks for scalable management beyond scripts; a reply distinguishes writing Dell rotation scripts from reliable deployment/compliance reporting. The author's takeaway is vendor tooling plus scripts. This establishes a longstanding operational job, not current unmet demand for this app. |
| Original implementation documentation, updated 2026-09-29 | [ConfigJon password management](https://www.configjon.com/intune-bios-password-management/) | Documents target versions, rolling payload windows, recovery, missing markers and failure when no retained version unlocks a device. Existing recovery is a substitute, not a missing feature. |
| Original implementation reference | [ConfigJon troubleshooting](https://www.configjon.com/intune-bios-reference/) | Firmware reports whether a password is set, not which version. Markers record script state. The reference already explains missing-payload versions, devices beyond the recovery window and the trade-off with package size. |
| Original implementation reporting documentation | [ConfigJon reporting](https://www.configjon.com/intune-bios-reporting/) | Already supplies local logs, status lines, CSV export, Graph run states and optional Log Analytics reporting. Export-plus-script is a serious baseline; collecting or rendering the same data is not a wedge. |
| Original platform documentation | [Microsoft Intune BIOS configuration](https://learn.microsoft.com/en-us/intune/device-configuration/templates/configure-bios-windows) | Documents Dell per-device passwords, reporting, retrieval and external backup requirements. Unenrollment does not remove the BIOS password. This rules out positioning ordinary password escrow/reporting as novel. |
| Original OEM documentation | [HP Sure Admin](https://developers.hp.com/hp-client-management/blog/hp-sure-admin-step-step) | Offers certificate-based firmware authorization, Configuration Manager deployment through MIK/CMSL, and HP Connect for Intune. It can remove the password-rotation job on supported devices; it is not another password-version cohort. |

**Confidence:** medium that firmware credential lifecycle is a real operational concern; low that this narrow pre-publication comparison warrants a standalone product. The two community discussions are independent but separated by years. Documentation from several pages of one project is one evidence family, not several independent customer validations. No observed time saving or payment intent.

## Shortlist and wedge-first gate — before scoring

Constraint: **Automate the annoying thing**, using existing exports rather than creating another management platform. Four software candidates were checked; only the narrowed first candidate is retained for scoring.

### 1. FallbackFence — narrow and retain

**Wedge-first:** Engineer maintaining ConfigJon Dell/HP remediation packages → native device-status CSV plus a prepared PowerShell/Excel join → the engineer must still relate stale/missing fleet observations to the *next* package's retained versions; recurring cost is a hypothesis, not established failure → a metadata-only before/after fallback-window comparison → ConfigJon users reached through a reproducible fixture and exact-query technical guide about `pw-version-not-in-payload` and fallback-window planning, with maintainer-permitted sharing → a fresh offline/failed-rotation request and recently updated recovery documentation justify testing now, without a deadline claim.

- **Direct competitors/substitutes:** ConfigJon password management and reporting; Dell/Intune native management; HP Sure Admin changes the job rather than merely competing on UI.
- **Indirect substitute:** the existing CSV export plus a small join against an operator-maintained version list.
- **Status quo:** keep a wider fallback window or manually inspect lagging devices before changing it. This can be entirely adequate.
- **Pain test:** losing the usable recovery version is a credential-access risk. No source quantifies weekly time lost or reports an actual failed retirement in this specific workflow.
- **Gate:** reject the original broad mixed-OEM BIOS manager. Retain only the precise package-review hypothesis, with low wedge credit and no assumed repeatable access to users.
- **Kill condition:** native export plus prepared join solves the review adequately, operators do not regularly retire versions, or the proposed inputs cannot be acquired reliably without extra deployment work.

### 2. CreditCrashLab — reject

**Wedge-first:** Small API SaaS evaluating prepaid credits → [Flexprice](https://github.com/flexprice/flexprice), Lago and provider integration tests → suspected uncertainty about retries/overages is not evidence the tests fail → a proposed local failure-scenario runner → billing-project maintainers through upstream reproducible fixtures → [today's production-experience request](https://www.reddit.com/r/selfhosted/comments/1xu2u2u/best_open_source_billing_tools/), not a documented billing incident.

- **Direct substitute:** Flexprice's [existing integration suite](https://github.com/flexprice/flexprice/tree/main/integration-testing-suite/go) already includes wallet, billing, usage and invoice steps. This was inspected, not inferred absent.
- **Indirect/status quo:** a provider test deployment and prepared HTTP scenarios; the requester is already evaluating existing systems.
- **Pain test:** billing mistakes could lose money, but this post establishes uncertainty, not a recurring failure or missing test workflow. A visible moderation disclosure mentions AI use; no inference of independent customer validation follows from it.
- **Kill condition / decision:** no specific unsupported failure scenario established; reject before scoring. An upstream fixture is preferable to another billing platform or generic test wrapper.

### 3. ShelfLink — reject

**Wedge-first:** iPhone owner using Calibre Web Automated → Apple Books downloads, Readest or MapleRead → the author explicitly calls the current flow good → a proposed subscription-free integrated reader → CWA/iOS reader discussions → [a fresh recommendation request](https://www.reddit.com/r/selfhosted/comments/1xu6w3o/best_ios_epub_app_for_calibre_web/).

- **Direct substitutes:** a visible reply recommends Readest with CWA; [MapleRead](https://www.maplepop.com/web/mr/overview.php) documents Calibre exchange and no recurring subscription fees.
- **Indirect/status quo:** download the next EPUB into Apple Books and read it, which already satisfies this author.
- **Pain test:** no >30-minute weekly waste, financial loss or blocked reading demonstrated.
- **Kill condition / decision:** tolerable workaround and existing products; reject before scoring, not a new generic reader.

### 4. KmsPilot — reject

**Wedge-first:** Windows administrator piloting a CIS recommendation → Microsoft policy documentation plus a small GPO pilot → the source seeks deployment experience, not a missing inventory tool → a proposed offline activation-policy comparison → exact-setting technical search → [today's NoGenTicket question](https://www.reddit.com/r/sysadmin/comments/1xu6ovz/cis_turn_off_kms_client_online_avs_validation_any/).

- **Direct substitute:** [Microsoft Licensing CSP documentation](https://learn.microsoft.com/en-us/windows/client-management/mdm/policy-csp-licensing) explicitly maps `DisallowKMSClientOnlineAVSValidation`, policy name `NoAcquireGT` and registry value `NoGenTicket`; these identifiers have different roles and must not be conflated.
- **Indirect/status quo:** read the policy definition, use existing activation diagnostics, stage the GPO and observe a controlled pilot.
- **Pain test:** possible rollout risk, but no incident or repeated comparison burden is established. The policy description does not itself prove every requested Office/MAK/renewal scenario safe.
- **Kill condition / decision:** a documentation answer and pilot are sufficient until a repeatable unsupported workflow is demonstrated; reject before scoring. Do not mutate activation or claim a 180-day outcome from an immediate check.

## Problem

A finite password-version window deliberately excludes older versions. An engineer preparing a new package needs to know which assigned devices were last observed on a version that would disappear, and which devices have insufficient evidence to review at all.

The existing scripts already classify drift and try fallback recovery. Existing reporting already exposes those classifications. The possible gap is **prospective comparison of the proposed window against a complete declared fleet**, not recovery, vaulting, telemetry collection or proof that a specific credential works.

This is adjacent to the fresh MECM request, not an assertion that its author runs ConfigJon Intune remediations or would switch to this tool. A report for this niche does not supply the author's unique-per-device password generation, secure escrow or rotation requirements.

## Target user

An endpoint engineer already publishing ConfigJon version-window remediations for Dell/HP devices through Intune, with an exportable assigned-device inventory and a reason to remove older versions. Exclude HP Sure Admin devices, native Dell password management and unrelated task-sequence implementations from the initial adapter.

## MVP scope

A small Python CLI, initially one documented ConfigJon export format:

1. Read an operator-prepared, minimized assigned-device roster, run-state export and **non-secret** proposed manifest containing vendor, deployment/cohort identity, target version and retained version labels. Record capture times, declared scope and completeness limitations.
2. Join by stable device identifiers within the correct cohort, not display name or integer version alone. If the native CSV lacks a stable identifier or observation time, require an explicit supplementary mapping or report unresolved identity/freshness. No silent guessing.
3. Distinguish last-reported version retained, last-reported version omitted, missing/stale observation, marker-only/degraded, incompatible/out-of-scope, reset/password-not-set, and conflicting records. `TargetVersion = 0` is a separate clearing operation, not an ordinary retained version.
4. Show which devices move from retained to omitted under the proposed manifest. For missing markers, list uncertainty rather than concluding no available fallback can work. Unknowns remain visible even if observed devices all appear covered.
5. Produce local JSON/HTML review output and a nonzero review-required exit when omissions, input ambiguity or declared completeness gaps exist. Do not label a zero exit 'safe to rotate' or 'safe to delete'.

**Non-goals:** firmware queries, password attempts, reading/decrypting CMS payloads, parsing executable PowerShell to discover secrets, vault access, password backup or deletion, package deployment, live Graph collection, HP key provisioning and actual firmware writes. Use an operator-prepared version manifest rather than executing or importing a downloaded remediation script.

**Safety boundary:** a marker plus `IsPasswordSet` is an observation, not credential verification or proof of escrow/recoverability. A retained version label does not prove the matching ciphertext, certificate/private key or authorized retrieval path remains available. Keep that limitation explicit. No real credentials, serial numbers, primary-user data or device identifiers belong in public examples; local inputs and outputs may still be sensitive.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct workflow substitute | [ConfigJon management and reporting](https://www.configjon.com/intune-bios-password-management/) | Already implements rolling recovery, drift detection and readable output. Its [reporting guide](https://www.configjon.com/intune-bios-reporting/) provides CSV, Graph and optional Log Analytics. A separate viewer would duplicate it. |
| Direct native management substitute | [Dell BIOS configuration in Intune](https://learn.microsoft.com/en-us/intune/device-configuration/templates/configure-bios-windows) | Per-device passwords, status and retrieval are already documented. Not the same package format; do not pretend this app manages native Dell passwords. |
| Job-changing substitute | [HP Sure Admin / HP Connect / MIK](https://developers.hp.com/hp-client-management/blog/hp-sure-admin-step-step) | Signed firmware authorization can eliminate the password-window job on supported devices, including Configuration Manager deployment options. |
| Indirect substitute | Prepared PowerShell join or Excel/Power Query workbook | Compare the existing status export with an explicit cohort/version manifest. Benchmark against this, not an empty spreadsheet. |
| Status quo | Keep the old window and manually review exceptions | May be sufficient. Retaining old credentials also has exposure and package-size trade-offs; neither 'retain everything' nor 'delete all old versions' is a universal recommendation. |

No verified price advantage: these scripts/documentation are publicly accessible, while native/enterprise licensing and hardware eligibility vary. No paid-product pricing, TAM or purchase intent is asserted.

## Wedge

A single prospective operation: **'If this package stops carrying these versions, which last-known devices become review cases, and where is evidence missing?'**

That is narrower than the source's general manager request and does not require trusting a new tool with firmware credentials. The visible documentation makes the operation technically plausible but also makes a short native script a powerful competitor. The comparison gap and repeat usage are not validated.

Distribution experiment: an exact-workflow article with a reproducible synthetic fleet, plus a maintainer-approved example or contribution to the existing project. This is a concrete route to test, not an owned channel or permission to post; no social action was taken. Distribution remains 3/5 until users or a maintainer demonstrate repeatable access and interest.

## Kill condition

Kill the standalone app, or reduce it to an upstream recipe, if any of the following holds:

- Three relevant operators can perform the complete acquisition-plus-review workflow with the prepared export/join in roughly ten minutes per rollout and do not want another maintained tool.
- Operators do not regularly remove versions or already resolve this in native reporting/Log Analytics.
- Stable device/cohort identity, complete assignment scope or useful capture times require more integration effort than the comparison saves.
- A timed comparison does not materially improve correct identification of omitted/stale/unknown cases over the prepared native baseline; a proposed validation target is at least 30 minutes saved in a real rollout review, not a measured result.
- Achieving value requires passwords, decryption, firmware unlock tests or a claim of guaranteed recoverability. Those are a different, higher-trust product.

No kill threshold has been measured yet. These are validation criteria, not claimed outcomes.

## Scoring

Only the narrowed survivor is scored; rejected candidates do not receive reassuring numerical scores.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Credential-access risk is material and the source explicitly mentions offline/failed rotations. Recurrence for this particular package review remains unverified. |
| Feasibility | 4/5 | One offline format and an explicit non-secret manifest fit a 1–3 day prototype; ambiguous identity/freshness and schema variation must fail visibly. |
| Demo potential | 4/5 | A before/after window makes omitted and unknown devices obvious in a small fixture. This is a proposed demo, not an executed product. |
| Distribution | 3/5 | A named implementation community and exact-query guide exist, but no maintainer agreement, recurring acquisition channel or pilot users. |
| Competitive wedge / timing | 2/5 | Existing reports plus a prepared join may be enough; fresh request and September updates justify research, not a standalone-tool advantage. |
| Total | 17/25 | Below 18; Distribution and competitive-wedge gates both fail. |

## Decision

**Winner: FallbackFence, idea-only. No dedicated project repository or implementation created.**

The broad BIOS manager is rejected. Retain only this bounded comparison hypothesis. Strong substitutes are a reason to test an upstream recipe first, not to inflate the score. Nothing here certifies firmware access, escrow or a rollout's safety.

## Next build step

Prepare one synthetic cohort/window fixture and the equivalent native PowerShell/worksheet join, covering an offline old-version device, a missing marker, a reset, a mismatched cohort, a stale observation and an excluded Sure Admin device. Measure full acquisition and review effort with relevant operators before implementing a CLI or creating a repo. Track validation in Beads `apps-s1g`.

## Run verification

The daily JSON/index/brief consistency and public-safety checks are run separately from the repository-wide snapshot check. The latter still fails on the pre-existing `source_commit` provenance-schema mismatch tracked in Beads `apps-mq0`; this run does not change snapshots or claim the full repository suite is green.

## Source access caveats

- The canonical Reddit `find` probe encountered blocked public JSON (403/theme-beta); r/sysadmin returned public RSS. r/selfhosted and r/webdev were initially unavailable with 429. A later small `posts` probe recovered r/selfhosted through RSS; r/webdev still returned 429 and was not used as evidence. RSS score/comment placeholders are unknown, not zero engagement.
- Web extraction subsequently retrieved full selected Reddit posts and visible replies, including the winner's native-substitute recommendations. This improves context but is not exhaustive comment retrieval or proof of consensus. Reddit-constrained web search supplied the older corroborating discussion.
- `xurl whoami` succeeded using existing authentication; search returned **401 Unauthorized**. No OAuth2 user was configured, so no interactive authorization was attempted. A web search constrained to X produced no usable result. There is **no X demand validation** in this brief.
- Dell's linked support article was bot-blocked during extraction. Microsoft documentation and HP's original documentation were readable; the blocked Dell page is not used to establish feature absence.
- All actions on Reddit/X were read-only. No interview, benchmark, hardware test, credential test or app execution occurred during this research run.
