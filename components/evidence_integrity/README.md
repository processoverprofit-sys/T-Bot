# T-Bot Evidence Integrity Toolkit V1 — Revision A

Standalone release V1 (Revision A).

A standalone source-derived byte-integrity and strict JSON
verification component.

Features:
- SHA-256 hashing of bounded nonempty byte inputs.
- Verification against an independently supplied digest.
- Strict UTF-8 decoding.
- Rejection of duplicate JSON keys.
- Rejection of floating-point and non-finite JSON numbers.
- Explicit JSON container nesting limits.
- Rejection of unpaired Unicode surrogates in keys and values.
- Exact top-level fields, mode and version checks.

## Nesting contract

max_depth defaults to 64.

It must be an exact integer from 1 through 128.
Booleans, subclasses and other types are rejected.

The root object or array counts as depth 1.
Only JSON containers outside strings contribute to depth.
A valid document exceeding the limit is rejected with
JSON_DEPTH_LIMIT before JSON parsing.

The lexical check is not a complete JSON grammar validator.
The standard-library parser still validates JSON syntax.

## Unicode contract

Unpaired surrogate code points in decoded strings are rejected
with INVALID_UNICODE_SURROGATE.

Valid paired surrogate escapes may decode to a supplementary
Unicode character and remain acceptable.

No Unicode normalization or confusable-character detection
is performed.

## Resource and error boundaries

Caller-provided max_bytes bounds input size, not peak memory
or total CPU consumption.

max_depth bounds structural nesting. It does not guarantee
successful parsing at every permitted depth on every
interpreter configuration.

Python integer-digit and recursion limits still apply.
Parser ValueError, UnicodeError and RecursionError become
MALFORMED_JSON unless already an EvidenceError.

MemoryError and other process-resource failures are not
claimed to be normalized or safely recoverable.

Validation order:
1. Expected fields and document settings.
2. Expected nesting-limit setting.
3. Expected digest format.
4. Byte-limit and input-type validation.
5. Digest comparison.
6. UTF-8 decoding and lexical nesting check.
7. JSON parsing and parser-specific rejection.
8. Unicode scalar-value checks.
9. Top-level field, mode and version checks.

A malformed document can encounter the depth limit before
its full syntax has been evaluated.

Digest equality does not establish producer authenticity,
truth, freshness or operational authorization.

This component does not provide complete manifest verification
or nested semantic schema validation.

## Run the fictional tests

Python 3.12.3 was used for the observed results. No third-party
Python packages are needed. From the extracted component directory:

```sh
sha256sum -c MANIFEST.sha256
python3 -I -S -B test_integrity.py
```

The harness pins the exact release source digest and exits nonzero
on test failure. It changes integer and recursion limits only within
its own process. A normal invocation does not establish network isolation;
the owner used a separate network-isolated runner for recorded tests.

See TEST_RESULTS.md for observed results and limitations, TEST_PLAN.md
for the fictional cases, and REVIEWERS.md for review assignments.

MIT applies only to this standalone component and its included files.
No licence to the private application or unrelated repository content
is granted by this package.
