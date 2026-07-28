# Security Policy

## Supported versions

This project is pre-release. Security fixes target the latest main branch until a stable release exists.

## Reporting a vulnerability

Open a GitHub security advisory or contact the maintainer privately if the issue includes sensitive details.

## Sensitive data rules

- Do not commit real Uptime Kuma push URLs.
- Do not commit hostnames, private IPs, customer names, screenshots, or service inventories from real environments.
- Use placeholders and synthetic fixtures for examples.
- Packet output must redact push URLs by default.

## Scope

WinSvcBeacon is a monitoring bridge, not a credential manager or remote remediation tool. v0 should not auto-restart services, store Kuma credentials, or make unprompted changes to Windows hosts.
