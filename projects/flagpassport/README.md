# FlagPassport

A local, read-only exposure report for Forge feature-flag client code before
anonymous evaluation stops working on December 1, 2026.

## Problem

Atlassian will stop evaluating Forge Feature Flags Client SDK values for an
unauthenticated user on December 1, 2026. A `FeatureFlags.initialize()` call
without an `accountId` will fall back to defaults. That can silently hide or
expose the wrong UI path in an app that permits logged-out access.

The vendor documentation explains the behavior, but a Marketplace partner still
has to locate client-SDK calls, determine whether the affected module can serve
an unauthenticated visitor, map each default value to its UI consequence, and
leave a reviewable test record. That is easy to miss across a multi-app estate
and can block a sale, support path, or onboarding route.

## Target user

A Jira or Confluence Marketplace partner whose Forge apps use `FeatureFlags`
from `@forge/bridge`, especially where a module may set `unlicensedAccess` or
otherwise render before an Atlassian account is available.

## MVP

- Read explicit user-supplied Forge source and manifest paths; never discover
  accounts, scan a whole machine, or call Atlassian APIs.
- Detect client-side `FeatureFlags` imports, construction, initialization, and
  flag checks.
- Correlate candidate calls with manifest module access settings and mark
  ambiguous cases as `manual-review`, never safe.
- Emit Markdown and JSON exposure packets with default values, source labels,
  relevant module settings, and an authenticated/unauthenticated test matrix.
- Redact file contents and never copy credentials, IDs, or other source values
  into output.

## Non-goals

- Not a generic Forge security scanner or a replacement for vendor documentation.
- Not an automatic code fixer, deployment tool, or test runner.
- Not a remote Marketplace inventory, authentication helper, or feature-flag
  service.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Atlassian developer changelog | https://developer.atlassian.com/changelog/ | Atlassian announced that anonymous evaluations through `FeatureFlags` in `@forge/bridge` stop on December 1, 2026; affected calls fall back to default values. |
| Atlassian SDK guidance | https://developer.atlassian.com/platform/forge/feature-flags/client-vs-server-sdk/ | The client SDK runs in Forge UI and takes the current user at initialization, while server-side evaluation is a distinct path. |
| Atlassian developer community | https://community.developer.atlassian.com/t/forge-feature-flag-docs-incorrect/100007 | A Marketplace partner reported a client/server feature-flag documentation mismatch that Atlassian corrected, supporting a conservative, evidence-producing review workflow. |
| FSRT | https://github.com/atlassian-labs/FSRT | Atlassian Labs maintains a Forge static analyzer for common vulnerabilities; it is a strong adjacent substitute but does not publish this dated anonymous-client-SDK migration check. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Atlassian feature-flags documentation and migration notice | Authoritative for the change and implementation choices, but it does not inventory an app's client calls, manifest exposure, defaults, and manual tests. |
| Direct competitor | FSRT | A Forge static analyzer for common vulnerabilities. It scans a project, but its public scope is security requirements rather than this December 2026 client-SDK behavior change. |
| Indirect substitute | Semgrep/custom AST rule, grep, manifest review, and spreadsheet | Can find an import, but maintaining project-specific correlation and a reviewer-friendly test packet is manual work. |
| Status quo | Wait for a logged-out route to receive flag defaults after the deadline, then investigate the code path | A fallback can silently alter UI behavior on a public, unlicensed, or onboarding flow. |

## Wedge

FlagPassport is not a generic static-analysis wrapper. It makes one vendor
change reviewable: client `FeatureFlags` use plus possibly unauthenticated
module exposure plus the behavior of each default. The first-user channel is
concrete: changelog/search traffic for the December deadline, Forge developer
community discussions, and Marketplace-partner migration content.

## Status

`v0.1.0-alpha.0` — local scaffold and specification only. No remote configured.
