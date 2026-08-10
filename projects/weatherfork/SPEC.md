# SPEC — WeatherFork

## User story

As a Home Assistant user with an Ecowitt weather station, I want one local endpoint that stores each weather upload, forwards it to Home Assistant, and renders comparison views, so that I do not have to choose between automations, durable history, and weather-report UX.

## Core flow

1. User points the Ecowitt console's custom upload target at WeatherFork.
2. WeatherFork validates and normalizes the incoming payload.
3. WeatherFork stores the sample locally before attempting any outbound forwarding.
4. WeatherFork forwards the original or normalized payload to configured sinks such as Home Assistant.
5. User opens a local static report to inspect recent data, missing uploads, and seasonal comparisons.

## Feature list

### v0.1.0-alpha.1 MVP skeleton

- `weatherfork ingest --fixture examples/ecowitt-sample.json` dry-run command.
- Minimal HTTP receiver accepting form-encoded or JSON Ecowitt-like samples.
- Local archive writer using SQLite or JSONL.
- Sink-forwarding interface with timeout and non-blocking failure recording.
- Static report generator from archived samples.

### v0.2.0-alpha.1 usable demo

- Docker Compose example.
- Home Assistant callback sink example.
- Fixture set for current-year and previous-year comparison.
- Gap detection for missed uploads.
- Public-safe demo report artifacts.

## Data model

```text
weather_sample
- id: stable hash of station_id + observed_at + normalized payload
- station_id: configured station or payload-derived source
- observed_at: timestamp supplied by receiver or payload
- received_at: server timestamp
- raw_payload: original key/value payload
- normalized: canonical temperature, humidity, pressure, rainfall, wind, lightning fields where present

forward_attempt
- id
- sample_id
- sink_name
- attempted_at
- status: success | timeout | http_error | skipped
- message: short public-safe diagnostic
```

## Technical approach

- Build as a small Python CLI plus HTTP server first; avoid a full web framework until routing complexity requires it.
- Store locally first, then forward, so Home Assistant downtime does not lose weather data.
- Treat every forwarding destination as best-effort and observable; one bad sink must not block another.
- Render static HTML/JSON output so the demo can be reviewed without operating a server.

## Validation plan

- Use synthetic Ecowitt-style payload fixtures only; do not commit real station identifiers, coordinates, or private hostnames.
- Verify one payload can be stored, forwarded to a local test sink, and rendered into a report.
- Compare setup time against the current substitute path: WeeWX + Home Assistant + Node-RED glue.
- Kill or narrow the idea if WeeWX plus an existing Ecowitt extension already provides a clean relay-to-Home-Assistant path and comparable seasonal views in under 15 minutes.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and product spec.
- v0.1.0-alpha.1 — local dry-run ingest, archive writer, and report generator.
- v0.2.0-alpha.1 — HTTP receiver, forwarding sinks, Docker Compose demo.
