# Runbook — DeepTutor locally (structured + mimic shortcuts)

**Using-superpowers:** Full **phased walkthrough** below matches upstream **Get Started** ([`README.md`](./README.md) Options **A / B / C**). **`mimic-scripts/set-root.sh`** defaults **`DEEPTUTOR_ROOT`** to **this standalone folder** (override to point elsewhere).

Parent hub copy (dual paths, related docs): **[../How-To.md](../How-To.md)**.

---

## Phased walkthrough (any checkout)

### 0. Prerequisites (once)

| Check | Requirement |
|--------|--------------|
| `python3 --version` | **Python 3.11+** |
| `node --version` | **Node 20.9+** |
| `npm --version` | Bundled with Node |
| Provider | At least one **LLM API key** |

### 1. Go to the project

```bash
cd "$DEEPTUTOR_ROOT"    # or: cd /Users/steven/Downloads/Compressed/DeepTutor-main
```

Use **`mimic-scripts`** (defaults `DEEPTUTOR_ROOT` = this directory):

```bash
cd ~/PYTHON_MARKETPLACE_MASTER/MY_SETUP/deeptutor-mimic
source mimic-scripts/set-root.sh
```

(Optional git: `python scripts/update.py`.)

### 2. Python environment

```bash
cd "$DEEPTUTOR_ROOT"
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 3. Install — **one** path

**A — Setup Tour (recommended)**

```bash
python scripts/start_tour.py
```

→ pick **Web app (recommended)** → jump to **§5**.

**B — Manual**

```bash
python -m pip install -e ".[server]"
# Optional: .[tutorbot], .[tutorbot,matrix], .[math-animator], .[all]
cd web && npm install && cd ..
```

**Mimic one-liner** (default extra: `server`):

```bash
cd ~/PYTHON_MARKETPLACE_MASTER/MY_SETUP/deeptutor-mimic
source mimic-scripts/set-root.sh
./mimic-scripts/install-editable.sh          # or: DEEP_EXTRAS=all ./mimic-scripts/install-editable.sh
```

### 4. Configure `.env`

```bash
cp .env.example .env
# edit LLM_* ; for RAG set EMBEDDING_* (EMBEDDING_HOST = full URL, v1.3.0+)
```

From this standalone root:

```bash
source mimic-scripts/set-root.sh
test -f "$DEEPTUTOR_ROOT/.env" || cp "$DEEPTUTOR_ROOT/.env.example" "$DEEPTUTOR_ROOT/.env"
```

### 5. Start the app (browser UI)

```bash
cd "$DEEPTUTOR_ROOT"
python scripts/start_web.py
```

→ [http://localhost:3782](http://localhost:3782)

Split terminals:

```bash
python -m deeptutor.api.run_server
```

```bash
cd web && npm run dev -- -p 3782
```

**Mimic helpers:**

```bash
cd ~/PYTHON_MARKETPLACE_MASTER/MY_SETUP/deeptutor-mimic
source mimic-scripts/set-root.sh
./mimic-scripts/start-full-stack.sh
```

### 6. CLI sanity check (optional)

```bash
cd "$DEEPTUTOR_ROOT"
deeptutor run chat "Say OK in one word." --format json
deeptutor kb list
```

Agent docs in repo root: `SKILL.md`, `AGENTS.md`.

### 7. Docker (Option C)

```bash
cd "$DEEPTUTOR_ROOT"
docker compose -f docker-compose.ghcr.yml up -d
# or: docker compose up -d
```

Use **`docker-compose.yml` from `$DEEPTUTOR_ROOT`** so build context resolves; `bundled/` copies are for offline reference only.

---

## Framework note

If API install is correct, capability **tool drift** fails fast at server start — align manifests with `ToolRegistry` before shipping changes.

---

## TutorBot / channels

```bash
python -m pip install -e ".[tutorbot]"
```

(Matrix optional; secrets only in `.env`.)
