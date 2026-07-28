# Security Policy

## Supported versions

SplitPath is pre-release. Security fixes apply to the latest alpha tag.

## Reporting a vulnerability

Open a GitHub security advisory or a minimal public issue that does not include secrets or private infrastructure details.

## Diagnostic safety

The MVP must remain read-only. It may inspect DNS, TCP, TLS, and HTTP metadata for a user-provided hostname, but it must not change DNS records, reverse-proxy config, firewall rules, router settings, overlay-network settings, or cloud-provider settings.

Diagnostic packets should redact private network details by default and avoid request bodies.
