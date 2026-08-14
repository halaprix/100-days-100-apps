# PushBench Readiness Packet

Profile: tiny-local-unifiedpush

## Summary

| Backend | Result | p95 latency | Error rate | Notes |
|---|---|---:|---:|---|
| ntfy-http | pending fixture run | n/a | n/a | Scenario shape defined. |
| ntfy-websocket | pending fixture run | n/a | n/a | Reconnect storm test required. |
| autopush-fixture | pending fixture run | n/a | n/a | WebSocket + HTTP push path stubbed. |

## Recommendation

Run the tiny local profile first. Do not benchmark public/default push servers.
