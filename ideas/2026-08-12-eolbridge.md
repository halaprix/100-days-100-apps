# Day 052 — EolBridge

Date: 2026-08-12
Status: repo-created
Repo: [`projects/eolbridge`](../projects/eolbridge)

## One-line pitch

EolBridge turns Drupal 10 version, module, Composer, and platform-readiness facts into an executive upgrade/budget packet before the December 2026 support cliff.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/sysadmin | https://www.reddit.com/r/sysadmin/comments/1vm4kqc/how_are_you_handling_drupal_10_eol_in_december/ | Fresh sysadmin post says Drupal 10 reaches end of life on December 9, 2026; teams range from staged upgrades to not knowing their current version, and some cannot get budget because the site “still works fine.” |
| Drupal.org core schedule | https://www.drupal.org/about/core/policies/core-release-cycles/schedule | Web search surfaced the official Drupal core release schedule stating Drupal 10 reaches end of life on December 9, 2026, with no new Drupal 10 releases after that date. |
| Drupal.org Upgrade Status | https://www.drupal.org/project/upgrade_status | Existing module validates demand for major-version readiness checks: system requirements, next-major compatibility, Update Status integration, and compatibility of contributed/custom components. |
| Drupal.org Rector | https://www.drupal.org/project/rector | Existing automation can reduce manual code-upgrade work for Drupal 9, 10, and 11, but it is developer-oriented rather than a management/budget evidence packet. |
| Microsoft / Entra TAP search result | https://learn.microsoft.com/en-us/entra/identity/authentication/howto-authentication-temporary-access-pass | Nearby sysadmin signal showed onboarding/PIN friction around Temporary Access Pass and Windows Hello for Business, but this overlaps prior passkey/onboarding packet territory. |

## Problem

Drupal 10 EOL is a predictable deadline, but many small organizations will still delay because the site keeps working and the upgrade looks like a vague dev-agency expense. The technical team may know the risk, but they need a compact, defensible packet that says: current Drupal/core/contrib state, blockers, owner-facing risk, rough effort bands, and what happens if the upgrade is deferred. Existing developer tools help scan code; they do not package the result for budget approval.

## Target user

Small-agency developers, nonprofit/SME sysadmins, and fractional IT owners responsible for one or more Drupal 10 sites where the upgrade decision needs approval from non-technical stakeholders.

## MVP scope

- Read a public-safe `composer.json`, `composer.lock`, and optional sanitized module/theme inventory export.
- Detect Drupal core major/minor, PHP/platform constraints, pinned packages, abandoned packages where Composer metadata exposes them, and obvious next-major blockers.
- Produce a markdown/HTML packet with: deadline banner, current-state summary, blocker table, owner questions, risk copy, and a staged upgrade plan.
- Include manual-entry fields for site owner, business criticality, traffic/revenue class, and agency estimate bands.
- Refuse secrets and redact environment-looking values; do not connect to production Drupal, databases, or admin panels in the MVP.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Drupal Upgrade Status | Strong developer-side readiness module for major upgrades; checks environment, system requirements, Update Status data, and project compatibility. It does not target budget-holder packets. |
| Direct competitor | Drupal Rector | Strong code-modernization automation for deprecated Drupal APIs. It helps developers fix code, but it is not an EOL decision memo or stakeholder approval artifact. |
| Direct competitor | Drupal agencies / upgrade audits | Agencies can produce the complete audit and estimate, but smaller orgs often delay because they need a lightweight pre-budget artifact before paid discovery. |
| Indirect substitute | Composer audit/outdated, drush status, spreadsheet | Flexible and cheap, but the burden is on the sysadmin/developer to translate package facts into risk, timeline, and approval language. |
| Status quo | Wait until the site breaks or a vulnerability forces action | The site “still works fine,” so budget approval slips; once EOL hits, new Drupal 10 fixes stop and every future vulnerability becomes harder to justify safely. |

## Wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| EolBridge | Small-agency Drupal developers and SME sysadmins → Upgrade Status, Rector, Composer checks, agency audits → developer tools find blockers but do not create a budget-ready EOL packet → sanitized Composer/module inventory to executive markdown/HTML decision packet → r/sysadmin/r/drupal search, agency blog content, direct replies to EOL planning threads → fresh Drupal 10 EOL deadline and budget-approval pain | Winner; timely, narrow, and distribution has search/reply paths. |
| WhfbPrep Pause | Entra admins staging laptops before users start → Intune policy, Temporary Access Pass docs, Windows Hello for Business settings → admins still hit forced PIN setup during pre-login prep → onboarding-mode checklist and policy diff packet → r/sysadmin and Microsoft Q&A search → fresh onboarding friction post | Held: useful but overlaps prior PasskeyPilot/Entra territory and risks becoming docs-only. |
| WireCert Trace | Windows 11 admins debugging 802.1X wired certificate failures → Microsoft 802.1X troubleshooting docs, NPS logs, cert MMC, vendor drivers → onboard NIC vs dock behavior is hard to isolate quickly → read-only packet comparing adapter, cert store, EAP profile, and event logs → r/sysadmin plus Windows 11 802.1X search → fresh weird onboard-NIC failure | Strong runner-up; likely future candidate, but needs more repeated-source validation. |
| DfsShortcut Probe | RDS admins seeing DFS Namespace shortcuts render blank → DFS troubleshooting docs, event logs, registry attempts → symptom crosses shell, DFS referrals, DNS, and RDS profile state → packetized DFSN shortcut diagnostics for RDS hosts → r/sysadmin/RDS search → fresh “spent so much time” post | Held: narrow pain, but direct evidence is one thread and demo is less crisp. |
| FounderSource Vault | Non-technical SaaS founders relying on outsourced dev partners → software/SaaS escrow, GitHub access, contract clauses → classic escrow is heavy and late; founders lose practical custody of code/build/deploy assets → lightweight handoff/access checklist and repo continuity packet → r/SaaS founder posts and agency-partner searches → fresh founder lost SaaS twice after partner handoffs | Rejected for today: real pain, but trust/legal surface is messy and distribution can drift into generic founder advice. |

## Wedge

EolBridge can win by staying below full agency discovery and above raw developer scanner output. The narrow promise is: “drop in safe dependency/module facts, get a packet a budget-holder can approve or reject.” A 1–3 day MVP can be entirely local and fixture-driven while still producing a useful artifact for agencies and internal IT teams.

## Kill condition

Reject or narrow if Upgrade Status, Drupal.org tooling, or common agency audit templates already produce a management-ready EOL packet with effort/risk language, or if first users say a Composer/Upgrade Status export already takes less than 15 minutes to convert into budget approval materials. Also reject if users mostly want automated code fixes; that is Rector’s lane.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | EOL creates security and budget risk; the pain is approval delay, not just developer toil. |
| Feasibility | 4/5 | A local parser plus markdown/HTML packet generator from Composer and manual inventory inputs is buildable in 1–3 days. |
| Demo potential | 4/5 | Clear demo: sample `composer.lock` in, blocker/risk packet out with deadline and upgrade stages. |
| Distribution | 4/5 | Specific channels exist: r/sysadmin and r/drupal EOL threads, Drupal agency blog/search content, GitHub examples, and direct replies to upgrade-planning discussions. |
| Competitive wedge / timing | 4/5 | Timing is strong because Drupal 10 has a dated EOL cliff; competitors solve developer readiness/code fixes, not budget-ready packets. |
| Total | 20/25 | Clears repo threshold and both dimension gates. |

## Decision

Create repo. EolBridge scored 20/25 with distribution 4/5 and competitive wedge/timing 4/5, so it clears the creation gates. Scaffold/spec snapshot was added under `projects/eolbridge`; no dedicated GitHub remote was created during this local-first run.

## Next build step

Implement `eolbridge packet --composer-lock fixtures/drupal10/composer.lock --site-profile fixtures/drupal10/site.yml --out packet.md` to generate a deterministic sample EOL decision packet without reading production systems.

## Source access caveats

Reddit public JSON was blocked; r/sysadmin collection used `reddit-rss-fallback`. r/selfhosted, r/webdev, and r/SideProject probes hit `HTTP 429`, so no score/comment counts were used. X/Twitter `whoami` worked, but X search returned `401 Unauthorized`; no X data was used and no social writes were attempted. Drupal.org pages returned a client-challenge through `web_extract`, so the official schedule/tooling evidence is based on web-search snippets pointing to the original Drupal.org URLs, not extracted page bodies.
