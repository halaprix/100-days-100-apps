# Security Policy

## Supported versions

This project is pre-1.0. Security fixes will target the latest alpha branch until a stable release exists.

## Reporting a vulnerability

Open a private security advisory on GitHub when available, or contact the maintainer through the public repository without including sensitive details.

## Sensitive data policy

DavSync Doctor must never log or commit:

- Passwords, app passwords, cookies, OAuth tokens, or Authorization headers.
- Full private server URLs or private hostnames in shared reports.
- Contact names, email addresses, phone numbers, addresses, notes, or calendar contents.
- Raw server logs from real deployments unless redacted first.

The CLI should default to redacted output and require explicit opt-in for any write probe.
