# Day 035 — ProxyEnv Doctor

Date: 2026-07-24
Status: repo-created

## One-line pitch

CLI preflight that rehearses `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` behavior across common developer tools before self-hosted CI jobs fail behind a proxy.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/webdev | https://www.reddit.com/r/webdev/comments/1v4px3u/why_do_we_use_env_vars_like_http_proxy_for_proxy/ | Fresh developer reported a self-hosted GitLab CI pipeline failing because proxy env vars were not set and asked why app-layer proxy variables are still required. |
| GitLab blog | https://about.gitlab.com/blog/we-need-to-talk-no-proxy/ | GitLab documented that subtle proxy-variable implementation differences caused a customer weekend outage and that no standard exists for `NO_PROXY`. |
| GitLab Runner docs | https://docs.gitlab.com/runner/configuration/proxy/ | Runner behind proxy requires variables at service, runner, container, and Docker-in-Docker layers; docs explicitly set upper and lower case variants because tools differ. |
| Docker CLI docs | https://docs.docker.com/engine/cli/proxy/ | Docker notes there is no standard for proxy env var handling and that proxy settings may leak into container configuration. |
| Docker daemon docs | https://docs.docker.com/engine/daemon/proxy/ | Docker daemon proxy config has separate precedence and `NO_PROXY` matching behavior, creating another layer where runner setups drift. |
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1v4umf1/i_somehow_broke_my_ssl_in_caddy_and_im_at_my_wits/ | Separate fresh reverse-proxy thread showed the same pattern: Docker + Windows + proxy/cert layers become hard to debug when docs are split. |

## Problem

Self-hosted CI behind a proxy fails in boring but expensive ways. A runner host can have one proxy setting, Docker another, the build container another, and each tool can interpret uppercase/lowercase proxy variables or `NO_PROXY` entries differently.

The result is a troubleshooting loop where one command succeeds, another command fails, and the operator keeps adding proxy variables to more places without knowing which layer actually broke. That wastes deploy time and can also leak proxy credentials into container metadata or logs.

## Target user

Developers and platform engineers running self-hosted GitLab Runner, Docker executor, Docker-in-Docker, or similar CI jobs behind a corporate/lab proxy.

## MVP scope

- `proxyenv-doctor scan` prints a redacted Markdown/JSON packet of proxy-related environment variables and likely conflicts.
- Fixture mode for demo environments such as `gitlab-dind`, `docker-cli`, and `npm-script` without real proxy credentials.
- Static compatibility matrix for curl, wget, git, npm, Docker CLI, Docker daemon hints, GitLab Runner, and Docker-in-Docker.
- Warnings for casing conflicts, missing `NO_PROXY`, unsupported wildcard/port assumptions, Docker-in-Docker `docker:2375` / `docker:2376` omissions, and tool-level config overrides.
- `proxyenv-doctor gitlab-snippet` emits copy/pasteable runner and `.gitlab-ci.yml` snippets for manual review.

## Shortlist and wedge-first gate

| Candidate | Wedge-first line | Gate result |
|---|---|---|
| ProxyEnv Doctor | Self-hosted CI developers/platform engineers → GitLab/Docker docs, netshoot, curl/git/npm debug commands → static docs do not execute the current runner/container/tool matrix and one successful tool can hide another failure → redacted executable proxy-env compatibility packet with GitLab/Docker snippets → r/webdev/r/devops/r/sysadmin plus search content around `NO_PROXY` and GitLab Runner proxy failures → fresh Reddit failure plus 2025/2026 docs still emphasize no standard | Pass; scored as winner. |
| CaddyCert Map | Windows self-hosters running Caddy/Nginx Proxy Manager/DuckDNS → Caddy docs, NPM UI, Certbot tutorials, forum replies → docs are scattered across DNS, ports, Docker, and ACME certificate modes → local read-only cert-route explainer for Caddy/NPM configs → r/selfhosted replies to Caddy/DuckDNS/cert failures → multiple fresh reverse-proxy threads | Rejected as daily winner: useful but overlaps prior HeaderPass/reverse-proxy diagnostics, and direct docs/forums already cover much of it. |
| SwarmDNS Planner | Homelab Docker Swarm users with apex domains on GitHub Pages → Traefik labels, Cloudflare API scripts, manual DNS records → automation is confusing when the root domain belongs to GitHub Pages and service subdomains live elsewhere → dry-run DNS/label plan for Swarm deployments → r/selfhosted/Docker Swarm content → fresh request for automatic DNS records | Rejected: status-quo manual records are annoying but often tolerable; wedge is too close to Traefik/Cloudflare automation docs. |
| Backup Mail Normalizer | Self-hosters checking backup reports every morning → backup dashboards, email filters, Uptime Kuma, Healthchecks, vendor consoles → parsing legacy email reports is tedious → local parser fixture kit for backup status emails → r/selfhosted backup-tool discussions → fresh side-project request for pain points | Rejected: crowded dashboard/monitoring category and overlaps earlier backup ideas; distribution depends on broad self-hosted attention. |
| Workspace Range Handoff | Google Workspace admins moving a user between departments → Admin console, Vault, Takeout, GAM scripts, Drive ownership transfer → native UI does not make date-bounded email/Drive handoff obvious → read-only query-plan packet for date-range handoffs → r/sysadmin/Google Workspace admin searches → fresh admin request | Held: potentially painful, but MVP likely needs sensitive Google admin scopes too early; safer as a later research spike. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | GitLab Runner proxy docs | Authoritative but static. They explain config placement; they do not run a current runner/container/tool matrix or produce a failure packet. |
| Direct competitor | Docker daemon / Docker CLI proxy docs | Necessary docs, but behavior is split across daemon, CLI, Desktop, build args, and container envs. They do not cover git/npm/curl case precedence in one preflight. |
| Direct competitor | netshoot | Excellent Docker/Kubernetes network troubleshooting container, but it is a general toolbox. It does not specialize in proxy-env semantics or `NO_PROXY` compatibility packets. |
| Indirect substitute | curl, wget, git config, npm config, ad hoc CI debug jobs | Free and flexible, but every operator has to know which probes to run and how to interpret tool-specific differences. |
| Status quo | Retry pipelines, add both upper/lower env vars everywhere, inspect runner logs, or bypass the proxy | Works eventually, but wastes time, can leak credentials into container configuration, and often leaves hidden drift for the next job. |

## Wedge

ProxyEnv Doctor wins only if it stays narrower than broad network debuggers and broader than a single docs page. The wedge is the executable matrix packet: run it where the CI job runs, get a redacted table of what each common tool is likely to do, and copy a reviewed GitLab/Docker snippet rather than guessing.

That wedge is feasible in 1–3 days because the first version can be static-rule heavy, fixture-driven, and read-only. It does not need access to a real corporate proxy to demo value.

## Kill condition

Reject or narrow if existing GitLab/Docker docs plus a short netshoot/curl recipe solve the painful job in under 10 minutes for most users, or if users say the real blocker is corporate proxy policy/access rather than diagnosing env-var drift.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | Proxy drift can block CI/deploys and waste >30 minutes; credential leakage risk raises the pain. |
| Feasibility | 5/5 | Standard-library CLI, static rules, fixture mode, and Markdown/JSON output are straightforward. |
| Demo potential | 4/5 | Fixture scan → redacted matrix → warnings → generated snippets is screenshot/GIF-friendly. |
| Distribution | 4/5 | Specific channels exist: r/webdev, r/devops, r/sysadmin, GitLab Runner/Docker proxy search queries, and reply/content strategy around `NO_PROXY` failures. |
| Competitive wedge / timing | 3/5 | Docs and netshoot are strong substitutes, but the narrow executable compatibility-packet wedge is not covered well. |
| Total | 20/25 | Clears repo threshold and dimension gates. |

## Decision

Create the repo. ProxyEnv Doctor clears 18/25 with Distribution 4/5 and Competitive wedge/timing 3/5. Status is `repo-created` because the scaffold was pushed and tagged.

Repo: https://github.com/halaprix/proxyenv-doctor

## Next build step

Implement `proxyenv-doctor scan --fixture gitlab-dind` with a static tool matrix, credential redaction, Markdown output, JSON output, and tests for casing conflict / missing `NO_PROXY` warnings.

## Research access note

Reddit public JSON was blocked for several subreddits; usable Reddit evidence came through the `reddit-rss-fallback` layer. Some subreddit RSS fallbacks returned HTTP 429, so I used the available RSS snippets plus original GitLab/Docker documentation for validation. X auth probing succeeded with `whoami`, but X search returned 401 Unauthorized, so X was not used as evidence.
