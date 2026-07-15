#!/usr/bin/env python3
"""fal.ai adapter — queue-based image generation (§7.3)."""
import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import yaml
from common.paths import require_abs, ensure_parent, refuse_overwrite
from common.secrets import assert_no_secrets
from common.verify import verify_nonempty
from common.envload import require_env
from common.result import success_json, error_json

BACKEND = "fal"
DEFAULT_TIMEOUT = 300


def _fal(method: str, url: str, body=None, key: str = "") -> dict:
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data,
        headers={"Authorization": f"Key {key}", "Content-Type": "application/json",
                 "User-Agent": "structured-asset-pipeline/1.0"}, method=method)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read())


def _find_url(result: dict) -> str | None:
    for key in ("images", "image", "audio", "output"):
        val = result.get(key)
        if isinstance(val, list) and val:
            item = val[0]
            return item.get("url") if isinstance(item, dict) else str(item)
        if isinstance(val, str) and val.startswith("http"):
            return val
    return None


def run(args) -> None:
    t0 = time.time()
    require_abs(args.spec, "--spec")
    out = require_abs(args.out, "--out")
    with open(args.spec) as f:
        spec = yaml.safe_load(f)
    unit_id = spec.get("unit_id", "unknown")
    model = spec.get("model")
    if not model:
        print("ERROR: spec.model is required for fal adapter", file=sys.stderr); sys.exit(1)
    prompt = spec.get("prompt", "").strip()
    if not prompt:
        print("ERROR: spec.prompt empty", file=sys.stderr); sys.exit(1)
    assert_no_secrets(prompt)

    if args.dry_run:
        print(f"[dry-run] fal: model={model} prompt={prompt[:80]}…", file=sys.stderr)
        success_json(backend=BACKEND, unit_id=unit_id, out=out, bytes_written=0,
                     model=model, dry_run=True, duration_ms=0)
        return

    refuse_overwrite(out)
    key = require_env("FAL_KEY", "FAL_API_KEY")
    params = dict(spec.get("params") or {})
    params.pop("version", None)
    body = {"prompt": prompt, **params}

    submit_url = f"https://queue.fal.run/{model}"
    print(f"[fal] submitting to {submit_url}", file=sys.stderr)
    try:
        submitted = _fal("POST", submit_url, body, key)
    except urllib.error.HTTPError as e:
        body_err = e.read().decode(errors="replace")
        code = 2 if e.code in (401, 403) else 3
        error_json(backend=BACKEND, unit_id=unit_id, error_code=code,
                   error=f"HTTP {e.code}: {body_err[:200]}", retryable=(e.code >= 500))
        sys.exit(code)
    request_id = submitted.get("request_id")
    status_url = submitted.get("status_url") or f"https://queue.fal.run/{model}/requests/{request_id}/status"
    response_url = submitted.get("response_url") or f"https://queue.fal.run/{model}/requests/{request_id}"

    while True:
        if time.time() - t0 > (args.timeout or DEFAULT_TIMEOUT):
            error_json(backend=BACKEND, unit_id=unit_id, error_code=3, error="Poll timeout", retryable=True)
            sys.exit(3)
        time.sleep(2)
        try:
            status_data = _fal("GET", status_url, key=key)
        except urllib.error.HTTPError as e:
            body_err = e.read().decode(errors="replace")
            error_json(backend=BACKEND, unit_id=unit_id, error_code=3,
                       error=f"Poll HTTP {e.code}: {body_err[:200]}", retryable=True)
            sys.exit(3)
        status = status_data.get("status", "").upper()
        print(f"[fal] status={status}", file=sys.stderr)
        if status in ("COMPLETED", "SUCCESS"):
            break
        if status in ("FAILED", "ERROR"):
            error_json(backend=BACKEND, unit_id=unit_id, error_code=3,
                       error=status_data.get("error", status), retryable=False)
            sys.exit(3)

    try:
        result = _fal("GET", response_url, key=key)
    except urllib.error.HTTPError as e:
        body_err = e.read().decode(errors="replace")
        error_json(backend=BACKEND, unit_id=unit_id, error_code=3,
                   error=f"Result fetch HTTP {e.code}: {body_err[:200]}", retryable=True)
        sys.exit(3)
    url = _find_url(result)
    if not url:
        error_json(backend=BACKEND, unit_id=unit_id, error_code=3,
                   error=f"Cannot find output URL in response: {str(result)[:200]}", retryable=False)
        sys.exit(3)

    ensure_parent(out)
    urllib.request.urlretrieve(url, out)

    try:
        verify_nonempty(out, min_bytes=1024)
    except RuntimeError as e:
        error_json(backend=BACKEND, unit_id=unit_id, error_code=4, error=str(e), retryable=False)
        sys.exit(4)

    success_json(backend=BACKEND, unit_id=unit_id, out=out,
                 bytes_written=os.path.getsize(out), model=model,
                 request_id=request_id, duration_ms=int((time.time() - t0) * 1000))


def main():
    p = argparse.ArgumentParser(description="fal.ai adapter")
    p.add_argument("--spec", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    args = p.parse_args()
    try:
        run(args)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
