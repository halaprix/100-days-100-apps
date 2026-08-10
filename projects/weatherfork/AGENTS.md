# Agent Instructions — WeatherFork

WeatherFork is a local-first Ecowitt weather-station relay/archive/comparison tool for Home Assistant users.

## Rules

- Keep examples public-safe: no real station IDs, exact home coordinates, private hostnames, private addresses, credentials, or raw personal weather logs.
- Use only synthetic payloads and fixture timestamps in examples/tests.
- Do not build a broad webhook automation platform; the wedge is Ecowitt-shaped relay + durable archive + seasonal comparison.
- Store before forwarding; Home Assistant downtime must not drop samples.
- Beads is the only task tracker. Use `bd` for all work.
- Conventional Commits only. Do not add LLM co-author trailers.

## MVP boundary

The first runnable slice is local: parse fixture payloads, normalize key weather fields, persist them, and render static comparison output. HTTP receiving and Docker packaging come after the static contract is proven.
