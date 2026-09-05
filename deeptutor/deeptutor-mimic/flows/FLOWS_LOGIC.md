# Flows and logic — functional clone spec

Long-form Mermaid and file-level exploration: **`Guides/DeepTutor-ARCHITECTURE_MAP_MERMAID_AND_EXPLORATION.md`** (`PYTHON_MARKETPLACE_MASTER/Guides/...`).

This file is the **minimal logic contract** you must preserve to mimic DeepTutor.

---

## 1. Single spine (all entrypoints converge)

1. **CLI** (`deeptutor_cli`) builds a turn payload → **`DeepTutorApp`**.
2. **REST / WebSocket** (`deeptutor/api`) adapt HTTP/WS frames → same façade.
3. **`DeepTutorApp`** uses **`TurnRuntimeManager`** to run a turn: **`ChatOrchestrator.handle(UnifiedContext)`**.
4. Orchestrator resolves **`active_capability`** via **`CapabilityRegistry`**, constructs **`StreamBus`**, awaits **`BaseCapability.run(context, bus)`**.
5. Tools are invoked **inside** capabilities; names must exist on **`ToolRegistry`** or startup **`validate_tool_consistency`** in `deeptutor/api/main.py` fails.

**Invariant:** *One context shape in, streamed events out.* adapters only translate wire format.

---

## 2. Turn timeline (conceptual)

| Phase | What happens |
|-------|----------------|
| Adapter ingest | Parse user message, KB names, tool toggles, capability name / aliases. |
| Façade | Resolve capability; enrich **`UnifiedContext`**; allocate session/turn ids as needed. |
| Orchestrator | If capability unknown → error stream (or safe fallback to `chat` when configured). |
| Capability | Multi-stage pipeline; emits tokens, tool calls, errors via **`StreamBus`**. |
| Tool calls | `ToolRegistry` dispatch → RAG, search, code exec, etc. |
| Client | SSE / WS / Rich consumes **`StreamEvent`** sequence until terminal result. |

---

## 3. Registry drift (framework safety)

On API startup, **`validate_tool_consistency()`** compares:

- Every `tools_used` (or equivalent) on capability manifests from **`CapabilityRegistry`**
- Against **`tool_registry.list_tools()`**

If any referenced tool is missing → **configuration drift** error (hard fail). Mimic implementations must keep manifests and registrations aligned.

---

## 4. Dependency layers (behavioral mimic)

From `pyproject.toml` optional-dependencies:

- **`[cli]`** — LLM SDKs + LlamaIndex RAG + document parsers (attachments).
- **`[server]`** — FastAPI, uvicorn, websockets, auth helpers, logging repair utilities.
- **`[tutorbot]`** — Cron, MCP, channel SDKs (Telegram, Slack, etc.).
- **`[matrix]`** — Matrix channel (native `libolm` dependency).
- **`[math-animator]`** — Manim (system LaTeX/ffmpeg prerequisites).

Full mimic of *hosted* product = at least **`server`**; full mimic of *bots* = add **`tutorbot`**.

---

## 5. Operator flows (happy path)

1. **Configure:** copy `bundled/env.example` → `$DEEPTUTOR_ROOT/.env`, set `LLM_*`, `EMBEDDING_*`, optional `SEARCH_*`.
2. **First run:** `python scripts/start_tour.py` (interactive setup).
3. **CLI check:** `deeptutor run chat "ping"` with `--format json` for machine verification.
4. **API check:** `deeptutor serve` or `scripts/start_web.py` → hit health/docs → unified WS if UI depends on it.

---

## 6. Extension points (same as upstream)

- **New tool:** implement `BaseTool`, register in tool registry/bootstrap.
- **New capability:** implement `BaseCapability`, register manifest + class path.
- **New HTTP route:** router under `deeptutor/api/routers/`, mount in `main.py` (follow existing auth pattern).

Bundled **`AGENTS.md`** shows minimal plugin manifest + capability class pattern.
