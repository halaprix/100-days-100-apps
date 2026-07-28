# Security Policy

## Supported versions

SheetSentry is in alpha. Security fixes target the latest `main` branch until the first stable release.

## Reporting a vulnerability

Open a private security advisory on GitHub if available, or contact the maintainer through the repository owner profile.

## Scope

Security-sensitive areas include:

- accidental logging of private endpoint URLs or query strings,
- handling of provider error bodies,
- snapshot files that may contain sensitive sheet data,
- any future support for private sheets.

The MVP must stay public/read-only and must not require OAuth tokens, service-account JSON, cookies, or provider API keys.
