# FreeTierFit

FreeTierFit is a local-first CLI that checks whether a self-hosted Docker Compose stack fits a tiny free-tier VM before you deploy and discover it is too slow, too memory-hungry, or ARM-incompatible.

## Problem

New self-hosters often start with an always-free or very cheap VM and then ask which apps will actually run there. Existing lists recommend apps, and Docker docs explain limits, but the painful work is translating a specific Compose stack into a memory, CPU, disk, port, and architecture fit decision for a constrained host.

## Target user

Self-hosters and side-project builders running small services on Oracle Cloud Always Free, cheap ARM VPS plans, or other low-resource personal servers.

## MVP

- `free-tier-fit init` creates a local host budget profile such as `oci-a1-free`, `tiny-vps-1g`, or `custom`.
- `free-tier-fit scan docker-compose.yml` parses services, images, resource limits, ports, volumes, and known app hints.
- `free-tier-fit report` prints fit/warn/fail findings for memory overcommit, missing limits, disk pressure, exposed ports, and ARM64 image risk.
- Fixture catalog for common lightweight apps plus unknown-service fallbacks.

## Non-goals

- Not a cloud account manager and not a provisioning tool.
- Not a live benchmark service.
- Not a replacement for Docker Compose, Portainer, Coolify, or monitoring.
- No credentials, SSH access, or provider API keys in the MVP.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1uu5psr/what_are_you_favorite_light_weight_apps_to_self/ | Fresh self-hoster asks what lightweight apps are useful on an Oracle Free Ubuntu VM with limited resources. |
| Oracle docs | https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm | Always Free resources are positioned for small-scale apps and proof-of-concept testing. |
| Docker docs | https://docs.docker.com/engine/containers/resource_constraints/ | Docker exposes memory/CPU constraints, but users still need app-specific budget decisions. |
| Awesome Selfhosted | https://github.com/awesome-selfhosted/awesome-selfhosted | Large catalog validates demand for self-hostable app discovery, but not host-fit scoring. |
| Dockpulse | https://github.com/hariharanragothaman/dockpulse | Adjacent tool profiles/rewrites container limits, validating resource pain while leaving a beginner free-tier preflight wedge. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Dockpulse, Docker resource-limit calculators | They help profile or express CPU/memory limits, but are not framed around “will this self-hosted stack fit my exact free-tier host before I deploy?” |
| Direct competitor | Portainer, Coolify, Uptime Kuma, Netdata | Useful after or during deployment; they do not answer the pre-deploy app selection and resource-budget question for a constrained VM. |
| Indirect substitute | Awesome Selfhosted, Compose-Examples, blog posts, Reddit comments | Discovery is abundant, but requirements are scattered and rarely normalized to tiny-host budgets and ARM compatibility. |
| Status quo | Ask Reddit, copy a Compose file, deploy, watch services get OOM-killed or crawl, then remove apps manually | The loop wastes setup time and can cause data loss or public downtime on small servers. |

## Wedge

FreeTierFit stays out of the broad monitoring and PaaS lanes. The wedge is a deterministic preflight report for a named tiny-host budget plus a curated app-requirements catalog. It gives beginners a shareable “this stack fits / does not fit” report before they touch cloud credentials.

## Current status

v0.1.0-alpha.0 — scaffold/spec only.
