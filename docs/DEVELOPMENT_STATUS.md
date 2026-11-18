# Development status

**Public documentation | 18 November 2026**

T-Bot is an independently developed research and software-engineering project. I am learning as I build it, using AI-assisted development and review. It is not a qualified operational trading system or a public release. Nobody is being asked to deposit funds, connect a wallet or trust the bot with their SOL.

## What is established publicly

| Area | Status |
| --- | --- |
| Project goals and engineering principles | Documented |
| Private implementation | Under active development |
| System-wide functional qualification | Not claimed complete |
| Independent professional security certification | Not claimed |
| Verified paper-trading performance | Not available for publication here |
| Production readiness | Not achieved/claimed |
| Live-money execution | Not authorised |
| Public operational application or source distribution | None |
| Standalone educational example | Separate lab; not private application code or qualification evidence |
| Selected source-derived validation toolkit | Four standalone validators; [57/57 original and reproduction tests](../components/validation/TEST_RESULTS.md); not private-application qualification |
| Selected source-derived evidence integrity toolkit | Byte-integrity and strict JSON utilities; [historical V1 59/60, corrected Revision A and portable reproduction each 84/84](../components/evidence_integrity/TEST_RESULTS.md); not private-application qualification |

This table is a disclosure summary, not an audit of private implementation. It makes no claim about specific private test runs, their counts or outcomes.

## Who is reviewing the work?

Development is owner-led and AI-assisted. AI can help with analysis, code review, drafting test specifications and identifying weaknesses. It does not provide independent human assurance, and agreement between AI reviewers is not professional security certification. The owner remains responsible for engineering decisions and authorisation. No completed independent human audit is asserted in these public documents.

Security-first describes the priority given to risk reduction and verification; it does not describe a demonstrated security outcome. AI-generated code, analysis and test expectations can contain correlated errors. A credible assurance claim requires evidence of implementation behaviour, appropriate test coverage, reproducibility, limitations and independently established review provenance. No agreement between AI reviewers is treated as a substitute for independent human review.

## What needs to happen next?

The intended sequence is review of requirements and expected outcomes, preparation of controlled test environments, functional testing under fictional or simulated inputs, assessment of failures and independent review where available. Paper trading and any eventual live-money qualification are separate stages that require their own readiness decisions. No stage is authorised by this documentation.

Where results are eventually shared, the aim is to identify the tested scope, environment in non-sensitive terms, expected outcome, actual outcome, limitations and reviewer independence. Negative results and unresolved issues matter as much as passes.

See [testing](TESTING.md) and [community feedback](COMMUNITY_FEEDBACK.md).
