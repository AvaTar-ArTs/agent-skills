#!/usr/bin/env python3
"""
Inspect Markdown content inside ~/.agents.

Outputs:
- ./tmp-csv/md-content-index.csv
- ./tmp-md/md-content-report.md

The goal is to expose useful content signals, not just filenames:
activation language, workflow rules, examples, tools/commands, tests, and
TDD posture.
"""

from __future__ import annotations

import argparse
import csv
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import datetime
from pathlib import Path


DEFAULT_ROOT = Path("/Users/steven/.agents")
SKIP_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    ".pytest_cache",
    "tmp",
    "tmp-csv",
    "tmp-md",
}

TOOL_PATTERNS = (
    "bash",
    "read",
    "edit",
    "write",
    "grep",
    "glob",
    "task",
    "todowrite",
    "webfetch",
    "websearch",
    "skill",
    "apply_patch",
    "rg",
    "jq",
    "git",
    "gh",
    "python",
    "node",
)


@dataclass
class MdRow:
    path: str
    kind: str
    name: str
    description: str
    line_count: int
    heading_count: int
    headings: str
    activation: str
    workflow: str
    hard_rules: str
    examples: int
    code_blocks: int
    tools: str
    slash_commands: str
    tdd_style: str
    test_mentions: int
    risk_flags: str
    quality_flags: str


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def compact(value: str, limit: int = 360) -> str:
    value = re.sub(r"\s+", " ", value or "").strip()
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "..."


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not match:
        return {}
    data: dict[str, str] = {}
    current: str | None = None
    for raw in match.group(1).splitlines():
        line = raw.rstrip()
        if not line.strip():
            continue
        if not line.startswith((" ", "\t")) and ":" in line:
            key, value = line.split(":", 1)
            current = key.strip()
            data[current] = value.strip().strip("'\"")
        elif current:
            data[current] = f"{data[current]} {line.strip().strip('\"')}".strip()
    return data


def strip_frontmatter(text: str) -> str:
    return re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S)


def iter_md_files(root: Path):
    for path in sorted(root.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        yield path


def classify_kind(path: Path, root: Path) -> str:
    rel = path.relative_to(root)
    parts = rel.parts
    if parts[0] == "skills" or path.name == "SKILL.md":
        return "skill"
    if parts[0] == "agents":
        return "agent"
    if parts[0] == "plugins":
        return "plugin-doc"
    if parts[0] == "deep-research":
        return "skill"
    return "doc"


def extract_headings(text: str) -> list[str]:
    headings = []
    for line in text.splitlines():
        match = re.match(r"^(#{1,4})\s+(.+?)\s*$", line)
        if match:
            headings.append(match.group(2).strip())
    return headings


def extract_section(text: str, heading_words: tuple[str, ...], limit: int = 520) -> str:
    lines = text.splitlines()
    capture = False
    bucket = []
    for line in lines:
        is_heading = line.lstrip().startswith("#")
        lower = line.lower()
        if is_heading and any(word in lower for word in heading_words):
            capture = True
            continue
        if capture and is_heading:
            break
        if capture:
            bucket.append(line)
    return compact("\n".join(bucket), limit)


def extract_activation(text: str, fm: dict[str, str]) -> str:
    if fm.get("description"):
        return compact(fm["description"])
    section = extract_section(text, ("when to use", "when activated", "activation", "trigger"))
    if section:
        return section
    match = re.search(r"(?im)^\s*(?:use when|when to use|trigger)\s*:?\s*(.+)$", text)
    return compact(match.group(1) if match else "")


def extract_workflow(text: str) -> str:
    section = extract_section(text, ("workflow", "process", "steps", "checklist", "procedure"))
    if section:
        return section
    numbered = []
    for line in text.splitlines():
        if re.match(r"^\s*\d+\.\s+", line):
            numbered.append(line.strip())
        if len(numbered) >= 5:
            break
    return compact(" ".join(numbered))


def extract_hard_rules(text: str) -> str:
    rules = []
    for line in text.splitlines():
        lower = line.lower()
        if any(term in lower for term in ("must", "never", "always", "required", "do not", "don't")):
            stripped = re.sub(r"^\s*[-*]\s*", "", line.strip())
            if stripped:
                rules.append(stripped)
        if len(rules) >= 5:
            break
    return compact(" | ".join(rules), 520)


def extract_tools(text: str) -> str:
    lower = text.lower()
    found = []
    for tool in TOOL_PATTERNS:
        if re.search(rf"\b{re.escape(tool)}\b", lower):
            found.append(tool)
    return ", ".join(found)


def extract_slash_commands(text: str) -> str:
    commands = sorted(set(re.findall(r"(?<!https:)(?<!http:)(?<!\w)/(?:[a-zA-Z][\w:-]*)", text)))
    return ", ".join(commands[:20])


def tdd_style(text: str) -> str:
    lower = text.lower()
    if any(term in lower for term in ("red-green-refactor", "red/green/refactor", "failing test first", "write a failing test")):
        return "strict TDD"
    if any(term in lower for term in ("test-driven development", "tests first", "test first", "tdd")):
        return "test-first"
    if any(term in lower for term in ("acceptance criteria", "verification", "validate", "run tests", "test coverage")):
        return "verification-oriented"
    return "not TDD-specific"


def risk_flags(text: str, rel_path: str) -> list[str]:
    lower = text.lower()
    flags = []
    if "api_key" in lower or "token" in lower or "secret" in lower or "password" in lower:
        flags.append("mentions secrets/auth")
    if "rm -rf" in lower or "delete" in lower or "destructive" in lower:
        flags.append("destructive ops")
    if "curl" in lower or "download" in lower or "install" in lower:
        flags.append("network/install ops")
    if "settings.json" in rel_path or "/fixtures/" in rel_path:
        flags.append("fixture/reference")
    return flags


def quality_flags(text: str, fm: dict[str, str], headings: list[str]) -> list[str]:
    flags = []
    desc = fm.get("description", "")
    if not desc:
        flags.append("missing frontmatter description")
    elif len(desc) < 35:
        flags.append("thin description")
    if "Use when working with:" in desc:
        flags.append("boilerplate trigger")
    if "example" not in text.lower():
        flags.append("no examples")
    if len(headings) < 3:
        flags.append("thin structure")
    if "verify" not in text.lower() and "test" not in text.lower():
        flags.append("weak verification")
    return flags


def analyze_file(path: Path, root: Path) -> MdRow:
    text = read_text(path)
    fm = parse_frontmatter(text)
    rel = str(path.relative_to(root))
    headings = extract_headings(text)
    body = strip_frontmatter(text)
    code_blocks = body.count("```") // 2
    test_mentions = len(re.findall(r"\btests?\b|\btdd\b|\bverification\b|\bvalidate\b", text, flags=re.I))
    name = fm.get("name") or (path.parent.name if path.name == "SKILL.md" else path.stem)
    return MdRow(
        path=rel,
        kind=classify_kind(path, root),
        name=compact(name, 120),
        description=compact(fm.get("description", "")),
        line_count=len(text.splitlines()),
        heading_count=len(headings),
        headings=compact("; ".join(headings[:12]), 520),
        activation=extract_activation(text, fm),
        workflow=extract_workflow(text),
        hard_rules=extract_hard_rules(text),
        examples=len(re.findall(r"\bexample[s]?\b", text, flags=re.I)),
        code_blocks=code_blocks,
        tools=extract_tools(text),
        slash_commands=extract_slash_commands(text),
        tdd_style=tdd_style(text),
        test_mentions=test_mentions,
        risk_flags=", ".join(risk_flags(text, rel)),
        quality_flags=", ".join(quality_flags(text, fm, headings)),
    )


def write_csv(rows: list[MdRow], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(asdict(rows[0]).keys()) if rows else [])
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


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


def table_line(cells: list[str]) -> str:
    return "| " + " | ".join(cell.replace("|", "\\|") for cell in cells) + " |"


def write_report(rows: list[MdRow], out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    by_kind = Counter(row.kind for row in rows)
    by_tdd = Counter(row.tdd_style for row in rows)
    dupes = defaultdict(list)
    for row in rows:
        dupes[(row.kind, row.name)].append(row.path)

    weak = [row for row in rows if "missing frontmatter description" in row.quality_flags or "boilerplate trigger" in row.quality_flags]
    strict = [row for row in rows if row.tdd_style in {"strict TDD", "test-first"}]
    tool_heavy = sorted(rows, key=lambda row: len(row.tools.split(", ")) if row.tools else 0, reverse=True)[:20]
    hard_rule_heavy = [row for row in rows if row.hard_rules][:30]
    high_value = [
        row for row in rows
        if row.kind == "skill"
        and row.workflow
        and row.activation
        and row.examples
        and row.tdd_style != "not TDD-specific"
    ][:40]

    lines = [
        "# ~/.agents Markdown Content Inspection",
        "",
        "Generated by `scripts/inspect_md_content.py`.",
        "",
        "## Summary",
        "",
        table_line(["Metric", "Value"]),
        table_line(["---", "---"]),
        table_line(["Markdown files inspected", str(len(rows))]),
        table_line(["Kinds", ", ".join(f"{k}: {v}" for k, v in by_kind.most_common())]),
        table_line(["TDD posture", ", ".join(f"{k}: {v}" for k, v in by_tdd.most_common())]),
        table_line(["Weak trigger/description candidates", str(len(weak))]),
        "",
        "## Most Useful Skill Content Candidates",
        "",
        table_line(["name", "tdd_style", "why useful", "path"]),
        table_line(["---", "---", "---", "---"]),
    ]
    for row in high_value[:25]:
        why = compact("; ".join(part for part in (row.activation, row.workflow) if part), 180)
        lines.append(table_line([row.name, row.tdd_style, why, row.path]))

    lines += [
        "",
        "## Duplicate Names To Review",
        "",
        table_line(["kind", "name", "count", "paths"]),
        table_line(["---", "---", "---", "---"]),
    ]
    for (kind, name), paths in sorted(dupes.items(), key=lambda item: (item[0][0], item[0][1].lower())):
        if len(paths) > 1:
            lines.append(table_line([kind, name, str(len(paths)), "; ".join(paths[:6])]))

    lines += [
        "",
        "## Weak Trigger / Routing Candidates",
        "",
        table_line(["kind", "name", "flags", "path"]),
        table_line(["---", "---", "---", "---"]),
    ]
    for row in weak[:80]:
        lines.append(table_line([row.kind, row.name, row.quality_flags, row.path]))

    lines += [
        "",
        "## TDD/Test-First Content",
        "",
        table_line(["kind", "name", "tdd_style", "test_mentions", "path"]),
        table_line(["---", "---", "---", "---", "---"]),
    ]
    for row in strict[:80]:
        lines.append(table_line([row.kind, row.name, row.tdd_style, str(row.test_mentions), row.path]))

    lines += [
        "",
        "## Tool-Heavy Content",
        "",
        table_line(["kind", "name", "tools", "path"]),
        table_line(["---", "---", "---", "---"]),
    ]
    for row in tool_heavy:
        lines.append(table_line([row.kind, row.name, row.tools, row.path]))

    lines += [
        "",
        "## Hard Rule Samples",
        "",
        table_line(["kind", "name", "rules", "path"]),
        table_line(["---", "---", "---", "---"]),
    ]
    for row in hard_rule_heavy:
        lines.append(table_line([row.kind, row.name, row.hard_rules, row.path]))

    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Inspect Markdown content in ~/.agents.")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--csv", type=Path, default=None)
    parser.add_argument("--report", type=Path, default=None)
    args = parser.parse_args()

    root = args.root.resolve()
    csv_path = args.csv or (Path.cwd() / "tmp-csv" / "md-content-index.csv")
    report_path = args.report or (Path.cwd() / "tmp-md" / "md-content-report.md")

    rows = [analyze_file(path, root) for path in iter_md_files(root)]
    rows.sort(key=lambda row: (row.kind, row.name.lower(), row.path))
    write_csv(rows, csv_path)
    append_csv_changelog(csv_path, len(rows), "Regenerated Markdown content inspection index.")
    write_report(rows, report_path)
    print(f"inspected {len(rows)} markdown files")
    print(f"csv -> {csv_path}")
    print(f"report -> {report_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
