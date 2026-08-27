# RedirectLedger agent instructions

- Keep all commands local-first and read-only by default. Never require WordPress, DNS, CDN, analytics, or hosting credentials.
- Treat site URLs, titles, headings, canonicals, and crawl exports as potentially sensitive customer data. Fixtures must be synthetic; reports must not include cookies, response bodies, tokens, or private hostnames.
- Never deploy redirect rules. Generate review artifacts and exports only after explicit human approval is represented in the mapping file.
- Use Beads for project tasks. Create and claim a bead before a product change; close it only after validation, commit, and push status are verified.
- Use Conventional Commits and ground public product claims in fetchable sources.
- Before completion, run the scaffold verifier and fixture tests when they exist.