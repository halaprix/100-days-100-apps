# SPEC — SyncBrake

## User story

As a hybrid identity admin, I want to turn Entra Connect pending-export changes and break-glass readiness facts into a redacted go/no-go packet, so that I can catch mass-delete and admin-lockout risks before a sync change reaches Microsoft Entra ID.

## Core flow

1. User exports pending changes from a staging server or Synchronization Service workflow.
2. User runs `syncbrake packet --export pending-export.csv --readiness readiness.yml --out packet.md`.
3. SyncBrake parses the export and readiness checklist locally.
4. It classifies object-level delete/disable risk, privileged/admin-looking accounts, emergency-access gaps, and threshold state.
5. It renders a deterministic markdown packet with a stop/go banner, blast-radius summary, review table, break-glass checklist, rollback prompts, and next actions.

## Inputs

- `pending-export.csv`: sanitized `CSExportAnalyzer`-style CSV or fixture-format export rows.
- `readiness.yml`: safe manual facts:
  - change window label
  - delete threshold state
  - staging mode used: yes/no
  - cloud-only emergency access accounts verified: count/date
  - support path verified: yes/no
  - rollback owner
  - notes

## Data model

```text
ExportChange
  object_id: string
  display_name: string | null
  user_principal_name: string | null
  object_type: user | group | device | contact | other
  object_modification_type: add | update | delete | disable | unknown
  attributes_changed: list[string]
  risk_flags: list[string]

ReadinessFacts
  change_label: string
  threshold_enabled: bool
  threshold_value: int | null
  staging_mode_used: bool
  emergency_accounts_verified_count: int
  emergency_accounts_last_tested: string | null
  support_path_verified: bool
  rollback_owner: string | null

Packet
  generated_at: ISO-8601 date
  decision: stop | review | proceed
  blast_radius: list[SummaryItem]
  high_risk_changes: list[ExportChange]
  readiness_gaps: list[string]
  next_actions: list[string]
```

## Technical approach

- Build a small Python CLI first; keep dependencies minimal.
- Parse CSV with the standard library and support a fixture format before exact `CSExportAnalyzer` parity.
- Render deterministic markdown so output is diffable in CI.
- Redact UPN domains, tenant-looking names, hostnames, private paths, and support-case details.
- Keep all examples synthetic and public-safe.

## Validation plan

- Golden-file test for `fixtures/pending-export.csv` + `fixtures/readiness.yml` to `tests/golden/sample-packet.md`.
- Public-safety test for UPN/domain/hostname/support-case redaction.
- Risk-classification test for privileged account deletes and missing emergency-access verification.
- Demo check that generated packet includes decision banner, blast radius, readiness gaps, and next actions.

## Milestones

- v0.1.0-alpha.0 — repo scaffold/spec snapshot.
- v0.1.0-alpha.1 — CLI parses fixtures and renders deterministic markdown packet.
- v0.2.0-alpha.1 — closer `CSExportAnalyzer` compatibility, HTML export, richer redaction tests.
