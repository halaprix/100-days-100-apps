# SPEC — PasskeyPilot

## User story

As a Microsoft Entra admin, I want a repeatable passkey rollout packet before enabling synced passkeys, so that I can separate standard-user convenience from privileged-user security requirements and avoid blind tenant-wide changes.

## Core flow

1. User copies `examples/smb-standard-users.yaml` and fills public-safe cohort facts: user group, role sensitivity, device platform mix, passkey providers, recovery constraints, and Conditional Access notes.
2. User runs `passkey-pilot plan --answers <file>`.
3. The rule engine classifies cohorts as `device-bound required`, `synced acceptable with guardrails`, `pilot first`, or `blocked pending more data`.
4. The app writes `passkey-rollout-packet.md` with rationale, rollout phases, helpdesk notes, rollback questions, and references.
5. Optional later mode ingests sanitized Graph exports for already-registered FIDO2/passkey methods.

## Data model

```yaml
tenant_context:
  tenant_size: smb | mid_market | enterprise
  regulated_environment: false
  current_mfa_methods: [sms, otp_app, authenticator]
  conditional_access_strength_required: false
cohorts:
  - name: standard-users
    privileged: false
    handles_sensitive_systems: false
    device_platforms:
      windows: 80
      macos: 10
      ios: 60
      android: 40
    allowed_passkey_providers: [icloud_keychain, google_password_manager, microsoft_password_manager]
    unmanaged_personal_devices_allowed: true
    support_risk_notes: "Some users resist dedicated work apps on personal phones."
  - name: privileged-admins
    privileged: true
    handles_sensitive_systems: true
    device_platforms:
      windows: 100
      ios: 30
      android: 20
    allowed_passkey_providers: [microsoft_authenticator, fido2_security_key]
    unmanaged_personal_devices_allowed: false
```

## Rule categories

- Privileged users: recommend device-bound passkeys and flag synced passkeys as a blocker unless explicitly waived.
- Synced passkeys: warn that admins cannot see or control every device holding a synced passkey copy.
- Attestation: explain that synced passkeys do not support attestation and that device-bound profiles can use attestation/AAGUID restrictions.
- Platform/provider fit: compare cohort platforms against provider minimums from public Microsoft documentation.
- Conditional Access: remind users to align authentication strengths, registration campaigns, and recovery paths.
- Rollout hygiene: recommend pilot groups, helpdesk language, success metrics, rollback criteria, and exception tracking.

## Technical approach

- Language: Python 3.12.
- CLI: `argparse` initially; no dependency lock until implementation begins.
- Inputs: YAML fixtures and optional CSV imports.
- Output: deterministic markdown report plus JSON summary for tests.
- Public-safety: examples use synthetic group names, reserved domains such as `example.test`, and no tenant IDs, real domains, UPNs, hostnames, or private ticket data.

## Validation plan

- Unit tests for each rule category using synthetic fixtures.
- Snapshot tests for markdown packet output.
- Golden examples for standard users, privileged admins, mixed Android/iOS fleets, and regulated environments.
- Wedge validation: share a packet template in r/sysadmin / M365 admin communities and see whether admins correct the assumptions or ask for Graph import.

## Milestones

- v0.1.0-alpha.0 — scaffold and spec.
- v0.1.0-alpha.1 — fixture schema, CLI skeleton, and deterministic packet for one sample tenant.
- v0.2.0-alpha.1 — rule coverage for synced/device-bound/attestation/provider constraints and markdown snapshots.
- v0.3.0-alpha.1 — optional sanitized Graph export import, still read-only.
