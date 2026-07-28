# SPEC — BackupLocksmith

## User story

As a novice self-hoster or small-office admin locked out of a backup web console, I want a read-only recovery packet that identifies my install shape and safe next steps, so that I can regain administrative access without deleting backup metadata or exposing sensitive data.

## Core flow

1. Operator runs `backup-locksmith inspect` locally or against a synthetic fixture.
2. The tool detects likely UrBackup install mode: Linux package/systemd, Docker Compose/LinuxServer-style container, or Windows service.
3. It collects only non-secret facts: service/container name, listening port, likely config/data paths, version hints, and whether backup storage paths need an out-of-band snapshot before changes.
4. It emits a Markdown packet with:
   - summary and confidence,
   - blockers/warnings/info,
   - official reset references,
   - pre-reset capture checklist,
   - safe handoff notes for an experienced admin.
5. The operator uses the packet to follow official recovery docs or ask for help without posting private paths, hostnames, passwords, or backup contents.

## Data model

```yaml
Finding:
  id: string
  severity: blocker | warning | info
  title: string
  evidence: string
  recommendation: string
  source_url: string | null

InstallProfile:
  product: urbackup
  install_mode: linux-package | docker | windows-service | unknown
  version: string | null
  service_names: string[]
  container_names: string[]
  web_ports: integer[]
  config_path_hints: string[]
  backup_path_hints: string[]
  findings: Finding[]
```

## Technical approach

- Start as a Python CLI with no daemon and no network calls during inspection.
- Use fixture-driven development first so the demo is public-safe.
- Real host detection should be read-only:
  - `systemctl show`/service listing where available,
  - Docker metadata reads when Docker is present,
  - Windows service queries in a later platform-specific slice,
  - optional file-existence checks without reading backup contents.
- Emit Markdown and JSON so the packet can be attached to a support thread, change ticket, or email.
- Include a `--redact` mode that removes hostnames, usernames, private paths, and IP-like strings before sharing.

## Validation plan

- Unit-test synthetic Linux package, Docker, and Windows fixture profiles.
- Verify generated Markdown includes official references and never includes fixture passwords or secret-looking values.
- Run a public-safety scanner over fixture output before examples are committed.
- Validate demand by sharing the synthetic packet in self-hosted/UrBackup-adjacent contexts and checking whether operators ask for more products/install modes.
- Kill or narrow if official UrBackup tooling already provides a safe cross-platform recovery packet, or if real users say the problem is solved by a single obvious docs link.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and product spec.
- v0.1.0-alpha.1 — fixture-based CLI that emits a Markdown packet.
- v0.2.0-alpha.1 — read-only Linux package and Docker detectors.
- v0.3.0-alpha.1 — redaction checks and Windows service fixture support.
