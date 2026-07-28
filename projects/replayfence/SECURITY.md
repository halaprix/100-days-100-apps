# Security Policy

## Reporting

Please report security issues privately through GitHub security advisories once enabled for the repository. Do not open public issues containing exploit details or real webhook payloads.

## Public-safety rules

Never commit:

- real webhook signing secrets,
- OAuth tokens, cookies, API keys, or bearer tokens,
- private endpoint URLs or hostnames,
- customer payloads or personal data,
- account IDs that identify a private tenant or workspace.

Use synthetic fixtures and reserved domains for examples.

## MVP security posture

ReplayFence should be local-first. It should not store production events in a hosted service, and it should not require provider credentials for its first useful version.
