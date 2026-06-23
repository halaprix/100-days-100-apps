# Scoring Rubric

A good idea is not just clever. It should be painful, buildable, demoable, distributable, and have a credible wedge against existing options.

| Score | Decision |
|---:|---|
| 22–25 | Strong build candidate |
| 18–21 | Create repo + spec, then reassess |
| 14–17 | Save as idea only |
| <14 | Reject unless there is a strategic reason |

Repo creation also requires the dimension gates below. A useful, feasible idea
with a weak wedge is still only `idea-only`.

| Gate | Minimum | Why |
|---|---:|---|
| Total score | 18/25 | Avoid low-signal daily streak repos. |
| Competitive wedge / timing | 3/5 | Forces a reason to win despite existing options. |
| Distribution | 4/5 | Forces a concrete first-user path, not a generic audience. |

## Anti-patterns

- Commodity physical gadgets, merch, or gift SKUs. This is **100 Days, 100 Apps**: physical products are rejected unless Marian explicitly asks for product/SKU research.
- Generic AI wrapper with no distribution.
- Generic AI wrapper in a crowded category, unless it has a narrow workflow
  wedge and a concrete first-user channel.
- Marketplace without supply or demand access.
- App requiring paid/private APIs before MVP proof.
- Products depending on spammy outreach.
- Distribution that is only "post on Product Hunt", "post on r/SaaS", or
  "share with indie hackers".
- Idea with strong existing products and no clear wedge.
- "Novel" idea where the real competitor is a spreadsheet/manual workflow that is already good enough.
- Ideas whose best path is Amazon/AliExpress/Alibaba sourcing instead of a software MVP.

Treat these crowded categories as **reject-by-default** unless the wedge is
specific and validated by source evidence: AI video/demo tools, generic security
scanner/autofix wrappers, analytics dashboards, LLM spend/observability,
job-application automation, social-listening/lead-mining tools, note/todo/focus
apps, and generic browser extensions.

## Required competitor gate

Before assigning the final score, check:

| Type | What to look for |
|---|---|
| Direct competitors | Same job, same user, same budget. |
| Indirect substitutes | Spreadsheet, Notion, Zapier, generic AI/chat, scripts, agencies, manual process. |
| Status quo | Why the user has not switched yet. |
| Wedge | Faster setup, narrower segment, better distribution, lower trust barrier, better demo, or timely platform shift. |

Use **Competitive wedge / timing** as the fifth scoring dimension. Score it low if incumbents already solve the painful job and there is no sharp wedge.

Before scoring, write one line for each shortlisted candidate:

```text
Specific user → existing substitute → why substitute fails → narrow wedge → distribution path → reason now
```

Reject or narrow the candidate if any field is vague.

## Distribution scoring

Score distribution harshly. A named community is not enough.

| Score | Meaning |
|---:|---|
| 1 | No clear audience. |
| 2 | Generic audience exists. |
| 3 | Specific community exists, but no repeatable access path. |
| 4 | Specific community plus clear content/search/reply strategy. |
| 5 | Built-in sharing/referral/channel advantage. |

## Status-quo pain test

The current workaround must be bad enough to matter. Prefer ideas where the
status quo wastes more than 30 minutes per week, causes lost money, creates
public embarrassment, blocks a launch/sale, or creates compliance/security risk.
If the workaround is already tolerable, reject even if the MVP is easy.

Hard kill: if the idea is a commodity physical product or accessory and the wedge is only "make a nicer version", reject it before scoring. Do not deliver it as the daily winner for this app repo.
