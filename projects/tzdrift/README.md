# TzDrift

Local-first timezone change readiness reports for sysadmins who need to know which servers, containers, and runtimes are carrying stale tzdata before a DST law change breaks schedules, logs, or billing windows.

## Problem

Civil time rules change for political reasons, sometimes with little operational lead time. A July 2026 sysadmin discussion about the Sunshine Protection Act asked how permanent Daylight Saving Time would affect workloads, and public reporting says the House passed a bill that would make Daylight Saving Time permanent.

The hard part for operators is not knowing that tzdata exists. It is quickly answering: which hosts and containers have stale timezone data, which Java/Python runtimes carry their own timezone database, which cron/systemd timers run in local time, and what should be patched before a maintenance window.

TzDrift is the narrow CLI for that moment: inventory timezone data versions and local-time schedulers, classify drift risk, and export a Markdown/CSV decision packet without changing any host configuration.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS fallback — r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1uwsl7e/thoughts_on_how_your_work_life_will_be_affected/ | Fresh sysadmin thread asks how work life changes if the Sunshine Protection Act becomes law. |
| Time | https://time.com/article/2026/07/14/daylight-saving-time-permanent-bill-house/ | Reports that the House passed a bill to make Daylight Saving Time permanent. |
| GovTrack | https://www.govtrack.us/congress/bills/119/hr139/text | Bill text amends federal time law by repealing the temporary daylight-saving period section and changing offsets. |
| IANA tz database | https://data.iana.org/time-zones/tz-link.html | The tz database is updated periodically as governments change time boundaries and daylight-saving rules, and is used across Linux, Android, databases, and other systems. |
| Oracle Java TZData versions | https://www.oracle.com/java/technologies/tzdata-versions.html | Java runtimes ship specific tzdata versions and may need TZUpdater or runtime upgrades separate from OS packages. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | OS package managers and patch dashboards | Show package status, but do not connect tzdata/JRE/container versions to local-time scheduler risk or produce an operator packet. |
| Direct competitor | Oracle TZUpdater / Java vendor docs | Useful for Java remediation, but scoped to JDK/JRE and not an environment-wide audit. |
| Direct competitor | Fleet management tools such as Ansible, Jamf, Intune, or vulnerability scanners | Can deploy updates or detect CVEs; timezone law readiness is not their default report shape and often requires custom scripts. |
| Indirect substitute | `zdump`, `timedatectl`, `dpkg -l tzdata`, `rpm -q tzdata`, Dockerfile inspection, custom shell scripts | Operators can stitch these together, but it is manual and inconsistent across distros, containers, and language runtimes. |
| Status quo | Wait for distro/vendor updates, patch everything, and handle broken cron/log/billing symptoms after the change | Reactive; wastes maintenance time and misses embedded runtime timezone databases. |

## Wedge

TzDrift is not a generic monitoring dashboard or patch manager. It is a read-only, event-driven readiness packet for timezone-law changes:

- collect OS tzdata versions across local manifests, SSH-supplied command output, or pasted package inventories,
- inspect container images and Dockerfiles for timezone package/version hints,
- detect Java runtime tzdata versions where possible,
- find local-time cron/systemd timers and risky scheduling patterns,
- compare findings against a bundled public rule file for known policy/timezone-change events,
- export a Markdown/CSV report with risk classes and manual remediation links.

The first-user path is concrete: r/sysadmin, SRE/devops blogs, and search traffic around "Sunshine Protection Act sysadmin", "tzdata update Java", and "permanent daylight saving time software" during legislative/news cycles.

## Target user

- Solo or small-team sysadmins managing mixed Linux servers and containers.
- SREs who need a quick preflight packet before a timezone/DST maintenance window.
- MSP operators who need a client-safe explanation without exposing host details publicly.

## MVP

- Cross-platform CLI, initially Linux/macOS.
- Local inventory mode for the current host: OS, tzdata package/version, timezone config, cron/systemd timers.
- Offline scan mode for pasted package lists, Dockerfiles, `docker inspect` JSON, and Java `tzupdater -V` output.
- Rules file for July 2026 Sunshine Protection Act readiness and general tzdata freshness checks.
- Markdown and CSV export with evidence links and manual next steps.
- Synthetic fixtures for demos and tests.

## Non-goals

- No legal, compliance, or employment advice.
- No automatic patching in v0.
- No credential storage, agent daemon, or hosted service.
- No claims that the tool predicts whether legislation will become law.
- No collection of real hostnames, private IPs, tenant names, or infrastructure dumps in public examples.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
