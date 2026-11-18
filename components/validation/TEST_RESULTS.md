# Observed Functional Test Results

Date: 2026-11-18 (UTC)

Python version: 3.12.3

Scope: standalone validation toolkit, fictional inputs only.

The source was preserved byte-for-byte from the earlier
57-case functional test. The portable harness preserves
the same case definitions.

The new harness was executed in a network-disabled
standalone test environment.

| Test group | Passed |
| --- | --- |
| Digest validation | 11/11 |
| Alias validation | 17/17 |
| Reason-code validation | 11/11 |
| Ordered integer validation | 18/18 |
| Total | 57/57 |

Failures: 0
Errors: 0
Skipped: 0

Tested source SHA-256:

    4ba70dc44ae3b467d896d226570f7b6b48add265df378516c3d9ca9702669dc2

Portable harness SHA-256:

    bf1193dc57163287afb35a1a5e16c6f3923a871ea68cde7c3b44b296fea2a8df

These are owner-run, AI-assisted functional tests.
No independent human review is claimed.
The results do not qualify the private application.

Developers are invited to reproduce and challenge these
results using the instructions in README.md and REVIEWERS.md.
