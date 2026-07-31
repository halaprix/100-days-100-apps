# SPEC — CpuFlag Gate

## User story

As a self-hoster running Docker workloads inside Proxmox VMs, I want a read-only CPU-feature preflight packet so that I can fix x86-64-v2/v3 workload crashes without blindly changing VM CPU settings.

## Core flow

1. User collects public-safe command outputs from the host and guest:
   - `lscpu` on the Proxmox host;
   - `lscpu` inside the VM;
   - `qm config <vmid>` with private names redacted;
   - optional container crash snippet such as `CPU does not support x86-64-v2`.
2. User runs `cpuflag-gate check --fixture examples/proxmox-kvm64-immich.json`.
3. Tool classifies host level, guest-exposed level, workload-required level, and risk.
4. Tool emits blockers, warnings, candidate CPU model settings, and verification commands.
5. User pastes the markdown packet into a change note before manually changing Proxmox settings.

## Data model

```yaml
scenario:
  name: proxmox-kvm64-immich
  environment:
    hypervisor: proxmox-ve
    live_migration_required: false
    vm_cpu_model: kvm64
  host_cpu:
    vendor: amd
    detected_level: x86-64-v3
    flags: [cx16, lahf_lm, popcnt, sse4_1, sse4_2, ssse3, avx, avx2]
  guest_cpu:
    detected_level: x86-64-v1
    flags: [lm, cmov, cx8, fpu, fxsr, mmx, syscall, sse2]
  workload:
    name: immich-ml
    required_level: x86-64-v2
    error: RuntimeError: NumPy was built with baseline optimizations X86_V2
  privacy:
    labels_use_reserved_domains: true
    example_domain: example.test
```

## Technical approach

- Language: Python 3.12 for a fast CLI scaffold.
- Inputs: YAML/JSON fixtures and saved command output files, not live system access.
- Rules:
  - map CPU flags to x86-64-v1/v2/v3/v4 levels;
  - detect guest level below workload level;
  - detect host capable but guest masked by Proxmox/QEMU model;
  - warn when suggested `host` passthrough conflicts with live migration;
  - suggest named models only as review candidates, not as automatic fixes.
- Output: deterministic markdown packet suitable for tests and public demos.

## Validation plan

- Fixture test: `kvm64` guest + v2 workload => blocker and candidate model note.
- Fixture test: guest and workload both v2+ => pass with no blocker.
- Fixture test: live migration required + `host` candidate => warning.
- Public-safety scan for secret markers, private domains, and private hostnames.
- Wedge validation: post a synthetic Immich/MySQL-style packet in self-hosting channels and measure whether users prefer it over raw `lscpu` snippets.

## Milestones

- v0.1.0-alpha.0 — repo scaffold.
- v0.1.0-alpha.1 — fixture parser and CPU-level classifier.
- v0.1.0-alpha.2 — markdown packet generator and scaffold tests.
- v0.2.0-alpha.1 — runnable demo with Immich/MySQL/Anaconda fixtures.
