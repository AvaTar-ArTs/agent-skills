"""File existence and non-empty verification (R3, R12)."""
import os


def verify_nonempty(path: str, min_bytes: int = 1) -> None:
    """Raise RuntimeError if file missing, empty, or below min_bytes."""
    if not os.path.exists(path):
        raise RuntimeError(f"Verification failed: file not found: {path}")
    size = os.path.getsize(path)
    if size < min_bytes:
        raise RuntimeError(
            f"Verification failed: {path} is {size} bytes (need >= {min_bytes})"
        )
