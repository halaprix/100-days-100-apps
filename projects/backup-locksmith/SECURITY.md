# Security Policy

## Supported versions

BackupLocksmith is experimental. Only the latest `main` branch and tagged alpha releases receive security fixes.

## Reporting a vulnerability

Open a GitHub security advisory or contact the maintainer through the repository owner profile. Do not publish exploit details or sensitive backup-system data in public issues.

## Data handling

BackupLocksmith should not collect passwords, backup contents, tokens, private hostnames, private IP addresses, or customer data. If a future detector needs to inspect local state, it must document exactly which non-secret metadata it reads and must provide redaction before shareable output.

## Current safety boundary

v0 scope is read-only packet generation. The tool must not modify UrBackup configuration, databases, containers, services, or backup storage.
