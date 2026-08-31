# EnrollFence specification

## User story

As an Intune administrator, I want to evaluate a sanitized export of my Windows
enrollment configuration against an explicit corporate-device-only policy so I
can review permitted paths and evidence gaps before changing tenant settings.

## Inputs

- Local JSON or YAML fixture/export containing only selected policy metadata:
  enrollment restrictions, filters, assignments, Autopilot registrations, and
  an operator-provided intent statement.
- A built-in, versioned catalogue of supported Windows enrollment paths and the
  facts each path needs for a safe decision.

The MVP must reject unrecognized fields by default and redact/avoid values that
could identify a user, device, or tenant.

## Outputs

- Human-readable Markdown review packet.
- Machine-readable JSON result.
- Per-path outcome: `allowed`, `blocked`, `unknown`, or `outside-evidence`.
- Rule-level evidence, missing facts, warnings, and required human tests.

## Feature slices

1. Validate a small fixture schema and reject unsafe/unrecognized input.
2. Model a fixed set of Windows enrollment paths with explicit assumptions.
3. Evaluate filter support, policy priority, assignment scope, and ownership
   evidence without modifying any remote system.
4. Render a dated packet with outcome matrix, warnings, and test checklist.
5. Add fixtures for corporate Autopilot, personal enrollment, restored-device,
   and conflicting-policy scenarios.

## Data model

```text
PolicyExport
  intent: string
  restrictions: Restriction[]
  filters: Filter[]
  assignments: Assignment[]
  autopilotRegistrations: Registration[]

PathAssessment
  pathId: string
  outcome: allowed | blocked | unknown | outside-evidence
  evidence: string[]
  warnings: string[]
  requiredTests: string[]
```

No live tenant data, credentials, device identifiers, user identifiers, or raw
configuration files are retained by the tool.

## Build plan

1. Implement schema and fixture loader using the standard library.
2. Encode a sourced path catalogue with source-date metadata.
3. Implement deterministic rule evaluation and report rendering.
4. Add unit tests and sanitized fixtures.
5. Validate the packet with five Intune administrators before expanding scope.

## Validation plan

- Unit-test each outcome against sanitized fixture input.
- Assert the tool does not make network calls or require credentials.
- Test that unrecognized input and missing ownership evidence fail closed to
  `unknown` rather than claiming a policy is safe.
- Ask five target administrators whether the packet changes a real review;
  stop or narrow if fewer than three would trial it.
