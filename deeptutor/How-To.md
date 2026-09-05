# DeepTutor — How-To (general local setup)

This is a **single, path-agnostic walkthrough** for running DeepTutor from a checkout of this repository. It follows the same phases as the upstream **Get Started** section in [`README.md`](./README.md) (Options **A**, **B**, and **C**), without assuming a particular folder on your machine.

**Also useful**

| Doc | When to use it |
|-----|----------------|
| [`README.md`](./README.md) | Full feature list, release notes, and authoritative install options. |
| [`RUNBOOK.md`](./RUNBOOK.md) | Same phases plus **mimic** shortcuts (`mimic-scripts/`, `DEEPTUTOR_ROOT`) if you use a standalone mirror layout. |
| [`MIMIC_OVERVIEW.md`](./MIMIC_OVERVIEW.md) | How a “mimic” tree relates to upstream and optional sync scripts. |
| [`ENV_KEYS.md`](./ENV_KEYS.md) | Environment variable reference. |
| [`SKILL.md`](./SKILL.md), [`AGENTS.md`](./AGENTS.md) | CLI and agent-oriented usage. |

**Reusable pattern:** prerequisites → enter repo → Python env → install (one path) → configure `.env` → run → verify → optional Docker.

---

## 0. Prerequisites (once)

| Check | Requirement |
|--------|--------------|
| `python3 --version` | **Python 3.11+** |
| `node --version` | **Node 20.9+** (for the `web/` UI) |
| `npm --version` | Bundled with Node |
| Provider | At least one **LLM API key** (tour or `.env` guides you) |

Windows without a compiler: see [`README.md`](./README.md) (Visual Studio Build Tools).

---

## 1. Go to the repository root

Use whichever path is true on your machine:

```bash
cd /path/to/My-Deep-Proprietary
```

If you use a **`DEEPTUTOR_ROOT`** convention (see [`RUNBOOK.md`](./RUNBOOK.md)):

```bash
cd "$DEEPTUTOR_ROOT"
```

---

## 2. Create and activate a Python environment

Pick **one** pattern (venv is typical on macOS or Linux):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

**Windows PowerShell:**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

**Conda:**

```bash
conda create -n deeptutor python=3.11
conda activate deeptutor
python -m pip install --upgrade pip
```

---

## 3. Install — choose **one** path

### Path A — Setup Tour (recommended for first run)

Interactive wizard: tooling checks, Python and Node dependencies, `.env`, optional TutorBot/Matrix/Manim depending on choices.

```bash
python scripts/start_tour.py
```

When asked for a profile, first-time users usually pick **Web app (recommended)**. Then continue at **step 5**.

### Path B — Manual

From the repository root, with your virtual environment active:

```bash
python -m pip install -e ".[server]"
```

Optional extras (only if you need them):

```bash
python -m pip install -e ".[tutorbot]"
# python -m pip install -e ".[tutorbot,matrix]"   # Matrix needs libolm
# python -m pip install -e ".[math-animator]"   # Manim + heavier system deps
# python -m pip install -e ".[all]"             # everything + dev tools
```

Frontend:

```bash
cd web && npm install && cd ..
```

### Path C — Mimic helper scripts (optional)

If your checkout includes `mimic-scripts/` and you use `set-root.sh` / `install-editable.sh`, follow [`RUNBOOK.md`](./RUNBOOK.md) for the exact commands.

---

## 4. Configure `.env`

```bash
cp .env.example .env
```

Edit `.env`. Minimum for **chat**:

- `LLM_BINDING`, `LLM_MODEL`, `LLM_API_KEY`, and usually `LLM_HOST`

For **Knowledge / RAG**, set the embedding variables (`EMBEDDING_*`). In **v1.3.0+**, **`EMBEDDING_HOST` must be the full embeddings URL** (see comments in [`.env.example`](./.env.example)).

Default ports unless you change them: backend **8001**, frontend **3782**.

---

## 5. Start the app (browser UI)

From the repository root, with the venv active:

```bash
python scripts/start_web.py
```

Keep that terminal open and open the URL printed in the log (typically [http://localhost:3782](http://localhost:3782)).

**Split terminals** (same behavior as README):

```bash
python -m deeptutor.api.run_server
```

```bash
cd web && npm run dev -- -p 3782
```

---

## 6. Quick CLI check (optional)

```bash
deeptutor run chat "Say OK in one word."
```

More CLI and automation context: [`SKILL.md`](./SKILL.md), [`AGENTS.md`](./AGENTS.md).

---

## 7. Docker (optional)

From the repository root after `.env` exists:

- Pull image: `docker compose -f docker-compose.ghcr.yml up -d`
- Or build locally: `docker compose up -d`

Then open [http://localhost:3782](http://localhost:3782). Details: README **Option C**.

---

## Mental model (one line per layer)

- **`deeptutor/`** — Python backend, orchestration, APIs  
- **`deeptutor_cli/`** — `deeptutor` CLI  
- **`web/`** — Next.js UI  
- **`.env`** — providers, ports, feature flags  
- **`scripts/start_web.py`** — typical one-command boot for **backend + frontend** together  

For CI, extra packages, and longer-form docs, this repo may also include **`docs/`**, **`packages/`**, and **`.github/`** — see those trees when you need workflows or developer documentation beyond this file.
