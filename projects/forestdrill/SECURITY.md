# Security Policy

ForestDrill is a planning and reporting tool. It must stay read-only in v0.

## Supported versions

| Version | Supported |
|---|---|
| 0.1.0-alpha.0 | Scaffold/spec only |

## Reporting a vulnerability

Open a GitHub issue or contact the maintainer through the repository profile. Do not include secrets, real tenant IDs, real domains, hostnames, IP addresses, usernames, screenshots, backup job IDs, or private recovery runbooks in public reports.

## Data safety rules

ForestDrill fixtures and examples must use synthetic data only. The project must not read credentials, connect to production AD/Azure/backup systems, perform backups, perform restores, or change recovery configuration in v0.
