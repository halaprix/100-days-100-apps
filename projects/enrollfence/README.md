# EnrollFence

> Local, read-only policy linting for the gap between "corporate Windows only"
and what an Intune enrollment configuration can actually permit.

## Status

Research scaffold. No production parser has been implemented.

## Problem

An Intune administrator can combine enrollment restrictions, filters, Autopilot,
user scopes, and Windows enrollment paths to express a corporate-device policy.
Those settings live in separate configuration surfaces. Native reports explain a
device's enrollment after the fact, but do not answer a prospective question:
which known enrollment paths remain permitted by the proposed policy?

The manual alternative is documentation review, tenant screenshots, and a small
set of test devices. That is slow to repeat after a policy change and can miss a
path such as Settings or Company Portal enrollment. The cost is a policy that
looks strict but does not implement the organization's intended boundary.

## Target user

A small-team Microsoft Intune administrator responsible for Windows Autopilot
and enrollment restrictions, who must demonstrate that only approved corporate
devices can enter endpoint management.

## MVP

- Read a sanitized local JSON/YAML export of selected enrollment restrictions,
  filters, assignments, and Autopilot registrations.
- Evaluate a fixed, documented matrix of Windows enrollment paths and device
  facts against the supplied policy model.
- Emit a Markdown and JSON decision packet that labels each path as allowed,
  blocked, unknown, or outside the tool's evidence.
- Flag unsupported filter properties, contradictory priority/assignment rules,
  missing ownership evidence, and untestable intent claims.
- Stay local and read-only. No Graph API calls, tenant authentication, policy
  writes, device actions, or claims that a policy is secure.

## Non-goals

- Replacing Intune, Autopilot, endpoint-management suites, or their reports.
- Deploying, enrolling, blocking, wiping, or otherwise changing a device.
- Collecting serial numbers, user names, tenant data, or other live inventory.
- Guaranteeing that a tenant cannot be bypassed; the report is review evidence,
  not a security certification.

## Evidence

- [Fresh r/sysadmin question on Entra Join and Intune enrollment restrictions](https://www.reddit.com/r/sysadmin/comments/1w33qcy/entrajoin_and_intuneenroll_restrictions/)
- [Microsoft: Windows device enrollment guide](https://learn.microsoft.com/en-us/intune/device-enrollment/windows/guide)
- [Microsoft: View enrollment reports](https://learn.microsoft.com/en-us/intune/device-enrollment/monitor-reports)
- [Microsoft: enrollment restrictions](https://learn.microsoft.com/en-us/intune/device-enrollment/restrictions)

## Development

This repository intentionally contains only scaffold documentation and a
scaffold verifier. Run:

```bash
python3 scripts/verify_scaffold.py
git diff --check
```

## License

Apache-2.0. See [LICENSE](LICENSE).
