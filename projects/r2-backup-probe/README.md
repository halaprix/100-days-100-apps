# R2 Backup Probe

A local-first CLI that diagnoses Duplicati + Cloudflare R2 backup connection failures before users keep retrying blind.

## Problem

Self-hosters use Duplicati with S3-compatible storage because it is convenient, encrypted, and cheap to restore from providers like Cloudflare R2. The failure mode is messy: Duplicati's connection test can pass, but the actual backup can fail later with S3 compatibility, TLS, endpoint, client-library, checksum, or unsupported-operation errors.

The current workflow is forum archaeology: export command lines, find the right advanced options, compare Duplicati AWS SDK versus Minio behavior, read Cloudflare R2 docs, run ad-hoc `rclone` checks, and paste logs into support threads.

## Target user

Self-hosters and small-office admins running Duplicati backups to Cloudflare R2 or another S3-compatible bucket who need a safe, explainable preflight before trusting the backup job.

## MVP

- `r2-backup-probe lint <duplicati-export>`: parse a Duplicati destination URL/export and flag R2-specific issues.
- `r2-backup-probe explain <log-file>`: match common Duplicati/R2 errors to likely causes and next checks.
- Optional live probe that writes and deletes a tiny test object using the user's explicit credentials.
- Redacted markdown report for forum/GitHub support threads.
- Preset checks for endpoint shape, TLS, `--s3-client=minio`, chunk encoding, bucket/path ambiguity, and unsupported S3 features.

## Non-goals

- No hosted dashboard or telemetry.
- No credential storage.
- No replacement for Duplicati, rclone, restic, or Cloudflare documentation.
- No automatic deletion outside the explicit tiny probe object.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1umvdih/duplicati_cloudflare_r2_test_connection_failed/ | Fresh user report: Duplicati Cloudflare R2 test connection failed with a confusing checksum-related error. |
| Duplicati docs | https://docs.duplicati.com/backup-destinations/standard-based-destinations/s3-compatible-destination | Duplicati S3-compatible docs say non-AWS providers may need `--s3-disable-chunk-encoding` or `--s3-client=minio`; defaults can be incompatible. |
| Duplicati forum | https://forum.duplicati.com/t/back-up-to-cloudflare-r2-storage-fails/15511 | Older but detailed thread shows "Connection worked" while backup fails, plus manual advice to inspect logs and try Minio/backend tools. |
| Duplicati GitHub | https://github.com/duplicati/duplicati/issues/4673 | Open R2 support issue documents endpoint/TLS/custom-server confusion and incomplete S3 compatibility. |
| Cloudflare R2 docs | https://developers.cloudflare.com/r2/platform/troubleshooting/ | R2 troubleshooting points users to curl/S3 signing checks and differentiates REST API tokens from S3-compatible API tokens. |
| Cloudflare R2 rclone docs | https://developers.cloudflare.com/r2/examples/rclone/ | `rclone` is a strong substitute for validating R2 credentials and object access, but not Duplicati-specific. |

## Status

v0.1.0-alpha.0 — scaffold/spec only.
