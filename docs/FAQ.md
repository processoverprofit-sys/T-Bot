# Frequently asked questions

## Can I download T-Bot?

No. The private T-Bot application is not released. A [standalone educational lab](../examples/review_gate/README.md) and [source-derived validation toolkit](../components/validation/README.md) are available to evaluate separately. Neither is the operational application.

## What is its current status?

Private development and security qualification; no live-money execution is authorised. No trading performance is claimed. See [development status](DEVELOPMENT_STATUS.md).

## Has it been independently audited?

No independent certification is claimed. The private-system [testing examples](TESTING.md) are fictional and unexecuted. The standalone lab has its own demonstration results. The validation toolkit has [owner-run, AI-assisted 57/57 original and reproduction test results](../components/validation/TEST_RESULTS.md), not private-application qualification results. AI-assisted review is not independent human assurance.

## Is AI picking trades?

Not in the intended design. Trading eligibility and risk decisions use explicit rules over validated inputs and policy state. AI assists development and review, not trade selection or execution authority. This design boundary still requires implementation-level evidence. See [architecture](ARCHITECTURE.md).

## Does security-focused mean the application is secure?

No. Security is an engineering objective. AI-assisted review can miss defects, and no independent human audit or system-wide qualification is claimed. See [development status](DEVELOPMENT_STATUS.md).

## How can I help?

Choose a [starter task](../community/START_HERE.md) or [code-review assignment](../components/validation/REVIEWERS.md) and read [CONTRIBUTING.md](../CONTRIBUTING.md) and the [central community guide](https://github.com/processoverprofit-sys/Processoverprofit-sys/blob/main/docs/COMMUNITY.md). Direct Discord applications remain pending. Do not request private access through public issues or pull requests.

[Return to overview](../README.md)
