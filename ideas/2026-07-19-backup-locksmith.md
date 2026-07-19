# Day 031 — BackupLocksmith

Date: 2026-07-19
Status: repo-created

## One-line pitch

A local-first recovery packet generator for self-hosted backup-console lockouts, starting with UrBackup admin-account failures, so novice self-hosters can regain access without deleting backup metadata or pasting unsafe commands.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS fallback — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1v0awgz/im_new_to_making_self_hosted_servers_so_im_trying/ | Fresh post from a novice self-hoster says UrBackup prompted them to create an admin account, then immediately rejected the password; the author primarily uses Windows and describes Linux terminal recovery as a nightmare. |
| Reddit RSS fallback — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1v0fbwd/portable_hdd_question/ | Adjacent fresh self-hosting signal: another novice is rebuilding a Plex/Arr stack and moving disks, showing the same audience is doing risky storage/backup work with limited Linux confidence. |
| Reddit web search — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/17o63zy/i_love_the_idea_behind_urbackup_but_its_executed/ | Older public thread describes UrBackup as attractive but frustrating, with weird/inconsistent deployment issues in stricter environments. |
| UrBackup manual | https://www.urbackup.org/administration_manual.html | Official manual says fresh installs have no administrator password and everyone can see backed-up files until an admin account is created, confirming first-run account setup is security-sensitive. |
| UrBackup How To | https://urbackup.atlassian.net/wiki/display/US/How+To | Public search result for the official how-to documents `start_urbackup_server --reset_pw` for admin password reset, proving a recovery mechanism exists but is not packaged into OS/container-specific guidance. |
| UrBackup FAQ | https://www.urbackup.org/faq.html | FAQ documents operational gotchas around server identity, restore safety, paths, and service behavior that novices need before making changes to a backup server. |
| AlternativeTo | https://alternativeto.net/software/urbackup/ | Shows many mature backup alternatives, confirming BackupLocksmith must not compete as backup software; it is a narrow recovery/readiness helper. |

Source access notes: Reddit public JSON endpoints returned `HTTP 403 theme-beta`, so collection used the reddit-readonly skill's public RSS fallback where available. Several subreddit RSS feeds returned `HTTP 429`; no retry loop was used. Reddit comment/thread JSON was not used. X `whoami` worked, but X search returned `401 Unauthorized`, so X was not used as evidence. Competitor validation used public docs and web search/extraction.

## Shortlist and wedge gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| BackupLocksmith | Novice self-hosters or small-office admins locked out of UrBackup → official docs, forum replies, shell/Docker/systemd commands, reinstalling, or asking Reddit → substitutes contain the reset command but not a safe read-only install-mode packet, and novices can destroy useful backup metadata while guessing → local packet generator that identifies likely UrBackup install shape, pre-reset facts, official references, and unsafe paths without writing to the system → r/selfhosted, r/urbackup, UrBackup search queries, backup homelab content, and support-thread reply strategy → fresh lockout post plus official docs show first-run password/reset remains a security-sensitive trap. | Winner; clears repo threshold if scoped as read-only packet generation, not password reset automation. |
| ArchiveLite | Self-hosters wanting an archive.today-like service → ArchiveBox, SingleFile, Browsertrix, Wallabag/Linkwarden/Hoarder, Internet Archive → substitutes are mature and broad, but some users want one-click public-page capture → tiny single-purpose capture UI with WARC/PDF/screenshot output → selfhosted/web-archiving communities and SEO → fresh request asks for self-hosted archive.is behavior. | Rejected: crowded category with strong incumbents; wedge is convenience, not enough status-quo pain. |
| FriendGatePlan | Homelab owners sharing services with ~20 friends without per-user SaaS limits → Tailscale/Headscale, Cloudflare Tunnel, Pangolin, Authentik, Authelia, Caddy, manual diagrams → substitutes solve major parts but force complex architecture tradeoffs → local access-architecture sanity packet for friend-facing services → r/selfhosted and homelab security content → fresh architecture-overhaul post asks for feedback. | Held/rejected for today: useful but overlaps recent HeaderPass/PeerPath/PortLease access-networking winners. |
| OfferVaultLocal | Privacy-sensitive developers tracking card offers → bank portals, CardPointers, AwardWallet, Rakuten/Honey-style extensions, spreadsheets → substitutes either need account access or manual checking → local-only browser extension that parses offers only on explicit bank pages → webdev/privacy/credit-card communities → fresh r/webdev post shows someone built this exact pain. | Rejected: finance browser-extension trust and crowded rewards space make distribution and policy risk high. |
| SlashCanon | Web developers debugging forced trailing slashes and redirects → curl, browser devtools, Lighthouse, Screaming Frog, online redirect checkers → substitutes are easy for experienced devs and the pain is often educational → small CLI that reports canonical URL/redirect/cache consequences → webdev/SEO content → fresh r/webdev question asks why trailing slashes are forced. | Rejected: status-quo workaround is tolerable; not enough pain for the daily winner. |

## Problem

Backups are only useful if the operator can administer and restore them. For novice self-hosters and small-office admins, backup-console lockouts are a bad failure mode: they happen right after installing something important, the recovery advice is scattered across docs and forum snippets, and the operator may not understand the difference between a package install, container install, Windows service, config directory, backup storage directory, and server identity files.

The status quo wastes time and can create real risk:

- endpoints remain unprotected while the admin is locked out,
- the user may reinstall or wipe a container volume and lose useful metadata,
- an unsecured default web UI may expose backed-up files if account setup failed,
- support requests often leak more environment detail than needed,
- a simple reset command is still unsafe if run against the wrong binary/data path or before taking a config snapshot.

## Target user

- Self-hosters running UrBackup from a Linux package, LinuxServer.io-style container, or Windows install.
- Small-office admins who inherited a self-hosted backup server.
- MSP/helpdesk operators who want a safe intake packet before touching a customer's backup box.

## MVP scope

- Python CLI: `backup-locksmith inspect --fixture examples/urbackup-linux.json` for a public-safe demo first.
- Synthetic fixture profiles for UrBackup Linux package, Docker, and Windows service layouts.
- Read-only detectors for common service/container names and web-port hints in a later slice.
- Finding model with `blocker`, `warning`, and `info` severities.
- Markdown packet export with install-mode confidence, official reset references, pre-reset capture checklist, unsafe-action warnings, and redacted support handoff text.
- No passwords, no backup contents, no direct modifications to UrBackup config/database/container/service state in v0.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | UrBackup manual, FAQ, How To, community forum, and Reddit answers | Authoritative for commands and behavior. They do not inspect the local install shape or produce a redacted recovery packet for a novice. |
| Direct competitor | MSP/helpdesk/backup consultants | Better for business-critical recovery, but too heavy for home labs and small offices that need safe first triage or a packet to hand off. |
| Indirect substitute | Shell commands, Docker Compose files, systemd, AI chat, search snippets, reinstalling the container | Experienced admins can solve it manually. Novices can easily act before identifying data paths, service names, and backup metadata risk. |
| Status quo | Guess passwords, abandon backups, reinstall, delete volumes, or post screenshots/logs asking for help | Can prolong an unprotected state, lose metadata, or leak sensitive environment details. |

## Wedge

BackupLocksmith should stay narrower than backup software and safer than an automated reset tool. Its wedge is a read-only, local-first recovery packet for one painful moment: "I cannot get into my backup console; what can I safely check before I break something?"

Why this can still work despite existing options:

- Official docs are necessary but not enough for novices who do not know which install path applies.
- A packet generator can be useful without privileged API access or destructive actions.
- Synthetic fixtures make the demo easy and public-safe.
- The output is naturally shareable: Markdown can be pasted into a support thread after redaction or attached to an MSP/helpdesk ticket.
- Distribution is concrete: answer/search content around "UrBackup admin password reset", "UrBackup locked out", "UrBackup Docker reset password", r/selfhosted, and r/urbackup.

## Kill condition

Kill or narrow if UrBackup ships a first-party cross-platform recovery wizard that detects Linux package/Docker/Windows installs, shows safe pre-reset steps, redacts local details, and exports a support packet. Also kill any scope that requires reading backup contents, collecting passwords, cracking credentials, or directly modifying backup metadata before the read-only packet proves value.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Backup-console lockout blocks protection/restore work and can lead to destructive novice recovery attempts. |
| Feasibility | 5/5 | v0 can be fixture-driven Markdown/JSON packet generation with simple read-only detectors later. |
| Demo potential | 4/5 | Synthetic Linux/Docker/Windows examples can show clear blocker/warning output and redacted handoff packets. |
| Distribution | 4/5 | Specific support/search channels exist: r/selfhosted, r/urbackup, UrBackup reset-password SEO, and helpdesk/MSP intake workflows. |
| Competitive wedge / timing | 3/5 | The command-level fix exists in official docs, so the wedge is marginal but real: install-shape detection, safety warnings, and shareable recovery packets for novices. |
| Total | 20/25 | Clears repo threshold and both dimension gates. |

## Decision

Create `halaprix/backup-locksmith` as a dedicated project repo: https://github.com/halaprix/backup-locksmith. The score clears the 18/25 threshold, Distribution is 4/5, and Competitive wedge/timing is 3/5. Repo status is `repo-created`: scaffold pushed to GitHub and tagged `v0.1.0-alpha.0`.

## Next build step

Implement `backup-locksmith inspect --fixture examples/urbackup-linux.json` so it validates a synthetic UrBackup lockout profile, emits blocker/warning/info findings, and writes a redacted Markdown recovery packet with official reset references and pre-reset capture steps.
