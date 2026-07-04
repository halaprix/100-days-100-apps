# Day 016 — R2 Backup Probe

Date: 2026-07-04
Status: repo-created
Repo: https://github.com/halaprix/r2-backup-probe

## One-line pitch

A local-first CLI that diagnoses Duplicati + Cloudflare R2 backup connection failures before self-hosters keep retrying blind.

## Source access caveats

- Reddit public JSON was blocked for the collection pass; `reddit-readonly` used RSS fallback for r/selfhosted. RSS fallback scores/comment counts are unavailable and treated as meaningless.
- r/sysadmin and r/LocalLLaMA RSS requests returned Reddit `HTTP 429` during the same pass, so I stopped retrying and used web search/extract for competitor and substitute validation.
- X/Twitter `xurl whoami` worked, but `xurl search` returned `401 Unauthorized`, so no X evidence was used.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1umvdih/duplicati_cloudflare_r2_test_connection_failed/ | Fresh user report: Duplicati Cloudflare R2 test connection failed with a confusing checksum-related error while configuring self-hosted backup storage. |
| Duplicati docs | https://docs.duplicati.com/backup-destinations/standard-based-destinations/s3-compatible-destination | Duplicati says non-AWS S3-compatible providers may need `--s3-disable-chunk-encoding` or `--s3-client=minio`; AWS-library defaults can be incompatible. |
| Duplicati forum | https://forum.duplicati.com/t/back-up-to-cloudflare-r2-storage-fails/15511 | Detailed R2 thread shows Duplicati reporting "Connection worked" while the actual backup fails, then advice to inspect logs, try Minio, and use backend tools. |
| Duplicati GitHub | https://github.com/duplicati/duplicati/issues/4673 | Open R2 support issue documents endpoint/TLS/custom-server confusion and incomplete S3 compatibility around Duplicati + R2. |
| Cloudflare R2 docs | https://developers.cloudflare.com/r2/platform/troubleshooting/ | R2 troubleshooting distinguishes S3-compatible API auth from REST API auth and suggests curl/S3 signing checks for unclear failures. |
| Cloudflare R2 rclone docs | https://developers.cloudflare.com/r2/examples/rclone/ | `rclone` is a strong substitute for validating R2 credentials and object access, but it is not Duplicati-specific. |

## Problem

Self-hosters choose Duplicati + Cloudflare R2 because encrypted backups plus low-egress object storage are attractive. The failure mode is operationally dangerous: a UI connection test can pass or fail with opaque S3 errors, while the real backup may still break later because Duplicati, the AWS/Minio client choice, endpoint shape, TLS defaults, checksums, chunked signing, or token type do not line up with R2.

The status quo is forum archaeology and trial-and-error against a backup path. That can burn more than 30 minutes per incident and, worse, creates false confidence in a backup job that has not actually proven write/list/delete behavior.

## Target user

Self-hosters and small-office admins running Duplicati backups to Cloudflare R2 or another S3-compatible bucket who need a safe, explainable preflight before trusting the job with real data.

## MVP scope

- CLI: `r2-backup-probe lint <duplicati-export>` parses a Duplicati export, command line, or destination URL.
- Rule checks for endpoint shape, TLS, bucket/path ambiguity, `--s3-client=minio`, chunk encoding, token/API mismatch, and unsupported S3 feature signatures.
- `r2-backup-probe explain <log-file>` maps sanitized Duplicati/R2 errors to likely causes and next checks.
- Optional `--live` probe writes and deletes a tiny sentinel object only when explicitly requested.
- Redacted markdown report for Duplicati forum/GitHub support threads; no credential storage and no telemetry.

## Shortlist and wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| R2 Backup Probe | Self-hosters running Duplicati to Cloudflare R2 → Duplicati test button, docs, forums, rclone, manual log reading → substitutes either only test generic object access or require knowing Duplicati-specific S3 options/error signatures → local Duplicati/R2 linter + explainer + redacted support report → r/selfhosted, Duplicati forum/GitHub issues, Cloudflare R2 search traffic → fresh Reddit failure plus still-open R2 support issue and R2 adoption. | Winner; narrow backup-risk wedge and concrete first-user channels. |
| NASBrief | Beginners building first home NAS/media/backup box → Plex/Jellyfin docs, NAS guides, ChatGPT, Synology/QNAP buying guides → guidance is fragmented and hardware-specific → questionnaire that outputs a minimal topology and service plan → r/selfhosted beginner posts/search → home-lab interest stays high. | Rejected: too advisory/content-like; status quo is tolerable and distribution is broad beginner traffic. |
| AliasPort | People buying custom domains for email aliases and provider portability → SimpleLogin/Addy.io docs, registrar docs, email provider setup guides → users struggle to understand what moves when switching providers → local domain/email alias migration checklist and DNS record simulator → r/selfhosted/email privacy search content → portability anxiety is recurring. | Idea-only runner-up; useful but direct products already own much of the workflow, and willingness to pay is unclear. |
| DuckDNS Remote Check | Raspberry Pi/Jellyfin users setting DuckDNS + nginx proxy remote access → Nginx Proxy Manager docs, port checkers, router UI, forum replies → beginners cannot tell DNS, NAT, firewall, or proxy failure apart → local/network-side diagnostic script with safe redaction → r/selfhosted support threads/search → home media remote access remains common. | Rejected for today: overlaps prior HeaderPass/PeerPath network diagnostics and risks becoming generic home-network troubleshooting. |
| ServerFinder | New home-lab users who cannot find a headless server IP → Angry IP Scanner, router DHCP list, Wireshark, arp-scan → tools show too much and beginners do not know what is safe → guided LAN discovery wizard that identifies likely BMC/server NICs → r/selfhosted beginner support/search → second-hand mini-server setups are common. | Rejected: useful but weaker status-quo pain; existing scanners solve most of the job. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Duplicati built-in Test connection, logs, BackendTool/BackendTester | Native and free. The gap is that the UI test does not explain Duplicati/R2-specific compatibility failures well, and users still have to discover the right advanced options and log locations. |
| Direct competitor | Duplicati docs and forum support threads | Rich source of fixes, but not executable. Users must search, redact, compare versions, and decide which advice applies. |
| Direct competitor | `rclone` with Cloudflare R2 config | Strong generic R2 object-access validator and a real substitute. It does not lint Duplicati exports or map Duplicati-specific AWS SDK/Minio/chunk-signing errors to settings. |
| Indirect substitute | Switch backup tool to restic/borg/rclone, or use a different S3 provider | Often reasonable, but migration is more work than fixing a nearly-working Duplicati setup. |
| Indirect substitute | Manual curl/S3 SDK probes and reading Cloudflare R2 troubleshooting docs | Powerful for experts; too low-level for self-hosters who just need the backup job to become trustworthy. |
| Status quo | Retry options, paste logs into forums, or trust a backup after only a shallow connection test | Wastes time and creates backup reliability risk; the pain is not just annoyance, it can become data-loss risk if a job was never truly validated. |

## Wedge

R2 Backup Probe should not become a generic S3 GUI or backup tool. The wedge is a narrow preflight question:

> Given this Duplicati export/log and an R2 target, which known Duplicati/R2 incompatibility is likely, what exact setting should I check next, and what redacted report can I paste into support?

That leaves strong substitutes in place. `rclone` remains the generic object-storage validator; Duplicati remains the backup engine; Cloudflare docs remain the reference. The product wins only as a small translator between Duplicati's configuration/log language and R2's S3-compatible quirks.

## Kill condition

Kill or narrow if current Duplicati releases add first-class Cloudflare R2 support with clear diagnostics, if the common failures collapse to one documented setting, or if early users only want a general backup dashboard. Also reject expansion into credential storage or hosted monitoring because it would destroy the local-first trust wedge.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Backup misconfiguration can create real data-loss risk; the workaround can burn >30 minutes and produce false confidence. |
| Feasibility | 4/5 | A 1-3 day MVP can parse exports/logs and ship rule-based findings with fixture tests; live S3 probing is optional. |
| Demo potential | 4/5 | Clear terminal demo: feed a sanitized export/log, show ranked findings, suggested flags, docs links, and redacted markdown report. |
| Distribution | 4/5 | Specific channels exist: r/selfhosted support posts, Duplicati forum/GitHub issues, and search-led docs for "Duplicati Cloudflare R2" failures. |
| Competitive wedge / timing | 3/5 | Strong substitutes exist, especially Duplicati support and rclone, but none is a Duplicati/R2-specific local explainer. Fresh Reddit signal plus the open R2 support issue support timing. |
| Total | 19/25 | Clears repo threshold and gates. |

## Decision

Create the dedicated repo because R2 Backup Probe scored 19/25, Distribution is 4/5, and Competitive wedge / timing is 3/5.

Repo created, scaffold pushed, and tagged: https://github.com/halaprix/r2-backup-probe

## Next build step

Implement `r2-backup-probe lint` with fixture-based parsing for Duplicati S3 destination URLs/exported command lines, the first R2 compatibility rule set, and redacted markdown report output.
