# SPEC — QueryGap

## User story

As a self-hoster running AdGuard Home, I want a read-only reconciliation report for dashboard statistics versus query-log rows, so that I can understand mismatches without leaking private DNS activity into support threads.

## Core flow

1. User runs `querygap scan --fixture agh-buffered` for a demo or `querygap scan --querylog ./querylog.json --stats stats.json` against exported local files.
2. The CLI parses stats and query-log entries without making network calls by default.
3. It computes comparable windows and counters: total queries, blocked queries, unique domains, clients, and timestamp ranges.
4. It applies rules for known mismatch causes: buffering, retention, rotation, RAM-only logs, duplicate/unique counts, attribution, timezone/window drift, and stale plugin/UI versions.
5. It emits Markdown and JSON reports with redacted examples and safe next questions.

## Data model

```text
StatsSnapshot
- source: file | api | fixture
- generated_at: string
- window_start: optional string
- window_end: optional string
- total_queries: optional int
- blocked_queries: optional int
- top_clients: list<CounterItem>
- top_domains: list<CounterItem>

QueryLogSample
- source: file | api | fixture
- entries_seen: int
- window_start: optional string
- window_end: optional string
- blocked_entries: int
- unique_domains: int
- unique_clients: int
- rotation_detected: bool

Finding
- severity: info | warning | risk
- code: string
- message: string
- evidence: string
- recommendation: string

Report
- stats: StatsSnapshot
- querylog: QueryLogSample
- findings: list<Finding>
- redactions: list<string>
```

## Technical approach

- Start as a small Python CLI using only the standard library.
- Accept AdGuard query-log NDJSON/JSON streams and a simple stats JSON fixture.
- Keep rules in versioned JSON or Python data structures so behavior is reviewable.
- Redact domains, client names, and private/local network identifiers in human output by default.
- Provide fixture mode first so the demo and CI do not need a live AdGuard Home instance.
- Add optional authenticated local API collection only after offline parsing is safe and tested.

## Validation plan

- Unit-test fixture scans for query-log buffering, retention mismatch, timezone/window mismatch, RAM-only log loss, and unique-vs-total count confusion.
- Test redaction against private-looking domains, client names, and local network values.
- Run a CI smoke command that verifies the scaffold now and later runs the fixture scan.
- Validate wedge by posting a redacted fixture packet in self-hosted/AdGuard support contexts and checking whether users can map it to their mismatch.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and specification.
- v0.1.0-alpha.1 — fixture-driven CLI with Markdown/JSON output.
- v0.2.0-alpha.1 — offline query-log/stat parser with redaction tests.
- v0.3.0-alpha.1 — optional local API collector and support-packet templates.
