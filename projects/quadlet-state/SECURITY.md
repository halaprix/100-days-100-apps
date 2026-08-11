# Security

QuadletState is scaffold/spec only. Do not use it to manage live services yet.

## Reporting

Open a GitHub issue in the parent 100-days index or contact the maintainer through the public repository profile.

## Scope

- Inline secrets in inventories.
- Accidental leakage of `.env` contents or private host details.
- Unsafe future apply behavior that could modify systemd or Podman state without a clear plan.

## Out of scope

- Vulnerabilities in Podman, systemd, Docker Compose, Nix, or Ansible.
- Support for private infrastructure debugging through public issues.
