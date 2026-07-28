# Security

LabFit should remain local-first and public-safe.

## Supported versions

Only the latest pre-1.0 alpha is supported during incubation.

## Reporting

Open a GitHub issue for non-sensitive bugs. For sensitive reports, do not paste secrets, private hostnames, IPs, or inventory files into public issues.

## Scope

In scope:

- Leaks of private inventory details in generated reports.
- Unsafe defaults that encourage exposing services publicly without warnings.
- Bugs that could cause LabFit to collect or transmit local data.

Out of scope for the scaffold:

- Vulnerabilities in Proxmox, NAS operating systems, Docker, or the services mentioned in examples.
- Attacks requiring modified local fixtures under the attacker's control.
