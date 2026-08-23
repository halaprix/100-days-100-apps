# ChainBreak SPEC

## User story

As a remote-site IT operator, I want a local pre-change report showing whether my declared console, power, and alternate-access routes traverse the component I am about to restart, so that I can stop a circular recovery plan before it creates downtime or travel.

## Feature list

### MVP

1. Read a local YAML inventory of components, endpoint types, and directed dependency edges.
2. Accept a planned change target and one or more declared recovery goals.
3. Find recovery paths from operator entry points to each goal after excluding the change target.
4. Flag goals with no independent path, paths that traverse the target, and missing required assumptions.
5. Render a deterministic Markdown packet with a stop/review banner, evidence table, path trace, limitations, and human checklist.
6. Ship only synthetic fixtures and no network client.

### Later

- CSV and NetBox export adapters that remain offline and explicit.
- Optional graph visualization for the generated packet.
- Policy presets for one-person remote sites and change approval templates.
- CI-friendly JSON and SARIF-style output.

## Data model

```yaml
components:
  - id: vpn-gateway
    kind: vpn
  - id: management-console
    kind: console
  - id: alternate-jump-host
    kind: jump-host
recovery_goals:
  - management-console
edges:
  - from: operator-internet
    to: vpn-gateway
  - from: vpn-gateway
    to: management-console
  - from: operator-internet
    to: alternate-jump-host
  - from: alternate-jump-host
    to: management-console
```

The MVP accepts only the explicit `edges` key and should reject unknown keys rather than silently inventing topology.

## Build plan

1. Define a small schema and two synthetic fixtures: a circular VPN-to-console path and an independent alternate route.
2. Implement directed path analysis that removes the planned change target before testing each recovery goal.
3. Render a Markdown packet that exposes the exact edges used and all unverified assumptions.
4. Add golden-output tests and a public-safety/scaffold verifier.
5. Ask two remote-site operators to compare the packet with their current map/runbook before adding adapters.

## Validation plan

- Unit-test that a console reachable only through the target receives a stop/review finding.
- Unit-test that an alternate route produces a qualified pass while retaining its declared-assumption disclaimer.
- Verify the CLI opens no sockets, reads no credentials, performs no discovery, and does not control devices.
- Demo with synthetic `example.test` component names only.
- Reject or narrow if operators can produce the same per-change independent-recovery verdict from existing tools in under 10 minutes, or decline to maintain the minimal dependency input.
