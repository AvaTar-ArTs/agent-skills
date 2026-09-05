# DeepTutor — How-To (local setup)

**Using-superpowers:** Treat this as a **structured walkthrough** (clear phases, no guessing). Steps match the repo’s own **Get Started** flow in [`README.md`](./README.md) (**Option A** / **Option B** / **Option C**), adapted so **your tree can live at** `/Users/steven/Downloads/Compressed/DeepTutor-main` (or any clone — use `cd` to your root).

**Reuse elsewhere:** Same phase pattern works for other projects: **0 prerequisites → 1 enter repo → 2 language env → 3 install profile → 4 config → 5 run → 6 verify → 7 optional container**.

---

## 0. Prerequisites (once)

| Check | Requirement |
|--------|--------------|
| `python3 --version` | **Python 3.11+** |
| `node --version` | **Node 20.9+** (needed for local **web** UI) |
| `npm --version` | Comes with Node |
| Money/key | At least one **LLM API key** (tour or `.env` walks you through providers) |

Windows without a compiler: see [`README.md`](./README.md) (Visual Studio Build Tools).

---

## 1. Go to the project

A zip checkout counts the same as a `git clone`:

```bash
cd /Users/steven/Downloads/Compressed/DeepTutor-main
```

Or any path:

```bash
cd /path/to/DeepTutor
```

(Optional later: `python scripts/update.py` when you want to sync with Git — see README.)

---

## 2. Create and activate a Python environment

Pick **one** pattern (venv is typical on macOS):

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

## 3. Install software — choose **one** path

### Path **A — Setup Tour** (recommended by upstream)

Runs an interactive wizard: checks tooling, installs Python + Node deps, writes `.env`, optional TutorBot/Matrix/Manim.

```bash
python scripts/start_tour.py
```

When it asks for a profile, first-time users usually pick **Web app (recommended)**.

Then skip ahead to **step 5** for daily launch.

### Path **B — Manual** (you run each command yourself)

```bash
python -m pip install -e ".[server]"
```

Optional extras (only if you need them):

```bash
python -m pip install -e ".[tutorbot]"
# python -m pip install -e ".[tutorbot,matrix]"   # Matrix needs libolm
# python -m pip install -e ".[math-animator]"      # Manim + heavy system deps
# python -m pip install -e ".[all]"                # everything + dev tools
```

Frontend:

```bash
cd web && npm install && cd ..
```

---

## 4. Configure `.env`

```bash
cp .env.example .env
```

Edit `.env`. Minimum to **chat**:

- `LLM_BINDING`, `LLM_MODEL`, `LLM_API_KEY`, and usually `LLM_HOST`

For **Knowledge / RAG**, also set embedding vars (`EMBEDDING_*`). Comments in [`.env.example`](./.env.example) spell out that **`EMBEDDING_HOST` must be the full embeddings URL** (v1.3.0+).

Default ports (unless you changed them): backend **8001**, frontend **3782**.

---

## 5. Start the app (browser UI)

From repo root, with venv active:

```bash
python scripts/start_web.py
```

Leave that terminal open; open the URL it prints (typically [http://localhost:3782](http://localhost:3782)).

**Manual split** (two terminals), same as README:

```bash
python -m deeptutor.api.run_server
```

```bash
cd web && npm run dev -- -p 3782
```

---

## 6. Quick CLI sanity check (optional)

```bash
deeptutor run chat "Say OK in one word."
```

More commands and agent-facing usage are in [`SKILL.md`](./SKILL.md) and [`AGENTS.md`](./AGENTS.md).

---

## 7. Docker instead (optional — Option C)

From repo root after `.env` exists:

- Pull image: `docker compose -f docker-compose.ghcr.yml up -d`
- Or build locally: `docker compose up -d`

Then open [http://localhost:3782](http://localhost:3782). Details stay in the same README **Option C** block.

---

## Mental model (one line per layer)

- **`deeptutor/`** — Python backend + orchestration + APIs  
- **`deeptutor_cli/`** — `deeptutor` CLI  
- **`web/`** — Next.js UI  
- **`.env`** — providers, ports, auth flags  
- **`scripts/start_web.py`** — usual way to boot **backend + frontend** together  

For **architecture** (flows, routers, Mermaid), if you keep a cross-repo atlas: `PYTHON_MARKETPLACE_MASTER/Guides/DeepTutor-ARCHITECTURE_MAP_MERMAID_AND_EXPLORATION.md`.
