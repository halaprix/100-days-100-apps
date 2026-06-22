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

The output must be an **app/software bet**: SaaS, CLI, developer tool,
browser extension, local-first automation, or similar software MVP. Commodity
physical products, merch, gift SKUs, and ecommerce arbitrage ideas are out of
scope for this repo unless Marian explicitly asks for that kind of research.

The daily file must include:

1. source evidence,
2. repeated pain point,
3. proposed app,
4. target user,
5. MVP scope,
6. competitor/substitute check,
7. wedge or kill condition,
8. scoring table,
9. go/no-go decision,
10. repo link if created.

## Competitor/substitute check

Run this before scoring every shortlisted idea. Competition is whatever the target user would choose instead, not only same-category startups.

Minimum fields:

| Type | Question |
|---|---|
| Direct competitors | Which products already solve the same job? |
| Indirect substitutes | Are users using spreadsheets, Notion, scripts, agencies, generic tools, or manual workflows? |
| Status quo | What happens if the user does nothing new? |
| Wedge | Why can a 1-3 day MVP still get attention? |
| Kill condition | What evidence would make us reject or narrow the idea? |

If there is no credible wedge, mark the idea `rejected` or narrow it before scoring.

If the idea is a physical accessory whose best route is Alibaba/Amazon sourcing
and branding, mark it `rejected` for this repo even if it is commercially
plausible as a SKU. This repository is not a generic product-import lab.

## Scoring

| Dimension | Max | Meaning |
|---|---:|---|
| Usefulness | 5 | How painful and repeated the problem is |
| Feasibility | 5 | Can an MVP be built quickly with known tools? |
| Demo potential | 5 | Can it be shown clearly in a screenshot/GIF? |
| Distribution | 5 | Is there an obvious place to find users? |
| Competitive wedge / timing | 5 | Is there a timely reason and a credible wedge against existing options? |

Default threshold for creating a dedicated repo: **18/25**.

## Repo creation rule

Do not create a project repo just because a day passed. Create a repo when the idea clears the threshold or when Marian explicitly asks to build it.

## Privacy

This is a public build-in-public repository. Do not commit tokens, private infrastructure details, home paths, screenshots with personal data, or private conversations.
