#!/usr/bin/env python3
"""
Export a compact catalog of ~/.agents assets.

    The output is intentionally smaller than the enriched scanner CSVs:
    name, use, details, and tdd_style are the primary fields.

    By default, output is staged in ./tmp-csv/ relative to the current
    working directory. CSVs are treated as living tables: rows may be added,
    removed, or changed, and each generation appends to a changelog beside
    the CSV.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


DEFAULT_ROOT = Path("/Users/steven/.agents")
DEFAULT_OUT_NAME = "agents-catalog.csv"

SKIP_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    ".pytest_cache",
}


@dataclass
class CatalogRow:
    name: str
    use: str
    details: str
    tdd_style: str
    kind: str
    path: str


def compact(value: str, limit: int = 260) -> str:
    value = re.sub(r"\s+", " ", value or "").strip()
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "..."


def read_text(path: Path, limit: int = 80_000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")[:limit]
    except OSError:
        return ""


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        return {}

    data: dict[str, str] = {}
    current_key: str | None = None
    for raw_line in match.group(1).splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        if not line.startswith((" ", "\t")) and ":" in line:
            key, value = line.split(":", 1)
            current_key = key.strip()
            data[current_key] = value.strip().strip("'\"")
        elif current_key:
            data[current_key] = f"{data[current_key]} {line.strip().strip('\"')}".strip()
    return data


def first_heading(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped.lstrip("#").strip()
    return ""


def first_use_sentence(text: str, fallback: str = "") -> str:
    frontmatter = parse_frontmatter(text)
    description = frontmatter.get("description", "")
    if description:
        return compact(description)

    for pattern in (
        r"(?im)^description:\s*(.+)$",
        r"(?im)^use(?:\s+when)?:\s*(.+)$",
        r"(?im)^when\s+to\s+use\s*:?\s*(.+)$",
        r"(?im)^##\s+when\s+(?:activated|to use).*?\n(.+?)(?:\n##|\Z)",
    ):
        match = re.search(pattern, text, flags=re.S)
        if match:
            return compact(match.group(1))

    return compact(fallback or first_heading(text))


def detail_from_markdown(text: str) -> str:
    headings = []
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            heading = stripped.lstrip("#").strip()
            if heading.lower() not in {"when activated", "when to use"}:
                headings.append(heading)
        if len(headings) >= 4:
            break

    if headings:
        return compact("; ".join(headings))

    body = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S).strip()
    for paragraph in re.split(r"\n\s*\n", body):
        if paragraph.strip() and not paragraph.lstrip().startswith("#"):
            return compact(paragraph)
    return ""


def has_test_signal(path: Path) -> bool:
    probes = [path]
    if path.is_file():
        probes.append(path.parent)
    for base in probes:
        if not base.exists():
            continue
        parent = base if base.is_dir() else base.parent
        for child in parent.rglob("*"):
            if any(part in SKIP_DIRS for part in child.parts):
                continue
            name = child.name.lower()
            if name.startswith("test_") or name.endswith(("_test.py", ".test.js", ".test.ts", ".spec.js", ".spec.ts")):
                return True
            if child.is_dir() and name in {"test", "tests", "__tests__"}:
                return True
    return False


def tdd_style(text: str, path: Path) -> str:
    lower = text.lower()
    if any(term in lower for term in ("red-green-refactor", "red/green/refactor", "test-driven development", "write failing test", "failing test first")):
        return "strict TDD"
    if any(term in lower for term in ("tdd", "tests first", "test first")):
        return "test-first"
    if has_test_signal(path):
        return "test-backed"
    if any(term in lower for term in ("verify", "validation", "checklist", "review", "acceptance criteria")):
        return "verification-oriented"
    return "not TDD-specific"


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def iter_agent_files(root: Path):
    agents_dir = root / "agents"
    if not agents_dir.exists():
        return
    for path in sorted(agents_dir.rglob("*.md")):
        if not should_skip(path):
            yield path


def iter_skill_files(root: Path):
    skills_dir = root / "skills"
    if not skills_dir.exists():
        return
    for path in sorted(skills_dir.rglob("SKILL.md")):
        if not should_skip(path):
            yield path


def iter_plugin_manifests(root: Path):
    plugins_dir = root / "plugins"
    if not plugins_dir.exists():
        return
    patterns = ("plugin.json", "gemini-extension.json")
    for path in sorted(plugins_dir.rglob("*")):
        if should_skip(path) or path.name not in patterns:
            continue
        if "tests" in path.parts and "fixtures" in path.parts:
            continue
        yield path


def row_from_markdown(path: Path, kind: str, root: Path) -> CatalogRow:
    text = read_text(path)
    frontmatter = parse_frontmatter(text)
    name = frontmatter.get("name") or path.parent.name if path.name == "SKILL.md" else frontmatter.get("name") or path.stem
    use = first_use_sentence(text, fallback=name)
    details = detail_from_markdown(text)
    return CatalogRow(
        name=compact(name, 120),
        use=use,
        details=details,
        tdd_style=tdd_style(text, path),
        kind=kind,
        path=str(path.relative_to(root)),
    )


def row_from_plugin(path: Path, root: Path) -> CatalogRow | None:
    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError:
        return None

    name = data.get("name") or path.parent.name
    description = data.get("description") or ""
    keywords = data.get("keywords") or []
    if isinstance(keywords, list):
        keyword_text = ", ".join(str(item) for item in keywords[:10])
    else:
        keyword_text = str(keywords)

    parent = path.parent
    if parent.name == ".claude-plugin":
        parent = parent.parent
    components = []
    for component in ("skills", "agents", "commands", "hooks", "mcpServers"):
        if component == "mcpServers":
            has_component = bool(data.get("mcpServers"))
        else:
            has_component = (parent / component).exists()
        if has_component:
            components.append(component)

    details = "; ".join(part for part in (keyword_text, f"components: {', '.join(components)}" if components else "") if part)
    manifest_text = json.dumps(data, sort_keys=True)
    return CatalogRow(
        name=compact(str(name), 120),
        use=compact(str(description or name)),
        details=compact(details),
        tdd_style=tdd_style(f"{manifest_text}\n{details}", parent),
        kind="plugin",
        path=str(path.relative_to(root)),
    )


def build_rows(root: Path) -> list[CatalogRow]:
    rows: list[CatalogRow] = []

    for path in iter_agent_files(root):
        rows.append(row_from_markdown(path, "agent", root))

    for path in iter_skill_files(root):
        rows.append(row_from_markdown(path, "skill", root))

    for path in iter_plugin_manifests(root):
        row = row_from_plugin(path, root)
        if row:
            rows.append(row)

    rows.sort(key=lambda row: (row.kind, row.name.lower(), row.path))
    return rows


def write_csv(rows: list[CatalogRow], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=["name", "use", "details", "tdd_style", "kind", "path"],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(row.__dict__)


def append_csv_changelog(out_path: Path, row_count: int, note: str) -> None:
    changelog = out_path.with_name(f"{out_path.stem}-CHANGELOG.md")
    stamp = datetime.now().astimezone().isoformat(timespec="seconds")
    entry = (
        f"## {stamp}\n\n"
        f"- CSV: `{out_path.name}`\n"
        f"- Rows written: {row_count}\n"
        f"- Change: {note}\n\n"
    )
    with changelog.open("a", encoding="utf-8") as fh:
        fh.write(entry)


def main() -> int:
    parser = argparse.ArgumentParser(description="Export a compact ~/.agents catalog CSV.")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="CSV destination. Defaults to ./tmp-csv/agents-catalog.csv in the current working directory.",
    )
    args = parser.parse_args()

    out_path = args.out or (Path.cwd() / "tmp-csv" / DEFAULT_OUT_NAME)
    rows = build_rows(args.root)
    write_csv(rows, out_path)
    append_csv_changelog(out_path, len(rows), "Regenerated compact agents catalog from current filesystem contents.")
    print(f"wrote {len(rows)} rows -> {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
