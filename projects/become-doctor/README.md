# BecomeDoctor

A local CLI that checks whether an Ansible inventory will survive the Ubuntu `sudo-rs` transition before `become: true` playbooks hang in production.

## Problem

Ubuntu 25.10 begins the move to `sudo-rs` as the default `sudo` implementation, with Ubuntu 26.04 LTS in the adoption path. Ansible `become` depends on privilege-escalation prompt behavior, and public Ansible/Ubuntu issues already show compatibility problems around `sudo-rs` prompt handling.

Today, operators discover the problem too late: upgrade a host, run a playbook, hit a vague privilege-escalation hang, then search issue trackers during a maintenance window.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1unmkti/ubuntu_is_disabling_sudors_and_keep_using_sudo/ | Fresh public confusion around Ubuntu, `sudo-rs`, and Ansible become problems. |
| Ansible upstream issue | https://github.com/ansible/ansible/issues/85837 | Ansible tracked `sudo-rs` compatibility because Ubuntu 25.10 switches to `sudo-rs`; prompt behavior affected the sudo become plugin. |
| Ubuntu Community Hub | https://discourse.ubuntu.com/t/adopting-sudo-rs-by-default-in-ubuntu-25-10/60583 | Ubuntu announced `sudo-rs` by default in 25.10 as a step toward wider adoption. |
| Ubuntu bug archive | https://www.mail-archive.com/ubuntu-bugs@lists.ubuntu.com/msg6279295.html | Public bug says Ubuntu 26.04 + ansible-core + `sudo-rs` can time out waiting for the privilege-escalation prompt. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Ansible upstream compatibility fixes | Fixes core behavior, but does not provide a fleet readiness report for mixed Ubuntu/Ansible versions. |
| Direct competitor | Molecule / ansible-test / distro CI | Strong for maintainers; heavy for small operators who need a quick pre-upgrade check. |
| Indirect substitute | Manual VM upgrade rehearsal | Accurate but slow and duplicated across environments. |
| Indirect substitute | Ubuntu/Ansible docs and issue trackers | Useful references, not an executable diagnosis. |
| Status quo | Run the playbook and debug the hang | Risks blocked maintenance windows and misdiagnosis. |

## Wedge

BecomeDoctor is a narrow, executable compatibility probe for one timely migration: Ubuntu's `sudo-rs` default and its effect on Ansible `become`. It does not try to lint every playbook. It answers: "Will this inventory's privilege escalation likely work after the upgrade, and what should I do if not?"

## Target user

Small-team sysadmins, homelab operators, and infrastructure engineers who manage Ubuntu hosts with Ansible and need a safe preflight before Ubuntu 25.10/26.04 upgrades.

## MVP

- `become-doctor scan --local` for the current machine.
- `become-doctor scan --inventory hosts.ini` for an Ansible inventory.
- Detect Ubuntu release, `sudo` provider, `sudo-rs` version where available, Ansible version, and relevant become settings.
- Run a safe no-op privilege-escalation probe and classify known failure modes.
- Print a redacted report with remediation: upgrade ansible-core, test a release candidate, install legacy `sudo-ws` temporarily, or adjust become invocation.
- Fixture-backed tests so CI does not need privileged containers.

## Non-goals

- No credential storage.
- No hosted dashboard or telemetry.
- No automatic package changes.
- No broad Ansible best-practices linting in the MVP.
- No mutation of remote hosts beyond an explicit safe no-op privilege-escalation probe.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
