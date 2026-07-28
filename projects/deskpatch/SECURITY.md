# Security Policy

DeskPatch is a privilege-boundary project. Treat every change as security-sensitive until proven otherwise.

## Supported versions

| Version | Supported |
|---|---|
| 0.1.0-alpha.x | Experimental only |

## Reporting a vulnerability

Open a private security advisory on GitHub once the remote repository exists. Until then, do not publish exploit details in public issues.

## Non-negotiable constraints

- No stored admin passwords.
- No arbitrary command execution.
- No unsigned update manifests.
- No installer execution without SHA-256 verification.
- No remote code/config execution from untrusted sources.

## Current status

Scaffold/spec only. Do not deploy on real endpoints.
