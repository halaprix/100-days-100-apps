# QueryGap

Read-only CLI that reconciles AdGuard Home dashboard statistics with raw query logs and explains likely config, retention, buffering, or client-attribution gaps before self-hosters chase phantom DNS issues.

## Problem

AdGuard Home exposes dashboard statistics and query-log rows, but those two views can disagree. A self-hoster may see hundreds of blocked queries in the dashboard while the query log appears to show a different count, or malware/phishing events can disappear before the user investigates them.

The painful part is not DNS theory. It is the support loop: eyeballing UI counters, Ctrl+F-ing logs, searching GitHub discussions, and sharing screenshots or config snippets that may leak private network behavior.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1v5x9zu/adguard_home_dashboard_and_query_log_inconsistent/ | Fresh AdGuard Home Docker user saw dashboard blocked-query counts disagree with query-log counts and asked whether the config was wrong. |
| AdGuard Home GitHub discussion | https://github.com/AdguardTeam/AdGuardHome/discussions/5653 | Maintainer says raw query logs live in `data/querylog.json` / `.1`, the format is not stable, and users continue asking about missing blocked entries. |
| GL.iNet forum | https://forum.gl-inet.com/t/adguard-home-dns-query-log-issues/50768 | Router users report query logs disappearing quickly; answer notes RAM-only defaults and storage-wear tradeoffs. |
| Grafana dashboard / exporter | https://grafana.com/grafana/dashboards/23579-adguard-metrics-statistics/ | Existing AdGuard exporter uses `/control/stats` and `/control/querylog`, proving APIs exist but current substitutes skew toward ongoing dashboards. |
| GitHub / DNSQueryAnalyzer | https://github.com/lopperman/AdGuardHome_DNSQueryAnalyzer | Existing DuckDB analyzer documents query-log buffering and rotation, validating the underlying failure mode. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | AdGuard Home dashboard and query-log UI | Authoritative for normal use, but it does not explain why two views disagree or create a safe diagnostic packet. |
| Direct competitor | AdGuard Exporter + Grafana dashboards | Strong for monitoring; heavy for a one-off reconciliation question. |
| Direct competitor | AdGuardHome_DNSQueryAnalyzer | More powerful long-term analysis with DuckDB and a web dashboard. QueryGap stays narrower: offline reconciliation and support-safe explanation. |
| Indirect substitute | `jq`, Ctrl+F, screenshots, router forums, GitHub discussions | Flexible but error-prone and easy to overshare. |
| Status quo | Keep tweaking settings or paste screenshots/config snippets into support threads | Eventually works, but wastes time and can expose private domains, client names, or host details. |

## Wedge

QueryGap is not another DNS analytics dashboard. It is a one-shot, privacy-safe reconciliation packet: compare a stats snapshot with query-log rows, identify likely reasons for gaps, and produce a small report that says what was checked without leaking private domains or client identifiers.

## Target user

Self-hosters running AdGuard Home on Docker, routers, OPNsense plugins, Home Assistant add-ons, or small servers.

## MVP

- `querygap scan --fixture agh-buffered` demo mode with synthetic stats/query-log fixtures.
- `querygap scan --querylog ./querylog.json --stats stats.json` for offline reconciliation.
- Rules for buffering, retention, rotation, RAM-only logs, duplicate/unique counts, client attribution, timezone/window mismatch, and stale UI/plugin versions.
- Markdown and JSON output with redaction notes and safe support-thread questions.
- Optional local API mode later; no network calls by default.

## Non-goals

- Not replacing AdGuard Home.
- Not becoming a full DNS analytics dashboard.
- Not transmitting DNS logs to a remote service.
- Not storing private domains, client names, or local network details.
- Not changing AdGuard Home configuration automatically.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
