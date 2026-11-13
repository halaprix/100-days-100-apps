# Day 107 — CreditRoute

Date: 2026-11-13
Status: idea-only

## One-line pitch

A local-first app that helps Microsoft 365 CSP support teams review customer-specific SLA-credit intake gaps and route each request to the authorized provider, without promising eligibility or submitting claims.

## Research brief

- **Decision:** retain one bounded software hypothesis; create a project only if total and dimension gates pass.
- **Target customer:** a CSP support coordinator handling multiple business customers after the same Microsoft 365 incident, especially an indirect reseller handing evidence to its provider.
- **Geography:** English-language CSP workflows first; agreements and distributor requirements remain account-specific.
- **Substitutes:** Partner Center support, the provider's existing intake, a prepared claim worksheet and public how-to guides.
- **Time horizon:** a 1–3 day prototype for one documented intake schema, not a billing platform or outage monitor.
- **Must answer:** does checking many customer requests create repeated rework beyond a configured support form? Can a local view reduce complete acquisition-and-review effort rather than merely produce another template?
- **Evidence bar:** public operator context plus original Microsoft documentation. No interviews, claim outcomes, savings or willingness to pay were observed.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Fresh public community post, 2026-11-13; RSS discovery, full post and visible replies retrieved | [A small win for the sysadmins today](https://www.reddit.com/r/sysadmin/comments/1xv27w7/a_small_win_for_the_sysadmins_today/) | Explicitly encourages claiming SLA refunds after the outage. This is interest in compensation, not a request for an intake app. The author's staffing/root-cause speculation is unverified and is not adopted. |
| Original platform documentation, updated 2026-06-16 | [How and when to request a credit](https://learn.microsoft.com/en-us/partner-center/billing/request-credit) | Only CSP direct and indirect providers can submit these requests; indirect resellers cannot submit directly. Requires tenant GUID, incident ID, customer impact and a customer request from the affected tenant's domain. A ticket number and timestamp alone are insufficient. |
| Original contractual document, November 1, 2026; downloaded and read | [Online Services SLA editions and November document](https://www.microsoft.com/licensing/docs/view/service-level-agreements-sla-for-online-services) | General Terms distinguish claim submission, Microsoft approval and service credits. Outage communications do not confirm eligibility; actual downtime and the affected service matter. The applicable edition depends on the subscription agreement/term, not simply the latest download. |
| Original platform documentation | [Microsoft 365 service health](https://learn.microsoft.com/en-us/microsoft-365/enterprise/view-service-health) | Already supplies incident IDs, affected services, updates and recent issue history. Copying a status feed is not a product wedge and does not establish individual customer impact. |
| Original billing documentation | [Bills and reconciliation data](https://learn.microsoft.com/en-us/partner-center/billing/read-your-bill) | Native exports already describe finalized charges/credits versus open-period estimates. Credit intake is not invoice reconciliation, and an accepted ticket is not money credited. |
| Fresh secondary guide, 2026-11-13; commercially interested reseller | [SourceIT claim guide](https://sourceit.com.sg/blogs/news/microsoft-365-outage-sla-credit-claim-how-to) | Already provides a clear checklist and buying-route explanation. Strong free substitute, not independent customer demand. Its claim that October is the latest SLA edition is stale against the retrieved November listing. |
| Fresh secondary reporting, 2026-11-13 | [Windows Latest credit-request walkthrough](https://www.windowslatest.com/2026/11/13/microsoft-365-outage-you-may-get-money-off-your-bill-if-you-use-it-for-work-but-youll-have-to-ask-microsoft-for-it-as-a-server-failure-takes-down-outlook-teams-and-exchange/) | Includes an existing admin-center support path and cautions against automatic percentage claims. It explicitly uses an older agreement for its percentage example; that example is not imported as this app's rulebook. |

**Confidence:** high that a documented, time-bound customer-specific claim process exists; low that a separate app beats provider intake plus a prepared worksheet. Multiple outage posts concern the same event, not independent recurring evidence of claim-preparation pain. No operator reported measured intake time or a rejected claim caused by these omissions.

## Shortlist and wedge-first gate — before scoring

Constraint: **Automate the annoying thing**, using existing evidence and support workflows rather than inventing another status dashboard. Three software candidates were checked. Only the narrowed first candidate survives for scoring.

### 1. CreditRoute — narrow and retain

**Wedge-first:** CSP coordinator handling multiple customer requests for one incident → provider support form, Microsoft checklist and a prepared worksheet → possible repeated omissions and wrong-provider handoffs, not a demonstrated failure of those substitutes → a local multi-customer gap review with explicit submission ownership → an exact-query CSP claim-preparation guide and synthetic example, shared only where community rules permit → today's outage has prompted explicit credit interest while evidence can still be collected.

- **Direct workflow substitutes:** Partner Center support and the customer's CSP provider; the SourceIT and Windows Latest guides already explain the route and required information.
- **Indirect substitute:** a configured support form, ticket macro and worksheet with mandatory fields.
- **Status quo:** ask the licensing provider to handle the request, use its checklist, or decide that the possible credit is not worth the effort.
- **Pain test:** a missed or incomplete claim can forfeit a possible service credit. The value, recurrence and preparation burden for this segment are unmeasured; outage-related business losses do not equal credit value.
- **Gate:** reject a generic refund generator. Retain only a customer-by-customer intake review hypothesis, with low wedge credit and no assumption that a provider lacks this already.
- **Kill condition:** the existing provider form and prepared worksheet catch the same omissions quickly, or the provider handles the process without customer-by-customer duplication.

### 2. MailReturn — reject

**Wedge-first:** IT lead deciding whether mail service has recovered for its users → native service health and existing Microsoft 365 monitoring → regional reports differ but there is no demonstrated missing monitoring capability → a proposed local recovery-observation matrix → an Exchange recovery-testing guide for affected administrators → [today's Australian recovery report](https://www.reddit.com/r/sysadmin/comments/1xv2ahw/omg1_im_connected_to_microsoft_exchange/) and a visible reply still reporting failure in Southeast Asia.

- **Direct substitutes:** [Microsoft service health](https://learn.microsoft.com/en-us/microsoft-365/enterprise/view-service-health) and [Exoprise-powered monitoring in TeamViewer DEX](https://www.exoprise.com/), whose retrieved page explicitly offers Microsoft 365 outage visibility and proactive alerts. No claim that current Exoprise lacks a particular probe is made.
- **Indirect/status quo:** a prepared test checklist, existing monitoring and actual user confirmation. One recovered mailbox does not prove fleet recovery, complete backlog delivery or all application paths working.
- **Pain test:** interrupted mail blocks work, but this is not evidence that another observation UI solves an unmet job.
- **Kill condition / decision:** crowded monitoring/dashboard category with strong native and commercial substitutes; reject before scoring. Active mail tests send messages and are not read-only collection.

### 3. FallbackDrill — reject

**Wedge-first:** Small-office IT lead without an email-outage plan → an offline contact list, an agreed fallback channel and a tabletop exercise → a source admits no prior planning, not a missing software capability → a proposed no-Microsoft-login drill app → a practical continuity exercise guide for small IT teams → [today's emergency provider-switch question](https://www.reddit.com/r/sysadmin/comments/1xv1u90/if_this_is_not_fixed_by_the_morning_est_we_will/).

- **Direct workflow substitutes:** [Enterprise Singapore's documented continuity exercises](https://www.enterprisesg.gov.sg/resources/blog/be-prepared-for-uncertainty-with-a-business-continuity-plan) and the [existing small-office email-continuity guide](https://sourceit.com.sg/blogs/news/second-email-system-backup-after-microsoft-365-outage). The latter already distinguishes simple fallback channels, emergency mailboxes and third-party continuity services.
- **Indirect/status quo:** paper contacts, a prepared notice and a short rehearsal. Visible Reddit replies warn that a rushed MX/provider switch introduces split mail history, automation/authentication dependencies and a second migration back.
- **Pain test:** business interruption is real; the evidence supports preparation, not replacing a cheap checklist with another app.
- **Kill condition / decision:** no measured drill-maintenance burden or repeatable software advantage. Reject before scoring; do not encourage an emergency DNS change. A guessed Mimecast continuity URL returned 404, so it supplies no feature evidence in either direction.

## Problem

Microsoft's CSP claim process requires evidence for the individual customer and an authorized submitter. A coordinator can have an incident ID and a ticket yet still lack a customer request, impact details or the right submission route. A general incident bulletin is not proof that every licensed user was unavailable for its entire duration.

The possible product gap is **reviewing omissions across an explicit batch of customer requests before provider handoff**, not learning the public claim instructions. The existing form may already do the job. This run establishes a reason to test the hypothesis, not recurring unmet demand.

## Target user

A CSP support coordinator already handling several business-customer credit inquiries for one non-Azure Microsoft 365 incident. Start with one provider's agreed intake requirements. Exclude personal/family accounts, general consumer refunds, Azure credits, mixed-provider automatic routing and contractual eligibility assessment.

## MVP scope

A local browser app with an explicit JSON/CSV import/export contract and no server or account integration:

1. Import a minimized, operator-prepared customer-request register: stable customer/tenant identity, incident identifier, service, buying route, responsible provider, referenced evidence and reviewer-declared status. Validate literal GUID format without silently repairing values. Do not infer the provider from an email domain.
2. Show required-field and handoff gaps separately from content review. Track whether an operator has reviewed impact times, affected-user information, errors, customer request and tenant-domain correspondence; merely checking a box or matching a domain does not authenticate an email or prove entitlement.
3. Record impact intervals and provenance without extrapolating across unobserved periods or treating all seats as affected. Preserve unknown affected service, incomplete observations, conflicting requests and duplicated rows for human review.
4. Require the reviewer to record the applicable agreement/edition, confirmed billing-period basis and provider-confirmed deadline, including any earlier provider intake cutoff. If unconfirmed, show **deadline unverified**, not a fabricated countdown. Display the referenced rule's scope; no universal incident-date-plus-30-days logic.
5. Produce a local gap list and provider handoff draft. Distinguish prepared, handed off, provider acknowledged, Microsoft submission confirmed, decision pending, approved and invoice credit observed. Later states require explicit evidence references; the app cannot confirm them from intake completion alone.

**Non-goals:** submitting tickets or claims, sending email, DNS changes, tenant login, mailbox access, automated raw-email ingestion, probing production services, live invoice matching, computing credit percentages or legal advice. No promises of compensation, guaranteed acceptance or recovery of lost business revenue.

**Safety:** customer requests and tenant identifiers are sensitive business records. Use references to evidence already held in the existing support system, not copied mailbox bodies or credentials. Local-only is a proposed architecture, not a security audit: a delivered implementation would need network-request tests, safe rendering, export controls and an explicit storage/deletion policy. Public fixtures must be synthetic.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct native workflow | [Partner Center credit request and support](https://learn.microsoft.com/en-us/partner-center/billing/request-credit) | Already defines submission ownership, evidence requirements and processing. Indirect resellers must use their provider; this app cannot grant authority. |
| Direct operational substitute | Existing CSP provider's intake/support workflow | Microsoft explicitly assigns the provider role. Particular distributor portals were not inspected, so there is no claim that their forms lack validation or bulk handling. Obtain one actual agreed schema before implementing. |
| Direct informational substitute | [SourceIT checklist](https://sourceit.com.sg/blogs/news/microsoft-365-outage-sla-credit-claim-how-to) and the retrieved Windows Latest walkthrough | Instructions and support steps are already freely readable. A prose generator is unnecessary. Secondary claims about agreement editions must be checked against original documents. |
| Indirect substitute | Prepared spreadsheet, mandatory ticket fields and support macro | Strong baseline for the exact batch-review job. Measure complete collection, correction and handoff effort, not comparison with an empty spreadsheet. |
| Adjacent native substitute | [Service health](https://learn.microsoft.com/en-us/microsoft-365/enterprise/view-service-health) and [invoice reconciliation](https://learn.microsoft.com/en-us/partner-center/billing/read-your-bill) | Supply incident context and financial records respectively. Neither makes an intake check equivalent to approved credit; these are different stages, not missing features to invent. |
| Status quo | Let the provider manage it, or make no claim | Rational when expected credit is small or the provider already has a satisfactory process. An app must improve the economics, not merely add administration. |

No verified price advantage or market-size estimate. The reviewed instructions are public; provider support arrangements vary. No paid competitor absence is inferred from empty search results.

## Wedge

**One incident, several customer requests, one explicit question: what evidence and submission ownership are still missing before each request reaches the right provider?**

A local batch review could avoid another OAuth integration and retain uncertainty instead of promising refunds. But a configured form or worksheet can plausibly do all of this. That makes the wedge a testable hypothesis, not an established advantage.

Distribution experiment: a reproducible example targeting the exact CSP evidence-and-submission-owner problem, with a provider-reviewed checklist and permitted sharing in relevant admin communities. The fresh r/sysadmin useful-project thread provides a possible rule-compliant venue, not an owned channel or permission to promote. No posting occurred. Distribution stays 3/5 until actual access and recurring use are demonstrated.

## Kill condition

Kill the standalone app, or reduce it to a reusable form/worksheet, if:

- Three relevant coordinators can complete the same acquisition-and-review exercise with existing provider intake plus a prepared worksheet in about ten minutes per batch and do not want another tool.
- No coordinator has repeated multi-customer omissions or handoff rework; one large outage is not enough.
- A timed fixture comparison fails to improve correct identification of missing requests, wrong routes, unsupported impact assumptions and unverified deadlines without adding collection work. A proposed target is at least 30 minutes saved in a real multi-customer batch, not a measured result.
- Expected possible credits do not justify acquisition, maintenance and reviewer time, or a provider already centralizes everything satisfactorily.
- Value requires speculative entitlement calculations, collecting mailbox contents or bypassing authorized submission roles.

## Scoring

The competitor gate above precedes scoring. Rejected candidates are not assigned reassuring numeric scores.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | A documented deadline and required evidence can affect possible financial recovery. Actual lost credits and recurring intake rework are unverified. |
| Feasibility | 4/5 | One explicit schema and local gap view fit a 1–3 day prototype. Agreement/provider variation prevents an honest universal calculator. |
| Demo potential | 4/5 | A synthetic customer batch can visibly show different missing evidence and owners. No product demo was built during this run. |
| Distribution | 3/5 | Specific CSP audience and an exact-workflow content experiment; no provider partnership, pilot users or proven repeatable acquisition. |
| Competitive wedge / timing | 2/5 | Excellent incident timing does not overcome a free checklist, configured support form and adequate worksheet. Standalone benefit is not demonstrated. |
| Total | 17/25 | Below 18; both Distribution and competitive-wedge gates also fail. |

## Decision

**Winner: CreditRoute, idea-only. No dedicated project repository or implementation created.**

Keep the narrow intake-review hypothesis; reject a generic refund generator, another recovery dashboard and a continuity-checklist app. The next investment is a comparison with the existing provider workflow, not a scaffold.

Important rule boundary: the retrieved November SLA is newer than the reseller guide says, but it is not automatically the applicable agreement. For non-Azure claims its General Terms describe receipt by the end of the following Applicable Period; Partner Center describes one month after the billing month ends. Confirm account-specific applicability and provider cutoffs rather than silently treating the phrasings as a universal deadline. The two documents also use different Azure deadline language; Azure is outside this MVP.

## Next build step

Prepare one synthetic six-case intake fixture and an equivalent configured worksheet: direct provider, indirect reseller, missing customer request, uncertain affected service, unconfirmed billing basis and provider acknowledgment without a Microsoft submission receipt. Have a relevant coordinator compare full preparation and review effort against its existing workflow before writing the app. Validation is tracked in Beads `apps-2c2`.

## Run verification

Validate JSON, today's unique day/date entry, README/brief consistency, section completeness, score arithmetic and changed-artifact public safety. The repository-wide consolidated-snapshot verifier still fails with the pre-existing `KeyError: 'source_commit'`, tracked in `apps-mq0`; this run changes no snapshots and does not claim the full suite is green.

## Source access caveats

- The canonical Reddit `find` probe returned r/sysadmin through **RSS fallback** after JSON was blocked with 403/theme-beta. r/selfhosted, r/webdev and r/SideProject were unavailable with HTTP 429; no tight retry loop. RSS scores/comment counts are unknown, not evidence of zero engagement.
- Web extraction subsequently retrieved the three selected Reddit posts and visible replies. This is not exhaustive thread retrieval or proof of consensus. Reddit-constrained search returned no additional usable corroboration.
- `xurl whoami` succeeded; search returned **401 Unauthorized**. No OAuth2 user was configured and no interactive authorization was attempted. X-constrained search supplied no usable demand evidence; a general search surfaced an AI-generated X template that was excluded, not counted as a customer signal.
- Several competitor searches returned empty results even for known products. Original vendor/native pages were inspected instead; empty results do not establish market whitespace. Exoprise's retrieved homepage now presents TeamViewer DEX. A Mimecast continuity URL returned 404 and an unrelated SLA-tool URL could not be retrieved; neither supports a feature-absence claim.
- The original November SLA document was successfully downloaded and its introduction and General Terms read. No customer agreement, tenant incident record, distributor portal or actual claim was accessed. All social actions were read-only. No customer interviews, benchmark, claim submission or app execution occurred.
