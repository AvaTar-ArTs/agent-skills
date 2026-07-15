"""Absolute path helpers and backup utilities (R2, R4, R10)."""
import os
import sys
from datetime import datetime, UTC


def require_abs(path: str, name: str = "path") -> str:
    """Raise ValueError if path is not absolute (enforces R2)."""
    if not os.path.isabs(path):
        raise ValueError(f"{name} must be absolute, got: {path!r}")
    return path


def ensure_parent(path: str) -> None:
    """Create parent directory of path if it does not exist."""
    os.makedirs(os.path.dirname(path), exist_ok=True)


def backup_with_timestamp(path: str) -> str | None:
    """Rename existing file with backup suffix; return backup path or None if original absent."""
    if not os.path.exists(path):
        return None
    ts = datetime.now(UTC).strftime("%Y%m%d-%H%M%S")
    base, ext = os.path.splitext(path)
    backup = f"{base}-backup-{ts}{ext}"
    os.rename(path, backup)
    return backup


def refuse_overwrite(out: str) -> None:
    """Exit 1 if out already exists and is non-empty, unless PIPELINE_ALLOW_OVERWRITE=1 (R10)."""
    if os.environ.get("PIPELINE_ALLOW_OVERWRITE") == "1":
        return
    if os.path.exists(out) and os.path.getsize(out) > 0:
        print(
            f"ERROR: output file already exists and is non-empty: {out}\n"
            f"  Delete it, run backup_with_timestamp() first, or set PIPELINE_ALLOW_OVERWRITE=1.",
            file=sys.stderr,
        )
        sys.exit(1)
