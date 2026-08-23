# Day 059 — ChainBreak

Date: 2026-08-23
Status: repo-created
Repo: [`projects/chainbreak`](../projects/chainbreak)

## One-line pitch

ChainBreak turns a small, local recovery-dependency inventory into a change-window packet that flags circular remote-access paths before a VPN, firewall, or jump host is restarted.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vvfb7y/vpn_server_250km_away_wont_come_back_online_pour/ | A fresh solo-IT incident: a patched VPN server did not return, its iDRAC path depended on that VPN, and the author nearly faced a 500 km round trip. A second remote-management path was added only after recovery. |
| LibreNMS documentation | https://docs.librenms.org/Extensions/Network-Map/ | LibreNMS builds dynamic maps from discovered xDP and MAC/ARP data; it is topology visualization, not an explicit check that a named recovery path depends on the component being changed. |
| NetBox Visual Explorer | https://netboxlabs.com/docs/visual-explorer/ | NetBox can visualize cable, WAN, power, and L2/L3 dependencies from a maintained system of record. It is a strong substitute, but needs complete modeling and does not present a focused pre-change circular-recovery verdict. |
| Auvik support | https://support.auvik.com/hc/en-us/articles/204908674-Your-network-map | Auvik maps physical/logical connectivity and VPN tunnels, confirming that topology maps are established infrastructure products rather than a whitespace claim. |

## Problem

A remote-access component can also be the only route to recover itself: the VPN exposes the management controller, the jump host reaches the firewall, or an identity proxy authorizes the console. During a patch/reboot window this dependency loop is usually discovered from a diagram, spreadsheet, or memory only after the component fails.

The status quo can mean hours of downtime, an urgent workaround, or an on-site trip. That clearly exceeds the pain threshold: the fresh r/sysadmin incident explicitly involved a threatened 500 km drive and a delayed patch recovery.

## Target user

Solo or small-team IT operators responsible for remote sites, especially those changing a VPN gateway, firewall, remote-access jump host, or management-plane route without an enterprise CMDB.

## MVP scope

- Read a local YAML or CSV inventory of components, management endpoints, and directed recovery dependencies.
- Let the operator declare a planned change target and intended remote recovery methods.
- Detect paths where every listed recovery route traverses the change target, plus missing independent power/console/alternate-path declarations.
- Render a deterministic Markdown/HTML change-window packet with a stop/review banner, path explanations, assumptions, and a human checklist.
- Ship only synthetic fixtures. No discovery, credentials, active probes, network access, device control, or claims of complete topology coverage.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | NetBox and Visual Explorer | A capable source-of-truth and visualization stack that can represent dependencies, but it requires maintained inventory data and its published views are broad infrastructure visualizations rather than a local pre-change recovery-loop gate. |
| Direct competitor | LibreNMS and Auvik network maps | Both provide topology visibility; their documented maps focus on discovered/physical/logical links. They are valuable inputs but do not replace an operator-authored statement of which paths can recover a particular planned outage. |
| Indirect substitute | Visio/draw.io diagrams, spreadsheets, runbooks, and a second-admin review | Familiar and flexible, but dependency direction and alternate-path assumptions tend to be implicit, stale, or difficult to verify during a change window. |
| Status quo | Restart the gateway and improvise if the management route disappears | The fresh incident shows a circular iDRAC-over-VPN route can turn a routine patch into downtime and a potential long road trip. |

## Wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| ChainBreak | Solo/small-team remote-site operators before restarting a VPN, firewall, or jump host → NetBox, LibreNMS/Auvik maps, diagrams, and runbooks → topology is broad or incomplete and rarely answers whether the specific recovery route traverses the change target → local, explicit directed dependency check that emits a pre-change recovery packet from a minimal inventory → searches and practical write-ups around remote-access outage, iDRAC-over-VPN, jump-host, and change-window failures in r/sysadmin, MSP, NetBox, and self-hosted communities → a fresh incident makes the costly loop concrete | Winner; narrow workflow, material status-quo cost, and a specific technical-search/community path. |
| Remote-console monitor | Remote-site operators → Uptime Kuma, PRTG, LibreNMS, Auvik, and vendor alerts → these products already monitor reachability and alerts, while a new monitor does not establish independent recovery → no narrow wedge beyond generic monitoring → generic sysadmin channels → same incident | Rejected; crowded monitoring category and wrong job. |
| Virtual-browser phishing blocker | IT teams → managed-device policy, browser isolation, identity controls, EDR, and security vendors → existing controls are policy/security programs, and the source does not prove a narrowly unserved workflow → generic browser-security extension → security audiences → fresh discussion | Rejected; generic security wrapper/extension is reject-by-default with no proven channel. |
| Legacy-server compatibility checker | Administrators moving an old line-of-business application → vendor support, VM snapshots, application compatibility testing, and upgrade labs → the available signal does not establish repeat pain or a defensible data source for compatibility predictions → broad OS-version check → generic sysadmin searches → a fresh Server 2016/2019 question | Rejected; a useful query but no credible MVP evidence source or wedge. |

## Wedge

ChainBreak is not another network map or monitoring system. It asks a smaller, safety-critical question before a particular change: **can any declared recovery path still reach a console or power control without traversing the component being changed?** A minimal, operator-authored directed graph is feasible where full CMDB modeling is not. The output is review evidence and explicitly listed assumptions, not discovery or a guarantee that every path works.

## Kill condition

Reject or narrow if two target operators can produce the same per-change recovery verdict from their current NetBox/monitoring/runbook workflow in under 10 minutes, or if they will not maintain the few dependency facts needed for a meaningful result. Do not add agent-based discovery or privileged integrations merely to inflate coverage; an unverified graph must remain visibly incomplete.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 5/5 | A failed remote-access change can produce downtime, urgent travel, and an unsafe recovery scramble. |
| Feasibility | 5/5 | Directed-graph validation, YAML/CSV input, fixtures, and Markdown output fit a deterministic 1–3 day CLI MVP. |
| Demo potential | 4/5 | A small synthetic inventory can visibly turn into a red circular-dependency finding and recovery-path table. |
| Distribution | 4/5 | Specific search intent and repeatable communities exist: remote-access outage, iDRAC-over-VPN, jump-host, and change-window discussions in sysadmin/MSP/NetBox/self-hosted channels. |
| Competitive wedge / timing | 3/5 | Mature map products are strong; the focused per-change recovery verdict is distinct but must prove that operators will maintain its minimal inventory. |
| Total | 21/25 | Clears the repo threshold and both dimension gates; competitive wedge/timing is the weakest dimension. |

## Decision

Create repo. ChainBreak scores 21/25 with distribution 4/5 and competitive wedge/timing 3/5. A local dedicated scaffold and its public-safe master snapshot were created; no dedicated GitHub remote was created.

## Next build step

Implement `chainbreak check --inventory fixtures/branch-site.yml --change vpn-gateway --out packet.md` against one synthetic VPN/iDRAC circular-dependency fixture and one independent-management fixture. Validate the packet with two operators before adding importers or discovery.

## Source access caveats

Reddit public JSON was blocked with `theme-beta`; RSS fallback supplied the fresh r/sysadmin permalink, while several other configured subreddit reads hit RSS `HTTP 429`. The linked Reddit page was later publicly extractable, but no score or comment-count claim is made. Read-only `xurl search` returned `401 Unauthorized`, so no X evidence was used and no social writes were attempted. Competitor validation used public documentation for NetBox, LibreNMS, and Auvik.
