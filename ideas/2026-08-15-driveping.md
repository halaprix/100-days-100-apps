# Day 055 — DrivePing

Date: 2026-08-15
Status: repo-created
Repo: [`projects/driveping`](../projects/driveping)

## One-line pitch

DrivePing is a glanceable Android head-unit connectivity sentinel that shows live latency/loss while driving and exports a drop log after intermittent YouTube, maps, or hotspot failures.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/androidapps | https://www.reddit.com/r/androidapps/comments/1vop3cb/looking_for_a_pinglatency_monitor_that_stays/ | Fresh Android user with an aftermarket car head unit wants continuous connectivity checks, status-bar visibility, boot auto-start, and something different from bandwidth meters. |
| Google Play / Ping Monitor On Status Bar | https://play.google.com/store/apps/details?id=com.mrstudios.pingmonitorfree&hl=en | Existing app confirms demand for ping in the status bar; description also shows Android-version limitations and overlay fallback. |
| Google Play / PingTools Network Utilities | https://play.google.com/store/apps/details?id=ua.com.streamsoft.pingtools&hl=en-US | Broad Android network utility includes watcher/continuous monitoring, ping, traceroute, and background work, but it is a toolbox rather than a car-head-unit drop logger. |
| Google Play / Network Monitor Mini | https://play.google.com/store/apps/details?id=info.kfsoft.android.TrafficIndicator&hl=en | Common substitute monitors upload/download speed in a screen corner, which does not answer idle connectivity or latency loss. |
| Android Developers / Foreground services | https://developer.android.com/develop/background-work/services/fgs | Android foreground services are the right visible long-running primitive but create status-bar notifications and have modern background-start restrictions. |
| Android Developers / background-start restrictions | https://developer.android.com/develop/background-work/services/fgs/restrictions-bg-start | Android 12+ and 15+ foreground-service restrictions make boot/always-on behavior a timely implementation risk to handle explicitly. |

## Problem

Aftermarket Android car head units often show Wi-Fi or hotspot connectivity while apps still report no network, stall, or lose server access. Drivers cannot safely open a network toolbox while moving, and bandwidth meters are misleading because a connection can be broken while no traffic is flowing. The painful job is to know, at a glance, whether the head unit currently has real Internet reachability and whether the failure was DNS, gateway, packet loss, latency, or the media app itself.

The status quo wastes repeated troubleshooting sessions: restart hotspot, toggle Wi-Fi, blame YouTube, blame the head unit, try generic Android Auto guides, or manually run ping tools after the failure has already disappeared. For anyone debugging a car install, delivery route tablet, camper/RV hotspot, or kiosk-like Android head unit, that can easily cost more than 30 minutes per week until the root cause is found.

## Target user

People running aftermarket Android car head units, camper/RV Android tablets, delivery-route dashboards, or kiosk-like Android devices that need safe, glanceable Internet health while the primary app is in front.

## MVP scope

- Android foreground service with a persistent notification showing current target, latency, packet-loss state, and last drop time.
- Optional large overlay mode for head units where status-bar text is not available or Android version blocks direct placement.
- Probe profiles for gateway, DNS resolver, and public HTTPS endpoint so failures are classified as local Wi-Fi, DNS, Internet, or app/service-specific.
- Boot/start-on-unlock setup checklist that explains Android 12/15 foreground-service restrictions and OEM battery exceptions instead of pretending always-on is universal.
- Drive-session log export as local JSON/CSV/Markdown: timestamp, network type, target, latency, loss, DNS result, and state transitions.
- No background location, no tracking, no cloud account, and no storage of personal browsing or app usage.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Ping Monitor On Status Bar | Very close substitute for status-bar ping. Its Play listing indicates Android-version limitations and overlay fallback; it is generic and not positioned around head-unit drive-session diagnosis or drop-log export. |
| Direct competitor | PingTools Network Utilities | Broad and capable network toolbox with watcher, ping, traceroute, and saved/shareable data. Strong substitute for admins, but too interactive and broad for a glanceable in-drive sentinel. |
| Indirect substitute | Network Monitor Mini and network-speed indicators | Good for seeing current traffic, but speed meters do not prove idle reachability, DNS health, or latency/loss. |
| Indirect substitute | Android Auto/head-unit troubleshooting guides, hotspot toggles, manual pings | Useful after a failure, but they do not create a timestamped packet-loss/DNS/drop timeline while the problem is happening. |
| Status quo | Guess, restart network pieces, or open tools after parking | Tolerable for one-off phone debugging; painful for repeated head-unit/hotspot failures where the evidence disappears before the user can inspect it. |

## Wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| DrivePing | Aftermarket Android head-unit users debugging intermittent Internet while driving → ping/status-bar apps, PingTools, speed meters, Android Auto guides → substitutes are generic, interactive, traffic-focused, or lack a drive-session drop log → car-safe foreground notification/overlay plus DNS/gateway/HTTPS classification and exportable incident packet → r/androidapps, XDA/head-unit forums, RV/camper hotspot groups, and search pages for “Android head unit no network YouTube” → fresh post asks for exactly continuous ping/latency visibility with boot behavior | Winner; narrow enough to survive direct competitors and concrete channels exist. |
| SecureClipVault | Android users wanting saved clipboard snippets hidden from people borrowing the phone → password managers, Gboard clipboard, clipboard managers → substitutes either expose clipboard or require app switching → keyboard-adjacent encrypted snippet picker → r/androidapps searches → fresh post asks to save sensitive clipboard items | Rejected; encouraging password-like clipboard storage is unsafe, and Android keyboard/overlay limits make the wedge risky. |
| SeniorLoad Planner | College senior juggling classes, two internships, and two jobs → paper planners, Google Calendar, Notion, Todoist → generic tools are too flexible and paper cannot rebalance conflicts → printable week planner generated from recurring commitments → campus communities and planner search → fresh productivity post asks for planner fit | Rejected for this repo; notes/todo/planner category is crowded and status-quo pain is not sharp enough. |
| HostEnv Diff | Developers switching local/staging/client hosts-file environments → Sleezr, SideDNS, SwitchHosts, Gas Mask, manual /etc/hosts → incumbents already handle profiles and DNS helpers → CI-style hosts diff/review packet for teams → HN/local-dev search → recent Show HN products confirm pain | Held; real developer workflow, but new direct competitors already address much of the job. |
| RestoreDrill Lite | Small Postgres app owners needing proof backups restore → pgBackRest, Databasus, Restoredrill, scripts → many tools exist but setup can be heavy → one-command local restore evidence packet → HN/Postgres/selfhosted searches → recent Show HN backup-restore tools | Held/rejected for this run; backup-restore verification is important but already represented by prior lab ideas and direct tools. |

## Wedge

DrivePing is not a general Android network toolbox. It wins by treating the car/head-unit context as the product: one glance, one foreground notification or overlay, a few safe probe targets, and an exportable drop timeline that can be posted to a support thread or used to compare hotspot/router changes. The Android 12/15 foreground-service and boot restrictions become part of the setup checklist rather than a hidden failure mode.

## Kill condition

Reject or narrow if Ping Monitor On Status Bar or PingTools already provides boot-safe foreground ping plus DNS/gateway/HTTPS classification, car-scale overlay presets, and exportable drive-session drop logs on modern Android head units. Also reject if Android foreground-service and overlay restrictions make reliable car-head-unit behavior impossible without sideload-only permissions that normal users will not grant.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Intermittent head-unit connectivity wastes repeated troubleshooting time and can block navigation/media/work dashboards; the source asks for a very specific monitoring behavior. |
| Feasibility | 3/5 | The MVP is buildable with Android foreground services, notifications, overlays, and network probes, but boot/background restrictions and OEM battery policies add real implementation risk. |
| Demo potential | 4/5 | A demo can show simulated packet loss, notification/overlay state changes, and an exported drive-session incident packet. |
| Distribution | 4/5 | Specific channels exist: r/androidapps threads, XDA/head-unit forums, Android car stereo YouTube/search content, camper/RV hotspot communities, and direct replies to “status bar ping” searches. |
| Competitive wedge / timing | 3/5 | Direct competitors exist, including a status-bar ping app, but the car-head-unit drop-log packet and modern Android foreground-service setup niche is sharper than a generic ping utility. |
| Total | 18/25 | Clears repo threshold and both dimension gates, but the weakest dimensions are feasibility and competitive wedge/timing. |

## Decision

Create repo. DrivePing scored 18/25 with distribution 4/5 and competitive wedge/timing 3/5, so it clears the creation gates. Scaffold/spec snapshot was added under `projects/driveping`; no dedicated GitHub remote was created during this local-first run.

## Next build step

Build the first Android foreground-service spike: probe one HTTPS target every 5 seconds, render latency/loss in a persistent notification, simulate drops in an emulator or fake probe adapter, and export a local JSON drive-session log.

## Source access caveats

Reddit public JSON was blocked with `theme-beta`, and the run used `reddit-rss-fallback` for r/androidapps and r/productivity. Several subreddit RSS probes hit `HTTP 429`, so no Reddit scores/comment counts were used. X/Twitter `whoami` worked, but `xurl search` returned `401 Unauthorized`; no X posts were used and no social writes were attempted. Competitor validation used web search and original Android/Play documentation where available.
