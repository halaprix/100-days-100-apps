# SPEC — ForestDrill

## User story

As a small-team Windows sysadmin, I want a repeatable AD backup recovery-drill packet before I touch production, so that I can catch missing system-state coverage, backup-plane trust risks, cold-tier restore delays, and untested account/runbook gaps before an outage or ransomware event.

## Core flow

1. User copies `examples/small-org-ad-backup.yaml` and fills only public-safe facts: approximate DC count, backup products, backup management trust boundary, storage tiers, restore-account categories, and scenarios they intend to test.
2. User runs `forestdrill plan --answers <file>`.
3. The rule engine classifies each area as `ready`, `needs evidence`, `risky`, or `blocked`.
4. The app writes `forestdrill-packet.md` with a summary, gaps, drill agenda, account-verification checklist, storage-tier caveats, and questions for vendors or leadership.
5. Optional later mode ingests sanitized CSV exports from backup inventory reports, still read-only.

## Data model

```yaml
environment:
  org_size: small_team
  domain_controller_count: 20
  hypervisors: [hyper_v, vmware]
  ad_recycle_bin_enabled: true
backup_plan:
  primary:
    product: dell-avamar
    covers_system_state: true
    covers_bare_metal: true
    backup_manager_joined_to_ad: true
  secondary:
    target: azure-blob
    tier: cold
    method: mars-or-azure-cli
recovery_accounts:
  built_in_administrator_verified: true
  dsrm_password_verified: false
  break_glass_account_verified: false
drill_scenarios:
  - isolated-network-forest-restore
  - single-domain-restore
  - gpo-and-sysvol-restore
  - backup-manager-unavailable
```

## Rule categories

- System-state coverage: flag DCs/scenarios without explicit system-state evidence.
- Backup-plane trust: flag backup managers, credentials, or storage paths that depend on the compromised forest.
- Storage-tier risk: warn when cold/archive tiers may break recovery-time expectations.
- Isolated-network drill: require scenario, identity, DNS, time sync, and reconnection boundaries to be documented.
- Recovery accounts: require DSRM, built-in administrator, break-glass, backup-console, and storage-access validation categories.
- Evidence packet hygiene: require public-safe placeholders and block real domains, hostnames, IPs, tenant IDs, or screenshots.

## Technical approach

- Language: Python 3.12.
- CLI: `argparse` initially; no network calls in v0.
- Inputs: YAML fixtures and optional sanitized CSV inventory.
- Outputs: deterministic markdown report plus JSON summary for tests.
- Safety: examples use `example.test`, generic product labels, and no real hostnames, IPs, usernames, backup IDs, tenant IDs, or credentials.

## Validation plan

- Unit tests for every rule category using synthetic fixtures.
- Snapshot tests for the markdown packet.
- Golden examples for small org, MSP client review, cold-tier storage, and backup-manager-is-AD-joined scenarios.
- Public-safety test that rejects private infrastructure markers and credential-shaped strings in fixtures.
- Wedge validation: publish a sample packet to sysadmin/MSP communities and measure whether admins correct assumptions, ask for vendor-specific import, or say existing tools already cover it.

## Milestones

- v0.1.0-alpha.0 — scaffold and spec.
- v0.1.0-alpha.1 — fixture schema, CLI skeleton, and one deterministic packet.
- v0.2.0-alpha.1 — rule coverage for system-state, trust boundary, storage tier, and recovery-account checks.
- v0.3.0-alpha.1 — optional sanitized CSV import and markdown snapshot tests.
