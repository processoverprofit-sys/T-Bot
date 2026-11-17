# Public risk-control principles

**Status:** Intended requirements for discussion, not a published operational policy, trading strategy or verification result. Actual internal thresholds, tuning, implementation and configurations are excluded.

| ID | Condition | Intended result |
| --- | --- | --- |
| RP-01 | A required critical input is absent or invalid | Reject eligibility; do not treat missing information as safe. |
| RP-02 | Available evidence cannot establish a mandatory risk requirement | Do not proceed to execution. |
| RP-03 | A mandatory exposure or loss limit would be violated | Prevent further exposure. |
| RP-04 | Required liquidity, execution-cost or exit feasibility conditions are not established | Do not treat the opportunity as eligible. |
| RP-05 | Required authorisation is absent or invalid | Prevent execution regardless of earlier eligibility. |
| RP-06 | A critical integrity or validation failure occurs | Stop the affected operation rather than silently continue. |
| RP-07 | Required evidence of a decision or outcome cannot be established | Treat the result as unqualified; investigate before accepting it. |

These public requirements are deliberately expressed as abstract predicates. They are not the private rule registry or a claim of tested coverage. IDs here are local to this public document and are not internal control identifiers.

## Rule-based decision boundary

The intended decision process evaluates explicit requirements using validated inputs, a defined policy version and relevant state. AI-generated advice is not a substitute for a required rule result or execution authorisation. This is a design requirement, not a claim that the private implementation has passed an isolation or reproducibility test.

## Limitations

Risk checks do not guarantee that a token is safe, that an exit remains possible, or that a trade is profitable. Liquidity and execution costs may change rapidly. Deterministic processing does not make financial markets deterministic. Security qualification and evidence of trading performance are different things.

## Feedback requested

Are these requirements stated clearly enough to be testable? Which failure categories should be represented separately? What evidence would be necessary to evaluate them without access to operational secrets?

See [testing](TESTING.md) for illustrative cases.
