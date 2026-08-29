# Security policy

## Scope

SwapCheck is designed to process local policy exports and repository metadata.
Those inputs can be sensitive. The default implementation must not upload them,
make network requests, or emit source content in reports.

## Reporting a vulnerability

Do not include secrets, policy exports, or private repository files in a public
issue. Use GitHub's private vulnerability reporting feature when this repository
is published, or contact the maintainer through the repository's security
advisory channel.

## Supported versions

Until the first stable release, only the latest `main` revision is supported.
