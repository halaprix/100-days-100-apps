# Day 054 — PushBench

Date: 2026-08-14
Status: repo-created
Repo: [`projects/pushbench`](../projects/pushbench)

## One-line pitch

PushBench is a local benchmark harness and cost packet for choosing ntfy vs Autopush/Sunup as a self-hosted UnifiedPush backend before real Android users depend on it.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1vnwk04/nfty_vs_autopush_for_degoogled_android_push/ | Fresh self-hosted post asks whether ntfy or Autopush is better for de-Googled Android push notifications, specifically performance, operating cost, and thousands of daily users. |
| UnifiedPush docs / Distributors | https://unifiedpush.org/users/distributors/ | UnifiedPush says users choose a distributor and may self-host the push server; ntfy, NextPush, XMPP rewrite proxies, and Sunup/Autopush are documented options. |
| UnifiedPush docs / ntfy | https://unifiedpush.org/users/distributors/ntfy/ | ntfy is documented as an Android UnifiedPush distributor that can use the public server or a self-hosted server; server technology includes WebSockets or HTTP JSON streaming. |
| UnifiedPush docs / self-hosted ntfy troubleshooting | https://unifiedpush.org/users/troubleshooting/self-hosted-ntfy/ | Self-hosted ntfy operators hit ACL, rate-limit, reverse-proxy, and Matrix gateway issues, including 429 messages from rate limits. |
| Mozilla Autopush docs | https://mozilla-services.github.io/autopush-rs/ | Autopush-rs is a Rust Mozilla Push server using WebSockets and HTTP endpoints, with deployment and reliability docs but no UnifiedPush operator sizing packet. |
| k6 WebSocket docs | https://grafana.com/docs/k6/latest/using-k6/protocols/websockets/ | Generic load-test tools can test WebSocket traffic, but operators still need UnifiedPush-specific registration/publish/receive scenarios and cost interpretation. |

## Problem

People running de-Googled Android or Linux push setups have to choose between ntfy, Autopush/Sunup, Gotify-like routes, and default public servers. The painful question is not “can it run?” but “what happens when this has hundreds or thousands of daily users, slow mobile clients, reconnect storms, ACL/rate-limit constraints, and limited VPS resources?”

The status quo is anecdotal forum advice, generic load-test tools, or running one backend until missed notifications or infrastructure costs become visible. That can waste days of setup and create public embarrassment when messages silently delay, 429, or disappear after users have already switched.

## Target user

Self-hosted UnifiedPush operators, de-Googled Android community maintainers, small app communities, and privacy-focused service admins deciding whether to run ntfy, Autopush/Sunup, or another push backend for real users.

## MVP scope

- Read a YAML load profile: concurrent devices, reconnect rate, publish rate, payload sizes, retention/cache settings, target latency SLO, and monthly VPS budget.
- Generate backend-specific synthetic scenarios for ntfy HTTP/WebSocket and Autopush-style WebSocket + HTTP push paths.
- Run against local Docker Compose fixtures first; no public push service abuse and no default-server load tests.
- Emit a deterministic markdown/JSON “push readiness packet” with throughput, p50/p95 latency, error/429 rate, rough CPU/RAM/network envelope, and a plain-English recommendation.
- Include safe defaults, tiny local fixtures, and warnings when a profile would hit public/default servers.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | ntfy server docs and troubleshooting | Good for configuring ntfy and diagnosing ACL/rate-limit/proxy issues, but not a repeatable apples-to-apples sizing packet across ntfy and Autopush. |
| Direct competitor | Mozilla Autopush-rs docs | Strong server documentation for Autopush architecture and deployment, but not a UnifiedPush operator benchmark harness or VPS cost recommender. |
| Direct competitor | Generic load-test tools such as k6 and Locust | Powerful for HTTP/WebSocket traffic, but the user must hand-build UnifiedPush-specific registration, reconnect, publish, receive, and rate-limit scenarios. |
| Indirect substitute | Forum anecdotes, one-off scripts, public-server trial, Grafana dashboards after deployment | Useful after the fact; weak before choosing a backend because test profiles and cost assumptions are not comparable. |
| Status quo | Pick ntfy because it is easy, or Autopush because it sounds faster, then discover latency, 429, memory, or operational limits with real users | Fast for hobby use, but risky for small communities where missed push notifications are visible and trust-damaging. |

## Wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| PushBench | Self-hosted UnifiedPush operators choosing ntfy vs Autopush/Sunup → docs, generic k6/Locust tests, forum anecdotes → substitutes do not encode UnifiedPush registration/reconnect/publish/receive patterns or cost envelopes → local-only benchmark harness plus markdown sizing packet → r/selfhosted, UnifiedPush/GrapheneOS/de-Googled Android setup threads, and search content for “ntfy vs Autopush” → fresh post asks exactly for performance/cost at thousands of users | Winner; clear niche, concrete first-user path, and a buildable CLI/demo. |
| RestoreProof | Self-hosters validating full restores → restic/Kopia/Duplicati, BackupProof, Docker Compose notes → existing tools cover backup readiness but not always a one-service isolated restore rehearsal → service-level restore drill plan from Compose labels → r/selfhosted backup threads and search content → fresh “how often do you test full restore?” post | Held; useful, but prior backup ideas and BackupProof narrow the wedge. |
| Port443Mux Doctor | pfSense/HAProxy users sharing TCP/443 with OpenVPN → HAProxy forum/blog configs, Netgate threads, manual packet tests → SSL offload vs TCP passthrough confusion is easy to miss → read-only protocol classifier and safe HAProxy layout explainer → r/selfhosted/pfSense/OpenVPN searches → fresh DPI/cruise access thread | Held; technical pain is real, but route can drift toward censorship/VPN evasion and docs already cover much of it. |
| ShareVault Plan | Non-technical small-office self-hosters storing client and personal files → OMV/TrueNAS/Synology ACL guides, Samba docs → raw permission models are confusing for mixed client/personal privacy needs → simple YAML-to-Samba/OMV permission plan and checklist → OMV/selfhosted beginner threads → fresh financial-consultant home-server post | Idea-only; risk is high, but direct NAS products already own this workflow and distribution is mostly beginner support. |
| PromptParity | Local LLM users seeing same model differ across harnesses → promptfoo, lm-eval-harness, Inspect, LangSmith, manual parameter diffs → generic eval tools are heavy for one prompt/harness mismatch → tiny harness-diff packet for system prompt, template, params, stop tokens → LocalLLaMA model-release threads → fresh DeepSeek harness variance post | Rejected for this run; LLM eval/observability is crowded and the first-user channel is weaker than PushBench. |

## Wedge

PushBench wins by being narrower than generic load testing and more decision-oriented than backend docs. It does not try to become a monitoring dashboard or hosted push provider. The first slice only answers: “given this local profile, which backend survives, where does it fail, and what monthly VPS class is plausible?” That makes the output useful before migration, public rollout, or community recommendation.

## Kill condition

Reject or narrow if an existing UnifiedPush project already ships a maintained ntfy-vs-Autopush benchmark suite with realistic reconnect/publish/receive scenarios and cost guidance, or if first users say their backend choice is dominated by app compatibility rather than performance/cost. Also reject any MVP direction that load-tests public/default push servers instead of local fixtures.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Missed or delayed notifications hurt trust, and backend migration after users opt in is annoying; evidence asks directly about performance/cost at scale. |
| Feasibility | 4/5 | A local Docker Compose fixture, YAML profile, WebSocket/HTTP runner, and markdown report are buildable in 1–3 days. |
| Demo potential | 4/5 | Strong demo: run the same profile against fixture backends and show a pass/fail/cost packet. |
| Distribution | 4/5 | Specific channels exist: r/selfhosted, de-Googled Android/GrapheneOS discussions, UnifiedPush setup/troubleshooting searches, and ntfy-vs-Autopush comparison content. |
| Competitive wedge / timing | 4/5 | Backend docs and generic load tools exist, but no obvious lightweight UnifiedPush decision packet surfaced; fresh post asks for this comparison now. |
| Total | 20/25 | Clears repo threshold and both dimension gates. |

## Decision

Create repo. PushBench scored 20/25 with distribution 4/5 and competitive wedge/timing 4/5, so it clears the creation gates. Scaffold/spec snapshot was added under `projects/pushbench`; no dedicated GitHub remote was created during this local-first run.

## Next build step

Implement `pushbench run --profile fixtures/load-profile.yml --backend ntfy --out report.md` against a local fixture backend, then add the Autopush profile adapter and compare both outputs in one packet.

## Source access caveats

Reddit public JSON was blocked for r/selfhosted and the run used `reddit-rss-fallback`; RSS score/comment counts are reported as zero and were not used for ranking. Several Reddit subreddit probes hit `HTTP 429`, so web search and original docs were used for competitor validation. X/Twitter `whoami` worked, but `xurl search` returned `401 Unauthorized`; no X data was used and no social writes were attempted.
