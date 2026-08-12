# SPEC — EolBridge

## User story

As a small-agency Drupal developer or SME sysadmin, I want to turn safe Drupal 10 dependency and module facts into an EOL decision packet, so that non-technical stakeholders can approve an upgrade plan before support ends.

## Core flow

1. User runs `eolbridge packet --composer-lock composer.lock --site-profile site.yml --out packet.md` against sanitized local files.
2. EolBridge parses Composer and profile data without reading production secrets.
3. It classifies core version, PHP/platform constraints, pinned packages, abandoned packages where visible, and manual-entry business context.
4. It renders a deterministic packet with current state, blockers, risk language, staged upgrade plan, owner questions, and next actions.
5. User attaches the packet to a budget request, client email, or internal change-planning ticket.

## Inputs

- `composer.json` and `composer.lock` copied from a Drupal project.
- Optional `site-profile.yml` with safe manual fields:
  - site name label
  - business criticality
  - public/private site class
  - approximate traffic/revenue class
  - owner/team
  - known custom modules/themes
  - desired upgrade window

## Data model

```text
SiteProfile
  label: string
  business_criticality: low | medium | high | critical
  site_class: public | internal | mixed
  owner: string
  desired_upgrade_window: string | null
  custom_components: list[string]

PackageFact
  name: string
  version: string
  type: string | null
  source: composer_lock | composer_json | site_profile
  flags: list[string]

Packet
  generated_at: ISO-8601 date
  deadline: date
  summary: list[string]
  blockers: list[Blocker]
  staged_plan: list[Stage]
  owner_questions: list[string]
```

## Technical approach

- Build a small Python CLI first; keep dependencies minimal.
- Use deterministic rendering so packet output is diffable in CI.
- Maintain redaction rules for values that look like URLs with credentials, tokens, private keys, `.env` contents, or database DSNs.
- Ship fixtures under `fixtures/drupal10/` and expected output under `tests/golden/` once implementation begins.

## Validation plan

- Golden-file test for a sample Drupal 10 Composer lockfile and site profile.
- Public-safety test that secret-looking fixture values are rejected or redacted.
- Demo test that the generated packet includes deadline, blockers, owner questions, and staged plan.
- Wedge validation: ask 3 Drupal agency/dev users whether the packet saves at least 30 minutes compared with rewriting Upgrade Status/Composer output into client-facing language.

## Milestones

- v0.1.0-alpha.0 — repo scaffold/spec snapshot.
- v0.1.0-alpha.1 — CLI parses fixtures and renders deterministic markdown packet.
- v0.2.0-alpha.1 — HTML export, richer blocker taxonomy, and redaction tests.
