# Agent Instructions — ForegroundProbe

ForegroundProbe is a local-first Android foreground-service readiness-packet tool.

## Rules

- Keep examples public-safe: no device identifiers, log dumps, package identifiers from real apps, user data, screenshots, private paths, hosts, or credentials.
- The MVP reads only user-selected local manifest/config fixtures and produces deterministic findings.
- Do not add telemetry, cloud analysis, Play Console access, background-service mutation, battery-optimization bypasses, or device-control commands.
- State limitations plainly: static analysis cannot prove runtime survival across every Android vendor or OEM configuration.
- Beads is the only task tracker. Use `bd` for work items.
- Use Conventional Commits. Do not add LLM co-author trailers.

## MVP boundary

The first runnable slice parses synthetic Android project metadata and renders an Android 12–15 preflight packet. It does not connect to a device or change an Android project.
