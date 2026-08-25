# VariantGuard agent instructions

- Keep checks local and read-only: never require Cloudflare credentials or apply
  Cache Rules automatically.
- Treat URLs, request headers, and response bodies as sensitive. Reports may
  include a sanitized URL, selected safe headers, body hashes, and rule IDs;
  never include response bodies, cookies, authorization, or embedded secrets.
- Use Beads for work tracking. Create and claim a bead before product changes;
  close it only after validation and commit.
- Use Conventional Commits and ground product claims in public sources.
- Run fixture tests and `scripts/verify_scaffold.py` before claiming scaffold
  changes complete.
