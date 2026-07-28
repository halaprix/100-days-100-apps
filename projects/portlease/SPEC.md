# SPEC — PortLease

## User story

As a self-hoster who discovers suspicious WAN access or wants to verify that UPnP is not silently exposing services, I want a read-only report of active router-created port mappings and likely owner devices, so that I can understand exposure before changing router settings or asking for help.

## Core flow

1. User runs `portlease scan` from a machine on the LAN.
2. PortLease discovers UPnP IGD and NAT-PMP/PCP-capable gateways.
3. PortLease queries active mappings without adding, deleting, or refreshing leases.
4. PortLease enriches internal hosts with local evidence:
   - internal IP,
   - MAC address if visible,
   - vendor prefix where available,
   - reverse DNS / mDNS hostname where available,
   - optional user labels from a local YAML file.
5. PortLease flags risky mappings and ambiguous evidence.
6. User exports:
   - terminal table,
   - Markdown incident report,
   - JSON for later comparison.

## Data model

```yaml
scan:
  scanned_at: datetime
  host:
    os: string
    interfaces:
      - name: string
        address: string
  gateways:
    - address: string
      protocol: upnp_igd|nat_pmp|pcp
      server: string|null
      mappings:
        - protocol: tcp|udp
          external_port: integer
          internal_host: string
          internal_port: integer
          description: string|null
          lease_seconds: integer|null
          remote_host: string|null
          risk_flags:
            - ssh_exposed
            - admin_ui_exposed
            - nas_ui_exposed
            - long_lived_mapping
            - unknown_owner
  hosts:
    - ip: string
      mac: string|null
      vendor: string|null
      hostname: string|null
      user_label: string|null
```

## Technical approach

- Start with Python for fast protocol/library iteration and easy packaging.
- Prefer existing protocol libraries where maintained; otherwise shell out to `upnpc` only as an optional fallback.
- Keep v0 strictly read-only. Any future remediation command must require an explicit `--apply` and separate bead/spec.
- Use Markdown templates for report output.
- Include fixture-based tests for mapping parsing and risk classification.
- Avoid storing private network details in public samples; all fixtures use RFC 5737 / RFC 1918 synthetic addresses.

## Risk rules

Initial rules should be transparent and source-linked where appropriate:

- TCP/22 to any internal host: `ssh_exposed`.
- TCP/80, 443, 8080, 8443 to likely NAS/admin host: `admin_ui_exposed` or `nas_ui_exposed`.
- TCP/3389, 5900: remote desktop exposure.
- Lease duration missing or longer than 24 hours: `long_lived_mapping`.
- Internal host cannot be identified by MAC/hostname/user label: `unknown_owner`.
- Mapping description is generic or blank: `weak_provenance`.

## Validation plan

- Unit-test parsers against captured/synthetic UPnP and NAT-PMP outputs.
- Run a local fixture demo that produces a report matching the UGREEN-style scenario without using real private data.
- Validate on at least one OpenWrt or miniupnpd test gateway before claiming hardware support.
- Compare output against raw `upnpc -l` to prove PortLease adds owner/risk/report value rather than hiding details.
- Kill or narrow if router diversity makes read-only mapping discovery unreliable across common self-hosted setups.

## Milestones

- v0.1.0-alpha.0 — repo scaffold.
- v0.1.0-alpha.1 — parser/risk engine with synthetic fixtures and Markdown report.
- v0.2.0-alpha.1 — live read-only UPnP IGD scan on one tested router class.
- v0.3.0-alpha.1 — NAT-PMP/PCP support and before/after diff report.
