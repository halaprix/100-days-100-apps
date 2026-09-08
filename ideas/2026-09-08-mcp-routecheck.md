# Day 075 — McpRouteCheck

Date: 2026-09-08
Status: repo-created

## One-line pitch

A local, read-only CLI that turns selected Atlassian Rovo MCP v1 configuration
files into a redacted v2 migration packet before the March 1, 2027 behavior
change breaks an agent connection.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Atlassian developer changelog | https://developer.atlassian.com/changelog/ | On September 8, Atlassian announced Rovo MCP v2 general availability, new products/tools, a new v2 endpoint, and the March 1, 2027 v1 behavior change. |
| Atlassian Rovo MCP v1-to-v2 upgrade guide | https://support.atlassian.com/atlassian-ai-gateway/docs/how-to-upgrade-from-atlassian-rovo-mcp-v1-to-atlassian-rovo-mcp-v2/ | Client-specific migration work includes plugin/connector replacement, reauthentication, cached-credential cleanup, and a separate gateway endpoint for flat tool exposure. |
| Atlassian Rovo MCP setup guide | https://support.atlassian.com/atlassian-ai-gateway/docs/get-started-with-the-atlassian-remote-mcp-server/ | Supported clients span desktop, CLI, IDE, and gateway modes; v2 can act across Jira, Confluence, Bitbucket, and other Atlassian products with the user's existing permissions. |
| Atlassian supported-tools reference | https://support.atlassian.com/atlassian-ai-gateway/docs/supported-tools/ | v2 uses discovery/execution paths and offers a paginated flat tool list for gateways, so endpoint replacement alone may not establish compatibility. |
| MCP Inspector | https://github.com/modelcontextprotocol/inspector | The official visual MCP-server testing tool is an established substitute and raises the bar: the wedge must be migration inventory, not generic protocol inspection. |

## Problem

Rovo MCP v2 is available now, but v1 use will begin exposing and using v2 tools
on March 1, 2027. An incompatible client may need credential-cache cleanup, a
new connector/plugin, reauthentication, or a different gateway tool-list mode.
A team with user-, project-, and gateway-scoped configurations can miss one
reference when following client documentation manually.

The status quo passes the pain test for teams that rely on an agent to reach
Jira, Confluence, or Bitbucket: a failed connection can block a work workflow,
and migration triage across scopes can take materially longer than 30 minutes.
This is not a claim that every single-connection user needs a separate tool;
for one known configuration, Atlassian's guide remains sufficient.

## Target user

An Atlassian administrator, MCP gateway operator, or developer-tooling maintainer
who owns more than one Rovo MCP v1 connection and needs a reviewable migration
plan before the v1-to-v2 behavior change.

## MVP scope

- Read explicit user-selected JSON and TOML configuration paths locally; never
  scan a machine automatically.
- Identify likely v1 Rovo endpoint references without copying headers, tokens,
  or credential-bearing fields to output.
- Classify client, scope, and gateway-mode signals; preserve ambiguous cases as
  `unknown` rather than guessing.
- Emit deterministic Markdown and JSON packets with affected connection labels,
  v2/gateway recommendations, reauthentication reminders, and manual checks.
- Offer a dry-run patch preview only. No config edits, browser launch,
  authentication, remote inventory, or Atlassian API calls in the MVP.

## Shortlist and wedge-first gate

1. **McpRouteCheck — selected.** Atlassian Rovo MCP v1 connection owner with
   multiple client/project/gateway configurations → Atlassian upgrade guides and
   MCP Inspector → the guides are authoritative but connection-by-connection,
   while the inspector tests a live server rather than inventorying local v1
   config → redacted, local, cross-file Rovo v2 migration packet → Atlassian
   developer changelog/upgrade searches plus targeted GitHub discussions for
   named supported clients → v2 is GA now and the March 1, 2027 v1 behavior
   change gives a concrete migration window. **Kill:** five multi-config
   operators complete a migration from the official guide in under 15 minutes
   without missing a scope, and none values an inventory receipt.
2. **HubSpot legacy-app migration linter — rejected.** HubSpot app maintainer →
   official migration guide and `hs app migrate` → the public guide already
   branches on app type, project version, serverless use, and install count;
   an MVP risks restating official decision logic → static migration checklist →
   HubSpot developer searches → current platform changes are real, but no fresh
   community pain or distinct first-user channel was found. **Kill:** weak
   wedge against vendor tooling and insufficient demand evidence.
3. **Production-only logging planner — rejected.** Web developer facing a bug
   that only reproduces in production → Sentry, Bugsnag, PostHog, structured
   logging, request IDs, and temporary log changes → these strong existing
   products/workflows already handle collection, while the fresh discussion
   supplied no narrow workflow that they fail → safer temporary logging recipe
   → generic web-development audience → generic observability is a crowded
   reject-by-default category. **Kill:** crowded category and no sharp wedge.
4. **Read-only audit mutation fence — rejected.** Consultant limited to a
   read-only code audit → sandboxing, git hooks, filesystem permissions, and
   manual `git status` → a fresh r/webdev report alleges a framework-created
   instruction file, but comments dispute its causality and no official
   Next.js corroboration was retrieved → command side-effect receipt →
   consultant/audit-contract searches → the claimed loss is unverified, making
   the evidence too weak for a daily winner. **Kill:** uncorroborated premise.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | MCP Inspector | Official visual tool for testing MCP servers. It is appropriate for protocol and tool-call debugging, but does not generate a local Rovo v1 inventory or client-specific migration receipt. |
| Direct competitor | Atlassian client-specific upgrade guides | The source of truth for individual clients. They do not provide one cross-file, redacted pre-change report for an operator's selected configurations. |
| Indirect substitute | Search configuration files and manually follow the upgrade guide | Works for one known connection, but can miss user/project/global scope, headers that require manual review, or gateway-specific tool-list behavior. |
| Status quo | Wait for an agent connection to fail or change behavior, then diagnose under time pressure | Can block workflows that use Jira, Confluence, or Bitbucket through the connection. |

## Wedge

McpRouteCheck does not try to replace MCP Inspector, build an MCP proxy, or
rewrite Atlassian's instructions. Its narrow job is to produce a safe,
reviewable migration inventory from explicit local configuration inputs before
an operator changes anything. That converts a vendor migration guide into an
approval-friendly packet across multiple scopes while avoiding credentials and
network access.

The distribution route is concrete: search-driven landing pages and release
notes for the Rovo v1-to-v2 transition, then targeted posts or replies in public
GitHub discussions for supported client integrations. The deadline is vendor-set,
the affected product is named, and the initial audience is identifiable rather
than a generic "MCP users" group.

## Kill condition

Stop or narrow McpRouteCheck if five operators with multiple Rovo MCP
configurations can complete the official migration in under 15 minutes without
missing a scope or needing a reviewable inventory. Also stop if real client
configuration formats put secrets in fields that cannot be safely excluded from
a deterministic report, or if MCP Inspector gains Rovo-specific multi-config
migration inventory.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | A failed connection can block work access; the value concentrates in multi-config teams, not one-off users. |
| Feasibility | 4/5 | Explicit-path JSON/TOML readers, safe finding records, and deterministic packets fit a 1–3 day CLI MVP; client-format coverage must remain conservative. |
| Demo potential | 5/5 | A mixed synthetic configuration set turning into a redacted affected-config packet and `unknown` findings is easy to show. |
| Distribution | 4/5 | Vendor changelog and exact migration searches point to named affected users, with repeatable GitHub/community follow-up around supported clients. |
| Competitive wedge / timing | 4/5 | The vendor-set v1-to-v2 transition and cross-file migration receipt are distinct from generic MCP testing and documentation, though official guides remain a strong substitute. |
| Total | 21/25 | Clears the 18-point threshold and both dimension gates. |

## Decision

**repo-created.** McpRouteCheck scores 21/25, with Distribution at 4/5 and
Competitive wedge / timing at 4/5. A local dedicated scaffold was created and
its public-safe snapshot is tracked at [`projects/mcp-routecheck`](../projects/mcp-routecheck/).
No dedicated GitHub remote was created or pushed.

## Next build step

Implement fixture-first v1/v2/gateway JSON and TOML readers that emit a single
redacted finding schema; prove in tests that header and credential values never
reach packet output.

## Source access caveats

Reddit public JSON was blocked with the documented `403` theme-beta response.
The read-only tool used RSS successfully for r/SideProject, r/selfhosted, and
r/webdev; its r/SaaS, r/sysadmin, r/androidapps, and r/productivity requests
then returned `429` and were not retried. RSS does not expose reliable score or
comment metadata, so this brief makes no engagement claim. Fresh Reddit signals
were used only to reject weak/crowded alternatives; the selected Rovo MCP
transition is supported by direct Atlassian documentation.

`xurl whoami` succeeded through the existing OAuth1/bearer setup, but the
read-only X search probe returned `401 Unauthorized` and the default profile had
no OAuth2 token. No X signal is used. Several general web-search queries returned
no results; direct extraction of Atlassian and MCP Inspector pages succeeded.
