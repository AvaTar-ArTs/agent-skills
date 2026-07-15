#!/usr/bin/env python3
"""Initialize self-evolving memory database at ~/.agent-skills/memory/shared.sqlite"""

import sqlite3
from pathlib import Path

MEMORY_DIR = Path.home() / ".agent-skills" / "memory"
DB_PATH = MEMORY_DIR / "shared.sqlite"
MEMORY_DIR.mkdir(parents=True, exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS decisions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        topic TEXT NOT NULL,
        choice TEXT NOT NULL,
        context TEXT,
        outcome TEXT,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP,
        embedding TEXT
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS patterns (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pattern TEXT NOT NULL,
        frequency INTEGER DEFAULT 1,
        first_seen TEXT DEFAULT CURRENT_TIMESTAMP,
        last_seen TEXT DEFAULT CURRENT_TIMESTAMP,
        confidence REAL DEFAULT 0.5
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS preferences (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        key TEXT UNIQUE NOT NULL,
        value TEXT NOT NULL,
        source TEXT,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP
    )''')
    
    conn.commit()
    conn.close()
    print(f"✓ Memory database at {DB_PATH}")

if __name__ == "__main__":
    init_db()
