# Stage 7 — Security and publication quality checklist

**Status:** Review proposal only. This document does not qualify T-Bot for operation or authorise live-money execution.

## Historical verified public repository baseline (17 November 2026, before the Issues setting changed)

- `main` is covered by an active ruleset preventing deletion and force pushes, but not requiring pull requests or approvals.
- Issues and Discussions are disabled; issue templates are dormant.
- The repository is public documentation, not a release of operational source.
- `docs/TESTING.md` contains fictional, unexecuted examples, not observed test results.
- The threat model is preliminary; no independent security certification or verified paper-trading performance is claimed.
- The existing `SECURITY.md` describes private vulnerability reporting; the live GitHub setting has not been independently confirmed.

## Subsequent configuration update (17 November 2026)

The maintainer enabled public Issues; the setting was verified. Issues are now available for non-sensitive tasks and feedback under [CONTRIBUTING.md](../CONTRIBUTING.md). The historical baseline above is retained for traceability. This does not authorize private access, a new component release, or any operational activity. Private vulnerability reporting remains unverified. Other settings are outside this update.

## Before proposing a public change

| Gate | Requirement |
| --- | --- |
| Scope | Documentation only; no application source, private fixtures or internal operational details |
| Privacy | No real names, personal email, wallet addresses, keys, API credentials, signing data, internal paths or unpublished evidence |
| Accuracy | Label each statement as objective, historical record, observed result or unverified proposal |
| Evidence | Do not describe fictional cases as passed; publish actual results only after independent evidence and disclosure review |
| Security | Never publish vulnerabilities or sensitive findings in public PRs or discussions |
| Review | Inspect changed files and public commit identity before any merge |
| Operational authority | No trade, wallet access, signing, runtime qualification or production admission is authorised |

## Owner-only GitHub configuration review

1. Assess a mandatory PR-to-main rule without locking out the single maintainer; retain existing no-delete/no-force-push protection.
2. Independently confirm private vulnerability reporting, secret scanning and push protection availability and state.
3. Inspect repository and app permissions, tokens and Actions permissions without exposing secrets.
4. Consider a strictly documentation-only link/Markdown check in a **separately approved** PR. No shell commands from untrusted contributions, secrets, trading dependencies or private code.
5. Historical recommendation: leave Issues and Discussions disabled unless a moderation and reporting process is separately approved. Public Issues have since been separately enabled by the maintainer; the public contribution and security policies still apply. No change to Discussions is authorized by this update.

## Public evidence standard (future, conditional)

A potential non-sensitive report should identify: claim or requirement; scope; evidence provenance; date; expected and observed outcomes; limitations; independent reviewer role if applicable; disclosure approval. If a field is unknown, mark it **not established**, never **PASS**.

## Review outcome

This checklist is a proposal, not proof of implemented controls. Repository settings, authentication, public access routes, branch deletion, operational software and financial activity remain unchanged pending separate approval.
