#!/usr/bin/env python3
"""Export and search local Cline session JSON as markdown."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import re
from pathlib import Path
from typing import Any


HOME = Path.home()
DEFAULT_SOURCE = HOME / ".cline" / "data" / "sessions"
DEFAULT_OUT = HOME / ".cline" / "chat-history"
TRACKING_NAME = ".exported_sessions.json"


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


def session_dirs(source: Path) -> list[Path]:
    if not source.exists():
        return []
    return sorted([p for p in source.iterdir() if p.is_dir()])


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


def output_path(out: Path, meta: dict[str, Any], messages_doc: dict[str, Any], messages: list[dict[str, Any]]) -> Path:
    session_id = meta.get("session_id") or messages_doc.get("sessionId") or "unknown-session"
    started = meta.get("started_at") or messages_doc.get("updated_at") or ""
    date = str(started)[:10] if started else "undated"
    title = meta.get("metadata", {}).get("title") or meta.get("prompt") or first_user_text(messages) or session_id
    return out / f"{date}_{safe_slug(str(session_id), 'session')}_{safe_slug(str(title))}.md"


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


def iter_loaded(source: Path):
    for session_dir in session_dirs(source):
        try:
            meta, messages_doc, message_path = load_session(session_dir)
        except Exception as exc:
            yield session_dir, None, None, None, exc
            continue
        yield session_dir, meta, messages_doc, message_path, None


def cmd_export(args: argparse.Namespace) -> int:
    source = Path(args.source).expanduser()
    out = Path(args.out).expanduser()
    tracking = load_tracking(out)
    exported = skipped = failed = 0
    for session_dir, meta, messages_doc, message_path, exc in iter_loaded(source):
        if exc:
            failed += 1
            print(f"FAIL {session_dir}: {exc}")
            continue
        assert meta is not None and messages_doc is not None and message_path is not None
        sid = str(meta.get("session_id") or messages_doc.get("sessionId") or session_dir.name)
        digest = session_hash(message_path)
        if not args.force and tracking.get(sid) == digest:
            skipped += 1
            continue
        messages = messages_doc.get("messages", [])
        target = output_path(out, meta, messages_doc, messages)
        if args.dry_run:
            print(f"WOULD {sid} -> {target}")
        else:
            out.mkdir(parents=True, exist_ok=True)
            target.write_text(render_markdown(meta, messages_doc, messages), encoding="utf-8")
            tracking[sid] = digest
            print(f"WROTE {target}")
        exported += 1
    if not args.dry_run:
        save_tracking(out, tracking)
    print(f"exported={exported} skipped={skipped} failed={failed}")
    return 0 if failed == 0 else 1


def cmd_list(args: argparse.Namespace) -> int:
    source = Path(args.source).expanduser()
    rows = []
    for session_dir, meta, messages_doc, _message_path, exc in iter_loaded(source):
        if exc:
            rows.append((session_dir.name, "ERROR", str(exc)))
            continue
        assert meta is not None and messages_doc is not None
        messages = messages_doc.get("messages", [])
        title = meta.get("metadata", {}).get("title") or first_user_text(messages)
        rows.append((meta.get("started_at") or messages_doc.get("updated_at") or "", meta.get("session_id") or session_dir.name, title))
    for started, sid, title in sorted(rows, reverse=True)[: args.limit]:
        print(f"{started}\t{sid}\t{str(title).replace(chr(10), ' ')[:120]}")
    return 0


def cmd_search(args: argparse.Namespace) -> int:
    source = Path(args.source).expanduser()
    needle = args.query.lower()
    hits = 0
    for session_dir, meta, messages_doc, _message_path, exc in iter_loaded(source):
        if exc:
            continue
        assert meta is not None and messages_doc is not None
        haystack = json.dumps({"meta": meta, "messages": messages_doc.get("messages", [])}, ensure_ascii=False).lower()
        if needle in haystack:
            hits += 1
            title = meta.get("metadata", {}).get("title") or first_user_text(messages_doc.get("messages", []))
            print(f"{meta.get('started_at', '')}\t{meta.get('session_id') or session_dir.name}\t{str(title).replace(chr(10), ' ')[:120]}")
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
        p.add_argument("--source", default=str(DEFAULT_SOURCE))
        if name == "export":
            p.add_argument("--out", default=str(DEFAULT_OUT))
            p.add_argument("--dry-run", action="store_true")
            p.add_argument("--force", action="store_true")
            p.set_defaults(func=cmd_export)
        elif name == "search":
            p.add_argument("query")
            p.set_defaults(func=cmd_search)
        elif name == "latest":
            p.set_defaults(func=cmd_latest)
        else:
            p.add_argument("--limit", type=int, default=20)
            p.set_defaults(func=cmd_list)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
