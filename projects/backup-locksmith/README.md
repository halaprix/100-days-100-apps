# BackupLocksmith

Local-first recovery packet generator for self-hosted backup-console lockouts, starting with UrBackup.

## Problem

Novice self-hosters and small-office admins set up backup software because losing data is scary, then get blocked by the first administrative failure: the web console asks for a password, the new admin account is not accepted, or the service/container layout does not match the short forum answer they found.

The risky part is not that the reset command is impossible. It is that the operator may not know which binary, service, data directory, container, port, or safety step applies before touching a backup server that may hold the only good copy of their files.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS fallback — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1v0awgz/im_new_to_making_self_hosted_servers_so_im_trying/ | Fresh self-hoster says UrBackup prompted them to create an admin account, then locked them out; they primarily use Windows and describe the Linux terminal as a nightmare. |
| Reddit web search — r/selfhosted | https://www.reddit.com/r/selfhosted/comments/17o63zy/i_love_the_idea_behind_urbackup_but_its_executed/ | Older public thread signals broader UrBackup frustration around weird and inconsistent deployment issues. |
| UrBackup manual | https://www.urbackup.org/administration_manual.html | UrBackup's manual says a fresh install has no administrator password and everyone can see backed-up files until an admin account is created. |
| UrBackup How To | https://urbackup.atlassian.net/wiki/display/US/How+To | Public how-to snippet documents `start_urbackup_server --reset_pw` for resetting the server admin password, but does not package OS/container-specific recovery context. |
| UrBackup FAQ | https://www.urbackup.org/faq.html | FAQ shows operational gotchas around server identity, web settings, and restore safety that novices must understand when fixing access. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | UrBackup documentation, FAQ, and community/forum posts | Authoritative for commands and behavior, but scattered and not adapted to the operator's local install shape. |
| Direct competitor | Backup consultants/MSPs | Appropriate for business-critical recovery, but too heavy for a home lab or small office that needs a safe first triage packet. |
| Indirect substitute | Shell history, Docker Compose files, systemd commands, search results, and AI chat | Can work for experienced admins. For novices, it risks pasting destructive commands before identifying data paths or service state. |
| Status quo | Guess the password, reinstall, wipe the container, or abandon the backup setup | This can leave endpoints unprotected or destroy useful metadata while trying to regain access. |

## Wedge

BackupLocksmith is not a backup product and does not reset credentials in v0. The wedge is a read-only, local-first recovery packet: detect the likely UrBackup install mode, surface official reset references, list the exact pre-reset facts to capture, warn about unsafe reinstall/delete paths, and produce a Markdown checklist a novice can follow or hand to a more experienced admin.

## Target user

- Self-hosters running UrBackup from a Linux package, LinuxServer.io container, or Windows install.
- Small-office admins who inherited a self-hosted backup box.
- MSP/helpdesk operators who want a safe intake packet before touching a customer's backup server.

## MVP

- `backup-locksmith inspect --fixture examples/urbackup-linux.json` for a synthetic demo.
- Read-only detectors for common UrBackup service/container layouts.
- Markdown recovery packet with install mode, service status, web port, data/config path checklist, official reset references, and pre-reset backup steps.
- Severity labels: `blocker`, `warning`, `info`.
- Synthetic fixtures only in v0.1; no real passwords, backup contents, or destructive commands.

## Non-goals

- No credential cracking or password bypassing.
- No direct writes to UrBackup config, database, backup storage, or containers in v0.
- No replacement for a tested backup/restore strategy.
- No advice to expose backup consoles to the public internet.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
