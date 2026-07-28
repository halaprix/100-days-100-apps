# Security Policy

## Supported versions

HeaderPass is pre-release. Security reports are welcome for the default branch.

## Reporting a vulnerability

Open a GitHub security advisory or contact the maintainer privately through GitHub. Do not include real Cloudflare tokens, cookies, hostnames, private URLs, screenshots with personal data, or infrastructure details in public issues.

## Scope

Important areas:

- Redaction of headers, cookies, tokens, and account identifiers.
- Avoiding accidental persistence of secrets in logs or runbooks.
- Preventing the CLI from becoming a credential relay or bypass tool.
- Safe handling of user-supplied config files.

## Design stance

The MVP is read-only and local-first. It should diagnose access paths and produce redacted runbooks, not mutate Cloudflare, Tailscale, DNS, or reverse-proxy configuration automatically.
