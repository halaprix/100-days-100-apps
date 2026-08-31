# Security policy

## Supported versions

This is a research scaffold; no release is supported yet.

## Reporting a vulnerability

Do not publish credentials, tenant data, device identifiers, or exploitation
details in a public issue. Use GitHub's private vulnerability reporting feature
for this repository when available, or contact the maintainer through the
repository's verified contact channel.

## Product boundary

EnrollFence is intended to remain local and read-only. A finding that could
cause it to expose input data, make network calls, mutate tenant policy, or
misrepresent an unknown condition as safe is security-relevant.
