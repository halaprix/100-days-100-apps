# SPEC — BayTrace

## User story

As a homelab operator with flaky Proxmox or Linux storage detection, I want a safe local diagnostic command so that I can identify whether the issue is likely controller, cable, drive, power sequencing, udev, or device naming before I create or import storage.

## Core flow

1. User boots the storage host and runs `baytrace scan --label boot-1`.
2. CLI collects read-only host facts:
   - block devices, serials, models, sizes, filesystems, mount state;
   - PCI storage controllers and kernel drivers;
   - SMART availability and selected health attributes when permitted;
   - recent kernel messages for ATA/SATA resets, link speed changes, I/O errors, and udev settle timeouts.
3. User optionally power-cycles or reseats one cable/bay and runs another labeled scan.
4. `baytrace compare boot-1 boot-2` flags unstable device presence, serial mismatches, controller resets, and unsafe assumptions.
5. `baytrace report` produces a redacted support bundle with findings, confidence, and next checks.

## Data model

```text
Scan
- id: stable scan id
- label: user supplied label
- captured_at: timestamp
- host: redacted OS/kernel summary
- controllers: Controller[]
- disks: Disk[]
- events: StorageEvent[]

Controller
- pci_id
- driver
- description
- risk_flags: cheap_multiplier | raid_mode | reset_spam | unknown

Disk
- kernel_name
- by_id_name
- serial_hash
- model
- size_bytes
- transport
- smart_available
- health_summary
- filesystem_summary

StorageEvent
- source: dmesg | udev | smartctl
- severity: info | warn | fail
- message_redacted
- evidence

Finding
- id
- severity
- title
- explanation
- suggested_next_step
- confidence
```

## Technical approach

- Language: Python for fast CLI iteration and easy Linux subprocess parsing.
- CLI: `argparse` first; graduate to Typer only if command complexity grows.
- Collection commands: `lsblk --json`, `lspci -nnk`, `udevadm settle --timeout=0`, `dmesg --ctime`, optional `smartctl -a`.
- Storage: local JSON scan files under a user-selected output directory; never upload data.
- Redaction: hash serial numbers by default, redact hostnames, and omit mount paths unless the user opts in.
- Safety: MVP is read-only. Any future destructive checks must require explicit flags and warnings.

## Validation plan

- Unit-test parsers with synthetic `lsblk`, `lspci`, `dmesg`, and `smartctl` fixtures.
- Add comparison fixtures for stable disks, missing disk, serial swap, controller reset spam, udev timeout, and SMART-unavailable devices.
- Run on a normal Linux VM to prove graceful degradation when no SATA hardware or SMART access is available.
- Validate wedge by manually sharing a synthetic redacted report in a self-hosted/Proxmox-style support context and checking whether it reduces follow-up questions.

## Milestones

- v0.1.0-alpha.0 — repo scaffold.
- v0.1.0-alpha.1 — CLI skeleton, scan file schema, and parser fixtures.
- v0.2.0-alpha.1 — compare/report workflow with redaction tests.
