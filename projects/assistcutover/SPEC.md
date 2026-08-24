# SPEC — AssistCutover

## User story

As an engineer responsible for an Assistants API application, I want a local
readiness packet that shows every migration-sensitive dependency and its test
obligation, so I can plan a safe Responses API cutover before the shutdown.

## Core flow

1. Run `assistcutover scan .` in the application repository.
2. Scan known JavaScript/TypeScript and Python source files without executing
   them or reading environment files.
3. Classify legacy API usage by migration concern and severity.
4. Write `assistcutover-report.json` and `assistcutover-report.md`.
5. Use `--fail-on high` in CI until all blocking patterns have owners/tests.

## Feature list

- Detection rules for SDK calls and raw endpoint strings.
- Findings for assistant configuration, thread/message/run lifecycle, dynamic
  assistant creation, Code Interpreter, File Search/vector stores, and function
  tool schemas.
- Ordered migration checks derived from documented target patterns.
- Source locations, confidence, and a stable finding ID for CI baselining.
- Redaction-by-design: report code paths and rule IDs, never source contents or
  environment values.

## Data model

```text
Report
  version: string
  generated_at: string
  target: string
  findings: Finding[]
  summary: { low, medium, high }

Finding
  id: string
  category: enum
  severity: enum
  path: relative path
  line: number
  migration_check: string
  confidence: enum
```

## Technical approach

A Python CLI walks only source extensions, ignores version-control/dependency
folders, and evaluates deterministic text/AST-aware rules. The first release
will favor explicit false-positive controls over speculative rewrites. Markdown
and JSON renderers consume the same in-memory report.

## Validation plan

- Fixture repositories cover each detection category and a clean repository.
- Golden Markdown/JSON reports assert locations, severity, and redaction.
- The scanner must never read `.env` files or make network calls.
- Validate the wedge with five Assistants API maintainers: ask whether the
  packet found a dependency that their first manual checklist missed. Narrow to
  dynamic-creation and persistent-state migration if it does not.

## Milestones

- `v0.1.0-alpha.0` — scaffold and decision record.
- `v0.1.0-alpha.1` — scanner rules with fixtures and JSON output.
- `v0.2.0-alpha.1` — Markdown packet, baseline support, and demo fixture.
