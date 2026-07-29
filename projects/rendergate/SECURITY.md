# Security Policy

RenderGate is a planning tool. v0 must not apply live network, identity, tunnel, firewall, or SSH changes.

## Reporting a vulnerability

Open a private security advisory or contact the maintainer through the repository owner profile. Do not include real secrets, private hostnames, private IP addresses, tailnet data, tunnel tokens, or customer configuration in public issues.

## Public-safety boundary

Examples and tests must use synthetic labels only. The project should reject fixtures containing credentials, private addresses, real domains, or secret-like tokens.
