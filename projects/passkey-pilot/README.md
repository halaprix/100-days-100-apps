# PasskeyPilot

A Microsoft Entra passkey rollout packet generator for choosing synced vs device-bound passkeys before a tenant-wide MFA change.

## Problem

Microsoft Entra admins now have granular passkey profiles, synced passkeys, device-bound passkeys, attestation settings, Conditional Access authentication strengths, and mixed mobile-device constraints to reconcile. The risky part is not clicking the toggle; it is deciding which groups should get synced passkeys, which groups must stay device-bound, and what helpdesk/security exceptions will appear after rollout.

PasskeyPilot turns a public-safe questionnaire and optional CSV fixtures into a review packet: group recommendations, platform/provider compatibility notes, privileged-user blockers, Conditional Access reminders, and a pilot rollout checklist.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vcbc0x/entra_synced_passkeys_security_vs_password_otp/ | Fresh admin question weighing synced passkeys for standard users against device-bound passkeys for privileged admins because Android/device constraints make a blanket policy hard. |
| Microsoft Learn | https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-synced-passkeys | Synced passkeys reduce recovery/issuance cost but Microsoft recommends device-bound passkeys for admins and highly privileged users. |
| Microsoft Learn | https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2 | Entra passkey profiles now encode passkey type, attestation, AAGUID restrictions, and targeted groups. |
| Microsoft Learn FAQ | https://learn.microsoft.com/en-us/entra/identity/authentication/passkey-faq | Microsoft states admins cannot see or control exactly which devices hold a synced passkey copy, making policy choice and lifecycle monitoring important. |
| LazyAdmin | https://lazyadmin.nl/office-365/synced-passkeys-microsoft-entra-id/ | Practitioner guide says synced passkeys improve adoption but require device compliance and Conditional Access discipline. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Microsoft Entra admin center and Microsoft Learn | Authoritative for configuration, but it does not turn a messy device/group/security tradeoff into a short decision packet for change review. |
| Direct competitor | ManageEngine ADSelfService Plus FIDO2 Passkeys Report | Strong for reporting registered passkeys and last use; not focused on pre-rollout synced-vs-device-bound segmentation. |
| Direct competitor | Maester / Entra ID Security Config Analyzer tests | Useful for config security checks such as FIDO2 attestation, but not a rollout planner with device/provider assumptions and helpdesk runbook output. |
| Indirect substitute | PowerShell/Graph scripts, spreadsheets, admin checklists, consultant-written rollout docs | Flexible but fragmented; admins still reconcile groups, mobile platforms, privileged users, recovery, and Conditional Access manually. |
| Status quo | Admin reads docs/blog posts, debates risk in a meeting, toggles a pilot group, then reacts to support tickets and exception requests | Can waste days in planning/rework and creates security risk if privileged users accidentally receive synced passkeys. |

## Wedge

PasskeyPilot is narrower than identity governance suites and safer than ad-hoc scripts:

- v0 is fixture-driven, read-only, and can run without tenant credentials;
- it focuses on the new synced-vs-device-bound Entra passkey decision, not generic MFA reporting;
- it emits a markdown packet suitable for a change advisory, security review, or pilot announcement;
- it encodes public Microsoft guidance and practitioner pitfalls as deterministic checks;
- later Graph integration can be added only after the packet format proves useful.

## Target user

- Microsoft 365 / Entra admins planning passkey profiles for SMB and mid-market tenants.
- MSP identity engineers who need repeatable client-facing rollout notes.
- Security leads reviewing whether standard users can use synced passkeys while admins remain device-bound.

## MVP

- `passkey-pilot plan --answers examples/smb-standard-users.yaml`.
- YAML/CSV fixture schema for user cohorts, role sensitivity, device platforms, passkey providers, and policy constraints.
- Rule engine for privileged-user blockers, synced-passkey caveats, Android/iOS/provider minimums, attestation constraints, and Conditional Access reminders.
- Markdown packet export with recommendation, rollout phases, helpdesk script, rollback notes, and open questions.

## Non-goals

- Not connecting to Microsoft Graph in v0.
- Not changing Entra policies automatically.
- Not making a compliance certification claim.
- Not replacing tenant security review or Microsoft documentation.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
