# PurgeBrake

A local-first dry-run packet generator for dangerous email remediation searches before an admin quarantines or purges the wrong messages.

## Problem

Security and Microsoft 365 admins need to remove phishing or sensitive emails quickly, but remediation tools sit on top of broad mailbox search primitives. A missing sender, empty parameter set, over-broad subject query, or unsupported purge condition can turn a targeted cleanup into a company-wide incident.

Existing products can search, quarantine, and purge messages. PurgeBrake does not replace them. It sits one step earlier: validate the intended search, require enough predicates, generate a preview/export checklist, and produce a human-reviewable approval packet before any destructive action happens.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vadrt1/knowbe4_phishrip_service_disruption_not_sure_what/ | Fresh admin report says a PhishRIP query for a specific phishing domain was processed without parameters and quarantined broad email results, creating urgent rollback risk. |
| KnowBe4 PhishRIP guide | https://support.knowbe4.com/hc/en-us/articles/360045742834-PhishRIP-Guide | PhishRIP searches for reported emails and removes similar emails across Microsoft 365 or Google Workspace inboxes; permanent deletion cannot be restored by KnowBe4. |
| KnowBe4 Global PhishRIP guide | https://support.knowbe4.com/hc/en-us/articles/17305995205523-Global-PhishRIP-Guide | Global PhishRIP can automatically quarantine found messages using sender or URL criteria from recent global blocklist entries. |
| Microsoft Learn — eDiscovery delete | https://learn.microsoft.com/en-us/purview/edisc-search-mailbox-data | Microsoft warns to validate search scope before purge, export report-only results first, and notes purge cannot be undone. |
| Practical 365 — compliance search purge | https://practical365.com/compliance-search-purge/ | Independent M365 guidance stresses precise criteria and calls out Purview purge limits and estimate-search behavior. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | KnowBe4 PhishRIP / Global PhishRIP | Strong remediation workflows, but the public pain point is preflight safety when a query/action becomes over-broad. PurgeBrake produces a separate approval packet before action. |
| Direct competitor | Microsoft Defender for Office 365 / Explorer remediation | Native investigation and remediation path for delivered malicious email. PurgeBrake focuses on local linting, predicate sufficiency, and rollback evidence before using the native tool. |
| Direct competitor | Microsoft Purview eDiscovery search and purge | Powerful search/delete workflow with role separation and preview/export paths. It is still complex enough that admins rely on PowerShell snippets and manual query review. |
| Direct competitor | Proofpoint, Mimecast, IR/SOAR email remediation | Enterprise suites can pull or quarantine messages. PurgeBrake is not a SOAR; it is a vendor-adjacent guardrail packet for risky one-off searches. |
| Indirect substitute | Peer review, change ticket, PowerShell scripts, screenshots of search results | Common, but inconsistent under incident pressure and easy to skip when a phishing campaign is live. |
| Status quo | Admin writes a search, runs preview if time permits, clicks quarantine/purge, then discovers whether the scope was right | Wastes incident-response time and can create major rollback, legal, and user-trust fallout when scope is wrong. |

## Wedge

PurgeBrake wins only by staying narrow: email-remediation preflight, not another security scanner or mail gateway.

The v0 wedge is a deterministic, local-first packet:

- reject empty or missing critical predicates before a query reaches a remediation tool;
- flag broad sender/domain/date patterns, unsupported purge conditions, cross-provider mismatch, and no rollback owner;
- require preview/export evidence and two-person approval for high-impact scopes;
- emit a public-safe markdown packet with query summary, risk level, expected match bounds, required screenshots/exports, rollback steps, and approval checklist.

## Target user

- Microsoft 365 and Google Workspace admins who handle phishing or sensitive-email cleanup.
- Small security teams using KnowBe4 PhishER/PhishRIP, Defender, Purview, or vendor runbooks.
- MSP technicians who need a repeatable client-safe preflight packet before destructive email actions.

## MVP

- `purgebrake check --fixture examples/phish-domain-remediation.json` for synthetic public-safe scenarios.
- Fixture model for provider, action, query predicates, target locations, expected match count range, approvals, preview/export evidence, and rollback owner.
- Rule engine that emits blockers/warnings for empty predicates, wildcard subject/body matches, missing date bounds, unsupported identifier purge conditions, permanent delete without export, and missing rollback.
- Markdown packet export for change tickets and peer review.

## Non-goals

- Not connecting to real Microsoft 365, Google Workspace, KnowBe4, Proofpoint, Mimecast, or mailbox APIs in v0.
- Not storing real domains, users, mailbox names, message IDs, tenants, incident IDs, or credentials.
- Not replacing mail security gateways, SIEM, SOAR, eDiscovery, or Defender.
- Not giving legal advice about retention, litigation hold, or compliance deletion.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
