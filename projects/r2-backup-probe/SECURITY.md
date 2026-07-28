# Security Policy

## Supported versions

This project is pre-release. Security reports for `main` are welcome.

## Reporting a vulnerability

Open a GitHub security advisory when available, or contact the maintainer through the repository owner profile.

## Sensitive data policy

R2 Backup Probe is meant to inspect backup configuration and logs, which may contain secrets or operational details. The project should:

- never store credentials,
- redact secrets, account IDs, bucket names, local paths, usernames, and hostnames in generated reports by default,
- avoid telemetry and hosted collection,
- keep optional live probes explicit and minimal.

Do not attach raw production backup logs to public issues.
