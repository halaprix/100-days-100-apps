# CpuFlag Gate

A read-only Proxmox/KVM CPU exposure preflight for x86-64-v2/v3 container and ML workload crashes.

## Problem

Self-hosters often run Docker hosts inside Proxmox VMs. A guest can see an old virtual CPU model such as `kvm64` even when the physical host supports newer x86-64 levels. That hidden mismatch shows up late: MySQL images fail with `CPU does not support x86-64-v2`, Python/NumPy/ML containers crash-loop, and admins blame the app image instead of the VM CPU type.

CpuFlag Gate does not tune a cluster automatically. It creates a deterministic packet showing host CPU level, guest-exposed level, workload requirements, live-migration risk, and the exact Proxmox/QEMU setting candidates to review before changing anything.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1vbioov/immich_ml_crashlooped_after_update_it_was_proxmox/ | Fresh Immich ML crash-loop report traced to Proxmox default `kvm64` hiding x86-64-v2 from a Ryzen host. |
| GitHub — docker-library/mysql | https://github.com/docker-library/mysql/issues/1055 | MySQL Oracle Linux 9 images require x86-64-v2; users reported Proxmox/dev VM breakage and CPU model workarounds. |
| QEMU docs | https://www.qemu.org/docs/master/system/i386/cpu.html | QEMU documents host passthrough, named CPU models, ABI levels, and discourages limited legacy `kvm64`/`qemu64` models. |
| ProxCLMC | https://github.com/credativ/ProxCLMC/ | Existing tool validates cluster-wide live-migration CPU baselines, proving the domain matters while leaving room for workload-specific preflight. |
| Anaconda | https://www.anaconda.com/blog/updated-cpu-requirements-linux-recommendations-windows | Anaconda is moving Linux packages toward x86-64-v2 from May 2026, including scientific/ML package context such as NumPy, SciPy, and pandas. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | ProxCLMC | Strong for cluster-wide Proxmox live-migration CPU compatibility. CpuFlag Gate narrows to per-VM workload crash prevention and packetized before/after review. |
| Direct competitor | Proxmox UI/docs and QEMU docs | Authoritative, but users must map host flags, guest CPU model, workload image baseline, and migration tradeoffs manually. |
| Indirect substitute | `lscpu`, `/proc/cpuinfo`, `qm config`, forum posts, shell snippets | Cheap and available, but fragmented; they do not explain why a container image fails inside a VM whose physical host is capable. |
| Status quo | Admin reads crash logs, searches the error, changes VM CPU type to `host` or a named model, then hopes migration/security assumptions still hold | Wastes incident time and risks unsafe changes, especially on homelab or small-office Proxmox hosts with mixed workloads. |

## Wedge

CpuFlag Gate wins by being narrower than Proxmox inventory and safer than forum-copy fixes:

- compare host and guest-exposed x86-64 levels;
- lint common workload requirements for MySQL/Oracle Linux 9, Anaconda scientific stacks, Immich ML/NumPy, and generic container images;
- warn when `host` passthrough breaks live-migration assumptions;
- emit a markdown packet with current CPU model, required flags, candidate settings, rollback notes, and commands to verify after reboot;
- stay read-only in v0 and require no Proxmox API token.

## Target user

- Self-hosters running Docker/Immich/MySQL/ML stacks inside Proxmox VMs.
- Small-office admins using Proxmox for app VMs without a dedicated virtualization engineer.
- Homelab content creators who publish reproducible migration or upgrade guides.

## MVP

- `cpuflag-gate check --fixture examples/proxmox-kvm64-immich.json` for synthetic public-safe scenarios.
- Parsers for saved `lscpu`, `qm config`, and container error snippets.
- Rule engine for x86-64-v1/v2/v3/v4 requirements and Proxmox CPU model candidates.
- Markdown packet export for a change ticket or build-log post.

## Non-goals

- Not changing Proxmox VM settings automatically in v0.
- Not connecting to the Proxmox API or requiring SSH credentials in v0.
- Not guaranteeing live-migration safety for heterogeneous clusters.
- Not benchmarking CPU performance.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
