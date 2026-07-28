# PipeTwin

A CLI that turns failed CI runs or pasted job logs into local repro bundles with runner hints, service stubs, missing-env reports, and a shareable command.

## Problem

Small teams and solo maintainers still debug CI failures by pushing speculative fixes, waiting for hosted runners, reading logs, and trying to recreate the runner environment by hand. Local-CI tools exist, but the developer often still has to know which job, matrix values, services, env keys, and runner assumptions mattered.

PipeTwin starts from the failure artifact instead: a failed run URL or log file.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/webdev | https://www.reddit.com/r/webdev/comments/1ugug1z/pikoci_selfhosted_cicd_that_runs_as_a_single/ | Fresh self-hosted CI project foregrounds one-binary setup and local job execution. |
| PikoCI | https://pikoci.com/ | Positions local execution as “no server, no push, no waiting.” |
| nektos/act | https://github.com/nektos/act | Large GitHub Actions local-runner project validates the pain of testing workflows without push/wait loops. |
| Dagger | https://dagger.io/ | Local-first repeatable pipeline execution is a major platform promise. |
| Concourse CI | https://concourse-ci.org/ | `fly execute` validates the local pipeline debugging workflow. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | nektos/act | Strong GitHub Actions local runner. PipeTwin should complement it by generating a repro bundle from a failed run/log. |
| Direct competitor | Dagger | Powerful local-first CI/runtime, but requires adopting Dagger modules. |
| Direct competitor | PikoCI / Concourse | Local execution works inside their pipeline models. PipeTwin targets teams keeping existing CI. |
| Indirect substitute | Docker Compose, Makefile, Taskfile, Dev Containers | Useful building blocks, but manual mapping from hosted failure to local run. |
| Status quo | Push, wait, read logs, guess, repeat | Cheap once, expensive when failures recur or block releases. |

## Wedge

PipeTwin is not another CI platform. It is a failure-to-repro adapter: capture the hosted failure, produce the closest local command, and state exactly what could not be reproduced safely.

## Target user

- Open-source maintainers debugging PR failures.
- Small SaaS teams blocked by GitHub Actions/GitLab CI jobs.
- Self-hosted CI users who want local repro before pushing.
- Contributors who need a maintainer-shareable way to reproduce CI-only failures.

## MVP

- `pipetwin capture <failed-run-url-or-log-file>` for pasted/public GitHub Actions logs.
- Extract job name, commit SHA, matrix values, service container hints, runner image hints, and missing env keys.
- Generate `pipetwin.repro.yml` and a local run command.
- Secret-safe placeholders: never store secret values.
- `pipetwin explain` report showing exact vs approximated runner state.
- Markdown output for PR comments/issues.

## Non-goals

- Full CI replacement.
- Perfect hosted-runner emulation.
- Secret synchronization.
- Private API dependence for the first proof.
- Support for every CI dialect in v0.1.

## Status

v0.1.0-alpha.0 — scaffold/spec only. Remote publication is pending GitHub write access.
