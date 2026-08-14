# Security Policy

## Supported versions

PushBench is pre-release. Only the latest scaffold snapshot is maintained.

## Reporting a vulnerability

Open a GitHub issue in the master `halaprix/100-days-100-apps` repo if the issue is public-safe. If details include secrets, private infrastructure, real push tokens, or user data, do not post them publicly.

## Security boundaries

- The MVP must not load-test public push services.
- The MVP must not collect real push subscription tokens or notification payloads.
- Fixtures must stay synthetic and local-only.
