# Day 071 — ScheduleMap

Date: 2026-09-04
Status: idea-only

## One-line pitch

A local-first CLI that reconciles scheduled AI-agent jobs into a task-to-run map,
then flags duplicate schedules, orphaned tasks, and jobs with no clear owner
before an unattended workspace quietly stops doing work.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Community report — Reddit RSS fallback | https://www.reddit.com/r/selfhosted/comments/1w6sg7n/i_had_too_many_ai_agents_building_my_ai_agent_31/ | A fresh self-hosted AI-agent operator reports 31 cron jobs for 21 tasks after repeated partial-context sessions, then discovers nothing ran for two days. It is one detailed report, not engagement or consensus evidence. |
| Cronitor — product documentation | https://cronitor.io/cron-job-monitoring | Cronitor explicitly monitors scheduled agent tasks and alerts on missed, failed, or slow runs. This validates that schedule failure is a real operational category, while also setting a high substitute bar. |
| Healthchecks.io — product documentation | https://healthchecks.io/docs/ | Healthchecks models one check per cron job and alerts when expected pings do not arrive. It confirms execution liveness is well served, but it requires each job to report in. |

## Problem

A solo operator who lets several AI-assisted sessions evolve an unattended
workspace can accumulate schedules that look individually valid but no longer
represent a coherent set of tasks. The first visible symptom may be a missed
job, duplicated work, or a dead task that is only discovered days later.

The fresh report is material because the status quo did not merely cost a few
minutes of cleanup: after months of setup, the system had done nothing for two
days. The evidence is still thin—one public account—so this is a validation bet,
not a build mandate.

## Target user

A technical solo operator running multiple scheduled AI-agent workflows who
keeps task, instruction, and schedule configuration in a version-controlled
workspace.

## MVP scope

- Read an explicitly supplied workspace export; run locally and never transmit
  prompts, task content, or credentials.
- Parse a small, documented set of schedule sources first: crontab-style files,
  systemd timer exports, GitHub Actions schedules, and a generic JSON/YAML
  agent-job manifest.
- Produce a task-to-schedule graph with duplicate cadence, overlapping command,
  unlabeled task, and no-owner findings.
- Require an operator-supplied task manifest for semantic claims; otherwise mark
  a job as unlinked rather than guessing from prompt text.
- Emit Markdown and JSON findings with source locations relative to the supplied
  export. Do not execute jobs, modify schedules, or promise run monitoring.

## Shortlist and wedge-first gate

1. **ScheduleMap — selected, idea-only.** Solo operator of a multi-agent
   scheduled workspace → Cronitor, Healthchecks, crontab/systemd views, and
   manual config review → execution monitors discover a missed run only after
   instrumentation, while manual review has no task-level reconciliation across
   sources → local static task-to-schedule graph with duplicate/orphan/ownership
   findings → exact searches for scheduled AI-agent workflows, self-hosted agent
   communities, and open-source agent-framework documentation → a fresh report
   describes 31 schedules for 21 tasks and a two-day silent stop. **Kill:** a
   maintained monitor or scheduler already imports mixed agent schedule sources
   and reports task-level duplicates and ownership gaps without external
   telemetry, or five target operators say reconciliation takes under 30 minutes
   per week and has not caused missed work.
2. **VoiceRange Fixture — rejected.** Browser pitch-tool maintainer → Playwright
   fake-media flags, QA Wolf microphone injection, and generic audio fixtures →
   these already inject controlled audio, while the fresh report only proves one
   low-register threshold bug → prebuilt pitch-boundary fixture matrix → Web
   Audio/Playwright searches and test-tool repositories → one strong but very
   narrow post. **Kill:** QA Wolf or open-source fixture tooling already provides
   calibrated pitch-boundary assertions, or maintainers report the test gap is
   rare. The category is too close to existing test plumbing for a daily winner.
3. **PrivateMailbox Hub — rejected.** Privacy-sensitive multi-account mail user
   → eM Client, Spark, Canary, self-hosted webmail, and desktop clients → the
   requested feature bundle is a full mail client/server product with OAuth,
   push, and delivery complexity → account aggregation server → self-hosted mail
   searches → one request but no narrow distribution path. **Kill:** mature,
   security-sensitive category with no credible 1–3 day wedge.
4. **PressCitation Ledger — rejected.** Indie founder considering syndicated
   releases → press-release distributors, SEO tools, and AI-search visibility
   products → the source is a vendor promotion, not independent demand, and
   attribution to AI answers is difficult to prove → release-to-citation audit
   → founder/PR searches → no validated buyer pain. **Kill:** promotional source
   plus a crowded, claim-heavy SEO category.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Cronitor | It monitors cron jobs and scheduled agent tasks, recording runs and alerting on missed, failed, or slow execution. It is strong at runtime liveness, not a local preflight that reconciles task intent across schedule files. |
| Direct competitor | Healthchecks.io | It provides per-job checks based on expected HTTP pings and can be self-hosted. It detects that an instrumented job did not run, but does not infer whether several configuration sources represent duplicate or orphaned task intent. |
| Indirect substitute | crontab listings, systemd timer views, CI schedule pages, spreadsheets, and manual config review | An operator can inspect each source and maintain a task list by hand. The cost is cross-source reconstruction and no durable review packet. |
| Status quo | Add a schedule while changing an agent workspace, then notice drift only from missing output or duplicated work | The public report describes 31 jobs for 21 tasks and a two-day silent stop. This is consequential, but only one account has reported it in this run. |

## Wedge

ScheduleMap would not compete on runtime alerting. Its narrow job is a
credential-free, static **intent preflight**: turn mixed schedule exports plus a
small task manifest into a reviewable graph before the jobs run. That makes it
useful before operators commit to external ping URLs, dashboards, or agent
telemetry—and leaves execution monitoring to Cronitor or Healthchecks.

The distinction is plausible rather than proven. Cronitor now explicitly markets
scheduled-agent monitoring, so ScheduleMap must demonstrate that static
cross-source task reconciliation catches a failure class those tools do not.

## Kill condition

Reject the bet if Cronitor, Healthchecks, or a maintained open-source scheduler
can import the same mixed schedule sources and flag duplicate task cadence,
missing task ownership, and orphaned task intent without adding runtime
instrumentation. Also reject if five solo multi-agent operators report that
manual reconciliation takes under 30 minutes per week and missed/doubled work
has not blocked a delivery or caused an incident.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | A silent two-day stop or duplicate work can block delivery; only one fresh operator report supports frequency. |
| Feasibility | 4/5 | A read-only parser, explicit task manifest, graph, and report fit a small local CLI; universal agent-config parsing does not. |
| Demo potential | 4/5 | A before/after graph can visibly turn 31 unlabeled schedules into duplicate and orphan findings. |
| Distribution | 3/5 | Searches and communities for scheduled AI-agent workflows are specific, but no repeatable channel or first-user cohort is yet proven. |
| Competitive wedge / timing | 3/5 | Agent schedule sprawl is timely and the static-preflight distinction is concrete, but established monitors are adjacent and well-positioned. |
| Total | 18/25 | The numeric threshold is met, but the required distribution gate fails. |

## Decision

**idea-only.** ScheduleMap scores 18/25 and meets the competitive-wedge gate,
but Distribution is 3/5, below the required 4/5. No dedicated project repository
was created. The source evidence is one detailed fresh report; the responsible
next move is to validate the workflow rather than produce a scaffold.

## Next build step

Interview five solo operators of scheduled AI-agent workspaces and collect
sanitized schedule/task exports. Promote only if at least three contain a
cross-source duplicate, orphan, or unowned job that existing runtime monitoring
does not surface before execution.

## Source access caveats

Reddit public JSON was blocked. RSS fallback provided the fresh r/SideProject
and r/selfhosted listings used for this run; r/SaaS, r/startups, r/webdev, and
r/sysadmin fell back to unavailable/HTTP 429 responses and were not retried.
RSS exposes neither reliable scores nor comment context, so this brief makes no
engagement or consensus claim.

X `xurl` could read the account identity, but its read-only search probe returned
`401 Unauthorized`; no X signal is used. Web research supplied competitor and
platform-documentation validation.
