# R2 Backup Probe Specification

## User story

As a self-hoster running Duplicati backups to Cloudflare R2, I want a local preflight that explains why my Duplicati/R2 configuration or logs fail, so I can fix the backup before trusting it with real data.

## Feature list

### v0.1 CLI

1. `r2-backup-probe lint <file>`
   - Accepts a Duplicati exported command line, destination URL, or sanitized config snippet.
   - Parses bucket, folder path, endpoint, TLS, S3 client, and relevant advanced options.
   - Emits warnings with documentation links and suggested Duplicati option changes.

2. `r2-backup-probe explain <log-file>`
   - Matches known error signatures such as unsupported streaming payloads, endpoint shape errors, token/API mismatch, TLS-disabled custom server URLs, and checksum/header conflicts.
   - Produces a ranked explanation rather than a single guess.

3. `r2-backup-probe report`
   - Outputs a redacted markdown report suitable for Duplicati forum or GitHub issues.
   - Redacts secrets, account IDs, bucket names by default, local paths, and usernames.

4. Optional `--live` probe
   - Only runs when the user explicitly opts in.
   - Writes and deletes a tiny sentinel object under a clearly named prefix.
   - Never stores credentials.

## Data model

```text
ParsedConfig
  provider: cloudflare-r2 | generic-s3 | unknown
  endpoint_host: redacted string
  use_ssl: boolean | unknown
  bucket: redacted string | missing
  prefix: redacted string | missing
  s3_client: aws | minio | unknown
  options: map<string, redacted string>

Finding
  severity: info | warning | error
  code: string
  summary: string
  evidence: string
  recommendation: string
  docs_url: string | null
```

## Build plan

1. Implement fixture-driven parser for Duplicati destination URLs and exported command lines.
2. Add rule engine for R2/Duplicati compatibility findings.
3. Add log signature matcher with tests based on sanitized snippets.
4. Add markdown report renderer and redaction tests.
5. Add optional live S3 probe behind `--live` with a dry-run default.

## Validation plan

- Unit tests for URL/config parsing.
- Fixture tests for known Duplicati/R2 error messages.
- Redaction tests for secrets, bucket names, local paths, account IDs, and usernames.
- CLI smoke test that runs without network or credentials.
- Optional manual live test against a throwaway R2 bucket outside CI.
