#!/usr/bin/env python3
"""ElevenLabs TTS adapter — text-to-speech audio generation (§7.5)."""
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
from common.envload import require_env, get_env
from common.result import success_json, error_json

BACKEND = "elevenlabs"
DEFAULT_MODEL = "eleven_multilingual_v2"
API_BASE = "https://api.elevenlabs.io/v1"


def run(args) -> None:
    t0 = time.time()
    require_abs(args.spec, "--spec")
    out = require_abs(args.out, "--out")
    with open(args.spec) as f:
        spec = yaml.safe_load(f)
    unit_id = spec.get("unit_id", "unknown")
    prompt = spec.get("prompt", "").strip()
    if not prompt:
        print("ERROR: spec.prompt empty (must contain spoken text for ElevenLabs)", file=sys.stderr); sys.exit(1)
    assert_no_secrets(prompt)

    voice_id = spec.get("voice_id") or (spec.get("params") or {}).get("voice_id")
    if not voice_id or voice_id == "REPLACE_ME":
        print("ERROR: spec.voice_id required (or spec.params.voice_id); it must be set to a valid ElevenLabs voice ID", file=sys.stderr)
        sys.exit(1)

    model = spec.get("model") or DEFAULT_MODEL
    params = spec.get("params") or {}
    output_format = params.get("output_format", "mp3_44100_128")

    if args.dry_run:
        print(f"[dry-run] elevenlabs: model={model} voice={voice_id} text={prompt[:60]}…", file=sys.stderr)
        success_json(backend=BACKEND, unit_id=unit_id, out=out, bytes_written=0,
                     model=model, dry_run=True, duration_ms=0)
        return

    refuse_overwrite(out)
    api_key = require_env("ELEVENLABS_API_KEY")
    voice_settings = {}
    for field in ("stability", "similarity_boost", "style", "speed"):
        if field in params:
            voice_settings[field] = params[field]

    body = json.dumps({
        "text": prompt,
        "model_id": model,
        "voice_settings": voice_settings or {"stability": 0.5, "similarity_boost": 0.75},
    }).encode()
    url = f"{API_BASE}/text-to-speech/{voice_id}?output_format={output_format}"
    req = urllib.request.Request(url, data=body,
        headers={"xi-api-key": api_key, "Content-Type": "application/json",
                 "User-Agent": "structured-asset-pipeline/1.0"}, method="POST")

    print(f"[elevenlabs] POST /v1/text-to-speech/{voice_id} model={model}", file=sys.stderr)
    try:
        with urllib.request.urlopen(req, timeout=args.timeout or 120) as resp:
            audio = resp.read()
    except urllib.error.HTTPError as e:
        body_err = e.read().decode(errors="replace")
        code = 2 if e.code in (401, 403) else 3
        error_json(backend=BACKEND, unit_id=unit_id, error_code=code,
                   error=f"HTTP {e.code}: {body_err[:200]}", retryable=(e.code >= 500))
        sys.exit(code)

    ensure_parent(out)
    with open(out, "wb") as f:
        f.write(audio)

    try:
        verify_nonempty(out, min_bytes=1024)
    except RuntimeError as e:
        error_json(backend=BACKEND, unit_id=unit_id, error_code=4, error=str(e), retryable=False)
        sys.exit(4)

    success_json(backend=BACKEND, unit_id=unit_id, out=out,
                 bytes_written=os.path.getsize(out), model=model,
                 duration_ms=int((time.time() - t0) * 1000))


def main():
    p = argparse.ArgumentParser(description="ElevenLabs TTS adapter")
    p.add_argument("--spec", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--timeout", type=int, default=120)
    args = p.parse_args()
    try:
        run(args)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
