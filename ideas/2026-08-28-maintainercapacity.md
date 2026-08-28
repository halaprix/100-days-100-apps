# Day 064 — MaintainerCapacity

Date: 2026-08-28
Status: idea-only

## One-line pitch

A local-first portfolio-maintenance brief that turns a small team’s repo and service inventory into an owner-facing capacity report: what must be maintained, what is changing, and what new work it displaces.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Public community report (Reddit RSS fallback, page fetched) | [r/webdev: “How many properties are you responsible for?”](https://www.reddit.com/r/webdev/comments/1w090bc/how_many_properties_are_you_responsible_for/) | A lone web developer describes a growing portfolio of Firebase, Apps Script, and GCP work; dependencies and API deprecations create maintenance work that stakeholders do not see. The author later says they maintain about a dozen apps; replies describe substantially larger portfolios.[1] |
| Vendor documentation | [GitHub Dependabot version updates](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-version-updates) | Dependabot automates package-update pull requests, but its unit of work is a repository manifest rather than a cross-portfolio capacity explanation.[2] |
| Vendor documentation | [Renovate Dependency Dashboard](https://docs.renovatebot.com/key-concepts/dashboard/) | Renovate aggregates pending dependency updates per repository; it is an important substitute, not the proposed stakeholder-facing inventory.[3] |
| Vendor documentation | [Backstage Software Catalog](https://backstage.io/docs/features/software-catalog/) | Backstage tracks ownership and metadata across software ecosystems, but is designed as a centralized catalog and is much broader than a small-team maintenance brief.[4] |
| Vendor documentation | [Google Cloud feature deprecations](https://docs.cloud.google.com/service-usage/docs/deprecations) | Google publishes dated feature deprecations, confirming that service-lifecycle changes are a concrete maintenance input rather than merely hypothetical risk.[5] |

## Problem

A one-person or very small web team can accumulate many small Firebase, Apps Script, GCP, and site projects. Dependency bots reduce individual update chores, but they do not answer the planning question: **what maintenance work exists across the portfolio, who owns it, and what feature work must slip if it is ignored?**

The status quo is a mix of Dependabot/Renovate queues, repository tabs, spreadsheets, and the maintainer’s memory. That becomes material once updates, deprecations, and support requests are competing for the same person’s time; the source report explicitly describes a growing portfolio and stakeholder-expectation gap.[1]

## Target user

The sole dedicated web developer, or a two-to-five-person internal web team, maintaining a growing set of stakeholder-owned Firebase, Google Apps Script, GCP, and static-web projects.

## MVP scope

A local CLI with a checked-in `maintainercapacity.yml` inventory. It would:

1. import repository names, owner/stakeholder, platform, and last-review date;
2. ingest dependency-bot exports or a small CSV of pending updates;
3. record dated platform/API notices as explicit review items; and
4. render a one-page Markdown/HTML “maintenance capacity brief” grouped by owner, urgency, and estimated review time.

It does not log into cloud tenants, make updates, or claim to discover every deprecation automatically.

## Shortlist and wedge-first gate (before scoring)

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| MaintainerCapacity | Small internal web team with a growing Firebase/GAS/GCP portfolio → Dependabot, Renovate, Backstage, and spreadsheets → they show dependency or catalog state, not the maintenance load competing with stakeholder requests → local, owner-labelled capacity brief → Firebase, Apps Script, and small-team web-maintenance discussions plus a reusable inventory template → a fresh r/webdev thread reports this exact portfolio/expectation gap.[1] | **Narrowed and scored.** The pain can block planned work; distribution is real but not yet repeatable enough for a repo. |
| AgentCue | Coding-agent users → generic sounds/terminal notifications → a generic alert does not explain whether a human decision is required → event classification for coding-agent attention → agent-tool users → a fresh post already ships Beckon, a CLI that distinguishes done, permission, and failure states. | **Rejected before scoring.** The direct solution is already being built and no sharper user/channel evidence was found. |
| AgencyFit Packet | Seed-stage B2B SaaS teams → agency directories, referrals, and sales calls → generic lists do not state stage/budget fit → comparable agency-fit packet → seed-founder communities → the available source only asks for recommendations, while a reliable product needs unavailable, constantly changing agency qualification data. | **Rejected before scoring.** Data quality and distribution would be the product; neither is established. |
| Pricing-page interrogation | First-time SaaS founders → copywriters, pricing consultants, and generic AI chat → founders struggle to articulate the value metric → guided evidence intake → generic founder communities → one fresh post reports the problem, but the category has no verified narrow workflow or first-user channel. | **Rejected before scoring.** The status-quo pain is credible but the wedge and distribution are vague. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Backstage Software Catalog | Tracks ownership and metadata across an ecosystem. It is the closest catalog substitute, but requires a broader developer-portal adoption path than the proposed local report.[4] |
| Direct competitor | Renovate Dependency Dashboard | Gives a repository-level overview of pending updates and approval flow; it solves update visibility, not cross-project capacity communication.[3] |
| Indirect substitute | GitHub Dependabot | Automates dependency update pull requests from repository manifests.[2] |
| Indirect substitute | Spreadsheet plus calendar reminder | Common low-cost way to list projects and review dates, but it decays unless the maintainer repeatedly curates it. |
| Status quo | The maintainer manually explains portfolio load during planning | This hides lifecycle work until a dependency, API, or stakeholder request becomes urgent.[1] |

## Wedge

This is not another dependency updater or internal developer portal. The narrow wedge is an **offline, stakeholder-readable maintenance capacity brief** for small teams with platform-heavy portfolios. A maintainer labels a modest inventory once; the tool renders the explanation needed for the next planning conversation, without requiring a tenant connection, a data warehouse, or a Backstage rollout.

The first useful channel is not a broad launch: publish the inventory template and before/after report in Firebase, Google Apps Script, and small-team web-maintenance discussions where maintainers already ask how to keep many properties current. That is a specific community path, but not yet a repeatable acquisition loop.

## Kill condition

Reject the idea if five target maintainers say a Dependabot/Renovate dashboard plus a spreadsheet already answers the planning conversation in under ten minutes per week, or if they will not keep the owner/review metadata current. In either case the proposed report merely duplicates tolerable work.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | The work competes directly with new delivery and can create unplanned incidents or missed deprecations; current evidence is a single fresh thread rather than a broad sample.[1] |
| Feasibility | 4/5 | A local inventory plus CSV/manual lifecycle inputs and a Markdown/HTML renderer is a 1–3 day MVP. Automatic cloud discovery is intentionally out of scope. |
| Demo potential | 4/5 | A before/after portfolio report can make hidden maintenance load visible in a short screen recording. |
| Distribution | 3/5 | Firebase, Apps Script, and small-team web-maintenance communities are identifiable, but there is no demonstrated repeatable acquisition loop yet. |
| Competitive wedge / timing | 3/5 | The local capacity-report framing is narrower than Dependabot, Renovate, or Backstage; it still needs interviews to prove that framing changes planning decisions.[2][3][4] |
| Total | 18/25 | Clears the numeric threshold, but fails the required distribution gate. |

## Decision

**Idea-only. No dedicated repository created.** The 18/25 total and 3/5 wedge meet two gates, but distribution is only 3/5; the first-user path is a specific community, not a repeatable channel. The idea should earn a repo only after direct validation shows that the brief changes capacity or prioritization conversations.

## Next build step

Run five short interviews with maintainers of at least five internal web properties. Ask them to reconstruct their last maintenance-versus-feature tradeoff using a blank owner/review inventory. Build the local renderer only if at least three say the resulting one-page brief would change a planning or staffing conversation.

## Source access caveats

Reddit public JSON was blocked; the read-only tool used RSS fallback for r/webdev and the linked page was then fetched directly. RSS returned no engagement metrics, so none are claimed. Other configured subreddits hit RSS 429 and web-search fallback returned no usable fresh results. X search was attempted through `xurl` and returned HTTP 401; no X evidence is claimed.

## Sources

[1] https://www.reddit.com/r/webdev/comments/1w090bc/how_many_properties_are_you_responsible_for
[2] https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-version-updates
[3] https://docs.renovatebot.com/key-concepts/dashboard
[4] https://backstage.io/docs/features/software-catalog
[5] https://docs.cloud.google.com/service-usage/docs/deprecations
