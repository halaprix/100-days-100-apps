# Day 044 — ChunkRail

Date: 2026-08-02
Status: idea-only
Repo: —

## One-line pitch

A WebRTC data-channel file-transfer stress harness that finds unsafe chunk sizes, backpressure thresholds, and receiver-write fallbacks before browser-to-browser transfers blow up memory or stall.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit — r/webdev | https://www.reddit.com/r/webdev/comments/1vd65re/i_built_mayopizza_a_filetransfer_site_that_sends/ | Fresh builder post says RTCDataChannel is not a stream, large file transfers require manual chunking/backpressure, and receiver storage needs a File System Access fallback chain. |
| MDN | https://developer.mozilla.org/en-US/docs/Web/API/RTCDataChannel/bufferedAmount | `bufferedAmount` grows as `send()` queues data; MDN explicitly points to using the low-buffer event to know when there is room to queue more. |
| MDN | https://developer.mozilla.org/en-US/docs/Web/API/RTCDataChannel/bufferedAmountLowThreshold | `bufferedAmountLowThreshold` and `bufferedamountlow` are the browser primitives for cooperative flow control, but developers still have to wire the policy correctly. |
| Stack Overflow | https://stackoverflow.com/questions/32240191/webrtc-datachannel-buffered-full | Public Q&A evidence that naive WebRTC data-channel file sends can hit buffer limits and fail around large queued sends. |
| GitHub / FilePizza | https://github.com/kern/filepizza | Peer-to-peer browser file transfer is a proven category, but production apps expose transfer UX, not a standalone developer harness for chunk/backpressure tuning. |
| PairDrop | https://pairdrop.net/ | Another widely used browser P2P transfer app; useful substitute for end users, not for developers trying to validate their own transfer loop. |

## Source access caveats

- Reddit public JSON was blocked with `HTTP 403 theme-beta`; r/webdev and r/SideProject posts came from the bundled Reddit RSS fallback.
- Fetching individual Reddit comment threads returned `HTTP 403`, so the brief uses public post titles/snippets plus external documentation and competitor pages.
- Several subreddit JSON/RSS attempts hit `HTTP 429`; I stopped instead of looping.
- X `whoami` worked, but X search returned `401 Unauthorized`; X was not used as evidence.
- Web search/extraction was used for MDN, Stack Overflow, FilePizza, PairDrop, and AI-music competitor validation.

## Shortlist wedge gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| ChunkRail | Web developers building browser-to-browser large-file transfer → MDN docs, Stack Overflow answers, FilePizza/PairDrop source, manual large-file tests → docs explain primitives but do not give a repeatable browser stress packet for chunk size, high-water marks, memory, and receiver fallback behavior → local harness that sweeps transfer policies and exports a failure/report packet → WebRTC search content, r/webdev build posts, GitHub examples, targeted replies to `RTCDataChannel bufferedAmount` questions → recent builder evidence shows the failure mode still surprises app makers. | Winner, but held as idea-only; score 17/25 and distribution is only 3/5. |
| AIDistroPacket | Independent AI-assisted musicians → OriginTape, distributor forms, blog checklists, spreadsheets of rights/disclosure proof → generic checklists and passports may miss distributor-specific disclosure wording and split/artwork proof → distributor-specific release packet diff for Suno/Udio-style workflows → r/musicmarketing, AI music communities, SEO around distributor rejection/disclosure → 2026 AI music disclosure rules are moving quickly. | Held/rejected today: OriginTape is already a direct recent competitor for the passport job; needs evidence of a sharper distributor-specific gap. |
| LaunchRoute | Solo iOS makers stuck at friends-and-family downloads → App Store Optimization tools, launch checklists, paid ads, Reddit advice, founder communities → advice is generic and does not identify the first real stranger channel for a specific app → small launch-channel experiment planner tied to app category and proof assets → SideProject launch autopsy posts and app-maker communities → fresh post shows the pain, but category is crowded marketing/growth tooling. | Rejected before scoring: distribution tooling is crowded and the status-quo pain is vague without a concrete app category. |
| TinySub Lite | Tiny Shopify stores selling coffee/consumables → Shopify Subscriptions, Recharge, Seal, Appstle, custom theme/app work → premium subscription apps can feel overpriced for small stores, while native Shopify subscriptions can be barebones → opinionated low-price subscription setup for one-SKU repeat purchases → Shopify App Store search and coffee/CPG operators → fresh SideProject post cites the price pain. | Rejected before scoring: Shopify subscription apps are crowded and platform-review friction makes a 1–3 day MVP less convincing. |
| PasswordCharProbe | Web developers whose password rules reject password-manager generated strings → password-manager generators, manual QA, auth library defaults → signup forms often document one policy but enforce another edge-case character set → tiny CI/browser probe that fuzzes generated passwords against signup/login flows → webdev/auth-library communities and QA content → fresh r/webdev post surfaced invalid generated password frustration. | Held as a future niche QA idea; today's evidence is a single anecdote and the workaround is tolerable for many teams. |

## Problem

Developers building browser-to-browser file transfer often discover too late that `RTCDataChannel` behaves like a message queue, not a stream. Sending a large file safely means choosing chunk sizes, high/low watermarks, pause/resume behavior, integrity checks, receiver-side disk writes, and browser fallbacks. A naive loop can queue too much data, spike memory, hit browser buffer limits, or make Safari/older-browser fallback behavior bad enough to break the demo.

The status quo is not catastrophic for every team, but it is expensive when a product depends on large transfers: developers copy snippets, test with a few local files, then debug browser-specific stalls manually. That can waste hours per implementation and cause public embarrassment if a supposedly private direct-transfer app fails on a real user file.

## Target user

- Web developers building browser-to-browser file-transfer products or features with WebRTC data channels.
- Indie builders shipping privacy-preserving transfer tools, support-file upload flows, or local-network sharing apps.
- Maintainers of self-hosted transfer tools who need a reproducible browser stress report before changing chunking logic.

## MVP scope

- Static local harness that opens two browser peers in one page or two tabs using a local signaling shim.
- Synthetic payload generator plus optional real-file mode for 100 MB / 1 GB style tests without uploading bytes to a server.
- Configurable chunk size, high-water mark, low-water threshold, ACK cadence, integrity hash, and receiver sink strategy.
- Browser report: peak `bufferedAmount`, send pauses, throughput, memory hints where available, receiver fallback used, and failure point.
- Markdown/JSON export packet with recommended safer defaults and reproducible environment notes.
- Non-goals for v0: TURN diagnostics, encrypted file-sharing product UX, cloud storage, or replacing PairDrop/FilePizza.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | WebRTC samples, MDN examples, blog posts, Stack Overflow answers | Explain the primitives and common fixes, but do not provide a repeatable app-specific stress harness and exportable report. |
| Direct competitor | FilePizza | Strong open-source peer-to-peer transfer product; it proves the category but is not positioned as a developer diagnostic harness for arbitrary transfer loops. |
| Direct competitor | PairDrop / Snapdrop-style apps | Excellent end-user transfer tools; not useful for validating a developer's own chunking/backpressure implementation. |
| Indirect substitute | Manual large-file testing in Chrome/Safari/Firefox, custom scripts, copying code from existing transfer apps | Flexible but inconsistent; failures are often discovered by trying a few files and watching memory/errors manually. |
| Status quo | Ship a hand-rolled send loop, tune thresholds by feel, and wait for bug reports when large files or unsupported receiver sinks fail | Can waste hours and create public demo/support embarrassment, but the pain is limited to teams building WebRTC transfer features. |

## Wedge

Specific user → existing substitute → why substitute fails → narrow wedge → distribution path → reason now

Web developers building browser-to-browser large-file transfer → MDN docs, Stack Overflow answers, FilePizza/PairDrop source, manual large-file tests → sources teach APIs or ship full transfer products, but they do not give a repeatable browser stress packet for chunk size, high-water marks, memory, receiver-write fallback, and failure reproduction → local harness that sweeps transfer policies and exports a markdown/JSON report → WebRTC search content, r/webdev build posts, GitHub examples, and targeted replies to `RTCDataChannel bufferedAmount` questions → a fresh builder post shows the same low-level failure modes still surprise people shipping P2P file-transfer apps.

ChunkRail can work as a narrow dev tool if it stays diagnostic: it should not become another file-transfer app. The wedge is the reproducible transfer-policy report a maintainer can attach to an issue or use before changing defaults.

## Kill condition

Reject or narrow if one of these is proven:

- Existing WebRTC libraries already ship a maintained, browser-matrix transfer stress harness with report export.
- Builders say copying PairDrop/FilePizza internals is faster than running a separate harness.
- The harness cannot measure enough useful browser behavior without non-standard APIs or heavy automation.
- Evidence remains one-off and no repeated questions appear around `bufferedAmount`, chunk size, receiver storage, or Safari/File System Access fallbacks.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 3/5 | Pain is real and can waste hours, but it affects a narrow slice of web developers building large WebRTC transfers. |
| Feasibility | 4/5 | A local static harness plus report export is buildable in 1–3 days without paid APIs. |
| Demo potential | 4/5 | A GIF can show unsafe settings spiking the queue, then safer settings producing a clean report. |
| Distribution | 3/5 | Specific communities and search terms exist, but there is no built-in channel; distribution depends on technical content and targeted replies. |
| Competitive wedge / timing | 3/5 | Strong docs and open-source apps exist, but the diagnostic/report niche is still distinct. |
| Total | 17/25 | Save as idea-only; below repo threshold and distribution gate fails. |

## Decision

Save as `idea-only`. ChunkRail is a credible narrow dev-tool bet, but it does not clear the 18/25 repo threshold and Distribution is only 3/5. No dedicated repo was created.

Weakest dimensions: Usefulness, Distribution, and Competitive wedge / timing at 3/5.

## Next build step

Run a one-day spike: build a single-page local WebRTC loopback that sends a synthetic 500 MB payload with two chunk/high-water configurations, records `bufferedAmount` over time, and exports a markdown report. If that demo is compelling and search/reddit evidence repeats, reconsider repo creation.
