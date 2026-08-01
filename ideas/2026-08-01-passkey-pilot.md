# Day 043 — PasskeyPilot

Date: 2026-08-01
Status: repo-created
Repo: [`projects/passkey-pilot`](../projects/passkey-pilot)

## One-line pitch

A Microsoft Entra passkey rollout packet generator that helps admins decide synced vs device-bound passkey profiles before a tenant-wide authentication change.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vcbc0x/entra_synced_passkeys_security_vs_password_otp/ | Fresh admin question weighing synced passkeys for standard users against device-bound passkeys for privileged admins because Android/device constraints make a blanket policy hard. |
| Microsoft Learn | https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-synced-passkeys | Synced passkeys reduce recovery and issuance cost, but Microsoft recommends device-bound passkeys for admins and highly privileged users. |
| Microsoft Learn | https://learn.microsoft.com/en-us/entra/identity/authentication/how-to-authentication-passkeys-fido2 | Entra passkey profiles now encode passkey type, attestation, AAGUID restrictions, and targeted groups. |
| Microsoft Learn FAQ | https://learn.microsoft.com/en-us/entra/identity/authentication/passkey-faq | Microsoft states admins cannot see or control exactly which devices hold a synced passkey copy, so policy choice and lifecycle monitoring matter. |
| LazyAdmin | https://lazyadmin.nl/office-365/synced-passkeys-microsoft-entra-id/ | Practitioner guide says synced passkeys improve adoption but require device compliance and Conditional Access discipline. |

## Source access caveats

- Reddit public JSON was blocked with `HTTP 403 theme-beta`; the r/sysadmin post list came from the bundled Reddit RSS fallback.
- Fetching individual Reddit comment threads returned `HTTP 403`, so the brief uses the public post title/snippet plus external documentation.
- Other subreddit RSS/JSON attempts hit `HTTP 429`; I stopped instead of looping.
- X `whoami` worked, but X search returned `401 Unauthorized`; X was not used as evidence.
- Web search/extraction was used for Microsoft documentation and competitor/substitute validation.

## Shortlist wedge gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| PasskeyPilot | Microsoft Entra admins planning passkey profiles → Microsoft Learn, Entra admin center, PowerShell/Graph scripts, spreadsheets → sources explain pieces but not a change-review packet for synced vs device-bound cohorts → fixture-driven rollout packet for standard-user synced passkeys while privileged users stay device-bound → r/sysadmin, M365 admin blogs, MSP runbooks, targeted replies to passkey rollout questions → synced passkeys and passkey profiles are current Entra changes with visible admin confusion. | Winner; score 20/25 and gates pass. |
| SecretLink Swap | Sysadmins replacing an EOL one-time password sharing app → Password Pusher, One-Time Secret, Bitwarden Send-style tools, PrivateBin → many replacements already provide public expiring links → migration checklist and drop-in comparison for no-auth recipients → r/sysadmin threads asking for replacements → pain is real but direct competitors are too strong. | Rejected before scoring as a standalone app; better as content/template. |
| IT Spend Stitch | IT directors tracking hardware/license spend outside accounting → Excel, ITAM/CMDB suites, SaaS spend tools → spreadsheets drift and suites are heavy → lightweight import that links purchase rows to inventory IDs → r/sysadmin finance/spend threads → recurring budget pain, but this is a crowded analytics/ITAM category. | Rejected/narrowed; distribution and wedge too weak. |
| AI Ready Packet | Internal AI rollout owners in locked-down Windows environments → endpoint analytics, Intune reports, surveys, consultant assessments → tools report device state but not automation hostility and workflow blockers → local questionnaire/report for AI pilot blockers → sysadmin/enterprise AI rollout communities → AI deployment pressure is timely. | Held as idea-only; crowded AI-readiness category and source evidence too thin today. |

## Problem

Entra admins are being asked to move users toward passkeys, but the rollout decision is now segmented: synced passkeys are easier for standard users and reduce recovery cost, while privileged users and regulated cohorts may need device-bound passkeys, attestation, FIDO2 security keys, or Microsoft Authenticator. The admin still has to reconcile user groups, device platforms, provider support, Conditional Access, recovery, and helpdesk impact manually.

The status quo wastes planning time and can create security risk: a too-broad synced-passkey rollout may put privileged accounts on a credential model where admins cannot see or control every synced device, while a too-strict device-bound rollout can generate avoidable support tickets and failed adoption.

## Target user

- Microsoft 365 / Entra admins planning passkey profiles for SMB and mid-market tenants.
- MSP identity engineers who need repeatable client-facing rollout notes.
- Security leads reviewing whether standard users can use synced passkeys while admins remain device-bound.

## MVP scope

- CLI command: `passkey-pilot plan --answers examples/smb-standard-users.yaml`.
- YAML/CSV fixture schema for cohorts, role sensitivity, device platform mix, allowed passkey providers, and policy constraints.
- Deterministic rules for privileged-user blockers, synced-passkey caveats, provider/platform minimums, attestation constraints, and Conditional Access reminders.
- Markdown output packet with recommendation, rollout phases, helpdesk script, rollback notes, and open questions.
- No Microsoft Graph connection or tenant credentials in v0.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Microsoft Entra admin center and Microsoft Learn | Authoritative for configuration, but they do not turn a mixed cohort/security tradeoff into a short decision packet for CAB/security review. |
| Direct competitor | ManageEngine ADSelfService Plus FIDO2 Passkeys Report | Strong for reporting registered passkeys and last use; not focused on pre-rollout synced-vs-device-bound segmentation. |
| Direct competitor | Maester / Entra ID Security Config Analyzer tests | Useful for config security checks such as FIDO2 attestation; not a rollout planner with device/provider assumptions and helpdesk runbook output. |
| Indirect substitute | PowerShell/Graph scripts, spreadsheets, admin checklists, consultant-written rollout docs | Flexible but fragmented; admins still reconcile groups, mobile platforms, privileged users, recovery, and Conditional Access manually. |
| Status quo | Admin reads docs/blog posts, debates risk in a meeting, toggles a pilot group, then reacts to support tickets and exception requests | Can waste days in planning/rework and creates security risk if privileged users accidentally receive synced passkeys. |

## Wedge

Specific user → existing substitute → why substitute fails → narrow wedge → distribution path → reason now

Microsoft Entra admins planning passkey profiles → Microsoft Learn, Entra admin center, PowerShell/Graph scripts, spreadsheets → sources explain configuration and reporting but not a concise change-review packet for synced vs device-bound cohorts → fixture-driven rollout packet that separates standard users, privileged admins, mobile platform constraints, attestation, Conditional Access, and support notes → r/sysadmin, M365 admin blogs, MSP runbooks, and targeted replies to passkey rollout questions → Microsoft's 2026 passkey profile/synced-passkey docs are fresh and admins are actively asking how to balance usability against risk.

PasskeyPilot can win as a small app because it is not trying to be identity governance. It is a deterministic pre-rollout packet generator: useful before an admin has tenant API exports, safe enough to run in public examples, and narrow enough to demo with a single YAML fixture.

## Kill condition

Reject or narrow if one of these is proven:

- Microsoft or a major Entra admin suite ships a native synced-vs-device-bound rollout planner with cohort recommendations and CAB-ready export.
- Admins say a checklist/blog post is enough and they would not run a local packet generator before a passkey rollout.
- Graph-export reporting becomes required for usefulness before a fixture-driven v0 can prove value.
- The rules cannot be kept deterministic without pretending to provide tenant-specific security advice.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Authentication rollout mistakes create security/support risk, and the Reddit signal shows real admin uncertainty. |
| Feasibility | 5/5 | A fixture-driven CLI/report generator is a 1–3 day MVP with no paid/private API dependency. |
| Demo potential | 4/5 | One YAML fixture can produce a clear before/after markdown packet, cohort table, and blocker list. |
| Distribution | 4/5 | Specific communities exist: r/sysadmin, M365/Entra admin blogs, MSP runbooks, and search traffic around synced passkeys. |
| Competitive wedge / timing | 3/5 | Timely Entra passkey changes create urgency, but Microsoft docs and reporting tools are strong substitutes; wedge must stay narrow. |
| Total | 20/25 | Clears repo-creation threshold and gates. |

## Decision

Create the repo scaffold as `repo-created` because the total is 20/25, Distribution is 4/5, and Competitive wedge / timing is 3/5. Scaffold/spec snapshot is consolidated into the master repo at `projects/passkey-pilot`; the local project repo has no dedicated GitHub remote.

Weakest dimension: Competitive wedge / timing at 3/5, because Microsoft docs, Maester-style config checks, and ManageEngine reporting are meaningful substitutes.

## Next build step

Implement `passkey-pilot plan --answers examples/smb-standard-users.yaml` so the sample fixture emits a deterministic markdown rollout packet with cohort recommendations, blockers, guardrails, and open questions.
