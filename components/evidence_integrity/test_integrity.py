import hashlib
import importlib.util
import sys
from pathlib import Path

path = Path(__file__).resolve().with_name("integrity.py")

expected = (
    '0e5276893cee5539a60357946aaac604e81a247c82413c3be492ab3781bacbc5'
)

if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
    raise SystemExit("SOURCE_HASH_MISMATCH")

print("SOURCE_IDENTITY=PASS")
print("PYTHON_VERSION=" + sys.version.split()[0])

# Load only the authorized standalone candidate.

spec = importlib.util.spec_from_file_location(
    "integrity", path
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

Error = module.EvidenceError
sha = module.sha256_bytes
verify = module.read_verified_json

BASE = b'{"mode":"DEMO","version":1,"payload":42}'
FIELDS = {"mode", "version", "payload"}

def digest(raw):
    return hashlib.sha256(raw).hexdigest()

def read(raw=BASE, **changes):
    settings = {
        "expected_digest": digest(raw),
        "fields": FIELDS,
        "expected_mode": "DEMO",
        "expected_version": 1,
        "max_bytes": 8192
    }

    settings.update(changes)

    return verify(raw, **settings)

def document(value):
    return (
        b'{"mode":"DEMO","version":1,"payload":'
        + value + b'}'
    )

def accepted(raw):
    obj, observed = read(raw)
    return (
        type(obj) is dict
        and observed == digest(raw)
    )

def payload(raw):
    return read(raw)[0]["payload"]

passed = 0
failed = 0
seen = set()

def case(number, action, *, value=True, error=None):
    global passed, failed

    if number in seen:
        raise SystemExit("DUPLICATE_TEST_ID")

    seen.add(number)
    name = f"T{number:02d}"

    try:
        actual = action()

        ok = (
            error is None
            and type(actual) is type(value)
            and actual == value
        )

        outcome = "EXPECTED_VALUE" if ok else "UNEXPECTED_VALUE"

    except Exception as exc:
        ok = (
            error is not None
            and type(exc) is Error
            and str(exc) == error
        )

        outcome = (
            "EXPECTED_REJECTION" if ok
            else "UNEXPECTED_EXCEPTION_" + type(exc).__name__
        )

    if ok:
        passed += 1
    else:
        failed += 1

    print(f"{name} {'PASS' if ok else 'FAIL'} {outcome}")

class BytesSubclass(bytes):
    pass

class IntSubclass(int):
    pass

class StrSubclass(str):
    pass

print("\n=== ORIGINAL TEST SPECIFICATIONS ===")

case(1, lambda: sha(b"abc", max_bytes=3),
     value="ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad")

case(2, lambda: sha(b"", max_bytes=1),
     error="INPUT_BYTE_LIMIT")

case(3, lambda: sha("abc", max_bytes=3),
     error="INPUT_BYTE_LIMIT")

case(4, lambda: sha(bytearray(b"abc"), max_bytes=3),
     error="INPUT_BYTE_LIMIT")

case(5, lambda: sha(BytesSubclass(b"abc"), max_bytes=3),
     error="INPUT_BYTE_LIMIT")

case(6, lambda: sha(b"abcd", max_bytes=4),
     value=digest(b"abcd"))

case(7, lambda: sha(b"abcd", max_bytes=3),
     error="INPUT_BYTE_LIMIT")

case(8, lambda: sha(b"a", max_bytes=True),
     error="INVALID_BYTE_LIMIT")

case(9, lambda: sha(b"a", max_bytes=0),
     error="INVALID_BYTE_LIMIT")

case(10, lambda: sha(b"a", max_bytes=-1),
     error="INVALID_BYTE_LIMIT")

case(11, lambda: read(),
     value=(
         {"mode":"DEMO", "version":1, "payload":42},
         digest(BASE)
     ))

case(12, lambda: read(expected_digest="0"*64),
     error="DIGEST_MISMATCH")

case(13, lambda: read(expected_digest="A"*64),
     error="INVALID_EXPECTED_DIGEST")

case(14, lambda: read(expected_digest="a"*63),
     error="INVALID_EXPECTED_DIGEST")

case(15, lambda: read(expected_digest=123),
     error="INVALID_EXPECTED_DIGEST")

case(16, lambda: read(
    b'{"mode":"DEMO","version":1,"payload":1,"payload":2}'
), error="DUPLICATE_JSON_KEY")

case(17, lambda: read(document(b'{"x":1,"x":2}')),
     error="DUPLICATE_JSON_KEY")

case(18, lambda: read(document(b"1.5")),
     error="INVALID_JSON_NUMBER")

case(19, lambda: read(document(b"1e3")),
     error="INVALID_JSON_NUMBER")

case(20, lambda: read(document(b"NaN")),
     error="INVALID_JSON_NUMBER")

case(21, lambda: read(document(b"Infinity")),
     error="INVALID_JSON_NUMBER")

case(22, lambda: read(document(b"-Infinity")),
     error="INVALID_JSON_NUMBER")

case(23, lambda: read(b"\xff"),
     error="MALFORMED_JSON")

case(24, lambda: read(BASE[:-1]),
     error="MALFORMED_JSON")

case(25, lambda: read(BASE + b"x"),
     error="MALFORMED_JSON")

case(26, lambda: read(b"[]"),
     error="SCHEMA_MISMATCH")

case(27, lambda: read(b'{"mode":"DEMO","version":1}'),
     error="SCHEMA_MISMATCH")

case(28, lambda: read(
    b'{"mode":"DEMO","version":1,"payload":42,"extra":0}'
), error="SCHEMA_MISMATCH")

case(29, lambda: read(BASE.replace(b"DEMO", b"OTHER")),
     error="MODE_OR_VERSION_MISMATCH")

case(30, lambda: read(BASE.replace(b'"version":1', b'"version":2')),
     error="MODE_OR_VERSION_MISMATCH")

case(31, lambda: read(BASE.replace(b'"version":1', b'"version":true')),
     error="MODE_OR_VERSION_MISMATCH")

case(32, lambda: read(expected_version=True),
     error="INVALID_EXPECTED_DOCUMENT_SETTINGS")

case(33, lambda: read(fields=["mode", "version", "payload"]),
     error="INVALID_EXPECTED_FIELDS")

case(34, lambda: payload(document(b'{"values":[1,2,3]}')),
     value={"values":[1,2,3]})

case(35, lambda: payload(document('"café"'.encode("utf-8"))),
     value="café")

case(36, lambda: read(
    BASE + b" ", expected_digest=digest(BASE)
), error="DIGEST_MISMATCH")

case(37, lambda: accepted(BASE + b" "))

print("\n=== ADDITIONAL BOUNDARY TESTS ===")

case(38, lambda: sha(b"a", max_bytes=1.5),
     error="INVALID_BYTE_LIMIT")

case(39, lambda: sha(b"a", max_bytes=IntSubclass(1)),
     error="INVALID_BYTE_LIMIT")

case(40, lambda: sha(memoryview(b"a"), max_bytes=1),
     error="INPUT_BYTE_LIMIT")

case(41, lambda: read(
    expected_digest=StrSubclass(digest(BASE))
), error="INVALID_EXPECTED_DIGEST")

case(42, lambda: read(fields=frozenset(FIELDS)),
     error="INVALID_EXPECTED_FIELDS")

case(43, lambda: read(fields=FIELDS | {1}),
     error="INVALID_EXPECTED_FIELDS")

case(44, lambda: read(fields={"version","payload"}),
     error="INVALID_EXPECTED_FIELDS")

case(45, lambda: read(expected_mode=123),
     error="INVALID_EXPECTED_DOCUMENT_SETTINGS")

case(46, lambda: read(expected_mode=StrSubclass("DEMO")),
     error="INVALID_EXPECTED_DOCUMENT_SETTINGS")

case(47, lambda: read(expected_version=IntSubclass(1)),
     error="INVALID_EXPECTED_DOCUMENT_SETTINGS")

case(48, lambda: read(BASE.replace(b'"DEMO"', b'42')),
     error="MODE_OR_VERSION_MISMATCH")

case(49, lambda: read(BASE.replace(b'"version":1', b'"version":1.0')),
     error="INVALID_JSON_NUMBER")

case(50, lambda: read(
    document(br'{"x":1,"\u0078":2}')
), error="DUPLICATE_JSON_KEY")

case(51, lambda: read(document(b'"a\x01b"')),
     error="MALFORMED_JSON")

case(52, lambda: read(b"\xef\xbb\xbf" + BASE),
     error="MALFORMED_JSON")

# Revision A requires rejection of unpaired surrogates.

case(53, lambda: read(document(br'"\ud800"')),
     error="INVALID_UNICODE_SURROGATE")

case(54, lambda: payload(document(br'"\ud83d\ude00"')),
     value="\U0001f600")

case(55, lambda: read(document(b'"\xed\xa0\x80"')),
     error="MALFORMED_JSON")

# Explicit interpreter settings for reproducible integer tests.
# These changes affect only this isolated process.

sys.set_int_max_str_digits(640)

case(56, lambda: type(payload(document(b"1"*640))) is int)

case(57, lambda: read(document(b"1"*641)),
     error="MALFORMED_JSON")

sys.setrecursionlimit(1000)

case(58, lambda: read(
    document(b"["*2000 + b"0" + b"]"*2000)
), error="JSON_DEPTH_LIMIT")

case(59, lambda: read(
    b"{", expected_digest="0"*64
), error="DIGEST_MISMATCH")

case(60, lambda: payload(document(b'[true,false,null]')),
     value=[True, False, None])


print("\n=== REVISION A CORRECTIVE REGRESSIONS ===")

case(61, lambda: read(max_depth=1),
     value=(
         {"mode":"DEMO","version":1,"payload":42},
         digest(BASE)
     ))

case(62, lambda: read(
    document(b"[]"), max_depth=1
), error="JSON_DEPTH_LIMIT")

case(63, lambda: read(
    document(b'{"x":1}'), max_depth=2
)[0]["payload"], value={"x":1})

case(64, lambda: read(
    document(b'{"x":[]}'), max_depth=2
), error="JSON_DEPTH_LIMIT")

case(65, lambda: read(max_depth=True),
     error="INVALID_DEPTH_LIMIT")

case(66, lambda: read(max_depth=0),
     error="INVALID_DEPTH_LIMIT")

case(67, lambda: read(max_depth=129),
     error="INVALID_DEPTH_LIMIT")

case(68, lambda: read(max_depth=2.5),
     error="INVALID_DEPTH_LIMIT")

case(69, lambda: read(max_depth=IntSubclass(2)),
     error="INVALID_DEPTH_LIMIT")

case(70, lambda: read(
    document(b'"[{}]"'), max_depth=1
)[0]["payload"], value="[{}]")

case(71, lambda: read(
    document(br'"a\"[{}]b"'), max_depth=1
)[0]["payload"], value='a"[{}]b')

case(72, lambda: read(
    document(br'"end\\"'), max_depth=1
)[0]["payload"], value="end\\")

case(73, lambda: read(document(b"[0}")),
     error="MALFORMED_JSON")

case(74, lambda: read(document(b'"unterminated')),
     error="MALFORMED_JSON")

case(75, lambda: read(
    document(br'{"\udc00":1}')
), error="INVALID_UNICODE_SURROGATE")

case(76, lambda: read(
    document(br'["\ud800"]')
), error="INVALID_UNICODE_SURROGATE")

case(77, lambda: payload(
    document(br'{"\ud83d\ude00":1}')
), value={"\U0001f600":1})

case(78, lambda: read(
    BASE.replace(b'"DEMO"', br'"\ud800"')
), error="INVALID_UNICODE_SURROGATE")

deep = document(b"["*2000 + b"0" + b"]"*2000)

case(79, lambda: read(
    deep, expected_digest="0"*64
), error="DIGEST_MISMATCH")

case(80, lambda: read(document(b'"\xff"')),
     error="MALFORMED_JSON")

case(81, lambda: read(
    deep, max_bytes=len(deep)-1
), error="INPUT_BYTE_LIMIT")

depth128 = document(b"["*127 + b"0" + b"]"*127)
depth129 = document(b"["*128 + b"0" + b"]"*128)

def verify_maximum_depth():
    obj, observed = read(depth128, max_depth=128)

    value = obj["payload"]

    for _ in range(127):
        if type(value) is not list or len(value) != 1:
            return False
        value = value[0]

    return (
        type(value) is int
        and value == 0
        and observed == digest(depth128)
    )

case(82, verify_maximum_depth)

case(83, lambda: read(depth129, max_depth=128),
     error="JSON_DEPTH_LIMIT")

case(84, lambda: read(document(b"[1,]")),
     error="MALFORMED_JSON")


print("\n=== STANDALONE TEST RESULTS ===")
print("TESTS_OBSERVED=" + str(len(seen)))
print("PASS=" + str(passed))
print("FAIL=" + str(failed))
print("UNICODE_SURROGATE_TEST=REJECTION_REQUIRED")
print("INTEGER_DIGIT_LIMIT=640")
print("RECURSION_LIMIT=1000")

if seen != set(range(1, 85)):
    raise SystemExit("TEST_COVERAGE_INCOMPLETE")

print(
    "STANDALONE_TEST_RESULT="
    + ("PASS" if failed == 0 else "FAIL")
)

raise SystemExit(0 if failed == 0 else 1)
