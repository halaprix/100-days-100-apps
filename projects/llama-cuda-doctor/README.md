# Llama CUDA Doctor

A local CLI doctor for llama.cpp users that diagnoses NVIDIA driver, CUDA toolkit, `nvcc`, GPU compute-capability, and build-flag mismatches before they waste hours rebuilding blind.

## Problem

Local LLM builders on Linux can lose huge performance or fail builds because Ubuntu packages, NVIDIA drivers, CUDA toolkits, Python wheels, Docker images, and llama.cpp build flags drift independently. The failure mode is usually not obvious: a new Blackwell GPU can be compiled as an older architecture, `nvcc` may come from the wrong toolkit path, or a container may see the GPU while the host build does not.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/LocalLLaMA | https://www.reddit.com/r/LocalLLaMA/comments/1uif4g7/ubuntu_cuda_llamacpp_nvcc_versioning/ | Fresh post reports Ubuntu apt CUDA being too old for a Blackwell RTX 5060 Ti, incorrect compute capability, and roughly doubled performance after installing newer CUDA and rebuilding llama.cpp with the right path. |
| llama.cpp build docs | https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md | Official docs mention explicitly specifying CUDA architectures when `nvcc` cannot detect the GPU correctly. |
| llama.cpp Docker docs | https://github.com/ggml-org/llama.cpp/blob/master/docs/docker.md | Official Docker flow exposes CUDA version and GPU architecture build arguments; this validates a containerized escape hatch. |
| NVIDIA Blackwell compatibility guide | https://docs.nvidia.com/cuda/blackwell-compatibility-guide/index.html | NVIDIA documents toolkit/architecture compatibility requirements for Blackwell CUDA applications. |
| NVIDIA Developer Forums | https://forums.developer.nvidia.com/t/software-migration-guide-for-nvidia-blackwell-rtx-gpus-a-guide-to-cuda-12-8-pytorch-tensorrt-and-llama-cpp/321330 | NVIDIA guidance calls out CUDA 12.8+, compatible drivers, and llama.cpp-specific Blackwell migration advice. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | llama.cpp docs and GitHub issues | Authoritative, but users still have to connect driver, toolkit, architecture, Docker, and build-output clues manually. |
| Direct competitor | ai-dock/llama.cpp-cuda and other prebuilt CUDA binaries | Useful if a matching binary exists; less useful for source builds, unusual GPUs, mixed-GPU rigs, or diagnosing why a local build is slow. |
| Indirect substitute | `nvidia-smi`, `nvcc --version`, CUDA samples, Stack Overflow, forum posts | These expose facts, not a ranked fix plan. Users copy/paste commands across threads and rebuild repeatedly. |
| Status quo | Blind rebuilds and forum archaeology | Costs hours, can leave GPUs underutilized, and makes performance comparisons unreliable. |

## Wedge

Llama CUDA Doctor is not another llama.cpp installer. It wins by being a read-only diagnostic report: inspect the local environment, explain the mismatch in plain language, then print the exact next build command or Docker route for that machine.

## Target user

Linux local-LLM builders using NVIDIA GPUs with llama.cpp, llama-cpp-python, node-llama-cpp, or Docker images—especially RTX 50/Blackwell owners, mixed-GPU users, and people switching between distro CUDA packages and NVIDIA CUDA installers.

## MVP

- `llama-cuda-doctor report` gathers `nvidia-smi`, `nvcc`, CUDA paths, driver version, GPU names, compute capabilities, and relevant environment variables.
- Detect stale distro CUDA, unsupported/missing architecture flags, multiple CUDA installations, and Docker GPU-runtime gaps.
- Print a ranked fix plan: host rebuild, explicit CMake architecture flags, or NVIDIA Container Toolkit + llama.cpp Docker path.
- Support `--from-fixture` so reports can be demoed without local NVIDIA hardware.
- Export Markdown/JSON for GitHub issue attachments.

## Non-goals

- No driver installation or privileged system mutation in v0.1.
- No benchmarking claims without user-run evidence.
- No full llama.cpp package manager.
- No cloud GPU provisioning.

## Status

v0.1.0-alpha.0 — scaffold/spec only; local commit ready while GitHub push permissions are blocked.
