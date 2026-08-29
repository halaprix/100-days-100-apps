# SwapCheck agent instructions

- Keep the tool local and read-only. Never require GitHub credentials, call a
  GitHub API, edit Copilot policy, or execute prompts/models in the MVP.
- Treat policy exports, repository files, prompts, and completions as sensitive.
  Reports may emit relative file paths, line numbers, model IDs, and safe
  metadata only; never emit file contents, tokens, cookies, or prompt text.
- Use Beads for all work. Create and claim a bead before a product change; close
  it only after validation and commit.
- Use Conventional Commits. Ground model-retirement claims in public GitHub
  documentation, and label time-sensitive manifests with their source date.
- Run `python3 scripts/verify_scaffold.py` and `git diff --check` before
  claiming scaffold work complete.
