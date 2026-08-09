# StatePin

A serverless status board for self-hosters whose cron jobs, CI, and backups currently disappear into webhook logs.

## Problem

Many self-hosters push cron, CI, backup, and disk-status messages into a Discord or Slack channel. That preserves history, but it is a log, not a current-state view. To answer "is everything OK right now?" they scroll, compare timestamps, and manually infer which latest message superseded which older message.

Full dashboards such as Glance, Homepage, Homarr, Grafana, or Uptime Kuma are useful when the user wants to run another service. The source signal explicitly asks for the opposite: a small always-current board that scripts can update with a one-line HTTP call, without operating a dashboard server.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1vj75nq/current_state_at_a_glance_instead_of_a_webhook/ | Fresh self-hoster says cron jobs, CI, and backups push to Discord webhooks, but scrolling the log makes it hard to answer current status; wants a no-server one-line-curl state view. |
| Healthchecks.io docs | https://healthchecks.io/docs/ | Healthchecks.io monitors cron pings/dead-man-switch behavior and explicitly focuses on pings and alerts rather than arbitrary state cards. |
| Healthchecks dashboard | https://github.com/healthchecks/dashboard | A standalone dashboard exists for Healthchecks checks, confirming demand for simple views, but it depends on Healthchecks check state. |
| Glance | https://github.com/glanceapp/glance | Popular self-hosted dashboard/startpage project; strong substitute when users are willing to run a service. |
| Homepage | https://github.com/gethomepage/homepage | Mature application dashboard with Docker and service API integrations; broader and heavier than a no-server arbitrary-state board. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Healthchecks.io / Cronitor-style heartbeat monitors | Excellent for "did a scheduled job ping on time?" and alerting, but not a minimal arbitrary current-state board for backup age, CI branch, disk percent, and custom notes in one view. |
| Direct competitor | Uptime Kuma, Grafana, Glance, Homepage, Homarr | Powerful dashboards, but the user has to run and maintain another service or integrate with each tool's model. |
| Indirect substitute | Discord/Slack webhook log, Shields.io badges, Gist/Pages hacks | Cheap and familiar, but current state is reconstructed manually from history or brittle snippets. |
| Status quo | Keep dumping messages into a chat channel and scroll when worried | Wastes time every week and can hide stale backups or failed jobs behind newer unrelated messages. |

## Wedge

StatePin is intentionally smaller than monitoring. It stores named cards, not time-series metrics: `backup=ok age=2h`, `ci=green branch=main`, `disk=71%`, `last_import=failed`. The MVP is a hosted or self-deployable signed update endpoint plus a static board view, so scripts can update one card with curl and viewers get the latest state without running a dashboard container.

## Target user

- Self-hosters with cron jobs, CI jobs, backups, and housekeeping scripts already sending chat webhooks.
- Small maintainers who want a private or public current-status page for personal infrastructure without a monitoring stack.
- Users searching for Healthchecks/Uptime Kuma/Glance alternatives because they need arbitrary state, not just pings or service uptime.

## MVP

- `statepin render examples/statepin.yml --out dist/` for a local/static proof.
- Signed `POST /api/cards/<card>` contract documented for a one-line curl update.
- Card schema: key, label, status, value, updated_at, max_age, detail, link.
- Static dashboard with stale/ok/warn/fail styling and a JSON export.
- Synthetic examples for backups, CI, disk, and cron; no real infrastructure data.

## Non-goals

- Not a log aggregator.
- Not a metrics/time-series database.
- Not a full Uptime Kuma, Grafana, Glance, or Homepage replacement.
- No secrets, private hostnames, private IPs, or real webhook URLs in examples.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
