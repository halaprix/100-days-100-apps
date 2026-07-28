# Security Policy

## Supported versions

FreeTierFit is in alpha. Security fixes target the latest `main` branch until the first stable release.

## Reporting a vulnerability

Open a private security advisory on GitHub if available, or contact the maintainer through the repository owner profile.

## Scope

Security-sensitive areas include:

- accidental logging of private hostnames, private Compose paths, or private infrastructure details,
- future handling of provider profiles,
- report output that may include private image names, ports, or volumes.

The MVP must stay local-only and must not require cloud credentials, SSH access, cookies, provider API keys, or tokens.
