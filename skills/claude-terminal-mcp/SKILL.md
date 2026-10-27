---
name: claude-terminal-mcp
description: >-
  Use when the agent needs access to Claude Terminal MCP tools. Available tools: app_info, chat_respond_permission, control_tower_agents, control_tower_interrupt, db_add_connection, db_describe_table, db_disconnect, db_export, db_list_connections, db_list_tables, and 128 more.
---

# Claude Terminal Tools

## How to Call Tools

```bash
python3 scripts/call-tool.py <tool_name> '<arguments_json>'
```

## Tools

### app_info

Get Claude Terminal app info: version, platform, uptime, data directory, project count.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py app_info '{}'
```

---

### chat_respond_permission

Respond to a pending permission request on a chat tab programmatically (allow / deny / always-allow). Only works when the tab status is `awaiting_permission`. For deny, `message` is sent back to the agent as feedback.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| action | string | Yes | Decision to send back to the agent |
| message | string | No | Optional feedback message (used when action=deny). |
| requestId | string | No | Optional explicit permission requestId (defaults to the current pending one). |
| tabId | string | Yes | Stable tab identifier of the chat tab |

**Example:**
```bash
python3 scripts/call-tool.py chat_respond_permission '{"action":"...","message":"...","requestId":"...","tabId":"..."}'
```

---

### control_tower_agents

List all active or recently active Claude sessions across all projects. Shows project name, session age, path, and activity recency. Use this to see what Claude is currently doing across your workspace.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| max_age_minutes | number | No | Only show sessions active within the last N minutes (default: 60) |

**Example:**
```bash
python3 scripts/call-tool.py control_tower_agents '{"max_age_minutes":0}'
```

---

### control_tower_interrupt

Send an interrupt signal (Ctrl+C) to all running Claude terminals for a specific project. Useful to stop a long-running operation without killing the session.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | Project name, ID, or path basename |

**Example:**
```bash
python3 scripts/call-tool.py control_tower_interrupt '{"project":"..."}'
```

---

### db_add_connection

Add a new database connection to Claude Terminal. Supports sqlite, mysql, mariadb, postgresql, mongodb, and redis. The connection is saved and immediately available for use.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| connectionString | string | No | MongoDB connection URI. Required for mongodb type. |
| database | string | No | Database name. For redis: DB index (default: 0). Not needed for sqlite. |
| filePath | string | No | Path to SQLite file. Required for sqlite type. |
| host | string | No | Hostname (default: localhost). Not needed for sqlite. |
| name | string | Yes | Display name for the connection (e.g. "My Production DB") |
| port | number | No | Port number. Defaults: mysql=3306, postgresql=5432, redis=6379. Not needed for sqlite. |
| type | string | Yes | Database type |
| username | string | No | Username. Not needed for sqlite or redis. |

**Example:**
```bash
python3 scripts/call-tool.py db_add_connection '{"connectionString":"...","database":"...","filePath":"...","host":"...","name":"...","port":0,"type":"...","username":"..."}'
```

---

### db_describe_table

Get detailed schema for a specific table: column names, types, primary keys, nullability, and defaults.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| connection | string | Yes | Connection name or ID |
| table | string | Yes | Table or collection name |

**Example:**
```bash
python3 scripts/call-tool.py db_describe_table '{"connection":"...","table":"..."}'
```

---

### db_disconnect

Disconnect from a database. Closes the active connection and clears it from cache. The next query will automatically reconnect. Useful when a connection is in a bad state.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| connection | string | Yes | Connection name or ID to disconnect (from db_list_connections) |

**Example:**
```bash
python3 scripts/call-tool.py db_disconnect '{"connection":"..."}'
```

---

### db_export

Execute a SQL query and return results as CSV or JSON. Useful for exporting data.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| connection | string | Yes | Connection name or ID |
| format | string | No | Output format (default: csv) |
| sql | string | Yes | SQL SELECT query to export |

**Example:**
```bash
python3 scripts/call-tool.py db_export '{"connection":"...","format":"...","sql":"..."}'
```

---

### db_list_connections

List all database connections configured in Claude Terminal. Returns connection name, type (sqlite/mysql/postgresql/mongodb/redis), and connection details. Call this first to discover available databases.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py db_list_connections '{}'
```

---

### db_list_tables

List tables (or MongoDB collections, or Redis databases) in a database connection, with their column names. Use filter to search by name.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| connection | string | Yes | Connection name or ID (from db_list_connections) |
| filter | string | No | Optional name filter (case-insensitive substring match) |

**Example:**
```bash
python3 scripts/call-tool.py db_list_tables '{"connection":"...","filter":"..."}'
```

---

### db_query

Execute a SQL query against a database connection. Supports SELECT, INSERT, UPDATE, DELETE. For Redis: use native commands (GET, SET, KEYS, etc.) or _REDIS_SCAN {dbIndex} {limit} {pattern?}. Results limited to 100 rows.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| connection | string | Yes | Connection name or ID |
| sql | string | Yes | SQL query to execute |

**Example:**
```bash
python3 scripts/call-tool.py db_query '{"connection":"...","sql":"..."}'
```

---

### db_reconnect

Force reconnect to a database. Closes the current connection (if any) and opens a fresh one, then pings to verify it works. Use this to recover from connection errors.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| connection | string | Yes | Connection name or ID to reconnect (from db_list_connections) |

**Example:**
```bash
python3 scripts/call-tool.py db_reconnect '{"connection":"..."}'
```

---

### db_remove_connection

Remove a database connection from Claude Terminal. Closes any active connection and deletes the configuration.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| connection | string | Yes | Connection name or ID to remove (from db_list_connections) |

**Example:**
```bash
python3 scripts/call-tool.py db_remove_connection '{"connection":"..."}'
```

---

### db_schema_full

Dump the complete database schema: all tables with columns, types, primary keys, foreign keys, and indexes. Returns everything in one call.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| connection | string | Yes | Connection name or ID |

**Example:**
```bash
python3 scripts/call-tool.py db_schema_full '{"connection":"..."}'
```

---

### db_stats

Get database statistics: row count per table, total rows, database size, and table count.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| connection | string | Yes | Connection name or ID |

**Example:**
```bash
python3 scripts/call-tool.py db_stats '{"connection":"..."}'
```

---

### discord_bot_status

Get Discord bot project info: detected library, language, version, and command count.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | No | Project name, ID, or folder name. Defaults to current project. |

**Example:**
```bash
python3 scripts/call-tool.py discord_bot_status '{"project":"..."}'
```

---

### discord_list_commands

Scan a Discord bot project for slash commands and prefix commands. Returns command names, descriptions, types, and file locations.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | No | Project name, ID, or folder name. Defaults to current project. |

**Example:**
```bash
python3 scripts/call-tool.py discord_list_commands '{"project":"..."}'
```

---

### errorlog_clear

Clear all error log entries and pattern alerts.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py errorlog_clear '{}'
```

---

### errorlog_entries

Get recent error log entries. Supports filtering by level (critical/warning/info), domain, and search text. Returns newest first, max 100 entries.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| domain | string | No | Filter by domain (e.g. "ipc:git", "service:workflow", "mcp", "uncaught") |
| level | string | No | Filter by severity level |
| limit | number | No | Max entries to return (default 50, max 100) |
| search | string | No | Search text in message, domain, or stack trace |

**Example:**
```bash
python3 scripts/call-tool.py errorlog_entries '{"domain":"...","level":"...","limit":0,"search":"..."}'
```

---

### errorlog_export

Export the full error log as a JSON object for bug reports. Includes stats, pattern alerts, and the last 500 entries.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py errorlog_export '{}'
```

---

### errorlog_patterns

Get recurring error patterns detected in the last hour. Shows errors that repeat 5+ times with frequency count.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py errorlog_patterns '{}'
```

---

### errorlog_stats

Get error log statistics: total count, critical/warning/info breakdown, pattern alerts count, top domains. Useful for a quick health check.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py errorlog_stats '{}'
```

---

### fivem_command

Send a command to a running FiveM server console (e.g., "ensure myresource", "restart myresource", "refresh").

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| command | string | Yes | Command to send to the FiveM server console |
| project | string | Yes | FiveM project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py fivem_command '{"command":"...","project":"..."}'
```

---

### fivem_ensure

Ensure (start/restart) a FiveM resource on the running server. Validates that the resource exists in the project before sending the ensure command.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | FiveM project name or ID |
| resource | string | Yes | Resource name to ensure |

**Example:**
```bash
python3 scripts/call-tool.py fivem_ensure '{"project":"...","resource":"..."}'
```

---

### fivem_list_resources

List all FiveM resources in a project. Scans the resources/ directory for fxmanifest.lua files and shows which are ensured in server.cfg.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | FiveM project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py fivem_list_resources '{"project":"..."}'
```

---

### fivem_read_manifest

Read and parse a FiveM resource manifest (fxmanifest.lua). Returns parsed fields (fx_version, scripts, dependencies) and raw content.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | FiveM project name or ID |
| resource | string | Yes | Resource name (folder name in resources/) |

**Example:**
```bash
python3 scripts/call-tool.py fivem_read_manifest '{"project":"...","resource":"..."}'
```

---

### fivem_resource_files

List files in a FiveM resource directory. Useful to see the structure of a resource (client/, server/, shared/ scripts, config files, etc.).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | FiveM project name or ID |
| resource | string | Yes | Resource name |

**Example:**
```bash
python3 scripts/call-tool.py fivem_resource_files '{"project":"...","resource":"..."}'
```

---

### fivem_server_cfg

Read and analyze server.cfg of a FiveM project. Returns ensured resources, server settings (hostname, tags, etc.), and raw content.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | FiveM project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py fivem_server_cfg '{"project":"..."}'
```

---

### fivem_start

Start a FiveM server for a project. Triggers the server start asynchronously in Claude Terminal.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | FiveM project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py fivem_start '{"project":"..."}'
```

---

### fivem_stop

Stop a running FiveM server for a project. Sends a graceful quit command.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | FiveM project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py fivem_stop '{"project":"..."}'
```

---

### kanban_add_column

Add a new column to a project's kanban board.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| color | string | No | Column color as hex (e.g. #8b5cf6). Default: #888888 |
| project | string | Yes | Project name, folder name, or ID |
| title | string | Yes | Column title |

**Example:**
```bash
python3 scripts/call-tool.py kanban_add_column '{"color":"...","project":"...","title":"..."}'
```

---

### kanban_add_task

Create a new kanban task in a project. Adds to the specified column (or the first column by default).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| column | string | No | Column id or title (default: first column) |
| description | string | No | Optional task description |
| dueDate | string | No | Due date in YYYY-MM-DD format |
| priority | string | No | Priority level: p0 (critical), p1 (high), p2 (medium), p3 (low) |
| project | string | Yes | Project name, folder name, or ID |
| title | string | Yes | Task title |

**Example:**
```bash
python3 scripts/call-tool.py kanban_add_task '{"column":"...","description":"...","dueDate":"...","priority":"...","project":"...","title":"..."}'
```

---

### kanban_archive

Archive all completed tasks (in the Done column) from the kanban board. Archived tasks are stored separately.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| column | string | No | Column to archive from (default: "Done") |
| project | string | Yes | Project name, folder name, or ID |

**Example:**
```bash
python3 scripts/call-tool.py kanban_archive '{"column":"...","project":"..."}'
```

---

### kanban_bulk_move

Move multiple kanban tasks to a target column at once.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| column | string | Yes | Target column id or title |
| project | string | Yes | Project name, folder name, or ID |
| tasks | string | Yes | Comma-separated task IDs or titles |

**Example:**
```bash
python3 scripts/call-tool.py kanban_bulk_move '{"column":"...","project":"...","tasks":"..."}'
```

---

### kanban_delete_column

Delete a kanban column. Tasks in this column are moved to the first available column.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| column | string | Yes | Column id or title to delete |
| project | string | Yes | Project name, folder name, or ID |

**Example:**
```bash
python3 scripts/call-tool.py kanban_delete_column '{"column":"...","project":"..."}'
```

---

### kanban_delete_task

Delete a kanban task permanently.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | Project name, folder name, or ID |
| task | string | Yes | Task id or title (substring match) |

**Example:**
```bash
python3 scripts/call-tool.py kanban_delete_task '{"project":"...","task":"..."}'
```

---

### kanban_filter

Filter kanban tasks by priority, due date, or column.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| column | string | No | Filter by column id or title |
| has_due_date | boolean | No | Filter tasks with (true) or without (false) a due date |
| overdue | boolean | No | Filter tasks past their due date |
| priority | string | No | Filter by priority level |
| project | string | Yes | Project name, folder name, or ID |

**Example:**
```bash
python3 scripts/call-tool.py kanban_filter '{"column":"...","has_due_date":true,"overdue":true,"priority":"...","project":"..."}'
```

---

### kanban_list_columns

List the kanban columns of a project with their task counts.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | Project name, folder name, or ID |

**Example:**
```bash
python3 scripts/call-tool.py kanban_list_columns '{"project":"..."}'
```

---

### kanban_list_tasks

List kanban tasks for a project. Optionally filter by column. Shows title, column, description, worktree, and session count.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| column | string | No | Optional column id or title to filter tasks |
| project | string | Yes | Project name, folder name, or ID |

**Example:**
```bash
python3 scripts/call-tool.py kanban_list_tasks '{"column":"...","project":"..."}'
```

---

### kanban_move_task

Move a kanban task to a different column.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| column | string | Yes | Target column id or title |
| project | string | Yes | Project name, folder name, or ID |
| task | string | Yes | Task id or title (substring match) |

**Example:**
```bash
python3 scripts/call-tool.py kanban_move_task '{"column":"...","project":"...","task":"..."}'
```

---

### kanban_rename_column

Rename a kanban column.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| column | string | Yes | Current column name or ID |
| project | string | Yes | Project name, folder name, or ID |
| title | string | Yes | New title for the column |

**Example:**
```bash
python3 scripts/call-tool.py kanban_rename_column '{"column":"...","project":"...","title":"..."}'
```

---

### kanban_search

Search kanban tasks across a project by title or description content.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | Project name, folder name, or ID |
| query | string | Yes | Search term (case-insensitive substring match) |

**Example:**
```bash
python3 scripts/call-tool.py kanban_search '{"project":"...","query":"..."}'
```

---

### kanban_stats

Get kanban board statistics: task counts per column, priorities distribution, overdue count.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | Project name, folder name, or ID |

**Example:**
```bash
python3 scripts/call-tool.py kanban_stats '{"project":"..."}'
```

---

### kanban_update_task

Update a kanban task fields: title, description, worktree path, priority, or due date.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| description | string | No | New description |
| dueDate | string | No | Due date in YYYY-MM-DD format (empty string to remove) |
| priority | string | No | Priority level (empty string to remove) |
| project | string | Yes | Project name, folder name, or ID |
| task | string | Yes | Task id or title (substring match) |
| title | string | No | New title |
| worktreePath | string | No | Linked git worktree path (empty string to unlink) |

**Example:**
```bash
python3 scripts/call-tool.py kanban_update_task '{"description":"...","dueDate":"...","priority":"...","project":"...","task":"...","title":"...","worktreePath":"..."}'
```

---

### marketplace_featured

Get featured/popular skills from the skills.sh marketplace.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | number | No | Maximum number of results (default: 10) |

**Example:**
```bash
python3 scripts/call-tool.py marketplace_featured '{"limit":0}'
```

---

### marketplace_install

Install a skill from the skills.sh marketplace into Claude Terminal.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| skill | string | Yes | Skill name or slug to install |

**Example:**
```bash
python3 scripts/call-tool.py marketplace_install '{"skill":"..."}'
```

---

### marketplace_installed

List all skills currently installed in Claude Terminal.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py marketplace_installed '{}'
```

---

### marketplace_search

Search for skills on the skills.sh marketplace.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | number | No | Maximum number of results (default: 10, max: 30) |
| query | string | Yes | Search query for skills |

**Example:**
```bash
python3 scripts/call-tool.py marketplace_search '{"limit":0,"query":"..."}'
```

---

### marketplace_uninstall

Uninstall a skill from Claude Terminal.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| skill | string | Yes | Skill name or slug to uninstall |

**Example:**
```bash
python3 scripts/call-tool.py marketplace_uninstall '{"skill":"..."}'
```

---

### mcp_registry_detail

Get detailed information about a specific MCP server from the registry.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| server | string | Yes | Server ID or name from the MCP registry |

**Example:**
```bash
python3 scripts/call-tool.py mcp_registry_detail '{"server":"..."}'
```

---

### mcp_registry_search

Search the official MCP server registry for MCP servers.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | number | No | Maximum number of results (default: 10) |
| query | string | Yes | Search query for MCP servers |

**Example:**
```bash
python3 scripts/call-tool.py mcp_registry_search '{"limit":0,"query":"..."}'
```

---

### notification_send

Send a desktop notification via Claude Terminal.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| body | string | Yes | Notification body text |
| title | string | Yes | Notification title |
| type | string | No | Notification type (default: info) |

**Example:**
```bash
python3 scripts/call-tool.py notification_send '{"body":"...","title":"...","type":"..."}'
```

---

### parallel_cancel_run

Cancel an active parallel run. Aborts all running tasks immediately.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| run | string | Yes | Run ID (full or partial) or goal substring |

**Example:**
```bash
python3 scripts/call-tool.py parallel_cancel_run '{"run":"..."}'
```

---

### parallel_cleanup_run

Clean up a completed parallel run: remove git worktrees, delete task branches, and remove from history. Use after merging or when results are no longer needed.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| run | string | Yes | Run ID (full or partial) or goal substring |

**Example:**
```bash
python3 scripts/call-tool.py parallel_cleanup_run '{"run":"..."}'
```

---

### parallel_list_runs

List parallel task runs for a project. Shows run ID, goal, phase, task count, duration, and branches. Runs decompose a goal into independent sub-tasks executed in parallel via git worktrees.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | number | No | Max runs to return (default: 10) |
| project | string | No | Project path to filter runs. Defaults to current project. |

**Example:**
```bash
python3 scripts/call-tool.py parallel_list_runs '{"limit":0,"project":"..."}'
```

---

### parallel_merge_run

Merge all completed task branches from a parallel run into a unified branch. Creates a temporary merge worktree, merges branches sequentially, and resolves conflicts via Claude. The merged branch is named parallel/<feature>/all.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| run | string | Yes | Run ID (full or partial) or goal substring |

**Example:**
```bash
python3 scripts/call-tool.py parallel_merge_run '{"run":"..."}'
```

---

### parallel_run_detail

Get detailed info about a specific parallel run: goal, phase, all tasks with their status, branches, worktree paths, and errors. Use run ID or goal substring to find a run.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| run | string | Yes | Run ID (full or partial) or goal substring |

**Example:**
```bash
python3 scripts/call-tool.py parallel_run_detail '{"run":"..."}'
```

---

### parallel_start_run

Start a new parallel task run. Claude decomposes the goal into independent sub-tasks, creates git worktrees, and executes them in parallel. The run starts asynchronously — use parallel_list_runs to check progress.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| auto_tasks | boolean | No | Let Claude decide the optimal number of tasks (overrides max_tasks) |
| effort | string | No | Effort level: low, medium, high, xhigh, max (default: high) |
| goal | string | Yes | Feature description to decompose into parallel tasks |
| main_branch | string | No | Base branch for worktrees (default: current branch) |
| max_tasks | number | No | Maximum number of parallel tasks (2-10, default: 4) |
| model | string | No | Claude model to use (default: claude-sonnet-4-6) |

**Example:**
```bash
python3 scripts/call-tool.py parallel_start_run '{"auto_tasks":true,"effort":"...","goal":"...","main_branch":"...","max_tasks":0,"model":"..."}'
```

---

### plugin_catalog

Browse available plugins from registered marketplaces.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| marketplace | string | No | Specific marketplace URL to browse. If omitted, lists all known marketplaces. |

**Example:**
```bash
python3 scripts/call-tool.py plugin_catalog '{"marketplace":"..."}'
```

---

### plugin_install

Install a Claude Code plugin. The installation runs asynchronously in Claude Terminal.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| marketplace | string | No | Optional marketplace URL to install from |
| plugin | string | Yes | Plugin name or URL to install |

**Example:**
```bash
python3 scripts/call-tool.py plugin_install '{"marketplace":"...","plugin":"..."}'
```

---

### plugin_list

List all Claude Code plugins currently installed.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py plugin_list '{}'
```

---

### plugin_uninstall

Uninstall a Claude Code plugin.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| plugin | string | Yes | Plugin name to uninstall |

**Example:**
```bash
python3 scripts/call-tool.py plugin_uninstall '{"plugin":"..."}'
```

---

### project_create

Add a new project to Claude Terminal.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| color | string | No | Hex color (e.g. #d97706) |
| icon | string | No | Icon name |
| name | string | No | Display name (defaults to folder name) |
| path | string | Yes | Absolute path to the project directory |
| type | string | No | Project type (default: general) |

**Example:**
```bash
python3 scripts/call-tool.py project_create '{"color":"...","icon":"...","name":"...","path":"...","type":"..."}'
```

---

### project_delete

Remove a project from Claude Terminal. This only removes it from the project list, it does not delete any files.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | Project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py project_delete '{"project":"..."}'
```

---

### project_info

Get detailed info about a specific project: path, type, quick actions, editor, color/icon customization.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | Project name, folder name, or ID |

**Example:**
```bash
python3 scripts/call-tool.py project_info '{"project":"..."}'
```

---

### project_list

List all projects configured in Claude Terminal with their type, path, and folder organization.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| filter | string | No | Optional name filter (case-insensitive substring match) |

**Example:**
```bash
python3 scripts/call-tool.py project_list '{"filter":"..."}'
```

---

### project_open

Open a project in the configured code editor (VS Code, Cursor, etc.) via Claude Terminal.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | Project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py project_open '{"project":"..."}'
```

---

### project_stats

Get project statistics: lines of code per language, file count, directory size.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | Project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py project_stats '{"project":"..."}'
```

---

### project_todos

Scan a project directory for TODO, FIXME, HACK, and XXX comments in source files.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| pattern | string | No | Comment pattern to search for (default: TODO|FIXME|HACK|XXX) |
| project | string | Yes | Project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py project_todos '{"pattern":"...","project":"..."}'
```

---

### project_update

Update project settings in Claude Terminal (name, color, icon, type, editor).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| color | string | No | Hex color (e.g. #d97706) |
| editor | string | No | Preferred code editor (e.g. code, cursor) |
| icon | string | No | Icon name |
| name | string | No | New display name |
| project | string | Yes | Project name or ID |
| type | string | No | Project type |

**Example:**
```bash
python3 scripts/call-tool.py project_update '{"color":"...","editor":"...","icon":"...","name":"...","project":"...","type":"..."}'
```

---

### quickaction_add

Add a new quick action to a project. Quick actions are shell commands that can be triggered from the UI or via MCP.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| command | string | Yes | Shell command to execute (e.g. "npm run build"). Supports variables: $PROJECT_PATH, $PROJECT_NAME, $BRANCH, $HOME |
| icon | string | No | Icon for the action (default: play) |
| name | string | Yes | Display name for the action (e.g. "Build", "Dev Server") |
| pinned | boolean | No | Pin this action to the project card for quick access (max 3 pinned) |
| project | string | Yes | Project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py quickaction_add '{"command":"...","icon":"...","name":"...","pinned":true,"project":"..."}'
```

---

### quickaction_delete

Remove a quick action from a project.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| action | string | Yes | Quick action name or ID to delete |
| project | string | Yes | Project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py quickaction_delete '{"action":"...","project":"..."}'
```

---

### quickaction_list

List quick actions configured for a project. Quick actions are shell commands (build, test, dev, etc.) that can be run in a terminal.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | Project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py quickaction_list '{"project":"..."}'
```

---

### quickaction_run

Trigger a quick action on a project. Opens a terminal in Claude Terminal and runs the command. The action executes asynchronously.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| action | string | Yes | Quick action name or ID |
| project | string | Yes | Project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py quickaction_run '{"action":"...","project":"..."}'
```

---

### quickaction_update

Update an existing quick action on a project. Change its name, command, icon, or pinned state.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| action | string | Yes | Quick action name or ID to update |
| command | string | No | New shell command |
| icon | string | No | New icon |
| name | string | No | New display name |
| pinned | boolean | No | Pin or unpin the action |
| project | string | Yes | Project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py quickaction_update '{"action":"...","command":"...","icon":"...","name":"...","pinned":true,"project":"..."}'
```

---

### claude-terminal_session_list

List recent Claude Code sessions for a project. Returns session IDs, first prompt, date, message count. Use session_replay to get the full step-by-step breakdown of a session.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | number | No | Maximum number of sessions to return (default: 10, max: 50) |
| project_path | string | No | Absolute path to the project. Defaults to CT_PROJECT_PATH env var (current project in Claude Terminal). |

**Example:**
```bash
python3 scripts/call-tool.py claude-terminal_session_list '{"limit":0,"project_path":"..."}'
```

---

### session_replay

Parse a Claude Code session JSONL file into an ordered audit trail. Returns every step: user prompts, tool calls (with input/output), Claude responses, and thinking blocks. Includes a summary with estimated token usage, tool breakdown, and files touched. Useful for auditing what Claude did in a past session, debugging failed sessions, or understanding costs.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| include_thinking | boolean | No | Include extended thinking blocks in output (default: false — they can be very long) |
| max_steps | number | No | Limit output to first N steps (default: unlimited) |
| project_path | string | No | Absolute path to the project. Defaults to CT_PROJECT_PATH. |
| session_id | string | Yes | Session UUID from session_list |

**Example:**
```bash
python3 scripts/call-tool.py session_replay '{"include_thinking":true,"max_steps":0,"project_path":"...","session_id":"..."}'
```

---

### settings_get

Get Claude Terminal settings. Returns all settings or a specific key.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| key | string | No | Specific setting key to read (e.g. "accentColor", "language", "editor"). Omit to return all settings. |

**Example:**
```bash
python3 scripts/call-tool.py settings_get '{"key":"..."}'
```

---

### settings_set

Update a Claude Terminal setting. Changes take effect after app reload.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| key | string | Yes | Setting key to update (e.g. "accentColor", "language", "editor") |
| value | any | Yes | New value for the setting (string, number, boolean, or array) |

**Example:**
```bash
python3 scripts/call-tool.py settings_set '{"key":"...","value":"..."}'
```

---

### sidebar_get_pinned

Get the current pinned tabs configuration in the Claude Terminal sidebar. Returns which tabs are pinned (visible in sidebar) and which are hidden in the More overflow menu.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py sidebar_get_pinned '{}'
```

---

### sidebar_set_pinned

Set which tabs are pinned (visible) in the Claude Terminal sidebar. Unpinned tabs move to the More overflow menu. The "claude" tab is always pinned. Changes take effect after the app reloads or restarts.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| pinned | array<string> | Yes | Tab IDs to pin. Available: claude, git, database, mcp, plugins, skills, agents, workflows, dashboard, timetracking, memory, connectivity |

**Example:**
```bash
python3 scripts/call-tool.py sidebar_set_pinned '{"pinned":[]}'
```

---

### tab_close

Close a tab identified by its stable tabId. Kills the underlying PTY or ends the chat session.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| tabId | string | Yes | Stable tab identifier |

**Example:**
```bash
python3 scripts/call-tool.py tab_close '{"tabId":"..."}'
```

---

### tab_list

List all orchestration tabs (terminals + chats) with stable IDs, mode, status, and activity timestamps. Use this to discover tabs before calling tab_send / tab_status / tab_close.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| mode | string | No | Optional filter by tab mode |
| project | string | No | Optional filter by project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py tab_list '{"mode":"...","project":"..."}'
```

---

### tab_read_output

Read buffered output for a tab. For terminal tabs, returns recent chunks (ANSI-stripped) from a ring buffer (up to ~500KB). For chat tabs, returns structured message entries. Use `afterCursor` to stream incrementally.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| afterCursor | number | No | Return only entries with cursor > this value (default 0 = from beginning). |
| maxEntries | number | No | Maximum number of entries to return (default 200, max 1000). |
| tabId | string | Yes | Stable tab identifier |

**Example:**
```bash
python3 scripts/call-tool.py tab_read_output '{"afterCursor":0,"maxEntries":0,"tabId":"..."}'
```

---

### tab_send

Send content to a specific tab by its stable tabId. For chat tabs the content is submitted as a user message; for terminal tabs it is typed as a command with a trailing newline. Fire-and-forget with a short response confirmation (~2-5s).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| content | string | Yes | Text to send (prompt for chat, command for terminal) |
| tabId | string | Yes | Stable tab identifier (see tab_list) |

**Example:**
```bash
python3 scripts/call-tool.py tab_send '{"content":"...","tabId":"..."}'
```

---

### tab_status

Return the detailed status for a tab identified by its stable tabId. Includes mode-specific details (lastCommand/isPromptReady for terminals, tokensUsed/pendingPermission for chats).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| tabId | string | Yes | Stable tab identifier (see tab_list) |

**Example:**
```bash
python3 scripts/call-tool.py tab_status '{"tabId":"..."}'
```

---

### tab_wait

Block until a tab reaches any of the target statuses (default: idle, awaiting_permission, error). Subscribe-based on the renderer side, no polling. Returns the final status snapshot. Useful for fan-out orchestration: kick work with tab_send, then tab_wait until each tab goes idle or stops on a permission prompt.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| tabId | string | Yes | Stable tab identifier |
| targetStatuses | array<string> | No | Statuses that resolve the wait (default: idle, awaiting_permission, error). |
| timeoutMs | number | No | Max wait in ms (default 60000, max 600000). |

**Example:**
```bash
python3 scripts/call-tool.py tab_wait '{"tabId":"...","targetStatuses":[],"timeoutMs":0}'
```

---

### tab_wait_any

Block until ANY of the given tabs reaches a target status. Returns the first tab that matched. Ideal for parallel orchestration: start N tabs, then tab_wait_any to grab the first that completes.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| tabIds | array<string> | Yes | Stable tab IDs to watch |
| targetStatuses | array<string> | No | Statuses that resolve the wait (default: idle, awaiting_permission, error). |
| timeoutMs | number | No | Max wait in ms (default 60000, max 600000). |

**Example:**
```bash
python3 scripts/call-tool.py tab_wait_any '{"tabIds":[],"targetStatuses":[],"timeoutMs":0}'
```

---

### claude-terminal_terminal_close

[Legacy — prefer tab_close with a stable tabId] Close a terminal tab in Claude Terminal.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | Project name or ID |
| terminalId | string | No | Terminal ID to close (if not provided, closes the active terminal) |

**Example:**
```bash
python3 scripts/call-tool.py claude-terminal_terminal_close '{"project":"...","terminalId":"..."}'
```

---

### claude-terminal_terminal_create

Open a new terminal tab in Claude Terminal for a project. Returns the newly created tab's stable `tabId` that can be passed to tab_send / tab_status / tab_close. When `skipPermissions` is omitted, the user's global setting is used (same behavior as creating a tab from the UI).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| mode | string | No | Terminal mode (default: terminal) |
| project | string | Yes | Project name or ID |
| skipPermissions | boolean | No | Bypass Claude permission prompts for this tab (chat mode only). If omitted, the global user setting is applied. |

**Example:**
```bash
python3 scripts/call-tool.py claude-terminal_terminal_create '{"mode":"...","project":"...","skipPermissions":true}'
```

---

### claude-terminal_terminal_list

[Legacy — prefer tab_list] List active terminals in Claude Terminal. Shows terminal ID, project, mode (terminal/chat), and status.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | No | Optional filter by project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py claude-terminal_terminal_list '{"project":"..."}'
```

---

### terminal_read_output

[Legacy] Read recent output from a terminal in Claude Terminal. Returns the last N lines of terminal output.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| lines | number | No | Number of lines to return (default: 50, max: 200) |
| project | string | Yes | Project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py terminal_read_output '{"lines":0,"project":"..."}'
```

---

### terminal_send_command

[Legacy — prefer tab_send with a stable tabId] Send a command to a running terminal in Claude Terminal. The command is typed into the first terminal of the specified project, which is ambiguous when multiple tabs exist.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| command | string | Yes | Command to send to the terminal |
| project | string | Yes | Project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py terminal_send_command '{"command":"...","project":"..."}'
```

---

### time_compare

Compare time spent between two periods (e.g., this week vs last week).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| period | string | No | Period to compare (default: week) |

**Example:**
```bash
python3 scripts/call-tool.py time_compare '{"period":"..."}'
```

---

### time_export

Export time tracking data as CSV or JSON. Filterable by project and date range.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| end_date | string | No | End date filter YYYY-MM-DD (optional) |
| format | string | No | Output format (default: csv) |
| project | string | No | Filter by project name (optional) |
| start_date | string | No | Start date filter YYYY-MM-DD (optional) |

**Example:**
```bash
python3 scripts/call-tool.py time_export '{"end_date":"...","format":"...","project":"...","start_date":"..."}'
```

---

### time_monthly

Get detailed monthly time tracking statistics.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| month | string | No | Month in YYYY-MM format (defaults to current month) |

**Example:**
```bash
python3 scripts/call-tool.py time_monthly '{"month":"..."}'
```

---

### time_project

Get detailed time tracking for a specific project: today, this week, this month, all time, and recent sessions.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | Project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py time_project '{"project":"..."}'
```

---

### time_sessions

List raw time tracking sessions with start/end times and durations. Supports filtering by project and date.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| date | string | No | Filter by specific day YYYY-MM-DD (optional) |
| limit | number | No | Max sessions to return (default: 20, max: 100) |
| project | string | No | Filter by project name (optional) |

**Example:**
```bash
python3 scripts/call-tool.py time_sessions '{"date":"...","limit":0,"project":"..."}'
```

---

### time_summary

Get a full time tracking summary: this month stats, top projects, daily breakdown for the last 7 days.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py time_summary '{}'
```

---

### time_today

Get time spent today: total and per project breakdown.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py time_today '{}'
```

---

### time_week

Get time spent this week: total and per project breakdown.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py time_week '{}'
```

---

### time_yearly

Get yearly time tracking overview from monthly archives.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| year | number | No | Year (defaults to current year) |

**Example:**
```bash
python3 scripts/call-tool.py time_yearly '{"year":0}'
```

---

### usage_get

Get current Claude API usage data: tokens consumed, daily limit, percentage used, and reset time.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py usage_get '{}'
```

---

### usage_refresh

Request a refresh of Claude API usage data. Claude Terminal will fetch the latest usage from the Anthropic API.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py usage_refresh '{}'
```

---

### webapp_scripts

List all npm/yarn/pnpm scripts available in the project with their commands. Shows dev, build, test, lint and any custom scripts.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | WebApp project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py webapp_scripts '{"project":"..."}'
```

---

### webapp_stack

Detect the full tech stack of a webapp project: framework, bundler, CSS solution, test runner, linter, package manager, TypeScript, and Node version. One call gives complete project context.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | WebApp project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py webapp_stack '{"project":"..."}'
```

---

### webapp_start

Start the dev server for a webapp project. Uses the configured devCommand or auto-detects from package.json scripts.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | WebApp project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py webapp_start '{"project":"..."}'
```

---

### webapp_stop

Stop the running dev server for a webapp project.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| project | string | Yes | WebApp project name or ID |

**Example:**
```bash
python3 scripts/call-tool.py webapp_stop '{"project":"..."}'
```

---

### workflow_add_node

Add a node to an existing workflow graph. Returns the new node ID. Available types: workflow/trigger, workflow/shell, workflow/claude, workflow/git, workflow/http, workflow/db, workflow/file, workflow/notify, workflow/wait, workflow/log, workflow/condition, workflow/loop, workflow/variable, workflow/get_variable, workflow/transform, workflow/subworkflow, workflow/switch, workflow/project, workflow/time. workflow/get_variable is a pure data node (no exec pins) — connect it directly to any data input pin to supply a variable value. workflow/project with action "list" returns all Claude Terminal projects as an array — connect its Projects output (slot 2) to a Loop node Items input (slot 1) to iterate over projects. Loop node: slot 0 output = Each (body of the loop, connects to first child node), slot 1 output = Done (continues after loop ends). Child nodes inside a loop body are NOT shown as top-level steps in run history — only the loop step itself appears, with an iteration badge. For claude/shell/git nodes, set projectId="__custom__" and cwd="<path>" to use a custom working directory (supports variable interpolation like $item.path). workflow/file actions: read (content→slot2), write, append, copy, delete, exists (exists→slot3), move/rename (use destination property for new path), list (glob→slot4 files array, slot5 count — use properties: { path: "./src", pattern: "**/*.js", recursive: true, type: "files|dirs|all" }). list output files array is ideal to connect to a Loop node to process each file. workflow/time reads Claude Terminal time tracking data — actions: get_today (today=slot2/week=slot3/month=slot4 ms + projects=slot5 array), get_week (total=slot2 ms + days=slot3 array [{date,dayOfWeek,ms,formatted}]), get_project (today=slot2/week=slot3/month=slot4/total=slot5 ms + sessionCount=slot6 — set projectId property OR connect a string data pin to its projectId input slot1), get_all_projects (projects=slot2 array sorted by today desc + count=slot3 — connect projects to Loop Items slot1), get_sessions (sessions=slot2 array + count=slot3 + totalMs=slot4, filterable via startDate/endDate properties, optional projectId input pin slot1). Divide ms by 3600000 for hours. Pattern: get_all_projects→Loop→get_project builds per-project reports. Tip: you can skip pos and call workflow_auto_layout after adding all nodes to arrange them cleanly.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| pos | array<number> | No | Position [x, y] on the canvas. Optional — use workflow_auto_layout after building to arrange all nodes cleanly. |
| properties | object | No | Node properties (command, prompt, variable, operator, value, etc.) |
| title | string | No | Optional custom display title for the node |
| type | string | Yes | Node type (e.g. workflow/shell, workflow/condition) |
| workflow | string | Yes | Workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workflow_add_node '{"pos":[],"properties":{},"title":"...","type":"...","workflow":"..."}'
```

---

### workflow_add_variable

Add an abstract variable definition to a workflow. Variables are named typed values stored in the Variables panel (separate from graph nodes). Once defined, they can be referenced in workflow/variable and workflow/get_variable nodes by name. Types: string, number, boolean, array, object, any.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| name | string | Yes | Variable name (e.g. "today", "projectList") |
| varType | string | No | Variable type (default: any) |
| workflow | string | Yes | Workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workflow_add_variable '{"name":"...","varType":"...","workflow":"..."}'
```

---

### workflow_auto_layout

Auto-arrange all nodes in a workflow graph for clean visual layout. Uses topological sort to place nodes in columns left-to-right following execution flow. Call this after building a workflow to clean up node positions.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow | string | Yes | Workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workflow_auto_layout '{"workflow":"..."}'
```

---

### claude-terminal_workflow_cancel

Cancel a running workflow execution.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| run_id | string | Yes | Run ID to cancel |

**Example:**
```bash
python3 scripts/call-tool.py claude-terminal_workflow_cancel '{"run_id":"..."}'
```

---

### workflow_clone

Duplicate an existing workflow with a new name.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| name | string | Yes | Name for the clone |
| workflow | string | Yes | Source workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workflow_clone '{"name":"...","workflow":"..."}'
```

---

### workflow_connect_nodes

Connect an output slot of one node to an input slot of another. Slot conventions: most nodes have 1 input (slot 0) and outputs slot0=Done/True, slot1=Error/False. Condition: slot0=TRUE path, slot1=FALSE path. Loop: slot0=Each body (connects to first child node inside the loop), slot1=Done (connects to first node after the loop). IMPORTANT: child nodes inside a loop body must be connected to the Loop's slot0 (Each) — they will not appear as top-level steps, only the Loop node does.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| from_node | number | Yes | Origin node ID |
| from_slot | number | Yes | Output slot index (0=Done/True/Start, 1=Error/False/Each) |
| to_node | number | Yes | Target node ID |
| to_slot | number | Yes | Input slot index (almost always 0) |
| workflow | string | Yes | Workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workflow_connect_nodes '{"from_node":0,"from_slot":0,"to_node":0,"to_slot":0,"workflow":"..."}'
```

---

### claude-terminal_workflow_create

Create a new workflow with an optional initial graph. Returns the new workflow ID. Use this to start building a workflow from scratch.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| graph | object | No | Optional full LiteGraph JSON { nodes[], links[] } to set immediately |
| name | string | Yes | Workflow name (required) |
| trigger_type | string | No | Trigger type (default: manual). webhook = triggered by external HTTP POST via cloud relay |
| trigger_value | string | No | Cron expression or hook type depending on trigger_type |

**Example:**
```bash
python3 scripts/call-tool.py claude-terminal_workflow_create '{"graph":{},"name":"...","trigger_type":"...","trigger_value":"..."}'
```

---

### claude-terminal_workflow_delete

Delete a workflow permanently.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow | string | Yes | Workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py claude-terminal_workflow_delete '{"workflow":"..."}'
```

---

### workflow_delete_node

Delete a node (and all its connected links) from a workflow graph.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| node_id | number | Yes | Node ID to delete |
| workflow | string | Yes | Workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workflow_delete_node '{"node_id":0,"workflow":"..."}'
```

---

### workflow_diagnose

Analyse a workflow run and diagnose what happened: success/failure cause, error messages, which step failed, loop iteration results, and suggested fixes. Use this to understand why a run failed or to verify a run worked correctly. Combines run history + step outputs for a complete picture.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| run_id | string | Yes | Run ID to diagnose. Get it from workflow_runs output. |

**Example:**
```bash
python3 scripts/call-tool.py workflow_diagnose '{"run_id":"..."}'
```

---

### workflow_enable

Enable or disable a workflow.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| enabled | boolean | Yes | true to enable, false to disable |
| workflow | string | Yes | Workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workflow_enable '{"enabled":true,"workflow":"..."}'
```

---

### workflow_export

Export a workflow definition as JSON for sharing or backup.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow | string | Yes | Workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workflow_export '{"workflow":"..."}'
```

---

### workflow_get

Get detailed info about a specific workflow: steps, trigger config, concurrency, dependencies, and recent runs.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow | string | Yes | Workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workflow_get '{"workflow":"..."}'
```

---

### workflow_get_graph

Get the full graph (nodes + links) of a workflow in a readable format. Use this to understand the current structure before making changes.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow | string | Yes | Workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workflow_get_graph '{"workflow":"..."}'
```

---

### workflow_get_variables

List all variables defined in a workflow. Variables are abstract definitions (name + type) stored in the Variables panel, separate from graph nodes. Also shows which graph nodes reference each variable.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow | string | Yes | Workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workflow_get_variables '{"workflow":"..."}'
```

---

### workflow_import

Import a workflow from a JSON definition.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| json | string | Yes | JSON workflow definition |
| name | string | No | Override the workflow name (optional) |

**Example:**
```bash
python3 scripts/call-tool.py workflow_import '{"json":"...","name":"..."}'
```

---

### claude-terminal_workflow_list

List all workflows configured in Claude Terminal with their trigger type, enabled status, and last run result.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py claude-terminal_workflow_list '{}'
```

---

### workflow_rename

Rename an existing workflow. Changes the display name of the workflow.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| new_name | string | Yes | New name for the workflow |
| workflow | string | Yes | Current workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workflow_rename '{"new_name":"...","workflow":"..."}'
```

---

### workflow_run_logs

Get full step-by-step logs and outputs for a specific run. Shows stdout/stderr for shell nodes, Claude agent output, HTTP responses, error details, and loop iteration results. Use this after workflow_runs to get the detailed output of a specific run (identified by its run ID from the run history).

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| run_id | string | Yes | Run ID (e.g. run_abc123). Get it from workflow_runs output. |

**Example:**
```bash
python3 scripts/call-tool.py workflow_run_logs '{"run_id":"..."}'
```

---

### workflow_runs

Get run history for a workflow (or all workflows). Shows status, duration, trigger, and step results. Loop steps show iteration count (×N). Child nodes inside loops are not shown as separate steps — they are embedded in the loop step output.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | number | No | Max runs to return (default: 10) |
| workflow | string | No | Workflow name or ID (omit for all workflows) |

**Example:**
```bash
python3 scripts/call-tool.py workflow_runs '{"limit":0,"workflow":"..."}'
```

---

### claude-terminal_workflow_status

Get currently active (running/queued) workflow executions.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py claude-terminal_workflow_status '{}'
```

---

### workflow_test_node

Test a single workflow node by writing a test trigger. The node will be executed in isolation by Claude Terminal.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| node_id | number | Yes | The node ID to test |
| workflow | string | Yes | Workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workflow_test_node '{"node_id":0,"workflow":"..."}'
```

---

### workflow_trigger

Trigger a workflow to run. Returns the run ID. The workflow executes asynchronously — use workflow_runs to check results.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow | string | Yes | Workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workflow_trigger '{"workflow":"..."}'
```

---

### workflow_update_node

Update properties or title of an existing node in a workflow graph.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| node_id | number | Yes | Node ID to update |
| properties | object | No | Properties to merge into the node (partial update) |
| title | string | No | New custom title for the node |
| workflow | string | Yes | Workflow name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workflow_update_node '{"node_id":0,"properties":{},"title":"...","workflow":"..."}'
```

---

### workspace_add_link

Add a concept link between two entities (documents or projects) inside a workspace.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| description | string | No | Optional description of the relationship |
| label | string | Yes | Relationship label (e.g. "depends-on", "related-to") |
| source | string | Yes | Source entity name (document title or project name) |
| target | string | Yes | Target entity name (document title or project name) |
| workspace | string | Yes | Workspace name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workspace_add_link '{"description":"...","label":"...","source":"...","target":"...","workspace":"..."}'
```

---

### workspace_info

Get detailed info about a workspace: metadata, projects (resolved names/paths), documents, and concept links.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workspace | string | Yes | Workspace name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workspace_info '{"workspace":"..."}'
```

---

### workspace_list

List all workspaces with their project counts and document counts.

No parameters required.

**Example:**
```bash
python3 scripts/call-tool.py workspace_list '{}'
```

---

### workspace_read_doc

Read a knowledge base document from a workspace. Returns the full markdown content.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| doc | string | Yes | Document title, filename, or ID |
| workspace | string | Yes | Workspace name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workspace_read_doc '{"doc":"...","workspace":"..."}'
```

---

### workspace_search

Search across all documents in a workspace. Performs case-insensitive matching in titles and content, returning matching documents with snippets.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| query | string | Yes | Search query (case-insensitive) |
| workspace | string | Yes | Workspace name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workspace_search '{"query":"...","workspace":"..."}'
```

---

### workspace_write_doc

Create or update a knowledge base document in a workspace. If a document with the same title already exists it is updated; otherwise a new document is created.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| content | string | Yes | Markdown content |
| summary | string | No | Optional short summary |
| tags | array<string> | No | Optional tags for categorisation |
| title | string | Yes | Document title |
| workspace | string | Yes | Workspace name or ID |

**Example:**
```bash
python3 scripts/call-tool.py workspace_write_doc '{"content":"...","summary":"...","tags":[],"title":"...","workspace":"..."}'
```

---

