# Security Policy

Report security issues privately via GitHub Security Advisories when available.

## Scope

CpuFlag Gate is intended to work from public-safe fixtures and saved command outputs. It must not store secrets, private infrastructure details, real hostnames, IP addresses, SSH keys, Proxmox API tokens, or unsanitized support data.

## v0 safety boundary

The v0 tool is read-only and must not connect to Proxmox, SSH into hosts, or modify VM settings.
