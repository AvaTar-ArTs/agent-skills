#!/usr/bin/env python3
"""Audit Codex MCP configuration without exposing secret values."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import socket
import tomllib
from pathlib import Path
from urllib.parse import urlparse


SECRET_KEYS = {"authorization", "token", "secret", "password", "api_key", "apikey", "access_key"}


def secret_key(name: str) -> bool:
    lowered = name.lower().replace("-", "_")
    return lowered in SECRET_KEYS or any(part in lowered for part in ("token", "secret", "password", "authorization", "api_key"))


def resolves(host: str | None) -> bool | None:
    if not host or host in {"127.0.0.1", "localhost"}:
        return None
    try:
        socket.getaddrinfo(host, 443)
        return True
    except OSError:
        return False


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=Path.home() / ".codex/config.toml")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()
    config_path = args.config.expanduser().resolve()
    data = tomllib.loads(config_path.read_text(encoding="utf-8", errors="replace"))
    servers = data.get("mcp_servers", {})
    records = []
    endpoint_counts: dict[str, int] = {}
    for name, raw in sorted(servers.items()):
        cfg = raw if isinstance(raw, dict) else {}
        command = cfg.get("command")
        command_path = None
        command_exists = None
        if isinstance(command, str):
            command_path = str(Path(command).expanduser()) if "/" in command else shutil.which(command)
            command_exists = bool(command_path and Path(command_path).exists())
        url = cfg.get("url") if isinstance(cfg.get("url"), str) else None
        host = urlparse(url).hostname if url else None
        if url:
            endpoint_counts[url] = endpoint_counts.get(url, 0) + 1
        headers = cfg.get("http_headers") if isinstance(cfg.get("http_headers"), dict) else {}
        env = cfg.get("env") if isinstance(cfg.get("env"), dict) else {}
        records.append({
            "name": name,
            "transport": "http" if url else ("stdio" if command else "unknown"),
            "enabled": cfg.get("enabled", True),
            "command": command,
            "resolved_command": command_path,
            "command_exists": command_exists,
            "args_count": len(cfg.get("args", [])) if isinstance(cfg.get("args"), list) else None,
            "cwd": cfg.get("cwd"),
            "url": url,
            "host": host,
            "host_resolves": resolves(host),
            "header_names": sorted(headers),
            "literal_secret_headers": sorted(key for key, value in headers.items() if secret_key(str(key)) and isinstance(value, str) and value),
            "env_names": sorted(env),
            "missing_env_names": sorted(key for key, value in env.items() if isinstance(value, str) and value.startswith("$") and not os.environ.get(value[1:])),
            "tools_restricted": "tools" in cfg,
        })
    report = {
        "schema": "codex-mcp-audit/v1",
        "config": str(config_path),
        "server_count": len(records),
        "servers": records,
        "duplicate_urls": {url: count for url, count in endpoint_counts.items() if count > 1},
        "security_findings": [
            {
                "severity": "high",
                "server": item["name"],
                "finding": "literal authorization-like header in config",
                "header_names": item["literal_secret_headers"],
                "remediation": "rotate the credential and use a secret/environment mechanism",
            }
            for item in records if item["literal_secret_headers"]
        ],
    }
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
