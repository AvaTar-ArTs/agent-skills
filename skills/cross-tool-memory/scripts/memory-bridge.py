#!/usr/bin/env python3
"""MCP bridge for memory queries"""
import sqlite3
from pathlib import Path
import json

DB = Path.home() / ".agent-skills" / "memory" / "shared.sqlite"

def query_memory(term=None, table="decisions", limit=10):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    
    if table == "decisions":
        if term:
            c.execute(f"SELECT topic, choice, outcome FROM decisions WHERE topic LIKE '%{term}%' OR outcome LIKE '%{term}%' LIMIT ?", (limit,))
        else:
            c.execute("SELECT topic, choice, outcome FROM decisions ORDER BY rowid DESC LIMIT ?", (limit,))
    else:
        c.execute(f"SELECT * FROM {table} LIMIT ?", (limit,))
    
    results = c.fetchall()
    conn.close()
    
    for row in results:
        print(f"{row[0]} → {row[1] if len(row) > 1 else ''} | {row[2] if len(row) > 2 else ''}")

if __name__ == "__main__":
    import sys
    term = sys.argv[1] if len(sys.argv) > 1 else None
    query_memory(term)
