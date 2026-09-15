# Security Policy

## Supported boundary

PlanRetain is scaffold-only. Its intended MVP accepts explicit local exports,
never contacts Project Online or Microsoft 365, and never modifies input data.

## Reporting a vulnerability

Do not open a public issue with exports, tenant data, credentials, or exploit
details. Report a minimal reproduction without sensitive content to the
maintainer through the repository's private contact channel.

## Security invariants

- No network access.
- No execution of supplied files or project code.
- No credential or tenant-ID collection.
- Unknown inputs are reported as `manual-review` or `not-proven`.
