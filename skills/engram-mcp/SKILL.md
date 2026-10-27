---
name: engram-mcp
description: >-
  Use when the agent needs access to Engram MCP tools. Available tools: append_messages, create_conversation, delete_conversation, get_conversation, list_conversations, manage_subscription, memory_status, resolve_vault, search, vault_delete, and 4 more.
---

# Engram Tools

## How to Call Tools

```bash
python3 scripts/call-tool.py <tool_name> '<arguments_json>'
```

## Tools

### append_messages

Saves messages to the user's long-term memory, making them available in future sessions in this app and any other AI the user connects. Applicable when the user asks to remember or save something (a preference, a fact, a decision, a goal, project context), or under a standing request from the user to keep saving as the conversation continues. Stores messages verbatim, auto-chunked + embedded for search. conversation_id is optional: omit it to append to the user's default memory, or set it to group messages under a specific conversation. The response returns the conversation_id used. Stores only the messages passed in — it cannot fetch past or external chat history (bulk import is separate, via the Engram CLI). Not suitable for secrets (passwords, API keys, tokens, government IDs): stored text is searchable and resurfaces in future context; Engram's separate zero-knowledge encrypted vault is the store for credentials. Optionally accepts client-encrypted vault entries.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| conversation_id | string | No | Optional. Omit to append to the user's default memory; set to group messages under a specific conversation. |
| messages | array<object> | Yes | Messages to append |
| vault_entries | array<object> | No | Client-encrypted vault entries. Server stores these as opaque blobs — zero knowledge. |

**Example:**
```bash
python3 scripts/call-tool.py append_messages '{"conversation_id":"...","messages":[],"vault_entries":[]}'
```

---

### create_conversation

Create a new conversation and return its conversation_id, used to group subsequently appended messages under one topic. Memory is scoped to the user's account; on multi-seat team accounts, a stored conversation is visible to the whole team by default and can be restricted to its creator with visibility 'private'.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| agent_id | string | No | Agent identifier (e.g. "chatgpt") |
| metadata | object | No | Arbitrary metadata |
| tags | array<string> | No | Tags for filtering |
| title | string | No | Title for the conversation |
| visibility | string | No | Team accounts: 'private' keeps this conversation visible only to the seat that created it. Default 'shared' (org-wide). |

**Example:**
```bash
python3 scripts/call-tool.py create_conversation '{"agent_id":"...","metadata":{},"tags":[],"title":"...","visibility":"..."}'
```

---

### delete_conversation

Delete a conversation and all its messages, chunks, and vector embeddings.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| conversation_id | string | Yes | The conversation to delete |

**Example:**
```bash
python3 scripts/call-tool.py delete_conversation '{"conversation_id":"..."}'
```

---

### get_conversation

Get a conversation with its full verbatim messages. Supports pagination.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| conversation_id | string | Yes | The conversation to retrieve |
| message_limit | integer | No | Max messages to return |
| message_offset | integer | No | Message offset for pagination |

**Example:**
```bash
python3 scripts/call-tool.py get_conversation '{"conversation_id":"...","message_limit":0,"message_offset":0}'
```

---

### list_conversations

List conversations with filtering and sorting options.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| agent_id | string | No | Filter by agent ID |
| limit | integer | No | - |
| offset | integer | No | - |
| order | string | No | - |
| sort | string | No | - |
| tags | array<string> | No | Filter by tags |

**Example:**
```bash
python3 scripts/call-tool.py list_conversations '{"agent_id":"...","limit":0,"offset":0,"order":"...","sort":"...","tags":[]}'
```

---

### manage_subscription

View your current subscription or get a link to upgrade/manage your plan. Returns a Stripe Checkout URL for upgrades or a billing portal URL for existing subscribers. IMPORTANT: When this tool returns a URL, you MUST open it in the user's browser by running `open <url>` (macOS) or `xdg-open <url>` (Linux) — do not just display the URL as text.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| action | string | No | "status" — show current tier and limits. "upgrade" — get a checkout link to subscribe to Pro or Team. "portal" — get a link to manage an existing subscription. |
| plan | string | No | Target plan for upgrade. Defaults to "pro". Only used with action "upgrade". |
| quantity | number | No | Number of seats for team plan. Only used with action "upgrade" and plan "team". |

**Example:**
```bash
python3 scripts/call-tool.py manage_subscription '{"action":"...","plan":"...","quantity":0}'
```

---

### memory_status

Show how full the user's Engram memory is: lifetime storage used vs the plan's capacity, plus a monthly meter on plans that have one. Returns a ready-to-display progress bar string.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py memory_status '{}'
```

---

### resolve_vault

Retrieve encrypted vault entries by ID. Returns encrypted blobs — decryption happens client-side.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| vault_ids | array<string> | Yes | Vault entry IDs to resolve (e.g. vlt_abc123) |

**Example:**
```bash
python3 scripts/call-tool.py resolve_vault '{"vault_ids":[]}'
```

---

### search

Searches the user's long-term memory. Applicable when previously saved context is relevant to the current request — for example when the user references something from before ('what did we decide', 'like last time', 'my usual', a project/person/preference by name) or asks what is remembered about a topic. Hybrid search (semantic + keyword) across stored conversations. Each result includes a short chunk_summary, the full chunk_text snippet, conversation_title, tags, and relevance scores, best match first.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| conversation_id | string | No | Limit search to a specific conversation |
| limit | integer | No | Max results (default 5) |
| project | string | No | Filter by project name (matches conversation title prefix, case-insensitive). Use to avoid cross-project noise. |
| query | string | Yes | Search query text |
| tags | array<string> | No | Filter by conversation tags |

**Example:**
```bash
python3 scripts/call-tool.py search '{"conversation_id":"...","limit":0,"project":"...","query":"...","tags":[]}'
```

---

### vault_delete

Delete a named secret permanently. This action cannot be undone.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| name | string | Yes | Secret name to delete |

**Example:**
```bash
python3 scripts/call-tool.py vault_delete '{"name":"..."}'
```

---

### vault_get

Retrieve a named secret's encrypted blob. Decryption happens client-side with your vault key.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| name | string | Yes | Secret name to retrieve (e.g. DATABASE_URL) |

**Example:**
```bash
python3 scripts/call-tool.py vault_get '{"name":"..."}'
```

---

### vault_list

List all named secrets. Returns names and metadata only — never values or encrypted blobs.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py vault_list '{}'
```

---

### vault_set

Store a named secret. The value must be encrypted client-side before calling this tool. The server stores the encrypted blob — it never sees plaintext.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| encrypted_value | string | Yes | Base64-encoded AES-256-GCM ciphertext |
| iv | string | Yes | Base64-encoded initialization vector |
| name | string | Yes | Secret name (e.g. DATABASE_URL, OPENAI_KEY) |
| secret_type | string | No | Type of secret (e.g. api_key, connection_string, token) |

**Example:**
```bash
python3 scripts/call-tool.py vault_set '{"encrypted_value":"...","iv":"...","name":"...","secret_type":"..."}'
```

---

### whoami

Show which Engram account this connection is using — organization name, email, tier, and how you are authenticated. Use when unsure which account memories are being saved to or searched from.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py whoami '{}'
```

---

