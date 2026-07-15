"""Env-var resolution with alternate-name support (R2, §5.6)."""
import os
import sys


def require_env(*names: str) -> str:
    """Return value of first set env var among names; exit-2 (auth) with all names if none found."""
    for name in names:
        val = os.environ.get(name)
        if val:
            return val
    print(
        f"ERROR: missing required env var(s): {', '.join(names)}\n"
        f"Load with: source ~/.env.d/loader.sh",
        file=sys.stderr,
    )
    sys.exit(2)


def get_env(name: str, default: str | None = None) -> str | None:
    """Return env var value or default; never print the value."""
    return os.environ.get(name, default)
