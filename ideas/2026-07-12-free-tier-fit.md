# Day 024 — FreeTierFit

Date: 2026-07-12
Status: repo-created

## One-line pitch

FreeTierFit is a local-first CLI that checks whether a self-hosted Docker Compose stack fits a tiny free-tier VM before you deploy and discover it is too slow, too memory-hungry, or ARM-incompatible.

## Source access caveat

Reddit public JSON returned the known `theme-beta` HTTP 403 block, so the run used the reddit-readonly RSS fallback for r/selfhosted, r/webdev, and r/SideProject. Several configured subreddits returned RSS HTTP 429 and were treated as unavailable rather than retried in a loop. Reddit thread fetches returned HTTP 403, so comment context was unavailable. X `whoami` worked, but X search returned HTTP 401 Unauthorized, so X did not contribute usable search evidence.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1uu5psr/what_are_you_favorite_light_weight_apps_to_self/ | Fresh self-hoster asks what lightweight apps are worth running on an Oracle Free Ubuntu VM with limited resources. |
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1uu3pdd/new_to_self_hosting/ | Fresh beginner self-hosting post describes subscription avoidance and asks for first-project recommendations. |
| Oracle docs | https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm | Always Free resources are positioned for small-scale apps and proof-of-concept testing. |
| Docker docs | https://docs.docker.com/engine/containers/resource_constraints/ | Docker supports CPU/memory constraints, but users still need stack-level fit decisions for tiny hosts. |
| Awesome Selfhosted | https://github.com/awesome-selfhosted/awesome-selfhosted | Large catalog validates self-hostable app discovery demand, but does not normalize app choices to constrained host budgets. |
| Dockpulse | https://github.com/hariharanragothaman/dockpulse | Adjacent container-resource profiler validates resource-limit pain while leaving a beginner free-tier preflight wedge. |

## Problem

Free-tier and very cheap VMs are attractive for self-hosters because they make experimentation feel risk-free. The hard part is deciding what will actually run there. App catalogs list hundreds of services, Docker docs explain resource limits, and Reddit threads contain experience reports, but a beginner still has to translate a planned Compose stack into memory, CPU, disk, port, and architecture risk.

The status-quo pain clears the threshold: deploying an oversized stack can waste an evening, trigger OOM kills, corrupt app state, cause public downtime for personal services, or send the user back to Reddit with a half-broken server.

## Target user

Self-hosters and side-project builders running small services on Oracle Cloud Always Free, cheap ARM VPS plans, or other low-resource personal servers.

## Shortlist gate

| Candidate | Wedge-first line | Decision |
|---|---|---|
| FreeTierFit | Beginner self-hoster on Oracle Free or a tiny VPS → Awesome Selfhosted, Compose examples, Docker docs, Portainer/Coolify after deploy → substitutes recommend apps or monitor running containers but do not preflight one Compose stack against a named tiny-host budget → local read-only budget report for memory/disk/ports/ARM64 before deployment → r/selfhosted replies, GitHub examples, long-tail “will X fit Oracle free tier” searches → fresh r/selfhosted posts ask what lightweight apps to run and how to start. | Winner; clears repo gate. |
| NASFit BOM | DIY NAS beginner choosing parts → Newegg NAS Builder, NAS Compares, WunderTech guides, PCPartPicker forums → strong content/tools already answer most hardware selection questions → only a narrow “self-hosted workload-to-bay-count sanity check” wedge remains → r/selfhosted/HomeServer replies → two fresh NAS posts show confusion. | Idea-only; useful but competitors and recent lab storage ideas make wedge weaker. |
| QuotaRouter DryRun | Builder whose viral LLM app hits provider RPM limits → LiteLLM, Portkey, OpenRouter, Helicone, provider dashboards → mature gateways already do routing, fallbacks, retries, and 429 handling → possible wedge is an offline traffic/replay simulator for side projects → r/webdev/search replies → fresh webdev post describes per-minute limit failure. | Idea-only; crowded LLM gateway/observability lane. |
| KenyaVPS Radar | Developer in Kenya choosing a VPS for side projects and light AI → VPS benchmarks, provider comparison sites, region-specific anecdotes → public benchmarks are broad and data freshness is hard → possible wedge is a reproducible ping/price worksheet for East Africa → local dev communities/search → fresh post asks for real experiences and hidden fees. | Idea-only; distribution and data maintenance need sharper proof. |
| PlacementPrep Triage | Indian CSE student overwhelmed before placements → roadmap.sh, LeetCode, placement roadmaps, senior advice → crowded education category and many free substitutes exist → only a school-specific prioritization wedge remains → campus communities → fresh post shows overwhelm. | Rejected; status quo is noisy but not painful enough for this lab. |

## MVP scope

- `free-tier-fit init` creates a local `free-tier-fit.yaml` host profile such as `oci-a1-free`, `tiny-vps-1g`, or `custom`.
- `free-tier-fit scan docker-compose.yml` parses services, images, ports, volumes, explicit resource limits, restart policies, and known app hints.
- `free-tier-fit report` prints Markdown/JSON fit, warn, and fail findings for memory overcommit, missing limits, disk pressure, exposed ports, ARM64 image risk, and port conflicts.
- A checked-in fixture catalog covers common lightweight apps and intentionally reports unknown app requirements as unknown instead of inventing numbers.
- Demo fixtures show a stack that fits, one that overcommits memory, one with missing limits, one with ARM64 caveats, and one disk-heavy media stack warning.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Dockpulse, docker-unit-converter, Docker resource-limit docs | They help profile containers or express CPU/memory limits, but they are not focused on pre-deploy “will this self-hosted stack fit my exact free-tier host?” decisions. |
| Direct competitor | Portainer, Coolify, Netdata, Uptime Kuma | Useful once services are running; they do not help a beginner decide which Compose stack is safe before deployment. |
| Indirect substitute | Awesome Selfhosted, Compose-Examples, blog posts, Reddit comments | Discovery and advice are abundant, but requirements are scattered and rarely normalized to tiny-host budgets or ARM compatibility. |
| Status quo | Ask Reddit, copy a Compose file, deploy, watch services get OOM-killed or crawl, then remove apps manually | This wastes setup time and can cause data loss, broken personal services, or public downtime on tiny servers. |

## Wedge

FreeTierFit avoids the broad monitoring, hosting-panel, and app-catalog markets. The wedge is a deterministic, local preflight report for one Compose file against a named tiny-host budget. It can be useful in 1–3 days because the MVP is static analysis plus conservative catalog hints, not cloud provisioning, telemetry, or live benchmarking.

## Kill condition

Kill or narrow the idea if target users say they already deploy one service at a time and the current trial-and-error loop takes under 30 minutes, or if Dockpulse/Coolify/Portainer add an equivalent pre-deploy tiny-host fit report with app requirement hints. Also kill any MVP scope that needs SSH access, cloud credentials, private host inventory, or made-up resource estimates.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Tiny-host misfits waste real setup time and can break personal services; fresh r/selfhosted posts show beginner app-selection pain. |
| Feasibility | 4/5 | Compose parsing, static budget math, fixtures, and a small app catalog are buildable in 1–3 days. |
| Demo potential | 4/5 | Easy to show: run against a sample Compose file, get fit/warn/fail output, adjust stack, rerun green. |
| Distribution | 4/5 | Concrete channels: helpful r/selfhosted/HomeServer replies, GitHub examples for OCI Free, and long-tail searches around “Oracle free tier self hosted apps” and “Docker compose memory limits.” |
| Competitive wedge / timing | 3/5 | Existing tools cover pieces of the problem, but the free-tier/tiny-host preflight angle is narrow enough to test. This is the weakest dimension. |
| Total | 19/25 | Clears repo threshold and both dimension gates. |

## Decision

Create the dedicated repo because FreeTierFit scored 19/25, Distribution is 4/5, and Competitive wedge / timing is 3/5.

Repo: https://github.com/halaprix/free-tier-fit

## Next build step

Implement `free-tier-fit scan` with fixture-backed Compose parsing and budget findings for memory overcommit, missing limits, ARM64 caveat, disk-heavy media stack warning, and port conflict.
