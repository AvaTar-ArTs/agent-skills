#!/usr/bin/env python3
"""Audit the Codex runtime without reading session or credential contents."""

from __future__ import annotations

import argparse
import json
import os
import re
from collections import Counter
from pathlib import Path


SENSITIVE = {"auth.json", "history.jsonl", "config.toml", "hooks.json", "credentials.json", "token.json", "secrets.json"}
SKIP = {"sessions", "cache", "plugins", ".tmp", "tmp", "sqlite", "thread-writer-locks", "mcp-oauth-locks", "generated_images", "shell_snapshots"}


def files(root: Path, name: str) -> list[Path]:
    if not root.exists():
        return []
    return sorted(p for p in root.rglob(name) if p.is_file() and not any(part in SKIP for part in p.parts))


def broken_links(root: Path) -> list[str]:
    result = []
    for path in root.rglob("*"):
        if path.is_symlink() and not path.exists():
            result.append(str(path.relative_to(root)))
    return sorted(result)


def enabled_plugins(config: Path) -> list[str]:
    section = None
    result = []
    for line in config.read_text(encoding="utf-8", errors="replace").splitlines():
        match = re.match(r'\[plugins\."([^"]+)"\]', line)
        if match:
            section = match.group(1)
            continue
        if line.startswith("["):
            section = None
        if section and line.strip() == "enabled = true":
            result.append(section)
    return sorted(result)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--codex-home", type=Path, default=Path.home() / ".codex")
    parser.add_argument("--canonical", type=Path, default=Path.home() / ".agent-skills")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    codex = args.codex_home.expanduser().resolve()
    canonical = args.canonical.expanduser().resolve()
    agent_files = files(codex / "agents", "*.md")
    agent_names = Counter(p.stem for p in agent_files)
    skill_files = files(codex / "skills", "SKILL.md")
    report = {
        "schema": "codex-runtime-audit/v1",
        "codex_home": str(codex),
        "canonical_source": str(canonical),
        "projections": {
            "agents": {
                "path": str(codex / "agents"),
                "is_symlink": (codex / "agents").is_symlink(),
                "resolved": str((codex / "agents").resolve()) if (codex / "agents").exists() else None,
                "canonical_before_curation": (codex / "agents").is_symlink() and (codex / "agents").resolve() == canonical / "agents",
            },
            "superpowers": {
                "path": str(codex / "superpowers"),
                "healthy": (codex / "superpowers").is_symlink() and (codex / "superpowers").exists(),
                "resolved": str((codex / "superpowers").resolve()) if (codex / "superpowers").exists() else None,
            },
        },
        "counts": {
            "codex_local_skills": len(skill_files),
            "codex_visible_agents": len(agent_files),
            "canonical_skills": len(list((canonical / "skills").rglob("SKILL.md"))),
            "canonical_agents": len(list((canonical / "agents").rglob("*.md"))),
            "enabled_plugins": len(enabled_plugins(codex / "config.toml")),
        },
        "duplicate_agent_names": {name: count for name, count in sorted(agent_names.items()) if count > 1},
        "enabled_plugins": enabled_plugins(codex / "config.toml"),
        "broken_links": broken_links(codex),
        "sensitive_paths_excluded": sorted(str(p.relative_to(codex)) for p in codex.iterdir() if p.name in SENSITIVE),
        "canonical_agent_source": str(canonical / "agents"),
    }
    output = args.out
    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
