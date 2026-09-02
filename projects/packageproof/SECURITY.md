# Security Policy

## Reporting

Do not include credentials, APKs, signing keys, certificate fingerprints, or
private release metadata in public issues. Report a suspected vulnerability
privately to the maintainer with a minimal synthetic reproduction.

## Security boundary

PackageProof must not read keystores, submit data to Android/Google consoles,
or send artifact metadata over the network. A local preflight cannot prove
registration, authorization, or installability.
