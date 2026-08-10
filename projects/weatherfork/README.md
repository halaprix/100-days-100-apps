# WeatherFork

Fork one Ecowitt weather upload into Home Assistant, long-term storage, and year-over-year comparison charts without turning the setup into a full observability stack.

## Problem

Ecowitt weather-station owners who already use Home Assistant often hit a wiring problem: the station can be configured to push data into Home Assistant, but the owner also wants a durable archive, last-year-vs-this-year views, and sometimes fan-out to another endpoint. The current path is a pile of partial answers: Home Assistant for automations, WeeWX for long-term station reports, MQTT bridges for Home Assistant discovery, and Node-RED or custom scripts for relay.

That split wastes weekend-scale setup time and makes it easy to break the feed that household automations already depend on.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1vk6fmv/weather_station_data_storage_and_comparison/ | Fresh Ecowitt owner wants a dashboard alongside Home Assistant that stores data forever, supports last-year-vs-this-year comparisons, and can relay because Ecowitt appears to send to one custom endpoint. |
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1dccewx/api_repeater_endpoint_replicator/ | Older but directly matching workaround request: duplicate an Ecowitt/custom-endpoint payload to multiple Home Assistant endpoints for weather comparison. |
| Home Assistant docs | https://www.home-assistant.io/integrations/ecowitt/ | Home Assistant's Ecowitt integration works by creating a callback endpoint that the Ecowitt console sends data to. |
| Home Assistant Community | https://community.home-assistant.io/t/ecowitt2mqtt-send-data-from-an-ecowitt-device-to-mqtt/231169 | ecowitt2mqtt demand shows users want local Ecowitt data outside cloud APIs and into MQTT/Home Assistant. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | WeeWX | Mature open-source weather station software with graphs, reports, databases, uploads, skins, and a large installed base. Strong competitor for the archive/reporting half. |
| Direct competitor | ecowitt2mqtt / Ecowitt MQTT Bridge add-ons | Good path for sending Ecowitt data to MQTT and Home Assistant discovery, but not focused on endpoint fan-out plus year-over-year comparison UX. |
| Indirect substitute | Home Assistant long-term statistics + custom dashboards | Already installed for many users, but comparison/reporting and safe multi-sink relay are not a one-screen setup. |
| Indirect substitute | Node-RED, n8n, webhook relay, Caddy, small custom code | Flexible, but turns a weather-station owner into an integration maintainer. |
| Status quo | Pick either Home Assistant or WeeWX as the main receiver and glue the rest manually | Works eventually, but risks breaking automations, losing history, or spending hours on plumbing before seeing useful comparisons. |

## Wedge

WeatherFork is deliberately narrower than WeeWX and less generic than Node-RED: it is an Ecowitt-shaped relay/archive/comparison packet. The first demo only needs to prove three things: receive the current Ecowitt payload, forward it to configured sinks without blocking storage, and render a family-readable comparison page from durable local data.

## Target user

Self-hosted Home Assistant users with Ecowitt-compatible weather stations who want durable local history and seasonal comparison views while keeping Home Assistant automations fed.

## MVP

- HTTP endpoint that accepts Ecowitt-compatible `PASSKEY`/sensor payloads and normalizes common fields.
- Local SQLite or newline-delimited JSON archive with idempotent sample writes.
- Configured sink forwarding to one or more HTTP endpoints with retry/error reporting.
- Static HTML report for current readings, recent gaps, and last-year-vs-this-year overlays from fixture data.
- Dry-run mode that reads a captured payload file and prints what would be stored/forwarded.

## Non-goals

- Not replacing WeeWX's full station ecosystem, skins, upload targets, or hardware driver layer.
- Not becoming a generic webhook automation platform.
- Not requiring cloud accounts or exposing weather data publicly.
- Not controlling Home Assistant automations directly.

## Status

v0.1.0-alpha.0 — scaffold/spec only. First runnable slice is tracked in Beads.
