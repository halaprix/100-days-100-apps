# Day 094 — MenuRuleDiff

Date: 2026-10-30
Status: idea-only

## One-line pitch

An offline menu-rule comparison app for agencies moving restaurants off GloriaFood: reveal lost size-specific modifiers, selection constraints and unresolved price mappings before approving a replacement menu, starting with TastyIgniter.

## Research brief

- Decision: select one software bet, not another restaurant ordering platform; create a project only when the total and both dimension gates pass.
- Target customer: a small restaurant-web agency responsible for multiple GloriaFood migrations, especially to self-hosted TastyIgniter.
- Geography: English-language agency workflow; no jurisdiction-specific tax or food-safety certification.
- Category/substitutes: native menu exports, existing migration services, TastyIgniter Import/Export, a prepared comparison worksheet and manual menu review.
- Time horizon: a 1–3 day bounded comparison prototype after validation, not a production migration service.
- Must-answer questions: can target-side option relationships actually be exported; does an independent comparison save review time beyond an existing importer and onboarding specialist; will agencies supply real cases?
- Evidence bar: current community context plus original shutdown notices, source schema and target documentation. No interviews, real restaurant migrations, willingness-to-pay evidence or timed benchmark were obtained.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Public community report, 2026-10-30; RSS discovery and full page/visible comments read | [GloriaFood shutdown: notes for self-hosters](https://www.reddit.com/r/selfhosted/comments/1xj6qzf/oracle_is_shutting_down_gloriafood_a_free/) | A software/web builder warns about replacement ordering systems, maintenance and handover burden. This is a commercially interested builder's analysis, not a restaurant customer requesting this app. The comments do not establish independent migration demand. |
| Original product notice, retrieved today | [GloriaFood homepage](https://www.gloriafood.com/) | States end of life on **April 30, 2027**, continued support through that date, no direct Oracle replacement, and points to independent provider FoodAmigos. A real forced-transition window, not proof of an unserved category. |
| Original corporate notice, retrieved today | [Oracle Food and Beverage](https://www.oracle.com/food-beverage/) | States full end of service on **March 31, 2027**, disagreeing with the product homepage. Preserve both dates; plan conservatively before the earlier date rather than silently resolving the conflict. |
| Original integration documentation and example payload | [Fetch Menu API v2](https://github.com/GlobalFood/integration_docs/blob/master/fetch_menu/README.md) and [example JSON](https://github.com/GlobalFood/integration_docs/blob/master/fetch_menu/payload/menu.json) | Categories, items and sizes can each carry option groups. Documented group fields include `required`, `allow_quantity`, `force_min` and `force_max`; options have price/default fields. The example includes different topping prices by pizza size and an optional group with `force_min: 1`. A row-count match does not establish rule equivalence. |
| Original substitute documentation; strong counterevidence to a new exporter | [TastyIgniter Import/Export](https://tastyigniter.com/docs/extensions/importexport) and [extension repository](https://github.com/igniter-labs/ti-ext-importexport) | Existing CSV import/export, column mapping and custom export types already cover data movement. A small custom export plus a worksheet may solve the proposed review job. A complete option-relation export has not been exercised. |
| Original target documentation and resolved feature discussion | [Managing menu options](https://tastyigniter.com/support/articles/managing-menu-items-options) and [TastyIgniter issue 1178](https://github.com/tastyigniter/TastyIgniter/issues/1178) | Native options already support several display types and per-choice prices. The free-quantity feature request is **closed as completed**, with the maintainer saying it shipped in Cart v4.3.1. Its discussion illustrates ambiguous free-choice pricing, not a current missing feature or a fresh demand signal. |
| Competing vendor documentation; claims not independently tested | [Ontabee exporter](https://ontabee.com/gloriafood-menu-export/), [its export guide](https://ontabee.com/guides/gloriafood-menu-export/) and [Menuthere migration guide](https://menuthere.com/gloriafood-alternative/migration-guide) | Ontabee already offers a portable JSON export and explicitly discusses size-scoped groups and constraints. Menuthere already imports categories, items, sizes and add-ons. Exporting or preserving nesting alone is not a wedge. |
| Original competing migration-service announcement | [Restolabs migration program](https://www.restolabs.com/newsroom-press-releases/restolabs-launches-dedicated-migration-program-for-gloriafood-restaurants-and-reseller-partners) | Advertises automated migration, modifier/settings transfer, agency/reseller support and specialist accuracy review before launch. Human QA is already part of a strong substitute. Vendor claims do not prove its review is deficient. |

## Problem

A menu can retain every dish name while changing which options belong to a size, how many choices are allowed, or which choices carry a surcharge. The source schema demonstrates that this comparison is more complex than checking item counts or a flat price list.

The commercial harm is plausible: incorrect prices or choices can lose money or delay a restaurant's relaunch. The impending shutdown supplies real timing. However, no restaurant in today's sources reports a failed migration caused by these exact mappings, and no agency has demonstrated recurring review work exceeding thirty minutes. Distinguish **schema-level risk** from **observed customer pain**.

**Status-quo pain test:** this is a launch/revenue-risk hypothesis, not a claimed measured weekly saving. Existing guided migration and test-order processes may already make the workaround tolerable. The proposal remains idea-only until an agency shows material incremental review burden.

## Target user

An agency engineer and restaurant owner jointly signing off an existing GloriaFood menu rebuilt in a specific TastyIgniter/Cart version. Not an independent restaurant choosing its first ordering platform, and not a buyer seeking payment processing, a POS or an ordering engine.

## MVP scope

Constraint: **Nothing new except glue** — compare existing menu structures instead of rebuilding ordering, checkout or migration.

1. Read an operator-supplied GloriaFood Fetch Menu JSON file locally. No credentials, API calls or customer/order-history data in the initial app. Retain source location/currency, export timestamp and exact field paths.
2. Read a versioned target snapshot with items, option-group attachments, prices, defaults and selection settings. First validate whether existing TastyIgniter exports plus a small custom export type can supply these fields. A flat CSV without relationships is incomplete input, not evidence that the destination lost options.
3. Require explicit source-to-target mapping for category/item/size/group identities. Never silently match duplicate names or compare unrelated restaurant locations. Preserve category-, item- and size-level attachments without assuming undocumented inheritance or override rules.
4. Show structural differences and unresolved interpretations: dropped attachments, changed constraints/defaults/quantity settings, currency mismatches and unreviewed price fields. Preserve `required` separately from `force_min`; do not turn an optional group's minimum into an unconditional required selection. Retain raw price components rather than treating size prices as either absolute or additive without verified semantics.
5. Produce a local, escaped HTML comparison with source pointers, target version, mapping decisions and review coverage. Separate `different`, `unmapped`, `unsupported` and `not checked`; never produce an all-clear from equal counts or missing target data. Intentional changes require explicit owner acknowledgement.

Boundaries: no import writes, checkout automation, order placement, payment/refund, tax engine, printer tests, browser scraping or automatic go-live approval. No claim of complete cart-total equivalence, allergen safety, legal compliance, image-transfer rights or operational readiness. Undocumented API fields are not a stable contract. Missing settings such as delivery/payment configuration remain outside menu comparison, not silently approved.

A bounded parser/comparison UI is plausible in 1–3 days **once a usable target snapshot exists**. A reliable target adapter and pricing-semantic verification are prerequisites, not assumed completed work. No app, adapter or live migration was built today.

## Shortlist — competitor and wedge-first gates before scoring

Four software candidates were considered. The following gates precede the winner's numeric scoring; rejected candidates receive no rescue scores.

### 1. MenuRuleDiff — narrow and retain as research winner

**Wedge-first line:** agency signing off a GloriaFood-to-TastyIgniter menu → native export/custom CSV, Ontabee export, destination importer and specialist review → these already transfer data, but independent source-to-target rule review may still require manual reconciliation; that burden is unmeasured → offline relationship/constraint comparison with explicit unknowns, not another exporter → a reproducible TastyIgniter migration walkthrough, extension/community reviewers and exact size-modifier migration search queries → verified GloriaFood shutdown with conflicting official dates and a source schema containing nested rule attachments.

- Direct/near-direct: Ontabee export/migration, Menuthere import and Restolabs migration QA. These substantially weaken any claim of an unmet migration category.
- Indirect: TastyIgniter custom exports, prepared worksheet, agency onboarding and operator-run test orders.
- Status quo: choose a supported destination, use its migration service and review the menu manually.
- Gate result: retain only the independent semantic-review hypothesis. It has a specific user, artifact and acquisition experiment, but no verified comparative advantage or repeatable access. Kill it if a prepared worksheet or existing onboarding suffices.

### 2. ApiSweep — reject before scoring

Fresh source, full post and visible comments read: [API Discovery / Inventory?](https://www.reddit.com/r/sysadmin/comments/1xj8a16/api_discovery_inventory/).

**Wedge-first line:** sysadmin unsure which APIs exist across servers, containers and serverless → Akto plus gateway inventory, ZAP/Nmap and source-code search → the source has not yet separated undocumented routes from undiscovered services, so a specific substitute failure is unproven → proposed unified inventory → exact API-inventory setup examples → today's explicit request, but no verified new platform constraint.

- Direct competitor checked: [Akto Code](https://www.akto.io/blog/introducing-akto-code-automated-api-discovery-from-source-code) already advertises source discovery, traffic connectors and code/runtime correlation. This is vendor documentation, not a benchmark.
- Indirect: the thread describes crawling, port discovery and code-route searches; these are community suggestions, not actions performed by this run.
- Status quo: clarify coverage requirements and deploy an existing discovery tool.
- Kill condition fired: crowded security/inventory space, broad scope and no validated narrow workflow wedge. A credible heterogeneous discovery MVP exceeds a small glue app. Reject.

### 3. RoomFinderDiff — reject before scoring

Fresh source, full post and visible comments read: [Classic Outlook issues](https://www.reddit.com/r/sysadmin/comments/1xj7nvu/classic_outlook_issues/).

**Wedge-first line:** endpoint engineer handling intermittent empty Room Finder and people-search results for hundreds of users → Microsoft configuration guidance, support and a working/failing-machine checklist → repeated repairs have not fixed the reported problem, but missing comparison tooling is not established → proposed local client-state comparison → exact Room Finder incident queries and opt-in endpoint reviewers → today's incident and a similar anecdotal comment, not a confirmed WebView root cause.

- Native/direct substitute checked: [Microsoft's Room Finder controls](https://learn.microsoft.com/en-us/microsoft-365-apps/outlook/calendaring/room-finder) already explain UI behavior, registry controls and an adjacent outside-working-hours issue. None diagnoses this incident.
- Indirect: support ticket, native diagnostics and a prepared paired-machine worksheet. The source already tried profile recreation, add-in/safe-mode tests and WebView repair.
- Status quo: continue supported diagnosis or evaluate another Outlook client; no evidence establishes either as a successful fix here.
- Kill condition fired: another generic diagnostic packet without proof of a missing comparison workflow. Cannot infer causality from simultaneous symptoms or anecdotal cache suggestions. Reject before scoring.

### 4. IsolationReturn — reject before scoring

Fresh source, full post and visible comments read: [DNSFilter with SentinelOne](https://www.reddit.com/r/sysadmin/comments/1xj4es4/dnsfilter_with_sentinelone/).

**Wedge-first line:** MSP facing devices that do not reconnect after security remediation → DNSFilter/SentinelOne policy review, vendor diagnostics and onsite support → author reports costly repeated recovery, but exact filtering mode and isolation state are unknown → proposed passive reconnect checklist → precise product-pair troubleshooting examples → today's incident, while vendor guidance already addresses an overlapping quarantine/DNS interaction.

- Direct/native substitute checked: [DNSFilter PreCheck compatibility guidance](https://help.dnsfilter.com/hc/en-us/articles/48215608450323-DNS-PreCheck-VPN-compatibility-for-Windows-Roaming-Client) includes SentinelOne quarantine/DNS considerations and diagnostic/support instructions. Scope is DNS PreCheck; it is not proof of this incident's mode or cause.
- Indirect: existing diagnostic logs and joint vendor review. Community suggestions about exceptions or uninstalling security tools are not validated remediation.
- Status quo: preserve protections and follow an authorized, vendor-supported incident process.
- Kill condition fired: an existing native support path addresses the apparent wedge; a generic checklist adds little, while automated reconnect or policy modification would introduce security risk. Reject; no isolation, firewall, service or agent changes performed.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct/near-direct | [Ontabee export and migration](https://ontabee.com/guides/gloriafood-menu-export/) | Already offers portable menu JSON and claims to preserve size groups/min-max constraints. A free local exporter alone cannot justify this product. Independent target comparison has not been benchmarked against it. |
| Direct/near-direct | [Menuthere migration](https://menuthere.com/gloriafood-alternative/migration-guide) | Existing menu import, preview and detailed operational checklist. Its guide includes test orders; do not claim an app replaces those or that the importer loses modifiers. |
| Direct service | [Restolabs migration program](https://www.restolabs.com/newsroom-press-releases/restolabs-launches-dedicated-migration-program-for-gloriafood-restaurants-and-reseller-partners) | Automation, specialist validation and reseller support already target agencies. This may eliminate the need for a separate review product for its customers. |
| Native/indirect | [TastyIgniter Import/Export](https://tastyigniter.com/docs/extensions/importexport) | Existing custom types are an implementation path and a substitute. Review actual exported relationships and Cart version before claiming a gap. |
| Indirect | Prepared worksheet plus a short schema-aware script | May already compare a small menu quickly. Benchmark a prepared workflow, not an empty spreadsheet or raw JSON side by side. |
| Status quo | Destination onboarding, owner menu review and controlled test orders | Strongest practical competitor. Incremental time saved by independent comparison is currently unknown. |

## Wedge

**Independent, local source-to-target rule review**, not migration automation, data portability or another ordering platform. A restaurant can retain a review artifact regardless of its chosen vendor, with unresolved mappings visible rather than hidden behind a successful import count.

The technical surface is concrete: original source documentation has category/item/size groups and separate required/minimum/quantity fields. The commercial advantage remains a hypothesis. Existing exporters already discuss precisely these structures, and existing migration services already include accuracy checks. No retrieved source proves they fail. Timing earns credit because the shutdown is independently confirmed; it does not erase strong substitutes.

First-user experiment: publish a reproducible, clearly synthetic TastyIgniter migration example addressing size-scoped modifiers and ambiguous price fields, then seek opt-in agency/extension-maintainer review through the documented TastyIgniter community routes. No posts or outreach were made today. A channel design is not demonstrated repeatable access, so Distribution remains 3/5.

## Kill condition

Stop or reduce to a worksheet/upstream extension if any condition holds:

- Two independent opt-in agency cases do not reveal material review burden or launch risk after using the destination's existing importer and QA.
- A prepared worksheet plus native/custom export produces equivalent useful findings in ten minutes, or the prototype cannot save at least thirty minutes across a real multi-menu sign-off. These are validation targets, not measured savings.
- Target relationships cannot be acquired without unsupported scraping or disproportionate custom integration; flat data must never be presented as complete comparison coverage.
- Correct findings require implementing both checkout engines or interpreting undocumented inheritance/pricing behavior. Keep these cases unknown or abandon the 1–3 day scope.
- Existing Ontabee/Menuthere/Restolabs workflows already provide the independent comparison operators need, or agencies prefer their included onboarding.
- No repeatable opt-in reviewer/search channel emerges. A one-time shutdown cohort alone is not durable distribution.

## Scoring

Assigned after competitor and wedge-first gates above.

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Real migration deadline and concrete menu-rule risk; incremental agency pain is not yet measured. |
| Feasibility | 4/5 | Offline structure comparison is bounded; target snapshot and price-semantic checks are prerequisites. No complete checkout equivalence claim. |
| Demo potential | 4/5 | A clearly synthetic before/after menu can expose lost size attachments despite equal item counts, plus an explicit unknown case. No demo built today. |
| Distribution | 3/5 | Specific agency/TastyIgniter audience and exact migration walkthrough experiment, but no committed reviewers or demonstrated repeatable access. |
| Competitive wedge / timing | 3/5 | Independently verified shutdown and a precise review surface; strong exporters and included migration QA leave the standalone wedge provisional. |
| Total | 18/25 | Total clears 18 and wedge meets 3, but Distribution misses the required 4/5 gate. |

## Decision

**idea-only. No dedicated repository or scaffold created.** Weakest dimensions are Distribution and competitive wedge/timing, tied at 3/5; Distribution is the blocking creation gate.

Recommendation: validate independent rule-review value before writing a product. Avoid a new ordering platform and reject a generic menu exporter. Confidence is high in the shutdown and source-schema complexity, but low in standalone demand and moderate-to-low in the target-adapter feasibility. No market-size, prevalence, price or willingness-to-pay estimate is justified. Comparative evidence, usable real target exports and an opt-in reviewer channel would change this decision.

## Next build step

One validation commit: a clearly synthetic source/target fixture and expected rule-diff matrix covering category-level crust, size-specific toppings, optional groups with a minimum, duplicate names, an intentionally changed price, incomplete target coverage and unknown pricing semantics. Compare it against a prepared worksheet and TastyIgniter's existing export/custom-type route before implementing adapters. Require explicit target/Cart versions and agency review; record timing rather than assuming savings. Follow-up: Beads `apps-346`.

## Source access caveats

- The canonical read-only find requested six recent posts each from r/sysadmin, r/selfhosted and r/webdev, within 48 hours. r/sysadmin public JSON returned HTTP 403 and RSS supplied six posts. r/selfhosted and r/webdev were initially unavailable through the chain with HTTP 429. A later small r/selfhosted `posts` probe succeeded via RSS after JSON returned HTTP 403, yielding six posts. No tight retry loop; r/webdev was not recovered.
- RSS score/comment counts are unknown placeholders. Full web extraction subsequently retrieved all four shortlisted posts and visible comments; that is separate from public JSON access and not exhaustive comment access. The winner's evidence table excludes unrelated incident posts.
- X account lookup succeeded; a small search returned HTTP 401 Unauthorized. No OAuth2 user was listed. An attempted OAuth2 search unexpectedly started an interactive listener and timed out; it supplied no posts. No further authentication or search attempts were made. X-constrained web search returned no results, so no X validation is claimed.
- Several narrowly phrased Reddit/X/vendor searches returned empty sets; broader named-product queries and direct original pages recovered useful evidence. Empty results are not proof of absent competitors.
- The Foodiv migration URL returned a localized general product page rather than the requested article. Its search snippet is only a discovery lead, not verified feature evidence. A searched Akto documentation path returned a GitHub 404 and was discarded; the retrieved original Akto announcement supports the competitor finding instead.
- Original Oracle/GloriaFood notices disagree on the cutoff date. Some vendor search titles still say March while fetched pages say April. Use the retrieved original notices, preserve the discrepancy, and plan before March 31, 2027 pending clarification.
- Vendor export/pricing claims and target feature documentation were read, not exercised. TastyIgniter issue 1178 was resolved, not current unmet demand. No private keys, restaurant accounts, orders, payments or menu writes were accessed.
