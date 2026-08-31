# Day 067 — EnrollFence

Date: 2026-08-31
Status: repo-created

## One-line pitch

A local, read-only CLI that turns a sanitized Intune Windows-enrollment policy
export into a path-by-path review packet before an administrator assumes
"corporate devices only" is actually enforced.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit community report (RSS fallback) | https://www.reddit.com/r/sysadmin/comments/1w33qcy/entrajoin_and_intuneenroll_restrictions/ | A fresh administrator asks whether corporate PCs can be limited to Entra Join and OOBE Autopilot, and specifically worries that a restored corporate device could still enroll through Company Portal. This is one report, not consensus. |
| Microsoft Learn | https://learn.microsoft.com/en-us/intune/device-enrollment/windows/guide | Microsoft's current Windows enrollment guide documents multiple routes, including automatic enrollment through Settings and organization-owned and personal-device scenarios. |
| Microsoft Learn | https://learn.microsoft.com/en-us/intune/device-enrollment/monitor-reports | Intune's enrollment reports show failures and policies applied to a device after enrollment, establishing the native reporting substitute and its after-the-fact focus. |
| Public Intune specialist analysis | https://petervanderwoude.nl/post/understanding-enrollment-restrictions-for-windows-devices/ | Enrollment-restriction filters have a limited set of usable properties and must be combined with restrictions, which makes policy reasoning across configuration surfaces non-trivial. |

## Problem

A small Intune team may intend to admit only approved corporate Windows devices,
but the enforcement model spans enrollment restrictions, filter support,
assignment priority, Autopilot registration, user scope, and several Windows
enrollment routes. Administrators usually reconcile portal blades, Microsoft
documentation, screenshots, and a few test machines by hand. That can take
hours on a change window and can leave an allowed path undiscovered until a
restored or user-driven device appears in the tenant.

This clears the status-quo pain test: an unintentionally enrolled endpoint is a
security and compliance boundary failure, not a cosmetic configuration issue.

## Target user

A Microsoft Intune administrator at a small IT team or MSP who owns Windows
Autopilot and enrollment restrictions and must demonstrate that only approved
corporate devices can enter endpoint management.

## MVP scope

- Read a sanitized local JSON/YAML export of selected restrictions, filters,
  assignments, and Autopilot registrations.
- Evaluate a small, versioned catalogue of Windows enrollment paths against an
  explicit operator-supplied intent such as "corporate devices only."
- Render Markdown and JSON results that label each path `allowed`, `blocked`,
  `unknown`, or `outside-evidence`, with required manual tests.
- Flag unsupported filter properties, contradictory assignment/priority rules,
  missing ownership evidence, and claims the input cannot establish.
- Remain local and read-only: no tenant authentication, Graph API calls, policy
  writes, device enrollment, or security-certification claims.

## Shortlist and wedge-first gate

1. **EnrollFence — selected.** Small-team Intune administrator → Intune portal,
   Microsoft documentation, screenshots, spreadsheet, and test devices → they
   configure and document controls but do not turn a declared policy intent
   into a portable map of permitted/unknown enrollment paths → local,
   credential-free intent-to-path linter for Windows enrollment only → Intune
   documentation searches, Microsoft Tech Community, and targeted r/Intune /
   r/sysadmin policy-path discussions with a sanitized fixture → Microsoft is
   actively documenting multiple Windows enrollment routes and granular
   restriction filters, while a fresh admin report exposes the restored-device
   ambiguity.
2. **PodmanArm Doctor — rejected.** Ubuntu ARM self-hoster moving from Docker
   Compose → distribution packages, Homebrew, Podman documentation, and manual
   dependency debugging → the setup can be frustrating but vendor and distro
   guidance already answer most version/dependency cases → rootless ARM
   compatibility probe → Podman and Ubuntu support searches → a fresh
   r/selfhosted install question. **Kill:** one installation report does not
   prove a recurring >30-minutes-per-week pain or a channel beyond generic
   troubleshooting content.
3. **CloseGap — rejected.** IT support lead moving from reactive tickets to
   proactive operations → ServiceNow, Jira Service Management, ManageEngine,
   and spreadsheets → existing ITSM/automation products already offer workflow
   rules and reporting → ticket-closure-versus-control-coverage audit → ITSM
   communities → one fresh r/sysadmin incident. **Kill:** this collapses into a
   crowded analytics/ITSM workflow category with no narrow first-user wedge.
4. **AIAccess Boundary — rejected.** Enterprise admin allowing one department
   to use an external AI service → Purview DLP, Defender, SSO/session controls,
   vendor contracts, and security review → established platforms handle the
   core policy and monitoring job → AI data-access planner → security and
   Microsoft-administrator communities → a fresh r/sysadmin question. **Kill:**
   the core job is a crowded security-control category and the proposed planner
   would not remove the need for the incumbent controls.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Microsoft Intune enrollment restrictions | The authoritative configuration surface can restrict enrollment by platform, OS version, manufacturer, and ownership. It does not produce an offline intent-versus-path review packet. |
| Direct competitor | Intune enrollment and Autopilot reports | Native reports surface failures, applied policy, and deployment outcomes after an event. They are useful evidence but do not model a proposed policy before a change. |
| Direct competitor | ManageEngine Endpoint Central | A broader endpoint-management suite supports Windows Autopilot onboarding. It is a full management platform, not a credential-free local lint of an existing Intune export. |
| Indirect substitute | Microsoft documentation + portal screenshots + spreadsheet + test device | Flexible and authoritative, but the reviewer must manually join rules across screens and preserve why a route is considered allowed or unknown. |
| Status quo | Change settings and wait for enrollment behavior to reveal a gap | The team discovers an unintended path after a device or user has reached a management boundary, when remediation and audit explanation are harder. |

## Wedge

EnrollFence is not another endpoint-management console or a generic security
scanner. It asks one narrow pre-change question: given a sanitized policy model,
which Windows enrollment paths are evidenced as blocked, allowed, or still
unknown relative to a declared corporate-only intent? It earns attention by
being local, credential-free, and deterministic, producing a review artifact
without touching a tenant. The concrete first-user route is a public sanitized
fixture plus a policy-path explainer for Intune administrators searching for
Company Portal, Autopilot, and restored-device enrollment boundaries.

## Kill condition

Stop or narrow after five Intune administrators if fewer than three say that a
path-by-path packet would change a real enrollment-policy review, or if Intune
ships a first-party export/report that maps configured restrictions and filters
to all relevant Windows enrollment paths before a device enrolls. Also stop if
users want live tenant enforcement or device actions; those needs belong to
existing endpoint-management products and exceed the safe wedge.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | An unintended management enrollment is a real security/compliance risk, though the audience is restricted to teams with managed Windows fleets. |
| Feasibility | 5/5 | A local schema validator, fixed path catalogue, rule evaluator, and Markdown/JSON renderer fit a 1–3 day CLI MVP. |
| Demo potential | 5/5 | A sanitized policy fixture can visibly become a matrix with blocked, allowed, and unknown paths. |
| Distribution | 4/5 | Intune administrators have concrete search terms and public Microsoft/administrator communities; a public fixture and explainer are a repeatable content entry point. |
| Competitive wedge / timing | 3/5 | Native reporting and full endpoint suites are strong substitutes, but they do not occupy the narrow, no-credential pre-change intent-to-path packet. Current Windows enrollment guidance and the fresh policy-boundary question provide timely context, not a hard deadline. |
| Total | 21/25 | Clears the repo threshold and both dimension gates. |

## Decision

**repo-created.** A local dedicated EnrollFence scaffold was created and a
public-safe snapshot is consolidated at [`projects/enrollfence`](../projects/enrollfence).
No dedicated GitHub remote was created or claimed.

## Next build step

Implement `enf-3bs`: a fixture-only policy loader and four-path evaluator,
then validate the emitted packet with five Intune administrators before adding
any input format or path.

## Source access caveats

Reddit public JSON was blocked with the documented `theme-beta` response. The
RSS fallback returned fresh r/sysadmin and r/selfhosted entries; r/Microsoft365
and r/devops then failed their RSS fallback with HTTP 429, so no engagement
counts are claimed. Direct thread retrieval for the selected post was blocked
with the same Reddit response, so its RSS summary is treated as one community
report and no comment evidence is claimed. X `xurl` auth status was checked,
but search returned `401 Unauthorized`; no X evidence is claimed. Web evidence
comes from public Microsoft documentation, a public Intune specialist article,
and public competitor documentation.
