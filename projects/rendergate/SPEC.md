# SPEC — RenderGate

## User story

As a self-hoster with a GPU render workstation, I want a least-privilege access packet for one outside collaborator, so that they can trigger the intended job workflow without receiving broad access to the rest of my network.

## Core flow

1. User chooses an access stack: Tailscale, Cloudflare Access/Tunnel, SSH-only, or generic checklist.
2. User fills a public-safe access request fixture: collaborator label, target host label, service type, ports, allowed paths, expiration, and handoff method.
3. RenderGate evaluates the fixture against deterministic rules.
4. RenderGate emits blockers, warnings, generated snippets, acceptance tests, rollback steps, and redaction notes.
5. User manually applies the chosen policy in their real tool and runs the tests.

## Data model

```json
{
  "scenario": "render-coworker-access",
  "stack": "tailscale|cloudflare-access|ssh-only|generic",
  "collaborator": { "label": "external-editor", "expires_at": "2026-08-15" },
  "target": { "label": "render-box", "services": [{ "name": "job-api", "proto": "tcp", "port": 8080 }] },
  "constraints": {
    "allow_lan_subnet": false,
    "allow_admin_shell": false,
    "allow_file_drop": true,
    "require_rollback": true,
    "require_origin_protection": true
  }
}
```

All labels are synthetic. v0 examples must not contain real IP addresses, domains, hostnames, usernames, or keys.

## Technical approach

- Language: TypeScript or Python CLI, decided during alpha.1.
- Deterministic fixture parser and rules first; no live API calls.
- Rule categories: `blocker`, `warning`, `info`, and `snippet`.
- Output: Markdown packet and JSON findings.
- Include provider-specific snippets only as templates with placeholders.

## Validation plan

- Unit tests for fixture parsing and rule severity.
- Snapshot tests for Markdown output.
- Negative fixtures for common unsafe requests:
  - broad subnet route requested;
  - shared admin shell requested;
  - public hostname without origin token validation;
  - no expiration or rollback;
  - wildcard destination or all-ports access.
- Public-safety verifier that rejects private IPs, credentials, real-looking domains, and secret-like tokens in fixtures/docs.

## Milestones

- v0.1.0-alpha.0 — scaffold/spec snapshot.
- v0.1.0-alpha.1 — fixture parser, rule engine skeleton, sample packet.
- v0.2.0-alpha.1 — provider-specific snippets and acceptance-test checklist.
