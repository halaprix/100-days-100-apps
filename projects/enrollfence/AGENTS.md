# EnrollFence agent instructions

- Keep every product capability local and read-only. Do not require tenant
  credentials, call Microsoft Graph, alter Intune policies, enroll devices, or
  collect live endpoint data.
- Treat every configuration export as sensitive. Fixtures and reports may use
  safe synthetic IDs and relative paths only; never commit tenant IDs, serial
  numbers, user names, tokens, cookies, raw exports, or screenshots.
- Preserve the distinction between a deterministic policy assessment and a
  security guarantee. Unknown or unsupported cases must remain `unknown`.
- Use Beads for task tracking and Conventional Commits for repository history.
- Run `python3 scripts/verify_scaffold.py` and `git diff --check` before
  claiming scaffold work complete.
