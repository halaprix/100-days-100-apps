# Day 100 — ConsentBrief

Date: 2026-11-05
Status: idea-only

## One-line pitch

A local-first app that helps nondeveloper automation makers prepare a revision-specific evidence appendix for an existing IT approval request, exposing unanswered data-flow and ownership questions without pretending to approve or security-scan the app.

## Research brief

- **Decision:** retain a narrow maker-to-reviewer handoff hypothesis, not another AI security scanner or consent-management platform.
- **Target customer:** a small Microsoft 365 IT team receiving custom, employee-built automation requests from nondevelopers; the maker fills the appendix and the existing technical reviewer evaluates it.
- **Geography:** English-language organizational IT; no jurisdiction-specific compliance claim.
- **Substitute set:** Entra admin consent requests, a prepared Jira Service Management or equivalent ITSM questionnaire, existing developer review, and supported low-code governance.
- **Time horizon:** one-to-three-day offline form/export/diff MVP only after a native-workflow benchmark.
- **Must-answer question:** does a revision-specific, unknown-aware appendix reduce total maker and reviewer back-and-forth compared with a well-prepared form attached to the native consent request?
- **Evidence bar:** one fresh public thread with another visible operator reporting recurrence, plus original platform and workflow documentation. No interviews, observed customer workflow, prepayments, measured savings or defensible market-size estimate.
- **Creative constraint:** “Subtract” — remove scanning, approval routing, tenant access and AI-generated answers; retain only explicit facts, unknowns and revision comparison.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Fresh public operator report; RSS discovery and HTML post retrieved | [User vibe coded enterprise apps](https://www.reddit.com/r/sysadmin/comments/1xo9fm3/user_vibe_coded_enterprise_apps/) | Posted 2026-11-05 at 04:21 UTC. Author describes repeated requests for employee-built automations with broad tenant access, where makers cannot explain storage, encryption or external APIs. This supports a handoff problem, not a demonstrated missing security-scanner capability. |
| Visible public reply in the same thread | [Another operator describes daily recurrence](https://www.reddit.com/r/sysadmin/comments/1xo9fm3/comment/19s5svpaoly6d/) | Commenter reports discovering tools after colleagues already use them and describes management bypassing review. This reinforces recurrence but also limits the idea: software cannot repair absent authority or unwilling participation. It is not an independent interview or a separate demand channel. |
| Original native platform documentation | [Entra admin consent workflow overview](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/admin-consent-workflow-overview) and [review requests](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/review-admin-consent-requests) | Entra already has a request queue, application details, requested permissions, requester justification and review actions. A replacement consent queue has no demonstrated wedge. Native permission review is part of the baseline, not a feature to claim as absent. |
| Original incumbent workflow documentation | [Jira Service Management forms](https://support.atlassian.com/jira-service-management-cloud/docs/what-are-forms/) | Conditional fields, validation, instructions, attachment to existing requests, reopening for edits and form-triggered automation already cover much of structured intake. This is strong counterevidence to a standalone app. |
| Original low-code substitute documentation | [Innovation Backlog](https://learn.microsoft.com/en-us/power-platform/guidance/coe/use-innovationbacklog) and [current Power Platform admin center](https://learn.microsoft.com/en-us/power-platform/admin/admin-documentation) | Existing tooling gathers pain points, participants, tools and development ownership; supported platform administration includes security and deployment governance. The CoE Starter Kit page says it is no longer actively maintained and points to the admin center. That does not prove the successor lacks a relevant capability. |

**Confidence:** medium that repeated incomplete app submissions create consequential review work; low that a new software product beats an existing form and technical review. The evidence does not establish what these particular apps actually do, their effective permissions, or whether a questionnaire would change maker behavior. Do not repeat the commenter's generalization that a particular coding assistant always stores data in browser cache: persistence must be checked for the specific app.

## Shortlist: competitor and wedge-first gate before scoring

Three software candidates were checked. Rejected candidates are not numerically scored. The winner's numerical score follows the competitor checks below.

### 1. ConsentBrief — narrowed and retained

**Wedge-first line:** small M365 IT team reviewing a nondeveloper's custom automation → native Entra consent review plus a prepared ITSM questionnaire → the source reports missing facts at handoff, but does not demonstrate that a configured form fails → a revision-specific appendix that distinguishes maker declarations, attached evidence references, reviewer observations and unknowns, with a resubmission diff → a concrete “before requesting tenant consent” example and reusable ITSM form recipe for M365 application reviewers, shared only in relevant discussions where invited → today's operator thread describes recurring employee-built app submissions; no new regulatory deadline or platform retirement is claimed.

- **Direct functional competitors:** Entra's native consent workflow for permission approval; Jira Service Management forms for structured information collection. Both already solve core parts of the job.
- **Indirect substitutes:** an approved questionnaire, an existing developer's technical review, a data-flow diagram, or a supported low-code implementation with platform governance.
- **Status quo:** request the missing facts, return an incomplete submission, route it to the existing development team, or deny access under established policy. A maker who cannot answer needs technical help, not plausible answers invented by software.
- **Gate result:** reject generic app scanning, automatic least-privilege recommendations and a new approval queue. Retain only a bounded evidence-handoff/revision-comparison hypothesis. No proven incumbent feature gap is credited.
- **Kill condition:** a prepared native-request-plus-form workflow yields the same missing-fact detection and resubmission clarity at equal or lower total effort. Prefer publishing the questionnaire template rather than a product.

### 2. TemplateRoute — rejected before scoring

**Wedge-first line:** Windows AD CS operator seeing no web-enrollment templates after an HSM deployment → native certificate enrollment methods and Microsoft's template troubleshooting → an empty web dropdown is reported, but template version, publication, requestor permissions and provider configuration are unknown → candidate was a route-selection diagnostic app, but the supplied facts do not justify new software → an exact web-enrollment/CNG troubleshooting guide for AD CS administrators → a fresh deployment incident, not a demonstrated new platform gap.

- **Signal:** [IIS request ssl certificate but there is no template](https://www.reddit.com/r/sysadmin/comments/1xocb7u/iis_request_ssl_certificate_but_there_is_no/), posted today; the short post and visible comment were retrieved. The author mentions AD CS integrated with an Utimaco HSM and an empty template list. No configuration or template schema was supplied.
- **Direct functional substitute:** Microsoft's [Version 3 CNG templates and web enrollment guidance](https://learn.microsoft.com/en-us/troubleshoot/windows-server/certificates-and-public-key-infrastructure-pki/cng-templates-not-appear-certificate-web-enrollment) already documents this enrollment-method limitation and other common causes. It identifies MMC, scripts, autoenrollment and exported requests as alternatives for the described CNG scenario.
- **Indirect substitute / status quo:** native certificate tooling and CA/HSM support can inspect publication, access and provider settings. The actual incident is not diagnosed by the mere presence of an HSM.
- **Wedge and kill:** reject the app. A short documented decision tree may solve the question; no repeated paid workflow or missing capability is established. Do not recommend altering template schema versions or weakening cryptography to populate the dropdown. No enrollment or infrastructure change was performed.

### 3. OfficeWatch — rejected before scoring

**Wedge-first line:** small-office infrastructure administrator choosing device monitoring → Zabbix, existing monitoring platforms and device API integrations → the source asks what others use, while visible replies identify functioning options and alert fatigue rather than a missing collector → candidate was a lightweight office-device monitor, but no narrow unsolved workflow survives → an exact network-device onboarding and alert-dependency configuration recipe for small-office operators → a fresh discovery question, not a proven buying trigger.

- **Signal:** [What are you guys using to monitor your office network?](https://www.reddit.com/r/sysadmin/comments/1xocarg/what_are_you_guys_using_to_monitor_your_office/), posted today; full post and visible comments retrieved. Replies name Zabbix and PRTG, describe custom API aggregation and flag alert fatigue. They are not proof that another dashboard is wanted.
- **Direct competitor:** [Zabbix network monitoring](https://www.zabbix.com/network_monitoring) already documents SNMP monitoring, device discovery, automatic onboarding, templates, maintenance suppression and alert dependencies. Its product page describes the software as open-source without hidden costs; no hosted/support pricing comparison was performed.
- **Indirect substitute / status quo:** existing vendor consoles, API-based checks, configured thresholds and the current helpdesk workflow. No quantified weekly burden or unmet device-specific requirement is supplied.
- **Wedge and kill:** reject a new monitor/dashboard and a generic alert-fatigue wrapper. Existing collection and noise-reduction features already cover the stated job; tune the current system first.

## Problem

A nondeveloper can present a working automation while being unable to describe its data destinations, access needs, operating owner or recovery path. The IT reviewer must reconstruct these facts before deciding whether access is appropriate. A persuasive demo and a completed form are not evidence of safe implementation.

The current public reports mix technical unknowns with organizational bypass. ConsentBrief can only address cooperative, pre-review handoff. It cannot discover every unregistered tool, compel management to enforce policy or verify an assertion that a maker does not understand.

**Status-quo pain test:** the original report involves broad tenant-access requests; another operator reports tools used before review and possible sensitive-data exposure. That is a credible security-risk reason to investigate. No breach, effective privilege level, lost revenue, more-than-30-minutes-per-week measurement or time saving was verified. If the existing request template and developer review are adequate, reject the standalone app.

## Target user

A small M365 application-review team that already has an approved request/consent process and willing employee makers, but receives incomplete supporting information for custom automations outside a single low-code platform. Not a company seeking to replace security engineering, an adversarial shadow-IT discovery product, or a maker seeking a safety certificate to bypass review.

## MVP scope

Proposed software only; **not implemented or behavior-tested in this research run**:

1. A static, local-first browser form with explicit JSON import/export. The working document is saved to a user-controlled file; browser storage must not be the only durable copy. No account, backend, tenant access, external analytics or AI-generated answers.
2. Collect the app's declared revision, business purpose, accountable owner, data categories, destinations, runtime/storage locations, declared access needs, external service use, recovery instructions and existing review-request reference. Missing facts remain `unknown`; unsupported declarations stay distinct from evidence-backed observations.
3. Record evidence references and their scope/date, rather than ingesting code, live credentials, production data or executable attachments. Reviewers can record that they inspected a referenced artifact; the app does not infer encryption, residency, deletion behavior or effective privilege from a checkbox.
4. Compare two supplied revisions and highlight changed answers, missing evidence and unanswered fields. A content digest, if added later, only identifies supplied bytes; it neither proves the running deployment matches nor authenticates an earlier approval. No automatic carry-forward of a prior review to a different revision.
5. Export a plain, escaped HTML or Markdown appendix and a JSON document for attachment through the organization's existing approved system. Identify it as “information for review,” not “approved,” “secure” or “compliant.” All consent decisions and technical verification remain in the native workflow.

**Boundary:** this is a documentary handoff tool, not a security scanner, permission evaluator, consent broker or general task tracker. Requested access, granted access and actual runtime use are different facts. Do not treat a copied app manifest or maker's statement as proof of effective permissions. Do not execute submitted scripts, crawl private endpoints, publish evidence or grant/revoke tenant access. User-supplied text must be rendered as data, never executable HTML. An offline workflow still handles sensitive business metadata and must follow the recipient's retention and sharing policy.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct functional competitor | Entra admin consent requests | Already supports requests, reasons, requested permissions, app details, reviewers and review actions. Keep as the system for access decisions; do not duplicate it. |
| Direct functional competitor | Jira Service Management forms | Already supports conditional intake, validation, existing-request attachments, edits and automation. A prepared form is the main benchmark, not an empty ticket. |
| Adjacent platform substitute | Power Platform governance and Innovation Backlog concepts | Standardized intake and platform controls exist. The legacy kit's maintenance status is not evidence that current native governance is absent. Not all custom apps are Power Platform apps. |
| Indirect substitute | Approved questionnaire plus developer review | Can capture the same facts and unknowns without another application. Include maker effort, technical help and resubmission review in the timing baseline. |
| Status quo | Return incomplete requests or route to the existing developer team | May already be sufficient; the fresh author explicitly says developer teams exist. A policy/ownership problem alone does not justify new software. |

## Wedge

The possible wedge is a **portable, revision-specific evidence appendix for custom automation submissions**, not another place to approve apps. It would make unanswered questions visible and make changed resubmissions easier to inspect while leaving consent and expert judgment where they belong.

This is deliberately weak product differentiation until measured. Existing forms can implement much of it, and an existing developer may be the right solution to missing knowledge. No source proves revision comparison is currently painful or missing from the customer's chosen ITSM configuration. The best output may be a reusable request template rather than software.

Unlike the earlier generic VibeGuard bet in this index, this proposal explicitly excludes scanning and fixes. If research cannot distinguish its handoff value from that crowded category or a questionnaire, do not build it.

## Kill condition

Reject the standalone app if any condition holds:

- A configured ITSM form plus the native Entra request produces equally clear missing-fact detection and revision review at equal or lower complete workflow effort.
- Makers cannot supply the facts even with technical help, or management routinely bypasses the established process. An intake UI does not create review authority.
- Three relevant reviewers cannot provide recurring submission cases, or fewer than two achieve a provisional 30% reduction in combined maker/reviewer effort without additional missed unknowns. This is a validation target, not a measured result.
- A useful product requires inferring security facts from untrusted answers, executing uploaded code, broad tenant collection or automating consent decisions.
- The only distribution path is one support thread, or the value is fully captured by publishing a questionnaire template.

## Scoring

Assigned after competitor checks and narrowing, not used to rescue the rejected candidates.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Repeated incomplete submissions and possible sensitive-data exposure matter; the app's ability to change the workflow is unvalidated. |
| Feasibility | 5/5 | The intentionally small form, explicit JSON save/load, escaped appendix and answer diff are practical in one to three days without private APIs. No scanning, technical verification or approval integration is included. |
| Demo potential | 4/5 | A missing-fact appendix and a changed-revision comparison would be easy to demonstrate with synthetic cases. No working demo was produced today. |
| Distribution | 3/5 | M365 consent reviewers and a specific request-template/troubleshooting recipe identify a channel hypothesis, but recurring access or adoption is unproven. A named community alone does not earn 4/5. |
| Competitive wedge / timing | 2/5 | Fresh operator recurrence supports investigation; native consent and configurable forms are strong substitutes, and revision-review demand has not been established. |
| Total | 18/25 | Total reaches 18, but Distribution and competitive-wedge gates both fail. |

## Decision

**Idea-only. No dedicated project repo created.** ConsentBrief is today's strongest retained validation hypothesis, not a validated buyer need or a security product. Weakest dimension: competitive wedge/timing at 2/5, below the 3/5 gate. Distribution is 3/5, below the 4/5 gate. Reaching 18/25 does not override either gate.

The evidence supports improving an existing submission handoff and testing whether a prepared questionnaire already solves it. It does not support another consent platform, a generic AI security wrapper or paid-product claims. No pricing or willingness-to-pay evidence was collected.

This is the hundredth numbered product bet in the index; Day 000 is the separate meta-index entry. The milestone does not lower the build threshold or authorize repository creation for its own sake.

## Next build step

If taken forward, make one validation-sized commit with three synthetic app-submission fixtures, one changed-revision resubmission, a prepared ITSM questionnaire and an appendix schema. Include conflicting evidence, unknown storage location and declared-versus-reviewed distinctions. Compare complete maker/reviewer effort against native Entra permission review plus that prepared form with three relevant reviewers; require two to meet the improvement target before implementation. Prefer publishing the template if that baseline suffices. No outreach, tenant access, consent action or working prototype occurred in this run.

Follow-up is tracked in Beads (`apps-6vm`).

## Source access caveats

- Canonical `reddit-readonly find` requested five recent posts each from r/sysadmin, r/selfhosted and r/webdev, within 48 hours. r/sysadmin JSON was blocked with HTTP 403/theme-beta; RSS returned five posts. RSS scores/comment counts were unavailable, not zero engagement.
- The same probe reported r/selfhosted and r/webdev JSON/RSS unavailable with HTTP 429. No tight retry loop. Date-constrained Reddit web searches returned no results; broader searches found older inventory/handover posts, which were not used as fresh demand evidence.
- Selected sysadmin posts and visible comments were recovered through HTML extraction. Collapsed replies were not exhaustively retrieved. Recurrence within one thread is not broad market validation.
- `xurl whoami` succeeded, but read-only search returned HTTP 401 Unauthorized. No OAuth2 user was configured; no login flow was attempted. X-constrained web fallback searches also returned no usable evidence. No X validation is claimed.
- The original Microsoft, Atlassian and Zabbix documentation bodies were readable. Searches for additional app-intake vendors returned empty results; this is not proof they do not exist. Competitor capabilities are documented, not hands-on tested.
- Microsoft's retrieved consent pages disagree about some reviewer-history visibility and deny-notification details. Those discrepancies were not resolved or converted into a product gap. The proposal relies only on their shared, documented request/review capabilities; operational rollout would require current tenant-specific verification.

## Repository verification caveat

The existing repository-wide snapshot verifier still fails with `KeyError: 'source_commit'`, tracked separately in Beads (`apps-mq0`). No snapshot or verifier code changed in this daily run. Daily brief/index consistency, JSON and focused public-safety checks are verified separately; the repository-wide suite must not be described as green.
