# Day 082 — AlertDryRun

Date: 2026-09-16
Status: idea-only

## One-line pitch

A local, offline checker that inspects an exported n8n workflow plus redacted
sample error data and shows whether a Telegram error alert can be rendered and
sent without Markdown parse failures.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Community report — Reddit RSS fallback | [r/selfhosted: n8n Telegram node legacy Markdown](https://www.reddit.com/r/selfhosted/comments/1who59f/til_the_n8n_telegram_node_sends_legacy_markdown/) | A self-hoster reports that unpaired Markdown characters caused Telegram alert sends to return `400 can't parse entities`; the affected error handler meant watchdog failures were not delivered. This is one fresh report, not proof of prevalence. |
| Original documentation — n8n error handling | [n8n error workflows](https://docs.n8n.io/flow-logic/error-handling/) | n8n provides error workflows, saved executions, and log streaming after a workflow execution fails. These are recovery/diagnosis tools, not a static message-rendering preflight. |
| Original documentation — n8n Telegram node | [n8n Telegram node](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/) | n8n exposes Telegram message operations and links to Telegram's API and workflow templates. |
| Original documentation — Telegram Bot API | [Telegram formatting options](https://core.telegram.org/bots/api#formatting-options) | Telegram documents text-formatting modes at the API boundary, so message syntax is a real delivery constraint rather than a UI-only concern. |

## Problem

A workflow's error path is often the last place an operator notices bad dynamic
text. If a Telegram alert body includes an unescaped underscore, asterisks, or
brackets under a formatting mode, a delivery failure can hide the original
failure. The fresh report is particularly severe because the broken notification
node sat in the error handler: the operator had neither the original alert nor a
clear reminder to inspect failed executions.

The status quo passes the pain test only for workflows that send operational
errors or watchdog state. Replaying messages manually, reading execution logs,
or discovering a `400` after an incident can easily cost more than 30 minutes
per week and can leave a service failure unreported. A generic "format a
Telegram message" helper is not enough; the value is checking the actual n8n
error path before it is relied on.

## Target user

A self-hosted n8n operator who routes workflow, backup, or watchdog failures to
Telegram and wants a private preflight without granting a new service access to
n8n or Telegram.

## MVP scope

- Accept an explicit n8n workflow JSON export and a redacted JSON fixture for
  the Error Trigger payload; perform no network calls and retain no inputs.
- Identify Telegram Send Message nodes reachable from an Error Trigger or an
  explicitly selected error path.
- Render a constrained subset of n8n expressions against the fixture, flag
  unmatched Markdown delimiters and unsupported/dynamic expressions, and never
  declare unknown content safe.
- Emit a local Markdown/JSON report with the affected node, source expression,
  a safe plain-text fallback suggestion, and a fixture coverage warning.
- Ship fixtures that demonstrate a bad underscore, a valid escaped message, and
  an indeterminate dynamic expression.

## Shortlist and wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| **AlertDryRun — selected** | Self-hosted n8n operators whose Telegram error paths carry dynamic strings → n8n executions/error workflows, manual test runs, Telegram formatters, and custom Code nodes → these discover or patch a failure after execution, and generic escapers do not inspect the exported error route → offline workflow-export plus fixture renderer for Telegram error-path delivery → n8n workflow templates, error-handling searches, and self-hosted automation communities → a fresh report describes alerts silently failing inside the error handler. | Pass, but evidence is only one fresh community report and the repeatable channel remains unproven. |
| **Proxmox panel monitor — rejected** | KDE/Proxmox users checking guest and backup state → ProxMon, Proxmox UI, Grafana, and monitoring stacks → the fresh post already demonstrates a capable panel widget → another monitor has no narrow wedge → self-hosted desktop users → fresh launch. | Reject: direct solution is already being shipped; generic monitoring is crowded. |
| **Course-video self-hosting cost probe — rejected** | Course operators replacing hosted video → Vimeo, Wistia, Gumlet, PeerTube, CDN calculators, and consultants → playback/DRM/analytics failures are intertwined with infrastructure and licensing → cost/reliability comparison → course-hosting communities → fresh report says a four-month self-hosting attempt is failing. | Reject: a trustworthy result needs provider pricing, traffic, DRM, and analytics modelling beyond a 1–3 day MVP. |
| **Cloud-file exit planner — rejected** | Long-time ownCloud users moving platforms → Nextcloud, ownCloud, migration docs, and manual exports → migration is painful but existing platforms and services already own the job → generic exit checklist → self-hosted communities → fresh migration story. | Reject: status quo is unpleasant but the wedge is vague against mature migration paths. |
| **Conditional-access integration mapper — rejected** | Microsoft 365 admins combining endpoint posture and access policy → Entra Conditional Access, CrowdStrike, Zscaler/Cato/Citrix integrations, and consultants → vendor-native integrations and policy platforms already own the control plane → policy mapping report → identity/security communities → fresh r/sysadmin question asks about the architecture. | Reject: crowded security/configuration category and the MVP would risk becoming a generic security wrapper. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | n8n manual execution, saved executions, error workflows, and log streaming | n8n can surface a failure and route an error response after it occurs. It does not prove that a particular exported Telegram error route will render a future dynamic payload safely before activation. |
| Direct competitor | Custom n8n Code node or Telegram formatter/escaper | An operator can escape text themselves, but that requires identifying every dynamic error-field path and maintaining the workaround in each workflow. |
| Indirect substitute | Send a handcrafted test message, inspect the Telegram node manually, or set plain text | Useful for a fixed message, but weak where container names, error text, file names, or other runtime data alter the final text. |
| Status quo | Learn from failed executions or missing alerts during an incident | This is tolerable for noncritical chat automation, but not for an error handler that is supposed to report the failure itself. |

## Wedge

AlertDryRun is not a notification sender, workflow monitor, or generic Markdown
linter. It limits itself to the narrow and demonstrable question: *given this
exported n8n error path and this redacted payload fixture, can the Telegram
message be rendered safely, or is it unproven?* Offline inputs avoid new
credentials and make it reasonable to run before enabling an incident path.

A viable first-user path is a small open-source CLI plus fixtures and a concise
write-up targeting searches for n8n Telegram parse errors and error workflows,
then offering it as a workflow-template companion. That path is concrete enough
to retain the idea, but one fresh report does not yet prove repeatable demand.

## Kill condition

Reject AlertDryRun if three n8n operators with dynamic Telegram error alerts can
make their actual error route safe with a one-line plain-text/escape setting and
no recurring test burden, or if n8n ships native static validation/preflight that
covers dynamic Telegram messages. Also reject if useful checking requires live
workflow credentials or a real Telegram send instead of exports and fixtures.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | A silent failure in an error handler can hide the incident it should report; the evidence is a single fresh report, so this is not a 5. |
| Feasibility | 5/5 | An explicit-input local parser with a conservative expression subset and fixtures is a 1–3 day CLI slice. |
| Demo potential | 4/5 | A workflow export plus a failing payload becoming an actionable node-level report is easy to show; full expression compatibility is deliberately out of scope. |
| Distribution | 3/5 | n8n template/error-handling searches and self-hosted automation communities are specific, but there is no validated repeatable acquisition route yet. |
| Competitive wedge / timing | 3/5 | The static, error-path-specific, no-credentials preflight is distinct from after-the-fact error handling, but custom code and manual testing are cheap substitutes. |
| Total | 19/25 | Above the numeric threshold, but blocked by the distribution gate. |

## Decision

**idea-only.** AlertDryRun scores **19/25** but does **not** qualify for a
dedicated repository: Distribution is **3/5**, below the required **4/5**.
The weakest dimension is Distribution. The product is held pending proof that
n8n operators will reuse an export-and-fixture preflight rather than a
one-off plain-text setting or Code node.

## Next build step

Interview or observe five n8n operators who send dynamic Telegram error alerts;
ask for a redacted workflow export and fixture, then test whether the proposed
checker finds a real issue that a plain-text fallback did not already solve.

## Source access caveats

Reddit's public JSON endpoint returned the documented `403` theme-beta response
for r/SideProject, r/selfhosted, and r/sysadmin. The read-only tool retrieved the
selected r/selfhosted post through the public RSS fallback; RSS does not provide
usable vote or comment metrics, so none are claimed. r/SaaS, r/webdev, and
r/androidapps returned `429` at JSON/RSS layers and were not retried. The
r/sysadmin fresh post informed a rejected candidate only.

The `xurl` identity probe succeeded, but the default profile has no OAuth2 token
and its read-only search probe returned `401 Unauthorized`; no X signal is used.
Web search returned no independently indexed n8n community/GitHub linting result
for the exact problem, so the selected evidence is deliberately scoped to one
fresh community report plus original n8n and Telegram documentation.

## Sources

[1] https://www.reddit.com/r/selfhosted/comments/1who59f/til_the_n8n_telegram_node_sends_legacy_markdown/

[2] https://docs.n8n.io/flow-logic/error-handling/

[3] https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.telegram/

[4] https://core.telegram.org/bots/api#formatting-options
