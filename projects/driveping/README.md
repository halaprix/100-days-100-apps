# DrivePing

DrivePing is a glanceable Android head-unit connectivity sentinel that shows live latency/loss while driving and exports a drop log after intermittent YouTube, maps, hotspot, or kiosk-network failures.

## Problem

Aftermarket Android car head units and kiosk-like Android tablets can report Wi-Fi or hotspot connectivity while apps still stall or say there is no network. Generic bandwidth meters only show traffic; they do not prove idle reachability, DNS health, latency, packet loss, or when the failure started.

## Target user

People running aftermarket Android car head units, camper/RV Android tablets, delivery-route dashboards, or kiosk-like Android devices that need safe, glanceable Internet health while another app is in front.

## MVP

- Foreground service with persistent notification showing target, latency, packet loss, and last drop time.
- Optional large overlay mode for head units where status-bar text is unavailable.
- Probe profiles for gateway, DNS resolver, and public HTTPS endpoint.
- Local JSON/CSV/Markdown drive-session export.
- Setup checklist for Android foreground-service, boot, and battery restrictions.

## Non-goals

- No background location collection.
- No cloud account, fleet dashboard, remote monitoring, ads, or analytics in the first slice.
- No packet capture, VPN interception, or inspection of user traffic.
- No promise that every OEM head unit permits boot auto-start or overlay behavior.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/androidapps | https://www.reddit.com/r/androidapps/comments/1vop3cb/looking_for_a_pinglatency_monitor_that_stays/ | Fresh user asks for continuous ping/latency in the Android status bar for an aftermarket car head unit. |
| Ping Monitor On Status Bar | https://play.google.com/store/apps/details?id=com.mrstudios.pingmonitorfree&hl=en | Existing app confirms demand and Android-version display limitations. |
| PingTools Network Utilities | https://play.google.com/store/apps/details?id=ua.com.streamsoft.pingtools&hl=en-US | Broad substitute for Android network troubleshooting. |
| Android foreground services | https://developer.android.com/develop/background-work/services/fgs | Documents the foreground-service primitive and visible notification model. |

## Current status

v0.1.0-alpha.0 — scaffold/spec only, consolidated in the 100-days master repo.
