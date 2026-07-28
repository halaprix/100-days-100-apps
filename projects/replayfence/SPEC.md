# SPEC — ReplayFence

## User story

As a small SaaS developer receiving third-party webhooks, I want to replay captured payloads under duplicate/retry/out-of-order delivery scenarios, so that I can prove my handler is idempotent before launch.

## Core flow

1. Developer captures or saves a webhook fixture with headers and body.
2. Developer runs `replayfence run --target http://localhost:3000/webhook --fixture fixture.json --scenario duplicate,retry`.
3. ReplayFence sends scenario deliveries to the target with realistic timing and stable delivery IDs where appropriate.
4. ReplayFence runs optional side-effect probes after each scenario.
5. ReplayFence writes a JSON/Markdown report: pass/fail, status-code behavior, latency, duplicate side effects, and retry-hostile responses.

## Data model

```text
Fixture
- provider: stripe | github | generic
- headers: map<string,string>
- body: json | string
- idempotency_key_path: optional json pointer

Scenario
- name: duplicate | concurrent | delayed-retry | out-of-order | malformed
- deliveries: list<DeliveryStep>

DeliveryStep
- delay_ms
- header_overrides
- body_mutation
- expected_status_family

Report
- target
- fixture
- scenarios
- deliveries
- side_effect_probe_results
- failures
```

## Technical approach

- Start as a small Python CLI with `argparse` or `typer`.
- Use `httpx` for HTTP delivery and timeouts.
- Use plain JSON fixtures to avoid provider credentials.
- Keep provider presets as data files, not hard-coded branches where practical.
- Support side-effect probes as shell commands or HTTP checks that return JSON.
- Prefer deterministic local tests over live provider calls.

## Validation plan

- Include one intentionally non-idempotent demo handler that increments a counter on every delivery.
- Include one fixed handler that deduplicates by event ID.
- Verify ReplayFence fails the naive handler and passes the fixed handler.
- Compare MVP positioning against Hookdeck/Svix/ngrok/Stripe CLI: if they already offer equivalent receiver-side assertion packs, narrow provider support rather than competing broadly.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and public spec.
- v0.1.0-alpha.1 — CLI skeleton, JSON fixture loader, duplicate replay scenario.
- v0.2.0-alpha.1 — provider presets, side-effect probes, Markdown report, demo handlers.
