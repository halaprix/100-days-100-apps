# McpRouteCheck

A local, read-only migration packet for Atlassian Rovo MCP v1 configurations
moving to v2.

## Problem

Atlassian Rovo MCP v2 is generally available. Existing v1 use will begin exposing
v2 tools on March 1, 2027; clients that cannot handle the change may need cached
`clientIds` or `.well-known` credentials cleared. Atlassian's migration guidance
varies by client and gateway mode, so teams can miss a scope-specific connection
or accidentally carry obsolete endpoint assumptions into a production agent.

## Target user

An Atlassian administrator, MCP gateway operator, or developer-tooling maintainer
who owns one or more v1 Rovo MCP connections and needs a reviewable migration
plan before the v1-to-v2 behavior change.

## MVP

- Read selected, user-provided MCP configuration files locally.
- Identify v1 Rovo endpoint references without printing credentials or headers.
- Classify client, scope, and gateway-mode signals with explicit `unknown`
  results when a config cannot be safely recognized.
- Generate a Markdown and JSON migration packet: affected configuration, v2
  endpoint recommendation, reauthentication/removal reminder, and a manual
  verification checklist.
- Offer a dry-run patch preview only; never edit configs, open a browser,
  authenticate, or call Atlassian APIs.

## Non-goals

- Not a generic MCP server inspector, proxy, or gateway.
- Not an OAuth/token manager or a remote configuration inventory service.
- Not an automatic migration tool and not a replacement for client-specific
  Atlassian instructions.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Atlassian Rovo MCP v1-to-v2 upgrade guide | https://support.atlassian.com/atlassian-ai-gateway/docs/how-to-upgrade-from-atlassian-rovo-mcp-v1-to-atlassian-rovo-mcp-v2/ | Atlassian says v1 usage will begin exposing v2 tools on March 1, 2027; separate client instructions cover plugin replacement, credential cleanup, reauthentication, and gateway tool exposure. |
| Atlassian Rovo MCP setup guide | https://support.atlassian.com/atlassian-ai-gateway/docs/get-started-with-the-atlassian-remote-mcp-server/ | The supported client list spans desktop, CLI, IDE, and gateway modes; the documented v2 endpoint and authentication flow differ by client. |
| Atlassian supported tools | https://support.atlassian.com/atlassian-ai-gateway/docs/supported-tools/ | v2 uses deferred tool discovery/execution and offers a paginated flat list for gateways, creating a concrete compatibility check beyond an endpoint string swap. |
| MCP Inspector | https://github.com/modelcontextprotocol/inspector | The official visual testing tool is a strong MCP-server testing substitute, but it does not produce a Rovo v1-to-v2 config inventory or client-specific migration packet. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | MCP Inspector | Tests MCP servers interactively. It remains the right tool for protocol and tool-call debugging, but it does not inventory local Rovo v1 references or map them to client-specific upgrade steps. |
| Direct competitor | Atlassian's client-specific migration guides | Authoritative instructions for each client. They solve one connection at a time but do not give an operator an offline, cross-file affected-config report. |
| Indirect substitute | Search configuration files, edit endpoint strings, and follow the web guide manually | Viable for one known connection, but easy to miss user/project/global scope, gateway settings, or a required reauthentication step. |
| Status quo | Wait for an agent connection to fail or change behavior, then debug client configuration under time pressure | The March 2027 switch can block agent access to Jira, Confluence, or Bitbucket workflows. |

## Wedge

McpRouteCheck is deliberately not another MCP runtime, proxy, or server tester.
It turns a selected set of local configuration files into a redacted Rovo-specific
migration receipt, flagging v1 references, unrecognized scopes, and gateway
requirements before an operator performs any change. The first channel is
concrete: Atlassian developer changelog and upgrade searches, plus GitHub issues
and discussions for users of named supported clients.

## Status

`v0.1.0-alpha.0` — local scaffold and specification only. No remote configured.
