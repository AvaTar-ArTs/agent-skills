# Quick Start — Run Your Creative Tools

## Simplest Way

```bash
~/.claude/skills/setup-run-skills/wizard.sh
```

That's it. The wizard handles everything.

---

## Even Simpler — Add Alias

Add this to `~/.zshrc` (or `~/.bash_profile` if using bash):

```bash
alias run-tools="~/.claude/skills/setup-run-skills/wizard.sh"
```

Then reload your shell:

```bash
source ~/.zshrc
```

Now just run:

```bash
run-tools
```

---

## What Happens

When you run the wizard, you'll see:

```
🎼 Creative Tools Setup & Run Wizard

Which skill would you like to run?

  1) CHOTAKU MVP — FastAPI music engine (web app on http://localhost:8000)
  2) NocturneMelodies Insights — Creative music analysis
  3) Both (setup both, then run CHOTAKU)
  4) Exit

Choose [1-4]:
```

### Option 1: CHOTAKU MVP
- Installs Python dependencies (FastAPI, Uvicorn)
- Starts web server on http://localhost:8000
- You can open it in a browser
- Server runs until you press Ctrl+C

### Option 2: NocturneMelodies Insights
- Checks for API key (optional)
- If no key: runs demo mode with example data
- If key set: runs real Claude analysis
- Generates JSON insights files
- Analysis completes and exits

### Option 3: Both
- Sets up both tools
- Runs CHOTAKU MVP
- Server stays running for you to use

---

## First Time Setup

The first run will:
1. Check Python is installed
2. Install any missing packages
3. Create a learning state file at `~/.claude/skills/setup-run-skills/state.json`
4. Run your chosen tool

Subsequent runs will be faster because it remembers what worked.

---

## Using the Tools

### CHOTAKU MVP (after choosing option 1 or 3)

Once running, you can:

```bash
# In another terminal while server is running:

# Check it's alive
curl http://localhost:8000/health

# View the homepage
open http://localhost:8000

# Or grab the HTML
curl -s http://localhost:8000/ | head
```

Press **Ctrl+C** in the wizard terminal to stop the server.

### NocturneMelodies Insights (after choosing option 2)

The analysis runs automatically and creates JSON files:

```
~/.claude/skills/run-nocturne-insights/insights/
├── painted-white_usesuno.com_analysis.json
├── the-dead-galaxy_usesuno.com_analysis.json
└── convergence_analysis.json
```

View results:

```bash
cat ~/.claude/skills/run-nocturne-insights/insights/convergence_analysis.json | python -m json.tool
```

---

## Optional: Set API Key for Production Insights

For deeper AI analysis of your music, the wizard auto-loads API keys from `~/.env.d/`.

### Easiest Way: Create `~/.env.d/anthropic.env`

```bash
mkdir -p ~/.env.d
echo 'ANTHROPIC_API_KEY="sk-ant-..."' > ~/.env.d/anthropic.env
```

Next time you run the wizard:
```bash
run-tools
```

The wizard will auto-load your API key and enable production mode.

### Alternative: Set in Shell

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
run-tools
```

Or add to `~/.zshrc`:
```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.zshrc
source ~/.zshrc
```

### How It Works

1. Wizard starts → loads `~/.env.d/` files automatically
2. If ANTHROPIC_API_KEY is found → production mode enabled
3. If not found → demo mode used (still works great!)

No extra setup needed — the wizard handles it.

---

## Adaptive Learning

The wizard remembers successful runs. Each time you run it:

- It logs what worked
- It skips redundant setup
- It suggests next steps based on history

State is saved in: `~/.claude/skills/setup-run-skills/state.json`

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Python 3 not found" | `brew install python3` |
| "Port 8000 in use" | Kill: `lsof -i :8000 \| grep python \| awk '{print $2}' \| xargs kill -9` |
| "anthropic module not found" | `pip install anthropic` |
| "ANTHROPIC_API_KEY not set" | Demo mode works fine; for production, set the env var above |

---

## Done!

That's it. You now have:

✓ **CHOTAKU MVP** — Web app for the music ecosystem  
✓ **NocturneMelodies Insights** — AI analysis of your tracks  
✓ **Adaptive Wizard** — Handles setup and learns over time  

Next time, just run:

```bash
run-tools
```

(Or the full path if you didn't add the alias.)
