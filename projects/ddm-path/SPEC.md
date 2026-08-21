# DDMPath SPEC

## User story

As an Intune administrator managing organization-owned Apple devices, I want to turn static policy and device exports into a DDM migration packet, so that I can pilot the change without losing update control or manually reconciling policies, OS cohorts, and assignments in a spreadsheet.

## Feature list

### MVP

1. Import static JSON/CSV exports for Apple update policies, groups, assignments, and device inventory.
2. Normalize policy type, platform, OS version, supervision, assignment scope, schedule, and update action.
3. Detect legacy MDM policies, DDM-ready candidates, mixed/overlapping assignments, unsupported cohorts, and missing evidence.
4. Produce a deterministic Markdown packet: executive summary, cohort table, conflict list, pilot order, validation checks, and rollback guidance.
5. Ship only synthetic fixtures and a public-safety verifier.

### Later

- Read-only Graph adapter after static import proves useful.
- Policy-diff history between exports.
- Configurable organization change windows and communications templates.
- Explicit mapping from export columns to Intune report schemas.

## Data model

```json
{
  "policy": {
    "label": "ios-pilot-update",
    "platform": "ios",
    "management_mode": "legacy_mdm",
    "assignment": "pilot-group",
    "schedule": "overnight",
    "update_action": "install-later"
  },
  "device": {
    "label": "tablet-pilot-a",
    "platform": "ios",
    "os_major": 17,
    "supervised": true,
    "group": "pilot-group"
  }
}
```

## Build plan

1. Define small generic export schemas and synthetic fixtures.
2. Implement parsers and normalization rules.
3. Add DDM eligibility and assignment-overlap checks.
4. Render a Markdown packet and fixture-driven demo.
5. Add golden-file tests and a public-safety scan.

## Validation plan

- Unit-test each finding against synthetic records.
- Run a fixture demo that produces a migration packet with one legacy policy, one DDM candidate, and one ineligible cohort.
- Confirm the tool never opens network connections or mutates Intune.
- Interview or observe at least three Intune Apple administrators before adding a Graph adapter; reject if the portal export plus spreadsheet takes under 30 minutes per migration review.
