# QuadletState

Generate Podman Quadlet files from a small desired-state inventory, then show the diff before anything touches systemd.

## Problem

Self-hosters moving more containers to Podman Quadlets like the systemd-native model, but managing a multi-service homelab by hand gets tedious fast. Each app can require `.container`, `.pod`, `.network`, `.volume`, `.env`, dependency ordering, rootless paths, and secret placeholders. Podman's native Quadlet docs are powerful but low-level; conversion tools help bootstrap from a command or compose file, but they do not give a simple reviewed end-state inventory for ongoing small-server operations.

That workaround can burn weekend-scale time and can also create service drift: the files in dotfiles say one thing, systemd is running another, and nobody wants to discover that during an update window.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1vl6d91/declarative_end_state_container_deployment_tools/ | Fresh post from a self-hoster with many Podman Quadlets saying hand-writing quadlets has become tedious and asking for a declarative end-state tool that generates units/services. |
| Podman docs | https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html | Quadlet uses systemd unit-file syntax plus custom Podman sections; the official surface is flexible but verbose enough to justify a higher-level planner. |
| containers/podlet | https://github.com/containers/podlet | Existing official-adjacent tool generates Quadlet files from Podman commands, compose files, or existing objects; strong substitute but positioned as conversion/bootstrap rather than persistent desired-state planning. |
| quadlet-nix | https://github.com/SEIAROTg/quadlet-nix | Strong declarative option for Nix users, including typed Quadlet options and rootless/rootful support; validates demand but narrows the wedge to non-Nix self-hosters. |
| Podlet write-up | https://blog.richy.net/2025/02/09/podmanquadlet.html | Notes that podlet helps get started with Quadlet files and is not meant to be an end-all solution for creating and maintaining them. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Podlet | Converts Podman commands, compose files, and existing objects into Quadlet files. QuadletState must not compete as a better converter; it should own the desired-state + diff packet. |
| Direct competitor | quadlet-nix / NixOS modules | Strong declarative management for Nix users. The wedge is for people who want a plain YAML inventory and systemd/Podman files without adopting Nix. |
| Indirect substitute | Ansible templates, Shell scripts, dotfiles | Flexible and already common, but review/diff/idempotency is hand-rolled and easy to drift. |
| Indirect substitute | Docker Compose, Kubernetes, Nomad | Better orchestration surfaces for some users, but the target user explicitly wants rootless Podman + systemd/Quadlet on a small server. |
| Status quo | Hand-write Quadlet unit files, commit them, and run `systemctl daemon-reload` manually | Works for a few services; becomes tedious and risky once pods, networks, env files, and dependencies multiply. |

## Wedge

QuadletState is narrower than Nix and less magical than a full orchestrator: one public-safe inventory file, one generated Quadlet directory, one human-readable diff/plan. It wins if a self-hoster can paste a tiny YAML description of a pod plus services and immediately see exactly which `.container`, `.pod`, `.network`, and `.volume` files would change.

## Target user

Self-hosters running rootless Podman Quadlets on one or two Linux servers who keep service definitions in dotfiles and want repeatable changes without adopting Nix, Kubernetes, or a full configuration-management stack.

## MVP

- Parse a small YAML inventory describing pods, standalone containers, networks, volumes, env-file references, and systemd dependencies.
- Emit deterministic `.pod`, `.container`, `.network`, and `.volume` files into an output directory.
- Compare generated files with an existing Quadlet directory and print a colorless public-safe plan.
- Refuse to inline secrets; env files are referenced by path labels only.
- Include fixtures for one Immich-shaped pod plus one standalone service.

## Non-goals

- Not applying changes or running `systemctl` in the first slice.
- Not replacing Podman, Podlet, Quadlet, Nix, Ansible, Kubernetes, or Nomad.
- Not reading real `.env` contents or collecting machine-specific host details.
- Not becoming a generic Docker Compose compatibility layer.

## Status

v0.1.0-alpha.0 — scaffold/spec only. First runnable slice is tracked in Beads.
