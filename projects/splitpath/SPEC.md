# SPEC — SplitPath

## User story

As a self-hoster running Caddy or Nginx Proxy Manager behind a private overlay network, I want a read-only diagnostic packet for split-DNS and reverse-proxy access, so that I can fix private hostname routing without exposing services publicly or pasting sensitive config into forum threads.

## Core flow

1. User runs `splitpath probe service.example.com --lan-ip <expected-private-ip> --overlay-dns <optional-resolver-ip>`.
2. The CLI captures public DNS answers, OS resolver answers, optional resolver-specific answers, TCP reachability, TLS/SNI certificate metadata, and HTTP status/header basics.
3. The CLI classifies the failure class and writes a public-safe markdown/JSON packet with redacted local details and next-step suggestions.
4. User shares the packet in a support thread or uses it locally to decide whether the fix belongs in split DNS, reverse-proxy binding, TLS/SNI, or overlay routing.

## Data model

```json
{
  "target_host": "service.example.com",
  "expected_private_ip": "redacted-or-user-provided",
  "dns": {
    "public": [{"resolver": "system-public", "answers": []}],
    "system": {"answers": [], "source": "os-resolver"},
    "overlay": {"resolver": "optional", "answers": []}
  },
  "reachability": {
    "tcp_443": "pass|fail|skipped",
    "http_status": 0,
    "tls_subject": "redacted",
    "sni_ok": true
  },
  "classification": "missing-split-dns|public-only-dns|proxy-bind-mismatch|tls-sni-mismatch|unknown",
  "recommendations": []
}
```

## Technical approach

- Language: Python CLI first, using only standard library where practical.
- Commands: `probe`, `render`, and `doctor-fixture`.
- DNS checks: shell out to portable resolver tools when present (`dig`, `nslookup`, `getent`) and degrade gracefully when unavailable.
- HTTP/TLS checks: Python `socket`, `ssl`, and `http.client`; keep request bodies out of packets.
- Privacy: redact private addresses by default in public markdown unless the user passes `--show-private`.
- Packaging: start with a simple CLI module and fixture tests; defer publishing.

## Validation plan

- Unit-test classification rules with fixtures for:
  - public DNS points at public proxy but private overlay should be used,
  - system resolver returns public IP while overlay resolver returns private IP,
  - DNS is correct but reverse proxy is not reachable on overlay path,
  - TLS certificate/SNI mismatch,
  - all checks pass.
- Run a local fixture demo that produces a markdown packet without contacting real private infrastructure.
- Validate wedge by answering 3-5 support threads/searches where users combine Caddy/NPM, Cloudflare DNS, Tailscale/NetBird, and private hostnames.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and product spec.
- v0.1.0-alpha.1 — runnable `splitpath probe` skeleton with fixture mode.
- v0.2.0-alpha.1 — real DNS/TLS probes plus markdown packet output.
