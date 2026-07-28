# SPEC — DiskTrace

## User story

As a Windows Server administrator investigating intermittent freezes, I want a safe disk-I/O trace plan before I enable collection, so that I can capture useful pre-crash evidence without filling disks, harming production performance, or leaking unnecessary details.

## Core flow

1. Admin describes the incident in a local JSON/YAML fixture: symptoms, server role, VM/physical, desired attribution fields, retention window, allowed overhead, and existing tooling.
2. `disktrace plan` validates the request and classifies risky assumptions.
3. The planner recommends a bounded collection strategy: counters first, ETW/WPR or ProcMon only when the requested attribution requires it, explicit stop/rotation limits, and support handoff notes.
4. The tool writes a Markdown packet and optional JSON findings for review or escalation.

## Data model

### IncidentProfile

- `system`: Windows version family, server role, VM/physical/unknown, storage type if known.
- `symptom`: unresponsive, crash, high latency, unknown; recurrence frequency; last observed time.
- `needed_fields`: timestamp, process, PID, file path, read/write rate, total activity, response time.
- `collection_constraints`: max duration, max log size, allowed overhead, can reboot, can install ADK, can run Sysinternals.
- `existing_observations`: PerfMon counters, event logs, storage alerts, application logs.

### Finding

- `severity`: blocker, warning, info.
- `code`: stable finding ID.
- `message`: concise operator-facing statement.
- `rationale`: why this matters.
- `recommended_action`: next safe step.
- `references`: public docs links.

### Packet

- profile summary,
- recommended collection ladder,
- command templates with placeholders,
- retention/rotation limits,
- risk notes,
- support handoff checklist,
- redaction checklist.

## Technical approach

- Language: Python CLI initially; standard library plus a small CLI parser is enough for v0.
- Start fixture-only so every demo is public-safe and reproducible.
- Implement deterministic rules instead of an LLM dependency:
  - broad file-path tracing + long duration => blocker,
  - VM + guest-only tracing => warn to consider host/storage layer,
  - process/PID without file path => counters/resource monitor are enough,
  - exact file path attribution => WPR/ProcMon branch with strict duration/size limits,
  - automatic startup requested => require stop condition and storage budget.
- Export Markdown first; JSON output supports future tests and UI.

## Validation plan

- Unit tests for fixture parsing and finding codes.
- Golden Markdown packet snapshots for three synthetic cases:
  1. safe counter-only triage,
  2. risky broad ProcMon-style continuous capture,
  3. VM disk latency where host/storage evidence is required.
- Public-safety scan: no secrets, private paths, private hostnames, private IPs, or real trace data in examples.
- Wedge validation: publish a short "PerfMon vs ProcMon vs WPR for intermittent disk stalls" post and see whether sysadmins use the generated packet language in replies/support handoffs.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and spec.
- v0.1.0-alpha.1 — fixture parser, rules, JSON findings.
- v0.1.0-alpha.2 — Markdown packet export and golden examples.
- v0.2.0-alpha.1 — runnable CLI with packaged examples and docs.
