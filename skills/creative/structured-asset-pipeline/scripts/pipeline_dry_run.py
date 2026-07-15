#!/usr/bin/env python3
"""No-network dress rehearsal: dry-run all specs in a run directory (D10 / Step 9).

Usage:
  python scripts/pipeline_dry_run.py --run-dir /abs/path/to/run-directory

Expects run-directory/specs/*.yaml files (or tests/fixtures/mock-run/specs/ for CI).
Invokes each adapter with --dry-run; writes report-dryrun.md. No network; no credentials needed.
"""
import argparse
import json
import os
import subprocess
import sys

SKILL_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADAPTERS_DIR = os.path.join(SKILL_ROOT, 'scripts', 'adapters')

BACKEND_MAP = {
    'openai_images': 'openai_images.py',
    'replicate': 'replicate.py',
    'fal': 'fal.py',
    'comfyui': 'comfyui.py',
    'elevenlabs': 'elevenlabs.py',
    'suno_unofficial': 'suno_unofficial.py',
}


def load_spec(path: str) -> dict:
    import yaml
    with open(path) as f:
        return yaml.safe_load(f)


def run_dry(spec_path: str, run_dir: str) -> dict:
    spec = load_spec(spec_path)
    unit_id = spec.get('unit_id', os.path.basename(spec_path))
    backend = spec.get('backend', '')
    adapter_file = BACKEND_MAP.get(backend)
    if not adapter_file:
        return {'unit_id': unit_id, 'backend': backend, 'ok': False, 'error': f'Unknown backend: {backend}'}

    out_rel = spec.get('out_relpath', f'out/{unit_id}')
    out_abs = os.path.join(run_dir, out_rel)

    cmd = [sys.executable, os.path.join(ADAPTERS_DIR, adapter_file),
           '--spec', spec_path, '--out', out_abs, '--dry-run']
    proc = subprocess.run(cmd, capture_output=True, text=True)

    result_line = proc.stdout.strip().splitlines()[-1] if proc.stdout.strip() else '{}'
    try:
        result = json.loads(result_line)
    except json.JSONDecodeError:
        result = {'ok': False, 'error': result_line}
    result['exit_code'] = proc.returncode
    if proc.stderr:
        result['stderr_tail'] = proc.stderr.strip().splitlines()[-1]
    return result


def write_report(run_dir: str, results: list[dict]) -> str:
    lines = ['# Pipeline dry-run report\n', f'Run dir: {run_dir}\n\n',
             '| unit_id | backend | ok | exit | note |\n',
             '|---------|---------|----|----|------|\n']
    all_ok = True
    for r in results:
        ok = r.get('ok', False)
        if not ok:
            all_ok = False
        note = r.get('error') or r.get('stderr_tail') or ''
        lines.append(f"| {r.get('unit_id','?')} | {r.get('backend','?')} | {ok} | {r.get('exit_code','?')} | {note[:60]} |\n")
    lines.append(f'\n**Result: {"ALL PASS" if all_ok else "FAILURES DETECTED"}**\n')
    report_path = os.path.join(run_dir, 'report-dryrun.md')
    os.makedirs(run_dir, exist_ok=True)
    with open(report_path, 'w') as f:
        f.writelines(lines)
    return report_path


def main():
    p = argparse.ArgumentParser(description='pipeline_dry_run: dress rehearsal without credentials')
    p.add_argument('--run-dir', required=True, help='Absolute path to run directory containing specs/')
    args = p.parse_args()
    run_dir = args.run_dir
    if not os.path.isabs(run_dir):
        print(f'ERROR: --run-dir must be absolute, got: {run_dir!r}', file=sys.stderr)
        sys.exit(1)

    specs_dir = os.path.join(run_dir, 'specs')
    if not os.path.isdir(specs_dir):
        print(f'ERROR: specs/ directory not found in {run_dir}', file=sys.stderr)
        sys.exit(1)

    specs = sorted(f for f in os.listdir(specs_dir) if f.endswith('.yaml') and not f.startswith('00-'))
    if not specs:
        print(f'No unit spec files found in {specs_dir}', file=sys.stderr)
        sys.exit(1)

    print(f'[pipeline_dry_run] Found {len(specs)} specs in {specs_dir}')
    results = []
    for spec_file in specs:
        spec_path = os.path.join(specs_dir, spec_file)
        print(f'  dry-run: {spec_file}', end=' ', flush=True)
        r = run_dry(spec_path, run_dir)
        results.append(r)
        print('OK' if r.get('ok') else f'FAIL ({r.get("error","")})')

    report = write_report(run_dir, results)
    print(f'\nReport written: {report}')
    failed = [r for r in results if not r.get('ok')]
    if failed:
        print(f'FAILURES: {len(failed)}/{len(results)}')
        sys.exit(1)
    print(f'All {len(results)} units passed dry-run.')


if __name__ == '__main__':
    main()
