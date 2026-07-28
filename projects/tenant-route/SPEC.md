# SPEC — TenantRoute

## User story

As a small-team Microsoft 365 admin facing a tenant-country or CSP-region mismatch, I want a local decision packet that explains whether migration is likely unavoidable and what to ask my CSP/Microsoft, so that I do not waste days in scattered docs or walk into a vendor call unprepared.

## Core flow

1. User starts a local CLI or static web flow.
2. User enters current tenant country, target operating/billing country, current CSP/direct relationship, subscription counts, identity model, domains, workloads, compliance drivers, and deadline.
3. TenantRoute evaluates answers against a YAML ruleset.
4. User receives:
   - risk summary,
   - decision memo,
   - CSP/Microsoft support question list,
   - migration scoping packet,
   - action register.
5. User can export Markdown/CSV and attach it to an internal ticket or vendor email.

## Data model

```yaml
scenario:
  organization_name: string
  current_tenant_country: string
  target_billing_country: string
  current_commercial_channel: direct|csp|unknown
  target_channel: direct|csp|unknown
  user_count: integer
  subscriptions:
    - sku: string
      seats: integer
      term: monthly|annual|unknown
  identity:
    model: cloud_only|hybrid|unknown
    custom_domains:
      - domain: string
        transfer_required: boolean
  workloads:
    exchange: boolean
    sharepoint: boolean
    onedrive: boolean
    teams: boolean
    dynamics: boolean
    azure: boolean
  drivers:
    - local_billing
    - compliance
    - tax
    - data_residency
    - consolidation
  deadline: date|null
```

## Technical approach

- Start with a TypeScript CLI or small static app.
- Keep all data local; no credentials or API tokens.
- Store rules in versioned YAML files with source links.
- Generate Markdown from templates so output can be inspected and edited.
- Include sample scenarios for demos and regression checks.

## Rule classes

- Tenant country immutability risk.
- CSP sales-territory mismatch risk.
- Subscription transfer/reprovisioning questions.
- Domain and identity sequencing risks.
- Workload migration complexity flags.
- Deadline pressure and escalation checklist.

## Validation plan

- Compare generated packet against Microsoft Learn tenant-to-tenant planning docs and CSP regional authorization docs.
- Run the sample HK→UAE scenario from the public Reddit signal.
- Ask 2–3 Microsoft 365 admins/MSPs whether the output would improve a CSP/vendor discovery call.
- Kill or narrow the product if admins say CSPs already provide equivalent prep quickly for free.

## Milestones

- v0.1.0-alpha.0 — repo scaffold.
- v0.1.0-alpha.1 — CLI reads a scenario YAML and renders Markdown packets.
- v0.2.0-alpha.1 — guided questionnaire plus sample scenarios.
- v0.3.0-alpha.1 — static web demo with no backend.
