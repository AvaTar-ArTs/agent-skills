# Secrets & Environment Variables

## Never commit secrets

- No `.env` files in the skill directory
- No API keys, cookies, or tokens in any YAML spec, reference, or adapter
- Adapters log **names** of missing env vars, never their values

## Loading env vars on the operator's machine

```bash
# Preferred (Steven's machine)
source ~/.env.d/loader.sh art-vision audio-music llm-apis openai

# Minimal fallback
set -a
[ -f "$HOME/.env.d/art-vision.env" ]   && . "$HOME/.env.d/art-vision.env"
[ -f "$HOME/.env.d/audio-music.env" ]  && . "$HOME/.env.d/audio-music.env"
[ -f "$HOME/.env.d/llm-apis.env" ]     && . "$HOME/.env.d/llm-apis.env"
[ -f "$HOME/.env.d/openai.env" ]       && . "$HOME/.env.d/openai.env"
set +a
```

Each shell command in Claude Code may start a fresh shell — prefix adapter invocations with the source command in the same shell invocation, or confirm vars are already exported in the session.

## Env var reference

| Backend | Required | Fallback | Optional |
|---------|----------|----------|----------|
| OpenAI Images | `OPENAI_API_KEY` | — | `OPENAI_BASE_URL` (default: https://api.openai.com) |
| Replicate | `REPLICATE_API_TOKEN` | `REPLICATE_API_KEY` | — |
| fal | `FAL_KEY` | `FAL_API_KEY` | — |
| ComfyUI | — (local) | — | `COMFYUI_BASE_URL` (default: http://127.0.0.1:8188) |
| ElevenLabs | `ELEVENLABS_API_KEY` | — | — |
| Suno unofficial | `SUNO_API_BASE` | — | `SUNO_API_KEY`, `SUNO_MODEL_VERSION` |

## Intake redaction (R7)

Before writing source files, `scripts/common/secrets.py` scans for and redacts:

| Pattern | Example |
|---------|---------|
| `sk-proj-…` | OpenAI project keys |
| `sk-ant-…` | Anthropic keys |
| `r8_…` | Replicate keys |
| `Bearer <token>` | Generic OAuth |
| `api_key=…` | Inline key assignments |
| `Authorization: …` | Header values |
| `__client=…`, `session=…` | Browser cookies |
| `BEGIN PRIVATE KEY` | Private key blocks |

Redacted to `[REDACTED]` with a warning message to the user.

## At the confirmation gate

Run `--dry-run` for each backend the run uses. Missing env vars cause exit 2 with a named error. Surface all missing vars at once before asking user to load them.
