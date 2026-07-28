# Security Policy

## Reporting a vulnerability

Open a GitHub security advisory or a private issue with a minimal reproduction. Do not include real proxy credentials, internal hostnames, or tenant/network details.

## Data handling

ProxyEnv Doctor must be safe to run in sensitive CI environments:

- no network calls unless explicitly requested,
- no credential persistence,
- no telemetry,
- no unredacted proxy URLs in output,
- no automatic configuration writes in the MVP.

If a diagnostic needs a sensitive value, use fixtures or redacted examples.
