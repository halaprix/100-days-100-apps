# Day 051 — QuadletState

Date: 2026-08-11
Status: repo-created
Repo: [`projects/quadlet-state`](../projects/quadlet-state)

## One-line pitch

QuadletState turns a small desired-state inventory into Podman Quadlet files and a reviewable diff plan for self-hosters who do not want to adopt Nix or hand-write every unit.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1vl6d91/declarative_end_state_container_deployment_tools/ | Fresh post from a self-hoster with many Podman Quadlets saying hand-writing quadlets has become tedious and asking for an end-state tool that generates services/units from a declarative description. |
| Podman docs | https://docs.podman.io/en/latest/markdown/podman-systemd.unit.5.html | Quadlet files use systemd unit syntax plus Podman-specific sections; flexible, but low-level enough that a higher-level planner can reduce hand-maintenance. |
| containers/podlet | https://github.com/containers/podlet | Existing tool generates Podman Quadlet files from commands, compose files, and existing objects; this is a strong substitute and defines the conversion-tool boundary. |
| quadlet-nix | https://github.com/SEIAROTg/quadlet-nix | Nix-based declarative Quadlet management already exists, validating demand while leaving room for non-Nix users who want a plain inventory. |
| Podlet write-up | https://blog.richy.net/2025/02/09/podmanquadlet.html | Notes that Podlet helps get started with Quadlet files and is not meant to be an end-all solution for creating and maintaining them. |

## Problem

Rootless Podman + Quadlet is attractive for small self-hosted servers because it keeps containers under systemd instead of adding a separate orchestrator. The maintenance pain starts when one server grows from a few standalone services into pods, networks, volumes, env-file references, and ordering rules. The status quo is hand-written unit files in dotfiles plus manual `daemon-reload` discipline. That is workable for one app, but tedious and drift-prone across a homelab stack.

## Target user

Self-hosters running rootless Podman Quadlets on one or two Linux servers who keep service definitions in dotfiles and want repeatable, reviewable changes without adopting Nix, Kubernetes, Nomad, or a full Ansible role library.

## MVP scope

- Parse a small YAML inventory describing pods, standalone containers, networks, volumes, env-file references, and systemd dependencies.
- Emit deterministic `.pod`, `.container`, `.network`, and `.volume` files to an output directory.
- Compare generated files against an existing Quadlet directory and print a colorless public-safe plan: create, update, unchanged, delete-candidate.
- Refuse inline secret values; env files are referenced by safe placeholder paths only.
- Ship one fixture for an Immich/Jellyfin-shaped pod plus one standalone monitor service.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Podlet | Strong conversion tool for generating Quadlet files from Podman commands, compose files, or existing objects. QuadletState should not try to be a better converter; it should own persistent desired-state inventory + diff planning. |
| Direct competitor | quadlet-nix / NixOS modules | Strong declarative answer for Nix users with typed options and rootless/rootful support. The wedge is plain YAML for users who explicitly do not want to adopt Nix. |
| Indirect substitute | Ansible templates, shell scripts, dotfiles | Common and flexible, but review/diff/idempotency is custom per homelab and easy to drift. |
| Indirect substitute | Docker Compose, Kubernetes, Nomad | Better orchestration surfaces for some users, but the target user wants systemd-native rootless Podman on a small server. |
| Status quo | Hand-write Quadlet files and reload systemd manually | Works for a few services; becomes repetitive and risky once pods, networks, volumes, env-file references, and dependencies multiply. |

## Wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| QuadletState | Self-hosters maintaining many Podman Quadlets → Podlet, quadlet-nix, Ansible templates, hand-written dotfiles → converters bootstrap files but do not maintain desired state; Nix is a worldview switch → plain inventory-to-Quadlet generator with public-safe diff plan → r/selfhosted, Podman/Quadlet search content, GitHub examples → fresh request for declarative end-state generation | Winner; clear narrow workflow and concrete distribution. |
| TailCert Packet | Self-hosters with Tailscale/private DNS and no DNS API → Certbot/acme.sh/Caddy docs, Tailscale certs, manual DNS-01 → wildcard/private-service cases get fragmented and renewal automation is brittle → setup-decision packet for viable ACME path and renewal risk → r/selfhosted plus Let's Encrypt/Tailscale search → fresh wildcard-certificate workaround request | Held: useful, but existing ACME clients/docs are strong; wedge needs proof beyond advice packaging. |
| Stream405 Probe | Self-hosters using rclone + Alist/TeraBox/WebDAV for large archives → rclone flags, forum threads, provider trial-and-error → failures appear after large transfers and provider-specific streaming limits are opaque → fixture-based capability probe before a multi-GB transfer → rclone/alist issue searches and forums → fresh 405 large-file failure | Held: real pain, but narrow provider-specific reliability and possible ToS gray zone reduce confidence. |
| A1 Capacity Scout | Oracle Always Free users blocked by A1.Flex capacity → retry scripts and OCI docs → users still guess region/time/shape combinations → read-only capacity attempt planner and safer retry envelope → OCI free-tier GitHub/search traffic → fresh Frankfurt capacity complaint | Rejected: multiple existing retry tools directly solve the job; no sharp wedge. |
| DavStart | Calendar users leaving hosted Fruux/Google → Radicale/Baïkal/Nextcloud guides → beginner setup choice feels risky → local decision packet and client-sync checklist → r/selfhosted + DAVx5/Radicale search → fresh Fruux outage/self-hosting question | Rejected for today: too close to existing DavSync Doctor day and mostly a guide/checklist rather than distinct software. |

## Wedge

QuadletState can win only by being narrower than configuration management and clearer than conversion tools. The wedge is not “manage containers”; it is “give me a tiny desired-state file, generate exact Quadlet files, and show the diff before I touch systemd.” A 1–3 day MVP can demonstrate the core value entirely on fixture inventories without touching a live host.

## Kill condition

Reject or narrow if Podlet adds persistent desired-state inventories plus diff planning, or if non-Nix Quadlet users report that Ansible/Jinja templates already take less than 15 minutes to maintain for multi-service pods. Also reject if the first users mostly want Docker Compose compatibility rather than Quadlet-native output.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | The workaround can waste hours whenever services are added or reorganized and can create service drift, though it is not usually a compliance/revenue issue. |
| Feasibility | 4/5 | A local CLI that parses one fixture inventory, renders deterministic unit files, and prints a plan is buildable in 1–3 days. |
| Demo potential | 4/5 | Easy demo: fixture inventory in, generated `.container`/`.pod` files and diff plan out. |
| Distribution | 4/5 | Specific channel exists: r/selfhosted posts, Podman/Quadlet search content, GitHub examples, and direct replies to users asking for non-Nix declarative Quadlet workflows. |
| Competitive wedge / timing | 3/5 | Competitors are strong, especially Podlet and quadlet-nix. The wedge survives only as plain desired-state + diff planning for non-Nix small-server users. |
| Total | 19/25 | Clears repo threshold and both dimension gates. |

## Decision

Create repo. QuadletState scored 19/25 with distribution 4/5 and competitive wedge/timing 3/5, so it clears the creation gates. Scaffold/spec snapshot was added under `projects/quadlet-state`; no dedicated GitHub remote was created during this local-first run.

## Next build step

Implement `quadlet-state plan --inventory examples/quadlet-state.yml --out generated/` to parse the fixture, emit deterministic Quadlet files, and print create/update/unchanged plan output without applying changes.

## Source access caveats

Reddit public JSON was blocked, so r/selfhosted collection used the `reddit-rss-fallback` layer. Several subreddit RSS probes returned `HTTP 429`, so web search was used for competitor/substitute validation. X/Twitter `whoami` worked, but search returned `401 Unauthorized`; no X data was used and no social writes were attempted.
