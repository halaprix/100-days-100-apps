# Local Workspace Layout

This repository is designed to live inside a local lab directory with a sibling folder for generated app repos.

```text
100-days-lab/
├── index/      # this master index repo
└── projects/   # dedicated repos for ideas that clear the creation gate
```

Rules:

- `index/` owns the daily briefs, scoring, source config, and master index.
- `projects/<repo-name>/` owns each real app repo.
- Do not put app implementation code inside `index/`.
- Do not commit absolute local filesystem paths into public-facing docs.
- Project repos get their own `.beads/`; the index repo keeps only incubator/index tasks.
