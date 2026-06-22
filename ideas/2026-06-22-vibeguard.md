# Day 004 — VibeGuard

Date: 2026-06-22
Status: idea-only

## One-line pitch

A local-first security checkup for vibe-coded apps: run proven scanners, group the findings by launch risk, and generate a founder-readable fix plan or PR draft without pretending to be a full AppSec platform.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/SideProject | https://www.reddit.com/r/SideProject/comments/1ucdnfg/i_built_a_tool_that_scans_aigenerated_code_for/ | Fresh SideProject post frames a specific pain: founders shipping Cursor/Copilot/Claude-built apps may not understand SQL injection, leaked keys, or broken auth in the code they ship. |
| Reddit / r/SideProject | https://www.reddit.com/r/SideProject/comments/1ucdomt/cutlass_an_opensource_video_editor/ | Same fresh feed shows the broader wave: builders are adding AI agents to serious creation workflows, increasing the surface area for non-experts to ship complex software. |
| Competitor check / Semgrep | https://semgrep.dev/products/semgrep-code/ | Semgrep already offers SAST, AI-assisted triage, and remediation guidance in pull requests. This is a strong incumbent for teams with developer/security maturity. |
| Competitor check / GitHub Advanced Security | https://github.com/features/security | GitHub already offers code/security scanning, secret protection, and Copilot Autofix inside GitHub workflows, but pricing and positioning skew toward teams/organizations. |
| Competitor check / Gitleaks | https://gitleaks.io/ | Gitleaks is a trusted open-source secret scanner and a good building block rather than a product wedge by itself. |
| Competitor check / Snyk Code | https://snyk.io/product/snyk-code/ | Snyk Code already positions around AI-powered SAST and automatic fixes. Any new product must avoid competing as a generic scanner. |
| Competitor check / Aikido | https://www.aikido.dev/ | Aikido bundles code, cloud, runtime, autofix PRs, and AI pentesting, making the broad “security scanner with PRs” category very crowded. |

## Problem

Vibe-coded founders are shipping real apps faster than their security understanding catches up. Existing scanners can find issues, but the output often assumes the user already understands AppSec vocabulary, triage, false positives, exploitability, and whether a finding blocks launch. The painful job is not “run another scanner.” It is: “tell me, in plain language, whether my AI-built app is dangerously shippable, what I must fix first, and what can wait.”

## Target user

Indie founders, solo SaaS builders, and non-security developers using Cursor, Copilot, Claude Code, or similar tools to build small web apps. They can connect or clone a GitHub repo, but they do not want to become AppSec engineers before launching.

## MVP scope

- Local CLI or minimal web UI that runs on a cloned repo.
- Use existing scanners first: Gitleaks for secrets, Semgrep rules for common web vulnerabilities, dependency audit where the package manager supports it.
- Normalize results into three launch gates: **do not ship**, **fix soon**, **informational**.
- Explain each finding in founder language: affected file, why it matters, exploit scenario, smallest safe fix, and confidence.
- Produce a `SECURITY_LAUNCH_REPORT.md` and optional patch/PR draft for simple fixes.
- No hosted code upload in v1; local-first keeps trust and implementation scope small.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Semgrep, Snyk Code, GitHub Advanced Security, Aikido | Strong mature tools already scan code, prioritize findings, and in some cases create fixes/PRs. A generic “AI code security scanner” is not a good bet. |
| Direct competitor | DebtMap-style founder security scanner from the Reddit signal | The exact broad product idea is already being attempted by another builder, so the wedge must narrow. |
| Indirect substitute | Gitleaks, CodeQL, npm audit, pip-audit, OSV Scanner, CI templates | Builders can wire these up manually, but the raw output is noisy and not launch-decision oriented. |
| Indirect substitute | Ask ChatGPT/Claude to review code, or ask a security-minded friend | Fast but unreliable; may miss concrete scanner findings or hallucinate risk. |
| Status quo | Ship anyway and react if something breaks, leaks, or users complain | Common for tiny launches, especially when the app has no sensitive data yet. This lowers willingness to pay until stakes increase. |
| Wedge | Local-first “launch risk translator” for vibe-coded MVPs: it does not sell enterprise AppSec; it converts boring scanner output into a clear shippability report for one repo. |
| Kill condition | Reject or narrow further if incumbent tools offer a free, non-expert launch checklist that groups findings into shippability gates and works locally without account setup. |

## Wedge

The wedge is **translation and launch gating**, not detection. Semgrep, Snyk, GitHub, Aikido, and Gitleaks are better at scanning. VibeGuard would be useful if it makes a non-security founder understand whether they can safely launch this weekend. That is a smaller, more demoable job: run scanners, collapse noise, explain risk, and generate one public-safe report.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | The pain is credible and timely: AI-assisted builders are shipping code they did not fully write or review. |
| Feasibility | 4/5 | A 1-3 day MVP can wrap existing scanners and generate a static report for Node/Python web apps. |
| Demo potential | 4/5 | Strong before/after demo: scary raw scanner output becomes a clean launch gate report. |
| Distribution | 3/5 | Reachable in r/SideProject, indie hacker, Cursor/vibe-coding, and build-in-public circles, but trust is hard in security. |
| Competitive wedge / timing | 2/5 | Timing is strong, but direct competition is heavy and some incumbents already have AI/autofix positioning. The narrow local-first translator wedge keeps it alive but below build threshold. |
| Total | 17/25 | Save as idea-only today; do not create repo. |

## Decision

**Save as idea-only.** VibeGuard is the best idea from today’s public signals because it targets a real, timely workflow created by AI-assisted coding. It does **not** clear the 18/25 repo threshold because the broad category is crowded with mature scanner/autofix products and the strongest signal is a competitor-like SideProject post, not repeated independent user demand.

Create a repo only if a later signal confirms one of these narrower pains:

1. founders explicitly want a local launch-readiness report rather than another scanner dashboard,
2. existing tools overwhelm non-security builders with noisy output,
3. a spike shows the scanner-to-launch-gate translation is compelling on real public demo repos.

## Shortlist considered

| Idea | Source signal | Direct competitors | Indirect substitutes / status quo | Wedge | Kill condition | Score | Decision |
|---|---|---|---|---|---|---:|---|
| VibeGuard — local launch security check for vibe-coded apps | r/SideProject post about AI-generated code security holes and PR autofixes | Semgrep, Snyk Code, GitHub Advanced Security, Aikido, plus the poster’s own DebtMap-style tool | Gitleaks/CodeQL/audit scripts, asking an LLM/friend, shipping anyway | Translate scanner output into non-expert launch gates, local-first | Incumbents ship a free local “can I launch?” report for founders | 17/25 | Winner, idea-only |
| CutRoom Lite — open-source AI video editor profile for no-login export | r/SideProject Cutlass post complains that modern editors are bloated, paywalled, and require sign-in/export friction | CapCut, Premiere, DaVinci Resolve, Descript, Runway, VEED, OpusClip | Existing free editors, templates, CLI ffmpeg workflows | Narrow to privacy/no-account export for simple social clips | If Cutlass or another OSS editor already nails this UX | 15/25 | Hold; category is brutal |
| NoteBridge — cheap Dropbox-friendly notes sync checker | r/productivity user annoyed Obsidian mobile cannot view Dropbox-backed notes and subscriptions pile up | Joplin, Obsidian Sync, OneNote, Standard Notes, Logseq, Evernote | Plain files in Dropbox/iCloud, Markdown editors, manual copy/paste | Compatibility checker/migration guide rather than full notes app | Existing note apps already cover the user’s exact sync/budget needs | 13/25 | Reject as product; maybe content/tooling |
| ReviewTrust — verified feedback exchange without sketchy app-store gaming | r/SideProject user stuck at five reviews wants reciprocal app testing/reviews | IndieBoost, ASO Reviews, AppReview/ASO tools | Manual founder groups, Discords, friends, paid review farms | Shift from “5-star exchange” to usability feedback and proof-of-test | App-store policy risk or existing exchange platforms solve it | 10/25 | Reject; policy/quality risk |
| ScrollSwap — earn intentional entertainment by reducing phone scrolling | r/productivity teen wants to stop lying in bed scrolling so they can enjoy games/movies/comics | Cold Turkey, Opal, Freedom, One Sec, Screen Time/Digital Wellbeing | Delete apps, parental controls, willpower, blockers | Reward intentional entertainment instead of pure blocking | If existing blockers already support this reward loop well enough | 14/25 | Hold; consumer retention hard |
| FlipBrief — evidence-backed counterargument card for articles | r/SideProject browser extension finds counterarguments from public academic sources | Skeptic Reader/fact-checking extensions, Perplexity, generic LLM summarizers | Search manually, ask ChatGPT, read opposing publications | One-click “best opposing evidence” with citations | If output cannot avoid false balance or hallucinated relevance | 15/25 | Hold; trust burden high |

## Next build step

Do a 2-hour spike before any repo: run Gitleaks + Semgrep on a small public demo app with intentionally seeded issues, then generate a static `SECURITY_LAUNCH_REPORT.md` with three gates. If a non-security reader can decide what blocks launch in under one minute, rescore.

## Research access note

Reddit public JSON was blocked with `HTTP 403 theme-beta`, so the `reddit-readonly` script used RSS fallback where available. Some subreddit RSS calls returned `HTTP 429`, so the run stopped tight retries and used web search / product pages for competitor validation. X `whoami` worked, but `xurl search` returned `401 Unauthorized`, so X was not used as evidence today.
