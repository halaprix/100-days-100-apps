# Day 105 — FixInterleave

Date: 2026-11-11
Status: idea-only

## One-line pitch

A local CLI for ESLint plugin maintainers that compares combined autofixes with bounded single-fix/re-analysis traces on a supplied fixture, turning an interaction bug into a reviewable regression case rather than promising a universally safe fixer.

## Research brief

- **Decision:** retain a narrowly scoped rule-interaction test-helper hypothesis; do not build a replacement linter, generic autofix wrapper or hook scheduler.
- **Target customer:** maintainers of custom JavaScript ESLint rules that introduce references, rename bindings or remove declarations.
- **Geography:** English-language open-source tooling communities; no regulatory claim.
- **Substitutes:** ESLint RuleTester and Node APIs, widened fix ranges, editor individual-fix actions, a small fixture script, and lint-staged task sequencing for a different concurrency problem.
- **Time horizon:** a one-to-three-day, single-file JavaScript test-helper prototype, only after comparison with a prepared native fixture.
- **Must-answer question:** does a reusable interaction trace reduce real plugin debugging effort enough to beat a short native test and a well-formed issue template?
- **Evidence bar:** one fresh Reddit discussion, an older original demonstration and official tool documentation. No interviews, measured savings, independent production reproductions or willingness-to-pay evidence.
- **Creative constraint:** “Subtract” — keep the fixture comparison; remove production editing, generalized safety claims and dashboard scope.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Fresh public discussion, recovered through HTML | [Problem with concurrent linter fixes](https://www.reddit.com/r/webdev/comments/1xsvghv/problem_with_concurrent_linter_fixes/) | The November 10 discussion was about 13 hours old when fetched. Visible comments discuss non-overlapping but semantically interacting fixes. One commenter reports a separate ESLint/codemod last-writer-wins hook race and says serialization worked. These mechanisms must not be conflated. |
| Original technical article, published August 26, 2026 | [Problem with concurrent linter fixes](https://jfmengels.net/concurrent-linter-fixes/) | A utility-introducing fix and an unused-function-removal fix can be textually disjoint yet produce a dangling reference when combined. Crucial counterevidence: the author calls this rare, says they have not encountered it in practice, and labels the demonstration rules naive and unsuitable for real projects. The fresh Reddit share does not make this a newly discovered ESLint regression. |
| Original public demonstration | [eslint-concurrent-fixes-sscce](https://github.com/jfmengels/eslint-concurrent-fixes-sscce) | A source fixture and custom-rule implementation already exist. This is the same author's demonstration, not an independent affected customer. It was inspected, not executed in this run. |
| Official native substitute documentation | [Custom rules: applying and conflicting fixes](https://eslint.org/docs/latest/extend/custom-rules#applying-fixes) | ESLint re-runs enabled rules after applying fixes, up to ten times. It documents intentionally extending a fix's range to prevent surrounding fixes in the same pass, suggestions for unsuitable autofixes, and RuleTester. A new tool cannot claim ESLint has no interaction-control primitives. |
| Official native API documentation | [Node.js API](https://eslint.org/docs/latest/integrate/nodejs-api) | The documented APIs expose lint messages and edit information, autofix filtering and rule-testing utilities. A short maintained script is a serious baseline; an external package is not automatically necessary. |
| Official existing diagnostics | [Circular fixes troubleshooting](https://eslint.org/docs/latest/use/troubleshooting/circular-fixes) | ESLint already warns about detected fix cycles and documents using an editor's individual-fix action to identify conflicting rules. A semantic reference break need not be a cycle; the proposed tool must distinguish the two. |
| Original adjacent-tool documentation | [lint-staged task concurrency](https://github.com/lint-staged/lint-staged#task-concurrency) | Task arrays run sequentially and concurrency can be disabled. This is strong counterevidence to a new hook-serialization product, not proof that serializing processes solves interactions among fixes within one ESLint pass. |

**Confidence:** medium that the illustrated interaction is technically meaningful; low that it supports a separate product. Several comments echo the same example, so they are not counted as independent production incidents. The one concrete hook-race report describes a different mechanism and an already successful workaround. No claim about Biome's implementation is adopted from comments.

## Shortlist: competitor and wedge-first gate before scoring

Three software candidates were checked. Only the narrowed survivor receives a numeric score; rejected ideas do not earn feasibility points to offset a failed wedge.

### 1. FixInterleave — narrowed and retained

**Wedge-first line:** maintainer of a custom reference-changing ESLint plugin → RuleTester, native APIs, widened ranges and editor single-fix actions → isolated rule tests may not explain an interaction with another enabled rule, but a prepared native combined-rule fixture has not been shown inadequate → bounded fixture-level batch versus single-fix traces with a caller-defined outcome assertion → exact plugin interaction bug searches and maintainer-approved regression examples in affected plugin repositories → a fresh discussion revives a concrete older demonstration, not evidence of a new platform defect or widespread demand.

- **Direct functional competitors:** ESLint's own test/API/editor workflow; the author's existing SSCCE. elm-review is an architectural substitute for Elm, not a drop-in JavaScript replacement.
- **Indirect substitutes:** a short combined-rule test, source diffs, ordinary tests/type checking and an issue template.
- **Status quo:** disable or narrow the problematic autofix, adjust its declared range, offer a suggestion instead, and add a regression test. This may already be the best solution.
- **Gate result:** reject a “safe ESLint” wrapper and generic hook scheduler. Retain only an unvalidated test-helper wedge for known interaction fixtures.
- **Kill:** if a prepared native fixture is equally easy to create and interpret, contribute a recipe or test instead of creating a standalone product.

### 2. ClaudeSpendLens — rejected before scoring

**Wedge-first line:** Claude Enterprise IT owner answering a finance spending question → native usage dashboard/exports, Analytics API and spend controls → a fresh author wants prompt-level explanations and reports a bypassable desktop-only POC, but that account does not establish missing native usage reporting → a proposed external spend dashboard duplicates documented native capabilities without a proven narrower gap → specific Claude Enterprise administration questions → current public confusion is an education opportunity, not proof of a missing dashboard.

- **Signal:** [What product are you using to manage Claude Enterprise?](https://www.reddit.com/r/sysadmin/comments/1xt947q/what_product_are_you_using_to_manage_claude/), November 11. The author's description of Airia's scope/cost is their POC account, not an independently tested universal product fact.
- **Direct/native competitor:** [Anthropic's admin visibility and control article](https://claude.com/resources/articles/giving-admins-more-visibility-and-control-over-claude-usage-and-spend) documents per-user/group costs, exports, Analytics API, model controls and spend alerts. It names Datadog Cloud Cost Management and CloudZero as existing reporting destinations.
- **Indirect substitute / status quo:** native limits plus manager-owned increase approvals in the existing service desk; the visible discussion recommends this workflow. Usage metadata is not the full content or business justification of every prompt.
- **Kill:** crowded LLM spend/observability category, strong native substitute, no validated distribution or workflow gap. Do not build a surveillance layer, assume desktop interception covers web traffic, or equate token totals with productivity.

### 3. FirstDayHours — rejected before scoring

**Wedge-first line:** IAM administrator checking a new starter's access before laptop shipment → SailPoint provisioning, AD attributes/PowerShell, ADManager Plus and existing deployment processes → the source reports a Monday lockout after requested Tuesday–Friday hours, but also says a later attribute check found unrestricted hours → a proposed first-day schedule receipt cannot resolve organizational disagreement or establish the historical restriction → specific IAM/desktop handoff questions → today's incident motivates correcting the process, not buying another account report.

- **Signal:** [When Tribal Knowledge Becomes IT Policy](https://www.reddit.com/r/sysadmin/comments/1xt6lnm/when_tribal_knowledge_becomes_it_policy/). Read the post and visible comments: the author already used a PowerShell attribute check; another commenter reports hours of manual profile work, but that does not establish demand for a logon-hours app.
- **Direct competitor:** [ADManager Plus logon reports](https://www.manageengine.com/products/ad-manager/windows-active-directory-logon-reports.html) documents logon-hours reporting and management. Existing native attribute inspection already helped this author.
- **Indirect substitute / status quo:** an approved onboarding checklist, clear ownership and a corrected deployment workflow. [Windows Autopilot pre-provisioning](https://learn.microsoft.com/en-us/autopilot/pre-provision) separates technician and user phases, subject to documented device, licensing and targeting requirements; it does not pre-apply every user policy or guarantee every organization can migrate immediately.
- **Kill:** no demonstrated technical reporting gap; resistance to a safer process is not fixed by a new app. No credential handling, account modifications or automated restrictions proposed.

## Problem

A custom rule's fixture can pass in isolation while its edit interacts badly with another rule. A maintainer then needs to identify the relevant source state, proposed edits and assertion failure, not merely see the final diff. Textual non-overlap is not semantic independence.

Keep three distinct problems separate: simultaneous semantic edits within a lint pass, cyclic edits across passes, and independent processes overwriting the same file. A single-file run does not prevent the first problem: the original example is already a single file.

**Status-quo pain test:** broken references can block a build or introduce defects, which is consequential enough to investigate. However, the source author explicitly reports rarity and no direct production experience. No greater-than-30-minutes weekly burden or recurring unresolved maintainer workflow is established. This is why the idea remains a validation hypothesis rather than an authorized build.

## Target user

An ESLint plugin maintainer with a trusted local custom-rule fixture and a specific interaction to test. Not every JavaScript developer, an enterprise code-scanning buyer or a user seeking guaranteed automated refactoring safety.

## MVP scope

Proposed software only; no CLI was built or benchmarked today.

1. A Node CLI accepting one explicitly supplied JavaScript fixture, trusted flat config, selected rule IDs and a caller-defined expected diagnostic/output assertion. Pin the ESLint, parser, plugin and Node versions in the fixture record.
2. Use documented APIs to collect diagnostics and fix edit information. Compare native combined fixing against a bounded trace that selects one reported fix and re-analyzes after every application. Preserve rule IDs, source states, edit ranges, chosen ordering and stop reasons.
3. Compare two explicit selection orders for the selected fixture, not all possible interleavings. Keep a maximum step count, repeat-state detection and timeout. A stopped or unsupported trace is inconclusive, not a pass. Differences alone do not identify a bug.
4. Evaluate the maintainer's assertion on the original and each relevant result. A parse check does not catch all unresolved references; a clean lint/type/test result does not prove unchanged behavior. Record exactly which checks ran and their limits. Assertion failures are candidates for review, not automatic blame attribution to a rule pair.
5. Produce escaped local JSON/HTML traces and an opt-in regression-fixture template. Do not automatically upload source, reduce/rewrite a production repository, publish issues or change the working tree.
6. Initially exclude custom processors, multi-file fixes, TypeScript project services and arbitrary hook orchestration. Suggestions are not silently converted into autofixes. Version/config incompatibility must be reported explicitly rather than approximated as support.

**Execution boundary:** loading ESLint configuration/plugins executes JavaScript. “Local” and a child-process timeout are not a sandbox. Use only deliberately trusted fixtures in a disposable, permission-limited environment; do not accept untrusted uploaded repositories. Do not automatically execute package installation, fixture programs or arbitrary project tests. Any future assertion command requires explicit operator configuration and its own isolation. Code snippets and reports can contain proprietary material; keep public examples synthetic or permissioned, escape report content and never treat hashes as anonymization.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct native test workflow | [ESLint RuleTester and Node API](https://eslint.org/docs/latest/integrate/nodejs-api) | Already exposes the primitives for fixture assertions and combined configuration tests. Benchmark a prepared script, not a blank editor. |
| Native prevention/mitigation | [Widened fix ranges and suggestions](https://eslint.org/docs/latest/extend/custom-rules#applying-fixes) | Documented ways to prevent same-pass surrounding edits or avoid inappropriate autofixing. They may eliminate the need for a helper for a given rule. |
| Native diagnostic workflow | [Circular fixes and editor individual actions](https://eslint.org/docs/latest/use/troubleshooting/circular-fixes) | Existing interactive debugging is a real substitute; circular detection is not general semantic validation. |
| Existing demonstration | [Author's SSCCE](https://github.com/jfmengels/eslint-concurrent-fixes-sscce) | Already packages the illustrative problem. Repackaging it is not a defensible product by itself. |
| Adjacent task runner | [lint-staged](https://github.com/lint-staged/lint-staged#task-concurrency) | Sequential commands and concurrency settings already address many cross-process write races. Not equivalent to within-pass rule interactions. |
| Indirect substitute / status quo | Combined-rule test, assertion script, editor diff and narrowed autofix | Often enough for an occasional bug. Prefer an upstream test/example if total effort is equal or lower. |

## Wedge

The only retained wedge is **reusable, assertion-linked interaction traces for plugin regression fixtures**, not more linting, a promise of safe edits or another scheduler. The native APIs and documented range controls substantially weaken the standalone product case. No hands-on benchmark has demonstrated an advantage.

**Distribution hypothesis:** publish a minimal synthetic reference-introduction/removal fixture and a companion native test, answering exact “ESLint non-overlapping autofix interaction” searches; seek invited review or maintainer-approved placement in affected plugin test documentation. Those are concrete users and topics, but there is no confirmed recurring channel or access. Distribution stays 3/5. No social replies or outreach were sent.

## Kill condition

Reject a standalone app if any holds:

- RuleTester plus a prepared combined-rule script and individual-fix editor workflow gives equally accurate explanations at equal or lower total setup/review effort.
- Two actual plugin maintainers cannot supply distinct real interaction fixtures or describe recurring debugging need. Repeated discussion of the same toy example is insufficient.
- Widening the appropriate declared range, using suggestions or correcting a hook's existing sequencing solves the relevant job without a new tool.
- Useful output requires undocumented ESLint internals, exhaustive order exploration or claims that selected successful traces prove semantic safety.
- A reusable native fixture recipe or upstream regression test is sufficient; favor that narrower contribution.

## Scoring

Assigned after the competitor gate and narrowing.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 3/5 | A real illustrated correctness risk, but the original author explicitly calls it rare. Recurring production debugging pain is unverified. |
| Feasibility | 4/5 | A bounded single-file trusted-config fixture comparison is plausible in one to three days. General correctness and ecosystem-wide compatibility are excluded. |
| Demo potential | 4/5 | A combined dangling-reference result beside two different single-fix traces is easy to explain. This is a proposed demo, not executed output. |
| Distribution | 3/5 | Specific plugin-maintainer/search topics exist; repeatable access, placement and adoption remain unproven. |
| Competitive wedge / timing | 2/5 | Fresh discussion, older demonstration, strong native APIs and mitigation controls. No measured product gap. |
| Total | 16/25 | Below 18; both dimension gates also fail. |

## Decision

**Idea-only. No dedicated project repo created.** FixInterleave is today's strongest retained software research hypothesis, not a validated build opportunity. Weakest dimension: competitive wedge/timing at 2/5; Distribution is 3/5. Reject the broader safe-fixer and hook-scheduler variants.

The evidence supports a native-fixture comparison first. It does not establish a new ESLint regression, independent recurring demand, paid-market size or semantic correctness of serial fixing.

## Next build step

If pursued, make one validation-sized fixture commit with synthetic same-pass reference interaction, a circular-fix case and a separate serialized-hook control, plus explicit expected assertions and a prepared native ESLint baseline. Compare full fixture setup and diagnosis effort with two plugin maintainers before extracting a CLI package. Favor a native regression example if sufficient.

Follow-up is tracked in Beads (`apps-m7o`). No upstream issue, social reply, customer outreach or code execution from the demonstration was performed.

## Source access caveats

- Canonical `reddit-readonly posts` calls used small limits. r/sysadmin and r/Entrepreneur JSON requests were blocked with HTTP 403/theme-beta and returned RSS fallback posts. r/selfhosted and r/webdev calls returned HTTP 429; no tight retry loop. RSS score/comment counts are unavailable placeholders and were not used to establish demand.
- Reddit-constrained web search returned no results for the fresh date queries. A broader selfhosted query returned older posts that were not treated as fresh demand. Public HTML extraction recovered selfhosted/webdev listings and selected full posts with visible comments. Collapsed discussion was not exhaustively expanded. HTML recovery, not successful RSS, supplied the winner's thread.
- `xurl whoami` succeeded, but read-only search returned HTTP 401 Unauthorized. No OAuth2 user was configured, so no interactive login or credential change was attempted. X-constrained web search found unrelated requests with unverified recency; none validates this winner.
- Some concrete general competitor queries also returned no results. Official documentation was fetched directly instead of inferring missing features from search silence. The original article's August publication date is preserved separately from the fresh Reddit share.
- Vendor capabilities are documentation claims, not hands-on product acceptance tests. No demonstration, maintainer interview, benchmark or measured savings is claimed.

## Repository verification caveat

The existing repository-wide snapshot verifier still fails with `KeyError: 'source_commit'`, tracked in Beads (`apps-mq0`). No snapshot/verifier code changed today. Daily JSON, brief/index consistency and focused public-safety checks are separate from that failing repository-wide check; this run does not claim a green full suite.
