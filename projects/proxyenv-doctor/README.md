# ProxyEnv Doctor

CLI preflight that rehearses `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` behavior across common developer tools before self-hosted CI jobs fail behind a proxy.

## Problem

Self-hosted GitLab Runner, Docker, npm, git, curl, and language clients do not treat proxy environment variables the same way. A pipeline can work in one step and fail in another because a runner, container, or tool ignores a casing variant, bypass rule, port entry, or Docker-specific proxy config.

The repeated pain is not "what is a proxy?" It is the weekend-losing mismatch between the runner host, Docker daemon, Docker CLI, build container, and app-layer tools.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/webdev | https://www.reddit.com/r/webdev/comments/1v4px3u/why_do_we_use_env_vars_like_http_proxy_for_proxy/ | Fresh developer reported a self-hosted GitLab CI pipeline failing because proxy env vars were not set and asked why app-layer proxy variables are still required. |
| GitLab blog | https://about.gitlab.com/blog/we-need-to-talk-no-proxy/ | GitLab documented that subtle proxy-variable implementation differences caused a customer weekend outage and that no standard exists for `NO_PROXY`. |
| GitLab Runner docs | https://docs.gitlab.com/runner/configuration/proxy/ | Runner behind proxy requires variables at service, runner, container, and Docker-in-Docker layers; docs explicitly set upper and lower case variants because tools differ. |
| Docker CLI docs | https://docs.docker.com/engine/cli/proxy/ | Docker notes there is no standard for proxy env var handling and that proxy values can leak into container configuration. |
| Docker daemon docs | https://docs.docker.com/engine/daemon/proxy/ | Docker daemon proxy config has separate precedence and `NO_PROXY` matching behavior, creating another layer where runner setups drift. |

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct competitor | GitLab Runner proxy docs | Authoritative but static. They explain config placement; they do not execute a current runner/container/tool matrix and produce a failure packet. |
| Direct competitor | Docker daemon / Docker CLI proxy docs | Essential docs, but split daemon vs CLI vs Desktop behavior and do not cover git/npm/curl case precedence in one preflight. |
| Indirect substitute | netshoot, curl, wget, git config, npm config, ad hoc CI debug jobs | Flexible, but requires the operator to know which commands to run and how to interpret inconsistent proxy bypass behavior. |
| Status quo | Retry pipelines, paste proxy env vars into more places, inspect runner logs manually, or bypass the proxy entirely | Burns time, risks leaking proxy credentials into container metadata, and often creates false confidence because one tool succeeds while another still fails. |

## Wedge

ProxyEnv Doctor stays narrow: it is not a network debugger, runner manager, or proxy server. It is an executable proxy-env compatibility packet for the exact environment a CI job will run in.

The MVP can win by making a painful implicit matrix visible:

- which proxy vars are present at host, runner, shell, Docker, and container layers,
- which casing variants conflict,
- which `NO_PROXY` entries are likely ignored by specific tools,
- which tool-level configs override env vars,
- which generated GitLab Runner / Docker snippets would reduce drift.

## Target user

Developers and platform engineers running self-hosted GitLab Runner, Docker executor, or Docker-in-Docker behind a corporate or lab proxy.

## MVP

- `proxyenv-doctor scan` prints a Markdown and JSON packet of proxy env variables, redacting credentials.
- Matrix checks for curl, wget, git, npm, Docker CLI, Docker daemon hints, and GitLab Runner config snippets.
- Static rules for known `NO_PROXY` divergences: case precedence, ports, leading dots, wildcard use, and Docker-in-Docker `docker:2375` / `docker:2376` warnings.
- `proxyenv-doctor gitlab-snippet` emits copy/pasteable runner and `.gitlab-ci.yml` snippets for manual review.
- Fixture mode so the demo runs without real proxy credentials.

## Non-goals

- Not configuring production proxies automatically.
- Not storing, printing, or transmitting proxy credentials.
- Not replacing netshoot or packet captures.
- Not supporting every language runtime in the first slice.
- Not requiring live access to a corporate proxy for the demo.

## Status

v0.1.0-alpha.0 — scaffold/spec only.
