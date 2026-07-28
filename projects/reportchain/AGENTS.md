# Agent Instructions — ReportChain

ReportChain is a public, privacy-safe Microsoft 365 admin utility. Treat every artifact as public.

## Scope

Build a read-only-first CLI that helps admins preview manager/direct-report mailing-list structures and generate command packets. The project must not store credentials or mutate a Microsoft 365 tenant by default.

## Public-safety rules

Allowed:

- Public documentation links.
- Synthetic fixture data.
- Generic command examples using placeholder domains such as `example.com`.

Forbidden:

- Real tenant IDs, user exports, email lists, access tokens, OAuth details, session dumps, or screenshots from private tenants.
- Private infrastructure details or local machine paths.
- Any command that writes to a live tenant without an explicit user request and a dry-run preview.

## Git workflow

- Conventional Commits only.
- One logical change per commit.
- Push after commits when credentials permit.
- Never force-push `main`.
- No LLM co-author trailers.

## Build posture

- Prefer simple Python with deterministic fixture tests.
- Keep live Graph access optional and isolated.
- Tests must run without network access and without credentials.
- Default behavior must be read-only/dry-run.
