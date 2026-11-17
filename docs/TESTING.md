# Testing methodology and illustrative cases

**Status:** Proposed public test specifications. The examples below are fictional and have not been run or verified against the private application as part of this documentation. They are not actual private test records, an executable test suite, evidence of successful testing or paper-trading results.

## Proposed method

Define a requirement and a precise expected outcome before testing. Use controlled, non-live inputs and distinguish positive, negative and boundary cases. Record actual outcomes independently of the expectation, including failures and uncertainty. Repeat where reproducibility matters and record the reviewer's relationship to the work. Do not infer overall production readiness from isolated tests.

## Illustrative test specifications

| Example | Fictional setup / stimulus | Expected result | Requirement | Actual outcome |
| --- | --- | --- | --- | --- |
| EX-01 | Required input A is missing; other inputs are valid. | Reject eligibility. | RP-01 | Not run |
| EX-02 | A mandatory risk check returns UNKNOWN. | No execution; no implicit pass. | RP-02 | Not run |
| EX-03 | A fictional exposure policy reports LIMIT_EXCEEDED. | Prevent additional exposure. | RP-03 | Not run |
| EX-04 | A required market-condition check returns UNAVAILABLE. | Do not grant eligibility. | RP-04 | Not run |
| EX-05 | Eligibility is true; authorisation is absent. | No execution. | RP-05 | Not run |
| EX-06 | A critical integrity check returns FAIL. | Stop the affected operation. | RP-06 | Not run |
| EX-07 | A required decision record cannot be established. | Do not accept the result as qualified. | RP-07 | Not run |

The case names and symbolic inputs are illustrative only. No private fixtures, thresholds or execution procedures are included. See [risk principles](RISK_PRINCIPLES.md) for the corresponding public requirements.

## Additional proposed decision-boundary tests

The following fictional specifications address the distinction between rule-based decisions and AI-assisted development. They are unexecuted and do not establish that the private implementation meets the stated expectations.

| Example | Fictional stimulus | Expected design outcome | Actual outcome |
| --- | --- | --- | --- |
| EX-08 | Repeat an evaluation with identical validated inputs, policy version and relevant state. | Identical eligibility and risk decisions. | Not run |
| EX-09 | A fictional AI recommendation conflicts with a required rule outcome. | The recommendation does not replace the rule outcome or grant eligibility. | Not run |
| EX-10 | A fictional recommendation or eligibility result is supplied without execution authorisation. | No execution authority is granted. | Not run |

These are proposed assurance questions, not a claim that any model is connected to the runtime. Deterministic rule evaluation and security qualification are separate questions. Test results must be supported by observed evidence and appropriate review.

## Evidence and paper trading

No verified paper-trading logs or performance results are supplied here. The project is not qualified for live trading. Future public evidence, if available and approved, should distinguish simulated results, paper trading, functional tests and independent review. Simulated or paper results cannot establish real execution performance and may underrepresent fees, liquidity changes and slippage.

A future public evidence summary should include a case identifier, test scope, expected outcome, actual outcome, pass/fail/blocked status, date, limitations and review provenance. No result should be fabricated or labelled as passed merely because its expected outcome is documented.

Feedback on the proposed methodology and case completeness is welcome.
