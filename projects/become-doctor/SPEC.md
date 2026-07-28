# SPEC — BecomeDoctor

## User story

As an operator managing Ubuntu hosts with Ansible, I want a safe pre-upgrade compatibility check for `sudo-rs` and Ansible `become`, so that I can avoid privilege-escalation hangs during maintenance windows.

## Core flow

1. User runs `become-doctor scan --local` or `become-doctor scan --inventory hosts.ini`.
2. The tool detects OS release, `sudo` provider, `sudo-rs` version where available, Ansible version, and become-related settings.
3. The tool optionally runs a safe no-op privilege-escalation prompt probe.
4. A rules engine classifies the host as `ok`, `warning`, `likely-fail`, or `unknown`.
5. The CLI prints a redacted report with the evidence, confidence, and next action.

## Initial CLI shape

```bash
become-doctor scan --local
become-doctor scan --inventory hosts.ini --limit ubuntu_canary
become-doctor explain sudo-rs-ansible-prompt-timeout
become-doctor fixtures list
```

## Data model

```text
HostProbe
- host_alias: redacted stable label
- os_name
- os_version
- sudo_provider: legacy-sudo | sudo-rs | unknown
- sudo_version
- ansible_version
- become_method
- prompt_probe: pass | timeout | mismatch | skipped | unknown
- findings[]

Finding
- id
- severity: info | warning | fail | unknown
- title
- evidence[]
- remediation[]
- public_references[]
```

## Technical approach

- Language: Python CLI, likely `typer` or `argparse` for a small dependency footprint.
- Inventory parsing: start with INI/YAML inventory support; do not require full Ansible runtime for fixture tests.
- Probe mode: use safe commands only, redact command output by default, and make remote probing opt-in.
- Rules: versioned YAML/JSON rules for Ubuntu release + sudo provider + Ansible version + probe result.
- Tests: fixture snapshots for known combinations, including Ubuntu 26.04 + ansible-core 2.20.1 + `sudo-rs` prompt timeout.

## Validation plan

- Unit-test the rules engine with public issue-derived fixtures.
- Integration-test `scan --local --fixture ...` without privileged CI.
- Validate output against the public Ansible issue, Ubuntu announcement, and Ubuntu bug archive.
- Share the first alpha with r/ansible/r/sysadmin-style upgrade threads and ask whether the report catches their real failure mode.

## Privacy and safety

- Redact hostnames, usernames, IPs, full paths, inventory group names, and command lines in exported reports.
- Do not store credentials.
- Do not mutate remote hosts in the MVP.
- Make any privilege-escalation probe explicit and no-op.

## Milestones

- v0.1.0-alpha.0 — repo scaffold.
- v0.1.0-alpha.1 — fixture-backed rules engine and `scan --local --fixture` demo.
- v0.2.0-alpha.1 — inventory parser and safe local probe.
- v0.3.0-alpha.1 — remote no-op probe behind an explicit flag.
