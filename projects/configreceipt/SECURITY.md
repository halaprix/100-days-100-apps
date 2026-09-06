# Security policy

## Supported versions

Only the current development branch is supported.

## Reporting a vulnerability

Do not file public issues containing real configuration exports, credentials,
or environment details. Use the repository's private security-reporting channel
when one is configured, or contact the maintainer through the account profile
with a minimal reproduction using synthetic data.

## Security boundary

ConfigReceipt is intended to operate offline on files explicitly selected by a
user. It must not open network connections, connect to appliances, retain
credentials, or automatically restore configuration. Redacted output requires
human review and is never guaranteed secret-free.
