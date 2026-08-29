# SwapCheck

A local, read-only CLI that turns a GitHub Copilot model-policy export into a
reviewable migration packet before a model retirement or policy change affects
an organization.

## Problem

GitHub is retiring several Copilot models on September 1, 2026, while the new
global model policy rolls out through the same date. Enterprise administrators
must determine which selected models disappear, whether their replacement is
allowed by policy, and where behavior-sensitive workflows need an explicit
retest. The platform UI can configure policy, but it does not produce one
portable, reviewable before/after decision record.

## Target user

A GitHub Copilot Business or Enterprise administrator responsible for model
policy and teams that rely on named models in prompts, agent instructions, or
runbooks.

## Evidence

| Source | Link | Signal |
|---|---|---|
| GitHub changelog | https://github.blog/changelog/2026-07-31-upcoming-august-2026-model-deprecations-in-github-copilot/ | GitHub says several models retire September 1, 2026 and administrators may need to enable alternatives through model policy. |
| GitHub changelog | https://github.blog/changelog/2026-08-26-global-model-policy-generally-available/ | Global model policy enforcement rolls out through September 1; inherited policy state can change availability. |
| GitHub documentation | https://docs.github.com/copilot/reference/ai-models/supported-models | Model availability varies by plan and client, and can be limited by policy. |

## Competitor / substitute check

| Type | Name / substitute | Notes |
|---|---|---|
| Direct competitor | GitHub Copilot settings and model-policy UI | Correct place to configure access, but not a local migration manifest, source scan, or review packet. |
| Indirect substitute | GitHub changelog, spreadsheets, and manual repository search | Flexible, but teams must reconcile retirement dates, policy states, client availability, and named-model references by hand. |
| Status quo | Let the deadline or default policy change reveal a missing model | Creates avoidable interruptions or a silent behavior change in agent and review workflows. |

## Wedge

SwapCheck is not a generic LLM evaluation platform or a Copilot policy editor.
It is a credential-free, deterministic change-control packet for one acute job:
map named model references and a user-supplied policy export to a dated
replacement matrix, then generate explicit retest cases before the change.

## MVP

- Parse a local JSON/YAML policy export and a repository directory.
- Inventory named model references in selected text configuration files.
- Apply a versioned migration manifest with retirement dates and alternatives.
- Render Markdown and JSON: affected reference, policy state, replacement,
  client caveat, owner, and required retest.
- Exit nonzero in CI when a retired or policy-disabled model is found.

## Non-goals

- No GitHub API write access, browser automation, or stored credentials.
- No model benchmarking, prompt execution, or generated-code quality claims.
- No automatic policy edits or replacement of model names in source files.

## Status

`v0.1.0-alpha.0` — local scaffold and specification only. The project has no
remote repository yet.
