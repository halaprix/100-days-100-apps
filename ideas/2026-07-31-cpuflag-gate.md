# Day 042 — CpuFlag Gate

Date: 2026-07-31
Status: repo-created

## One-line pitch

A read-only Proxmox/KVM CPU exposure preflight that catches x86-64-v2/v3 container and ML workload mismatches before Docker images or libraries crash-loop inside VMs.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1vbioov/immich_ml_crashlooped_after_update_it_was_proxmox/ | Fresh Immich ML crash-loop report traced to Proxmox default `kvm64` hiding x86-64-v2 from a Ryzen host; the same user said MySQL 8 had already hit the same class of issue. |
| GitHub — docker-library/mysql | https://github.com/docker-library/mysql/issues/1055 | MySQL Oracle Linux 9 images require x86-64-v2; users reported automatic image updates breaking environments, including Proxmox VMs using old virtual CPU models. |
| QEMU docs | https://www.qemu.org/docs/master/system/i386/cpu.html | QEMU documents host passthrough, named CPU models, ABI compatibility levels, and discourages legacy `kvm64`/`qemu64` because they expose a limited feature set. |
| ProxCLMC | https://github.com/credativ/ProxCLMC/ | Existing open-source tool checks cluster-wide Proxmox CPU compatibility for live migration, proving the problem space is real while leaving workload-specific preflight uncovered. |
| Anaconda | https://www.anaconda.com/blog/updated-cpu-requirements-linux-recommendations-windows | Anaconda announced a May 2026 transition of new Linux package builds toward x86-64-v2, citing NumPy, SciPy, pandas, ML, and data workloads as beneficiaries. |
| Proxmox CPU-type explainer | https://www.yinfor.com/2023/06/how-i-choose-vm-cpu-type-in-proxmox-ve.html | Proxmox v8 changed the UI default toward x86-64-v2-AES, while older `kvm64` VMs remain common and require manual flag-level reasoning. |

## Problem

Modern Linux images and scientific/ML packages are steadily assuming x86-64-v2 or newer CPU features. Proxmox and KVM can mask those features from guests through conservative CPU models such as `kvm64`, so a physical host may be capable while the VM still looks like x86-64-v1.

The failure mode is confusing:

- Docker or ML containers fail after an otherwise normal image update;
- logs blame NumPy, glibc, MySQL, Oracle Linux, or the app;
- admins search for app-specific fixes before checking VM CPU exposure;
- quick fixes like switching to `host` passthrough can accidentally change live-migration assumptions.

The status quo wastes well over 30 minutes when it happens, blocks self-hosted app upgrades, and can cause data-service downtime.

## Target user

- Self-hosters running Docker, Immich, MySQL, or ML workloads inside Proxmox VMs.
- Small-office admins using Proxmox without a dedicated virtualization engineer.
- Homelab authors who publish reproducible upgrade/migration guides and want a public-safe diagnostics packet.

## MVP scope

- `cpuflag-gate check --fixture examples/proxmox-kvm64-immich.json` for synthetic public-safe scenarios.
- Parsers for saved `lscpu`, `qm config`, and container error snippets.
- Rule engine mapping CPU flags to x86-64-v1/v2/v3/v4 and comparing host, guest, and workload requirements.
- Markdown packet export with blockers, warnings, candidate Proxmox CPU settings, live-migration caveats, rollback notes, and post-reboot verification commands.
- No live Proxmox API, SSH, or automatic setting changes in v0.

## Shortlist and wedge-first gate

| Candidate | Wedge-first gate | Result |
|---|---|---|
| CpuFlag Gate | Proxmox self-hoster running Docker/ML/database workloads in VMs → Proxmox UI/docs, QEMU docs, `lscpu`, ProxCLMC, forum snippets → existing tools require manual host/guest/workload mapping and often optimize for cluster migration rather than app crash prevention → read-only workload-specific CPU exposure packet before changing VM CPU model → r/selfhosted, Proxmox forums, Immich/MySQL/Anaconda error-search content, reply-style diagnostics → fresh Immich report plus 2026 Anaconda x86-64-v2 package shift. | Winner; clears score and gates. |
| RouterRecord Scout | Self-hoster replacing an ISP router and needing local DNS records → router spec pages, Amazon Q&A, Pi-hole/AdGuard, hosts files → specs often hide whether static local DNS records exist and running DNS adds maintenance → searchable router-capability checklist for local DNS only → r/selfhosted buyer threads and search content → fresh router-local-DNS frustration. | Rejected for this repo: too close to purchase/SKU research unless narrowed into software config diagnostics. |
| OIDC Mirror Packet | Self-hoster running two LANs with Pocket ID/passkeys → Keycloak/Authelia federation, SCIM, LDAP, manual duplicate users → passkey/user mirroring is identity-risky and provider-specific → read-only identity topology packet that recommends sync/federation patterns without copying secrets → r/selfhosted identity threads and Pocket ID users → fresh OIDC mirroring question. | Held at 17/25; useful but wedge and safety boundary need stronger validation. |
| ColdStart Ledger | Self-hoster scaling apps to zero overnight with KEDA → KEDA docs, Kubernetes dashboards, Prometheus/Grafana, manual pod-hour math → existing tools show metrics but not per-app cold-start/user-impact packets → saved pod-hours plus first-request latency budget report → r/selfhosted Kubernetes homelab posts → fresh scale-to-zero showcase. | Held at 16/25; good demo, but status-quo pain is weaker and Kubernetes audience is narrower. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | ProxCLMC | Strong open-source tool for finding the maximum cluster-wide CPU compatibility level supported across Proxmox nodes. CpuFlag Gate narrows to per-VM workload crash prevention and human-review packets. |
| Direct competitor | Proxmox UI/docs and QEMU docs | Authoritative sources for CPU models, host passthrough, named models, and live migration caveats. They do not ingest workload error snippets or produce a change packet. |
| Direct competitor | Virtualization inventory/monitoring tools | Can inventory hosts and VM settings, but usually do not map a container image's required x86-64 level against guest-exposed flags. |
| Indirect substitute | `lscpu`, `/proc/cpuinfo`, `qm config`, shell snippets, forum answers | Free and available, but fragmented. Users must know to compare host vs guest flags and tie that to container image baselines. |
| Status quo | Admin debugs the app image, pins/downgrades a container tag, changes VM CPU type to `host` or a named model, reboots, and hopes migration/security tradeoffs are acceptable | Slow during outages and easy to apply blindly without a before/after packet. |

## Wedge-first gate

Proxmox self-hoster running Docker/ML/database workloads in VMs → Proxmox UI/docs, QEMU docs, `lscpu`, ProxCLMC, forum snippets → existing tools require manual host/guest/workload mapping and often optimize for cluster migration rather than app crash prevention → read-only workload-specific CPU exposure packet before changing VM CPU model → r/selfhosted, Proxmox forums, Immich/MySQL/Anaconda error-search content, reply-style diagnostics → fresh Immich report plus 2026 Anaconda x86-64-v2 package shift.

## Wedge

CpuFlag Gate is not another monitoring dashboard and not a Proxmox automation layer. It wins only by staying narrow: the preflight moment between seeing a CPU-baseline crash and manually changing a VM CPU model.

The MVP can get attention because it turns scattered commands into a packet:

- classify host and guest x86-64 levels;
- detect guest masking below workload requirement;
- explain why `kvm64`/`qemu64` are likely suspects;
- warn when `host` passthrough conflicts with live migration;
- suggest named model candidates for review rather than editing Proxmox;
- produce a public-safe markdown artifact that can be pasted into a forum post, change note, or build log.

## Kill condition

Reject or narrow if early validation shows ProxCLMC or Proxmox-native tooling already covers workload-specific host/guest/image CPU-baseline diagnosis clearly enough, or if the first-user channel only wants one-line advice (`set CPU to host`) rather than a repeatable packet. Also reject any v0 scope that requires live Proxmox credentials, SSH, private hostnames, or automatic VM edits.

## Non-goals

- Not changing Proxmox VM settings automatically.
- Not connecting to Proxmox, SSH, Docker, or registry APIs in v0.
- Not guaranteeing live-migration safety for heterogeneous clusters.
- Not benchmarking CPU performance.
- Not storing real node names, VM names, private hostnames, IPs, or support dumps.

## Source access caveats

The bundled Reddit script was not available in this environment, so Reddit collection used the documented public RSS fallback path. The r/selfhosted RSS feed worked for the winning signal; several other subreddit RSS fetches failed or were blocked, and web-search fallback returned sparse Reddit results. X `whoami` worked, but X search returned `401 Unauthorized`, so no X search evidence was used. Competitor and timing checks used public web/GitHub/vendor/docs pages fetched during the run.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | The issue blocks app/database/ML upgrades and creates outage-style debugging. Pain is intermittent but high when triggered. |
| Feasibility | 5/5 | v0 is a deterministic parser/classifier/markdown generator using saved outputs and synthetic fixtures. No credentials or live API needed. |
| Demo potential | 4/5 | A before/after packet for `kvm64` + Immich/MySQL/Anaconda workloads is easy to show in a terminal and markdown diff. |
| Distribution | 4/5 | Specific channels exist: r/selfhosted, Proxmox forums, Immich/MySQL issue-search traffic, and diagnostic replies to x86-64-v2 error posts. |
| Competitive wedge / timing | 4/5 | Existing docs/tools cover pieces, but the workload-specific packet is narrow; 2026 package baseline shifts make the problem more timely. |
| Total | 21/25 | Clears repo/snapshot threshold; weakest dimensions are usefulness, demo, distribution, and wedge tied at 4/5. |

## Decision

Create the canonical project snapshot in the master repo: [projects/cpuflag-gate](../projects/cpuflag-gate).

No dedicated GitHub remote was configured locally, so there is no separate GitHub repository to report for CpuFlag Gate.

## Next build step

Implement the first deterministic CLI slice: parse `examples/proxmox-kvm64-immich.json`, classify host and guest CPU levels, emit a blocker when the guest is below the workload requirement, and snapshot-test the markdown packet.
