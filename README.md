# 100 Days, 100 Apps

**Daily product lab for turning Reddit/X pain points into small app ideas and public repos.**

[![CI](https://github.com/halaprix/100-days-100-apps/actions/workflows/ci.yml/badge.svg)](https://github.com/halaprix/100-days-100-apps/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)

## What this is

A 100-day build-in-public experiment:

1. Watch Reddit, X/Twitter, and web signals for repeated pain points.
2. Generate a daily shortlist of practical app ideas.
3. Score each idea for usefulness, feasibility, demo potential, and distribution.
4. Pick one winner.
5. Create a public repo per selected project.
6. Maintain this repo as the master index.

The goal is not to create 100 empty repos. The goal is to create a public trail of **100 researched product bets**, each with enough context to decide whether it deserves implementation.

## Index

| Day | Date | App | Repo | Signal | Status | Notes |
|---:|---|---|---|---|---|---|
| 000 | 2026-06-19 | Meta index | [`halaprix/100-days-100-apps`](https://github.com/halaprix/100-days-100-apps) | Project kickoff | scaffolded | Daily pipeline repo |
| 001 | 2026-06-19 | CommentPulse | [`halaprix/comment-pulse`](https://github.com/halaprix/comment-pulse) | Creators need traceable comment-to-pain-point summaries | blocked | Scored 20/25; scaffold commit local, git push blocked by 403 |
| 002 | 2026-06-20 | TendTogether (held) | — | Neurodivergent-couple shared board with persistent Notice lane | idea-only | Scored 19/25; clears threshold but held — borderline, narrow audience. 9 ideas scored, 8 rejected on competitor gate. |
| 003 | 2026-06-21 | HumanMark | — | Developers cannot trust raw visitor counts in bot-heavy traffic | idea-only | Scored 17/25; no repo — crowded analytics category, single strong public thread. |
| 004 | 2026-06-22 | VibeGuard | — | Vibe-coded founders need a plain-language launch security gate | idea-only | Scored 17/25; no repo — strong timing, crowded AppSec/autofix category. |
| 005 | 2026-06-23 | DemoCut | — | SaaS founders need demo story/shot planning before recording complex products | idea-only | Scored 17/25; no repo — useful pain, but crowded AI demo/video category. |
| 006 | 2026-06-24 | DeskPatch | [`halaprix/deskpatch`](https://github.com/halaprix/deskpatch) | Locked-down analyst desktops need safe self-service Power BI updates without stored admin creds | blocked | Scored 19/25; remote repo created, local scaffold push blocked by GitHub 403. |
| 007 | 2026-06-25 | SelectDiet | — | Astro/static-site developers need bundle-aware select component decisions | idea-only | Scored 17/25; no repo — useful narrow dev-tool wedge, but evidence is still one strong thread plus package/docs signals. |
| 008 | 2026-06-26 | AgentLedger | — | Self-hosted personal agents need a proof-of-done task ledger that prevents drifting project and waiting lists | idea-only | Scored 18/25; no repo — total clears, but distribution gate fails at 3/5. |
| 009 | 2026-06-27 | PipeTwin | [`halaprix/pipe-twin`](https://github.com/halaprix/pipe-twin) | Maintainers need failed CI runs turned into local repro bundles before pushing blind fixes | blocked | Scored 19/25; remote repo created, local scaffold push blocked by GitHub 403. |
| 010 | 2026-06-28 | NIS2 EvidencePack | [`halaprix/nis2-evidencepack`](https://github.com/halaprix/nis2-evidencepack) | EU SME IT owners need offline NIS2 evidence binders without adopting full GRC SaaS | blocked | Scored 19/25; remote repo created, local scaffold commit 98e199d ready; push blocked by GitHub 403. |
| 011 | 2026-06-29 | Llama CUDA Doctor | [`halaprix/llama-cuda-doctor`](https://github.com/halaprix/llama-cuda-doctor) | Local LLM builders need CUDA/driver/llama.cpp mismatch diagnostics before rebuilding blind | blocked | Scored 19/25; remote repo created, local scaffold commit aa6a7ab ready; push blocked by GitHub 403. |
| 012 | 2026-06-30 | PeerPath | [`halaprix/peerpath`](https://github.com/halaprix/peerpath) | Self-hosters need Dockerized WireGuard/wg-easy host-to-peer routing diagnostics before pasting unsafe firewall fixes | blocked | Scored 20/25; remote repo created, local scaffold commit a3382d6 ready; push blocked by GitHub 403. |
| 013 | 2026-07-01 | PermTwin | — | SharePoint admins need safe user-to-user permission diffs before copying access | idea-only | Scored 17/25; no repo — direct competitors already cover permission reporting/compare, wedge needs sharper proof. |
| 014 | 2026-07-02 | HeaderPass | [`halaprix/headerpass`](https://github.com/halaprix/headerpass) | Self-hosters need safe diagnostics when Cloudflare Access/tunnel headers break mobile or API clients | repo-created | Scored 19/25; repo scaffold pushed and tagged v0.1.0-alpha.0. |
| 015 | 2026-07-03 | VramJanitor | [`halaprix/vram-janitor`](https://github.com/halaprix/vram-janitor) | Local LLM users need reclaimable desktop VRAM identified before launching models | repo-created | Scored 20/25; repo scaffold pushed and tagged v0.1.0-alpha.0. |
| 016 | 2026-07-04 | R2 Backup Probe | [`halaprix/r2-backup-probe`](https://github.com/halaprix/r2-backup-probe) | Duplicati + Cloudflare R2 backup users need executable diagnostics before trusting failed/opaque S3 connection tests | repo-created | Scored 19/25; repo scaffold pushed and tagged v0.1.0-alpha.0. |
| 017 | 2026-07-05 | BecomeDoctor | [`halaprix/become-doctor`](https://github.com/halaprix/become-doctor) | Ubuntu/Ansible operators need a safe `sudo-rs` become-compatibility preflight before upgrade windows | repo-created | Scored 19/25; repo scaffold pushed and tagged v0.1.0-alpha.0. |
| 018 | 2026-07-06 | LabFit | [`halaprix/labfit`](https://github.com/halaprix/labfit) | Self-hosters need Proxmox-vs-NAS workload placement advice before copying install scripts | repo-created | Scored 19/25; repo scaffold pushed and tagged v0.1.0-alpha.0. |
| 019 | 2026-07-07 | OOBEGuard | [`halaprix/oobeguard`](https://github.com/halaprix/oobeguard) | Windows imaging admins need OEM/OOBE setup trap checks before silent post-image script failures | repo-created | Scored 19/25; repo scaffold pushed and tagged v0.1.0-alpha.0. |
| 020 | 2026-07-08 | DavSync Doctor | [`halaprix/davsync-doctor`](https://github.com/halaprix/davsync-doctor) | Radicale/Baïkal self-hosters need Apple Contacts/CardDAV sync diagnostics before leaking configs into support threads | repo-created | Scored 19/25; repo scaffold pushed and tagged v0.1.0-alpha.0. |
| 021 | 2026-07-09 | BayTrace | [`halaprix/baytrace`](https://github.com/halaprix/baytrace) | Proxmox homelab builders need read-only SATA bay/controller diagnostics before trusting flaky disk detection | repo-created | Scored 21/25; repo scaffold pushed and tagged v0.1.0-alpha.0. |
| 022 | 2026-07-10 | StorePacket | [`halaprix/storepacket`](https://github.com/halaprix/storepacket) | Solo mobile SaaS founders need App Store submission packet prep before losing days in App Store Connect | repo-created | Scored 20/25; repo scaffold pushed and tagged v0.1.0-alpha.0. |
| 023 | 2026-07-11 | SheetSentry | [`halaprix/sheetsentry`](https://github.com/halaprix/sheetsentry) | Builders need sheet-backed API/MCP endpoint checks before provider caps or schema drift blank public pages | repo-created | Scored 20/25; repo scaffold pushed and tagged v0.1.0-alpha.0. |
| 024 | 2026-07-12 | FreeTierFit | [`halaprix/free-tier-fit`](https://github.com/halaprix/free-tier-fit) | Self-hosters need tiny-host Docker Compose fit checks before overloading free-tier VMs | repo-created | Scored 19/25; repo scaffold pushed and tagged v0.1.0-alpha.0. |
| 025 | 2026-07-13 | TenantRoute | [`halaprix/tenant-route`](https://github.com/halaprix/tenant-route) | Microsoft 365 admins need tenant-country/CSP-region decision packets before overbuying or delaying tenant migrations | repo-created | Scored 19/25; repo scaffold pushed and tagged v0.1.0-alpha.0. |
| 026 | 2026-07-14 | PortLease | [`halaprix/portlease`](https://github.com/halaprix/portlease) | Self-hosters need read-only UPnP/NAT-PMP lease reports before a NAS silently exposes services | repo-created | Scored 22/25; repo scaffold pushed and tagged v0.1.0-alpha.0. |
| 027 | 2026-07-15 | TzDrift | [`halaprix/tzdrift`](https://github.com/halaprix/tzdrift) | Sysadmins need timezone-law/tzdata readiness packets before stale runtimes or local-time schedulers drift | repo-created | Scored 21/25; repo scaffold pushed and tagged v0.1.0-alpha.0. |
| 028 | 2026-07-16 | ExitTrace | [`halaprix/exittrace`](https://github.com/halaprix/exittrace) | Sensitive-support sites need browser-trace safety audits before SEO titles or slugs expose at-risk users | repo-created | Scored 21/25; repo scaffold pushed and tagged v0.1.0-alpha.0. |

## Daily process

See [`docs/PROCESS.md`](./docs/PROCESS.md). Local layout is in [`docs/LOCAL_WORKSPACE.md`](./docs/LOCAL_WORKSPACE.md). Dedicated project repos use [`docs/REPO_TEMPLATE.md`](./docs/REPO_TEMPLATE.md).

## Operating rules

Agents must follow [`AGENTS.md`](./AGENTS.md): local-first while GitHub writes are blocked, Beads-only task tracking, public-safe evidence, and no social posting without explicit approval.

## Idea records

Daily briefs live in [`ideas/`](./ideas/). Each file should include source links, problem statement, MVP scope, scoring, and repo link when created.

## Machine-readable index

See [`index.json`](./index.json).

## License

Apache-2.0. See [`LICENSE`](./LICENSE).
