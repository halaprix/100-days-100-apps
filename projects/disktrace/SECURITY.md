# Security Policy

## Supported versions

DiskTrace is experimental. Only the latest `main` branch and tagged alpha releases receive security fixes.

## Reporting a vulnerability

Open a GitHub security advisory or contact the maintainer through the repository owner profile. Do not publish exploit details or sensitive production incident data in public issues.

## Data handling

DiskTrace must not collect, upload, or store credentials, private hostnames, private IP addresses, real file shares, customer data, or real ProcMon/WPR/PerfMon traces in v0.

## Current safety boundary

v0 scope is read-only, fixture-driven packet generation. The tool may generate command templates and warnings, but it must not run live tracing, install tools, modify collector settings, or change services.
