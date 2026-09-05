#!/usr/bin/env python3
"""Index skills/ and agents/ capability roots across a home directory.

The report records paths and metadata signals only; it does not copy prompt
content, credentials, or arbitrary file bodies into the index.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import subprocess
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path


SKIP = {
    ".git", "node_modules", "Library", ".cache", ".npm", ".bun", ".venv",
    "venv", "__pycache__", "dist", "build", ".tox", "vendor", "third_party",
}
ARCHIVE_MARKERS = {"backup", "backups", "archive", "archives", ".bak", "disabled", "history"}
CACHE_MARKERS = {"cache", "plugins", "marketplace", "extension-store", ".npm", ".bun", ".cache"}
RUNTIME_HOSTS = {".agent-skills", ".claude", ".codex", ".qwen", ".gemini", ".cursor", ".copilot", ".codeium", ".grok", ".windsurf", ".aider-desk", ".agents"}
SENSITIVE_NAMES = {
    ".env", ".env.local", ".env.production", ".env.development", "auth_info.json",
    "credentials.json", "credentials.jsonl", "token.json", "tokens.json",
    "secrets.json", "secret.json", "cookie.json", "cookies.json", "history.jsonl",
}
SENSITIVE_PARTS = {"auth", "authentication", "credential", "credentials", "secret", "secrets", "token", "tokens", "keychain", "cookies", "history", "histories", "sessions", "session", "private"}


def skipped(path: Path) -> bool:
    lowered = {part.lower() for part in path.parts}
    return any(part in SKIP for part in path.parts) or path.name.lower() in SENSITIVE_NAMES or bool(lowered & SENSITIVE_PARTS)


def classify(path: Path, home: Path) -> str:
    parts = path.relative_to(home).parts
    lowered = {part.lower() for part in parts}
    if parts[:1] == (".agent-skills",) and not any(marker in lowered for marker in ARCHIVE_MARKERS):
        return "canonical-source"
    if any(marker in lowered for marker in ARCHIVE_MARKERS) or any("backup" in part.lower() for part in parts):
        return "backup/archive"
    if any(marker in lowered for marker in CACHE_MARKERS):
        return "cache/vendored"
    if parts and parts[0] in RUNTIME_HOSTS:
        return "host-runtime"
    return "project-local"


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.S)
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line[:1].isspace():
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip("'\"")
    return values


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def candidate_dirs(home: Path) -> list[Path]:
    command = ["fd", "-HI", "-t", "d", "^(skills|agents)$", str(home)]
    for item in sorted(SKIP):
        command.extend(["-E", item])
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return sorted({Path(line.strip()) for line in result.stdout.splitlines() if line.strip()})


def files_under(root: Path, kind: str) -> list[Path]:
    result: list[Path] = []
    for path in root.rglob("*"):
        if skipped(path) or not path.is_file():
            continue
        if kind == "skill" and path.name == "SKILL.md":
            result.append(path)
        elif kind == "agent" and path.suffix.lower() == ".md":
            result.append(path)
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--home", type=Path, default=Path.home())
    parser.add_argument("--output-dir", type=Path, default=None)
    args = parser.parse_args()
    home = args.home.resolve()
    output = (args.output_dir or home / ".agent-skills" / "docs" / "audits").resolve()
    output.mkdir(parents=True, exist_ok=True)
    stamp = date.today().isoformat()

    rows: list[dict[str, object]] = []
    all_files: dict[str, set[Path]] = {"skill": set(), "agent": set()}
    for root in candidate_dirs(home):
        kind = "skill" if root.name == "skills" else "agent"
        files = files_under(root, kind)
        all_files[kind].update(files)
        rows.append({
            "kind": kind,
            "path": str(root),
            "classification": classify(root, home),
            "file_count": len(files),
            "frontmatter_count": sum(bool(frontmatter(read(path))) for path in files),
            "symlink": root.is_symlink(),
        })

    duplicate_names: dict[str, dict[str, list[str]]] = {"skill": defaultdict(list), "agent": defaultdict(list)}
    exact: dict[str, dict[str, list[str]]] = {"skill": defaultdict(list), "agent": defaultdict(list)}
    missing_description: dict[str, list[str]] = {"skill": [], "agent": []}
    for kind, paths in all_files.items():
        for path in sorted(paths):
            text = read(path)
            data = frontmatter(text)
            if data.get("name"):
                duplicate_names[kind][data["name"]].append(str(path))
            if data and not data.get("description"):
                missing_description[kind].append(str(path))
            digest = hashlib.sha256(text.encode()).hexdigest()
            exact[kind][digest].append(str(path))

    duplicate_names = {kind: {name: paths for name, paths in values.items() if len(paths) > 1} for kind, values in duplicate_names.items()}
    exact = {kind: {digest: paths for digest, paths in values.items() if len(paths) > 1} for kind, values in exact.items()}
    summary = {
        "generated": stamp,
        "home": str(home),
        "roots": len(rows),
        "roots_by_classification": dict(Counter(str(row["classification"]) for row in rows)),
        "files": {kind: len(paths) for kind, paths in all_files.items()},
        "files_by_classification": {
            kind: dict(Counter(classify(path, home) for path in paths))
            for kind, paths in all_files.items()
        },
        "duplicate_name_groups": {kind: len(groups) for kind, groups in duplicate_names.items()},
        "exact_duplicate_groups": {kind: len(groups) for kind, groups in exact.items()},
        "missing_description": {kind: len(paths) for kind, paths in missing_description.items()},
    }

    json_path = output / f"home-capability-index-{stamp}.json"
    csv_path = output / f"home-capability-roots-{stamp}.csv"
    md_path = output / f"home-capability-audit-{stamp}.md"
    import json
    json_path.write_text(json.dumps({"summary": summary, "roots": rows, "duplicate_names": duplicate_names, "exact_duplicates": exact, "missing_description": missing_description}, indent=2) + "\n")
    with csv_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["kind", "path", "classification", "file_count", "frontmatter_count", "symlink"])
        writer.writeheader()
        writer.writerows(rows)
    lines = [
        f"# Home Capability Audit — {stamp}", "", "## Scope", "",
        "Discovered `skills/` and `agents/` directories under `/Users/steven`, excluding dependency/build/cache internals listed in the scanner. The JSON/CSV index records paths and metadata counts, not prompt bodies or secrets.", "",
        "## Summary", "",
        f"- Capability roots: **{summary['roots']}**", f"- Skill files: **{summary['files']['skill']}**", f"- Agent Markdown files: **{summary['files']['agent']}**", f"- Skill duplicate-name groups: **{summary['duplicate_name_groups']['skill']}**", f"- Agent duplicate-name groups: **{summary['duplicate_name_groups']['agent']}**", f"- Exact duplicate skill groups: **{summary['exact_duplicate_groups']['skill']}**", f"- Exact duplicate agent groups: **{summary['exact_duplicate_groups']['agent']}**", "",
        "The all-home totals include cache/vendored and archive material. The canonical-source subset is the runtime baseline; host-runtime and project-local files are projections or separate workspaces until explicitly promoted.", "",
        "## Roots by classification", "", "| Classification | Roots |", "|---|---:|",
    ]
    lines.extend(f"| {key} | {value} |" for key, value in sorted(summary["roots_by_classification"].items()))
    lines.extend(["", "## Recommended consolidation order", "", "1. Keep `/Users/steven/.agent-skills` as the canonical source.", "2. Treat healthy host links as runtime projections and repair broken links before adding more copies.", "3. Mark project-local and host-specific copies as `active`, `alias`, `reference`, `backup`, or `cache`.", "4. Exclude dependency/plugin caches from runtime discovery and refresh this index from the script.", "", f"Machine-readable index: `{json_path.name}`; root CSV: `{csv_path.name}`."])
    md_path.write_text("\n".join(lines) + "\n")
    print(json.dumps({"summary": summary, "json": str(json_path), "csv": str(csv_path), "markdown": str(md_path)}, indent=2))


if __name__ == "__main__":
    main()
