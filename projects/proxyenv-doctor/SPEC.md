# SPEC — ProxyEnv Doctor

## User story

As a developer running self-hosted CI behind a proxy, I want an executable proxy-env compatibility packet before a job runs, so that I can fix `HTTP_PROXY`, `HTTPS_PROXY`, and `NO_PROXY` drift without burning a deploy window.

## Core flow

1. User runs `proxyenv-doctor scan --fixture gitlab-dind` or `proxyenv-doctor scan` in a runner shell/container.
2. The CLI collects proxy-related environment variables and selected tool config safely.
3. It redacts credentials and private host details from output.
4. It evaluates a static compatibility matrix for common tools.
5. It emits a Markdown/JSON packet with warnings, likely root causes, and reviewed snippets.

## Data model

```text
ScanInput
- environment: map<string,string>
- tool_presence: map<tool,bool>
- tool_config: map<tool,map<string,string>>
- fixture_name: optional string

MatrixFinding
- severity: info | warning | risk
- tool: curl | wget | git | npm | docker-cli | docker-daemon | gitlab-runner | dind
- variable: optional string
- message: string
- evidence: string
- recommendation: string

ScanPacket
- generated_at: string
- findings: MatrixFinding[]
- redactions: string[]
- snippets: map<string,string>
```

## Technical approach

- Start as a small Python CLI using only the standard library.
- Keep rules in versioned JSON so behavior is easy to review.
- Redact proxy URLs by removing credentials and replacing host labels in human output unless fixture mode is enabled.
- Use subprocess probes only for read-only commands such as `curl --version`, `git config --get http.proxy`, and `npm config get proxy`.
- Never perform network calls by default; optional live probes must be explicit.

## Validation plan

- Unit-test fixture scans for common failure modes: uppercase/lowercase conflict, missing `NO_PROXY`, Docker-in-Docker port omission, npm config override, and proxy credentials in URLs.
- Run a smoke command in CI that generates Markdown and JSON from fixtures.
- Compare output against GitLab and Docker documentation examples.
- Validate the wedge by posting a fixture packet in developer/admin communities and checking whether users can map it to their own CI failures.

## Milestones

- v0.1.0-alpha.0 — repo scaffold and specification.
- v0.1.0-alpha.1 — standard-library CLI with fixture mode and Markdown/JSON output.
- v0.2.0-alpha.1 — read-only local probes for curl, git, npm, Docker, and GitLab Runner config hints.
- v0.3.0-alpha.1 — optional live target probe and generated remediation snippets.
