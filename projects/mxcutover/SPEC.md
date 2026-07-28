# MxCutover Specification

## User story

As a Microsoft 365 admin switching secure email gateways, I want a local readiness packet before the cutover window, so I can verify mail-flow, DNS, SSO, permissions, and rollback assumptions before the vendor onboarding call turns into production risk.

## Feature list

### v0 prototype

1. Local CLI command: `mxcutover packet profile.yaml`.
2. Synthetic sample profiles for:
   - Mimecast to Proofpoint Essentials,
   - Proofpoint to Microsoft Defender / Exchange Online Protection,
   - generic secure email gateway to secure email gateway.
3. Read-only rule engine that validates required fields:
   - domains and current MX targets,
   - desired mail-flow mode,
   - SPF/DKIM/DMARC checklist state,
   - inbound/outbound connector assumptions,
   - SSO/app-registration prerequisites,
   - change window and rollback owner.
4. Markdown report with:
   - readiness score,
   - missing prerequisites,
   - cutover sequence,
   - rollback plan,
   - vendor/MSP question list,
   - public-safe evidence appendix.
5. JSON schema for profile validation.
6. Tests for profile parsing and packet generation.

### Later

- Optional DNS lookup mode for public MX/SPF/DMARC inspection.
- Optional Microsoft Graph read-only export after explicit local auth.
- Provider-specific checklist packs for Proofpoint, Mimecast, Defender/EOP, and Google Workspace.
- HTML packet export.
- MSP multi-customer report mode with strict no-secrets checks.

## Data model

```text
CutoverProfile
- organization_alias
- current_provider
- target_provider
- domains[]
- mail_flow_mode
- identity_setup
- dns_state
- connector_state
- risk_notes[]
- rollback_plan
- change_window
- approvers[]

DomainState
- domain
- current_mx[]
- planned_mx[]
- spf_status
- dkim_status
- dmarc_status
- ttl_plan

Finding
- id
- severity: blocker | warning | info
- area: dns | mail-flow | identity | permissions | rollback | vendor
- message
- recommended_action
- evidence_links[]
```

## Technical approach

- TypeScript or Python CLI; start with Python for fast YAML/schema/report generation.
- JSON Schema or Pydantic model for deterministic validation.
- Markdown templates kept in repo.
- No network calls in v0 unless a user explicitly enables DNS lookup mode later.
- Synthetic fixtures only; never commit tenant exports, real domains, or vendor secrets.

## Validation plan

- Unit tests for required-field validation and finding severity.
- Golden-file tests for Markdown packet output.
- Fixture profile that intentionally misses SPF/rollback/SSO prerequisites and must produce blockers.
- Public-safety scan that fails on obvious token/private-key/private-path patterns.
- Manual demo: generate a packet from the synthetic Mimecast-to-Proofpoint profile.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and product specification.
- v0.1.0-alpha.1 — CLI skeleton, schema, sample profile, and Markdown packet.
- v0.2.0-alpha.1 — provider checklist packs and public demo packet.
