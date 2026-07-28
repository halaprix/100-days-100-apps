# Security Policy

## Supported versions

MxCutover is pre-1.0. Only the latest `main` branch is supported.

## Reporting a vulnerability

Open a GitHub security advisory or contact the maintainer privately through GitHub.
Do not paste secrets, tenant exports, customer domains, or private mail logs into public issues.

## Scope

In scope:

- Bugs that could expose local packet inputs.
- Unsafe examples that encourage secret or tenant-data disclosure.
- Incorrect public-safety checks in fixtures or docs.

Out of scope for now:

- Production DNS, Microsoft 365, Proofpoint, or Mimecast automation, because v0 is read-only packet generation.
