#!/usr/bin/env python3
"""Build a provenance-aware capability registry and runtime health report.

The scanner records metadata only. It intentionally excludes credentials,
history, session data, databases, media, caches, and other sensitive/runtime
material from indexes. The canonical source is the only authoritative lock
source; other lock files are reported as host adapters.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable


SKIP_DIRS = {
    ".git", ".cache", ".npm", ".bun", ".venv", "venv", "node_modules",
    "__pycache__", "dist", "build", ".tox", "vendor", "third_party",
    "Library", "backups", "backup", "archives", "archive", "history",
    "sessions", "session", "cache", "caches", "plugins", "marketplace",
    "tmp", "tmp-csv", "tmp-md", "exports", "media", "artifacts",
}
SENSITIVE_NAMES = {
    ".env", ".env.local", ".env.production", ".env.development",
    "auth_info.json", "credentials.json", "credentials.jsonl",
    "token.json", "tokens.json", "secrets.json", "secret.json",
    "cookie.json", "cookies.json", "history.jsonl", "shared.sqlite",
}
SENSITIVE_PARTS = {
    "auth", "authentication", "credential", "credentials", "secrets",
    "secret", "tokens", "token", "keychain", "cookies", "cookie",
    "history", "histories", "sessions", "session", "private",
}
FRONTMATTER = re.compile(r"^---\n(.*?)\n---(?:\n|$)", re.S)
RUNTIME_HOSTS = {
    ".agents", ".claude", ".codex", ".cursor", ".gemini", ".qwen",
    ".grok", ".hermes", ".opencode", ".kimi", ".cline", ".copilot",
    ".codeium", ".windsurf", ".aider-desk",
}
KNOWN_PROJECTIONS = {
    ".claude/skills": "/Users/steven/.agent-skills/skills",
    ".claude/agents": "/Users/steven/.agent-skills/agents",
    ".codex/superpowers": "/Users/steven/.agent-skills/skills/using-superpowers",
    ".agents/skills": "/Users/steven/.agent-skills/skills",
}


def now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def is_sensitive(path: Path) -> bool:
    lowered = {part.lower() for part in path.parts}
    if path.name.lower() in SENSITIVE_NAMES:
        return True
    return bool(lowered & SENSITIVE_PARTS)


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts) or is_sensitive(path)


def parse_frontmatter(text: str) -> dict[str, str]:
    match = FRONTMATTER.match(text)
    if not match:
        return {}
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line[:1].isspace():
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip("'\"")
    return result


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def safe_read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def classify(path: Path, home: Path, canonical: Path) -> str:
    try:
        relative = path.resolve().relative_to(home.resolve())
    except ValueError:
        relative = path
    parts = relative.parts
    if path.resolve() == canonical.resolve() or parts[:1] == (canonical.name,):
        return "active"
    if any(part.lower() in {"backup", "backups", "archive", "archives"} or "backup" in part.lower() for part in parts):
        return "archived"
    if any(part.lower() in {"cache", "caches", "plugins", "marketplace"} for part in parts):
        return "cached"
    if parts and parts[0] in RUNTIME_HOSTS:
        return "projected"
    return "project-local"


def capability_files(root: Path, kind: str) -> Iterable[Path]:
    if not root.exists():
        return []
    result: list[Path] = []
    for current, dirs, files in os.walk(root, followlinks=False):
        current_path = Path(current)
        dirs[:] = [name for name in dirs if name not in SKIP_DIRS and not is_sensitive(current_path / name)]
        for name in files:
            path = current_path / name
            if is_sensitive(path):
                continue
            if kind == "skill" and name == "SKILL.md":
                result.append(path)
            elif kind == "agent" and path.suffix.lower() == ".md" and name != "README.md":
                result.append(path)
    return sorted(result)


def capability_roots(home: Path) -> dict[str, set[Path]]:
    """Find capability roots without descending into sensitive/runtime data."""
    roots: dict[str, set[Path]] = {"skill": set(), "agent": set()}
    for current, dirs, _files in os.walk(home, followlinks=False):
        current_path = Path(current)
        dirs[:] = [name for name in dirs if name not in {
            ".git", ".cache", ".npm", ".bun", ".venv", "venv", "node_modules",
            "__pycache__", "dist", "build", ".tox", "vendor", "third_party",
        } and not is_sensitive(current_path / name)]
        if current_path.name in {"skills", "agents"}:
            roots["skill" if current_path.name == "skills" else "agent"].add(current_path)
    # An outer skills/agents root already covers nested roots of the same kind.
    # Keeping only the minimal roots prevents exponential rescanning in plugin
    # trees that contain several nested compatibility layouts.
    for kind, candidates in roots.items():
        minimal: set[Path] = set()
        for candidate in sorted(candidates, key=lambda item: len(item.parts)):
            if not any(parent in minimal for parent in candidate.parents):
                minimal.add(candidate)
        roots[kind] = minimal
    return roots


def record(path: Path, kind: str, home: Path, canonical: Path) -> dict[str, object]:
    text = safe_read(path)
    metadata = parse_frontmatter(text)
    try:
        relative = str(path.resolve().relative_to(home.resolve()))
    except ValueError:
        relative = str(path)
    return {
        "kind": kind,
        "path": relative,
        "classification": classify(path, home, canonical),
        "name": metadata.get("name") or path.parent.name,
        "description_present": bool(metadata.get("description")),
        "sha256": sha256(path),
        "size_bytes": path.stat().st_size,
    }


def projection_report(home: Path) -> dict[str, object]:
    entries: list[dict[str, object]] = []
    for relative, expected in KNOWN_PROJECTIONS.items():
        path = home / relative
        target = os.readlink(path) if path.is_symlink() else None
        resolved = str(path.resolve()) if path.exists() else None
        entries.append({
            "path": relative,
            "expected_target": expected,
            "is_symlink": path.is_symlink(),
            "target": target,
            "resolved": resolved,
            "healthy": path.is_symlink() and path.exists() and resolved == expected,
        })
    roots = [home / name for name in RUNTIME_HOSTS if (home / name).exists()]
    broken: list[str] = []
    for root in roots:
        for current, dirs, files in os.walk(root, followlinks=False):
            current_path = Path(current)
            dirs[:] = [name for name in dirs if name not in SKIP_DIRS]
            for name in [*dirs, *files]:
                path = current_path / name
                if path.is_symlink() and not path.exists():
                    broken.append(str(path.relative_to(home)))
    return {"known": entries, "broken_links": sorted(set(broken))}


def lock_report(canonical: Path, home: Path) -> dict[str, object]:
    locks = [canonical / ".skill-lock.json", home / ".agents/.skill-lock.json"]
    result: list[dict[str, object]] = []
    for path in locks:
        if not path.exists():
            continue
        try:
            data = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError) as exc:
            result.append({"path": str(path), "error": str(exc)})
            continue
        result.append({
            "path": str(path),
            "authority": path.resolve() == (canonical / ".skill-lock.json").resolve(),
            "version": data.get("version"),
            "skills": sorted(data.get("skills", {}).keys()),
            "lastSelectedAgents": sorted(data.get("lastSelectedAgents", [])),
        })
    authority = next((item for item in result if item.get("authority")), None)
    drift = []
    if authority:
        for item in result:
            if item is authority:
                continue
            if item.get("skills") != authority.get("skills") or item.get("lastSelectedAgents") != authority.get("lastSelectedAgents"):
                drift.append(item["path"])
    return {"authority": str(canonical / ".skill-lock.json"), "files": result, "drift": drift}


def git_commit(root: Path) -> str | None:
    try:
        return subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return None


def enrich_duplicate_groups(groups: dict[str, list[str]], home: Path, canonical: Path) -> dict[str, object]:
    enriched: dict[str, object] = {}
    for key, paths in groups.items():
        entries = []
        for raw_path in paths:
            path = Path(raw_path)
            if not path.is_absolute():
                path = home / path
            entries.append({
                "path": raw_path,
                "classification": classify(path, home, canonical),
            })
        enriched[key] = {"members": entries, "classifications": sorted({str(item["classification"]) for item in entries})}
    return enriched


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--home", type=Path, default=Path.home())
    parser.add_argument("--canonical", type=Path, default=None)
    parser.add_argument("--out", type=Path, default=None)
    parser.add_argument("--full-home", action="store_true", help="Scan every home capability file; expensive on large plugin caches")
    parser.add_argument("--home-audit", type=Path, default=None, help="Reuse a prior home-capability-index JSON for classified root/dedup evidence")
    args = parser.parse_args()
    home = args.home.expanduser().resolve()
    canonical = (args.canonical or home / ".agent-skills").expanduser().resolve()
    out = (args.out or canonical / "catalog").resolve()
    out.mkdir(parents=True, exist_ok=True)
    indexes = out / "indexes"
    indexes.mkdir(parents=True, exist_ok=True)

    records: list[dict[str, object]] = []
    roots = capability_roots(home) if args.full_home else {"skill": {canonical / "skills"}, "agent": {canonical / "agents"}}
    roots["skill"].add(canonical / "deep-research")
    seen: set[Path] = set()
    for kind, root_paths in roots.items():
        for root in sorted(root_paths):
            for path in capability_files(root, kind):
                resolved = path.resolve()
                if resolved in seen:
                    continue
                seen.add(resolved)
                records.append(record(path, kind, home, canonical))
    records.sort(key=lambda item: (str(item["classification"]), str(item["kind"]), str(item["path"])))

    classified: dict[str, list[dict[str, object]]] = defaultdict(list)
    by_hash: dict[str, list[str]] = defaultdict(list)
    by_name: dict[str, list[str]] = defaultdict(list)
    for item in records:
        classified[str(item["classification"])].append(item)
        by_hash[str(item["sha256"])].append(str(item["path"]))
        by_name[f"{item['kind']}:{item['name']}"] .append(str(item["path"]))

    home_audit_path = args.home_audit
    home_audit: dict[str, object] = {}
    if home_audit_path and home_audit_path.exists():
        try:
            home_audit = json.loads(home_audit_path.read_text())
        except (OSError, json.JSONDecodeError):
            home_audit = {}
    home_roots = home_audit.get("roots", []) if isinstance(home_audit, dict) else []
    home_duplicate_hashes = home_audit.get("exact_duplicates", {}) if isinstance(home_audit, dict) else {}
    home_duplicate_names = home_audit.get("duplicate_names", {}) if isinstance(home_audit, dict) else {}
    dedup = {
        "generated_at": now(),
        "exact_hash_groups": enrich_duplicate_groups(home_duplicate_hashes or {key: value for key, value in by_hash.items() if len(value) > 1}, home, canonical),
        "name_groups": enrich_duplicate_groups(home_duplicate_names or {key: value for key, value in by_name.items() if len(value) > 1}, home, canonical),
        "method": "SHA-256 of capability files; provenance is the path classification and canonical source commit.",
    }
    projection = projection_report(home)
    locks = lock_report(canonical, home)
    registry = {
        "schema": "capability-authority/v1",
        "generated_at": now(),
        "home": str(home),
        "canonical_root": str(canonical),
        "canonical_git_commit": git_commit(canonical),
        "authority": {
            "source": str(canonical),
            "lock": str(canonical / ".skill-lock.json"),
            "statuses": ["active", "projected", "project-local", "archived", "cached"],
            "index_policy": "metadata, hashes, and paths only; sensitive/history/runtime data excluded",
        },
        "counts": {key: len(value) for key, value in sorted(classified.items())},
        "capabilities": records,
        "projections": projection,
        "locks": locks,
    }
    (out / "capability-authority.json").write_text(json.dumps(registry, indent=2, sort_keys=True) + "\n")
    (out / "deduplication.json").write_text(json.dumps(dedup, indent=2, sort_keys=True) + "\n")
    roots_by_class: dict[str, list[dict[str, object]]] = defaultdict(list)
    for root in home_roots:
        if isinstance(root, dict):
            source_class = str(root.get("classification", "project-local"))
            class_map = {
                "canonical-source": "active",
                "host-runtime": "projected",
                "backup/archive": "archived",
                "cache/vendored": "cached",
            }
            root = dict(root)
            root["classification"] = class_map.get(source_class, source_class)
            roots_by_class[str(root["classification"])].append(root)
    for classification in ("active", "projected", "project-local", "archived", "cached"):
        (indexes / f"{classification}.json").write_text(json.dumps({
            "schema": "capability-index/v1",
            "classification": classification,
            "generated_at": registry["generated_at"],
            "capabilities": classified.get(classification, []),
            "roots": roots_by_class.get(classification, []),
        }, indent=2, sort_keys=True) + "\n")
    (out / "projection-health.json").write_text(json.dumps(projection, indent=2, sort_keys=True) + "\n")
    (out / "lock-reconciliation.json").write_text(json.dumps(locks, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "registry": str(out / "capability-authority.json"),
        "counts": registry["counts"],
        "broken_links": len(projection["broken_links"]),
        "lock_drift_files": len(locks["drift"]),
        "exact_duplicate_groups": len(dedup["exact_hash_groups"]),
        "home_audit_reused": str(home_audit_path) if home_audit_path else None,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
