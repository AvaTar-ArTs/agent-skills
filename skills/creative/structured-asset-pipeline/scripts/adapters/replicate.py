#!/usr/bin/env python3
"""Replicate adapter — async prediction polling (§7.2)."""
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

BACKEND = "replicate"
API_BASE = "https://api.replicate.com/v1"
DEFAULT_TIMEOUT = 300
DEFAULT_MODEL = "black-forest-labs/flux-1.1-pro"  # placeholder — operator should set spec.model


def _api(method: str, path: str, body=None, token: str = "") -> dict:
    url = API_BASE + path
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json",
                 "User-Agent": "structured-asset-pipeline/1.0"}, method=method)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read())


def run(args) -> None:
    t0 = time.time()
    require_abs(args.spec, "--spec")
    out = require_abs(args.out, "--out")
    with open(args.spec) as f:
        spec = yaml.safe_load(f)
    unit_id = spec.get("unit_id", "unknown")
    model = spec.get("model") or DEFAULT_MODEL
    prompt = spec.get("prompt", "").strip()
    if not prompt:
        print("ERROR: spec.prompt empty", file=sys.stderr); sys.exit(1)
    assert_no_secrets(prompt)
    version = (spec.get("params") or {}).get("version")

    if args.dry_run:
        print(f"[dry-run] replicate: model={model} version={version} prompt={prompt[:80]}…", file=sys.stderr)
        success_json(backend=BACKEND, unit_id=unit_id, out=out, bytes_written=0,
                     model=model, dry_run=True, duration_ms=0)
        return

    refuse_overwrite(out)
    token = require_env("REPLICATE_API_TOKEN", "REPLICATE_API_KEY")
    body = {"input": {"prompt": prompt}}
    try:
        if version:
            body["version"] = version
            pred = _api("POST", "/predictions", body, token)
        else:
            pred = _api("POST", f"/models/{model}/predictions", body, token)
    except urllib.error.HTTPError as e:
        body_err = e.read().decode(errors="replace")
        code = 2 if e.code in (401, 403) else 3
        error_json(backend=BACKEND, unit_id=unit_id, error_code=code,
                   error=f"HTTP {e.code}: {body_err[:200]}", retryable=(e.code >= 500))
        sys.exit(code)

    pred_id = pred["id"]
    print(f"[replicate] prediction {pred_id} created; polling…", file=sys.stderr)
    interval = 1
    while True:
        if time.time() - t0 > (args.timeout or DEFAULT_TIMEOUT):
            error_json(backend=BACKEND, unit_id=unit_id, error_code=3, error="Poll timeout", retryable=True)
            sys.exit(3)
        time.sleep(interval)
        interval = min(interval * 1.5, 5)
        try:
            p = _api("GET", f"/predictions/{pred_id}", token=token)
        except urllib.error.HTTPError as e:
            body_err = e.read().decode(errors="replace")
            error_json(backend=BACKEND, unit_id=unit_id, error_code=3,
                       error=f"Poll HTTP {e.code}: {body_err[:200]}", retryable=True)
            sys.exit(3)
        status = p.get("status")
        print(f"[replicate] status={status}", file=sys.stderr)
        if status == "succeeded":
            output = p.get("output")
            url = (output[0] if isinstance(output, list) else output)
            if not url:
                error_json(backend=BACKEND, unit_id=unit_id, error_code=3,
                           error="Prediction succeeded but output is empty", retryable=False)
                sys.exit(3)
            ensure_parent(out)
            urllib.request.urlretrieve(url, out)
            break
        if status in ("failed", "canceled"):
            error_json(backend=BACKEND, unit_id=unit_id, error_code=3,
                       error=p.get("error", status), retryable=False)
            sys.exit(3)

    try:
        verify_nonempty(out, min_bytes=1024)
    except RuntimeError as e:
        error_json(backend=BACKEND, unit_id=unit_id, error_code=4, error=str(e), retryable=False)
        sys.exit(4)

    success_json(backend=BACKEND, unit_id=unit_id, out=out,
                 bytes_written=os.path.getsize(out), model=model,
                 request_id=pred_id, duration_ms=int((time.time() - t0) * 1000))


def main():
    p = argparse.ArgumentParser(description="Replicate adapter")
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
