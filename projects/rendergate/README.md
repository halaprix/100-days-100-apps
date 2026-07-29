# RenderGate

A local-first access packet generator for safely granting one outside collaborator access to one render workstation or job API without opening the rest of a homelab.

## Problem

Self-hosters and small creative teams increasingly run GPU workstations for render, audio, image, and video jobs. The messy moment comes when a coworker needs access from outside the network: the owner wants the collaborator to trigger jobs on one box, but not browse the LAN, SSH into unrelated services, or inherit broad VPN access.

Existing zero-trust and mesh-VPN products can solve this, but the first-time setup is scattered across policy docs, tunnel docs, firewall rules, identity provider choices, and manual testing. The risky default is over-broad tailnet access, a shared SSH account, or a tunnel that exposes more than intended.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1v9eixe/how_would_you_allow_specific_access_to_on/ | Fresh self-hoster asks how to let an out-of-network coworker use one GPU render workstation via an existing Claude/API workflow, while not granting access to anything else on the network. |
| Tailscale ACL docs | https://tailscale.com/kb/1018/acls | Tailscale supports deny-by-default, directional ACLs and port-scoped access, but users must understand policy syntax and the fact ACLs do not govern local LAN access. |
| Tailscale Grants docs | https://tailscale.com/kb/1324/grants | Grants add network and application-layer capabilities, route filtering, and device posture, increasing power but also policy surface area for casual homelab users. |
| Cloudflare Access docs | https://developers.cloudflare.com/cloudflare-one/applications/configure-apps/self-hosted-apps/ | Cloudflare Access can publish self-hosted apps behind identity policies and tunnels, with token validation and origin-protection requirements that are easy to miss. |
| Teleport docs | https://goteleport.com/docs/ | Teleport provides robust infrastructure access, RBAC, audit logs, and session recording, but is heavier than a one-box collaborator access packet. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Tailscale ACLs / Grants | Strong mesh networking and least-privilege primitives. RenderGate does not replace Tailscale; it generates a narrow one-coworker/one-box packet, tests, and rollback notes for non-network specialists. |
| Direct competitor | Cloudflare Tunnel + Access | Good for publishing a specific app behind identity. The setup still requires correct hostname, Access policy, tunnel origin, token validation, and local service binding choices. |
| Direct competitor | Teleport | Powerful for SSH/app/database/desktop access with audit controls. Heavier operational footprint than many homelab GPU sharing cases. |
| Direct competitor | ZeroTier / NetBird / generic mesh VPNs | Useful overlay networks, but users still need to reason about route scope, identity, firewall, service binding, and test coverage. |
| Indirect substitute | Manual firewall rules, shared SSH keys, reverse proxy snippets, Synology/Drive handoff | Fast to improvise, but easy to over-permit or leave stale access after the collaboration ends. |
| Status quo | Ask a forum, copy a VPN/tunnel recipe, test from the coworker's machine, and hope lateral access is blocked | Creates security risk, wastes setup/debug time, and often lacks a written rollback or acceptance test packet. |

## Wedge

RenderGate is narrower than zero-trust platforms and safer than copy-pasting a VPN recipe. It focuses on one high-risk workflow: temporary collaborator access to a single render workstation or job API.

The v0 wedge is a deterministic packet, not a network daemon:

- capture the intended source user, target host, service ports, file-drop path, and expiration;
- choose a conservative access pattern such as Tailscale policy, Cloudflare Access app, or SSH-only plan;
- emit explicit non-goals: no subnet routes, no LAN browse, no shared admin account, no public origin bypass;
- generate acceptance tests the owner can run from inside and outside the tailnet;
- include rollback and stale-access cleanup steps.

## Target user

- Self-hosters running GPU/render/audio/image workloads for occasional collaborators.
- Small creative or AI automation teams without a dedicated network/security admin.
- Homelab builders who already use Tailscale, Cloudflare Tunnel, or another overlay, but need least-privilege guardrails for one external user.

## MVP

- `rendergate plan --fixture examples/render-coworker-access.json` for a synthetic public-safe scenario.
- Input model for collaborator identity, target service, allowed ports, desired data handoff, chosen access stack, expiration, and existing tunnel/tailnet assumptions.
- Rule engine that emits blockers, warnings, and suggested policy snippets for Tailscale ACL/Grant, Cloudflare Access, and host-firewall patterns.
- Markdown export with acceptance tests, rollback checklist, and public-safe redaction notes.

## Non-goals

- Not a VPN, tunnel, identity provider, reverse proxy, or firewall manager.
- Not applying live network policy in v0.
- Not collecting credentials, private hostnames, private IPs, domains, or real collaborator identities.
- Not replacing enterprise PAM/ZTNA products.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
