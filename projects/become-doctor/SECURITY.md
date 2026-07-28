# Security Policy

## Supported versions

BecomeDoctor is pre-alpha. No production support guarantee exists yet.

## Reporting a vulnerability

Open a GitHub security advisory or a private report if the repository supports it. Do not post secrets, private inventories, hostnames, IP addresses, or command logs in public issues.

## Safety model

- The MVP must not store credentials.
- Reports must redact hostnames, usernames, IPs, full paths, inventory group names, and full command lines by default.
- Remote probing must be explicit and no-op.
- The tool must not automatically install packages, edit sudoers, change Ansible configuration, or mutate remote hosts.
