# SPEC — TzDrift

## User story

As a sysadmin facing a timezone-law change or tzdata advisory, I want a local report of stale timezone data and local-time scheduler risk, so that I can patch the right systems before cron jobs, logs, reports, billing windows, or user-facing schedules drift.

## Core flow

1. Run `tzdrift scan --local --event sunshine-2026` on a workstation or server.
2. TzDrift collects safe local facts: OS, timezone, tzdata package/version, libc hint, Java runtime tzdata hint, cron/systemd timer patterns, and container/Dockerfile hints when supplied.
3. TzDrift compares facts to a bundled ruleset with source links.
4. The CLI prints a risk summary and writes `tzdrift-report.md` plus `tzdrift-report.csv`.
5. The operator reviews manual remediation links and can rerun after patching to produce a before/after packet.

## Data model

```text
HostProfile
- source: local | package-list | dockerfile | docker-inspect | java-output
- os_family
- os_version
- timezone
- tzdata_version
- libc_family
- java_runtimes[]
- schedulers[]
- containers[]

RuntimeTimezoneProfile
- runtime: java | python | node | system
- version
- tzdata_version
- detection_method
- confidence

SchedulerFinding
- scheduler: cron | systemd-timer | application-config
- schedule_expression
- timezone_mode: local | utc | unknown
- risk_level
- evidence

EventRule
- id
- title
- affected_regions[]
- latest_known_tzdata
- source_links[]
- checks[]
```

## Technical approach

- Start as a Python CLI with no network requirement for the core scan.
- Keep rules in YAML with source links to IANA, vendor pages, and public legislation/news pages.
- Use pluggable collectors for package managers (`dpkg`, `rpm`, `apk`, `pacman`), Java runtime output, cron files, and systemd timer units.
- Treat all sensitive identifiers as optional/redacted fields in reports.
- Provide fixtures instead of real infrastructure data.

## Validation plan

- Unit tests for version parsing across Debian/Ubuntu, RHEL/Fedora, Alpine, Arch, and Java outputs.
- Fixture tests for cron/systemd timer risk classification.
- Golden-file tests for Markdown/CSV exports.
- Public-safety tests that synthetic reports do not contain private hostnames, private IPs, or secrets.
- Wedge validation: publish one sample Sunshine Protection Act readiness packet and see whether sysadmin/SRE readers ask for distro, Java, or container support next.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and spec.
- v0.1.0-alpha.1 — local host inventory and Markdown report.
- v0.1.0-alpha.2 — offline package-list, Dockerfile, and Java output parsers.
- v0.2.0-alpha.1 — synthetic demo bundle and CSV export.
