# Security Policy

## Reporting a vulnerability

Open a GitHub security advisory or a private issue with a minimal reproduction. Do not include real campaign submissions, client names, phone numbers, addresses, or customer data.

## Data handling

CampaignPacket must be safe for small businesses to run locally:

- no network calls unless explicitly requested in a future version,
- no credential persistence,
- no telemetry,
- no storage of real campaign submissions in the MVP,
- no unredacted phone numbers, addresses, client names, or private business details in shareable output,
- no automatic Teams Admin Center changes.

If a diagnostic needs sensitive values, use synthetic fixtures or redacted examples.
