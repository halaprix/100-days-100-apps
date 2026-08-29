# SPEC — SwapCheck

## User story

As a Copilot Business or Enterprise administrator, I want a local migration
packet that joins named model references with a policy export and a dated
retirement manifest, so that I can approve alternatives and retests before
availability changes interrupt a workflow.

## Core flow

1. The user supplies a local policy export, a checked-out repository, and the
   bundled or pinned migration manifest.
2. SwapCheck scans only supported text configuration paths for named model
   references and normalizes policy states.
3. It matches references against the manifest and renders a Markdown/JSON
   packet with affected workflows, suggested alternative, policy requirement,
   and a human-owned retest item.
4. `swapcheck check --fail-on retired` exits nonzero when CI detects a model
   already retired or scheduled to retire within the configured window.

## Feature list

- `swapcheck inventory <path>` for configurable, allowlisted text files.
- `swapcheck check --policy policy.json --manifest models.yml <path>`.
- Retirement-date and policy-state matcher.
- Markdown and JSON report renderers.
- Safe path, file-size, and secret-pattern exclusions.
- Fixture-backed tests for explicit, inherited, disabled, and unknown policies.

## Data model

```text
PolicyModel: model, state, scope, source_file
Reference: model, path, line, context_kind
Migration: retiring_model, retirement_date, alternatives, policy_note, source_url
Finding: severity, reference, policy_state, migration, required_retest
Report: generated_at, manifest_version, findings, skipped_paths
```

Reports store relative paths and line numbers only. They never include source
file contents, policy tokens, user prompts, completion data, or credentials.

## Technical approach

Implement a Python standard-library CLI. Treat the policy export and local
repository as sensitive inputs: do not upload them, do not access GitHub, and
redact model-adjacent values that match credential-like patterns. A small,
versioned manifest is bundled as public data and must cite GitHub's changelog.

## Validation plan

- Unit-test manifest parsing, date-window logic, policy-state resolution, and
  safe reference extraction.
- Integration-test fixture repositories with model names in supported config
  formats and ignored secret files.
- Demonstrate a report for a retired model that is both policy-enabled and
  policy-disabled, plus an unaffected reference.
- Validate the wedge with five Copilot administrators or platform engineers:
  proceed only if at least three would use the report in a model-change review.
- Verify that the tool never makes network calls in its default command path.

## Milestones

- `v0.1.0-alpha.0` — scaffold and specification.
- `v0.1.0-alpha.1` — manifest parser and fixture inventory.
- `v0.2.0-alpha.1` — policy matching and Markdown/JSON packet.
- `v0.3.0-alpha.1` — CI failure mode and five-user wedge validation.
