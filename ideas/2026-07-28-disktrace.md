# Day 039 — DiskTrace

Date: 2026-07-28
Status: repo-created

## One-line pitch

A local-first Windows Server disk-I/O incident packet generator that turns ETW/WPR/ProcMon collection choices into a safe, bounded trace plan before an intermittent freeze happens again.

## Problem

Windows administrators sometimes inherit servers that become unresponsive or crash with no clear culprit. The obvious question is "which process and file were hammering disk right before the incident?" Built-in tools expose parts of the answer, but the safe production collection plan is awkward:

- Performance Monitor and `Get-Counter` can track disk and process counters, but not a clean process/PID/file-path correlation.
- Process Monitor can capture rich file-system events, but continuous capture can create massive logs and affect performance.
- WPR/ETW is powerful, but profile selection, ring-buffer limits, retention, and handoff instructions are easy to get wrong under pressure.

DiskTrace is not another always-on monitoring agent. It produces a conservative incident packet: what to collect, what not to collect, how to bound file size/overhead, and how to hand the resulting trace to support without leaking unnecessary details.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1v1bw09/what_is_the_safest_and_most_reliable_way_to/ | Fresh sysadmin thread asks for continuous Windows Server disk activity logging with timestamp, process/PID, drive/file path, read/write speed, total activity, response time, and automatic startup. |
| Microsoft Q&A | https://learn.microsoft.com/en-us/answers/questions/5947518/what-is-the-safest-and-most-reliable-way-to-contin | Same detailed need appeared as a public Microsoft Q&A question, showing the pain is not confined to one subreddit. |
| Microsoft Sysinternals Process Monitor | https://learn.microsoft.com/en-us/sysinternals/downloads/procmon | ProcMon captures real-time file system, registry, and process activity with powerful filters, boot logging, and large native logs; it is powerful but risky as naive continuous logging. |
| Microsoft Windows Performance Recorder | https://learn.microsoft.com/en-us/windows-hardware/test/wpt/windows-performance-recorder | WPR is ETW-based and designed for recording system/application events for WPA analysis, but requires profile and capture-mode decisions. |
| Microsoft `logman` docs | https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/logman | Windows already has command-line tooling for Event Trace Sessions and Performance Monitor logs; the gap is safe plan generation and correlation guidance. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Process Monitor / ProcMon | Best ad-hoc visibility into file/process activity. Not a safe unattended production capture planner by itself; bad filters can produce huge logs and overhead. |
| Direct competitor | Windows Performance Recorder / Windows Performance Analyzer | Strong ETW workflow for performance analysis. Powerful but profile-heavy, and many admins still need a bounded disk-incident recipe. |
| Direct competitor | PerfMon, Resource Monitor, Get-Counter, logman | Built in and scriptable. They expose counters well but do not directly answer process + PID + exact file path + disk latency in one safe incident packet. |
| Indirect substitute | Enterprise monitoring/APM/RMM tools | Mature monitoring platforms can show disk pressure and alerts, but often do not capture the exact file-path/process trace around a rare freeze. |
| Status quo | Run ProcMon manually, keep broad counters forever, ask Reddit/Microsoft Q&A, or wait for the next crash | Wastes incident time, risks massive logs/performance hit, and often misses the one pre-crash window that mattered. |

## Wedge-first gate

Windows Server sysadmin with intermittent disk freezes → ProcMon, WPR/WPA,
PerfMon/logman, or enterprise monitoring → raw tools either miss process + PID +
file-path correlation or can create oversized/high-overhead traces when left on
blindly → fixture-driven incident packet that chooses bounded collection modes,
stop conditions, and redaction notes before the next freeze → r/sysadmin,
Microsoft Q&A/search traffic for "ProcMon disk freeze" and "WPR disk I/O trace"
queries → fresh public support-style questions plus recurring older freeze/file
lock threads show admins still assemble this workflow manually.

## Wedge

DiskTrace is narrower than monitoring suites and safer than "just run ProcMon forever". The first version wins by producing a production-safe, read-only collection packet for one incident class: intermittent Windows Server disk stalls where the admin needs the last few minutes of attributable disk activity.

The useful wedge is not new telemetry. It is guardrails:

- choose a small capture goal before collecting anything,
- warn when requested fields imply high-overhead tracing,
- recommend ring-buffer/rotation boundaries,
- separate counter logging from file-path tracing,
- produce a shareable support packet with commands, assumptions, and redaction notes.

## Kill condition

Reject or narrow if Windows admins can already get a safe, bounded process/PID/file-path disk-incident packet from standard WPR/ProcMon templates in under 10 minutes, or if early validation shows the real need is full managed monitoring rather than pre-incident collection planning.

## Target user

- Windows Server sysadmins handling intermittent unresponsive/crash incidents.
- MSP/helpdesk engineers who need a repeatable intake packet before escalating storage/performance issues.
- Small IT teams without a dedicated performance engineer.

## MVP scope

- `disktrace plan --fixture examples/windows-disk-freeze.json` for a synthetic public-safe demo.
- JSON input model for incident symptoms, server role, VM/physical status, requested fields, retention window, and allowed overhead.
- Rule engine that emits `blocker`, `warning`, and `info` findings.
- Markdown packet export with a recommended PerfMon/logman + WPR/ProcMon approach, explicit overhead warnings, stop conditions, and redaction notes.
- No live collection, driver installation, credentials, private host data, or uploaded traces in v0.

## Non-goals

- Not an always-on monitoring platform.
- Not a replacement for ProcMon, WPR/WPA, PerfMon, enterprise APM, or storage vendor tooling.
- Not collecting real production traces in v0.
- Not storing credentials, file contents, private hostnames, private IPs, or customer data.

## Status

v0.1.0-alpha.0 — scaffold/spec only.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Rare freezes and disk storms are high-stakes incidents; the pain is episodic, but the status quo can waste hours and miss the only useful capture window. |
| Feasibility | 5/5 | v0 is deterministic fixture-mode planning and markdown export, not live collection or privileged tracing. |
| Demo potential | 4/5 | A synthetic incident fixture can produce a clear before/after packet with blockers, warnings, commands, stop conditions, and redaction guidance. |
| Distribution | 4/5 | Specific communities and search paths exist: r/sysadmin support threads, Microsoft Q&A-style questions, and SEO around ProcMon/WPR/logman disk-freeze workflows. |
| Competitive wedge / timing | 3/5 | Microsoft tools are strong, so the wedge is narrow: guardrails and bounded incident packets, not replacing ProcMon/WPR/PerfMon. |
| Total | 20/25 | Clears repo/snapshot threshold; weakest dimension is competitive wedge because incumbents already own the underlying telemetry. |


## Decision

Create the canonical project snapshot in the master repo: [projects/disktrace](../projects/disktrace).

No dedicated GitHub repo was configured locally, so there is no separate GitHub repository to remove for DiskTrace.

## Next build step

Implement deterministic fixture-mode packet generation and rule tests before adding any live collection guidance.
