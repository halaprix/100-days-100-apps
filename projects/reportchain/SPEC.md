# SPEC — ReportChain

## User story

As a Microsoft 365 admin, I want to preview manager-based distribution-list membership and generate safe command packets before changing the tenant, so that direct-report email groups do not drift or accidentally include the wrong people.

## Core flow

1. Admin supplies a manager UPN and either a CSV export or read-only Graph data.
2. ReportChain resolves direct reports and, optionally, the full reporting tree.
3. ReportChain flags data risks: missing managers, cycles, disabled accounts, guest accounts, stale static members, and users outside scope.
4. ReportChain emits a Markdown and JSON packet with membership preview, native-option guidance, and copy/pasteable PowerShell commands.
5. Admin reviews the packet and runs tenant-changing commands manually outside ReportChain.

## Data model

```text
User
- id
- userPrincipalName
- displayName
- mail
- managerId | managerUpn
- accountEnabled
- userType
- department

ReportTree
- rootManager
- directReports[]
- recursiveReports[]
- excluded[]
- warnings[]

CommandPacket
- previewCommands[]
- createCommands[]
- updateCommands[]
- rollbackNotes[]
- assumptions[]
```

## Technical approach

Start as a Python CLI:

- `argparse` or `typer` command surface.
- CSV-first input for local demos and privacy-safe tests.
- Optional Microsoft Graph reader later, requiring only read scopes and never storing credentials.
- Pure functions for graph traversal and packet generation.
- Markdown and JSON output formats.

The CLI should explain platform constraints rather than hiding them. For example, direct reports can be read from Graph, but a full reporting tree requires recursive traversal or a maintained nested-group strategy.

## Validation plan

- Unit-test direct reports, recursive tree traversal, cycle detection, disabled-user exclusions, guest handling, and stale-member diffs using synthetic fixture data.
- Snapshot-test generated Markdown and PowerShell command packets.
- Compare generated packet guidance against Microsoft Graph, Microsoft Entra dynamic group, and Exchange Online recipient-filter docs.
- Validate the wedge by posting a read-only walkthrough in sysadmin/M365 communities and measuring whether admins ask for the fixture/demo or share their own edge cases.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and specification.
- v0.1.0-alpha.1 — CSV fixture parser, report-tree engine, and Markdown preview.
- v0.2.0-alpha.1 — command-packet generator and stale-list diff.
- v0.3.0-alpha.1 — optional read-only Graph fetcher behind explicit flags.
