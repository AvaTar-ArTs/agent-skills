"""Export and search local AI session JSON as markdown.

Supports multiple AI tool formats:
- Cline (~/.cline/data/sessions)
- Claude Code (~/.claude/projects)
- Codex (~/.Codex/projects)
- Poolside (~/.config/poolside/trajectories) - NDJSON format
- Generic session directories with *.json and *.messages.json structure
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Generator


HOME = Path.home()

# Tool presets for source directories
TOOL_PRESETS = {
    "cline": (HOME / ".cline" / "data" / "sessions", HOME / ".cline" / "chat-history"),
    "claude": (HOME / ".claude" / "projects", HOME / ".claude" / "chat-history"),
    "codex": (HOME / ".Codex" / "projects", HOME / ".Codex" / "chat-history"),
    "pool": (HOME / "Library" / "Application Support" / "poolside" / "trajectories", HOME / ".config" / "poolside" / "chat-history"),
    "auto": (HOME / ".cline" / "data" / "sessions", HOME / ".cline" / "chat-history"),
}

DEFAULT_SOURCE = TOOL_PRESETS["auto"][0]
DEFAULT_OUT = TOOL_PRESETS["auto"][1]
TRACKING_NAME = ".exported_sessions.json"


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    """Read a JSONL file (JSON Lines format) into a list of dicts."""
    entries = []
    with path.open("r", encoding="utf-8", errors="replace") as fh:
        for line in fh:
            line = line.strip()
            if line:
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return entries


def extract_claude_messages(jsonl_entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Extract conversation messages from Claude Code JSONL entries."""
    messages = []
    for entry in jsonl_entries:
        if entry.get("type") in ("user", "assistant"):
            msg = entry.get("message", {})
            if msg:
                role = msg.get("role", entry.get("type"))
                content = msg.get("content", "")
                messages.append({
                    "role": role,
                    "content": content,
                    "ts": entry.get("timestamp", ""),
                    "modelInfo": {"id": msg.get("model", ""), "provider": "claude"} if msg.get("model") else None,
                })
    return messages


def extract_poolside_messages(ndjson_entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Extract conversation messages from Poolside trajectory NDJSON entries."""
    messages = []
    session_start_time = ""
    for entry in ndjson_entries:
        entry_type = entry.get("type", "")
        if entry_type == "session.start":
            session_start_time = entry.get("timestamp", "")
        elif entry_type == "session.input":
            payload = entry.get("session_input", {})
            prompt = payload.get("prompt", "")
            if prompt:
                messages.append({
                    "role": "user",
                    "content": prompt,
                    "ts": entry.get("timestamp", session_start_time),
                })
        elif entry_type == "turn.output":
            # Assistant response - the output field contains the text
            output = entry.get("turn_output", {})
            text = output.get("text", "")
            if text:
                messages.append({
                    "role": "assistant",
                    "content": text,
                    "ts": entry.get("timestamp", ""),
                })
    return messages


def get_tool_preset(tool: str) -> tuple[Path, Path]:
    """Get source and output paths for a tool preset."""
    if tool in TOOL_PRESETS:
        return TOOL_PRESETS[tool]
    # If source/out provided explicitly, use those
    return None, None


def read_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8", errors="replace") as fh:
        return json.load(fh)


def safe_slug(value: str, fallback: str = "session") -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = re.sub(r"[^A-Za-z0-9._ -]+", " ", value)
    value = re.sub(r"\s+", "-", value.strip())
    return (value[:80].strip("-._") or fallback).lower()


def ts_to_iso(value: Any) -> str:
    if value is None:
        return ""
    try:
        number = float(value)
    except (TypeError, ValueError):
        return str(value)
    if number > 10_000_000_000:
        number /= 1000
    return dt.datetime.fromtimestamp(number, tz=dt.timezone.utc).isoformat()


def text_from_content(content: Any) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts: list[str] = []
        for item in content:
            if isinstance(item, dict):
                if item.get("type") == "text" and item.get("text"):
                    parts.append(str(item["text"]))
                elif "text" in item:
                    parts.append(str(item["text"]))
                elif "input" in item:
                    parts.append("```json\n" + json.dumps(item["input"], indent=2, ensure_ascii=False) + "\n```")
                else:
                    parts.append("```json\n" + json.dumps(item, indent=2, ensure_ascii=False) + "\n```")
            else:
                parts.append(str(item))
        return "\n\n".join(parts)
    if content:
        return json.dumps(content, indent=2, ensure_ascii=False)
    return ""


def first_user_text(messages: list[dict[str, Any]]) -> str:
    for msg in messages:
        if msg.get("role") == "user":
            text = text_from_content(msg.get("content"))
            if text.strip():
                return text.strip()
    return ""


def session_dirs(source: Path, session_filter: str | None = None) -> list[Path]:
    if not source.exists():
        return []
    dirs = sorted([p for p in source.iterdir() if p.is_dir()])
    if session_filter:
        # Filter by session_id or directory name
        dirs = [d for d in dirs if session_filter in d.name or any(
            session_filter in str(read_json(f)) if f.suffix == ".json" and "messages" not in f.name
            else False for f in d.iterdir() if f.is_file() and f.suffix == ".json"
        )]
    return dirs


def claude_session_files(source: Path, session_filter: str | None = None) -> list[Path]:
    """Find Claude Code JSONL session files across all project directories."""
    if not source.exists():
        return []
    files = []
    for project_dir in sorted(source.iterdir()):
        if project_dir.is_dir():
            for jsonl_file in sorted(project_dir.glob("*.jsonl")):
                if session_filter is None or session_filter in jsonl_file.stem:
                    files.append(jsonl_file)
    return files


def poolside_trajectory_files(source: Path, session_filter: str | None = None) -> list[Path]:
    """Find Poolside trajectory NDJSON files directly in the trajectories directory."""
    if not source.exists():
        return []
    files = []
    for ndjson_file in sorted(source.glob("trajectory-*.ndjson")):
        if session_filter is None or session_filter in ndjson_file.stem:
            files.append(ndjson_file)
    return files


def load_session(path: Path) -> tuple[dict[str, Any], dict[str, Any], Path]:
    meta_files = sorted(path.glob("*.json"))
    message_files = sorted(path.glob("*.messages.json"))
    if not message_files:
        raise FileNotFoundError(f"missing messages JSON in {path}")
    message_path = message_files[0]
    meta_path = next((p for p in meta_files if p != message_path), None)
    meta = read_json(meta_path) if meta_path else {}
    messages = read_json(message_path)
    return meta, messages, message_path


def session_hash(message_path: Path) -> str:
    digest = hashlib.sha256()
    with message_path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def output_path(out: Path, meta: dict[str, Any], messages_doc: dict[str, Any], messages: list[dict[str, Any]], ext: str = "md", tool_hint: str = "cline") -> Path:
    session_id = meta.get("session_id") or messages_doc.get("sessionId") or "unknown-session"
    started = meta.get("started_at") or messages_doc.get("updated_at") or ""
    # Claude timestamps are ISO strings, Cline may be numeric
    if started and isinstance(started, str) and "T" in started:
        date = started[:10]
    else:
        date = str(started)[:10] if started else "undated"
    title = meta.get("metadata", {}).get("title") or meta.get("prompt") or first_user_text(messages) or session_id
    return out / f"{date}_{safe_slug(str(session_id), 'session')}_{safe_slug(str(title))}.{ext}"


def render_markdown(meta: dict[str, Any], messages_doc: dict[str, Any], messages: list[dict[str, Any]]) -> str:
    session_id = meta.get("session_id") or messages_doc.get("sessionId") or ""
    title = meta.get("metadata", {}).get("title") or meta.get("prompt") or first_user_text(messages) or session_id
    lines = [
        f"# {title}",
        "",
        "## Metadata",
        "",
        f"- Session: `{session_id}`",
        f"- Source: `{meta.get('source', '')}`",
        f"- Status: `{meta.get('status', '')}`",
        f"- Started: `{meta.get('started_at', '')}`",
        f"- Ended: `{meta.get('ended_at', messages_doc.get('updated_at', ''))}`",
        f"- Model: `{meta.get('model', '')}`",
        f"- Provider: `{meta.get('provider', '')}`",
        f"- CWD: `{meta.get('cwd', '')}`",
        "",
        "## Messages",
        "",
    ]
    for msg in messages:
        role = msg.get("role", "unknown")
        stamp = ts_to_iso(msg.get("ts"))
        lines.append(f"### {role} {stamp}".rstrip())
        model_info = msg.get("modelInfo")
        if model_info:
            lines.append("")
            lines.append(f"Model: `{model_info.get('id', '')}` Provider: `{model_info.get('provider', '')}`")
        text = text_from_content(msg.get("content")).strip()
        lines.append("")
        lines.append(text or "_No text content captured._")
        metrics = msg.get("metrics")
        if metrics:
            lines.append("")
            lines.append("Metrics:")
            for key, value in metrics.items():
                lines.append(f"- {key}: `{value}`")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_json(meta: dict[str, Any], messages_doc: dict[str, Any], messages: list[dict[str, Any]]) -> str:
    """Render session as formatted JSON."""
    output = {
        "metadata": {
            "session_id": meta.get("session_id") or messages_doc.get("sessionId"),
            "source": meta.get("source", ""),
            "status": meta.get("status", ""),
            "started_at": meta.get("started_at", ""),
            "ended_at": meta.get("ended_at", messages_doc.get("updated_at", "")),
            "model": meta.get("model", ""),
            "provider": meta.get("provider", ""),
            "cwd": meta.get("cwd", ""),
            "title": meta.get("metadata", {}).get("title") or meta.get("prompt") or first_user_text(messages) or meta.get("session_id"),
        },
        "messages": messages,
    }
    return json.dumps(output, indent=2, ensure_ascii=False) + "\n"


def load_tracking(out: Path) -> dict[str, str]:
    path = out / TRACKING_NAME
    if not path.exists():
        return {}
    try:
        data = read_json(path)
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def save_tracking(out: Path, tracking: dict[str, str]) -> None:
    out.mkdir(parents=True, exist_ok=True)
    (out / TRACKING_NAME).write_text(json.dumps(tracking, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def iter_loaded(source: Path, session_filter: str | None = None, tool_hint: str | None = None):
    """Load sessions from a source directory. Supports Cline, Claude, and Poolside formats."""
    # Load Cline-style session directories
    if tool_hint in ("cline", "auto", None):
        for session_dir in session_dirs(source, session_filter):
            try:
                meta, messages_doc, message_path = load_session(session_dir)
            except Exception as exc:
                yield session_dir, None, None, None, exc, "cline"
                continue
            yield session_dir, meta, messages_doc, message_path, None, "cline"
    
    # Load Claude-style JSONL files in project subdirectories
    if tool_hint in ("claude", "auto"):
        for jsonl_path in claude_session_files(source, session_filter):
            try:
                entries = read_jsonl(jsonl_path)
                messages = extract_claude_messages(entries)
                if messages:
                    first_entry = entries[0] if entries else {}
                    meta = {
                        "session_id": first_entry.get("sessionId", jsonl_path.stem),
                        "source": "claude",
                        "cwd": first_entry.get("cwd", ""),
                        "started_at": first_entry.get("timestamp", ""),
                    }
                    messages_doc = {"messages": messages}
                    yield jsonl_path, meta, messages_doc, jsonl_path, None, "claude"
            except Exception as exc:
                yield jsonl_path, None, None, None, exc, "claude"
                continue
    
    # Load Poolside NDJSON trajectory files
    if tool_hint in ("pool", "auto"):
        for ndjson_path in poolside_trajectory_files(source, session_filter):
            try:
                entries = read_jsonl(ndjson_path)
                messages = extract_poolside_messages(entries)
                if messages:
                    # Extract session ID from filename (trajectory-standalone_019f5b57-b9b9-7772-99b2-0397ab8fd61f.ndjson)
                    session_id = ndjson_path.stem.replace("trajectory-", "")
                    meta = {
                        "session_id": session_id,
                        "source": "poolside",
                        "started_at": entries[0].get("timestamp", "") if entries else "",
                    }
                    messages_doc = {"messages": messages}
                    yield ndjson_path, meta, messages_doc, ndjson_path, None, "pool"
            except Exception as exc:
                yield ndjson_path, None, None, None, exc, "pool"
                continue


def cmd_export(args: argparse.Namespace) -> int:
    # Apply tool preset if --tool specified without explicit --source/--out
    source = Path(args.source).expanduser() if args.source != str(DEFAULT_SOURCE) else get_tool_preset(args.tool)[0]
    out = Path(args.out).expanduser() if args.out != str(DEFAULT_OUT) else get_tool_preset(args.tool)[1]
    
    tracking = load_tracking(out)
    exported = skipped = failed = 0
    for session_path, meta, messages_doc, message_path, exc, tool_hint in iter_loaded(source, args.session, args.tool):
        if exc:
            failed += 1
            print(f"FAIL {session_path}: {exc}")
            continue
        assert meta is not None and messages_doc is not None and message_path is not None
        sid = str(meta.get("session_id") or messages_doc.get("sessionId") or session_path.name)
        digest = session_hash(message_path)
        if not args.force and tracking.get(sid) == digest:
            skipped += 1
            continue
        messages = messages_doc.get("messages", [])
        ext = args.format if args.format != "auto" else "md"
        target = output_path(out, meta, messages_doc, messages, ext, tool_hint)
        content = render_markdown(meta, messages_doc, messages) if ext == "md" else render_json(meta, messages_doc, messages)
        if args.dry_run:
            print(f"WOULD {sid} -> {target}")
        else:
            out.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            tracking[sid] = digest
            print(f"WROTE {target}")
        exported += 1
    if not args.dry_run:
        save_tracking(out, tracking)
    print(f"exported={exported} skipped={skipped} failed={failed}")
    return 0 if failed == 0 else 1


def cmd_list(args: argparse.Namespace) -> int:
    source = Path(args.source).expanduser() if args.source != str(DEFAULT_SOURCE) else get_tool_preset(args.tool)[0]
    rows = []
    for session_path, meta, messages_doc, _message_path, exc, _tool_hint in iter_loaded(source, args.session, args.tool):
        if exc:
            rows.append((session_path.name, "ERROR", str(exc)))
            continue
        assert meta is not None and messages_doc is not None
        messages = messages_doc.get("messages", [])
        title = meta.get("metadata", {}).get("title") or first_user_text(messages) or meta.get("session_id", "")
        rows.append((meta.get("started_at", "") or messages_doc.get("updated_at", ""), meta.get("session_id", "") or session_path.name, title))
    for started, sid, title in sorted(rows, reverse=True)[: args.limit]:
        print(f"{started}\t{sid}\t{str(title).replace(chr(10), ' ')[:120]}")
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    source = Path(args.source).expanduser() if args.source != str(DEFAULT_SOURCE) else get_tool_preset(args.tool)[0]
    needle = args.query.lower()
    hits = 0
    for session_path, meta, messages_doc, _message_path, exc, _tool_hint in iter_loaded(source, args.session, args.tool):
        if exc:
            continue
        assert meta is not None and messages_doc is not None
        haystack = json.dumps({"meta": meta, "messages": messages_doc.get("messages", [])}, ensure_ascii=False).lower()
        if needle in haystack:
            hits += 1
            title = meta.get("metadata", {}).get("title") or first_user_text(messages_doc.get("messages", [])) or meta.get("session_id", "")
            print(f"{meta.get('started_at', '')}\t{meta.get('session_id', '') or session_path.name}\t{str(title).replace(chr(10), ' ')[:120]}")
    print(f"hits={hits}")
    return 0


def cmd_latest(args: argparse.Namespace) -> int:
    args.limit = 1
    return cmd_list(args)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)
    for name in ("export", "list", "search", "latest"):
        p = sub.add_parser(name)
        p.add_argument("--tool", choices=["cline", "claude", "codex", "pool", "auto"], default="cline",
                       help="Tool preset: claude (~/.claude/projects), cline (default), codex (~/.Codex/projects)")
        p.add_argument("--source", default=str(DEFAULT_SOURCE), help="Source directory containing session folders")
        if name == "export":
            p.add_argument("--out", default=str(DEFAULT_OUT), help="Output directory for exported files")
            p.add_argument("--dry-run", action="store_true", help="Preview exports without writing files")
            p.add_argument("--force", action="store_true", help="Force re-export even if already exported")
            p.add_argument("--format", choices=["md", "json", "auto"], default="auto", help="Output format (md=markdown, json=json, auto=detect)")
            p.add_argument("--session", help="Filter to specific session by session_id or directory name substring")
            p.set_defaults(func=cmd_export)
        elif name == "search":
            p.add_argument("query", help="Search string to find in session content")
            p.add_argument("--session", help="Filter to specific session by session_id or directory name substring")
            p.set_defaults(func=cmd_search)
        elif name == "latest":
            p.add_argument("--session", help="Filter to specific session by session_id or directory name substring")
            p.set_defaults(func=cmd_latest)
        else:
            p.add_argument("--limit", type=int, default=20, help="Maximum number of sessions to list")
            p.add_argument("--session", help="Filter to specific session by session_id or directory name substring")
            p.set_defaults(func=cmd_list)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
