# Community feedback and response

**17 November 2026 — Initial documentation response**

Thank you to the people who took the time to challenge my original project introduction on Reddit. I asked for feedback because I'm still learning how to build T-Bot properly and how to explain my work to other developers. The discussion made it clear that my original project overview was not enough for meaningful technical review.

This is not a request for investment, free operational testing or access to anyone's SOL. I want to learn from experienced developers and improve how I document the project.

| Feedback received (paraphrased) | Response in these documents | Remaining work |
| --- | --- | --- |
| Publish risk rules instead of asking people to trust the project description. | [Public risk principles](RISK_PRINCIPLES.md) give testable, high-level requirements. | Detailed operational policy remains private; no verification claim. |
| Provide paper-trading logs. | [Testing](TESTING.md) explicitly states that verified paper-trading results are not available here. | No logs published; qualification comes first. |
| Explain who is performing security qualification and distinguish AI review from independent assurance. | [Development status](DEVELOPMENT_STATUS.md) describes owner-led, AI-assisted work and the limits of assurance claims. | No completed independent human audit asserted. |
| Address slippage and rapidly changing or malicious tokens. | [Threat model](THREAT_MODEL.md) describes these risks and residual uncertainty. | Private control effectiveness is not established by this document. |
| Publish a threat model and actual test cases. | [Threat model](THREAT_MODEL.md) and [illustrative test specifications](TESTING.md) provide a starting point for review. | Actual private test records and verified public results have not been published. |

## Follow-up feedback — 17 November 2026

Two further questions highlighted ambiguity in the distinction between security objectives, AI-assisted development and runtime decision-making.

| Feedback (paraphrased) | Documentation response | Remaining evidence |
| --- | --- | --- |
| How can security be a priority if AI reviews are limited? | The [README](../README.md) and [development status](DEVELOPMENT_STATUS.md) explicitly distinguish security objectives from achieved assurance. AI review is not independent human assurance. | Implementation evidence and independent review are not established by this update. |
| Are decisions fixed rules or a model selecting trades? | The intended decision path is rule-based; AI assists development rather than choosing trades or granting authority. See [architecture](ARCHITECTURE.md) and [risk principles](RISK_PRINCIPLES.md). | Implementation-level reproducibility and separation evidence remain required. |

The [testing document](TESTING.md) includes additional fictional specifications for these questions. They are not executed tests or proof of security.

## Follow-up: requested risk-veto evidence

A further reviewer asked for genuine observed evidence of risk rejection and non-invocation of the executor. That remains outstanding: no accepted, disclosure-approved observation of the actual T-Bot sequence is supplied here. The [standalone lab](../examples/review_gate/README.md) demonstrates only a fictional review gate with a dummy counter and cannot satisfy that request. See [starter tasks](../community/START_HERE.md) for public work on test design and evidence quality.

## Follow-up: genuine source-derived component — 18 November 2026

In response to requests for actual code and reproducible tests, the [Validation Toolkit V1](../components/validation/README.md) makes four selected, non-operational source-derived validators available under a toolkit-only MIT licence. The [observed results](../components/validation/TEST_RESULTS.md) record two 57/57 owner-run, AI-assisted standalone runs. This does not supply the outstanding private risk-veto or execution evidence. The original [test plan](../components/validation/TEST_PLAN.md) is historical, not a statement of current test status. Experienced developers are invited to challenge the implementation via the [review guide](../components/validation/REVIEWERS.md) and [ENG-02](https://github.com/processoverprofit-sys/T-Bot/issues/8).

## Where I would appreciate help

- Critique the public threat model: what important risks or assumptions are missing?
- Suggest how to express risk requirements so their expected behaviour is unambiguous.
- Review the proposed test cases and suggest additional failure or boundary cases using fictional inputs.
- Suggest ways to present reproducible evidence without exposing sensitive implementation or personal information.

Non-sensitive lab and validation-toolkit changes and documentation corrections may be proposed through public pull requests at the maintainer's discretion. [Public Issues](https://github.com/processoverprofit-sys/T-Bot/issues) are enabled for non-sensitive engineering tasks, documentation corrections and general feedback. Please read [CONTRIBUTING.md](../CONTRIBUTING.md) and [SECURITY.md](../SECURITY.md). Do not submit operational source, sensitive information or vulnerabilities publicly.

## Continue the discussion on Discord

ProcessOverProfit also has a dedicated Discord community, connected to GitHub through repository notifications. It provides a place for project followers and approved developers to discuss public-safe engineering ideas, ask questions and learn from one another. If you found T-Bot through a community discussion, you can express interest in joining there where the rules permit. Invitations and developer access are managed by the maintainer; no private code or operational access is granted by joining. See the [central invitation-request guidance](https://github.com/processoverprofit-sys/Processoverprofit-sys/blob/main/docs/COMMUNITY.md#requesting-discord-access) for the current joining status.

I appreciate constructive criticism. This is the first step toward making the project easier to understand, not a claim that the underlying software has been independently verified.

**Process Over Profit — Verification Before Execution.**
