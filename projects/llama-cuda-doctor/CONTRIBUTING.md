# Contributing

Thanks for helping make local CUDA diagnostics less painful.

## Ground rules

- Keep checks read-only unless a future spec explicitly introduces guarded fix commands.
- Add tests or fixtures for every parser and recommendation rule.
- Do not paste unsanitized system reports into issues or commits.
- Use Conventional Commits.

## Local workflow

```bash
bd ready
bd update <id> --claim
# make changes
bd close <id> --reason "Done in <commit>"
git add .
git commit -m "feat: add diagnostic rule"
```

## Useful issue reports

A good report includes:

- GPU model(s), with serials removed if present.
- Driver version.
- CUDA toolkit version and `nvcc` path.
- llama.cpp or binding being built.
- Sanitized `llama-cuda-doctor export --format markdown` output.
