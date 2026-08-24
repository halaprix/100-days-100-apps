# AssistCutover agent instructions

- Keep the tool local-only: never require API keys, upload source, or execute
  scanned project code.
- Treat repository paths and source contents as sensitive output. Reports may
  include relative paths and rule IDs, not excerpts, secrets, or environment
  values.
- Use Beads for all work tracking. Create and claim a bead before modifying
  product code; close it only after validation and commit.
- Use Conventional Commits. Keep public docs grounded in public vendor docs or
  clearly labeled community reports.
- Run the scanner against fixtures and run `scripts/verify_scaffold.py` before
  claiming a scaffold change complete.
