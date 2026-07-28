# Contributing

DeskPatch is early-stage. Contributions should preserve the security model before adding features.

## Development rules

- Use Beads for task tracking.
- Use Conventional Commits.
- Keep changes small and reviewable.
- Add or update validation steps for security-sensitive changes.

## Security-sensitive areas

Discuss and document design before changing:

- manifest signature verification,
- command allowlisting,
- installer download and hash verification,
- Windows service permissions,
- audit log format.

Do not add features that run arbitrary commands or store admin credentials.
