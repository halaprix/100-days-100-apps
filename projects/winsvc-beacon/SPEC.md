# SPEC — WinSvcBeacon

## User story

As a Windows-heavy small-team sysadmin, I want a dry-run-first way to turn selected Windows Service states into Uptime Kuma push checks, so that I can monitor important services without deploying a full observability stack or trusting a one-off script.

## Core flow

1. Admin creates `services.yml` with service names and Uptime Kuma push targets.
2. `winsvc-beacon plan --config services.yml` validates the service names against a fixture in v0 and local Windows service data later.
3. `winsvc-beacon emit-powershell --config services.yml` generates the least-surprising PowerShell check script and Task Scheduler registration command.
4. `winsvc-beacon packet --config services.yml` exports a Markdown handoff packet with service mapping, monitor schedule, dry-run result, and rollback notes.

## Data model

```yaml
services:
  - name: W3SVC
    display_name: World Wide Web Publishing Service
    expected: Running
    kuma_push_url_env: KUMA_W3SVC_PUSH_URL
    grace_seconds: 120
schedule:
  every_minutes: 1
  task_name: WinSvcBeacon
packet:
  redact_push_urls: true
```

## Technical approach

- Start as a small Python CLI with no network calls required for the fixture demo.
- Use fixtures under `examples/` to model Windows service inventory and check output before real Windows integration exists.
- Keep generated PowerShell readable and auditable.
- Treat push URLs as secrets: read from environment variables, redact in packets, and never commit examples with real URLs.
- Make all write-like actions explicit: `plan` and `packet` are read-only; script/task installation belongs in a later confirmed command.

## Validation plan

- Fixture tests verify service-name matching, missing-service warnings, expected-state checks, and redacted packet output.
- Demo shows one healthy service, one stopped service, and one typo in `services.yml`.
- Wedge validation: answer/search content around "Uptime Kuma Windows service monitor" and "monitor Windows Services with Uptime Kuma" with the generated packet rather than a generic monitoring pitch.
- Kill condition: narrow or stop if Uptime Kuma ships first-party Windows service checks with installer, service discovery, dry-run validation, and redacted handoff output.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and product spec.
- v0.1.0-alpha.1 — fixture-backed CLI with `plan` and `packet`.
- v0.2.0-alpha.1 — generated PowerShell script and Task Scheduler instructions.
- v0.3.0-alpha.1 — real Windows service inventory integration tested on Windows.
