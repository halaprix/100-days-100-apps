# DDMPath

DDMPath turns exported Intune Apple-update policies and device reports into a local migration packet that flags legacy MDM overlap, ineligible cohorts, and a safe Declarative Device Management (DDM) pilot order.

## Problem

Microsoft says Apple deprecated MDM-based software-update workloads and Intune will end support for its MDM-based Apple update policies. An Intune admin must separate legacy policies from DDM policies, account for supervised-device and OS prerequisites, avoid conflicting assignments, choose pilot cohorts, and explain planned disruption. Intune can configure policies and show reports, but it does not turn exported policy and device evidence into a migration review packet.

## Target user

Small IT teams and managed-service providers that manage supervised Apple fleets with Microsoft Intune and need a reviewable plan before moving update controls to DDM.

## MVP

- Local CLI that ingests sanitized Intune policy and device-report CSV/JSON exports.
- Detect legacy MDM update policies, DDM candidates, overlapping assignments, unsupported OS cohorts, and missing update prerequisites.
- Produce a Markdown/HTML migration packet with a cohort map, pilot sequence, blockers, test cases, and rollback notes.
- Use synthetic fixtures and deterministic checks; no live Graph connection or policy mutation.

## Non-goals

- No Intune authentication, API credential handling, or tenant changes.
- No automatic policy conversion or device remediation.
- No full MDM, endpoint management, or update-dashboard replacement.
- No claim that an export completely represents a tenant.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Microsoft Intune | https://learn.microsoft.com/en-us/intune/device-updates/apple/deprecated-mdm-policies-ios | Apple deprecated MDM update workloads; Intune recommends DDM. |
| Microsoft Intune | https://learn.microsoft.com/en-us/intune/device-updates/apple/planning-guide-ios-ipados | DDM is recommended for supervised iOS/iPadOS 17+; update strategy affects security and user disruption. |
| Microsoft Intune | https://learn.microsoft.com/en-us/intune/device-updates/apple/planning-guide-macos | DDM is recommended for macOS 14+; older cohorts follow a different path. |

## Current status

v0.1.0-alpha.0 — scaffold/spec only; public-safe snapshot in the 100-days master index.
