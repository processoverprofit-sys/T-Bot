"""Source-derived byte integrity and strict JSON utilities, Revision A."""

import hashlib
import json
import re


class EvidenceError(ValueError):
    """The supplied evidence failed a verification requirement."""


def _require(condition, reason):
    if not condition:
        raise EvidenceError(reason)


def sha256_bytes(raw, *, max_bytes):
    """Return the SHA-256 hex digest of bounded, nonempty bytes."""
    _require(
        type(max_bytes) is int and max_bytes > 0,
        "INVALID_BYTE_LIMIT"
    )
    _require(
        type(raw) is bytes and 0 < len(raw) <= max_bytes,
        "INPUT_BYTE_LIMIT"
    )
    return hashlib.sha256(raw).hexdigest()


def _object(pairs):
    result = {}
    for key, value in pairs:
        _require(key not in result, "DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def _reject_number(_value):
    raise EvidenceError("INVALID_JSON_NUMBER")


def _fields(obj, fields):
    _require(
        type(obj) is dict and set(obj) == fields,
        "SCHEMA_MISMATCH"
    )



def _check_depth(text, max_depth):
    """Bound container nesting before calling the JSON parser."""
    stack = []
    in_string = False
    escaped = False

    for ch in text:
        if in_string:
            if escaped:
                escaped = False
            elif ch == "\\":
                escaped = True
            elif ch == '"':
                in_string = False
            continue

        if ch == '"':
            in_string = True
        elif ch in "[{":
            stack.append(ch)
            _require(
                len(stack) <= max_depth,
                "JSON_DEPTH_LIMIT"
            )
        elif ch in "]}":
            expected = "[" if ch == "]" else "{"
            _require(
                bool(stack) and stack.pop() == expected,
                "MALFORMED_JSON"
            )

    _require(
        not in_string and not stack,
        "MALFORMED_JSON"
    )


def _check_unicode(obj):
    """Reject unpaired surrogates in decoded keys and values."""
    pending = [obj]

    while pending:
        value = pending.pop()

        if type(value) is str:
            _require(
                not any(
                    0xD800 <= ord(ch) <= 0xDFFF
                    for ch in value
                ),
                "INVALID_UNICODE_SURROGATE"
            )
        elif type(value) is dict:
            pending.extend(value.keys())
            pending.extend(value.values())
        elif type(value) is list:
            pending.extend(value)


def read_verified_json(
    raw, expected_digest, fields, *,
    expected_mode, expected_version, max_bytes,
    max_depth=64
):
    """Verify caller-supplied identity and parse a strict JSON object.

    The expected digest must originate outside the supplied document.
    A matching digest does not authenticate its producer.
    """
    _require(
        type(fields) is set
        and all(type(key) is str for key in fields)
        and {"mode", "version"}.issubset(fields),
        "INVALID_EXPECTED_FIELDS"
    )
    _require(
        type(expected_mode) is str
        and type(expected_version) is int,
        "INVALID_EXPECTED_DOCUMENT_SETTINGS"
    )
    _require(
        type(max_depth) is int
        and 1 <= max_depth <= 128,
        "INVALID_DEPTH_LIMIT"
    )
    _require(
        type(expected_digest) is str
        and re.fullmatch(r"[0-9a-f]{64}", expected_digest)
        is not None,
        "INVALID_EXPECTED_DIGEST"
    )

    digest = sha256_bytes(raw, max_bytes=max_bytes)
    _require(digest == expected_digest, "DIGEST_MISMATCH")

    try:
        text = raw.decode("utf-8")
        _check_depth(text, max_depth)
        obj = json.loads(
            text,
            object_pairs_hook=_object,
            parse_float=_reject_number,
            parse_constant=_reject_number
        )
    except EvidenceError:
        raise
    except (ValueError, UnicodeError, RecursionError):
        raise EvidenceError("MALFORMED_JSON") from None

    _check_unicode(obj)
    _fields(obj, fields)

    _require(
        obj["mode"] == expected_mode
        and type(obj["version"]) is int
        and obj["version"] == expected_version,
        "MODE_OR_VERSION_MISMATCH"
    )

    return obj, digest
