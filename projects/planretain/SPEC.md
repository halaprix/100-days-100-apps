# PlanRetain specification

## User story

As a Project Online PMO administrator, I want a local receipt showing which
user-supplied exports cover projects, tasks, resources, custom fields, and
reported dependencies, so I can prove what remains to archive or test before
the September 30, 2026 retirement.

## Core flow

1. The user exports selected Project Online reports and supplies those files
   explicitly, plus an optional hand-written inventory manifest.
2. PlanRetain reads supported CSV and YAML locally without executing content or
   authenticating to any service.
3. It inventories schema, record counts, time ranges, and cross-file coverage.
4. It flags unprovided categories, unknown field mappings, and missing restore
   evidence as `manual-review` or `not-proven`.
5. It renders deterministic Markdown and JSON packets with a compact
   export/restore-test checklist.

## Feature list

### MVP

- Explicit CSV/YAML input paths only; no recursive machine discovery.
- Project, task, resource, assignment, and custom-field-column inventory.
- User-supplied integration/report references represented as metadata, never
  automatically discovered.
- Conservative coverage model: `covered`, `manual-review`, `not-proven`.
- Path-free Markdown/JSON report and restore-test matrix.
- Tests that prove input text, credentials, local paths, and identifiers are
  not copied into output.

### Later

- Validated adapters for documented Project Online export shapes.
- A guided schema-mapping file for approved source columns.
- Signed export manifests and reproducible archive bundles.
- A CI mode for repository-managed migration evidence.

## Data model

```json
{
  "packet_version": 1,
  "deadline": "2026-09-30",
  "coverage": [
    {"category": "projects", "classification": "covered", "count": 14},
    {"category": "custom-fields", "classification": "manual-review", "count": 6},
    {"category": "integrations", "classification": "not-proven", "count": 0}
  ],
  "restore_test": {"classification": "manual-review"}
}
```

## Technical approach

Start as a small offline Python CLI. It parses only explicit CSV/YAML inputs,
normalizes only headers and counts, and writes deterministic reports to an
output directory chosen by the user. Unsupported formats and missing categories
remain unknown instead of being treated as archived.

## Build plan

1. Add synthetic CSV/YAML fixtures for simple plans, custom-field columns,
   malformed headers, missing categories, and integration references.
2. Implement conservative schema adapters and the coverage model.
3. Render deterministic Markdown and JSON packets plus a restore-test matrix.
4. Add no-network, no-execution, and output-redaction tests.
5. Validate with five Project Online PMO/migration practitioners using redacted
   exports or representative fixtures.
6. Stop if a mature migration provider offers an equivalent free export-first
   archive receipt or practitioners can make one reliably in under 15 minutes.

## Validation plan

- Unit-test classification and unknown handling with synthetic fixtures only.
- Assert report output contains no input values, secret-shaped text, or paths.
- Assert the CLI opens no network connection and never invokes project code.
- Demo an incomplete fixture becoming a manual-review archive packet.
- Compare directly with migration vendors: PlanRetain must add export evidence,
  not claim to replace a migration engine.

## Milestones

- `v0.1.0-alpha.0` — scaffold and specification.
- `v0.1.0-alpha.1` — fixture-driven inventory and coverage report.
- `v0.2.0-alpha.1` — restore matrix and practitioner validation spike.
