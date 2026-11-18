# Contributing and Public Feedback

This repository is a **public documentation and selective standalone-code collaboration space**, not a distribution of the private T-Bot application.

## Public component, lab and documentation contributions

Public pull requests proposing **non-sensitive documentation corrections or changes confined to the standalone public lab or approved standalone toolkit** may be reviewed at the maintainer's discretion. [Public Issues](https://github.com/processoverprofit-sys/T-Bot/issues) are enabled for non-sensitive engineering tasks, documentation corrections and general feedback. Issues may be used to propose public-safe design and test ideas; code contributions remain confined to the approved standalone lab and the [validation](components/validation/README.md) and [evidence integrity](components/evidence_integrity/README.md) toolkits; any further component requires separate publication approval. No private repository, private application or development-system access is granted to contributors.

Please limit submissions to general, non-sensitive corrections or engineering suggestions. Only original, non-sensitive code and tests within the lab or approved standalone toolkit may be proposed. Do not submit operational source code, credentials, token values, wallet details, private paths, internal logs, exploit instructions, private test evidence, operational configuration or financial-performance claims.

## Developer code review

Start with [REVIEWERS.md](components/validation/REVIEWERS.md), the [implementation](components/validation/validators.py), [portable tests](components/validation/test_validators.py) and [observed results](components/validation/TEST_RESULTS.md). Coordinate public-safe findings through [ENG-02](https://github.com/processoverprofit-sys/T-Bot/issues/8). The seven review assignments cover types, formatting, regex behaviour, ordering, test coverage and maintainability. Distinguish observed results from hypotheses; do not post sensitive findings publicly. Community review is not formal independent qualification.

For the [Evidence Integrity Toolkit V1 (Revision A)](components/evidence_integrity/README.md), choose [EI-01–EI-08](components/evidence_integrity/REVIEWERS.md), inspect the [implementation](components/evidence_integrity/integrity.py), reproduce the [84 tests](components/evidence_integrity/test_integrity.py), and challenge the [observed results and limitations](components/evidence_integrity/TEST_RESULTS.md). Coordinate public-safe findings via [ENG-01](https://github.com/processoverprofit-sys/T-Bot/issues/7). The component does not implement complete manifest verification or producer authentication.

## Security findings

**Do not submit vulnerabilities through public issues or pull requests.** For a security concern with this public repository, use the private reporting route described in [SECURITY.md](SECURITY.md). Do not independently test any private project or infrastructure.

## Rights and expectations

Submit only material you have the right to share publicly. Contributions to the standalone lab must be compatible with its [MIT licence](examples/review_gate/LICENSE). Contributions to the validation toolkit must be compatible with its separate [MIT licence](components/validation/LICENSE). Contributions to the evidence integrity toolkit must be compatible with its separate [MIT licence](components/evidence_integrity/LICENSE). Each licence applies only within its own directory; the [rights notice](LICENSE-NOTICE.md) describes the remaining material. Feedback does not establish employment, contractual obligations, unrestricted access, a contributor licence agreement or an obligation to accept a contribution. Material posted publicly may be indexed or copied even if later removed.

## Before submitting

Read the [publication checklist](docs/PUBLICATION_CHECKLIST.md) and [community conduct](CODE_OF_CONDUCT.md). Choose a [starter task](community/START_HERE.md). Use the pull request template for non-sensitive lab or toolkit changes or documentation corrections. Include test outcomes and limitations.
