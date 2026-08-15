# DrivePing SPEC

## User story

As an Android head-unit owner debugging intermittent hotspot or Wi-Fi failures, I want a glanceable connectivity sentinel and exportable drop log, so I can tell whether failures are local Wi-Fi, DNS, Internet reachability, or the media/navigation app itself.

## Feature list

### MVP

1. Foreground connectivity service
   - Configurable probe interval.
   - Probe targets: gateway, DNS resolver, HTTPS endpoint.
   - State machine: unknown, healthy, degraded, offline.
2. Persistent display
   - Notification text: target, latency, loss, last drop.
   - Optional large overlay mode with conservative permission prompts.
3. Drive-session log
   - Append local events for state transitions and probe summaries.
   - Export JSON, CSV, and Markdown packet.
4. Setup checklist
   - Explain foreground-service notification, boot receiver limitations, and OEM battery settings.
   - Explicitly tell users when Android version or device policy blocks auto-start.

### Later

- Per-route/session labels.
- Local-only comparison view before/after router, hotspot, or antenna changes.
- Head-unit preset layouts for common screen densities.

## Data model

```json
{
  "session_id": "sample-drive-session",
  "started_at": "2026-08-15T07:00:00Z",
  "device_profile": "aftermarket-head-unit",
  "probes": [
    {
      "timestamp": "2026-08-15T07:00:05Z",
      "target": "https-endpoint",
      "state": "healthy",
      "latency_ms": 42,
      "loss_percent": 0,
      "dns_ok": true
    }
  ]
}
```

## Build plan

1. Create a Kotlin/Android foreground-service spike with one fake probe adapter and one HTTPS probe.
2. Render persistent notification state every interval.
3. Write local session events to app-private storage.
4. Add JSON export and a Markdown summary renderer.
5. Add overlay mode only after notification mode works reliably.

## Validation plan

- Unit-test state transitions from synthetic probe results.
- Unit-test JSON and Markdown export against golden fixtures.
- Emulator/manual spike: simulate failed DNS, failed HTTPS, and high latency.
- Verify app does not request location, contacts, SMS, microphone, camera, VPN, or packet-capture permissions in MVP.
