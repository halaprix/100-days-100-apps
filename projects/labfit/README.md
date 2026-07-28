# LabFit

A local-first planner that turns homelab hardware plus desired services into a placement report: what should run on Proxmox, the NAS, Docker/LXC, or stay separate.

## Problem

New self-hosters repeatedly reach the same crossroads: they have one mini PC, a NAS, Proxmox, Docker, and a list of services like Jellyfin, the *arr stack, Home Assistant, Pi-hole, Paperless, Vaultwarden, or Nextcloud. Existing guides explain how to install each piece, but they do not answer the user's actual question: where should each workload live on this hardware, what gets starved, and what failure mode should I avoid first?

The status quo is posting a full hardware inventory to r/selfhosted, reading conflicting opinions, then rebuilding the stack after storage, RAM, networking, or backup assumptions break.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1uoogix/jellyfin_arr_stack_run_on_proxmox_or_nas/ | User with Proxmox mini PC plus NAS asks whether Jellyfin/*arr should run on Proxmox or NAS. |
| Reddit r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1uonzl0/roast_me_constructively/ | Beginner homelab has Proxmox, Docker LXC, TrueNAS VM, *arr, Paperless, Vaultwarden, and NAS issues; asks for constructive architecture feedback. |
| Reddit r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1uolk4h/i_want_to_give_googledrivelike_remote_access_to/ | User wants Google-Drive-like family file access; says many tried solutions fail and asks for something idiot-proof. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | HLBuilder | Visual homelab/network planner; useful for topology, less focused on workload placement tradeoffs and failure-mode reports. |
| Direct competitor | Server sizing calculators / SmartMur hardware calculator | Estimate resources for generic service tiers, but do not map actual services to Proxmox vs NAS vs Docker/LXC with risk explanations. |
| Indirect substitute | Proxmox VE Helper Scripts / community install guides | Great for installing services after a decision; weak at deciding where the service should live. |
| Indirect substitute | Reddit/forum architecture reviews | High-signal but slow, repetitive, and dependent on volunteer attention. |
| Status quo | Trial-and-error rebuilds | Users discover bad placement when storage, backup, transcoding, permissions, or network paths fail. |

## Wedge

LabFit wins as a narrow decision report, not another deployer. It goes from a small YAML inventory plus desired services to an explainable placement plan with constraints, warnings, and alternatives. Incumbents plan topology or install scripts; LabFit answers the recurring "run it on Proxmox or the NAS?" question before users copy commands.

## Target user

Beginner-to-intermediate self-hosters with a mini PC or old desktop plus NAS who are planning their first durable service stack and want to avoid rebuilding it after common architecture mistakes.

## MVP

- `labfit plan examples/jellyfin-arr-nas.yml` to produce a placement report.
- Hardware model: CPU class, RAM, GPU/transcoding availability, disks, NAS shares, network links.
- Service catalog for the first 12 common apps: Jellyfin, Sonarr, Radarr, Prowlarr, qBittorrent, Home Assistant, Pi-hole/AdGuard, Paperless, Vaultwarden, Nextcloud, Immich, and backup.
- Rules for placement risks: RAM pressure, storage locality, transcoding, backup boundary, container-vs-VM overhead, NAS app-store lock-in, and remote access exposure.
- Markdown output suitable for pasting into a forum post or saving as a build plan.

## Non-goals

- No automatic deployment in the MVP.
- No collection of real hostnames, IPs, credentials, or telemetry.
- No remote scanning of a private network.
- No claim that the generated plan replaces backups or security review.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
