# Security Policy

## Supported versions

PasskeyPilot is pre-release. Only the latest `main` branch scaffold is in scope.

## Reporting a vulnerability

Open a GitHub issue when a public repository exists, or contact the maintainer through the public 100 Days, 100 Apps index.

Do not include secrets, real tenant IDs, domains, user principal names, device IDs, private customer data, or screenshots containing personal data in reports.

## Security boundary

PasskeyPilot v0 is read-only and fixture-driven. It must not connect to Microsoft Graph, inspect local credential files, change Entra policy, or exfiltrate tenant data.
