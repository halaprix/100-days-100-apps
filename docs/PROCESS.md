# Daily Ideation Process

## Inputs

- Reddit posts and comments from the public subreddits in `sources.yml`.
- X/Twitter search results when `xurl` is authenticated and credits permit it.
- Web search as fallback when X search is unavailable.

## Output per day

Each daily run creates one markdown file in `ideas/`:

```text
ideas/YYYY-MM-DD-short-name.md
```

The daily file must include:

1. source evidence,
2. repeated pain point,
3. proposed app,
4. target user,
5. MVP scope,
6. scoring table,
7. go/no-go decision,
8. repo link if created.

## Scoring

| Dimension | Max | Meaning |
|---|---:|---|
| Usefulness | 5 | How painful and repeated the problem is |
| Feasibility | 5 | Can an MVP be built quickly with known tools? |
| Demo potential | 5 | Can it be shown clearly in a screenshot/GIF? |
| Distribution | 5 | Is there an obvious place to find users? |
| Novelty/timing | 5 | Is there a timely reason to build it now? |

Default threshold for creating a dedicated repo: **18/25**.

## Repo creation rule

Do not create a project repo just because a day passed. Create a repo when the idea clears the threshold or when Marian explicitly asks to build it.

## Privacy

This is a public build-in-public repository. Do not commit tokens, private infrastructure details, home paths, screenshots with personal data, or private conversations.
