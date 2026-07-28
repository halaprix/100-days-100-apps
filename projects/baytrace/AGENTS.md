# Agent Instructions — BayTrace

BayTrace is a public, local-first diagnostic CLI for flaky homelab SATA/storage detection.

## Rules

- Keep the project public-safe: never commit real hostnames, private mount paths, disk serial numbers, IPs, logs with personal data, or credentials.
- The MVP must be read-only. Do not add destructive disk tests without explicit flags, warnings, and tests.
- Prefer synthetic fixtures for `lsblk`, `lspci`, `dmesg`, `udevadm`, and `smartctl` output.
- Redact or hash serial numbers by default in shared reports.
- Use conventional commits.
- Use `bd` for task tracking; do not use markdown task lists as a tracker.

## Verification

Before claiming work is complete, run the relevant tests or focused checks and include the command output in the handoff.
