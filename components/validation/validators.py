"""Standalone validation utilities."""

import re


def digest(v):
    return type(v) is str and re.fullmatch(r"[0-9a-f]{64}", v) is not None


def alias(v, prefix):
    return (
        type(v) is str
        and type(prefix) is str
        and re.fullmatch(
            re.escape(prefix) + r"[A-Z0-9_-]{1,40}", v
        ) is not None
    )


def reason_code(v):
    return type(v) is str and re.fullmatch(r"[A-Z0-9_]{1,100}", v) is not None


def _available(observed, available, decision):
    return (
        type(observed) is int
        and type(available) is int
        and type(decision) is int
        and 0 <= observed <= available <= decision
    )
