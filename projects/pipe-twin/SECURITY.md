# Security Policy

PipeTwin handles CI logs and environment-key names. Treat those as potentially sensitive.

## Supported versions

Pre-release only. Security fixes apply to the latest alpha branch.

## Reporting a vulnerability

Open a private security advisory on GitHub once the remote repository is available. Until then, do not put private CI logs or secrets in public issues.

## Secret handling policy

- PipeTwin must never store secret values.
- Fixtures must be synthetic, public, or sanitized.
- Reports may list missing env key names, but not values.
- Debug logs must redact obvious token-like values.
