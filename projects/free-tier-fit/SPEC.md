# FreeTierFit SPEC

## User story

As a self-hoster using a free-tier or tiny VPS, I want to check a planned Docker Compose stack against my host budget before deploying it, so I do not waste an evening debugging OOM kills, bad ARM images, port conflicts, or apps that are too heavy for the box.

## MVP features

1. `free-tier-fit init`
   - Create `free-tier-fit.yaml` with a host budget profile.
   - Include built-in profiles for `oci-a1-free`, `tiny-vps-1g`, and `custom`.
2. `free-tier-fit scan`
   - Parse one Docker Compose file.
   - Extract service names, images, ports, volumes, explicit CPU/memory limits, restart policies, and dependency count.
   - Warn when services lack limits on tiny hosts.
3. App hint catalog
   - Store a small local catalog of common self-hosted apps with conservative memory, disk, and ARM64 notes.
   - Treat unknown images as “needs manual estimate” instead of pretending to know.
4. Report output
   - Markdown and JSON report with fit/warn/fail findings.
   - Include likely fix suggestions: add limits, reduce app count, move database off-box, pick ARM64-compatible images, or choose a larger profile.

## Data model

```yaml
version: 1
host:
  profile: oci-a1-free
  memory_mb: 6144
  cpu_cores: 2
  disk_gb: 47
  architecture: arm64
scan:
  compose: docker-compose.yml
  reserve_memory_percent: 20
  reserve_disk_gb: 8
```

## Technical approach

- Language: TypeScript CLI on Node.js 22+.
- Parser: YAML parse of Compose files with conservative handling of anchors and extension fields.
- Catalog: checked-in YAML fixtures for common apps and unit tests around risk scoring.
- Reports: deterministic Markdown and JSON for easy sharing in support threads.

## Validation plan

- Unit-test Compose parsing against fixture files.
- Unit-test budget math for healthy, warning, and failure cases.
- Fixture demos for:
  - stack fits tiny host,
  - memory overcommit,
  - missing resource limits,
  - ARM64 image caveat,
  - disk-heavy media stack warning,
  - port conflict.
- Validate the wedge by replying manually in relevant self-hosted support threads with a report example, not by spamming.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and specification.
- v0.1.0-alpha.1 — runnable CLI with fixture-backed `scan` and `report`.
- v0.2.0-alpha.1 — initial catalog for 20 common self-hosted apps and OCI/tiny-VPS profiles.
