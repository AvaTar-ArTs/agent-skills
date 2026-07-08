"""Secret detection and redaction (R7)."""
import re

_PATTERNS = [
    re.compile(r'sk-proj-[A-Za-z0-9_-]{10,}'),
    re.compile(r'sk-ant-[A-Za-z0-9_-]{10,}'),
    re.compile(r'\bsk-[A-Za-z0-9_-]{20,}'),
    re.compile(r'\br8_[A-Za-z0-9]{10,}'),
    re.compile(r'Bearer\s+[A-Za-z0-9_\-\.]{20,}'),
    re.compile(r'api[_-]?key\s*[:=]\s*["\']?[A-Za-z0-9_\-]{16,}', re.IGNORECASE),
    re.compile(r'Authorization\s*:\s*[A-Za-z0-9 _\-\.]{20,}', re.IGNORECASE),
    re.compile(r'__client=[A-Za-z0-9_%]+'),
    re.compile(r'session=[A-Za-z0-9_%]{20,}'),
    re.compile(r'-----BEGIN (?:RSA |EC )?PRIVATE KEY-----'),
]


def redact(text: str) -> str:
    """Replace secret-looking strings with [REDACTED]. Returns cleaned text."""
    for pattern in _PATTERNS:
        text = pattern.sub('[REDACTED]', text)
    return text


def assert_no_secrets(text: str) -> None:
    """Raise ValueError if any secret pattern is found in text."""
    for pattern in _PATTERNS:
        if pattern.search(text):
            raise ValueError(f"Secret-looking content detected (pattern: {pattern.pattern[:40]}…)")
