# Proposed offline test plan

Status: NOT EXECUTED

## Digest validation

- Accept exactly 64 lowercase hexadecimal characters.
- Reject incorrect lengths, uppercase letters and non-strings.

## Alias validation

- Accept a literal prefix and valid suffix.
- Exercise suffix length boundaries of 1 and 40.
- Reject invalid suffix characters.
- Verify literal handling of regex characters in the prefix.
- Reject non-string prefixes and values.
- Preserve documented empty-prefix behaviour.

## Reason-code validation

- Exercise permitted characters and length boundaries.
- Reject lowercase, invalid characters and non-string values.

## Ordered integer validation

- Exercise equality and valid increasing values.
- Reject negative and incorrectly ordered values.
- Reject strings, floats, booleans and other non-integers
  in each argument position.

All proposed cases use fictional inputs.
No test outcomes are claimed.
