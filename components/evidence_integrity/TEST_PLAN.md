# Fictional test specification

Fictional test specification; see TEST_RESULTS.md for observations.

All inputs are invented and unrelated to operational T-Bot data.

Base document:
{"mode":"DEMO","version":1,"payload":42}

Use fields {"mode","version","payload"}.
Use expected_mode="DEMO", expected_version=1.
Use a sufficient caller-defined max_bytes.
Use independently computed expected SHA-256 digests.

| ID | Input / condition | Expected |
|---|---|---|
| T01 | Bytes abc | Known SHA-256 digest |
| T02 | Empty bytes | INPUT_BYTE_LIMIT |
| T03 | String input | INPUT_BYTE_LIMIT |
| T04 | Bytearray input | INPUT_BYTE_LIMIT |
| T05 | Bytes subclass | INPUT_BYTE_LIMIT |
| T06 | Size exactly at limit | Accept |
| T07 | Size exceeds limit | INPUT_BYTE_LIMIT |
| T08 | Boolean byte limit | INVALID_BYTE_LIMIT |
| T09 | Zero byte limit | INVALID_BYTE_LIMIT |
| T10 | Negative byte limit | INVALID_BYTE_LIMIT |
| T11 | Valid base document | Object and digest |
| T12 | Incorrect expected digest | DIGEST_MISMATCH |
| T13 | Uppercase expected digest | INVALID_EXPECTED_DIGEST |
| T14 | Incorrect digest length | INVALID_EXPECTED_DIGEST |
| T15 | Non-string expected digest | INVALID_EXPECTED_DIGEST |
| T16 | Duplicate top-level key | DUPLICATE_JSON_KEY |
| T17 | Duplicate nested key | DUPLICATE_JSON_KEY |
| T18 | Decimal number | INVALID_JSON_NUMBER |
| T19 | Exponent-form number | INVALID_JSON_NUMBER |
| T20 | NaN | INVALID_JSON_NUMBER |
| T21 | Infinity | INVALID_JSON_NUMBER |
| T22 | Negative Infinity | INVALID_JSON_NUMBER |
| T23 | Invalid UTF-8 | MALFORMED_JSON |
| T24 | Truncated JSON | MALFORMED_JSON |
| T25 | Trailing non-whitespace data | MALFORMED_JSON |
| T26 | Array instead of object | SCHEMA_MISMATCH |
| T27 | Missing required field | SCHEMA_MISMATCH |
| T28 | Unexpected additional field | SCHEMA_MISMATCH |
| T29 | Incorrect document mode | MODE_OR_VERSION_MISMATCH |
| T30 | Incorrect document version | MODE_OR_VERSION_MISMATCH |
| T31 | Boolean document version | MODE_OR_VERSION_MISMATCH |
| T32 | Boolean expected version | INVALID_EXPECTED_DOCUMENT_SETTINGS |
| T33 | Invalid expected field set | INVALID_EXPECTED_FIELDS |
| T34 | Valid nested integer data | Accept |
| T35 | Valid UTF-8 Unicode payload | Accept |
| T36 | Different whitespace, original digest | DIGEST_MISMATCH |
| T37 | Same data, newly matching digest | Accept |

For parsing and schema rejection cases, supply a matching
digest for the malformed or modified bytes so that the
specific parsing or validation branch is reached.

For T01, the known SHA-256 of abc is:
ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad

Historical V1 review topics (see the Revision A supplement):
- Interpreter-dependent integer digit limits.
- Recursion limits and deeply nested documents.
- Escaped unpaired Unicode surrogates.
- Caller-controlled resource limits.
- Digest provenance and trust assumptions.

The historical V1 planning text preceded the original run; see TEST_RESULTS.md.
All expectations remain subject to independent review.


# Revision A regression supplement

Fictional test specification; see TEST_RESULTS.md for observations.

T01–T37 retain their original expectations.
The following cases define the additional regression scope.

| ID | Condition | Expected |
|---|---|---|
| T38 | Float byte limit | INVALID_BYTE_LIMIT |
| T39 | Integer-subclass byte limit | INVALID_BYTE_LIMIT |
| T40 | Memoryview input | INPUT_BYTE_LIMIT |
| T41 | String-subclass digest | INVALID_EXPECTED_DIGEST |
| T42 | Frozenset fields | INVALID_EXPECTED_FIELDS |
| T43 | Non-string field name | INVALID_EXPECTED_FIELDS |
| T44 | Missing mode in expected fields | INVALID_EXPECTED_FIELDS |
| T45 | Numeric expected mode | INVALID_EXPECTED_DOCUMENT_SETTINGS |
| T46 | String-subclass expected mode | INVALID_EXPECTED_DOCUMENT_SETTINGS |
| T47 | Integer-subclass expected version | INVALID_EXPECTED_DOCUMENT_SETTINGS |
| T48 | Numeric document mode | MODE_OR_VERSION_MISMATCH |
| T49 | Floating-point document version | INVALID_JSON_NUMBER |
| T50 | Duplicate key using Unicode escape | DUPLICATE_JSON_KEY |
| T51 | Unescaped control character | MALFORMED_JSON |
| T52 | UTF-8 BOM | MALFORMED_JSON |
| T53 | Escaped unpaired high surrogate | INVALID_UNICODE_SURROGATE |
| T54 | Valid escaped surrogate pair | Accept supplementary character |
| T55 | Invalid UTF-8 surrogate bytes | MALFORMED_JSON |
| T56 | Integer containing 640 digits | Accept at configured limit |
| T57 | Integer containing 641 digits | MALFORMED_JSON |
| T58 | Document containing 2000 nested arrays | JSON_DEPTH_LIMIT |
| T59 | Malformed JSON with mismatched digest | DIGEST_MISMATCH |
| T60 | Nested booleans and null | Accept |
| T61 | Base document at max_depth=1 | Accept |
| T62 | Root object containing array at max_depth=1 | JSON_DEPTH_LIMIT |
| T63 | Root plus nested object at max_depth=2 | Accept |
| T64 | Root plus object plus array at max_depth=2 | JSON_DEPTH_LIMIT |
| T65 | Boolean nesting limit | INVALID_DEPTH_LIMIT |
| T66 | Zero nesting limit | INVALID_DEPTH_LIMIT |
| T67 | Nesting limit of 129 | INVALID_DEPTH_LIMIT |
| T68 | Floating-point nesting limit | INVALID_DEPTH_LIMIT |
| T69 | Integer-subclass nesting limit | INVALID_DEPTH_LIMIT |
| T70 | Brackets inside string at max_depth=1 | Accept |
| T71 | Escaped quote followed by brackets inside string | Accept |
| T72 | String ending with decoded backslash | Accept |
| T73 | Mismatched closing container bracket | MALFORMED_JSON |
| T74 | Unterminated JSON string | MALFORMED_JSON |
| T75 | Escaped unpaired low surrogate in nested key | INVALID_UNICODE_SURROGATE |
| T76 | Unpaired high surrogate in nested list value | INVALID_UNICODE_SURROGATE |
| T77 | Valid paired surrogate escape in nested key | Accept |
| T78 | Unpaired surrogate in document mode | INVALID_UNICODE_SURROGATE |
| T79 | Excessive depth with incorrect expected digest | DIGEST_MISMATCH |
| T80 | Invalid UTF-8 with matching digest | MALFORMED_JSON |
| T81 | Excessive depth and insufficient byte limit | INPUT_BYTE_LIMIT |
| T82 | Root plus 127 nested arrays at max_depth=128 | Accept |
| T83 | Root plus 128 nested arrays at max_depth=128 | JSON_DEPTH_LIMIT |
| T84 | Trailing comma within permitted depth | MALFORMED_JSON |

T53 and T58 supersede the historical V1 test expectations
prospectively. The original test results remain unchanged.

T56 and T57 require an isolated process with an integer
digit limit of 640.

T58, T82 and T83 require sufficient input byte limits.
For T82, use the intended Python 3.12.3 regression environment
with recursion limit 1000 and record the actual result.

Except where digest mismatch is explicitly tested, calculate
the expected digest independently from the fictional input.

Revision A and its portable harness were each observed to pass all 84 cases; see TEST_RESULTS.md.
