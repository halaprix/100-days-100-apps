# Day 101 — EnrollContrast

Date: 2026-11-06
Status: idea-only

## One-line pitch

An offline app that compares time-stamped Windows hybrid-enrollment evidence, separating the configured credential policy from what a particular enrollment attempt reported before an administrator considers destructive cleanup.

## Research brief

- **Decision:** retain an attempt-to-policy comparison hypothesis; reject another enrollment collector, generic endpoint scanner or automatic repair tool.
- **Target customer:** a small Windows endpoint team investigating a single hybrid-joined workstation that will not enroll in Intune while peers do.
- **Geography:** English-language organizational IT; no legal or compliance certification.
- **Substitute set:** Microsoft's MDM diagnostic bundle and troubleshooting checklist, DSRegTool, Intune Debug Toolkit, a prepared PowerShell event filter and a comparison worksheet.
- **Time horizon:** a one-to-three-day offline comparison MVP only after benchmarking the existing workflow.
- **Must-answer question:** can an attempt-scoped comparison prevent incorrect joins between current policy, older events and another enrollment record at less total effort than existing tools?
- **Evidence bar:** one fresh detailed incident, current original platform/tool documentation and a separately authored troubleshooting article. No endpoint access, interviews, measured savings, prepayments or defensible market-size estimate.
- **Creative constraint:** “Subtract” — remove collection, enrollment triggers and remediation; retain a small evidence comparison with explicit unknowns.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Fresh public operator report; RSS discovery, complete post recovered through thread RSS, visible HTML comments read | [At my wit's end trying to enroll one laptop in Intune](https://www.reddit.com/r/sysadmin/comments/1xp676n/at_my_wits_end_trying_to_enroll_one_laptop_in/) | Posted 2026-11-06 at 06:49 UTC. Author reports hours of investigation: GPO says User Credential, registry shows `UseAADCredentialType = 1`, but supplied attempt messages say Device Credential and return `0x80180018`; peers enroll successfully. These are reported observations, not a reproduced policy-engine defect or independently verified license state. |
| Original native collection documentation | [Collect MDM logs](https://learn.microsoft.com/en-us/windows/client-management/mdm-collect-logs) | The native bundle already includes policy/certificate summaries, detailed enrollment configuration, registry dumps, collection metadata and event logs. A new collector or prettier support ZIP has no demonstrated wedge. |
| Original native troubleshooting documentation | [Group Policy auto-enrollment troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/mem/intune/device-enrollment/troubleshoot-windows-auto-enrollment) and [diagnose enrollment](https://learn.microsoft.com/en-us/windows/client-management/mdm-diagnose-enrollment) | Microsoft already distinguishes enrollment success/failure events from task triggering. Task Scheduler event 102 does not establish enrollment success. Its error table identifies `0x80180018` as a user-license error and `0x8018000A` as already enrolled; neither code alone determines why the reported credential path was selected. |
| Original configuration and interpretation documentation | [Group Policy enrollment](https://learn.microsoft.com/en-us/windows/client-management/enroll-a-windows-10-device-automatically-using-group-policy) and [dsregcmd interpretation](https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd) | Device Credential has documented Intune scenario restrictions. `dsregcmd` user/SSO fields require the relevant user context; populated MDM URLs do not prove management. These boundaries matter more than a generic red/green readiness score. |
| Existing community software; original maintainer documentation | [Intune Debug Toolkit](https://msendpointmgr.com/intune-debug-toolkit/) and [DSRegTool](https://learn.microsoft.com/en-us/samples/azure-samples/dsregtool/dsregtool/) | Existing tools already provide extensive diagnostics, collection, policy-result views, event viewing and registration checks. The toolkit documents a free MIT-licensed launcher; competing on low price or “all logs in one place” is not credible. Capabilities were read, not hands-on tested. |
| Independent practitioner article; older publication with a recent stated revision, not a new customer interview | [Intune auto-enrollment troubleshooting](https://blog.infostruction.com/2024/02/13/the-trials-and-tribulations-of-intune-auto-enrollment-tips-and-tricks/) | Article states an update on 2026-11-03 and explicitly warns against clearing everything, distinguishes credential paths and already offers inventory-first, one-ID cleanup preview. It supports recurring diagnostic complexity but is strong counterevidence to a new cleanup/preflight wrapper. The article says its revised cleanup was not live-endpoint tested in that refresh. |

**Confidence:** medium that difficult enrollment incidents consume consequential administrator time; low that this particular comparison deserves a separate product. The incident author already assembled a detailed report, which is counterevidence to a packaging-only app. No source establishes recurring demand for cross-export comparison itself.

## Shortlist: competitor and wedge-first gate before scoring

Three software candidates were checked before assigning the retained candidate's score. Rejected candidates receive no numerical score.

### 1. EnrollContrast — narrowed and retained

**Wedge-first line:** endpoint administrator with one hybrid-enrollment outlier → native MDM bundle, Microsoft checklist, DSRegTool and Intune Debug Toolkit → a fresh incident contains a reported policy-versus-attempt discrepancy, but does not prove those tools fail → compare supplied evidence by capture time, user context and identifiable attempt, preserving unmatched or stale observations → an exact worked “User Credential configured, Device Credential reported” example and reusable fixture for endpoint troubleshooters, offered through relevant maintainer discussions only where invited → today's unresolved incident and the separately revised practitioner guide justify a bounded validation test, not a new platform-regression claim.

- **Direct functional competitors:** native MDM reporting and diagnosis; Intune Debug Toolkit's policy and log views; DSRegTool for adjacent registration prerequisites. Their documented breadth is the baseline.
- **Indirect substitutes:** an event XML filter, side-by-side native reports, a prepared worksheet and an existing Microsoft support case.
- **Status quo:** inspect the same artifacts manually, seek support or reimage under an approved recovery plan. The author reports hours of unsuccessful troubleshooting, but no weekly recurrence or quantified savings.
- **Gate result:** reject collection, automatic repair, stale-record deletion and a general health score. Retain only the specific comparison hypothesis. The tools' documentation does not establish that this comparison is absent, so wedge credit remains low.
- **Kill condition:** a prepared native filter/report comparison is as clear and fast, or existing-tool maintainers can provide the same result through a small fixture or documentation change. Prefer that contribution over a standalone app.

### 2. PhoneFreePilot — rejected before scoring

**Wedge-first line:** M365 administrator supporting workers without usable personal smartphones → native passkey deployment guidance, authentication reporting, employer-issued security keys and a rollout worksheet → a fresh question shows method and procurement confusion, not failure of those substitutes → proposed phone-free enrollment-planning app overlaps this index's PasskeyPilot bet → persona-specific onboarding examples for frontline-IT teams → Microsoft documents a February 1, 2027 retirement milestone for most in-scope users, but a deadline alone is not differentiation.

- **Signal:** [SMS go bye bye oh no!](https://www.reddit.com/r/sysadmin/comments/1xozimp/sms_go_bye_bye_oh_no/), posted today. Visible replies discuss staff without compatible phones and employer-funded keys. Do not repeat commenters' jurisdiction-specific employment-law assertions as verified facts.
- **Direct substitutes:** Microsoft's [retirement guidance](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-sms-voice-retirement) and [persona-based deployment guide](https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-deploy-phishing-resistant-passwordless-authentication) already cover migration planning, local/portable credentials and device readiness. The guide links a readiness workbook. Existing [policy-scope scanner](https://github.com/microsoft/entra-sms-voice-usage-analyzer) exports policy targets; its README explicitly says it is not a user inventory or actual-usage report.
- **Indirect substitute / status quo:** issue approved hardware, use the existing onboarding/helpdesk process, and pilot supported methods with the actual tenant/device/browser combination. A registered method is not proof of a successful operational sign-in.
- **Wedge and kill:** reject a new planning/reporting app without evidence of an unsolved workflow; route any future validated addition to PasskeyPilot. The poster says “end of February,” while official guidance says **February 1, 2027** for most users and **July 1, 2027** for Global Administrators and external users; preserve that discrepancy. The policy scanner's shorter timeline does not override the official cohort-specific notice. No tenant rollout or browser compatibility was tested.

### 3. BranchPowerMap — rejected before scoring

**Wedge-first line:** IT operator responsible for dispersed equipment at unattended branch sites → NetBox power modeling, vendor management and a local installation survey → the source's main obstacle is physical distribution and safe installation, not missing topology software → proposed software-only outlet-map app cannot remove the cabling or installation constraint → branch-operations documentation examples → a fresh multi-site question, with no software-specific buying signal.

- **Signal:** [UPS/PDU & MDF Power Layout](https://www.reddit.com/r/sysadmin/comments/1xoyys1/upspdu_mdf_power_layout/), posted today. Author describes many branch sites, working centralized setups at newer sites, and problematic dispersed legacy UPS arrangements. Visible replies suggest alternative equipment and electrical installation approaches.
- **Direct functional competitor:** [NetBox power tracking](https://netbox.readthedocs.io/en/stable/features/power-tracking/) already models panels, feeds, PDUs, ports/outlets and redundant topologies, including traditional non-datacenter environments.
- **Indirect substitute / status quo:** a documented site survey, vendor console and qualified local installation review. A software map does not establish electrical-code compliance or make a proposed cable arrangement safe.
- **Wedge and kill:** reject the app; the stated pain is real but the software gap is unproven. Do not turn it into a physical gadget/sourcing bet or another ChainBreak dependency-map project. No wiring recommendation or remote power action was made.

## Problem

A report captured now can show a policy value while a failed attempt reflects an earlier state, another identity context or a different enrollment record. Treating every line in a support bundle as simultaneous evidence can lead to an unjustified “Windows ignored policy” conclusion or broad cleanup that destroys useful context.

The fresh report describes this kind of apparent contradiction, not its cause. It supplies no independently acquired export bundle or paired control-device evidence. The app must help inspect the claim, not certify it.

**Status-quo pain test:** the author explicitly reports hours of work and a workstation that remains unmanaged. That supports material operational delay and a management gap, not a verified security incident or more-than-30-minutes-per-week measurement. Existing reports may already make review tolerable; that must be tested before building.

## Target user

An authorized endpoint troubleshooter who can obtain approved working-copy exports from a failing hybrid-joined Windows device and, where practical, a comparable successful device. Not an end user seeking to bypass enrollment, a fleet-monitoring replacement, or an operator needing an automatic reset.

## MVP scope

Proposed software only; **not implemented or endpoint-tested during this research run**:

1. An offline CLI and escaped HTML report over an explicit, allowlisted working-copy file set: event XML, relevant policy export, task metadata and `dsregcmd /status` text. Start with documented formats and retain unknown/unparsed fields. No arbitrary archive extraction, execution, live collection or tenant authentication.
2. A capture manifest with supplied timestamps, timezone, Windows build, collection user/elevation, evidence origin, scope and operator-declared device mapping. Capture context is a declaration unless the supplied artifact establishes it. Preserve unavailable, filtered, truncated and uncollected evidence separately from a negative result.
3. Separate columns for intended policy, observed policy at capture and credential text reported by a particular enrollment attempt. Preserve the literal `UseAADCredentialType = 1` from the source; do not assign its numeric semantics without the matching policy definition. The source's literal `/Enrollment` channel is not silently rewritten to Microsoft's documented `/Admin` channel.
4. Link events only when supplied identifiers and context support the relationship. Use correlation/record identifiers where available; proximity in time alone is not proof. Show ambiguity when events, user, enrollment GUID or capture ordering cannot be matched. A later snapshot cannot prove the effective policy at an earlier attempt. A successful control device is a comparison, not a causal experiment.
5. An evidence-backed discrepancy view with exact source references and unresolved questions. Keep local enrollment state, Entra join state and Intune service management/check-in evidence distinct. Neither populated MDM URLs nor Task Scheduler completion means enrollment succeeded. Absent success events in a bounded export do not prove no successful enrollment occurred.

**Boundary:** no registry/certificate/task deletion, `dsregcmd /leave`, forced policy refresh, enrollment retry, permission changes or security-policy exclusions. Do not execute cleanup suggestions from public comments. Some visible replies contain mistaken identity terminology or indiscriminate reset instructions; they are not authoritative remediation. Reading supplied exports does not make upstream acquisition privilege-free. Do not ingest whole DSRegTool bundles indiscriminately: documented outputs can contain sensitive device, environment and token material. Keep originals restricted, produce separately reviewed shareable derivatives, and do not claim that an offline report or hash anonymizes them.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct functional competitor | Windows MDM diagnostic report and Microsoft checklist | Already captures policies, certificates, registry and event context. This is the mandatory baseline, not an alleged missing feature. |
| Direct functional competitor | Intune Debug Toolkit | Existing free toolkit documents collection, policy-result views, MDM event viewing and other diagnostics. A contributor fixture or view may be preferable to another product. |
| Adjacent diagnostic substitute | DSRegTool | Extensive join/PRT/registration checks and log collection. It is not interchangeable with proof that Intune enrollment succeeded. |
| Indirect substitute | Prepared event filter plus native reports and worksheet | Can correlate the same handful of artifacts without a new app. Include acquisition and redaction effort in comparison timing. |
| Indirect substitute | Updated practitioner checklist and inventory-first cleanup preview | Already discourages blind reset and narrows cleanup selection. A cleanup wrapper is not a credible wedge; no cleanup is in this MVP. |
| Status quo | Existing support workflow, manual review or approved reimage | May be rational for one exceptional laptop. A single difficult incident does not establish repeat use or willingness to pay. |

## Wedge

The possible addition is **attempt-scoped evidence comparison that refuses invalid temporal and identity joins**, not faster collection, root-cause diagnosis or safer automatic deletion. The product hypothesis is that a small outlier comparison could reduce interpretation errors before support escalation.

That distinction is precise but unvalidated. Native reports, existing tool views and a prepared worksheet may already be sufficient. The author already wrote a detailed support report; repackaging it adds little. Build only if actual troubleshooters repeatedly need this comparison and existing-tool maintainers cannot solve it with a small change.

## Kill condition

Reject the standalone app if any condition holds:

- Native reports plus the official checklist and a prepared event filter/worksheet deliver equivalent clarity at equal or lower complete workflow effort.
- Three relevant endpoint operators cannot supply recurring cases, or fewer than two achieve a provisional 30% reduction in acquisition-plus-review time without more incorrect causal or enrollment-success conclusions. This is a proposed target, not a measured result.
- Meaningful comparison requires unbounded sensitive-bundle ingestion, unsupported policy-value assumptions, mandatory tenant-wide permissions or automatic cleanup.
- Missing attempt identifiers, context or capture ordering routinely prevent useful comparison. Do not manufacture certainty to improve the demo.
- The useful output is a maintainer fixture, report view or troubleshooting recipe rather than a standalone product, or distribution remains limited to one support thread.

## Scoring

Assigned after competitor checks and narrowing; no score rescues rejected candidates.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Hours of reported troubleshooting and a management-blocking outlier justify investigation; repeat comparison demand is unverified. |
| Feasibility | 4/5 | Small offline XML/text comparison is plausible in one to three days; schema, locale, time/context handling and incomplete artifacts limit confidence. No universal EVTX parser or live collector is included. |
| Demo potential | 4/5 | A current-policy/older-attempt mismatch is understandable with synthetic fixtures; no running demo exists today. |
| Distribution | 3/5 | Endpoint troubleshooters and an exact worked example identify a channel hypothesis, but recurring access or adoption is unproven. A named community alone does not earn 4/5. |
| Competitive wedge / timing | 2/5 | Fresh incident and a recent practitioner update are timely; native diagnostics and active community tools are strong, and no missing comparison feature has been demonstrated. |
| Total | 17/25 | Below 18/25; Distribution and competitive-wedge dimension gates also fail. |

## Decision

**Idea-only. No dedicated project repo created.** EnrollContrast is the strongest retained validation hypothesis from this run, not a confirmed product opportunity or a diagnosis of the source incident. Weakest dimension: competitive wedge/timing at 2/5. Distribution is 3/5. Do not create another endpoint diagnostic repository on this evidence.

The evidence supports testing interpretation continuity before destructive recovery. It does not support claims that Windows ignores the configured policy, that licensing is correctly configured in the actual tenant, that a reported enrollment record is stale, or that a new app would resolve the failure. No pricing or willingness-to-pay evidence was gathered.

The requested daily run continues the existing index at Day 101; earlier day numbers and the hundredth-bet milestone are preserved. No scheduling or project-scope configuration was changed.

## Next build step

If pursued, make one validation-sized fixture commit: three synthetic cases covering a genuine reported discrepancy, an event predating a policy capture, and a different enrollment identity, plus a prepared native filter/worksheet and expected unknown-aware output schema. Compare against native MDM reporting, Microsoft's checklist and the existing toolkit with three relevant operators. Require two to meet the time-and-correctness target before building; prefer an existing-tool contribution or recipe if sufficient. No outreach or endpoint action occurred in this run.

Follow-up is tracked in Beads (`apps-g9f`).

## Source access caveats

- Canonical `reddit-readonly find` requested eight recent posts each from r/sysadmin, r/selfhosted, r/webdev and r/androidapps, within 48 hours. JSON was blocked with HTTP 403/theme-beta for r/sysadmin and r/androidapps; their RSS feeds each returned eight posts. RSS score/comment-count placeholders are not engagement evidence.
- The same probe reported r/selfhosted and r/webdev JSON/RSS unavailable with HTTP 429. No tight retry loop. Date-constrained and broader Reddit web searches were attempted; no additional fresh demand evidence was recovered from those communities. Older webdev deployment results were not used as current signals.
- The canonical Intune thread JSON request returned HTTP 403. HTML recovered the post and visible comments, and a single thread-RSS request recovered the complete post. Old Reddit required login and was discarded. Collapsed comments were not exhaustively retrieved.
- `xurl whoami` succeeded with existing authentication, but read-only search returned HTTP 401 Unauthorized. No OAuth2 user was configured; no browser login or credential change was attempted. X-constrained web fallback returned no results for the enrollment query. No X validation is claimed.
- Original Microsoft, NetBox and toolkit documentation bodies were readable. Microsoft Learn's generic authorization banners appeared alongside the readable article text. Documentation and practitioner claims were not tested on endpoints. Search gaps do not establish competitor feature absence.

## Repository verification caveat

The existing repository-wide snapshot verifier still fails with `KeyError: 'source_commit'`, tracked separately in Beads (`apps-mq0`). No snapshot or verifier code changed in this run. Daily brief/index consistency, JSON and focused public-safety checks are verified separately; the repository-wide suite must not be described as green.
