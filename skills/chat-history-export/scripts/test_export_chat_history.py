import importlib.util
import json
import sys
from pathlib import Path


SCRIPT = Path(__file__).with_name("export_chat_history.py")
SPEC = importlib.util.spec_from_file_location("export_chat_history", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_targeted_export_records_resume_id_and_source_session(tmp_path):
    source = tmp_path / "sessions"
    session = source / "resume-abc123"
    session.mkdir(parents=True)
    (session / "meta.json").write_text(json.dumps({
        "session_id": "resume-abc123",
        "started_at": "2026-10-08T12:00:00Z",
        "metadata": {"title": "Resume test"},
    }))
    (session / "resume-abc123.messages.json").write_text(json.dumps({
        "sessionId": "resume-abc123",
        "messages": [
            {"role": "user", "content": "Continue from here"},
            {"role": "assistant", "content": "Ready."},
        ],
    }))
    out = tmp_path / "out"

    args = MODULE.build_parser().parse_args([
        "export", "--tool", "cline", "--source", str(source), "--out", str(out),
        "--session", "resume-abc123", "--resume-id", "resume-abc123", "--format", "md",
    ])
    assert args.func(args) == 0

    exported = next(out.glob("*.md")).read_text()
    assert "- Resume ID: `resume-abc123`" in exported
    assert "- Session: `resume-abc123`" in exported
