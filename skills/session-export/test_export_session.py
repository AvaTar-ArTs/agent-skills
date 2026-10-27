import importlib.util
import json
import sys


SCRIPT = __import__("pathlib").Path(__file__).with_name("scripts").joinpath("export_session.py")
SPEC = importlib.util.spec_from_file_location("export_session", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def test_resume_id_builds_compact_handoff_metadata():
    git = {"branch": "main", "head": "abc123", "status_lines": []}
    payload = MODULE.build_json_export("ecosystem audit", "workspace", git, resume_id="resume-abc123", depth="compact")

    assert payload["resume_id"] == "resume-abc123"
    assert payload["export_mode"] == "resume"
    assert payload["depth"] == "compact"
    assert payload["continuation_prompt"]
