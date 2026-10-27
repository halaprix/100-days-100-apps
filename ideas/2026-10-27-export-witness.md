# Day 091 — ExportWitness

Date: 2026-10-27
Status: idea-only

## One-line pitch

A local M365 audit-export handoff checker that distinguishes verified file integrity from operator-declared search provenance and unknown export completeness before an administrator transfers logs to an incident-response partner.

## Research brief

- Decision: select one practical software hypothesis; create a dedicated repo only if the total and both dimension gates pass.
- Target customer: small-team M365 administrators preparing an audit-log handoff under an incident responder's instructions, without an existing evidence-management workflow.
- Geography: initially English-language M365 operations; no jurisdiction-specific legal certification.
- Category: offline export-context review, not forensic acquisition, threat detection, or a generic security scanner.
- Time horizon: a one-to-three-day prototype only after a baseline comparison and responder review.
- Must-answer questions: does a structured distinction between integrity, provenance, and completeness prevent real handoff mistakes beyond a README, native export guidance, and BagIt? Will responders accept the output?
- Evidence bar: a complete fresh community report plus original platform and substitute documentation. Quick scan only: no customer interviews, payments, market-size estimate, or demonstrated acquisition channel.
- Creative constraint: nothing new except glue. Reuse existing checksums and packaging rather than invent another evidence format.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Public community report, 2026-10-27; RSS discovery followed by full public HTML and visible comments | [Police Evidence](https://www.reddit.com/r/sysadmin/comments/1xgmaew/police_evidence/) | An administrator reports a compromised M365 tenant and a police request for logs. They already exported a filtered CSV, documented the filter and method, and generated a hash, but ask what else is needed. Visible replies favor asking the recipient and involving an IR partner. This is one incident, not proof that another packaging tool is wanted. |
| Original Microsoft platform documentation | [Export, configure, and view audit log records](https://learn.microsoft.com/en-us/purview/audit-log-export-records) | Purview already exports raw audit data and documents Standard/Premium export limits of 50,000/1,000,000 records per search. Exports exceeding a limit can omit records. A checksum cannot establish search coverage or completeness. The page also documents PowerShell export and Excel transformations. |
| Original operational guidance; historical, not current legal advice | [RFC 3227 — Guidelines for Evidence Collection and Archiving](https://www.rfc-editor.org/rfc/rfc3227) | Calls for detailed actions/times, UTC or local-time context, transparent collection procedures, and chain-of-custody documentation. It explicitly says procedures may not suit every jurisdiction and should be confirmed with appropriate law enforcement. This supports caution, not a claim that a CLI makes evidence admissible. |
| Original format specification and implementation | [BagIt / RFC 8493](https://www.rfc-editor.org/rfc/rfc8493) and [Library of Congress bagit-python](https://github.com/LibraryOfCongress/bagit-python) | Existing packaging already supplies payload manifests, descriptive metadata, and validation. bagit-python documents checksum mismatch, missing-file, and unexpected-file errors. Generic hash-and-zip functionality is not an uncovered opportunity. |

### Evidence quality and uncertainty

The source author already performed much of the proposed workflow correctly and is in contact with the recipient. That is counterevidence to a replacement product. Their question is about confidence and accepted procedure, not an explicit request for software. Native export limits independently establish a technical limitation; they do not show that this author's export was truncated.

No independently retrieved second customer report establishes repeated unmet demand for the narrowed checker. General web search became unproductive, returning empty results even for broad terms; competitor discovery is consequently incomplete. Directly retrieved original documentation is the basis of the comparisons below. No willingness to pay or weekly time saving is claimed.

## Problem

Three different assertions are easy to conflate during a rushed audit-log handoff:

1. **File integrity:** do these bytes still match a previously recorded checksum?
2. **Search provenance:** what source, query, filters, time window, time zone, export method, and operator actions produced them?
3. **Completeness:** does the export contain everything the recipient requested, without query-limit loss, missing sources, or gaps?

A local checker can test the first against a trusted reference, prompt for the second, and identify explicit limitations for the third. It cannot reconstruct missing acquisition history, independently attest an operator's account, or prove that a filtered CSV represents all relevant activity.

Status-quo pain test: mistakes can impair an incident investigation or require another handoff under time pressure. The actual time loss and mistake rate are unmeasured. If the responder's existing instructions plus a short text file are sufficient, a standalone app should be rejected.

## Target user

The M365 administrator asked by an IR partner to provide specific existing audit exports and their context, who does not operate an established evidence platform. The responder defines the requested scope and acceptable transfer process. Not police investigators, forensic examiners replacing their tools, or all security teams.

## MVP scope

Proposed software only; no product implementation was built during this research run.

1. Accept operator-approved working copies of already-exported CSV files and a small context JSON. Never acquire logs from the tenant or operate directly on original evidence media. Reading can affect filesystem access metadata; “offline” is not a forensic write-blocking guarantee.
2. Capture exact operator-declared source, search filters, requested time window with offsets, export start/end, method, available result-count evidence, known omissions, and recipient instructions. Unknown values remain unknown, not guessed or backdated.
3. Stream SHA-256 checksums and compare with a separately supplied prior manifest when present. A newly generated checksum is a new reference, not proof that the input was authentic before this run. Reading errors, changing files, and absent references must fail or remain explicitly unverified.
4. Count parseable records without editing the input. Separate observed rows from operator-declared search results and documented export limits. Flag at-limit results as a review trigger, not proof of truncation; a below-limit CSV does not prove completeness. Do not silently merge or deduplicate evidence.
5. Produce a local review report with three separate states: integrity result, declared provenance fields, and completeness unknowns. If packaging is requested by the recipient, reuse BagIt on a separate copy rather than inventing a proprietary container. Do not open CSV data in a spreadsheet or execute formula cells.
6. Keep the operational handoff confidential and local. Provide a separate metadata-minimized demonstration summary; never publish tenant identifiers, queries, account names, file paths, audit rows, or evidence hashes to the incubator repo. Redacted derivatives must remain distinct from the received exports, with explicit derivation records if used.

Non-goals: legal admissibility claims, certifying chain of custody, reconstructing past custody, attributing attackers, proving all tenant activity was collected, collecting credentials, live tenant API access, automatic re-export, automatic redaction of source evidence, uploading files, or replacing professional incident response. Tool timestamps are local clock observations, not trusted timestamp authority attestations.

## Shortlist — competitor and wedge-first gate before scoring

Three software candidates were checked before assigning any numeric score. Rejected candidates are not rescued by easy-MVP points.

### 1. ExportWitness — retain only the export-context review hypothesis

**Wedge-first:** small-team M365 administrator handing approved exports to an IR partner → Purview CSV plus a text README, PowerShell hashes, BagIt, or the responder's case system → these already solve export, documentation, and integrity packaging; the remaining hypothesis is that a novice conflates those checks with completeness → a recipient-directed review separating integrity, operator-declared provenance, and unknown coverage without touching the tenant → a worked synthetic example discoverable through exact M365 audit-export-limit and IR-handoff searches, with a responder-reviewed template offered through relevant administrator discussions only after human approval → today's report exposes uncertainty at the handoff boundary, not a new technical or regulatory deadline.

- Direct job substitutes: [bagit-python](https://github.com/LibraryOfCongress/bagit-python) for integrity packaging and [DFIR-IRIS](https://github.com/dfir-iris/iris-web) for collaborative investigation detail management. IRIS was inspected at README level; no exact M365 checklist gap is asserted.
- Native/indirect substitutes: [Purview export guidance](https://learn.microsoft.com/en-us/purview/audit-log-export-records), a short PowerShell hash/count script, an existing evidence worksheet, and the recipient's instructions.
- Adjacent acquisition substitute: [PwC Office 365 Extractor](https://github.com/PwC-IR/Office-365-Extractor) documents source counts, selected/full audit extraction, and output/debug logs. Its older prerequisites and retention statements were not treated as current platform guidance; execution compatibility was not tested. Another collector is not the wedge.
- Status quo: preserve what has already been collected, document actions, and ask the IR partner/recipient what to provide and how. The source author already does this; the main unmet issue may be professional advice rather than software.
- Gate result: retain a bounded comparison hypothesis, not a validated commercial wedge. The workflow and search topic are specific, but repeatable user access is unproven.
- Kill condition: BagIt plus the recipient's existing worksheet flags the same material gaps with at most five minutes extra work, or responders prefer the worksheet and no recurring handoff problem is observed.

### 2. RuntimePatchMap — reject a generic .NET patch inventory wrapper

**Wedge-first:** .NET service owner responding to an out-of-band runtime fix → Microsoft's deployment-specific guidance, software inventory, and existing rebuild/redeploy process → shared-runtime inventory alone does not cover self-contained deployments, but the distinction is already explicit in official guidance → a deployment-owner reconciliation receipt would need evidence of a repeated ownership gap that today's sources do not establish → exact self-contained-runtime patch searches reach a concrete audience but no first-user channel was demonstrated → a fresh OOB release is timely, not proof of whitespace.

- Fresh signal: [community OOB patch summary](https://www.reddit.com/r/sysadmin/comments/1xgj5cj/outofband_net_patches_landed_oct_25_for_the/), retrieved in full with visible comments.
- Original validation: [Microsoft's OOB announcement](https://devblogs.microsoft.com/dotnet/dotnet-october-2026-oob-security-updates/) explicitly distinguishes shared-runtime updates plus restart, self-contained rebuild/republish, and container rebuild/redeploy. No need to copy a community claim about endpoint urgency into product policy.
- Direct substitute: [Defender Vulnerability Management inventory](https://learn.microsoft.com/en-us/defender-vulnerability-management/tvm-software-inventory) already exposes versions, vulnerabilities, evidence, and APIs. Coverage is not universal: Microsoft documents limits for manually installed Linux software. That limitation does not establish that a one-to-three-day wrapper can safely cover embedded runtimes.
- Indirect/status quo: application owners follow the vendor's checklist, existing CI/SBOM inventory and deployment tickets; a spreadsheet maps owners if needed. Patch work is security-relevant, but new-app demand is unproven.
- Kill condition fired: crowded generic scanner/inventory category, with no source-proven narrow workflow advantage or acquisition channel. **Rejected before scoring.**

### 3. AgentCheckoutGate — reject another agent allow-list or signature checker

**Wedge-first:** headless-commerce security owner approaching a WAF rules freeze → Cloudflare bot controls, Web Bot Auth libraries and validation CLI, plus merchant payment-abuse controls → authenticating an agent does not settle merchant authorization or fraud policy, but another signature validator does not solve that business decision → a staging checkout matrix is a possible narrower test artifact, not a proven product gap → exact agent-checkout/WAF troubleshooting content could reach commerce security engineers, but there are no accessible pilot stores → the source reports a November 1 rules freeze and concern about agent purchases; those are source-specific circumstances, not a universal deadline.

- Fresh signal: [Our bot rules weren't built for AI agents that buy](https://www.reddit.com/r/sysadmin/comments/1xghj9f/our_bot_rules_werent_built_for_ai_agents_that_buy/), full post and visible comments retrieved. The author explicitly says business has not decided which agents to allow. That is an unresolved policy decision, not necessarily a tooling failure.
- Direct alternatives: [Cloudflare Web Bot Auth](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) already documents cryptographic verification, registration, a directory-validation CLI, troubleshooting, and Rust/TypeScript libraries. [Cloudflare's agentic-commerce announcement](https://blog.cloudflare.com/secure-agentic-commerce/) describes work with Visa and Mastercard; future-tense SDK/rules plans were not treated as shipped features.
- Indirect substitute/status quo: a merchant-approved policy and a small staging integration test, retaining fraud/rate controls for checkout. User-Agent strings alone are spoofable; signing identity is not authorization to charge a card or bypass payment controls.
- Kill condition fired: the default product duplicates existing authentication tooling; a more ambitious real-payment/WAF conformance test exceeds safe, evidenced MVP scope. No authorized merchant fixture or repeatable channel exists. **Rejected before scoring.** No checkout requests or live abuse tests were performed.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct integrity-packaging substitute | [bagit-python](https://github.com/LibraryOfCongress/bagit-python) / [RFC 8493](https://www.rfc-editor.org/rfc/rfc8493) | Already creates and validates checksum manifests plus metadata. A hash-and-zip app is rejected. Use as a baseline or component, not a strawman. |
| Direct investigation-workflow substitute | [DFIR-IRIS](https://github.com/dfir-iris/iris-web) | Existing collaborative investigation platform. Operators already using it or an equivalent case system may not need another tool. Only its published overview was inspected. |
| Native export substitute | [Purview export and PowerShell guidance](https://learn.microsoft.com/en-us/purview/audit-log-export-records) | Already explains filters, raw data, CSV, and export limits. A checklist copied from this page may be enough. |
| Adjacent collection substitute | [Office 365 Extractor](https://github.com/PwC-IR/Office-365-Extractor) | Existing extraction and source-count workflow; not execution-tested or assumed current. ExportWitness must not become a redundant acquisition tool. |
| Indirect substitute | README plus hash/count script and recipient's worksheet | Very low setup cost, and close to what the source author already does. Most important benchmark. |
| Status quo / professional service | Recipient instructions, IR partner, insurer's response service | May answer the actual uncertainty better than software. A report must not imply these safeguards can be replaced. |

No exhaustive absence-of-competitors claim is made. Published features were read, not hands-on tested, and no pricing or savings claim is inferred.

## Wedge

Only the **separation of claims** survives: make it hard to label “checksum matches” as “complete, authentic, legally sufficient evidence.” A local review could make unknown provenance and potential limit issues explicit while following recipient instructions. This is narrower than evidence management and safer than an “admissibility certificate.”

The difference may fit better as a reusable template or an addition to an existing packaging tool than a standalone product. Today's scan does not establish that the standalone app wins. Distribution remains a search-and-template hypothesis, not verified repeatable access. Timing is an acute incident report rather than a new platform requirement.

## Kill condition

Reject the standalone app if any of these hold:

- A timed handoff exercise shows that the recipient's worksheet plus a short native script and BagIt detects the same material omissions within five minutes of the proposed report.
- Two independent responders cannot identify recurring, consequential provenance/completeness mistakes that this narrow report would prevent.
- Reviewers interpret a pass state as authenticity, comprehensive collection, chain-of-custody certification, or legal admissibility despite explicit separation of claims.
- Reliable output requires live tenant credentials, changing original evidence, reconstructing unknown historical actions, or accepting unverified operator declarations as independently established facts.
- A reusable template in an existing workflow is sufficient; prefer that route over creating another repo.

## Scoring

Only the narrowed survivor is scored after the gates above. Scores are judgments, not measured demand.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Incident handoff mistakes can have consequential security/investigation costs. One report; recurring loss and need for software are unproven. |
| Feasibility | 4/5 | Offline context review and streaming integrity checks are small; changing inputs, CSV variants, privacy, and careful uncertainty wording need real validation. |
| Demo potential | 4/5 | A synthetic example can visibly show a matching checksum alongside missing query context and unknown coverage. It cannot prove forensic soundness. |
| Distribution | 3/5 | Specific M365/IR audience and exact handoff/export-limit topics exist; no repeatable responder channel or committed pilot users. |
| Competitive wedge / timing | 2/5 | Native guidance, BagIt, worksheets, and IR services already cover much of the job. The separation-of-claims advantage is plausible but unmeasured. |
| Total | 17/25 | Below 18/25; Distribution also fails 4/5 and wedge/timing fails 3/5. |

## Decision

**ExportWitness is today's research winner, idea-only. No dedicated project repository created.** RuntimePatchMap and AgentCheckoutGate were rejected before scoring. Do not equate winning a weak shortlist with permission to build.

Recommendation: validate the review workflow against the existing worksheet-and-BagIt baseline first. Evidence supports a concrete M365 handoff uncertainty and a real difference between integrity and completeness. It does not establish repeated unmet demand, legal suitability, willingness to pay, or a sustainable channel. A measured reduction in consequential omissions plus responder acceptance would change the recommendation.

## Next build step

One validation commit in the master index: define an export-context schema and an evaluation protocol with three explicitly synthetic cases—complete context with matching reference, matching checksum but unknown query/coverage, and changed file with incomplete context. Compare reviewers' omission detection and preparation time against a recipient worksheet plus a native hash/count script and BagIt. Have two independent IR practitioners review the claims and results before promoting a standalone app. Synthetic fixtures validate logic only, not real acquisition history or legal acceptance.

Follow-up work belongs in Beads, not a Markdown task list.

## Source access caveats

- The canonical read-only Reddit helper found five r/sysadmin posts through `reddit-rss-fallback` after public JSON returned HTTP 403. RSS score/comment zero placeholders were not treated as engagement data.
- The same helper reported r/selfhosted, r/webdev, and r/androidapps unavailable with HTTP 429 and returned no posts from them. No tight API retry loop was used. A constrained Reddit web fallback returned no additional evidence.
- All three shortlisted r/sysadmin posts were subsequently retrieved as public HTML, including original bodies and visible comments. Collapsed replies were not exhaustively retrieved.
- X authentication status and `whoami` worked with existing OAuth1 credentials, but search returned HTTP 401. No OAuth2 token was present, and no auth change was attempted. A targeted `site:x.com` fallback returned no results. No X validation is claimed.
- Initial general competitor searches returned some results; later targeted and broad searches returned empty results. Direct original-document retrieval supplied the usable comparisons. This narrows discovery confidence and is not evidence that competitors do not exist.
- A Velociraptor documentation URL could not be retrieved and supplied no product-feature evidence. Other irrelevant fetched pages were not used to pad the winner's evidence.
- No social writes, customer-system actions, forensic acquisition, evidence uploads, or production probes were performed. Public artifacts contain only public-source summaries and a proposed workflow.
