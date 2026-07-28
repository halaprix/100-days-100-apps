# SPEC — Llama CUDA Doctor

## User story

As a Linux local-LLM builder with an NVIDIA GPU, I want a read-only diagnostic that tells me whether my driver, CUDA toolkit, `nvcc`, compute capability, and llama.cpp build flags agree, so that I can fix slow or failing CUDA builds without spending hours in forum threads.

## Core flow

1. User runs `llama-cuda-doctor report` in a terminal.
2. The CLI collects command outputs from `nvidia-smi`, `nvcc --version`, `which nvcc`, CUDA install paths, selected environment variables, and optional llama.cpp build/cache files.
3. The analyzer normalizes GPU names, expected compute capability, driver/toolkit compatibility, and current build target clues.
4. The report prints:
   - detected facts,
   - likely mismatch,
   - confidence,
   - exact next command or docs link,
   - optional Docker escape hatch.
5. User can run `llama-cuda-doctor export --format markdown` and attach the report to a GitHub/forum support request.

## Data model

```text
GpuInfo
- name
- driver_version
- detected_compute_capability
- expected_compute_capability
- source

CudaInstall
- nvcc_path
- nvcc_version
- toolkit_root
- source_hint: distro | nvidia-installer | conda | unknown

BuildContext
- project: llama.cpp | llama-cpp-python | node-llama-cpp | unknown
- cmake_cache_path
- cuda_architectures
- docker_context

Finding
- severity: info | warning | critical
- title
- evidence
- recommendation
- confidence
```

## Technical approach

- Implement as a Python CLI first: fast enough, easy subprocess handling, no compile step.
- Keep system commands read-only; never install drivers/toolkits or edit shell profiles.
- Ship a small GPU capability map for common NVIDIA architectures, including Blackwell/RTX 50-series entries where public docs identify the target.
- Parse known build contexts:
  - llama.cpp CMake cache/build logs,
  - `CMAKE_CUDA_ARCHITECTURES`,
  - `CUDA_DOCKER_ARCH`,
  - `CMAKE_CUDA_COMPILER`,
  - `GGML_CUDA`/legacy flags when present.
- Provide fixture files for tests and demos so CI does not need NVIDIA hardware.

## Validation plan

- Unit-test parsers with captured/synthetic outputs for:
  - stale distro CUDA,
  - Blackwell GPU with old toolkit,
  - multiple CUDA installations,
  - missing NVIDIA Container Toolkit,
  - mixed-GPU build architecture choices.
- Compare generated recommendations against official NVIDIA and llama.cpp docs.
- Demo on fixture input first, then request real reports from r/LocalLLaMA/llama.cpp users.
- Wedge validation: users should say the report would have reduced at least one rebuild or support-thread round trip.

## Milestones

- v0.1.0-alpha.0 — repo scaffold.
- v0.1.0-alpha.1 — parser skeleton, fixture runner, Markdown report.
- v0.1.0-alpha.2 — llama.cpp CMake/build-context checks.
- v0.2.0-alpha.1 — real-machine beta with anonymized report export.
