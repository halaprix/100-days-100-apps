# PushBench

PushBench is a local benchmark harness and cost packet for choosing ntfy vs Autopush/Sunup as a self-hosted UnifiedPush backend before real Android users depend on it.

## Problem

Self-hosted UnifiedPush operators have several backend options, but the decision often happens through anecdotes: ntfy is easy, Autopush is Rust/WebSocket-native, public servers are convenient, and generic load tools require too much custom scenario work. The missing piece is a local, comparable readiness packet for registration, reconnect, publish, receive, latency, errors, and rough VPS sizing.

## Target user

Self-hosted UnifiedPush operators, de-Googled Android community maintainers, small app communities, and privacy-focused service admins deciding whether to run ntfy, Autopush/Sunup, or another push backend for real users.

## MVP

- Read a YAML load profile with devices, reconnects, publish rate, payload sizes, target SLO, and budget.
- Generate backend-specific local scenarios for ntfy HTTP/WebSocket and Autopush-style flows.
- Run only against local Docker Compose fixtures in the first slice.
- Render a markdown/JSON push readiness packet with latency, error/429 rate, CPU/RAM/network envelope, and recommendation.
- Refuse to target public/default push servers by default.

## Non-goals

- No load tests against public ntfy, Mozilla, or third-party push infrastructure.
- No mobile app replacement, push provider, hosted SaaS, or dashboard in the first slice.
- No guarantee of production capacity from synthetic benchmarks alone.
- No collection of real user tokens, device identifiers, or notification payloads.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Reddit / r/selfhosted | https://www.reddit.com/r/selfhosted/comments/1vnwk04/nfty_vs_autopush_for_degoogled_android_push/ | Fresh operator asks which backend is better for performance/cost at thousands of users. |
| UnifiedPush docs / Distributors | https://unifiedpush.org/users/distributors/ | Documents the distributor and self-hosted push-server choice. |
| UnifiedPush docs / ntfy | https://unifiedpush.org/users/distributors/ntfy/ | ntfy is a UnifiedPush distributor with public or self-hosted server options. |
| Mozilla Autopush docs | https://mozilla-services.github.io/autopush-rs/ | Autopush-rs documents a Rust/WebSocket push server architecture. |

## Current status

v0.1.0-alpha.0 — scaffold/spec only, consolidated in the 100-days master repo.
