# SPEC — PipeTwin

## User story

As a maintainer with a CI failure that does not reproduce on my laptop, I want to turn the failed run or job log into a local repro bundle, so that I can debug without pushing blind commits and waiting on hosted runners.

## Core flow

1. User runs `pipetwin capture <failed-run-url-or-log-file>`.
2. PipeTwin reads public metadata or a pasted log file.
3. PipeTwin extracts the commit SHA, workflow/job name, matrix values, runner hints, service containers, key commands, and referenced env keys.
4. PipeTwin writes `pipetwin.repro.yml` with safe placeholders.
5. User runs `pipetwin run` to execute the closest local reproduction.
6. PipeTwin prints an `exact`, `approximated`, and `missing` report.
7. User shares the generated Markdown repro note in a PR or issue.

## Feature list

### v0.1.0-alpha.1

- CLI skeleton with `capture`, `run`, and `explain` commands.
- Pasted-log input mode for GitHub Actions logs.
- YAML output schema for repro bundles.
- Secret-safe env key detection.
- Example Node/Postgres CI failure fixture.

### v0.1.0-alpha.2

- Public GitHub Actions run URL support when metadata is accessible without credentials.
- Service-container mapping to Docker Compose.
- Matrix value extraction.
- Markdown report output.

### v0.2.0-alpha.1

- GitLab CI pasted-log support.
- Pluggable adapters for PikoCI/Concourse-style job descriptions.
- Better runner-image approximation warnings.

## Data model

```yaml
version: 1
source:
  kind: github_actions_log
  url: null
  captured_at: 2026-06-27T00:00:00Z
repo:
  remote: null
  commit: null
workflow:
  name: null
  job: null
  matrix: {}
runner:
  os: null
  image_hint: null
services:
  - name: postgres
    image: postgres:16
    env_keys: []
env:
  required_keys: []
  provided_keys: []
commands: []
repro:
  exact: []
  approximated: []
  missing: []
```

## Technical approach

- Implement as a small CLI, likely Python or Go after the first spike.
- Start with fixture-driven parsing instead of trying to call private CI APIs.
- Use Docker Compose output for service containers.
- Keep the generated bundle explicit and inspectable.
- Never ingest or persist secret values; only list required keys.

## Validation plan

- Test against at least three public GitHub Actions failure logs or sanitized fixtures.
- Compare against `act`: PipeTwin should either invoke/complement `act` or explain why the generated repro differs.
- Ask maintainers whether the Markdown repro report would be useful in PR reviews.
- Kill or narrow the project if `act` plus a short README already solves the selected fixture class.

## Milestones

- v0.1.0-alpha.0 — repo scaffold.
- v0.1.0-alpha.1 — pasted-log MVP with Node/Postgres fixture.
- v0.1.0-alpha.2 — public GitHub Actions run URL capture.
- v0.2.0-alpha.1 — multi-CI adapter spike.
