#!/usr/bin/env python3
"""Suno unofficial adapter — proxy-based music generation (§7.6). VOLATILE.

STATUS (2026-07-08): Suno has no general public self-serve API. This adapter
requires a self-hosted proxy (SUNO_API_BASE). Without it, live mode exits 5.
When the official Suno developer API ships, replace the HTTP logic here;
the CLI contract remains stable.

DO NOT hard-code SUNO_COOKIE or scrape suno.com directly.
Set SUNO_API_BASE to a local proxy that handles auth.
"""
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
from common.envload import get_env
from common.result import success_json, error_json

BACKEND = "suno_unofficial"
DEFAULT_TIMEOUT = 600  # music generation can take minutes
VOLATILE_NOTE = (
    "Suno access is via unofficial third-party APIs and breaks without notice. "
    "Check your proxy's docs, or apply to Suno's official developer API program."
)


def _proxy(method: str, base: str, path: str, body=None, key: str = "") -> dict:
    url = base.rstrip("/") + path
    data = json.dumps(body).encode() if body else None
    hdrs = {"Content-Type": "application/json", "User-Agent": "structured-asset-pipeline/1.0"}
    if key:
        hdrs["Authorization"] = f"Bearer {key}"
    req = urllib.request.Request(url, data=data, headers=hdrs, method=method)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read())


def run(args) -> None:
    t0 = time.time()
    require_abs(args.spec, "--spec")
    out = require_abs(args.out, "--out")
    with open(args.spec) as f:
        spec = yaml.safe_load(f)
    unit_id = spec.get("unit_id", "unknown")
    prompt = spec.get("prompt", "").strip()
    assert_no_secrets(prompt)
    assert_no_secrets(spec.get("lyrics", ""))
    params = spec.get("params") or {}
    assert_no_secrets(params.get("tags", ""))
    assert_no_secrets(params.get("title", "") or spec.get("title", ""))

    if args.dry_run:
        print(f"[dry-run] suno_unofficial: prompt={prompt[:60]}… tags={params.get('tags')} title={params.get('title')}", file=sys.stderr)
        success_json(backend=BACKEND, unit_id=unit_id, out=out, bytes_written=0,
                     model=None, dry_run=True, duration_ms=0)
        return

    refuse_overwrite(out)
    suno_base = get_env("SUNO_API_BASE")
    if not suno_base:
        msg = (
            "suno_unofficial: no SUNO_API_BASE configured; unofficial live calls disabled by default. "
            "Set SUNO_API_BASE to your proxy URL. " + VOLATILE_NOTE
        )
        error_json(backend=BACKEND, unit_id=unit_id, error_code=5, error=msg, retryable=False)
        sys.exit(5)

    suno_key = get_env("SUNO_API_KEY", "")
    endpoints = params.get("endpoints") or {}
    gen_path = endpoints.get("generate", "/api/generate")
    status_path_tpl = endpoints.get("status", "/api/get?ids={task_id}")

    body = {
        "prompt": prompt,
        "custom_mode": bool(spec.get("lyrics")),
        "lyrics": spec.get("lyrics"),
        "instrumental": params.get("make_instrumental", False),
        "tags": params.get("tags", ""),
        "title": params.get("title", spec.get("title", "")),
        "model_version": get_env("SUNO_MODEL_VERSION", "") or params.get("model_version", ""),
    }

    print(f"[suno_unofficial] POST {suno_base}{gen_path}", file=sys.stderr)
    try:
        resp = _proxy("POST", suno_base, gen_path, body, suno_key)
    except Exception as e:
        error_json(backend=BACKEND, unit_id=unit_id, error_code=3,
                   error=f"Request failed: {e}. {VOLATILE_NOTE}", retryable=True)
        sys.exit(3)

    task_id = resp.get("task_id") or resp.get("id") or (resp.get("data") or [{}])[0].get("id")
    if not task_id:
        error_json(backend=BACKEND, unit_id=unit_id, error_code=3,
                   error=f"No task_id in response: {str(resp)[:200]}. {VOLATILE_NOTE}", retryable=True)
        sys.exit(3)

    print(f"[suno_unofficial] task_id={task_id}; polling…", file=sys.stderr)
    while True:
        if time.time() - t0 > (args.timeout or DEFAULT_TIMEOUT):
            error_json(backend=BACKEND, unit_id=unit_id, error_code=3,
                       error=f"Poll timeout after {args.timeout}s. {VOLATILE_NOTE}", retryable=True)
            sys.exit(3)
        time.sleep(5)
        status_path = status_path_tpl.format(task_id=task_id)
        try:
            status_resp = _proxy("GET", suno_base, status_path, key=suno_key)
        except Exception:
            continue

        items = status_resp if isinstance(status_resp, list) else (status_resp.get("data") or [status_resp])
        for item in items:
            audio_url = item.get("audio_url") or item.get("song_path")
            if audio_url and audio_url.startswith("http"):
                ensure_parent(out)
                urllib.request.urlretrieve(audio_url, out)
                try:
                    verify_nonempty(out, min_bytes=1024)
                except RuntimeError as e:
                    error_json(backend=BACKEND, unit_id=unit_id, error_code=4, error=str(e), retryable=False)
                    sys.exit(4)
                success_json(backend=BACKEND, unit_id=unit_id, out=out,
                             bytes_written=os.path.getsize(out), model=None,
                             request_id=str(task_id), duration_ms=int((time.time() - t0) * 1000))
                return
        print(f"[suno_unofficial] waiting… {VOLATILE_NOTE[:40]}", file=sys.stderr)


def main():
    p = argparse.ArgumentParser(description="Suno unofficial adapter (VOLATILE)")
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
