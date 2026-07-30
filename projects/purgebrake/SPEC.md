# SPEC — PurgeBrake

## User story

As a Microsoft 365 or Google Workspace admin responding to a phishing incident, I want to dry-run and package a risky email remediation search before quarantine or purge, so that I can catch empty, broad, unsupported, or irreversible actions before they hit user mailboxes.

## Core flow

1. User chooses a remediation provider profile: `m365-purview`, `m365-defender`, `knowbe4-phishrip`, `google-workspace`, or `generic`.
2. User fills a public-safe fixture with intended action, predicates, target locations, expected match range, deletion mode, preview/export evidence, approvers, and rollback owner.
3. PurgeBrake evaluates deterministic safety rules.
4. PurgeBrake emits blockers, warnings, summary risk, required evidence, approval checklist, and rollback packet.
5. User manually applies the real remediation in their vendor tool only after the packet clears review.

## Data model

```json
{
  "scenario": "phish-domain-remediation",
  "provider": "knowbe4-phishrip",
  "action": "quarantine",
  "predicates": {
    "sender_domain": "example.test",
    "subject_contains": "synthetic invoice lure",
    "received_after": "2026-07-30T00:00:00Z",
    "received_before": "2026-07-30T06:00:00Z"
  },
  "scope": {
    "locations": "all-mailboxes",
    "expected_min_matches": 1,
    "expected_max_matches": 80
  },
  "evidence": {
    "preview_export_attached": true,
    "sample_messages_reviewed": 10
  },
  "approval": {
    "requires_two_person_review": true,
    "rollback_owner": "incident-admin"
  }
}
```

All examples use reserved synthetic domains such as `example.test`. v0 fixtures must not include real email addresses, domains, tenant names, message IDs, or customer identifiers.

## Technical approach

- Language: Python CLI for alpha.1 unless implementation constraints change.
- Deterministic fixture parser and rules first; no live API calls.
- Rule severities: `blocker`, `warning`, `info`, and `evidence_required`.
- Output: JSON findings and Markdown remediation packet.
- Provider profiles encode known safety constraints, not credentials or API calls.

## Initial rule set

- Block if all predicates are empty or only a generic body/subject wildcard exists.
- Block quarantine/purge when no received date bound is present for all-mailbox scope.
- Warn on all-mailbox scope with expected match maximum above a configurable threshold.
- Block permanent delete when preview/export evidence is missing.
- Warn when provider/action combines unsupported identifiers or search conditions.
- Block if rollback owner or approval path is missing for broad scope.
- Warn when sample review count is lower than the configured threshold.

## Validation plan

- Unit tests for fixture parsing and safety rule severity.
- Snapshot tests for Markdown packet output.
- Negative fixtures for common unsafe requests:
  - no predicates;
  - sender-only broad domain;
  - no date bound;
  - permanent delete without export;
  - missing approver or rollback owner;
  - unsupported provider/action condition.
- Public-safety verifier that rejects real-looking emails, non-example domains, secret-like tokens, tenant IDs, and private mailbox identifiers in examples/docs.

## Milestones

- v0.1.0-alpha.0 — scaffold/spec snapshot.
- v0.1.0-alpha.1 — fixture parser, safety rules, sample packet, tests.
- v0.2.0-alpha.1 — provider profiles for KnowBe4 PhishRIP, Purview purge, and Defender remediation.
