# Agent Instructions — CpuFlag Gate

CpuFlag Gate is a read-only CPU-feature preflight packet generator for Proxmox/KVM VM workloads.

## Scope

- Keep v0 deterministic, fixture-driven, and read-only.
- Inputs are saved command outputs or synthetic fixtures, not live Proxmox access.
- Generate blockers, warnings, candidate settings, verification commands, and rollback notes.
- Treat Proxmox/QEMU/vendor docs as references; do not pretend generated packets were executed.

## Public safety

Do not commit:

- secrets, tokens, passwords, private keys, cookies, OAuth details, or service tokens;
- real hostnames, VM names, node names, IP addresses, tailscale names, or private infrastructure details;
- screenshots or dumps from a real Proxmox host unless fully sanitized;
- private support tickets or conversations.

Use synthetic labels and reserved domains such as `example.test`.

## Development workflow

- Use Beads for task tracking inside this repo.
- Use Conventional Commits.
- Add tests before changing classification or safety rules.
- Keep outputs deterministic and easy to diff.

## Safety boundary

CpuFlag Gate may generate human-reviewable CPU exposure summaries and candidate setting notes. It must not connect to Proxmox, SSH into hosts, or change VM configuration in v0.
