# Day 040 — RenderGate

Date: 2026-07-29
Status: repo-created

## One-line pitch

A local-first access packet generator for safely granting one outside collaborator access to one render workstation or job API without opening the rest of a homelab.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1v9eixe/how_would_you_allow_specific_access_to_on/ | Fresh self-hoster asks how to let an out-of-network coworker use one GPU render workstation via an existing Claude/API workflow, while not granting access to anything else on the network. |
| Tailscale ACL docs | https://tailscale.com/kb/1018/acls | Tailscale supports deny-by-default, directional ACLs and port-scoped access, but users must understand policy syntax and the fact ACLs do not govern local LAN access. |
| Tailscale Grants docs | https://tailscale.com/kb/1324/grants | Grants add network and application-layer capabilities, route filtering, and device posture, increasing power but also policy surface area for casual homelab users. |
| Cloudflare Access docs | https://developers.cloudflare.com/cloudflare-one/applications/configure-apps/self-hosted-apps/ | Cloudflare Access can publish self-hosted apps behind identity policies and tunnels, with token validation and origin-protection requirements that are easy to miss. |
| Teleport docs | https://goteleport.com/docs/ | Teleport provides robust infrastructure access, RBAC, audit logs, and session recording, but is heavier than a one-box collaborator access packet. |

## Problem

Small creative teams and self-hosters increasingly run a dedicated GPU machine for rendering, image/audio/video generation, or API-triggered batch work. The awkward collaboration moment is not "can I expose this service?" It is:

- one outside coworker should reach one workflow on one machine;
- the rest of the LAN should remain unreachable;
- file handoff should happen through a controlled folder or existing drive sync;
- access should expire cleanly after the project;
- the owner needs confidence before they paste policy snippets from a forum.

Mesh VPNs and zero-trust products expose the primitives, but the least-privilege plan is scattered across provider docs, route scope, service binding, identity policies, firewall rules, and manual tests.

## Target user

- Self-hosters running GPU/render/audio/image workloads for occasional collaborators.
- Small creative or AI automation teams without a dedicated network/security admin.
- Homelab builders who already use Tailscale, Cloudflare Tunnel, or another overlay, but need least-privilege guardrails for one external user.

## MVP scope

- `rendergate plan --fixture examples/render-coworker-access.json` for a synthetic public-safe scenario.
- Input model for collaborator label, target service, allowed ports, desired data handoff, chosen access stack, expiration, and existing tunnel/tailnet assumptions.
- Rule engine that emits blockers, warnings, and suggested snippets for Tailscale ACL/Grant, Cloudflare Access, and host-firewall patterns.
- Markdown packet export with acceptance tests, rollback checklist, and redaction notes.
- No live network changes, real credentials, real hostnames, real IPs, API calls, or policy application in v0.

## Shortlist and wedge-first gate

| Candidate | Wedge-first gate | Result |
|---|---|---|
| RenderGate | Self-hoster with a GPU render box and one outside collaborator → Tailscale/Cloudflare Access/Teleport/manual firewall recipe → tools are powerful but first-time users can over-broaden routes, ports, or origin exposure → one-coworker/one-box access packet with policy snippets, acceptance tests, expiration, and rollback → r/selfhosted, homelab GPU/AI workflow posts, and search queries around Tailscale/Cloudflare collaborator access → fresh public request plus rising AI-render workstation sharing use case. | Winner; clears score and gates. |
| ProxMove Packet | Beginner Proxmox mini-PC owner replacing a small SSD → backup/restore docs, Clonezilla, forum advice → migration path depends on VM/LXC layout, storage type, backup target, and downtime tolerance → dry-run checklist for one-node Proxmox SSD swaps → r/selfhosted and Proxmox forum/search traffic → fresh Reddit request. | Useful, but overlaps prior homelab storage ideas and is more checklist than app; held. |
| FileBrowser Mount Lens | Filebrowser Quantum user with container-mounted `/srv` and confusing storage totals → Filebrowser settings, Docker volume remapping, forum support → users cannot see how bind mounts and excluded paths affect quota display → local compose/mount analyzer for Filebrowser storage accounting → r/selfhosted support threads → fresh issue. | Too narrow and likely solved by configuration/docs; rejected before scoring. |
| DiskTrace follow-up | Windows Server admin needing continuous disk activity logs before crash → ProcMon/WPR/PerfMon/logman → same pain as Day 039 DiskTrace → existing daily winner already covers it → r/sysadmin/Microsoft Q&A → still fresh. | Duplicate of Day 039; rejected. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Tailscale ACLs / Grants | Strong mesh networking and least-privilege primitives. RenderGate does not replace Tailscale; it generates a narrow one-coworker/one-box packet, tests, and rollback notes for non-network specialists. |
| Direct competitor | Cloudflare Tunnel + Access | Good for publishing a specific app behind identity. The setup still requires correct hostname, Access policy, tunnel origin, token validation, and local service binding choices. |
| Direct competitor | Teleport | Powerful for SSH/app/database/desktop access with RBAC and audit controls. Heavier operational footprint than many homelab GPU sharing cases. |
| Direct competitor | ZeroTier / NetBird / generic mesh VPNs | Useful overlay networks, but users still need to reason about route scope, identity, firewall, service binding, and test coverage. |
| Indirect substitute | Manual firewall rules, shared SSH keys, reverse proxy snippets, Synology/Drive handoff | Fast to improvise, but easy to over-permit or leave stale access after the collaboration ends. |
| Status quo | Ask a forum, copy a VPN/tunnel recipe, test from the coworker's machine, and hope lateral access is blocked | Creates security risk, wastes setup/debug time, and often lacks a written rollback or acceptance test packet. |

## Wedge-first gate

Self-hoster with a GPU render box and one outside collaborator → Tailscale ACLs/Grants, Cloudflare Access/Tunnel, Teleport, ZeroTier/NetBird, or manual firewall/reverse-proxy snippets → existing tools are strong but require users to combine identity, route, port, origin-protection, host-firewall, expiration, and tests without accidentally allowing broader LAN access → local-first one-coworker/one-box access packet with policy snippets, explicit unsafe-pattern blockers, acceptance tests, and rollback → r/selfhosted, homelab GPU/AI workflow posts, and search/reply content around Tailscale/Cloudflare collaborator access → fresh public request plus more AI/render workflows make temporary compute sharing more common.

## Wedge

RenderGate is not a new VPN, ZTNA, reverse proxy, or identity system. It wins only if it stays narrower: a deterministic preflight packet for one risky collaboration workflow.

The value is the guardrail layer before changing anything:

- reject broad subnet routes, wildcard destinations, all-ports rules, missing expiration, missing rollback, and public origins without token validation;
- emit provider-specific snippets as human-reviewable templates, not live changes;
- pair every suggestion with an acceptance test: collaborator can reach job API, cannot reach unrelated service, cannot browse LAN, access expires or can be removed;
- produce a shareable support packet that avoids real secrets and private network details.

## Kill condition

Reject or narrow if early validation shows self-hosters can already produce a safe one-collaborator/one-render-box policy packet from Tailscale or Cloudflare docs in under 10 minutes, or if the common need is full enterprise access governance rather than temporary homelab/creative-team sharing.

## Non-goals

- Not applying live Tailscale, Cloudflare, SSH, firewall, IdP, or reverse-proxy changes in v0.
- Not storing real collaborators, private IPs, hostnames, domains, keys, service tokens, tunnel IDs, or tailnet data.
- Not replacing Teleport, Cloudflare Access, Tailscale, ZeroTier, NetBird, VPNs, or enterprise PAM.

## Source access caveats

Reddit public JSON was blocked by `HTTP 403 theme-beta`; the Reddit evidence came through the skill's public RSS fallback. Reddit comment-thread fetching also returned 403, so only the RSS-visible post title/body snippet was used. X `whoami` worked, but X search returned `401 Unauthorized`; no X search evidence was used.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | The pain is intermittent but high-risk: a bad setup can expose a private network or leave stale collaborator access. |
| Feasibility | 4/5 | v0 is a deterministic fixture-mode packet generator with snippets/tests, not live policy application. Provider coverage must stay template-based. |
| Demo potential | 4/5 | A synthetic render-workstation fixture can produce a clear before/after packet with blockers, snippets, acceptance tests, and rollback. |
| Distribution | 4/5 | Specific communities and search paths exist: r/selfhosted, homelab GPU/AI workflows, Tailscale/Cloudflare how-to searches, and support-style replies. |
| Competitive wedge / timing | 3/5 | Incumbents own the underlying access stack. The narrow wedge is preflight guardrails for temporary one-box sharing, strengthened by increasing AI/render workstation collaboration. |
| Total | 19/25 | Clears repo/snapshot threshold; weakest dimension is competitive wedge/timing because the primitives are already mature. |

## Decision

Create the canonical project snapshot in the master repo: [projects/rendergate](../projects/rendergate).

No dedicated GitHub remote was configured locally, so there is no separate GitHub repository to remove for RenderGate.

## Next build step

Implement deterministic fixture-mode packet generation and tests for unsafe access requests: broad subnet route, wildcard destination, all-ports rule, no expiration, and missing rollback.
