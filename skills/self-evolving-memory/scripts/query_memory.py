#!/usr/bin/env python3
import sqlite3
from pathlib import Path
DB = Path.home() / ".agent-skills" / "memory" / "shared.sqlite"
conn = sqlite3.connect(DB)
for row in conn.execute("SELECT topic, choice FROM decisions ORDER BY rowid DESC LIMIT 10"):
    print(f"{row[0]} → {row[1]}")
