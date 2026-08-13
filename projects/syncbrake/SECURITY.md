# Security Policy

## Supported versions

SyncBrake is in alpha. Only the latest scaffold snapshot is maintained.

## Reporting a vulnerability

Open a public issue only for problems that do not disclose sensitive identity data. If a report requires real tenant details, redact it before sharing.

## Data handling

The MVP must be local-first and must not connect to Microsoft Graph, tenants, Entra Connect servers, domain controllers, or production exports. Fixtures must be synthetic. The tool should redact tenant names, UPN domains, hostnames, private paths, and support-case details in generated packets.
