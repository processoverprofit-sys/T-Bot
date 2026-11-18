# Candidate V1 changes

## Preserved

- digest
- reason_code

## Proposed corrections

### alias

Require the prefix to be a string and treat it as literal
text using re.escape.

This intentionally changes behaviour for prefixes previously
interpreted as regular expressions.

Empty string prefixes remain permitted.

### _available

Require decision to be an exact integer, matching the existing
type requirements for observed and available.

Boolean, floating-point and other non-integer decision values
are rejected.

No private source files were changed.
These changes have not undergone runtime testing.

## Release preparation

The preceding testing status describes the original source-only preparation stage. See TEST_RESULTS.md for subsequent observed results.
