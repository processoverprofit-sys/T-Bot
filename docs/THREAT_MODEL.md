# Public threat model

**Status:** Preliminary and non-exhaustive. A conceptual engineering review aid, not a security audit, certification or disclosure of internal defences.

## Assets and trust boundaries

The design seeks to protect credentials, authorisation decisions, financial exposure, software integrity and the reliability of recorded evidence. External market information is not inherently trusted. Risk assessment must not imply execution permission. Public documentation and community interactions are outside the private operational boundary.

| Threat or failure | Possible consequence | Intended control objective | Residual uncertainty |
| --- | --- | --- | --- |
| Malicious token or misleading market information | Financial loss or invalid risk assessment | Defensive validation and rejection of uncertain critical conditions | A token may change behaviour or evade screening. |
| Abrupt liquidity loss, adverse price changes or slippage | Execution or exit differs from assumptions | Require acceptable risk and execution conditions | Market changes may defeat prior assumptions. |
| Missing, stale or contradictory observations | Incorrect eligibility decision | Fail closed on required information failures | Freshness and consistency need qualification. |
| Credential exposure | Unauthorised access or signing | Keep secrets separate from distributable code and restrict authority | Separation must be verified; no audit claim here. |
| Authorisation bypass | Unapproved execution | Separate eligibility from permission | Boundary enforcement requires testing. |
| Software or dependency integrity failure | Incorrect or compromised behaviour | Verify integrity and handle failures defensively | Provenance and update controls require evidence. |
| Incomplete or misleading test evidence | False confidence | Record scope, expected and actual outcomes; distinguish unverified claims | Review independence and reproducibility matter. |

This model intentionally omits private deployment details, control mechanics, identities, sensitive evidence and exploitable findings. It is not permission to investigate or test any private system.

## Open questions

What additional threat categories should be included? How should residual risk be communicated? What types of independent review would make these control objectives more credible?

Use [CONTRIBUTING.md](../CONTRIBUTING.md) for public-safe documentation feedback and [SECURITY.md](../SECURITY.md) for confidential reporting within its defined scope.
