# SPEC — LabFit

## User story

As a self-hoster with a small Proxmox box and a NAS, I want a fast placement report for my desired services, so that I can decide what runs where before I spend a weekend rebuilding the stack.

## Core flow

1. User copies an example YAML inventory and edits hardware plus desired services.
2. User runs `labfit plan homelab.yml`.
3. LabFit validates the inventory, expands each desired service into resource and placement constraints, and scores placement options.
4. LabFit prints a Markdown report with a recommended layout, rejected alternatives, risk warnings, and questions to ask before deployment.
5. User saves the report or pastes the public-safe version into a forum thread for review.

## Initial CLI shape

```bash
labfit examples list
labfit plan examples/jellyfin-arr-nas.yml
labfit explain storage-locality
labfit catalog services
```

## Data model

```text
HomelabInventory
- hosts[]
- storage[]
- network_links[]
- desired_services[]
- constraints[]

Host
- name: local alias only
- role: proxmox | nas | desktop | mini_pc | other
- cpu_class
- ram_gb
- gpu: none | intel_quicksync | nvidia | amd | unknown
- disks[]
- notes[]

ServiceIntent
- name
- priority: must_have | nice_to_have
- data_profile: media | documents | secrets | config | ephemeral
- exposure: local_only | family_remote | public
- resource_profile

Finding
- severity: info | warning | high
- title
- evidence[]
- recommendation[]
- rejected_alternatives[]
```

## Technical approach

- Language: Python CLI with `argparse` first; keep dependencies minimal for alpha.1.
- Inventory: YAML input with examples; schema validation with clear error messages.
- Rules: versioned JSON/YAML catalog for services and placement constraints.
- Output: Markdown report plus `--json` for future UI use.
- Tests: fixture-backed rules tests; no private network or privileged CI needed.

## Validation plan

- Encode the three source scenarios as fixtures and confirm the report explains the same decision pressure.
- Compare output against public substitutes: HLBuilder, server sizing calculators, Proxmox helper scripts, and common self-hosted guides.
- Share a static sample report in r/selfhosted-style discussions and check whether users would paste it instead of writing a long hardware inventory by hand.
- Kill or narrow if users mainly want one-click deployment scripts rather than placement decision support.

## Privacy and safety

- Do not collect telemetry.
- Do not scan a live network in the MVP.
- Redact or avoid hostnames, IPs, usernames, share paths, and private URLs in public reports.
- Keep example inventories fictional.

## Milestones

- v0.1.0-alpha.0 — repo scaffold.
- v0.1.0-alpha.1 — fixture-backed rules engine and first Markdown report.
- v0.2.0-alpha.1 — expanded service catalog and JSON output.
- v0.3.0-alpha.1 — optional static web demo using only sample inventories.
