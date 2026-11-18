# Changelog

## V1 — Revision A (standalone release)

- Retained byte hashing, strict JSON parsing and caller-defined top-level document checks.
- Added explicit lexical container-depth validation (default 64, allowed 1–128).
- Added rejection of decoded unpaired Unicode surrogates in keys and values.
- Clarified parser limits, validation precedence and integrity versus authenticity.
- Expanded the original 60-case suite to 84 cases. T53 and T58 have prospectively corrected expectations.
- Preserved the historical V1 result: 59 passed, one failed (T58).
- Revision A: 84 passed, zero failed. The same 84 cases were reproduced with a portable harness.
- Public harness portability changes: resolve the source beside the harness, remove the Linux-specific isolation check from the harness itself, and use a generic source-identity marker. No test case or helper changed.

This source-derived standalone adaptation is not a publication of the complete private application.
