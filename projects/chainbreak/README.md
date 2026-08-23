# ChainBreak

ChainBreak is a local change-window preflight that checks whether every declared remote recovery path depends on the VPN, firewall, jump host, or management route being changed.

## Problem

Routine maintenance can become a remote-site outage when the component being restarted is also required to reach its own console, power control, or fallback path. A recent r/sysadmin incident described a VPN that did not return after patching, while iDRAC was reachable only through that VPN; the operator narrowly avoided a 500 km round trip.

Network maps, CMDBs, diagrams, and runbooks can document pieces of the topology, but small teams often lack a per-change answer to one hard question: **is at least one declared recovery route independent of this change target?**

## Target user

Solo or small-team IT operators responsible for remote sites, before changing a VPN gateway, firewall, jump host, or management-plane route.

## MVP

- Read a local YAML or CSV inventory of components, endpoints, and directed recovery dependencies.
- Evaluate a planned change target against declared console, power, and alternate-access routes.
- Flag circular recovery paths and missing independent-management assumptions.
- Generate a deterministic Markdown/HTML packet with a stop/review verdict, path explanations, assumptions, and human checks.
- Use synthetic fixtures only; no discovery, network calls, credentials, or device control.

## Non-goals

- No topology auto-discovery, monitoring replacement, CMDB, or privileged device integration.
- No active probing, VPN/firewall changes, remote-console control, or guarantee that a declared recovery path works.
- No attempt to model a full enterprise topology from incomplete data.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vvfb7y/vpn_server_250km_away_wont_come_back_online_pour/ | A patched VPN failed to return while iDRAC depended on that VPN; the operator added additional remote-management paths afterward. |
| LibreNMS | https://docs.librenms.org/Extensions/Network-Map/ | Provides dynamic device maps from discovery data, showing the substitute category is established. |
| NetBox Visual Explorer | https://netboxlabs.com/docs/visual-explorer/ | Visualizes documented WAN, power, cable, and L2/L3 dependencies. |
| Auvik | https://support.auvik.com/hc/en-us/articles/204908674-Your-network-map | Maps physical/logical connections and VPN tunnels. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | NetBox / Visual Explorer | Broad documented infrastructure visualization; needs maintained source-of-truth data and does not center a per-change recovery-loop verdict. |
| Direct competitor | LibreNMS / Auvik network maps | Strong visibility tools for discovered or logical topology, but not a directed recovery-assumption gate for one planned outage. |
| Indirect substitute | Diagrams, spreadsheets, runbooks, and peer review | Flexible but often stale; recovery path direction and independence remain implicit. |
| Status quo | Restart the component and improvise after management disappears | Risks downtime, emergency workarounds, and travel to a remote site. |

## Wedge

ChainBreak keeps the surface small: an operator supplies the recovery dependencies they actually trust, chooses a change target, and gets a reproducible verdict about circular paths and unproven assumptions. It complements a map or CMDB instead of trying to replace one.

## Current status

v0.1.0-alpha.0 — scaffold and specification only. The local dedicated repository has no remote configured.
