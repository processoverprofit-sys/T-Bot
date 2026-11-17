# Observed results — standalone educational lab only

17 November 2026. Assistant-run evaluation of two newly authored standalone Python files in a separate working sandbox, Python 3.13.5, standard-library unittest. No private T-Bot files, credentials, wallets, network services or actual executor were involved.

| Test | Observed result |
| --- | --- |
| Allowed verdict with approval | PASS |
| Denied verdict | PASS |
| Invalid verdict | PASS |
| Allowed verdict without approval | PASS |
| Non-boolean approval | PASS |
| Repeated input | PASS |
| Unknown verdict | PASS |

Observed unittest summary: Ran 7 tests; OK.

```json
{"input": {"approved": true, "verdict": "DENY"}, "output": {"decision": "REJECT", "dummy_action_count": 0}}
{"input": {"approved": true, "verdict": "UNKNOWN"}, "output": {"decision": "REJECT", "dummy_action_count": 0}}
{"input": {"approved": false, "verdict": "ALLOW"}, "output": {"decision": "REJECT", "dummy_action_count": 0}}
{"input": {"approved": true, "verdict": "ALLOW"}, "output": {"decision": "ALLOW", "dummy_action_count": 1}}
```

Git blob identities of evaluated files:
- decision_gate.py: d770d9da495c68390eaed1954c762a17b8062c01
- test_decision_gate.py: 973e2fa86e0deeb579d92d317166b3f5ffe10887

The counter is computed by the same function, not independently measured, and no executor exists here. These are not genuine T-Bot risk-veto observations, qualification evidence or performance results. AI assisted both code and test creation; no independent human review is claimed. Genuine T-Bot risk-veto evidence remains outstanding and requires separate qualification, evidence and disclosure approval. [Reproduction instructions](README.md).
