# Security Policy

## Supported versions

This project is pre-1.0. Security fixes will target the latest alpha branch until a stable release exists.

## Reporting a vulnerability

Open a private security advisory on GitHub when available, or contact the maintainer through the public repository without including sensitive details.

## Sensitive data policy

BayTrace must never log or commit:

- Passwords, tokens, cookies, or Authorization headers.
- Private hostnames, internal IP addresses, or private mount paths in shared reports.
- Full disk serial numbers unless the user explicitly disables redaction locally.
- Raw logs from real deployments unless redacted first.

The CLI should default to read-only checks and redacted output.
