# Revision A developer review assignments

EI-01 — SHA-256 accuracy and input contract.
EI-02 — Strict byte, digest and argument validation.
EI-03 — Duplicate keys and invalid number rejection.
EI-04 — UTF-8, Unicode scalar values and surrogate pairs.
EI-05 — Digest consistency and error precedence.
EI-06 — Exact fields, mode and version contract.
EI-07 — Lexical nesting scanner, escaping and boundaries.
EI-08 — Resource limitations, exception handling and test quality.

Specific corrective review questions:
- Can escaped quotes or backslashes confuse nesting counting?
- Are all decoded strings examined, including dictionary keys?
- Are valid supplementary Unicode characters preserved?
- Does the advertised nesting contract match the implementation?
- Are interpreter-dependent limits accurately documented?
- Are malformed or oversized inputs rejected as specified?

Report:
Reviewer, revision, function and line, finding,
expected behaviour, observed behaviour or static reasoning,
proposed correction, regression test and limitations.

Standalone component review only.
No private application access is requested.
