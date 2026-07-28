# ExitTrace

A local crawler and report generator for sensitive support websites that need discoverable SEO content without leaving dangerous page titles, URLs, referrers, history entries, or broken quick-exit flows on a survivor's device.

## Problem

Sensitive support pages have conflicting requirements. Accessibility and SEO guidance push teams toward descriptive titles, headings, and URLs. Survivor-safety guidance warns that browser history, tabs, autocomplete, sync, cookies, and sudden history clearing can expose someone who is being monitored.

Quick-exit buttons are useful, but official guidance is explicit: quick exit does not erase browser history. Small charities, legal-aid teams, and consultants need a repeatable way to inspect what their pages leave behind before publishing.

ExitTrace is the narrow tool for that handoff: crawl a site or static build, classify browser-visible trace risk, check quick-exit/safety-content basics, and export a page-by-page Markdown/CSV report.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit RSS fallback — r/webdev | https://www.reddit.com/r/webdev/comments/1uxu9yn/looking_for_a_solution_to_mask_page_titles_for/ | SEO consultant asks how to keep domestic-abuse support pages discoverable while preventing descriptive titles from showing in browser UI/history. |
| GOV.UK Exit a page quickly pattern | https://design-system.service.gov.uk/patterns/exit-a-page-quickly/ | Quick-exit guidance warns that internet browsing history will not be erased and should be explained to users. |
| GOV.UK Exit this page component | https://design-system.service.gov.uk/components/exit-this-page/ | Component is intended for pages that could put someone at risk of abuse or retaliation. |
| Safety Net Project / NNEDV | https://techsafety.org/seekinghelponline | Online help guidance says visited websites may still appear in browser history. |
| Safety Net Project / NNEDV | https://www.techsafety.org/internetbrowserprivacytips | Browser privacy guidance explains history, cookies, private browsing, sync, and safety tradeoffs. |
| W3C WCAG Page Titled | https://www.w3.org/WAI/WCAG22/Understanding/page-titled.html | WCAG requires meaningful page titles, which creates a tension for safety-sensitive content. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | GOV.UK quick-exit component and pattern | Strong implementation guidance, but not an auditor for arbitrary sites, titles, slugs, referrers, and report handoff. |
| Direct competitor | SEO/accessibility crawlers such as Lighthouse, Screaming Frog, Sitebulb, and axe | They catch SEO/accessibility issues, but do not classify survivor-safety trace risk. |
| Direct competitor | Domestic-abuse site quick-exit widgets and agency checklists | Useful components and advice, but not repeatable browser-trace evidence across every page. |
| Indirect substitute | Manual testing in Chrome, Safari, Firefox, private windows, and normal sessions | Possible for experts, slow for small teams, and easy to miss synced history/autocomplete/referrer issues. |
| Status quo | Publish descriptive pages with a quick-exit button and a safety note | Better than nothing, but page titles/URLs/history entries can still expose at-risk users. |

## Wedge

ExitTrace is not a generic SEO, accessibility, or security scanner. It is a safety-design audit for traces that sensitive pages leave in browser UI and browser storage:

- page titles,
- sensitive URL slugs,
- heading/title/breadcrumb wording,
- outbound referrers,
- quick-exit implementation details,
- safety-content warnings,
- browser caveats linked to public guidance.

The first-user path is narrow: web developers, SEO consultants, civic-design teams, and nonprofit teams working on domestic-abuse, legal-aid, health, trafficking, stalking, whistleblowing, or crisis-support content.

## Target user

- SEO consultants and web developers working on sensitive support resources.
- Small nonprofit/civic-tech teams preparing a safety review before launch.
- Accessibility-minded product teams balancing descriptive page titles with user safety.

## MVP

- `exittrace audit <url-or-path> --sensitive-map sensitive.yml`.
- Sitemap/local-directory crawl for pre-launch static builds.
- Checks for risky titles, sensitive slugs, referrer leakage, quick-exit presence, `rel="noreferrer"`, and safety-content links.
- Markdown and CSV output with severity, page URL, evidence snippets, and safer wording suggestions.
- Synthetic fixture site for demos and tests.

## Non-goals

- No claim that a website can make monitored browsing completely safe.
- No legal, clinical, survivor-advocacy, or emergency-safety advice.
- No hosted crawler in v0.
- No collection of real survivor-service URLs in public examples unless explicitly provided by the site owner.
- No browser-history deletion automation.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
