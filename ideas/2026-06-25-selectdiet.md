# Day 007 — SelectDiet

Date: 2026-06-25
Status: idea-only

## One-line pitch

A tiny decision app and recipe generator for Astro/static-site developers choosing a select/dropdown component: compare native, Radix, Ark UI, Base UI, React Aria, Headless UI, and SlimSelect by real island bundle cost, accessibility behavior, and copy-paste integration path.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/webdev | https://www.reddit.com/r/webdev/comments/1ueljxe/are_there_any_good_lightweight_headless_select/ | Fresh post from an Astro developer: a 20 KB page needs a restylable select, but Ark UI and Base UI reportedly add roughly 100 KB, making the user consider an ugly native select instead. |
| Reddit / r/webdev | https://www.reddit.com/r/webdev/comments/1uf2psq/migrate_wordpress_to_astro/ | Adjacent signal that developers are moving marketing/company sites from WordPress/page builders to Astro while using AI coding tools, increasing demand for low-JS component decisions. |
| Astro docs | https://docs.astro.build/en/concepts/islands/ | Astro's islands model hydrates interactive components separately; a single dropdown can dominate the JS budget on an otherwise static page. |
| Ark UI docs | https://ark-ui.com/docs/components/select | Ark UI's Select is a full-featured headless component across React/Solid/Vue/Svelte, confirming the direct competitor set is capable but broad. |
| Base UI docs | https://base-ui.com/react/components/select | Base UI's Select exposes extensive positioning, accessibility, grouping, and value APIs; strong substitute, but not a static-site size decision tool. |
| React Aria docs | https://react-spectrum.adobe.com/react-aria/Select.html | React Aria Select supports accessible collections, async, autocomplete, forms, and validation; another powerful general-purpose substitute. |
| npm registry metadata | https://www.npmjs.com/package/@ark-ui/react, https://www.npmjs.com/package/@base-ui-components/react, https://www.npmjs.com/package/react-aria-components, https://www.npmjs.com/package/@radix-ui/react-select | Public `npm view` checks showed large general packages by unpacked size (`@ark-ui/react` 3.16 MB, `@base-ui-components/react` 4.33 MB, `react-aria-components` 6.22 MB) versus select-specific Radix at 344 KB. This is only a package-size proxy, not a built bundle measurement, but it supports the source user's concern. |
| GitHub / Ark UI issue | https://github.com/chakra-ui/ark/issues/2353 | Search found a public issue titled “Huge bundle size in production build with Next.js,” reinforcing that component-library tree-shaking and bundle surprises are a known developer concern. |

Research note: Reddit public JSON was blocked by `HTTP 403 theme-beta`; r/SaaS and r/webdev posts were collected through the reddit-readonly RSS fallback. r/selfhosted and r/sysadmin RSS calls returned `HTTP 429`, and thread/comment extraction for promising posts returned `HTTP 403`, so the run stopped retrying and used RSS post bodies plus public web/docs/npm evidence. X read auth worked (`whoami`), but X search returned `401 Unauthorized`, so X was not used as evidence.

## Problem

Static-site and Astro developers often choose a headless UI library by reputation, docs, or snippets, then discover late that one interactive component drags a mostly-static page over its JavaScript budget. The source post is narrow but concrete: the page is about 20 KB, the developer needs a restylable select, and tried Ark UI and Base UI before deciding that a native select might be preferable to adding roughly 100 KB.

The status quo is not catastrophic, but it is annoying and repeated: install a package, build, inspect bundle output, remove it, try another package, then still hand-roll accessibility or accept native styling limits. That can easily burn an afternoon per component decision and lead to slow marketing pages.

## Target user

Astro, Preact, Solid, and React developers building mostly-static marketing/docs/product pages where:

- the page has one or two hydrated islands,
- performance budget matters,
- native form controls are acceptable unless custom styling/search/grouping is required,
- the developer wants an accessible select/dropdown without pulling in a broad design-system runtime.

## MVP scope

- A static comparison table for common select options: native `<select>`, Radix Select, Ark UI Select, Base UI Select, React Aria Select, Headless UI Select, SlimSelect, and one minimal custom recipe.
- Reproducible benchmark fixtures for Astro + Preact/Solid/React islands, with generated JS/CSS size per option.
- A decision wizard: “single select / multi-select / searchable / grouped / SSR form / no-JS fallback / max KB budget.”
- Copy-paste recipes for the recommended option, including native-first fallback when custom UI is not worth it.
- A CLI command that runs the same benchmark locally against the user's current package manager and framework.

Non-goals for v0.1: becoming a full component library, replacing accessibility testing, supporting every UI primitive, or claiming package unpacked size equals browser bundle size.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | Bundlephobia / bundlejs / package-size tools | Good for package-level size checks, but they do not answer “what does this select add inside an Astro island with this adapter and this usage pattern?” |
| Direct competitor | Radix UI Select, Ark UI Select, Base UI Select, React Aria Select, Headless UI Select | These solve the component job directly. SelectDiet would not compete as a component; it helps developers choose among them and provides slim recipes. |
| Direct competitor | SlimSelect / ThekSelect / small standalone select libraries | Often lighter and framework-agnostic, but require separate a11y/API evaluation and are not presented in Astro/static-site decision terms. |
| Indirect substitute | Native `<select>` with CSS | Best answer for many simple forms. Wedge exists only when the user needs restyling, async/search/multi-select, consistent UX, or a proof that native is still the right choice. |
| Indirect substitute | Manual benchmark with Vite/Astro bundle analyzer | Accurate, but slow and fiddly when comparing several libraries. This is the main workflow SelectDiet compresses. |
| Status quo | Install, build, inspect, uninstall, repeat | Works for experienced devs, but burns time and causes avoidable bundle regressions on static pages. |

## Wedge

**Wedge-first line:** Astro/static-site developers choosing one accessible select island → native select, generic headless libraries, Bundlephobia, and manual bundle analyzers → existing substitutes are either components, package-level proxies, or ad hoc local experiments that do not answer the Astro-island tradeoff quickly → a tiny benchmark-backed decision app with native-first recipes and per-framework fixture output → r/webdev, Astro community/search queries like “lightweight headless select Astro” and “Radix vs Ark UI bundle size” → Astro/islands adoption makes every hydrated component's JS budget visible.

The wedge is deliberately small: do not build another select. Build the buying/choosing surface for people who are already about to install one.

## Kill condition

Reject or narrow if developers say Bundlephobia plus local bundle analyzer is already good enough, or if benchmark fixtures cannot produce stable, reproducible numbers across Astro adapters. Also reject expansion into a generic component-comparison marketplace unless repeated evidence appears for other primitives.

## Shortlist notes

| Candidate | Wedge-first gate result | Score | Decision |
|---|---|---:|---|
| SelectDiet | Astro/static-site developers choosing one select island → native select/headless libraries/Bundlephobia → substitutes do not combine bundle, a11y, and Astro usage recipes → benchmark-backed chooser and CLI → r/webdev + Astro/search content → islands architecture makes small JS regressions salient. | 17/25 | Winner, idea-only. Narrow and demoable, but source evidence is still a single strong thread plus adjacent docs/package signals. |
| TemplateDocx | Technical students writing Markdown reports → Pandoc/Word/CloudConvert → generic converters miss department templates, equation/code styles, and submission preflight → local-first DOCX exporter with template lint → university tech communities/search → fresh r/SaaS validation post asked whether Markdown-to-DOCX is real pain. | 16/25 | Held. Useful, but Pandoc is a strong substitute and distribution is weaker. |
| FirstSaleLens | Creator-store SaaS founders → Mixpanel/PostHog/GA/spreadsheets → generic analytics do not map “first sale during trial” activation → seven-event first-sale funnel template → r/SaaS, Shopify app founders, Indian creator commerce groups → fresh post asks how to instrument first-sale-driven activation. | 15/25 | Rejected/held. Crowded analytics category; narrow workflow not yet strong enough. |
| AstroMigrate | WordPress developers moving company sites to Astro with AI tools → manual rebuild/export plugins/agencies → content, redirects, and page-builder assets are messy → CLI inventory and migration planner → WP/Astro search demand → AI coding makes static migration more tempting. | 15/25 | Held. Migration tools and agencies are crowded; evidence is directional, not sharp. |
| RouteSeeder | Fitness app builders needing realistic seed routes → OpenStreetMap/Strava/manual GPX collection → licensing and curation are painful → curated public-route seed dataset builder → side-project fitness builders → fresh r/SaaS post asks for famous route data. | 13/25 | Rejected. Data rights and distribution are weak; risks becoming a one-off dataset chore. |

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 3/5 | The pain can burn hours and create performance regressions, but it is a developer convenience/workflow pain rather than lost money or compliance risk. |
| Feasibility | 4/5 | A static app plus benchmark fixtures is buildable quickly, but reproducible cross-framework bundle measurements need care. |
| Demo potential | 3/5 | A before/after table and generated recipe are clear to developers, but less visually exciting than an end-user app. |
| Distribution | 4/5 | Specific audience and search path exist: Astro developers, r/webdev, GitHub issues on bundle size, and SEO around “lightweight headless select.” |
| Competitive wedge / timing | 3/5 | Component libraries and bundle tools are strong, but Astro/islands-specific selection guidance is narrow enough to test. |
| Total | 17/25 | Save as idea-only. It misses the 18/25 repo threshold despite passing the distribution gate. |

## Decision

Save SelectDiet as `idea-only`; do not create a dedicated repo today. The idea is narrow, software-only, and practical, but the evidence base is still thin: one strong Reddit post plus public package/docs signals. It needs one more validation pass across Astro/Preact/Solid developers before becoming a repo.

## Next build step

Run a 90-minute spike outside the daily index: create three Astro fixture pages using native select, Radix Select, and Ark/Base UI Select; measure production JS output; then publish the numbers as a short comparison post. If the numbers are stable and developers respond, create the repo.
