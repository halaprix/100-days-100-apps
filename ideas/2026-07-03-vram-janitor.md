# Day 015 — VramJanitor

Date: 2026-07-03
Status: repo-created
Repo: https://github.com/halaprix/vram-janitor

## One-line pitch

A local-first CLI that finds reclaimable desktop VRAM before you launch a local LLM.

## Source access caveats

- Reddit public JSON was blocked for the main collection pass; `reddit-readonly` used RSS fallback for r/SideProject, r/startups, and r/LocalLLaMA. RSS fallback scores/comment counts are unavailable and treated as meaningless.
- Several configured subreddits returned Reddit RSS `HTTP 429`, so web search fallback was used for competitor/substitute validation.
- X/Twitter `xurl auth status` showed the default app has no OAuth2 token; `xurl search` returned `401 Unauthorized`, so no X evidence was used.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/LocalLLaMA | https://www.reddit.com/r/LocalLLaMA/comments/1um5ik2/pay_attention_a_few_chats_waiting_in_tray_reserve/ | Fresh post says minimized hardware-accelerated apps such as Discord, Steam, Telegram, and other apps reserved 1 GB+ VRAM; the workaround is manually checking `nvidia-smi`, closing apps, or disabling acceleration. |
| DigitalOcean tutorial | https://www.digitalocean.com/community/tutorials/monitoring-gpu-utilization-in-real-time | Current GPU-monitoring guidance starts with `nvidia-smi --loop=1`, `nvidia-smi pmon`, `nvtop`, and `gpustat`; these are primitives, not a local-LLM launch preflight. |
| nvitop | https://github.com/XuehaiPan/nvitop | Mature interactive NVIDIA process viewer with thousands of stars; strong substitute for visibility, but not a narrow reclaim plan for fitting a model/context. |
| LACT | https://github.com/ilya-zlobintsev/LACT | Mature Linux GPU configuration and monitoring GUI; broader than a one-command local LLM VRAM cleanup check. |
| LLM Configurator | https://llmconfigurator.com/ | Shows active demand for GPU/VRAM fit checks for private local LLMs, but focuses on model/hardware compatibility rather than currently reclaimable desktop VRAM. |

## Problem

Local LLM users on desktop Linux frequently operate near the VRAM limit. A few minimized hardware-accelerated apps can reserve hundreds of MiB each. When a model barely fails to fit, the user has to inspect raw GPU process output, guess which PIDs are safe to close, retry inference, lower context size, pick a worse quant/model, or reboot.

The status quo is tolerable for experts once, but bad as a repeated workflow: it wastes setup/debug time, makes benchmark comparisons noisy, and can cause unnecessary hardware/model compromises.

## Target user

Linux desktop users running Ollama, llama.cpp, LM Studio, vLLM, or similar local inference stacks on NVIDIA GPUs, especially 8–24 GB cards where 0.5–2 GB of reclaimable desktop VRAM changes which model/context fits.

## MVP scope

- CLI: `vram-janitor scan`.
- Parse `nvidia-smi` process memory output and map PIDs to process names.
- Classify likely reclaimable desktop/browser/chat/game-launcher processes versus model runtimes and unknown CUDA jobs.
- Optional `--target-free-mib` / `--model-budget-mib` to answer whether reclaiming listed apps changes the launch decision.
- Safe action plan only: close app, disable hardware acceleration, use a non-accelerated browser profile, or retry after freeing memory.
- Redacted markdown report for support threads; no telemetry and no automatic process killing in v0.1.

## Shortlist and wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| VramJanitor | Local LLM desktop users near VRAM limits → `nvidia-smi`, nvitop, nvtop, LACT, manual app closing → general tools show processes but do not say which desktop apps are safe/relevant to reclaim before a model launch → one-command LLM preflight with reclaim estimate and safe action plan → r/LocalLLaMA posts, GitHub README demos, searchable "Discord/Steam VRAM local LLM" guides → local model sizes and desktop GPU pressure keep increasing. | Winner; narrow software wedge and concrete community distribution. |
| ToolGate Lite | Solo agent/MCP users adding many MCP servers → Toolport, MCP gateways, Docker MCP Gateway, security scanners → enterprise gateways are broad and crowded; solo users want local visibility/token-tax/security without adopting a platform → local read-only MCP manifest diff and token-cost report → r/LocalLLaMA/MCP security posts → MCP tool poisoning/rug-pull discourse is hot. | Rejected for today: crowded MCP gateway/security space; Toolport post already covers much of the wedge. |
| ReminderBell | Android users wanting a loud simple reminder → Samsung Reminders, Google Calendar/Tasks, reminder apps → built-in apps add clutter or fail preference fit → stripped-down alarm-first reminder with no tracking widgets → r/androidapps request thread → user explicitly wants less product surface. | Rejected: reminder/todo category is crowded and status-quo pain is annoyance, not clearly >30 min/week or revenue/security risk. |
| CodeAirlock Notes | Developers running AI coding agents → code-airlock, Docker Sandboxes, E2B, devcontainers, manual approvals → existing project from the source post already implements the core microVM idea → maybe a diff-review companion, not another sandbox → SideProject/agent dev channels → agent autonomy/security tension is timely. | Rejected: source post is itself a direct competitor; no fresh wedge strong enough today. |
| RagShape Lab | RAG builders debugging retrieval quality → Ragas, DeepEval, LlamaIndex evaluators, ad-hoc notebooks → generic evals underweight document-shape transformations → fixture-first benchmark for row/document shaping before model tweaks → r/LocalLLaMA RAG benchmark post and RAG dev content → document-shape insight is timely. | Idea-only runner-up; good insight, but evidence is one benchmark post and eval tooling is crowded. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | `nvidia-smi`, `nvidia-smi pmon`, `nvtop`, `nvitop`, `gpustat` | Excellent for visibility. They still leave local LLM users to identify safe-to-close desktop apps, estimate reclaimable VRAM, and decide whether the model/context can now fit. |
| Direct competitor | LACT and broader Linux GPU dashboards | Strong monitoring/configuration tools. Their scope is GPU control, not local LLM launch preflight and report generation. |
| Indirect substitute | Shell one-liners, process killing, disabling app hardware acceleration manually | Works for experts but is brittle, vendor-specific, and easy to forget. It also produces raw output that is awkward to paste into support threads safely. |
| Indirect substitute | LLM Configurator-style VRAM calculators | Useful for model/hardware fit, but they usually assume available VRAM rather than measuring what is currently reclaimable on the desktop. |
| Status quo | Close random apps, lower context/model size, accept slower CPU/RAM offload, or reboot | Wastes repeated setup time and can push users into worse models or unnecessary hardware conclusions. |

## Wedge

VramJanitor should not become another GPU dashboard. The wedge is a narrow preflight question:

> Before I launch this local model, what reclaimable desktop VRAM is blocking me, and what safe manual steps should I take?

That gives it a reason to exist beside strong incumbents. It wraps known primitives into a local-LLM-specific answer, keeps setup local, avoids privileged actions, and produces a small redacted report users can paste into r/LocalLLaMA or GitHub issues.

## Kill condition

Kill or narrow if early users only want a general GPU dashboard, automatic process killing, or overclock/fan controls. Also kill if `nvitop`, LACT, or Ollama/LM Studio ship an equivalent local-LLM preflight/reclaim report, because the standalone wedge would collapse.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Fresh LocalLLaMA evidence shows 1 GB+ VRAM lost to background apps; the workaround can waste repeated setup time and cause bad model/hardware decisions. |
| Feasibility | 5/5 | A 1-3 day MVP can parse `nvidia-smi`, classify common desktop apps, and export a report using fixture tests. |
| Demo potential | 4/5 | Easy terminal demo: before/after scan, reclaim estimate, model-budget threshold, redacted markdown output. |
| Distribution | 4/5 | Specific r/LocalLLaMA threads, GitHub README demos, and search-driven troubleshooting content provide a concrete path beyond generic launch posts. |
| Competitive wedge / timing | 3/5 | Strong monitoring incumbents exist, but they do not own the local-LLM reclaim-before-launch workflow. Timing is good because local models and desktop GPU pressure keep growing. |
| Total | 20/25 | Clears repo threshold and gates. |

## Decision

Create the dedicated repo because VramJanitor scored 20/25, Distribution is 4/5, and Competitive wedge / timing is 3/5.

Repo created, scaffold pushed, and tagged: https://github.com/halaprix/vram-janitor

## Next build step

Implement `vram-janitor scan` with fixture-based parsing of `nvidia-smi` CSV output, a first-pass desktop-app classification table, `--target-free-mib`, and redacted markdown report export.
