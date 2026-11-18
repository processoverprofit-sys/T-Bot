# External contribution security policy — V1

Status: proposed public contribution process; not evidence of implemented private controls or operational qualification.

Public contributions are untrusted input. A public merge never authorises promotion to a private system, execution with credentials, or financial activity.

## Acceptance boundary

1. Limit submissions to approved public standalone components and documentation. Do not include private material or request access to private systems.
2. Record the exact proposed commit and inspect all changed files, including tests, fixtures, configuration, dependencies and automation. Re-review any changed commit. A contributor's own tests or assurances are not independent evidence.
3. Reject unexplained executable content, unexpected dependencies, obfuscation, scope expansion, credential requests, or unexpected network or filesystem behaviour. Treat unresolved findings as blocking. Report sensitive findings through the security policy, not public issues.
4. Review untrusted code before running it. If testing is separately approved, use a disposable isolated environment without credentials, private data, wallets, privileged access, host mounts or private runners; deny unnecessary network access and bound resources. Do not use a production or development host as a sandbox.
5. Check dependency provenance, changes to build and test tooling, and independent regression evidence. Passing tests, scanners or matching hashes alone do not establish safety.
6. Require maintainer acceptance of the exact reviewed revision. No self-approval by contributors, automatic merge or bypass of required review. Public acceptance is a separate decision from private integration.
7. Retain the review record, reviewed revision, test scope, limitations and decision. Any later change requires renewed review.

## Private boundary

No public contribution is automatically imported into private systems. Any future private integration requires a separate owner-authorised qualification process. Public reviewers receive no private-system or financial authority.

## Repository controls to verify separately

Require pull requests and independent approval for the protected branch, invalidate stale approvals, restrict bypass, prevent force pushes and deletion, and verify automation permissions and external collaborator access. Do not run untrusted contributions in privileged workflows or on private runners. This document does not configure or certify GitHub settings.

See [CONTRIBUTING.md](../CONTRIBUTING.md), [SECURITY.md](../SECURITY.md), and the [public threat model](THREAT_MODEL.md).
