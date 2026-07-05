# Day 017 — BecomeDoctor

Date: 2026-07-05
Status: repo-created

## One-line pitch

A local CLI that checks whether an Ansible inventory will survive the Ubuntu `sudo-rs` transition before `become: true` playbooks hang in production.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1unmkti/ubuntu_is_disabling_sudors_and_keep_using_sudo/ | Fresh user confusion: Ubuntu is disabling `sudo-rs`? Is continuing traditional `sudo` safe, and why did Ansible become have problems? Reddit JSON was blocked; RSS fallback provided the title/snippet. |
| Ansible upstream issue | https://github.com/ansible/ansible/issues/85837 | Ansible tracked `sudo-rs` compatibility because Ubuntu 25.10 switches to `sudo-rs`; the issue describes prompt-format incompatibility in the `sudo` become plugin. |
| Ubuntu Community Hub | https://discourse.ubuntu.com/t/adopting-sudo-rs-by-default-in-ubuntu-25-10/60583 | Canonical announced Ubuntu 25.10 will be the first major distro to adopt `sudo-rs` by default and test the path toward 26.04 LTS. |
| Ubuntu bug archive | https://www.mail-archive.com/ubuntu-bugs@lists.ubuntu.com/msg6279295.html | Public bug report says Ubuntu 26.04 + ansible-core 2.20.1 + `sudo-rs` can time out waiting for the privilege escalation prompt. |
| Ansible docs | https://docs.ansible.com/projects/ansible/latest/playbook_guide/playbooks_privilege_escalation.html | `become` depends on existing privilege-escalation tools; when a playbook appears to hang, the docs point to privilege-escalation prompt handling. |

## Source access caveats

- Reddit public JSON returned `HTTP 403 theme-beta`; the bundled Reddit tool used public RSS for `r/selfhosted` post discovery.
- Reddit thread/comment fetches for the candidate posts also returned `HTTP 403`, so this brief uses the RSS post snippet rather than comments.
- X/Twitter `whoami` worked, but `xurl search` returned `401 Unauthorized`; X was not used as evidence.
- Several web-search fallback queries returned no useful Reddit results; competitor/timing checks used original public docs, issue trackers, and project pages.

## Problem

Admins who manage Ubuntu fleets with Ansible are about to hit a subtle privilege-escalation compatibility boundary: `sudo-rs` is intended as a safer replacement, but it is not a perfect 1:1 clone of legacy `sudo`, and prompt behavior has already affected Ansible `become`. The current workflow is reactive: upgrade a host, run a playbook, watch it hang or fail, search GitHub/Ubuntu bugs, then guess whether to upgrade Ansible, install `sudo-ws`, or change become settings.

That wastes time during OS upgrades and can block maintenance windows. It is also easy to misdiagnose as an SSH, password, or playbook issue rather than a privilege-escalation provider mismatch.

## Target user

Small-team sysadmins, homelab operators, and infrastructure engineers who run Ansible against Ubuntu 25.10/26.04 hosts and cannot afford blind `become: true` failures during upgrades.

## MVP scope

- `become-doctor scan --inventory hosts.ini`: connect to hosts or run locally and detect distro, `sudo` provider, `sudo-rs` version where available, Ansible version, and relevant become settings.
- Safe no-op probe: run a redacted, non-mutating privilege-escalation prompt test and classify known failure modes.
- Compatibility rules file: map Ubuntu release + Ansible version + `sudo-rs` behavior to likely outcomes.
- Remediation output: exact next action such as upgrade ansible-core, test Ubuntu 25.10 in CI, install `sudo-ws` temporarily, or rerun with `--ask-become-pass`.
- Public-safe report: redact hostnames, usernames, command paths, and inventory details by default.

## Shortlist and wedge-first gate

1. **BecomeDoctor** — Ubuntu/Ansible admins → manual upgrade tests, Ansible issues, Ubuntu bug reports → failures appear as vague `become` hangs and are discovered too late → local safe compatibility probe with remediation → r/ansible, r/sysadmin, Ubuntu upgrade searches, Ansible issue backlinks → Ubuntu 25.10/26.04 `sudo-rs` transition is happening now.
2. **Syncthing Fork Trust Card** — Android self-hosted backup users → F-Droid pages, Syncthing forum threads, FolderSync → fork trust and maintenance status are scattered and anxiety-heavy → local checklist/trust matrix for Android backup choices → r/selfhosted and F-Droid/Syncthing forum searches → official Android app discontinuation/fork confusion is active. Rejected as winner: product depends on ongoing human curation and trust claims.
3. **ReverseProxy Path Probe** — Docker self-hosters exposing Jellyfin/apps → Nginx Proxy Manager, Caddy docs, `curl`, container logs → connection-refused failures hide container-network/port mistakes → one-shot network path probe from proxy container to upstream → r/selfhosted replies/search and homelab docs → fresh Jellyfin/Nginx/Cloudflare failure. Held: overlaps heavily with HeaderPass and generic reverse-proxy diagnostics.
4. **ContextFit** — local LLM users choosing model/quant/context → llama-bench, spreadsheets, forum posts → token-generation metrics obscure prefill/KV/cache constraints → benchmark parser that recommends model/context fit from logs → r/LocalLLaMA benchmark posts → long-context agent workloads are top of mind. Held: crowded benchmark/calculator space; wedge needs real benchmark spike.
5. **HiResNav Matrix** — self-hosted music users with iOS DACs → Navidrome/Subsonic clients, forum recommendations → passthrough/EQ/background-play capabilities are scattered → searchable client/server compatibility matrix → r/selfhosted/iOS audio searches → fresh request. Rejected: narrower pain and weak app-vs-doc wedge.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Ansible upstream compatibility work / issue #85837 | Upstream fixes the core bug, but it does not answer whether a user's mixed fleet, distro version, and installed Ansible version are safe before an upgrade window. |
| Direct competitor | Molecule / ansible-test / distro CI | Powerful for maintainers, but too heavy for an operator who wants a quick inventory readiness report. |
| Indirect substitute | Manual VM upgrade rehearsal | Reliable but slow; duplicates work per fleet and still requires interpreting `sudo-rs` vs legacy `sudo` behavior. |
| Indirect substitute | Reading Ubuntu discourse, Launchpad bugs, Ansible docs | Good source material but not an executable diagnosis for a real inventory. |
| Status quo | Run playbooks after upgrade and debug hangs | Causes blocked maintenance, wasted debugging time, and potentially bad rollback decisions. |

## Wedge

BecomeDoctor is not a generic Ansible linter. It is a time-boxed compatibility probe for one timely migration: Ubuntu's default `sudo` provider changing to `sudo-rs` and the knock-on effect on Ansible `become`. The MVP can win by being executable, safe, and specific: run one command before an upgrade and get a redacted report with known failure modes and remediation.

## Kill condition

Reject or narrow if current ansible-core releases fully absorb the transition before Ubuntu 26.04 adoption and no operators report fleet-specific hangs. Also reject if safe probing requires storing credentials or mutating hosts; the MVP must stay read-only/no-op apart from the standard privilege-escalation check.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | `become` failures can block maintenance windows and are hard to distinguish from SSH/password/playbook issues. |
| Feasibility | 4/5 | CLI rules engine + safe probe is buildable in 1-3 days using Python, Ansible inventory parsing, and fixture-based tests. |
| Demo potential | 3/5 | Mostly terminal output; demo is clear but less visual than a UI product. |
| Distribution | 4/5 | Specific communities and search paths: r/ansible, r/sysadmin, Ubuntu 25.10/26.04 upgrade posts, Ansible issue/bug backlinks, DevOps blog snippets. |
| Competitive wedge / timing | 4/5 | Strong timing from Ubuntu's `sudo-rs` default and public Ansible/Ubuntu bug evidence; narrow enough to avoid generic linter competition. |
| Total | 19/25 | Clears repo threshold and both gates. |

## Decision

Create a dedicated repo: `halaprix/become-doctor`.

Reason: the score clears 18/25, distribution is 4/5, and competitive wedge/timing is 4/5. The weakest dimension is demo potential (3/5), not market/distribution.

## Next build step

Implement `become-doctor scan --local --fixture ubuntu-26-sudo-rs-timeout` with a fixture-backed rules engine that prints one redacted compatibility report and one remediation recommendation.
