# Day 060 — AssistCutover

Date: 2026-08-24
Status: repo-created

## One-line pitch

A local-only CLI that turns an OpenAI Assistants API repository into a migration
readiness packet before the August 26, 2026 sunset.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Original platform announcement | https://community.openai.com/t/assistants-api-beta-deprecation-august-26-2026-sunset/1354666 | OpenAI states that the Assistants API beta will sunset on August 26, 2026 and recommends the Responses API. |
| Official migration guide | https://developers.openai.com/api/docs/assistants/migration | The guide has side-by-side target patterns, including replacing thread state with conversations. |
| Developer community report | https://community.openai.com/t/assistants-api-beta-deprecation-august-26-2026-sunset/1354666 | A maintainer describes non-1:1 issues around dynamically created assistants and prompt objects; a related migration-experience topic was active on August 15, 2026. |

## Source access caveats

- Reddit public RSS fallback was reachable for `r/sysadmin`, but the fresh posts
  did not substantiate this API-migration bet, so they are intentionally not
  padded into the evidence table.
- `xurl whoami` worked, but `xurl search` returned `401 Unauthorized`; X search
  was therefore unavailable and no X signal is claimed.
- The winner is supported by original OpenAI documentation and its public
  developer community rather than a claim of broad cross-platform consensus.

## Problem

The hard sunset is two days away. Official documentation explains the target
architecture but cannot tell a team which legacy calls, state assumptions,
dynamically created assistants, tools, or file/vector-store dependencies exist
in its codebase. Manual grep and a generic coding-agent prompt make it easy to
miss a blocking dependency until deployment.

This passes the status-quo pain test: a missed dependency can block a production
AI feature or force an emergency migration, not merely cost a few minutes.

## Target user

A small product or platform team responsible for a JavaScript/TypeScript or
Python application that still uses the OpenAI Assistants API.

## Shortlist and wedge-first gate

| Candidate | Wedge-first gate | Outcome |
|---|---|---|
| AssistCutover | Assistants API maintainers → OpenAI migration docs plus grep → no repository-specific inventory of state/tool risks → local static readiness packet → OpenAI Developer Community migration threads and GitHub code search → API sunsets August 26, 2026 | **Selected**; narrow, offline preflight answers the urgent first question. |
| Entra change receipt | Microsoft 365 identity admins → service-health feeds and NVD → advisory wording can change faster than teams can record decisions → cloud-advisory receipt → M365 admin communities → current Entra CVE discussion | Rejected before scoring: existing alert/ITSM products and vendor notices already cover the job; a generic receipt has no concrete first-user path. |
| LAPS recovery matrix | Windows recovery admins → Windows LAPS portals, PowerShell, and privileged-access tools → policy/history edge cases are confusing → recovery-decision helper → Windows admin forums → current recovery thread | Rejected before scoring: password-recovery workflows are security-sensitive and existing privileged-access controls are the right system of record; a new tool would create trust risk. |
| Legacy server triage card | Small IT teams inheriting Windows Server 2003-era systems → tickets, inventories, and consultants → ad-hoc incident notes do not produce a retirement plan → read-only legacy-risk card → MSP and sysadmin communities → fresh legacy-server reports | Rejected before scoring: broad asset/risk-management incumbents already own the workflow; the narrow wedge and repeatable channel are not strong enough. |

## MVP scope

- Local scan only; no API calls, uploads, credentials, or code execution.
- Detect JavaScript/TypeScript/Python SDK calls and raw Assistants endpoints.
- Flag Assistants, Threads, Messages, Runs, dynamic assistant creation, function
  tools, Code Interpreter, File Search, and vector-store usage.
- Generate JSON and Markdown reports with source locations, migration checks, and
  `--fail-on high` for CI.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | OpenAI Assistants migration guide | Strong authoritative target-state guidance; it does not inspect a repository or produce a project-specific risk packet. |
| Indirect substitute | IDE search, grep, generic coding agents, hand-written migration checklist | Can find simple symbols, but it neither classifies semantic dependencies nor provides a stable auditable report. |
| Status quo | Delay migration or fix failures after the sunset | Avoidable outage/emergency-work risk; tolerable only when a repository has already completed a full inventory. |

## Wedge

AssistCutover is not another agent framework or automatic codemod. It is the
first local, deterministic preflight: a team gets a reviewable inventory and
ordered proof obligations before changing code. The scope is deliberately
limited to the specific sunset and languages with a short buildable MVP.

## Kill condition

Reject or narrow if (a) an official OpenAI codemod/preflight ships that covers
dynamic creation, state, tools, and file dependencies; or (b) five relevant
maintainers report that a simple IDE search plus the official guide reliably
captures every risk in under 15 minutes.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 5/5 | A hard retirement can block a production feature and turn an inventory gap into an emergency migration. |
| Feasibility | 5/5 | Deterministic local rules and Markdown/JSON reporting fit a 1–3 day CLI MVP. |
| Demo potential | 5/5 | A deliberately risky fixture can visibly become an ordered readiness packet. |
| Distribution | 4/5 | Specific terms and active migration threads create a repeatable path through the OpenAI Developer Community and public GitHub code search; no generic launch-only plan. |
| Competitive wedge / timing | 3/5 | The official guide is strong, but it does not inspect code. The two-day deadline creates a sharp but short-lived wedge. |
| Total | 22/25 | Clears the creation threshold and both dimension gates. |

## Decision

**Repo created locally.** The dedicated sibling repo and public-safe master
snapshot are `projects/assistcutover`. No dedicated GitHub remote was created
or claimed. The weakest dimension is competitive wedge/timing (3/5): this is a
valuable deadline tool, not a durable generic migration platform.

## Next build step

Implement fixture-backed detection rules for Python/JavaScript Assistants,
Threads, and Runs calls, then render the first JSON/Markdown packet.
