#!/usr/bin/env python3
"""OpenAI Images adapter — generates images via gpt-image-1 or dall-e-3 (§7.1)."""
import argparse
import base64
import json
import os
import sys
import time
import urllib.request

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import yaml
from common.paths import require_abs, ensure_parent, refuse_overwrite
from common.secrets import assert_no_secrets
from common.verify import verify_nonempty
from common.envload import require_env
from common.result import success_json, error_json

BACKEND = "openai_images"
DEFAULT_MODEL = "gpt-image-1"
DEFAULT_TIMEOUT = 120

# Supported sizes per model family
_ASPECT_TO_DALLE3 = {
    "1:1": "1024x1024",
    "3:4": "1024x1792", "2:3": "1024x1792", "9:16": "1024x1792",
    "4:3": "1792x1024", "3:2": "1792x1024", "16:9": "1792x1024",
}
_ASPECT_TO_GPT_IMAGE_1 = {
    "1:1": "1024x1024",
    "3:4": "1024x1536", "2:3": "1024x1536", "9:16": "1024x1536",
    "4:3": "1536x1024", "3:2": "1536x1024", "16:9": "1536x1024",
}


def resolve_size(spec: dict) -> str:
    if spec.get("size"):
        return spec["size"]
    model = (spec.get("model") or DEFAULT_MODEL).lower()
    ratio = spec.get("aspect_ratio", "1:1")
    table = _ASPECT_TO_DALLE3 if "dall-e" in model else _ASPECT_TO_GPT_IMAGE_1
    return table.get(ratio, "1024x1024")


def load_spec(spec_path: str) -> dict:
    require_abs(spec_path, "--spec")
    with open(spec_path) as f:
        spec = yaml.safe_load(f)
    if not spec.get("prompt"):
        print("ERROR: spec.prompt is empty", file=sys.stderr)
        sys.exit(1)
    assert_no_secrets(spec.get("prompt", ""))
    return spec


def run(args) -> None:
    t0 = time.time()
    spec = load_spec(args.spec)
    out = require_abs(args.out, "--out")
    unit_id = spec.get("unit_id", "unknown")
    model = spec.get("model") or DEFAULT_MODEL
    size = resolve_size(spec)
    prompt = spec["prompt"].strip()

    if args.dry_run:
        print(f"[dry-run] openai_images: model={model} size={size} prompt={prompt[:80]}…", file=sys.stderr)
        success_json(backend=BACKEND, unit_id=unit_id, out=out, bytes_written=0,
                     model=model, dry_run=True, duration_ms=0)
        return

    refuse_overwrite(out)
    api_key = require_env("OPENAI_API_KEY")
    base_url = os.environ.get("OPENAI_BASE_URL", "https://api.openai.com").rstrip("/")

    body = json.dumps({"model": model, "prompt": prompt, "size": size, "n": 1,
                        "response_format": "b64_json"}).encode()
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json",
               "User-Agent": "structured-asset-pipeline/1.0"}

    print(f"[openai_images] POST {base_url}/v1/images/generations model={model} size={size}", file=sys.stderr)
    req = urllib.request.Request(f"{base_url}/v1/images/generations", data=body,
                                  headers=headers, method="POST")

    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=args.timeout or DEFAULT_TIMEOUT) as resp:
                raw = resp.read()
            break
        except urllib.error.HTTPError as e:
            body_err = e.read().decode(errors="replace")
            if e.code == 429 and attempt == 0:
                print(f"[openai_images] 429 rate limited; retrying in 3s…", file=sys.stderr)
                time.sleep(3)
                continue
            if e.code in (401, 403):
                error_json(backend=BACKEND, unit_id=unit_id, error_code=2,
                           error=f"HTTP {e.code} auth: {body_err[:200]}", retryable=False)
                sys.exit(2)
            error_json(backend=BACKEND, unit_id=unit_id, error_code=3,
                       error=f"HTTP {e.code}: {body_err[:200]}", retryable=(e.code >= 500))
            sys.exit(3)
    else:
        error_json(backend=BACKEND, unit_id=unit_id, error_code=3,
                   error="Rate limited after retry", retryable=True)
        sys.exit(3)

    data = json.loads(raw)
    ensure_parent(out)

    if "data" not in data or not data["data"]:
        error_json(backend=BACKEND, unit_id=unit_id, error_code=3, error="Empty response data", retryable=False)
        sys.exit(3)

    item = data["data"][0]
    if "b64_json" in item:
        img_bytes = base64.b64decode(item["b64_json"])
        with open(out, "wb") as f:
            f.write(img_bytes)
    elif "url" in item:
        urllib.request.urlretrieve(item["url"], out)
    else:
        error_json(backend=BACKEND, unit_id=unit_id, error_code=3, error="No b64_json or url in response", retryable=False)
        sys.exit(3)

    try:
        verify_nonempty(out, min_bytes=1024)
    except RuntimeError as e:
        error_json(backend=BACKEND, unit_id=unit_id, error_code=4, error=str(e), retryable=False)
        sys.exit(4)

    duration_ms = int((time.time() - t0) * 1000)
    bytes_written = os.path.getsize(out)
    request_id = data.get("id") or (data.get("data", [{}])[0].get("request_id"))
    success_json(backend=BACKEND, unit_id=unit_id, out=out, bytes_written=bytes_written,
                 model=model, request_id=request_id, duration_ms=duration_ms)


def main():
    parser = argparse.ArgumentParser(description="OpenAI Images adapter")
    parser.add_argument("--spec", required=True, help="Absolute path to unit spec YAML")
    parser.add_argument("--out", required=True, help="Absolute path for output PNG")
    parser.add_argument("--dry-run", action="store_true", help="Validate + print; write nothing")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT)
    args = parser.parse_args()
    try:
        run(args)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
