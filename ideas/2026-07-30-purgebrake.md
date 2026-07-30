# Day 041 — PurgeBrake

Date: 2026-07-30
Status: repo-created

## One-line pitch

A local-first dry-run packet generator that catches empty, broad, unsupported, or irreversible email remediation searches before admins quarantine or purge the wrong mailbox data.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vadrt1/knowbe4_phishrip_service_disruption_not_sure_what/ | Fresh admin report says a PhishRIP query intended for a specific phishing domain was processed without parameters and quarantined broad email results, creating urgent rollback risk. |
| KnowBe4 PhishRIP guide | https://support.knowbe4.com/hc/en-us/articles/360045742834-PhishRIP-Guide | PhishRIP searches for users' reported emails and removes similar emails across Microsoft 365 or Google Workspace inboxes; KnowBe4 says permanently deleted emails cannot be restored. |
| KnowBe4 Global PhishRIP guide | https://support.knowbe4.com/hc/en-us/articles/17305995205523-Global-PhishRIP-Guide | Global PhishRIP can automatically quarantine found messages using sender or URL criteria from recent global blocklist entries. |
| Microsoft Learn — eDiscovery delete | https://learn.microsoft.com/en-us/purview/edisc-search-mailbox-data | Microsoft warns to validate the search scope before purge, export report-only results first, and notes purge cannot be undone. |
| Practical 365 — compliance search purge | https://practical365.com/compliance-search-purge/ | Independent M365 guidance stresses precise criteria and explains Purview purge limits, estimate-search behavior, and the risk of mistaken search criteria. |

## Problem

Phishing and data-spillage response is time-sensitive, but mailbox remediation tools expose powerful search-and-action workflows. The risky moment is not writing one more detection rule. It is clicking quarantine, soft delete, or hard delete after a query that might be empty, under-constrained, unsupported by the provider, or broader than the incident responder intended.

The status quo is fragile under pressure:

- an admin builds a search from sender, URL, subject, body text, date range, or message attributes;
- the preview/export step may be skipped or captured informally;
- vendor tooling may hide provider-specific caveats until late in the flow;
- rollback ownership is often assumed rather than written down;
- a bad query creates user disruption, legal/compliance risk, and public embarrassment.

## Target user

- Microsoft 365 and Google Workspace admins who handle phishing or sensitive-email cleanup.
- Small security teams using KnowBe4 PhishER/PhishRIP, Defender, Purview, or vendor runbooks.
- MSP technicians who need a repeatable client-safe preflight packet before destructive email actions.

## MVP scope

- `purgebrake check --fixture examples/phish-domain-remediation.json` for synthetic public-safe scenarios.
- Fixture model for provider, action, query predicates, target locations, expected match count range, approvals, preview/export evidence, and rollback owner.
- Rule engine that emits blockers/warnings for empty predicates, wildcard subject/body matches, missing date bounds, unsupported identifier purge conditions, permanent delete without export, and missing rollback.
- Markdown packet export for change tickets and peer review.
- No live provider integrations, no mailbox access, and no real incident data in v0.

## Shortlist and wedge-first gate

| Candidate | Wedge-first gate | Result |
|---|---|---|
| PurgeBrake | M365/Google/KnowBe4 admins remediating phishing or data-spillage email → PhishRIP, Defender, Purview/eDiscovery, SOAR runbooks, peer review → existing tools can act broadly and the review packet is inconsistent under incident pressure → local-first preflight that rejects empty/broad/unsupported/irreversible searches and emits approval/rollback evidence → r/sysadmin, M365 admin search traffic, MSP/security-admin content around PhishRIP/Purview purge safety → fresh public incident plus current Microsoft purge guidance. | Winner; clears score and gates. |
| RedirectScope | Sysadmin inheriting DNS and registrar URL redirect records → redirectchecker.io, DNS checkers, browser devtools, curl → tools explain hops but not registrar/browser/HSTS/DNS ownership traps in one packet → targeted redirect failure packet for inherited domains → r/sysadmin and search replies around URL redirect troubleshooting → fresh r/sysadmin redirect failure. | Useful, but direct checkers already cover much of the job; held at 17/25. |
| MCP DriftMap | Enterprise ERP/PPM platform admin watching users create AI-assisted artifacts in silos → platform governance, Power Platform-style admin controls, spreadsheets of custom reports → admins lack a lightweight inventory/risk view for read-only MCP/self-serve artifacts → read-only artifact registry and duplicate/risk clustering → platform-admin communities and MCP governance posts → fresh r/sysadmin and r/webdev MCP fragmentation signals. | Timely but enterprise access/distribution is unclear; held at 18/25 with distribution 3/5. |
| LocalDeepBench | Local LLM users wanting fast private deep research → local-deep-research, open-deep-research, Perplexity/Claude/Grok modes → local tools are hard to compare on speed/privacy/source count → reproducible benchmark harness for local research agents → r/LocalLLaMA benchmark posts → fresh request. | Crowded AI research-agent category and weak buyer pain; rejected before final scoring. |
| TicketPlain | Sysadmins struggling to explain technical issues to end users → ChatGPT rewriting, ticket templates, internal KB style guides → generic rewriting loses technical nuance or professionalism → deterministic incident-response explanation templates by audience → helpdesk/sysadmin communities → fresh writing-pain post. | Generic AI writing wrapper risk; rejected before final scoring. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | KnowBe4 PhishRIP / Global PhishRIP | Strong remediation workflows for finding and removing similar messages. PurgeBrake does not replace PhishRIP; it creates a separate safety packet before an admin runs a risky query/action. |
| Direct competitor | Microsoft Defender for Office 365 / Explorer remediation | Native investigation and remediation path for delivered malicious email. PurgeBrake focuses on local linting, predicate sufficiency, preview/export evidence, and rollback ownership before using Defender. |
| Direct competitor | Microsoft Purview eDiscovery search and purge | Powerful search/delete workflow with role separation, PowerShell/Graph differences, preview/export requirements, and purge limits. The complexity creates room for a narrow preflight packet. |
| Direct competitor | Proofpoint, Mimecast, IR/SOAR email remediation | Enterprise suites can pull or quarantine messages. PurgeBrake is vendor-adjacent guardrail tooling, not a replacement gateway or SOAR. |
| Indirect substitute | Peer review, change ticket, PowerShell scripts, screenshots of search results | Common and cheap, but inconsistent under incident pressure and easy to skip when a phishing campaign is live. |
| Status quo | Admin writes a search, runs preview if time permits, clicks quarantine/purge, then discovers whether the scope was right | Wastes incident-response time and can create major rollback, legal, and user-trust fallout when scope is wrong. |

## Wedge-first gate

M365/Google/KnowBe4 admins remediating phishing or data-spillage email → PhishRIP, Defender, Purview/eDiscovery, SOAR runbooks, peer review, and change tickets → existing tools can act broadly while review evidence is inconsistent under incident pressure → local-first preflight that rejects empty/broad/unsupported/irreversible searches and emits approval/rollback evidence → r/sysadmin, M365 admin search traffic, MSP/security-admin content around PhishRIP/Purview purge safety → fresh public incident plus current Microsoft purge guidance.

## Wedge

PurgeBrake is not a mail security product, SIEM, SOAR, eDiscovery UI, or generic security scanner. It wins only if it stays narrower: the few minutes before a destructive email remediation action.

The MVP can get attention because it turns a scary, vendor-specific incident-response step into a deterministic packet:

- block empty predicate sets and dangerously broad all-mailbox searches;
- require date bounds, preview/export evidence, and sample review before destructive actions;
- encode provider caveats such as unsupported conditions, purge limits, and irreversible deletion warnings;
- produce a markdown artifact that can be pasted into a change ticket without exposing real mailbox data;
- keep v0 local and synthetic, avoiding paid APIs and tenant credentials.

## Kill condition

Reject or narrow if early validation shows M365/KnowBe4 admins already have mandatory built-in guardrails that prevent empty or over-broad remediation searches, or if responders will not add a separate preflight step during live phishing incidents. Also reject any v0 scope that requires storing real mailbox exports, tenant identifiers, or credentials.

## Non-goals

- Not connecting to real Microsoft 365, Google Workspace, KnowBe4, Proofpoint, Mimecast, SIEM, SOAR, or ticketing APIs in v0.
- Not storing real domains, users, mailbox names, message IDs, tenants, incident IDs, or credentials.
- Not replacing mail security gateways, eDiscovery, Defender, or PhishRIP.
- Not giving legal advice about retention, litigation hold, or compliance deletion.

## Source access caveats

Reddit public JSON was blocked by `HTTP 403 theme-beta`; the Reddit evidence came through the skill's public RSS fallback. Fetching Reddit comment threads returned 403, so only the RSS-visible post title/body snippet was used. Some subreddit RSS calls returned `HTTP 429`; I stopped retrying and used web search and original vendor/Microsoft docs for validation. X `whoami` worked, but X search returned `401 Unauthorized`; no X search evidence was used.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 5/5 | A mistaken email purge/quarantine can create user disruption, compliance risk, rollback work, and public embarrassment. The status quo easily exceeds the pain threshold. |
| Feasibility | 4/5 | v0 is a deterministic fixture parser, safety-rule engine, and markdown packet generator. Live provider integrations are intentionally out of scope. |
| Demo potential | 4/5 | A synthetic bad PhishRIP/Purview fixture can clearly show blockers, warnings, and an approval packet in a terminal/GIF. |
| Distribution | 4/5 | Specific channels exist: r/sysadmin, M365/Purview/KnowBe4 troubleshooting searches, MSP/security-admin content, and reply-style incident-response checklists. |
| Competitive wedge / timing | 4/5 | Incumbents own remediation, but the wedge is preflight safety after a fresh public PhishRIP incident and current Microsoft purge warnings. |
| Total | 21/25 | Clears repo/snapshot threshold; weakest dimensions are feasibility, demo, distribution, and wedge tied at 4/5. |

## Decision

Create the canonical project snapshot in the master repo: [projects/purgebrake](../projects/purgebrake).

No dedicated GitHub remote was configured locally, so there is no separate GitHub repository to report for PurgeBrake.

## Next build step

Implement the first deterministic CLI slice: parse `examples/phish-domain-remediation.json`, run rules for empty predicates, missing date bounds, permanent delete without export, and missing rollback owner, then snapshot-test the markdown packet.
