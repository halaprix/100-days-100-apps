# Security policy

## Reporting a vulnerability

Do not open a public issue for a suspected vulnerability. Contact the maintainer
privately through the security contact configured for the repository.

## Product security boundaries

AssistCutover is designed to inspect local source files only. It must not:

- read environment files or credential stores;
- transmit source code or findings;
- execute scanned code; or
- print source snippets, access tokens, or environment values in reports.
