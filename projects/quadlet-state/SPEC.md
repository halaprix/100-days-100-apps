# SPEC — QuadletState

## User story

As a self-hoster running Podman Quadlets, I want to describe my desired container end state in one small inventory and preview generated unit-file changes, so that I can keep dotfiles reviewable without hand-writing every Quadlet unit.

## Core flow

1. User writes `quadlet-state.yml` with pods, containers, networks, volumes, env-file labels, and dependencies.
2. User runs `quadlet-state plan --inventory examples/quadlet-state.yml --existing ./quadlets --out ./generated`.
3. Tool validates the inventory and refuses unsafe inputs such as inline secrets.
4. Tool writes deterministic generated Quadlet files to the output directory.
5. Tool prints a plan: create, update, unchanged, and delete candidates.
6. User reviews the generated files and manually copies/applies them in v0.1.

## Data model

```text
Inventory
  version: string
  rootless: bool
  networks: [Network]
  volumes: [Volume]
  pods: [Pod]
  containers: [Container]

Pod
  name: string
  networks: [name]
  containers: [ContainerRef]

Container
  name: string
  image: string
  pod: optional name
  ports: [string]
  volumes: [mount]
  env_files: [label/path]
  after: [systemd unit]
  wants: [systemd unit]
```

No `.env` file content is read or copied. Paths in examples must be placeholders.

## Technical approach

- Start as a Python CLI with `argparse`, `dataclasses`, and PyYAML or a tiny strict parser.
- Render Quadlet unit files through small string templates sorted by stable keys.
- Keep output colorless and deterministic for copy/paste into support threads and CI logs.
- Build the first verifier around fixture parsing and required scaffold files.

## Validation plan

- Fixture inventory generates expected `.pod`, `.container`, `.network`, and `.volume` text.
- Diff mode detects added/changed/unchanged files against a fixture directory.
- Secret guard rejects values that look like inline tokens or passwords in `environment` fields.
- Competitive validation: compare against Podlet and quadlet-nix on setup time for the same Immich-shaped example; keep QuadletState only if the plain YAML + diff story is materially simpler for non-Nix users.

## Milestones

- v0.1.0-alpha.0 — scaffold/spec only.
- v0.1.0-alpha.1 — parse fixture inventory and render deterministic Quadlet files.
- v0.1.0-alpha.2 — add existing-directory diff and public-safe plan output.
- v0.2.0-alpha.1 — package as a local CLI with fixture tests and a short demo GIF.
