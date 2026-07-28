# Agent Instructions — CampaignPacket

## Mission

CampaignPacket is a small public CLI for preparing Microsoft Teams SMS / 10DLC campaign approval packets before admins resubmit rejected campaigns.

## Rules

- Keep the project public-safe: no tokens, private business data, real phone numbers, real customer names, addresses, screenshots, or campaign submissions in committed files.
- Use synthetic fixture data for examples and tests.
- Redact phone numbers, addresses, email addresses, client names, and private business details before printing shareable reports.
- Beads is the only task tracker. Use `bd ready`, `bd update <id> --claim`, and `bd close <id>`.
- Conventional Commits only. Do not add LLM co-author trailers.
- Prefer a tiny standard-library CLI before adding dependencies.
- Do not automate Teams Admin Center, send SMS, or imply approval is guaranteed.

## Verification

Before claiming completion, run:

```bash
bd list --json >/tmp/campaignpacket-beads.json
python3 scripts/verify_scaffold.py
git status --short --branch
git log --oneline --decorate -5
```
