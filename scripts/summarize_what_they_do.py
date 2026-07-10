#!/usr/bin/env python3
"""
Create a readable "what this is / what this does" inventory for ~/.agents.

Default scope is active/local authoring material:
- agents/**/*.md
- skills/**/*.md
- deep-research/**/*.md

Plugin repository docs are intentionally excluded unless --include-plugins is
passed; there are thousands of upstream README/docs files there.
"""

from __future__ import annotations

import argparse
import csv
import re
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


@dataclass
class SummaryRow:
    name: str
    kind: str
    this_is: str
    this_does: str
    use_when: str
    steps: str
    tdd_angle: str
    possible_next_step: str
    path: str


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def compact(value: str, limit: int = 340) -> str:
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


def body_without_frontmatter(text: str) -> str:
    return re.sub(r"^---\n.*?\n---\n", "", text, flags=re.S).strip()


def headings(text: str) -> list[str]:
    found = []
    for line in text.splitlines():
        match = re.match(r"^(#{1,4})\s+(.+?)\s*$", line)
        if match:
            found.append(match.group(2).strip())
    return found


def first_heading(text: str) -> str:
    hs = headings(text)
    return hs[0] if hs else ""


def first_paragraph(text: str) -> str:
    body = body_without_frontmatter(text)
    for block in re.split(r"\n\s*\n", body):
        block = block.strip()
        if not block or block.startswith("#") or block.startswith(">"):
            continue
        return compact(block)
    return ""


def extract_section(text: str, words: tuple[str, ...], limit: int = 500) -> str:
    lines = text.splitlines()
    capture = False
    bucket: list[str] = []
    for line in lines:
        is_heading = line.lstrip().startswith("#")
        lower = line.lower()
        if is_heading and any(word in lower for word in words):
            capture = True
            continue
        if capture and is_heading:
            break
        if capture:
            bucket.append(line)
    return compact("\n".join(bucket), limit)


def extract_numbered_or_bulleted_steps(text: str, max_steps: int = 7) -> list[str]:
    steps = []
    in_relevant_section = False
    for line in text.splitlines():
        stripped = line.strip()
        lower = stripped.lower()
        if stripped.startswith("#") and any(word in lower for word in ("workflow", "process", "steps", "procedure", "how to", "using")):
            in_relevant_section = True
            continue
        if in_relevant_section and stripped.startswith("#"):
            if steps:
                break
            in_relevant_section = False

        match = re.match(r"^(?:\d+\.|[-*])\s+(.+)$", stripped)
        if match and (in_relevant_section or not steps):
            value = match.group(1).strip()
            if len(value) > 8 and not value.startswith("`"):
                steps.append(compact(value, 140))
        if len(steps) >= max_steps:
            break
    return steps


def classify_kind(path: Path, root: Path) -> str:
    rel = path.relative_to(root)
    if rel.parts[0] == "agents":
        return "agent"
    if rel.parts[0] == "skills" or path.name == "SKILL.md":
        return "skill"
    if rel.parts[0] == "deep-research":
        return "skill"
    if rel.parts[0] == "plugins":
        return "plugin-doc"
    return "doc"


def infer_this_is(kind: str, name: str, text: str) -> str:
    title = first_heading(text)
    lower = text.lower()
    if kind == "agent":
        return compact(f"{name} is an agent/persona for {title or name}.")
    if kind == "skill":
        if "workflow" in lower or "process" in lower:
            return compact(f"{name} is a skill that captures a repeatable workflow.")
        if "script" in lower or "cli" in lower or "command" in lower:
            return compact(f"{name} is a skill with tool or command guidance.")
        return compact(f"{name} is a skill for {title or name}.")
    if kind == "plugin-doc":
        return compact(f"{name} is documentation bundled inside a plugin/source package.")
    return compact(f"{name} is a Markdown reference document.")


def infer_this_does(text: str, fm: dict[str, str]) -> str:
    desc = fm.get("description", "")
    if desc and "Use when working with:" not in desc:
        return compact(desc)
    paragraph = first_paragraph(text)
    if paragraph:
        return compact(paragraph)
    hs = headings(text)
    if hs:
        return compact("Covers: " + "; ".join(hs[:5]))
    return ""


def infer_use_when(text: str, fm: dict[str, str]) -> str:
    desc = fm.get("description", "")
    if desc:
        return compact(desc)
    section = extract_section(text, ("when to use", "when activated", "activation", "trigger"))
    if section:
        return section
    match = re.search(r"(?im)^\s*(?:use when|when to use|trigger)\s*:?\s*(.+)$", text)
    return compact(match.group(1) if match else "")


def infer_tdd_angle(text: str) -> str:
    lower = text.lower()
    if any(term in lower for term in ("red-green-refactor", "failing test", "write a failing test")):
        return "Use strict RED-GREEN-REFACTOR: write the failing test/eval first, implement, then refactor."
    if "eval" in lower or "benchmark" in lower or "assertion" in lower:
        return "Use eval-first TDD: define prompts/assertions before changing the skill or output."
    if "test" in lower or "verify" in lower or "validation" in lower:
        return "Use verification TDD: define the expected check before changing behavior."
    return "Add a first test/eval if behavior should be changed; otherwise use checklist verification."


def infer_possible_next_step(text: str, steps: list[str], use_when: str) -> str:
    lower = text.lower()
    if "boilerplate" in lower or "use when working with:" in use_when:
        return "Rewrite trigger description in plain scenario language."
    if not steps:
        return "Add a short numbered workflow: 1. Trigger, 2. Inputs, 3. Actions, 4. Output, 5. Verification."
    if len(steps) < 5:
        return "Add one or two missing workflow steps, especially verification/output handling."
    if "test" not in lower and "verify" not in lower:
        return "Add a final verification/TDD step."
    return "Review whether the workflow needs a promotion/staging step."


def format_steps(steps: list[str]) -> str:
    if not steps:
        return ""
    return " ".join(f"{idx}. {step}" for idx, step in enumerate(steps, 1))


def iter_markdown(root: Path, include_plugins: bool):
    allowed = {"agents", "skills", "deep-research"}
    if include_plugins:
        allowed.add("plugins")
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        if rel.parts[0] not in allowed:
            continue
        if not include_plugins and rel.parts[0] == "plugins":
            continue
        yield path


def summarize(path: Path, root: Path) -> SummaryRow:
    text = read_text(path)
    fm = parse_frontmatter(text)
    rel = path.relative_to(root)
    kind = classify_kind(path, root)
    name = fm.get("name") or (path.parent.name if path.name == "SKILL.md" else path.stem)
    steps = extract_numbered_or_bulleted_steps(text)
    use_when = infer_use_when(text, fm)
    return SummaryRow(
        name=compact(name, 120),
        kind=kind,
        this_is=infer_this_is(kind, name, text),
        this_does=infer_this_does(text, fm),
        use_when=use_when,
        steps=format_steps(steps),
        tdd_angle=infer_tdd_angle(text),
        possible_next_step=infer_possible_next_step(text, steps, use_when),
        path=str(rel),
    )


def write_csv(rows: list[SummaryRow], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(asdict(rows[0]).keys()) if rows else [])
        writer.writeheader()
        for row in rows:
            writer.writerow(asdict(row))


def append_csv_changelog(path: Path, row_count: int, note: str) -> None:
    changelog = path.with_name(f"{path.stem}-CHANGELOG.md")
    stamp = datetime.now().astimezone().isoformat(timespec="seconds")
    entry = (
        f"## {stamp}\n\n"
        f"- CSV: `{path.name}`\n"
        f"- Rows written: {row_count}\n"
        f"- Change: {note}\n\n"
    )
    with changelog.open("a", encoding="utf-8") as fh:
        fh.write(entry)


def table_row(cells: list[str]) -> str:
    return "| " + " | ".join(compact(cell, 220).replace("|", "\\|") for cell in cells) + " |"


def write_md(rows: list[SummaryRow], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# What These Agents And Skills Do",
        "",
        "Generated from Markdown content by `scripts/summarize_what_they_do.py`.",
        "",
    ]
    for kind in ("skill", "agent", "doc", "plugin-doc"):
        group = [row for row in rows if row.kind == kind]
        if not group:
            continue
        lines += [
            f"## {kind.title()}s",
            "",
            table_row(["name", "this is", "this does", "steps / next step", "path"]),
            table_row(["---", "---", "---", "---", "---"]),
        ]
        for row in group:
            step_text = row.steps or row.possible_next_step
            lines.append(table_row([row.name, row.this_is, row.this_does, step_text, row.path]))
        lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Summarize what ~/.agents Markdown files are and do.")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT)
    parser.add_argument("--include-plugins", action="store_true")
    parser.add_argument("--csv", type=Path, default=None)
    parser.add_argument("--md", type=Path, default=None)
    args = parser.parse_args()

    root = args.root.resolve()
    csv_path = args.csv or (Path.cwd() / "tmp-csv" / "what-they-do.csv")
    md_path = args.md or (Path.cwd() / "tmp-md" / "what-they-do.md")

    rows = [summarize(path, root) for path in iter_markdown(root, args.include_plugins)]
    rows.sort(key=lambda row: (row.kind, row.name.lower(), row.path))
    write_csv(rows, csv_path)
    append_csv_changelog(csv_path, len(rows), "Regenerated what-this-is/what-this-does summary from Markdown content.")
    write_md(rows, md_path)
    print(f"wrote {len(rows)} rows")
    print(f"csv -> {csv_path}")
    print(f"md -> {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
