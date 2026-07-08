"""Stdout JSON result helpers (§6.3, §6.4). Adapters print exactly one JSON line."""
import json
import sys
import time


def success_json(
    *,
    backend: str,
    unit_id: str,
    out: str,
    bytes_written: int,
    model: str | None = None,
    request_id: str | None = None,
    duration_ms: int | None = None,
    dry_run: bool = False,
    **extra,
) -> None:
    payload = {
        "ok": True,
        "backend": backend,
        "unit_id": unit_id,
        "out": out,
        "bytes": bytes_written,
        "model": model,
        "request_id": request_id,
        "duration_ms": duration_ms,
        "dry_run": dry_run,
    }
    payload.update(extra)
    print(json.dumps(payload))


def error_json(
    *,
    backend: str,
    unit_id: str | None,
    error_code: int,
    error: str,
    retryable: bool = False,
    **extra,
) -> None:
    payload = {
        "ok": False,
        "backend": backend,
        "unit_id": unit_id,
        "error_code": error_code,
        "error": error,
        "retryable": retryable,
    }
    payload.update(extra)
    print(json.dumps(payload))
