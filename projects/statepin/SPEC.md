# SPEC — StatePin

## User story

As a self-hoster with small scripts and jobs, I want each job to update a named status card with a one-line command, so that I can see current state without scrolling webhook logs or running a monitoring server.

## Core flow

1. User creates a board config with card names and stale thresholds.
2. A script updates one card after a run, for example `curl -X POST .../cards/backup` with a signed payload.
3. StatePin stores the latest value for that card and updates the board.
4. Viewer opens a static/private board and sees current status plus stale warnings.
5. User can export JSON or Markdown for support/debugging.

## MVP scope

### v0.1.0-alpha.1

- Local renderer: `statepin render examples/statepin.yml --out dist/`.
- Example card data for backup age, CI status, disk usage, and import job result.
- Deterministic stale-state calculation from `updated_at` and `max_age`.
- HTML dashboard plus JSON export.

### v0.2.0-alpha.1

- Minimal signed update endpoint contract.
- Cloudflare Workers or equivalent serverless reference deployment.
- Curl snippets generated per card without printing secrets.

## Data model

```yaml
board:
  title: Homelab current state
  generated_at: 2026-08-09T00:00:00Z
cards:
  - key: backups
    label: Backups
    status: ok
    value: ok 2h ago
    updated_at: 2026-08-09T00:00:00Z
    max_age: PT6H
    detail: Latest synthetic backup completed.
    link: null
```

Card status values: `ok`, `warn`, `fail`, `unknown`, `stale`.

## Technical approach

- Keep the first slice static and deterministic.
- Use Python or TypeScript CLI only after the scaffold; no framework until rendering needs it.
- Treat the update endpoint as an interface first, then implement the smallest serverless adapter.
- Public examples must use synthetic labels and no private infrastructure details.

## Competitor validation plan

- Compare the first demo against Discord webhook logs, Healthchecks badges, Healthchecks dashboard, Glance, Homepage, and Uptime Kuma.
- Kill or narrow if reviewers say Healthchecks badges/dashboard already cover arbitrary card state with no practical extra setup.
- Kill or narrow if the required hosted endpoint makes the product feel like just another monitoring SaaS.
- Keep if self-hosters can reproduce the source user's desired "one-line curl, no dashboard server" flow in under 10 minutes.

## Milestones

- v0.1.0-alpha.0 — repo scaffold.
- v0.1.0-alpha.1 — static renderer with synthetic card data.
- v0.2.0-alpha.1 — signed update endpoint proof.
- v0.3.0-alpha.1 — deployable demo and README walkthrough.
