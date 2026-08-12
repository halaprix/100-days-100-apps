# EolBridge

EolBridge turns Drupal 10 version, module, Composer, and platform-readiness facts into an executive upgrade/budget packet before the December 2026 support cliff.

## Problem

Drupal 10 EOL is a predictable deadline, but many small organizations delay because the site still works and the upgrade looks like a vague dev-agency expense. Developers can run readiness tools, but budget holders need a short packet that explains current state, blockers, risk, and staged next steps in approval language.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vm4kqc/how_are_you_handling_drupal_10_eol_in_december/ | Fresh sysadmin post reports Drupal 10 EOL planning confusion and budget-approval friction. |
| Drupal.org core schedule | https://www.drupal.org/about/core/policies/core-release-cycles/schedule | Official schedule page surfaced by web search says Drupal 10 reaches end of life on December 9, 2026. |
| Drupal Upgrade Status | https://www.drupal.org/project/upgrade_status | Existing readiness module validates developer-side upgrade checks. |
| Drupal Rector | https://www.drupal.org/project/rector | Existing automation helps update deprecated code, but does not produce a stakeholder decision packet. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Drupal Upgrade Status | Developer readiness scanner for environment and project compatibility; not a budget-holder packet. |
| Direct competitor | Drupal Rector | Automates code upgrades; not a deadline/risk/approval artifact. |
| Direct competitor | Drupal agencies / upgrade audits | Complete but often requires budget before discovery; EolBridge should help create the pre-budget case. |
| Indirect substitute | Composer audit/outdated, drush status, spreadsheets | Cheap and flexible, but leaves translation into risk and timeline to the technical owner. |
| Status quo | Wait until the site breaks or a vulnerability forces action | Defers cost until security support and upgrade lead time are both worse. |

## Wedge

EolBridge stays below full agency discovery and above raw developer scanner output: safe dependency/module facts in, budget-ready EOL decision packet out.

## Target user

Small-agency Drupal developers, nonprofit/SME sysadmins, and fractional IT owners responsible for one or more Drupal 10 sites where upgrade work needs non-technical approval.

## MVP

- Parse a public-safe `composer.json`, `composer.lock`, and optional sanitized site profile YAML.
- Detect Drupal core version, PHP/platform constraints, pinned packages, abandoned packages where Composer metadata exposes them, and obvious next-major blockers.
- Generate a deterministic markdown/HTML packet with deadline, current-state summary, blocker table, owner questions, risk copy, and staged upgrade plan.
- Refuse secrets and environment-looking values.

## Non-goals

- No production Drupal, database, or admin-panel access in the first slice.
- No automated code fixes; Rector owns that lane.
- No paid agency-estimate marketplace.
- No legal/security warranty.

## Status

v0.1.0-alpha.0 — scaffold/spec only, consolidated in the 100-days master repo.
