# Environment keys — configuration mimic

Canonical ordered list is **`ENV_KEY_ORDER`** in `deeptutor/services/config/env_store.py` on `DEEPTUTOR_ROOT`.

Copy **`bundled/env.example`** to `$DEEPTUTOR_ROOT/.env`** and fill values. Keys include:

## Ports & public URLs

- `BACKEND_PORT`, `FRONTEND_PORT`
- `NEXT_PUBLIC_API_BASE`, `NEXT_PUBLIC_API_BASE_EXTERNAL`

## Auth

- `AUTH_ENABLED`, `AUTH_SECRET`, `AUTH_TOKEN_EXPIRE_HOURS`, `AUTH_USERNAME`, `AUTH_PASSWORD_HASH`
- `NEXT_PUBLIC_AUTH_ENABLED`
- PocketBase (optional): `POCKETBASE_URL`, `POCKETBASE_PORT`, `POCKETBASE_ADMIN_EMAIL`, `POCKETBASE_ADMIN_PASSWORD`, `POCKETBASE_EXTERNAL_URL`

## LLM

- `LLM_BINDING`, `LLM_MODEL`, `LLM_API_KEY`, `LLM_HOST`, `LLM_API_VERSION`, `LLM_REASONING_EFFORT`

## Embeddings

- `EMBEDDING_BINDING`, `EMBEDDING_MODEL`, `EMBEDDING_API_KEY`, `EMBEDDING_HOST`, `EMBEDDING_DIMENSION`, `EMBEDDING_SEND_DIMENSIONS`, `EMBEDDING_API_VERSION`

## Provider-specific keys (when bindings require them)

- `SILICONFLOW_API_KEY`, `DASHSCOPE_API_KEY`, `COHERE_API_KEY`, `JINA_API_KEY`, `GEMINI_API_KEY`

## Search

- `SEARCH_PROVIDER`, `SEARCH_API_KEY`, `SEARCH_BASE_URL`, `SEARCH_PROXY`

Other modules read additional vars (e.g. `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `DISABLE_SSL_VERIFY`) — see `deeptutor/services/` greps when debugging provider failures.

**Rule:** Never commit a filled `.env`; only **`bundled/env.example`** belongs in git without secrets.
