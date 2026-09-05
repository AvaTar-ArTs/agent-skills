# Component inventory — everything that participates in runtime mimicry

All paths are relative to **`DEEPTUTOR_ROOT`** (see `SOURCE_OF_TRUTH.md`).

## Top-level repo

| Path | Role |
|------|------|
| `pyproject.toml` | Package name `deeptutor`, extras: `cli`, `server`, `tutorbot`, `matrix`, `math-animator`, `dev`, `all`. |
| `requirements/` | Flat requirement lists mirrored from extras (Docker/CI). |
| `scripts/` | `start_web.py`, `start_tour.py`, checks, codegen — **operators live here**. |
| `tests/` | Regression coverage for mimic parity when you change forks. |
| `web/` | Next.js app; talks to FastAPI via env (`NEXT_PUBLIC_*`, `BACKEND_PORT`). |
| `docker-compose.yml`, `Dockerfile` | Full-stack container mimic. |

## `deeptutor/` — framework spine

| Path | Role |
|------|------|
| `app/facade.py` | **`DeepTutorApp`**: `start_turn`, `stream_turn`, capability resolution. |
| `runtime/orchestrator.py` | **`ChatOrchestrator.handle`**: registry lookup → `StreamBus` → `capability.run`. |
| `runtime/registry/tool_registry.py` | Tool discovery; startup drift check compares capability manifests → tools. |
| `runtime/registry/capability_registry.py` | Capability manifests and classes. |
| `runtime/mode.py` | CLI vs SERVER run mode. |
| `core/context.py` | **`UnifiedContext`** — single turn payload shape. |
| `core/stream.py`, `core/stream_bus.py` | Streaming event protocol and fan-out. |
| `core/tool_protocol.py`, `core/capability_protocol.py` | Extension contracts. |
| `capabilities/` | Built-in multi-step modes (`chat`, `deep_solve`, `deep_question`, …). |
| `tools/builtin/` | Built-in tools (`rag`, `web_search`, `code_execution`, …). |
| `knowledge/` | KB/RAG pipelines used by tools. |
| `agents/` | Agent pipelines behind capabilities (chat, solve, research, …). |
| `api/` | FastAPI app (`main.py` loads env, **`validate_tool_consistency`**), routers, `unified_ws`. |
| `services/` | LLM, embedding, search, session, memory, auth, paths, config (`env_store.py`). |
| `tutorbot/` | Optional autonomous tutors + channels (extra `[tutorbot]`). |
| `multi_user/` | Multi-user API paths when enabled. |
| `config/` | YAML/loaders for features (incl. plugin name hints in loader). |

**Note:** `AGENTS.md` references `deeptutor/plugins/` for playground plugins; your tree may register extended capabilities via **`capabilities/`** and config loader instead — verify with `deeptutor plugin list` after install.

## `deeptutor_cli/`

Typer app: `deeptutor run`, `chat`, `kb`, `memory`, `serve`, `start`, etc. Entry: `deeptutor_cli/main.py` → same façade as HTTP.

## Minimum install slices for mimic

| Goal | Install |
|------|---------|
| CLI + RAG + providers | `pip install -e ".[cli]"` |
| + FastAPI + WS | `pip install -e ".[server]"` |
| + TutorBot / MCP / channels | `pip install -e ".[tutorbot]"` |
| Everything local | `pip install -e ".[all]"` |

## Frontend / API wiring

- Backend binds **`BACKEND_PORT`** (default 8001).
- Frontend binds **`FRONTEND_PORT`** (default 3782).
- `scripts/start_web.py` orchestrates both and syncs auth flags into `web/` env.

See **`ENV_KEYS.md`** for the canonical key list (`ENV_KEY_ORDER` in code).
