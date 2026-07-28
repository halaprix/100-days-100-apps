# Security Policy

## Supported versions

This project is pre-release. Security fixes apply to the latest `main` branch until the first tagged release.

## Reporting a vulnerability

Open a private security advisory on GitHub once the remote repository is active, or contact the maintainer through the owning `halaprix` account.

## Privacy expectations

Llama CUDA Doctor is intended to be read-only, but diagnostic reports can still expose sensitive context. Reports should redact:

- home-directory usernames,
- private hostnames,
- private network addresses,
- shell history,
- tokens or API keys in environment variables.

Do not include raw unsanitized reports in public issues.
