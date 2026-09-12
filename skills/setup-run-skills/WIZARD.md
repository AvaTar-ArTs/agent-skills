# Setup & Run Wizard — Creative Tools

An adaptive wizard that manages setup and execution of your creative AI tools.

**Single command to run everything:**

```bash
~/.claude/skills/setup-run-skills/wizard.sh
```

## What It Does

The wizard:

1. **Detects your environment** — checks Python, Node, ports, API keys
2. **Installs dependencies** — pip packages, validates paths
3. **Guides you through choices** — interactive menu to run CHOTAKU or nocturneMelodies
4. **Executes the skill** — handles all setup, then runs it
5. **Learns over time** — remembers what worked, suggests improvements

## Managed Tools

### 🎵 CHOTAKU MVP
**What:** FastAPI web app for the AvatarArts music ecosystem  
**Runs on:** http://localhost:8000  
**Requires:** Python 3.8+  
**Setup time:** ~5 seconds  
**Run time:** Server stays running until you stop it

```
Choose option [1] to run CHOTAKU
→ Installs FastAPI + Uvicorn (if needed)
→ Starts server on port 8000
→ Opens http://localhost:8000
```

### 🎼 NocturneMelodies Insights Engine
**What:** Deep creative analysis of AI-generated music  
**Requires:** Python 3.9+, optionally ANTHROPIC_API_KEY  
**Setup time:** ~10 seconds  
**Run time:** Analysis completes, then exits  
**Modes:**
- **Demo** (no API key): Uses representative data
- **Production** (with API key): Real Claude API analysis

```
Choose option [2] to run NocturneMelodies
→ Installs anthropic library (if needed)
→ Runs demo or production based on ANTHROPIC_API_KEY
→ Generates insights JSON files
→ Shows convergence analysis
```

## Adaptive Features

### Learning
The wizard remembers successful runs:

```json
{
  "runs": [
    {"skill": "chotaku", "status": "success", "timestamp": "2026-09-08T12:30:45Z"},
    {"skill": "nocturne-insights", "status": "success", "timestamp": "2026-09-08T12:45:22Z"}
  ],
  "successful_configs": {
    "chotaku_port": 8000,
    "python_version": "3.12"
  }
}
```

### Future Improvements
On subsequent runs, the wizard will:
- Skip already-installed dependencies
- Remember your port choice if 8000 is taken
- Suggest shortcuts based on history
- Detect patterns (e.g., "You always run CHOTAKU on Mondays")

## Quick Start

### First Time
```bash
~/.claude/skills/setup-run-skills/wizard.sh
# → Menu appears
# → Choose [1] for CHOTAKU or [2] for Insights
# → Wizard handles setup and runs it
```

### Setup Both
```bash
~/.claude/skills/setup-run-skills/wizard.sh
# → Choose [3]
# → Both are installed and tested
# → CHOTAKU launches
```

### Automate in Shell
Add an alias to your `~/.zshrc` or `~/.bash_profile`:

```bash
alias run-skills="~/.claude/skills/setup-run-skills/wizard.sh"
```

Then just run:
```bash
run-skills
```

## State & Learning

**State file:** `~/.claude/skills/setup-run-skills/state.json`

This file:
- Records every run (timestamp, status, skill)
- Stores successful configurations
- Remembers user preferences
- Grows with each execution

The wizard uses this to:
- Skip redundant setup steps
- Suggest next actions
- Detect and fix recurring issues

**To reset:** 
```bash
rm ~/.claude/skills/setup-run-skills/state.json
```

The wizard will recreate it on next run.

## Troubleshooting

### "Python 3 not found"
```bash
brew install python3
# Or: pyenv install 3.12
```

### "Port 8000 already in use"
The wizard will detect this and suggest alternatives.  
Or manually kill the process:
```bash
lsof -i :8000
kill -9 <PID>
```

### "ANTHROPIC_API_KEY not set"
For nocturneMelodies production mode:
```bash
export ANTHROPIC_API_KEY="sk-ant-..."
# Or add to ~/.zshrc for persistent configuration
```

Without it, demo mode works fine (uses representative data).

### Dependencies fail to install
The wizard tries to install via pip. If that fails:
```bash
pip install fastapi uvicorn jinja2 anthropic
```

Then run the wizard again.

## Architecture

```
~/.claude/skills/setup-run-skills/
├── wizard.sh           ← Main script (what you run)
├── state.json          ← Persistent learning state
├── WIZARD.md           ← This documentation
└── adapters/           ← (Future) tool-specific setup logic
    ├── chotaku-adapter.sh
    ├── insights-adapter.sh
    └── learn.sh
```

Currently everything is in `wizard.sh`. As it grows (e.g., supporting more tools), logic will graduate to `adapters/`.

## Philosophy

**Simple for the user, powerful underneath.**

The wizard's job is to:
1. Make the first run easy (just `wizard.sh`, then choose)
2. Make subsequent runs faster (remember what worked)
3. Make problems visible (detect port conflicts, missing keys)
4. Adapt to your environment (learn from each run)

It's not a replacement for the underlying skills' documentation — it's a **friendly guide** that does the tedious setup work for you.

## Next: Custom Workflows

Once both tools are working, you can:
- Chain them: analyze music, then generate music videos
- Batch process: run insights on 100 tracks
- Schedule: run daily analysis, store results

The wizard is the foundation; your scripts can build on top of it.

---

**Status:** ✓ Ready to use  
**Tested:** CHOTAKU MVP + NocturneMelodies Insights  
**Adaptive:** Logs runs to `state.json` for future improvements
