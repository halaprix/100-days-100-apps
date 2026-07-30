# Security Policy

## Supported versions

PurgeBrake is pre-release. No production version is supported yet.

## Reporting a vulnerability

Open a GitHub issue in the parent 100-days index repo with a public-safe description. Do not include secrets, tenant names, customer identifiers, mailbox exports, message IDs, or real incident data.

## Safety boundary

PurgeBrake v0 must not connect to live email, tenant, eDiscovery, PhishRIP, Defender, Google Workspace, Proofpoint, Mimecast, SIEM, SOAR, or ticketing APIs. It only processes synthetic fixtures and emits review packets.
