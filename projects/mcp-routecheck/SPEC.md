# McpRouteCheck specification

## User story

As an owner of Rovo MCP v1 configurations, I want a local, redacted migration
packet that names every affected configuration and its required next step, so I
can move to v2 without discovering a broken agent connection at the migration
boundary.

## Core flow

1. The user passes explicit file paths or directories; no automatic home-folder
   scan is performed.
2. McpRouteCheck reads supported JSON and TOML configuration shapes locally and
   identifies likely Rovo v1 connections without retaining secrets.
3. It classifies each occurrence as a client configuration, project configuration,
   or possible gateway configuration; ambiguous shapes stay `unknown`.
4. It renders a deterministic packet with location labels, a redacted endpoint
   finding, v2/gateway guidance, and a manual verification checklist.
5. An optional dry-run emits a proposed patch as output only. File writes require
   a later, separately designed command.

## Feature list

### MVP

- Explicit-path local discovery for JSON and TOML MCP configuration files.
- Structured recognition of Atlassian Rovo v1 endpoint forms.
- Header/token omission and redaction tests.
- Client/gateway classification with conservative unknown handling.
- Markdown and JSON migration packet output.
- Client-specific verification checklist: endpoint, plugin/connector replacement,
  reauthentication, and tool-discovery or flat-tool-list confirmation.

### Later

- Parsers for additional client configuration formats.
- A user-approved patch writer with atomic backups.
- CI check for repository-managed MCP configs.
- Optional authenticated runtime probe only after a separate security design.

## Data model

```json
{
  "packet_version": 1,
  "findings": [
    {
      "source_label": "project config",
      "format": "json",
      "scope": "project",
      "connection_name": "atlassian",
      "endpoint_state": "v1-detected",
      "auth_state": "redacted-or-not-inspected",
      "mode": "unknown",
      "recommendation": "review-v2-client-guide"
    }
  ],
  "summary": {"v1_detected": 1, "unknown": 0}
}
```

## Technical approach

Start as a small local CLI using parsers for JSON and TOML. It reads only
explicit inputs, produces deterministic output in a user-selected directory,
and has no HTTP client dependency. Credential-bearing fields are not copied to
reports, logs, or fixtures. Unsupported syntax is reported rather than guessed.

## Build plan

1. Add synthetic JSON/TOML fixtures: v1, v2, gateway, header-bearing, malformed,
   and unrelated MCP configuration cases.
2. Implement parser adapters and safe endpoint finding records.
3. Add client/gateway recommendation rules derived only from Atlassian's public
   migration documentation.
4. Render stable Markdown and JSON packets.
5. Add tests that prove no credential values reach output and no sockets open.
6. Validate the wedge with five operators who maintain Rovo MCP config in more
   than one scope. Stop if all can migrate confidently with the official guide
   in under 15 minutes and none values a cross-file receipt.

## Validation plan

- Unit-test recognition, unsupported-format behavior, scope classification, and
  redaction using synthetic data only.
- Verify no network dependencies or browser/process calls are present.
- Demo a mixed configuration set becoming a concise packet with an ambiguous
  finding preserved as `unknown`.
- Compare the packet with MCP Inspector and the official guide: it must add
  migration inventory and reviewability, not claim protocol validation.

## Milestones

- `v0.1.0-alpha.0` — scaffold and specification.
- `v0.1.0-alpha.1` — fixture-driven read-only CLI skeleton.
- `v0.2.0-alpha.1` — packet renderer and user validation spike.
