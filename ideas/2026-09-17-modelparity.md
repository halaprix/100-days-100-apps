# Day 083 — ModelParity

Date: 2026-09-17
Status: idea-only

## One-line pitch

A local CLI that turns a selected Excel pricing workbook plus approved input cases
into a redacted golden-test packet, then compares those expected results with a
replacement app or pricing API before the spreadsheet is retired.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Community report — Reddit, retrieved through public web extraction | [r/SaaS: calculation sheet in vertical SaaS](https://www.reddit.com/r/SaaS/comments/1wimfj7/for_vertical_saas_the_customers_calculation_sheet/) | A fresh post describes vertical-SaaS quoting where routine form inputs coexist with inspectable, editable calculation sheets for negotiated or exceptional cases. It explicitly says the cited UI demo is not a migration service for existing workbooks. [1] |
| Direct competitor — migration/extraction platform | [Power Accelerate Excel Assessment & Extraction Tool](https://www.poweraccelerate.com/excel-assessment-tool.html) | It inventories formulas, VBA, and workbook complexity, then routes workbooks toward Power Platform targets and rebuild work. This validates that spreadsheet-as-application migration is a real job, while setting a high incumbent bar. [2] |
| Direct substitute — workbook inspection | [TraceModel](https://www.tracemodel.com/) | TraceModel maps Excel formula and cross-sheet dependencies locally and exports structured dependency data; it helps understand the source model but does not claim to compare source results against a replacement service. [3] |
| Direct substitute — formula audit | [SheetLens](https://sheetlens.app/) | SheetLens provides local dependency maps and flags volatile functions, hard-coded numbers, errors, circular references, inputs, and outputs. A migration product cannot pretend source discovery is an unserved problem. [4] |
| Direct competitor — keep Excel as runtime | [CLE pricing logic](https://cle.contene.com/en/use-cases/pricing-logic/) | CLE exposes Excel pricing models through a decision API rather than requiring code to reproduce their pricing logic. That is a credible alternative when a team can retain Excel, rather than replace it. [5] |

## Problem

A spreadsheet-heavy business may want a customer-facing quoting flow, a Power
Platform rebuild, or a pricing API. The difficult part is not locating formulas;
it is proving that the replacement preserves the business cases people actually
care about: tier boundaries, customer-specific discounts, lookup-table paths,
and negotiated exceptions.

The status quo is manual UAT: an operator changes values in a workbook, re-enters
them into the new app, and compares a few totals by eye. That routinely exceeds
30 minutes per change cycle for a nontrivial quoting model and can turn a missed
case into an incorrect quote or margin loss. Formula maps and migration platforms
reduce discovery work, but they do not automatically become a portable,
reviewable source-versus-target acceptance suite.

## Target user

A small Power Platform or vertical-SaaS consultancy rebuilding one client-owned
Excel pricing workbook into a custom app or HTTP pricing endpoint, with a client
owner who must sign off that representative cases still calculate correctly.

## MVP scope

- Run locally against an explicit `.xlsx` workbook, a user-selected output cell,
  and CSV/JSON cases containing approved input values; upload nothing.
- Use a local spreadsheet engine to evaluate only the declared cases. Refuse to
  certify macro-enabled, external-link, volatile, or unsupported-formula cases
  rather than guessing.
- Emit a redacted JSON/Markdown packet: case identifier, input cell aliases,
  expected output, unsupported-feature warnings, and a source-workbook hash.
- Call an explicitly configured replacement HTTP endpoint or compare a saved
  target-result file; report exact per-case mismatches and tolerances.
- Include fixtures for a tiered discount, a failed lookup, and an unsupported
  external reference.

Non-goals: converting arbitrary workbooks into apps, executing VBA, hosting a
pricing service, or replacing CPQ software.

## Shortlist and wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| **ModelParity — selected** | Power Platform and vertical-SaaS consultancies rebuilding one client-owned pricing workbook → manual UAT, Excel-to-app migration services, dependency mappers, and Excel-as-API runtimes → these either discover/convert/run the workbook or require ad-hoc comparison, but do not provide a small source-versus-replacement acceptance packet for named business cases → local golden-case generator plus replacement API/file comparator → Excel-to-Power-Platform migration searches, consultancy implementation playbooks, and a reusable GitHub Action/CLI → a fresh vertical-SaaS discussion centers on retaining exceptional calculation behavior while modernizing the surrounding workflow. | Pass as an idea: the user, painful failure mode, and scope are specific. Distribution is concrete but not validated, so it cannot clear the repo gate. |
| **Customer quote portal from a workbook — rejected** | Small service businesses with a quote spreadsheet → Quotaire, CPQ tools, no-code calculators, and manual quotes → existing products already build online calculators and quotes from configured products/rules → generic quote portal → local service-business marketing → fresh spreadsheet discussion. | Reject: Quotaire already provides configurable internal/customer calculators, and CLE/servicePath-style products cover Excel-backed pricing. No evidence supports a distinct 1–3 day wedge. [5][6] |
| **Workbook dependency map — rejected** | Consultants inheriting an unfamiliar workbook → TraceModel, SheetLens, Excel auditing, and manual formula tracing → direct products already offer local dependency graphs, audit panels, and exports → another graph viewer → generic Excel/search traffic → fresh migration discussion. | Reject: the direct category is well served; a graph alone does not pass the status-quo or wedge test. [3][4] |
| **Phone-first Docker restart dashboard — rejected** | Self-hosters restarting containers away from a terminal → Portainer, Dockge, Komodo, SSH runbooks, and existing mobile dashboards → the fresh SideProject post is itself a working agentless Android dashboard, while container-management UIs are abundant → generic safer mobile controls → self-hosted communities → fresh app launch. | Reject: crowded server-dashboard category with no demonstrated workflow wedge; a new control surface would also create avoidable security scope. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Power Accelerate Excel Assessment & Extraction Tool | It scans formulas/VBA and produces migration-oriented output for Power Platform rebuilds. ModelParity must not duplicate estate assessment or code generation; it is only the independent acceptance check at the source/target boundary. [2] |
| Direct competitor | CLE Decision Engine API | Keeping Excel as the runtime avoids a parity migration entirely. ModelParity is relevant only when a team deliberately replaces the workbook or needs a proof that a second runtime agrees with it. [5] |
| Indirect substitute | TraceModel and SheetLens | Both make formulas and dependencies inspectable, locally. They are valuable preparation but do not replace execution of named cases against a target application. [3][4] |
| Indirect substitute | Manual UAT spreadsheet, screenshots, and a shared checklist | Cheap for a one-cell calculator, but brittle for pricing boundaries and hard to attach to a client sign-off or regression suite. |
| Status quo | Rebuild from formulas, then compare a few examples by eye | Teams tolerate it until an exception or discount rule produces an incorrect quote. The risk is financial and can block client acceptance. |

## Wedge

ModelParity is deliberately neither an Excel-to-app generator nor a quote
calculator. It asks a narrower question that migration and analysis tools leave
blurred: **does this declared replacement produce the same approved results as
this source workbook for these business cases?** The output is a portable,
redacted acceptance packet suitable for a client review and a CI regression
check.

The narrow first-user channel is consultancies already bidding or delivering
Excel-to-Power-Platform and vertical-SaaS migrations. A free CLI with
copy-pasteable fixtures and a GitHub Action could accompany searches and
implementation playbooks for that exact migration phrase. That is a specific
channel, but this run found no evidence yet that it is repeatable enough to
score Distribution above 3.

## Kill condition

Reject ModelParity if three migration consultancies show that their existing
conversion tooling already generates source-versus-target golden tests for real
workbooks, or that a short manual UAT checklist is accepted without recurring
rework. Also reject if representative inputs cannot be supplied without exposing
customer pricing, or if useful parity requires silently executing unsupported
VBA/external links instead of failing closed.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Pricing and exception mismatches can lose margin or delay client acceptance; evidence is a fresh single community report plus vendor material, not a prevalence study. |
| Feasibility | 4/5 | A local, narrow formula/case runner and file/HTTP comparator is feasible in 1–3 days; broad Excel/VBA compatibility is explicitly out of scope. |
| Demo potential | 5/5 | A spreadsheet case that passes, then a replacement response that fails at a tier boundary, is immediately legible. |
| Distribution | 3/5 | Excel-to-Power-Platform migration searches and consultancy playbooks are concrete but no repeatable first-user channel has been validated. |
| Competitive wedge / timing | 3/5 | Independent golden-case comparison is narrower than discovery, conversion, CPQ, or Excel-as-API products, but mature migration tools may already cover it. |
| Total | 19/25 | Above the numeric threshold, but blocked by the distribution gate. |

## Decision

**idea-only.** ModelParity scores **19/25** but does not qualify for a dedicated
repository because Distribution is **3/5**, below the required **4/5**. The
weakest dimension is Distribution. The competitor check also sets a strict
validation requirement: prove the independent parity packet is missing from
actual consultancy workflows before building.

## Next build step

Ask three Excel-to-Power-Platform or vertical-SaaS migration consultancies for a
redacted workbook, five already-approved business cases, and a replacement API
fixture; test whether a local parity packet catches a disagreement their current
migration tooling or UAT checklist misses.

## Source access caveats

Reddit's public JSON endpoint was blocked with the documented theme-beta `403`.
The read-only tool obtained recent r/SideProject and r/SaaS entries through its
RSS fallback, where scores and comment counts are unavailable and are not
claimed. The selected r/SaaS post was then retrieved directly through public web
extraction; it had no public replies at retrieval time. r/sysadmin, r/selfhosted,
and r/webdev hit RSS `429` after the JSON failure and were not retried. Web
search returned no usable fresh Reddit fallback results for those subreddits.

`xurl auth status` showed the default profile without OAuth2 credentials; the
read-only search probe returned `401 Unauthorized`. No X signal is used. Web
search and direct product pages were used for competitor validation, not as proof
of broad demand.

## Sources

[1] https://www.reddit.com/r/SaaS/comments/1wimfj7/for_vertical_saas_the_customers_calculation_sheet

[2] https://www.poweraccelerate.com/excel-assessment-tool.html

[3] https://www.tracemodel.com

[4] https://sheetlens.app

[5] https://cle.contene.com/en/use-cases/pricing-logic

[6] https://quotaire.com
