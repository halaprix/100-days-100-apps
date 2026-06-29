# Day 011 — Llama CUDA Doctor

Date: 2026-06-29
Status: blocked

## One-line pitch

A read-only CLI doctor that diagnoses NVIDIA driver, CUDA toolkit, `nvcc`, GPU compute-capability, and llama.cpp build-flag mismatches before local-LLM users waste hours rebuilding blind.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/LocalLLaMA | https://www.reddit.com/r/LocalLLaMA/comments/1uif4g7/ubuntu_cuda_llamacpp_nvcc_versioning/ | Fresh thread: Ubuntu apt CUDA was too old for a Blackwell RTX 5060 Ti, the setup effectively targeted the wrong compute capability, and performance roughly doubled after installing newer CUDA and rebuilding llama.cpp with the right path. |
| llama.cpp build docs | https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md | Official docs call out explicit CUDA architecture selection when `nvcc` cannot detect the GPU correctly; this validates the diagnostic surface. |
| llama.cpp Docker docs | https://github.com/ggml-org/llama.cpp/blob/master/docs/docker.md | Official Docker flow exposes CUDA version and GPU architecture build args, validating a container-based escape hatch for users stuck in host toolkit conflicts. |
| NVIDIA Blackwell compatibility guide | https://docs.nvidia.com/cuda/blackwell-compatibility-guide/index.html | NVIDIA documents toolkit and architecture compatibility requirements for Blackwell CUDA applications. |
| NVIDIA Developer Forums | https://forums.developer.nvidia.com/t/software-migration-guide-for-nvidia-blackwell-rtx-gpus-a-guide-to-cuda-12-8-pytorch-tensorrt-and-llama-cpp/321330 | NVIDIA migration guidance names CUDA 12.8+, compatible drivers, and llama.cpp-specific Blackwell setup concerns. |
| GitHub / llama.cpp issue | https://github.com/ggml-org/llama.cpp/issues/13271 | Public issue shows `compute_120` / old CUDA-version confusion: the same class of failure appears in support channels, not just one Reddit post. |
| GitHub / llama-cpp-python issue | https://github.com/abetlen/llama-cpp-python/issues/2028 | Public issue documents a Blackwell RTX 5060 Ti user needing source-build workarounds for CUDA acceleration. |

## Problem

Local LLM builders on Linux do not have one coherent source of truth for “is my NVIDIA stack actually correct for this llama.cpp build?” Ubuntu packages, NVIDIA drivers, CUDA installers, Python wheels, Docker images, and llama.cpp CMake flags all drift separately. The resulting failure can look like a slow model, a vague `nvcc` error, a binary compiled for the wrong architecture, or a container that sees the GPU while the host build does not.

The status-quo pain clears the threshold: a bad setup can waste multiple rebuild cycles, cost hours of forum archaeology, create misleading benchmark results, and leave expensive GPUs underutilized.

## Target user

Linux local-LLM builders using NVIDIA GPUs with llama.cpp, llama-cpp-python, node-llama-cpp, or Docker images—especially RTX 50/Blackwell owners, mixed-GPU users, and people switching between distro CUDA packages and NVIDIA CUDA installers.

## MVP scope

- `llama-cuda-doctor report` runs read-only checks: `nvidia-smi`, `nvcc --version`, `which nvcc`, CUDA install paths, selected environment variables, optional llama.cpp CMake cache/build logs, and Docker GPU-runtime hints.
- Normalize GPU names, detected/expected compute capability, driver version, CUDA toolkit version, and current build architecture flags.
- Detect common mismatches:
  - distro CUDA too old for the GPU,
  - `nvcc` path points to a different toolkit than expected,
  - missing or wrong `CMAKE_CUDA_ARCHITECTURES` / `CUDA_DOCKER_ARCH`,
  - mixed-GPU architecture ambiguity,
  - Docker path available but NVIDIA Container Toolkit not configured.
- Print a ranked fix plan with exact next command shape: host rebuild, explicit CMake flags, or containerized llama.cpp route.
- `--from-fixture` mode for demos and CI without local NVIDIA hardware.
- Markdown/JSON export safe for GitHub issues after redacting home-directory usernames and private hostnames.

Non-goals for v0.1: driver installation, privileged system mutation, benchmarking claims without user-run evidence, or becoming a full llama.cpp package manager.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | llama.cpp docs and GitHub issues | Authoritative and current, but users still have to join driver, toolkit, architecture, Docker, and build-cache clues by hand. |
| Direct competitor | NVIDIA CUDA / Blackwell docs and developer forum guides | Correct for compatibility, but not tailored to the user’s actual local llama.cpp or binding setup. |
| Direct competitor | ai-dock/llama.cpp-cuda and other prebuilt CUDA binaries | Useful when the user can use a matching binary; weaker for source builds, unusual GPUs, mixed-GPU rigs, Python bindings, or diagnosing why a local build is slow. |
| Indirect substitute | `nvidia-smi`, `nvcc --version`, CUDA samples, Stack Overflow, Reddit, forum posts | These expose facts and scattered advice, not a ranked machine-specific fix plan. |
| Status quo | Blind rebuilds and forum archaeology | Costs hours, creates noisy support threads, and can leave GPUs underutilized while appearing “working.” |

## Wedge

**Wedge-first line:** local-LLM builders with NVIDIA Linux boxes, especially Blackwell/mixed-GPU users → llama.cpp/NVIDIA docs, prebuilt CUDA binaries, `nvidia-smi`, `nvcc`, Stack Overflow, Reddit, and GitHub issues → each substitute exposes only part of the stack and users still rebuild blind → read-only “doctor report” that correlates the local driver/toolkit/GPU/build context and prints the next exact build or Docker path → r/LocalLLaMA, llama.cpp/llama-cpp-python issue searches, setup-guide SEO, and reply strategy on CUDA build failures → RTX 50/Blackwell migration and fast-moving llama.cpp CUDA defaults are producing fresh confusion now.

The product wins by being a diagnostic adapter, not an installer. It can be useful even when the final answer is “use the official Docker path” or “your distro CUDA is the wrong `nvcc`.”

## Kill condition

Reject or narrow if llama.cpp and binding maintainers ship an official `doctor` command that covers driver/toolkit/GPU/build-context checks, if prebuilt binaries become the dominant path for the target users, or if accurate recommendations require privileged hardware probing that a safe read-only CLI cannot do.

## Shortlist notes

| Candidate | Wedge-first gate result | Score | Decision |
|---|---|---:|---|
| Llama CUDA Doctor | NVIDIA local-LLM builders → docs, prebuilt binaries, `nvidia-smi`/`nvcc`, GitHub issues → facts are scattered and rebuild loops are expensive → read-only environment/build doctor with exact next command → r/LocalLLaMA, llama.cpp issue searches, setup-guide SEO → Blackwell/CUDA migration is actively causing confusion. | 19/25 | Winner. Clears repo-creation threshold and gates; remote repo created, local scaffold push blocked by GitHub 403. |
| DeReact Map | Design-system maintainers with a React/Emotion library needing non-React consumers → web components, Stencil, Lit, Mitosis, rewrites, SSR/static extraction → complex stateful React cannot be magically exported and teams need a migration map → CLI audit that splits tokens/simple components/complex wrappers → r/webdev/design-system content and search around “React library non-React consumers” → fresh thread shows this exact decision pain. | 17/25 | Held. Strong pain, but feasibility and proof need a real component corpus; no repo. |
| WPPulseboard | Small operators managing several WordPress/WooCommerce/booking sites → email notifications, ManageWP/MainWP/WP Remote, plugins, Zapier → broad site-management tools exist, but small operators still ask whether dashboard checking is normal → tiny cross-site event inbox focused only on orders/forms/bookings → WordPress agency/plugin channels → fresh SideProject post asks about the workflow. | 16/25 | Held. Useful, but WordPress management/notification competitors are strong. |
| StoryDelta | News-product builders/readers dealing with duplicate coverage → Google News, NewsBlur story clustering, RSS readers, AI digests → duplicate grouping and timeline/context are real pain, but consumer news is crowded and trust is hard → source-linked story timeline primitive for RSS power users → RSS/news-tool communities → fresh builder post names the clustering pain. | 14/25 | Rejected. Crowded AI/news-digest category and weak first-user channel. |
| Agent Email Replaybench | Agent workflow builders using email/OTP/reply flows → Lumbox, AgentMail-style inboxes, custom test mailboxes, mocks → infrastructure APIs break when wait/reply semantics change → fixture-based contract tests for email-agent APIs → r/n8n, r/AI_Agents, agent-infra builders → fresh Lumbox post says API semantics caused early breaking changes. | 16/25 | Held. Good adjacent pain, but direct infrastructure products already own the channel. |

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | The workaround can waste hours and distort performance on expensive GPUs; the fresh thread reports a roughly doubled result after fixing the stack. |
| Feasibility | 4/5 | A read-only parser/report CLI with fixtures is buildable in 1–3 days. Real hardware coverage can grow incrementally from user-submitted reports. |
| Demo potential | 4/5 | Strong terminal demo: feed a Blackwell/stale-CUDA fixture and show a clear mismatch plus exact CMake/Docker recommendation. |
| Distribution | 4/5 | Specific channels exist: r/LocalLLaMA, llama.cpp and binding GitHub issues, CUDA setup search traffic, and reply-worthy support threads. |
| Competitive wedge / timing | 3/5 | Docs and prebuilt binaries are strong substitutes, but no obvious lightweight “doctor” owns the machine-specific diagnosis layer. Timing is strengthened by Blackwell/RTX 50 migration. |
| Total | 19/25 | Clears total, distribution, and wedge gates. |

## Decision

Create the dedicated project scaffold for Llama CUDA Doctor, but mark the day `blocked` rather than cleanly `repo-created`: the GitHub repository was created at https://github.com/halaprix/llama-cuda-doctor, the local scaffold commit is ready (`aa6a7ab`), and `git push` failed with GitHub HTTP 403 (`Permission to halaprix/llama-cuda-doctor.git denied to halaprix`).

## Next build step

Implement the first runnable slice: Python CLI skeleton, fixture loader, parsers for `nvidia-smi`/`nvcc`/CMake cache snippets, and a Markdown report that flags stale CUDA and missing architecture flags without requiring NVIDIA hardware in CI.

## Research access note

Reddit public JSON was blocked in this environment; the run used the reddit-readonly RSS fallback for r/SideProject, r/webdev, and r/LocalLLaMA, while several configured subreddits returned RSS `HTTP 429` and were not retried. X search was attempted through `xurl` and returned `401 Unauthorized`, so X was not used as evidence. Competitor/substitute checks used web search and public docs/product pages.
