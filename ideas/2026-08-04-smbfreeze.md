# Day 046 — SmbFreeze

Date: 2026-08-04
Status: idea-only

## One-line pitch

A read-only Windows SMB incident-packet CLI that captures mapped-drive, Explorer, browser-download, ETW, and SMB client evidence before intermittent Windows 11 24H2/25H2 share hangs disappear.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vetbwl/smb_io_timeout_causing_explorer_shell_browser/ | Fresh admin report: after Windows 11 23H2 → 24H2, a mapped SMB share makes browser downloads sit at 100%, Explorer stops refreshing, SMB copies freeze, and restarting Explorer clears it temporarily. |
| Microsoft Learn — SMB troubleshooting | https://learn.microsoft.com/en-us/windows-server/storage/file-server/troubleshoot/troubleshooting-smb | Microsoft documents SMB troubleshooting as complex and recommends client/server traces, event logs, netsh packet capture, and good/bad traces for performance issues. |
| Microsoft Learn — Windows Performance Recorder | https://learn.microsoft.com/en-us/windows-hardware/test/wpt/windows-performance-recorder | WPR records ETW system/application events for WPA analysis, but it is a general-purpose capture tool rather than an SMB-incident packet generator. |
| Microsoft Learn — ETW | https://learn.microsoft.com/en-us/windows/win32/etw/about-event-tracing | ETW supports detailed production tracing without restarts and provides the substrate for focused capture, filtering, and summarization. |
| Microsoft Sysinternals — Process Monitor | https://learn.microsoft.com/en-us/sysinternals/downloads/procmon | ProcMon captures real-time file system, registry, process/thread activity with filters and stacks; powerful, but too broad for a repeatable SMB hang handoff packet. |

## Problem

Windows admins hit intermittent SMB/mapped-drive hangs where the visible symptom is not obviously "SMB is broken": browser downloads remain stuck at 100%, Explorer stops refreshing files, copies look frozen, and restarting Explorer clears the symptom before evidence is captured.

The status quo is painful because the admin must decide, during a live annoyance, which traces to run, how much data is safe to capture, which event logs matter, how to avoid private path leakage, and what to send to Microsoft/vendor/internal support. A single failed repro can waste more than 30 minutes, and a recurring file-share stall blocks user work.

## Target user

- Windows-heavy sysadmins supporting mapped drives and SMB shares after Windows 11 feature updates.
- Small MSPs that need a safe handoff packet before escalating intermittent Explorer or browser-download stalls.
- Internal IT generalists who can run PowerShell but do not live inside WPA, ProcMon, netsh trace, or SMB ETW providers every week.

## MVP scope

- `smbfreeze collect --mode safe --duration 90s --out packet.zip` PowerShell-first wrapper.
- Start/stop focused WPR/netsh/ETW sessions for SMB client, Explorer shell, file I/O, network, and relevant event logs.
- Capture non-sensitive environment facts: Windows build, SMB client config, mapped drive metadata with redacted server/share labels, Explorer process state, recent SMBClient events.
- Generate `packet.md` with timeline, collected artifacts, redaction summary, reproduction checklist, and suggested next diagnostics.
- Provide a fixture/demo mode with synthetic event logs and fake paths for public demos.
- No credential capture, no private hostnames/IPs in default output, and no automatic registry/GPO/protocol changes.

## Shortlist and wedge-first gate

| Candidate | Wedge-first gate | Result |
|---|---|---|
| SmbFreeze | Windows-heavy sysadmin debugging mapped-drive freezes → WPR/WPA, ProcMon, netsh trace, Event Viewer, vendor tickets → tools are powerful but fragmented and easy to run too late or with unsafe/private output → focused read-only SMB/Explorer hang packet with redaction and a good/bad trace checklist → r/sysadmin, Microsoft Learn/Q&A searches, MSP runbook content, reply-style diagnostics → fresh Windows 11 24H2/25H2 SMB hang report plus ongoing feature-update churn. | Winner, but held as idea-only because distribution is not yet strong enough for a repo. |
| PublicSurface Ledger | Self-hoster deciding what internal apps to expose publicly → Cloudflare Tunnel, reverse-proxy docs, nmap, Shodan, spreadsheets → existing tools show pieces but not a family-safe exposure decision log → local exposure inventory + risk labels before publishing a service → r/selfhosted and homelab hardening threads → fresh post asking where to draw the line on public services. | Rejected/narrow later: too close to prior PortLease/SplitPath/HeaderPass ideas unless scoped to a new workflow. |
| GameShotShelf | PC/console gamer archiving screenshots/videos → Immich, PhotoPrism, Playnite, folders, Steam library → photo apps are cumbersome for game/title tagging and video clips → self-hosted game-media gallery with import/tag-by-game conventions → r/selfhosted and game-preservation communities → fresh Immich-alternative request for game screenshots. | Held at 15/25: fun demo, but status-quo pain likely below the 30-min/week bar for most users. |
| KidVoice Room | Parent hosting cross-platform kid-safe voice chat → Discord, Mumble, TeamSpeak, Jitsi, Matrix/Element → incumbents either expose public/social surfaces, have echo/client friction, or need browser workarounds → private invite-only family gaming room with parent-readable setup checks → r/selfhosted parent threads and search content → fresh request after trying multiple options. | Held at 16/25: real safety need, but voice quality/mobile app delivery is too heavy for a 1–3 day MVP. |
| DNSReplica Packet | Sysadmin wanting Cloudflare as DNS source-of-truth with a secondary downstream provider → Cloudflare secondary DNS, DNSControl/octoDNS, registrar DNS, manual zone exports → existing options need plan/provider nuance and can silently drift → read-only zone export/diff packet for secondary-DNS readiness → r/sysadmin, Cloudflare/DNSSEC/PowerDMARC searches → fresh public-DNS redundancy question. | Held at 17/25: useful, but direct competitors and provider-native secondary DNS weaken the wedge. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Windows Performance Recorder / Windows Performance Analyzer | Authoritative ETW capture and analysis tools. They are broad; SmbFreeze would package a narrow SMB/Explorer/download hang profile and handoff summary. |
| Direct competitor | Microsoft SMB troubleshooting runbooks, netsh trace, Event Viewer | Microsoft already documents trace and event-log collection. The gap is repeatability, redaction, and incident-packet assembly for generalist admins. |
| Direct competitor | Sysinternals Process Monitor | Excellent for file/process activity and stack capture, but noisy and manual; it does not explain which SMB/Explorer facts to collect for this incident class. |
| Indirect substitute | PowerShell snippets, Wireshark, support ticket checklists, screenshots, user screen recordings | Free and familiar, but inconsistent. They often miss the short window while the hang is happening or leak private path/server details. |
| Status quo | Admin restarts Explorer, closes the mapped-drive window, retries the download/copy, then waits for the next hang to reproduce with better tooling ready | Tolerable once; costly when recurring because the symptom clears before evidence is packaged. |

## Wedge-first gate

Windows-heavy sysadmin debugging mapped-drive freezes → WPR/WPA, ProcMon, netsh trace, Event Viewer, vendor tickets → tools are powerful but fragmented and easy to run too late or with unsafe/private output → focused read-only SMB/Explorer hang packet with redaction and a good/bad trace checklist → r/sysadmin, Microsoft Learn/Q&A searches, MSP runbook content, reply-style diagnostics → fresh Windows 11 24H2/25H2 SMB hang report plus ongoing feature-update churn.

## Wedge

SmbFreeze should not compete with WPR, ProcMon, or Microsoft docs as a general troubleshooting platform. It wins only at the narrow moment when an admin sees an SMB/mapped-drive stall and needs to preserve a safe, comparable packet before restarting Explorer or changing random SMB settings.

The narrow v0 wedge:

- one command starts the right trace/event-log bundle;
- default output redacts server/share/path labels;
- the packet separates observed symptom, collected evidence, and next diagnostics;
- fixture mode makes the problem demoable without real infrastructure;
- no live remediation, registry edits, GPO changes, or protocol toggles.

## Kill condition

Reject or narrow if validation shows admins already have an internal WPR/ProcMon runbook that takes less than 10 minutes to execute and sanitize, if Microsoft publishes a dedicated SMB/Explorer hang collector covering the same workflow, or if the first-user channel only wants one-off registry/SMB setting fixes rather than evidence packets.

## Non-goals

- Not an SMB optimizer or registry-tweak recommender.
- Not an automated fix for Windows 11 24H2/25H2 behavior.
- Not a Wireshark/WPA replacement.
- Not a live agent that watches user machines continuously.
- Not collecting credentials, full uncensored paths, private hostnames, private IPs, or user files.

## Source access caveats

Reddit public JSON was blocked with `HTTP 403 theme-beta`, so Reddit collection used the bundled public RSS fallback for r/sysadmin and r/selfhosted. Fetching the full Reddit comment thread for the winning post was blocked by the same 403 response. Some additional subreddit RSS probes returned `HTTP 429`, so the shortlist leaned on the successful RSS results plus public Microsoft documentation. X `whoami` worked, but X search returned `401 Unauthorized`; no X search evidence was used. Web-search fallback returned sparse/empty results for exact SMB queries, so competitor checks used directly fetched public documentation pages.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Recurring SMB/Explorer stalls waste incident time and block user work, but public evidence is currently one strong fresh thread plus docs rather than repeated posts. |
| Feasibility | 5/5 | v0 is mostly PowerShell orchestration, ETW/netsh/event-log collection, redaction, and markdown generation with fixture tests. |
| Demo potential | 4/5 | Synthetic event logs and a before/after `packet.md` make a clear terminal/GIF demo. Real trace analysis can wait. |
| Distribution | 3/5 | r/sysadmin, MSP runbooks, and search content are specific, but the repeatable first-user path needs more proof before repo creation. |
| Competitive wedge / timing | 3/5 | The packet/redaction wedge is credible, but WPR, ProcMon, netsh, and Microsoft docs are strong substitutes. Feature-update timing helps. |
| Total | 19/25 | Clears total threshold, but fails the distribution gate for repo creation. |

## Decision

Save as `idea-only`. Do not create a repo today: total score clears 18/25, but Distribution is only 3/5 and the public evidence base is not yet broad enough to justify another project snapshot.

## Next build step

Run a focused validation spike: search Microsoft Learn/Q&A, Reddit, and MSP blogs for at least five independent Windows 11 24H2/25H2 mapped-drive or Explorer SMB hang reports, then draft the exact PowerShell collection profile and redaction contract if the pattern repeats.
