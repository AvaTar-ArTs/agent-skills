#!/usr/bin/env python3
"""ComfyUI local adapter — workflow JSON injection + history polling (§7.4)."""
import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
import uuid

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import yaml
from common.paths import require_abs, ensure_parent, refuse_overwrite
from common.secrets import assert_no_secrets
from common.verify import verify_nonempty
from common.envload import get_env
from common.result import success_json, error_json

BACKEND = "comfyui"
DEFAULT_TIMEOUT = 300


def _comfy(method: str, base: str, path: str, body=None) -> dict:
    url = base.rstrip("/") + path
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data,
        headers={"Content-Type": "application/json", "User-Agent": "structured-asset-pipeline/1.0"},
        method=method)
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read())


def _inject_prompt(graph: dict, node_ids: list[str] | None, prompt_text: str,
                    neg_node: str | None, neg_text: str) -> dict:
    """Inject prompt into CLIPTextEncode nodes in the workflow graph."""
    if node_ids:
        for nid in node_ids:
            if str(nid) not in graph:
                raise ValueError(f"prompt_node_id {nid!r} not found in workflow graph")
            graph[str(nid)]["inputs"]["text"] = prompt_text
    else:
        for nid, node in graph.items():
            if node.get("class_type") == "CLIPTextEncode":
                graph[nid]["inputs"]["text"] = prompt_text
                break
        else:
            raise ValueError(
                "No CLIPTextEncode node found in workflow; set spec.params.prompt_node_ids explicitly"
            )
    if neg_node and neg_text:
        graph[str(neg_node)]["inputs"]["text"] = neg_text
    return graph


def run(args) -> None:
    t0 = time.time()
    require_abs(args.spec, "--spec")
    out = require_abs(args.out, "--out")
    with open(args.spec) as f:
        spec = yaml.safe_load(f)
    unit_id = spec.get("unit_id", "unknown")
    prompt = spec.get("prompt", "").strip()
    assert_no_secrets(prompt)
    assert_no_secrets(spec.get("negative_prompt", ""))
    params = spec.get("params") or {}
    workflow_path = params.get("workflow_path")
    base_url = get_env("COMFYUI_BASE_URL", "http://127.0.0.1:8188")

    if args.dry_run:
        if not workflow_path:
            print("ERROR: spec.params.workflow_path required for comfyui", file=sys.stderr)
            sys.exit(1)
        wf_exists = os.path.exists(workflow_path)
        print(f"[dry-run] comfyui: base={base_url} workflow={workflow_path} exists={wf_exists}", file=sys.stderr)
        if not wf_exists:
            print(f"ERROR: workflow_path not found: {workflow_path}", file=sys.stderr)
            sys.exit(1)
        success_json(backend=BACKEND, unit_id=unit_id, out=out, bytes_written=0,
                     model=None, dry_run=True, duration_ms=0)
        return

    refuse_overwrite(out)
    if not workflow_path:
        print("ERROR: spec.params.workflow_path required for comfyui", file=sys.stderr); sys.exit(1)
    require_abs(workflow_path, "workflow_path")

    try:
        _comfy("GET", base_url, "/system_stats")
    except Exception:
        error_json(backend=BACKEND, unit_id=unit_id, error_code=3,
                   error=f"Cannot connect to ComfyUI at {base_url} — is it running?", retryable=True)
        sys.exit(3)

    with open(workflow_path) as f:
        graph = json.load(f)

    node_ids = params.get("prompt_node_ids")
    neg_node = params.get("negative_node_id")
    graph = _inject_prompt(graph, node_ids, prompt, neg_node, spec.get("negative_prompt", ""))

    client_id = str(uuid.uuid4())
    resp = _comfy("POST", base_url, "/prompt", {"prompt": graph, "client_id": client_id})
    prompt_id = resp["prompt_id"]
    print(f"[comfyui] prompt_id={prompt_id}; polling history…", file=sys.stderr)

    while True:
        if time.time() - t0 > (args.timeout or DEFAULT_TIMEOUT):
            error_json(backend=BACKEND, unit_id=unit_id, error_code=3, error="Poll timeout", retryable=True)
            sys.exit(3)
        time.sleep(2)
        history = _comfy("GET", base_url, f"/history/{prompt_id}")
        if prompt_id not in history:
            continue
        outputs = history[prompt_id].get("outputs", {})
        found_url = None
        for node_out in outputs.values():
            imgs = node_out.get("images", [])
            if imgs:
                img = imgs[0]
                qs = f"filename={img['filename']}&subfolder={img.get('subfolder','')}&type={img.get('type','output')}"
                found_url = f"{base_url.rstrip('/')}/view?{qs}"
                break
        if found_url:
            ensure_parent(out)
            urllib.request.urlretrieve(found_url, out)
            break

    try:
        verify_nonempty(out, min_bytes=1024)
    except RuntimeError as e:
        error_json(backend=BACKEND, unit_id=unit_id, error_code=4, error=str(e), retryable=False)
        sys.exit(4)

    success_json(backend=BACKEND, unit_id=unit_id, out=out,
                 bytes_written=os.path.getsize(out), model=None,
                 request_id=prompt_id, duration_ms=int((time.time() - t0) * 1000))


def main():
    p = argparse.ArgumentParser(description="ComfyUI local adapter")
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
