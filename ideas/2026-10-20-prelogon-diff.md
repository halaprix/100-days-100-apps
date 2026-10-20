# Day 084 — PreLogonDiff

Date: 2026-10-20
Status: idea-only

## One-line pitch

A local, read-only CLI that compares Windows EAP-TLS Wi-Fi evidence before and
after sign-in, showing which profile, certificate-store, or authentication-phase
assumption needs testing before an Intune rollout proceeds.

## Research brief

Decision: whether a phase-aware comparison deserves a dedicated app repository.
Target customer: small endpoint/network teams deploying Intune-managed Windows
certificate Wi-Fi, including Microsoft Cloud PKI deployments.
Geography: geography-independent Windows/Intune deployments.
Category: rollout troubleshooting, not a new PKI or RADIUS service.
Time horizon: a 1–3 day offline MVP; no fleet platform.
Must-answer question: does comparison add actionable information beyond the free
Windows WLAN report and Microsoft's existing troubleshooting instructions?
Evidence bar: fresh first-person pain plus official behavior documentation;
independent fixture validation is required before treating the wedge as proven.

## Evidence

| Source | Link | Signal |
|---|---|---|
| Fresh community report — Reddit RSS fallback, October 20, 2026, 03:59 UTC | [r/sysadmin: Intune EAP-TLS pre-logon failure](https://www.reddit.com/r/sysadmin/comments/1xai4af/intune_eaptls_wifi_has_anyone_got_machine_or_user/) | The author reports machine-only authentication working, but a machine-or-user profile failing at the sign-in screen and working after sign-in, with Cloud PKI and Intune. This is one report, not a diagnosed platform bug or community consensus. |
| Older independent community report — retrieved page | [HPE: user and computer certificate authentication](https://community.networking.hpe.com/discussion/cert-issue-eap-tls-authentication-certificate-based-for-both-user-and-computer-authentication) | A November 2025 thread describes separate device-without-login and signed-in-user certificate goals, with Intune, NDES and ClearPass. The author later reports resolving a template setting. This corroborates context/configuration confusion, not the exact fresh failure. |
| Official platform behavior — retrieved documentation | [Microsoft: Windows Wi-Fi settings](https://learn.microsoft.com/en-us/intune/intune-service/configuration/wi-fi-settings-windows) | User-or-machine selects device credentials when nobody is signed in and user credentials after sign-in. SSO timing is a separate setting. The mode label alone does not prove the deployed certificate and RADIUS paths work. |
| Official troubleshooting baseline — retrieved documentation | [Microsoft: troubleshoot Intune Wi-Fi profiles](https://learn.microsoft.com/en-us/troubleshoot/mem/intune/device-configuration/troubleshoot-wi-fi-profiles) | Microsoft already explains profile-event inspection, comparing certificate properties, and checking RADIUS logs when a deployed profile cannot connect. A new app must improve this workflow, not rediscover it. |
| Official native substitute — retrieved documentation | [Microsoft: wireless network report](https://support.microsoft.com/en-us/windows/analyzing-the-wireless-network-report-76da0daa-1db2-6049-d154-7bb679eb03ed) | The built-in WLAN report already includes three days of session events, profiles, and machine/user certificate listings. Collection alone is not a wedge. It also contains identifying system/user/network data, so safe sharing is a real design requirement. |
| Official protocol boundaries — retrieved documentation | [Microsoft: EAP for network access](https://learn.microsoft.com/en-us/windows-server/networking/technologies/extensible-authentication-protocol/network-access) | EAP-TLS, TEAP chaining, XML profiles, and server capabilities are distinct. A machine/user phase switch must not be conflated with simultaneous chained authentication. |

## Problem

A Wi-Fi profile can be deployed successfully without delivering connectivity at
the Windows sign-in screen. An operator then compares portal settings, local
profiles, certificate stores, client events and RADIUS evidence manually. A
successful signed-in connection is not sufficient proof of a working pre-logon
path.

The fresh report supports a blocked rollout/connectivity problem. It does not
measure weekly time loss or establish the root cause. The status-quo pain test
passes on rollout interruption and the risk of weakening authentication during
trial-and-error, not an invented claim of hours saved. Existing free tools may
already be fast enough; that remains the main falsification test.

## Target user

An Intune administrator and a network counterpart piloting Windows EAP-TLS Wi-Fi
where machine-only works but user-or-machine behavior differs across sign-in.
Start with one endpoint and one SSID, not an entire enterprise estate.

## MVP scope

- Accept explicitly supplied, local WLAN XML, allowlisted certificate metadata,
  and exported WLAN/EapHost event XML from a working and failing observation.
- Require each observation's phase and collection context. Do not infer a
  historical pre-logon certificate store from a later interactive-user snapshot.
- Normalize authentication mode, SSO timing, EAP method, certificate-store scope,
  validity and client-auth EKU metadata; explain mismatches with source links.
- Emit a phase-by-phase comparison with three result classes: observed mismatch,
  plausible hypothesis, and missing evidence. Never call it proof of root cause.
- Include an optional manually supplied RADIUS result. Without it, label server
  authorization, mapping and trust outcomes unknown.
- Produce local JSON and Markdown, with identifiers omitted by default and an
  explicit preview before any support sharing. Never export private keys or
  plaintext Wi-Fi secrets; never upload raw WLAN reports.
- Test three fixture pairs: user-store-only candidate, differing profile mode,
  and insufficient evidence. Use PowerShell for a future allowlisted collector;
  the first slice only parses saved inputs.

Non-goals: automatic remediation, disabling server-certificate validation,
collecting pre-logon evidence through a newly installed privileged service,
arbitrary RADIUS troubleshooting, TEAP migration, or operating a CA.

## Shortlist and wedge-first gate

Constraint: **Subtract** — reuse native diagnostics and add only a missing
comparison, rather than build another management console. Gates below were
applied before the selected candidate's score; rejected candidates are unscored.

### 1. PreLogonDiff — selected, narrowed

Intune Windows Wi-Fi pilot owner → native WLAN report, Intune troubleshooting,
certificate-provider support and manual before/after comparison → these supply
much of the evidence but leave phase/context reconciliation to the operator;
whether that is painful enough remains unproven → offline phase-aware comparison
of one working/failing pair → an exact-symptom walkthrough for Intune operators
and an opt-in fixture review with endpoint/network consultants → a fresh report
shows machine-only success versus machine-or-user pre-logon failure.

- Direct competition: Windows' native WLAN report is the strongest same-job
  diagnostic; SecureW2's Intune integration documentation appears in search but
  full product coverage could not be inspected. Treat that as an unresolved
  competitor, not evidence it lacks this feature.
- Indirect substitutes: Microsoft's checklist, Event Viewer, certificate-store
  inspection, SCEPman troubleshooting/logs, and a support engineer.
- Status quo: compare profiles/events manually or retain machine-only while
  validating whether it satisfies the actual access policy.
- Gate: narrow enough for research, but no proven acquisition loop; idea only.
- Kill: native reporting plus a short checklist is equally fast, or a provider
  already produces the same phase-aware explanation without infrastructure change.

### 2. RebuildTrust — rejected

Admins rebuilding frequently replaced VMs → OpenSSH host certificates, Smallstep
and provisioning scripts → manual fingerprint approval breaks automation but
host certificates already address changing host keys → hypothetical rebuild-to-key
approval receipt → provisioning guides for VM administrators → a fresh
[r/sysadmin host-key question](https://www.reddit.com/r/sysadmin/comments/1xaeujc/how_do_you_handle_ssh_host_keys_on_servers_that/).

- Direct competition: [Smallstep host certificate setup](https://smallstep.com/docs/ssh/hosts/)
  explicitly enrolls hosts and rotates certificates;
  [its open-source tutorial](https://smallstep.com/docs/tutorials/ssh-certificate-login/)
  configures OpenSSH client trust for host CAs.
- Indirect substitutes: signed provisioning inventory and manual fingerprint
  verification through an independent trusted channel.
- Status quo pain: strict-checking automation fails after rebuild, or an operator
  is tempted to accept a changed key without authenticating it.
- Gate/kill: real security pain, but no evidence a new approval app beats existing
  host-CA enrollment. Reject before scoring; never automate blind key acceptance.

### 3. MailPolicyPilot — rejected

Small-domain mail administrators considering MTA-STS → EasyDMARC checks,
URIports hosting, documentation and manual HTTPS policy hosting → setup uncertainty
exists but established products already check records and manage policies →
hypothetical testing-to-enforcement guide → exact MTA-STS setup searches → a fresh
[r/sysadmin implementation discussion](https://www.reddit.com/r/sysadmin/comments/1xald65/your_thoughs_on_mtasts_implementation/).

- Direct competition: [EasyDMARC's free checker](https://easydmarc.com/tools/mta-sts-check)
  checks DNS and HTTPS policy and explicitly supports pre-enforcement testing;
  [URIports](https://www.uriports.com/features/hosted-mta-sts) hosts and maintains
  policies and validates the setup.
- Indirect substitutes: manual DNS/HTTPS configuration, TLS reports and a mail
  administrator's rollout checklist.
- Status quo pain: bad enforcement can defer delivery, but this fresh source is
  an opinion request, not evidence of repeated failed deployments or paid demand.
- Gate/kill: proposed scope overlaps existing options and lacks a proven gap.
  Reject before scoring. Do not interpret MTA-STS as rejecting arbitrary senders;
  it constrains TLS delivery behavior for participating sending systems.

## Competitor / Substitute Check

| Type | Name / Substitute | Notes |
|---|---|---|
| Direct diagnostic substitute | Native Windows WLAN report | Already collects session histories, profiles and certificate listings. The proposed addition is explicit paired phase/context comparison, not a new collection bundle. |
| Direct workflow substitute | Microsoft Intune Wi-Fi troubleshooting | Already tells operators to inspect events, certificate properties and RADIUS logs. If the same checklist resolves representative cases as quickly, stop. |
| Potential direct competitor — inspection incomplete | SecureW2 Intune/802.1X tooling | Search surfaced enrollment/configuration documentation; full pages were bot-blocked. Do not claim the product lacks pre-logon diagnostics or compare unverified pricing. |
| Indirect substitute | SCEPman troubleshooting and logs | Retrieved vendor docs point to common problems and Log Analytics. Relevant when its certificate service is already used; not proof of a cross-phase comparison feature gap. |
| Indirect substitute | Event Viewer, certificate console and support ticket | Flexible and already installed; manual interpretation may be entirely sufficient. |
| Status quo | Keep the working configuration and troubleshoot the pilot | Avoids adopting a new tool but can leave a required sign-in workflow unvalidated. Machine-only may be acceptable; the app must not assume every deployment needs user switching. |

## Wedge

Only the **paired phase/context explanation** is potentially differentiated.
Native reports already collect most inputs. The app would make uncertainty
explicit: which observation used machine versus user context, which deployed
setting changed, and what still requires server evidence. It must not promise
that one certificate-store mismatch explains every pre-logon failure.

The first-user hypothesis is endpoint/network consultants searching the exact
symptom and reviewing a worked, redacted before/after case. That is a specific
validation path, not demonstrated repeatable access. No outreach or social
interaction was performed in this run.

## Kill condition

Compare three independently supplied, consented fixture pairs against a native
WLAN report plus the Microsoft checklist. Reject if the new comparison gives no
additional actionable finding, if ordinary operators already diagnose the cases
as quickly, or if useful evidence requires persistent privileged capture that
cannot fit the MVP. Also stop if vendors already provide equivalent paired
analysis or if no repeatable first-user route emerges. Never weaken certificate
validation to make a fixture pass.

## Scoring

| Dimension | Score | Notes |
|---|---:|---|
| Usefulness | 4/5 | A documented pilot symptom blocks a sign-in connectivity requirement; recurrence of the exact failure and willingness to pay remain unmeasured. |
| Feasibility | 4/5 | Saved XML/metadata comparison fits a 1–3 day slice. Safe real pre-logon capture and broad server diagnosis do not. |
| Demo potential | 4/5 | A before/after phase matrix can show an observed mismatch and an honest unknown; a full Wi-Fi lab demo is more involved. |
| Distribution | 3/5 | Specific Intune operators and symptom searches exist, but repeatable access and adoption are unvalidated. |
| Competitive wedge / timing | 3/5 | Fresh exact symptom and a narrow comparison hypothesis; native reports are strong and provider coverage is not fully inspected. |
| Total | 18/25 | Numeric threshold met; Distribution fails the 4/5 repository gate. |

## Decision

**idea-only; no dedicated repository created.** Total is **18/25**, with
Distribution and competitive wedge/timing tied weakest at **3/5**. Distribution
blocks repository creation. This is a testable workflow hypothesis, not a claim
of a new Intune defect, a validated market or an unserved diagnostic category.
The brief is the research artifact; no application was implemented today.

## Next build step

Make a fixture-only spike that parses two explicitly phase-labelled WLAN XML
observations and an allowlisted certificate-metadata file, producing a local
comparison with observed/hypothesis/unknown labels. Benchmark the output against
the native WLAN report/checklist on three consented cases before promoting this
to a dedicated app. Follow-up validation is tracked as `apps-brl`.

## Source access caveats

Reddit public JSON returned the documented theme-beta `403`; r/sysadmin RSS
fallback returned seven fresh entries. Its score/comment-count zeros mean
unavailable, not no engagement. The selected thread's comment-context fetch also
returned `403`, so no replies or accepted root cause are claimed. r/selfhosted
and r/webdev JSON/RSS collection was unavailable with `429` warnings; constrained
web searches produced no usable fresh replacement evidence. No request loop was
used.

X account lookup worked, but read-only search returned `401 Unauthorized` and
no OAuth2 token was present. A web fallback returned two related X snippets,
neither used as fresh demand evidence. No X validation is claimed.

Microsoft, HPE, Smallstep, EasyDMARC and URIports pages were retrieved. SecureW2
pages were bot-blocked; their search snippets establish only that relevant
integration material exists, not its full feature set. A SCEPman HTML page was
empty; Markdown retrieval exposed an invalid path and then allowed retrieval of
the canonical troubleshooting and Intune pages:
[troubleshooting](https://docs.scepman.com/other/troubleshooting.md) and
[Intune](https://docs.scepman.com/certificate-management/microsoft-intune.md).
No current price claims or willingness-to-pay estimates are made. Evidence
supports researching the pain with moderate confidence; differentiated utility
and commercial demand remain low-confidence hypotheses.
