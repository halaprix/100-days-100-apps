# PushBench Specification

## User story

As a self-hosted UnifiedPush operator, I want to run the same safe local benchmark profile against candidate push backends so I can choose ntfy, Autopush/Sunup, or another option with evidence instead of anecdotes.

## Feature list

1. Parse a YAML load profile with:
   - concurrent devices,
   - reconnects per minute,
   - publishes per minute,
   - payload-size buckets,
   - target p95 latency,
   - allowed error/429 rate,
   - rough monthly VPS budget.
2. Validate that benchmark targets are local or explicitly allowlisted fixture hosts.
3. Run backend adapters:
   - `ntfy-http` publish/subscribe path,
   - `ntfy-websocket` connection/reconnect path,
   - `autopush` WebSocket + HTTP push-path stub for local fixture mode.
4. Capture latency, success/error counts, reconnect failures, and rough resource observations.
5. Render markdown and JSON readiness packets with recommendation, caveats, and next test.

## Data model

```text
Profile
  name
  devices
  reconnects_per_minute
  publishes_per_minute
  payload_bytes
  target_p95_ms
  max_error_rate
  monthly_budget_usd

BackendResult
  backend
  scenario
  attempted
  succeeded
  failed
  p50_ms
  p95_ms
  error_rate
  observed_notes

Packet
  profile
  backend_results[]
  recommendation
  caveats[]
```

## Build plan

1. Implement profile parser and target safety guard.
2. Add a fake local backend fixture for deterministic CI.
3. Add ntfy adapter against local fixture-compatible endpoints.
4. Add Autopush adapter stub with WebSocket scenario shape.
5. Render markdown/JSON packet and golden test output.

## Validation plan

- Unit-test profile parsing and unsafe target rejection.
- Golden-test sample markdown packet from fixtures.
- Verify no public network target is used in CI.
- Run `python3 scripts/verify_scaffold.py` for scaffold invariants.
