#!/usr/bin/env python3
"""Audit the active ~/.agent-skills runtime surface.

This intentionally reports active source separately from backups, exports,
generated catalogs, and the Deeptutor project so stale totals do not look like
runtime capabilities.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path


SKIP_PARTS = {
    ".git", ".venv", "__pycache__", "node_modules", "backups", "deeptutor",
    "tmp", "tmp-csv", "tmp-md", "docs", "memory",
}
SENSITIVE_NAMES = {".env", ".env.local", "auth_info.json", "credentials.json", "token.json", "tokens.json", "secrets.json", "cookie.json", "cookies.json", "history.jsonl"}
SENSITIVE_PARTS = {"auth", "authentication", "credential", "credentials", "secret", "secrets", "token", "tokens", "keychain", "cookies", "history", "histories", "sessions", "session", "private"}


def in_scope(path: Path) -> bool:
    lowered = {part.lower() for part in path.parts}
    return not any(part in SKIP_PARTS for part in path.parts) and path.name.lower() not in SENSITIVE_NAMES and not bool(lowered & SENSITIVE_PARTS)


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.S)
    if not match:
        return {}
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line[:1].isspace():
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip("'\"")
    return result


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def collect(root: Path, pattern: str) -> list[Path]:
    return sorted(path for path in root.rglob(pattern) if in_scope(path))


def metadata_report(paths: list[Path], root: Path) -> dict[str, object]:
    names: defaultdict[str, list[str]] = defaultdict(list)
    missing_frontmatter: list[str] = []
    missing_name: list[str] = []
    missing_description: list[str] = []
    hashes: defaultdict[str, list[str]] = defaultdict(list)
    for path in paths:
        text = read(path)
        data = frontmatter(text)
        relative = str(path.relative_to(root))
        if not data:
            missing_frontmatter.append(relative)
            continue
        if not data.get("name"):
            missing_name.append(relative)
        else:
            names[data["name"]].append(relative)
        if not data.get("description"):
            missing_description.append(relative)
        hashes[hashlib.sha256(text.encode()).hexdigest()].append(relative)
    duplicate_names = {key: value for key, value in names.items() if len(value) > 1}
    exact_duplicates = {key: value for key, value in hashes.items() if len(value) > 1}
    return {
        "count": len(paths),
        "missing_frontmatter": missing_frontmatter,
        "missing_name": missing_name,
        "missing_description": missing_description,
        "duplicate_names": duplicate_names,
        "exact_duplicates": exact_duplicates,
    }


def broken_links(root: Path) -> list[str]:
    result = []
    for path in root.rglob("*"):
        if path.is_symlink() and not path.exists():
            result.append(str(path.relative_to(root)))
    return sorted(result)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    skills = collect(root / "skills", "SKILL.md")
    skills += collect(root / "deep-research", "SKILL.md")
    agents = [path for path in collect(root / "agents", "*.md") if path.name != "README.md"]
    report = {
        "root": str(root),
        "skills": metadata_report(skills, root),
        "agents": metadata_report(agents, root),
        "broken_links": broken_links(root),
        "top_level_skill_directories": sorted(
            path.name for path in (root / "skills").iterdir() if path.is_dir()
        ),
    }
    print(json.dumps(report, indent=2 if args.pretty else None, sort_keys=True))


if __name__ == "__main__":
    main()
