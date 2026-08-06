# Security Policy

## Supported versions

RelayTrace is pre-release. Security fixes target the latest alpha branch only.

## Reporting a vulnerability

Open a GitHub security advisory when a public remote exists, or contact the
maintainer through the parent 100-days index project.

## Public-safety boundary

Do not include real SMTP credentials, domains, email addresses, relay hostnames,
private logs, or message bodies in issues, examples, tests, or pull requests.
Use synthetic `.test` domains and fixture messages only.

RelayTrace should never mutate DNS, mail-server config, MX records, or mailbox
contents. The scaffold MVP is offline and read-only.
