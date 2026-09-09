# Day 076 — RunnerReady

Date: 2026-09-09
Status: idea-only

## One-line pitch

A read-only GitHub Actions CLI that turns an organization's self-hosted runner
versions and their end-of-life dates into a redacted upgrade-readiness packet
before unsupported runners interrupt CI.

## Evidence

| Source | Link | Signal |
|---|---|---|
| GitHub Actions changelog | [Early September 2026 updates](https://github.blog/changelog/2026-09-03-github-actions-early-september-2026-updates/) | GitHub added an API that returns registration and runtime support end dates for a specified runner version, making fleet-level upgrade planning timely.[1] |
| GitHub REST API documentation | [Self-hosted runners](https://docs.github.com/en/rest/actions/self-hosted-runners) | Organization runner inventory exposes runner version, status, and labels; the new organization endpoint exposes a version's runtime/registration end-of-life dates.[2] |
| Actions Runner Controller | [actions/actions-runner-controller](https://github.com/actions/actions-runner-controller) | A substantial Kubernetes-based runner-management substitute exists; the wedge must be version-deprecation triage, not runner provisioning or autoscaling.[3] |
| Reddit RSS fallback | [r/startups: accelerator applicants deserve a response](https://www.reddit.com/r/startups/comments/1wb63f3/vcsaccelerators_partners_deserve_to_know/) | A fresh founder report describes delayed decisions blocking time-sensitive planning. It informed a rejected application-status idea, not the selected runner-management bet.[4] |

## Problem

Self-hosted runner owners can list installed versions and now query end-of-life
schedules, but GitHub's API is still a primitive: an operator has to collect
versions, deduplicate them, query each schedule, interpret offline/busy/label
context, and turn that into an upgrade order and change record. Waiting until a
runner stops registering or running jobs can block CI and turn a planned
maintenance task into an incident.[1][2]

The status quo passes the pain test for an organization with production CI on
self-hosted runners: a runner-support deadline can interrupt deployments and
manual triage across a fleet can easily exceed 30 minutes. It does not justify a
separate tool for a single runner whose version is already known.

## Target user

A GitHub Actions organization administrator or platform engineer responsible for
a heterogeneous self-hosted runner fleet, especially one with persistent runners
outside Kubernetes and no existing fleet-upgrade record.

## MVP scope

- Accept explicit, user-supplied JSON exports from the GitHub organization
  runner-list and runner-version end-of-life endpoints; do not discover accounts
  or scan machines.
- Normalize runner version, online/busy state, labels, and support dates into a
  deterministic risk order.
- Emit a Markdown and JSON upgrade-readiness packet: affected versions, runtime
  versus registration deadline, runner counts, unknown data, and an owner/check
  checklist.
- Support fixture-only demo data and redact runner names by default.
- Do not update runners, create tickets, change runner groups, retain access
  tokens, or call remote APIs in the first build.

## Shortlist and wedge-first gate

1. **RunnerReady — selected, held as idea-only.** GitHub Actions organization
   administrator with several self-hosted runner versions → GitHub's new
   per-version end-of-life API, runner inventory endpoint, scripts, and Actions
   Runner Controller → these expose facts or manage Kubernetes runners but do
   not produce a reviewable, version-to-fleet upgrade order from supplied data →
   read-only runner deprecation packet → GitHub Actions documentation/searches,
   GitHub Marketplace validation, and targeted GitHub Actions community threads
   → GitHub exposed the version-deprecation API on September 3. **Kill:** five
   administrators can turn native API output into a complete upgrade order in
   under 15 minutes, or an established runner-management product ships the same
   version-to-fleet EOL packet.
2. **Accelerator decision-deadline receipt — rejected.** Founder awaiting an
   accelerator decision → deadline calendars, Notion trackers, and accelerator
   management systems → the fresh report shows real planning harm, but the
   buyer who can fix the communication problem is the program, while founders
   already have adequate reminder tools → applicant-side decision/escalation
   packet → founder/accelerator communities → no credible narrow distribution
   path or proof that a new tool changes program behavior. **Kill:** crowded
   tracking/calendar substitutes and a two-sided buyer problem.[4]
3. **Offline voice-to-invoice QA companion — rejected.** Solo seller recording
   sales by voice → invoice apps, bookkeeping software, and manual review → a
   fresh side-project post demonstrates implementation interest, not a repeated
   reconciliation failure that existing apps miss → transcription confidence and
   line-item review receipt → generic small-business audience → no evidence of
   a sharp workflow wedge. **Kill:** generic invoicing is crowded and the status
   quo pain was not established.
4. **Live-coding presence disclosure checker — rejected.** VS Code-extension
   author adding public presence → extension marketplace disclosure, privacy
   policy generators, and manual copy review → a fresh post describes data
   fields a specific product may share, but does not show repeated author pain
   or willingness to switch → manifest-to-disclosure diff → generic extension
   authors → insufficient demand and distribution proof. **Kill:** one product
   announcement is not demand evidence.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | GitHub self-hosted runner inventory plus runner-version EOL API | Native and authoritative. It returns runner versions and a selected version's support schedule, but leaves fleet-level joining, prioritization, and a review packet to the operator.[1][2] |
| Direct competitor | Actions Runner Controller | A mature Kubernetes controller for GitHub Actions runners. It is a strong substitute for ARC-managed fleets, but it is not a cross-environment, read-only EOL triage packet.[3] |
| Indirect substitute | `gh api`/curl script, spreadsheet, and maintenance ticket | Flexible and cheap, but the version-by-version joins and evidence are recreated for each upgrade window. |
| Status quo | Notice a registration/runtime failure, then inventory and upgrade runners during an incident | Risks a blocked CI/deployment path and loses a calm review window. |

No dedicated runner-version EOL packet product was verified in the small public
search used here. That is not evidence that none exists; it is why the wedge is
scored conservatively.

## Wedge

RunnerReady is not another runner controller, dashboard, or updater. Its narrow
job is to turn explicit GitHub API exports into a redacted, deterministic
maintenance packet that distinguishes runtime from registration risk, groups
identical versions, and keeps uncertainty visible. The September API release is
the reason this exact report can now be built without scraping release notes.[1]

The first-user channel is plausible but not yet validated: GitHub Actions
Marketplace discovery plus precise documentation/search content around runner
version deprecations and focused GitHub Actions community discussions. That is
a named audience, but not proven repeatable access, so it does not clear the
repo-creation distribution gate.

## Kill condition

Stop or narrow RunnerReady if five administrators with multiple runner versions
can produce a complete, reviewable upgrade order from the native endpoints in
under 15 minutes. Also stop if Actions Runner Controller or another established
fleet product adds a comparable cross-version EOL packet, or if users refuse
explicit JSON export and require credential-holding SaaS integration before
seeing value.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 3/5 | Unsupported runners can interrupt CI, but the acute pain is concentrated in multi-version fleets and no fresh operator report was retrieved. |
| Feasibility | 5/5 | Fixture-driven JSON normalization and deterministic Markdown/JSON reports are a 1–3 day local CLI MVP. |
| Demo potential | 5/5 | A synthetic mixed-version fleet becoming a deadline-ranked, redacted packet is immediately legible. |
| Distribution | 3/5 | The affected GitHub Actions audience is specific, but Marketplace/community discovery is a hypothesis rather than a proven repeatable channel. |
| Competitive wedge / timing | 3/5 | The new vendor API is a timely enabler, but native endpoints, scripts, and Actions Runner Controller are strong substitutes. |
| Total | 19/25 | Clears the numeric threshold but fails the Distribution gate. |

## Decision

**idea-only.** RunnerReady scores 19/25, but Distribution is 3/5, below the
required 4/5 for a dedicated repo. The idea is worth a validation spike, not a
new project repository: prove that operators value a fleet packet beyond the
native endpoint before scaffolding.

## Next build step

Interview or observe five GitHub Actions organization administrators with
multi-version self-hosted fleets, then run a fixture-backed packet prototype
against their redacted exports and measure whether it replaces more than 15
minutes of manual upgrade planning.

## Source access caveats

Reddit public JSON was blocked with the documented `403` theme-beta response.
The read-only tool used RSS fallback for r/SideProject and r/startups; r/SaaS,
r/selfhosted, r/sysadmin, and r/webdev then returned `429` and were not retried.
RSS does not expose reliable score or comment metadata, and the selected
RunnerReady bet does not claim Reddit validation; the single RSS post informed a
rejected alternative only.

The `xurl` auth probe found no OAuth2 token on the default profile, and the
read-only X search probe returned `401 Unauthorized`; no X signal is used.
General web searches for runner-deprecation competitors returned no results, so
competition is described only from directly retrieved GitHub documentation and
Actions Runner Controller. Direct retrieval of those public GitHub sources
succeeded.

## Sources

[1] https://github.blog/changelog/2026-09-03-github-actions-early-september-2026-updates — GitHub Actions: Early September 2026 updates
[2] https://docs.github.com/en/rest/actions/self-hosted-runners — REST API endpoints for self-hosted runners
[3] https://github.com/actions/actions-runner-controller — Actions Runner Controller
[4] https://www.reddit.com/r/startups/comments/1wb63f3/vcsaccelerators_partners_deserve_to_know — VCs/accelerators partners: founders deserve to know if you discarded them
