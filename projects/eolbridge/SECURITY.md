# Security Policy

## Supported versions

EolBridge is pre-release. Security fixes apply to the latest scaffold and future alpha releases only.

## Reporting issues

Open a GitHub issue in the 100-days master repo with a minimal public-safe reproduction. Do not include real Composer auth files, database URLs, client names, private domains, API keys, tokens, or production packet outputs.

## Data handling

The MVP is local-first and fixture-driven. It should not connect to Drupal admin panels, databases, hosting providers, or production servers. Inputs must be sanitized before sharing.
