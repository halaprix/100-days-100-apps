# Security Policy

## Supported versions

ReportChain is pre-release. Security fixes target `main` until the first stable release.

## Reporting a vulnerability

Open a private security advisory on GitHub if available, or contact the maintainer through the repository owner profile.

Do not include real Microsoft 365 tenant exports, access tokens, cookies, private email lists, or screenshots with personal data in public issues.

## Security posture

- Read-only and dry-run by default.
- No credential storage in v0.1.
- Tests and fixtures must be synthetic.
- Generated tenant-writing commands must be reviewable before execution and must not run automatically.
