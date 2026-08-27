# Contributing

## Development principles

- Keep redirect decisions explainable and reviewable.
- Prefer deterministic local parsing over remote integrations.
- Do not add customer crawl exports, credentials, cookies, or real site content to tests.
- Add a regression fixture for every matching or export edge case.

## Before opening a pull request

1. Create and claim a Beads issue.
2. Run the relevant tests and the scaffold verifier.
3. Run `git diff --check`.
4. Use a Conventional Commit and describe validation in the pull request.

## Scope guard

RedirectLedger proposes and verifies mappings; it does not log into hosts, change DNS, or deploy redirect rules.