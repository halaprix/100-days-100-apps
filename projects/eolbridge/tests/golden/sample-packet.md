# EolBridge sample packet

Generated from synthetic fixtures.

## Deadline

Drupal 10 reaches end of life on 2026-12-09.

## Current state

- Drupal core package: drupal/core-recommended 10.4.8
- Business criticality: high
- Site class: public

## Blockers

| Severity | Finding | Action |
|---|---|---|
| high | Abandoned package: drupal/legacy_widget | Replace or remove before upgrade planning is treated as low risk. |
| medium | Custom components listed: example_museum_events, example_museum_theme | Run Upgrade Status and Rector review for each custom component. |

## Owner questions

- Who approves the upgrade window?
- Is there a rollback plan and recent backup restore proof?
- Which custom modules/themes are business-critical?

## Staged plan

1. Inventory Composer packages, custom components, PHP/runtime constraints, and hosting constraints.
2. Run developer readiness tooling and classify blockers.
3. Schedule remediation sprint for abandoned packages and custom code.
4. Upgrade staging, test critical user journeys, and prepare rollback.
