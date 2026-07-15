#!/usr/bin/env python3
"""
Export decisions and preferences from cross-tool memory database.

Usage:
    python3 export_decisions.py decisions json --limit 30
    python3 export_decisions.py preferences csv --limit 100
    python3 export_decisions.py decisions md --topic agent-creation
"""

import argparse
import csv
import json
import sqlite3
from datetime import datetime
from pathlib import Path


DB_PATH = Path.home() / ".agent-skills" / "memory" / "shared.sqlite"
EXPORTS_DIR = Path.home() / ".agent-skills" / "memory" / "exports"


def get_connection():
    return sqlite3.connect(DB_PATH)


def export_decisions_json(limit: int = 50, topic_filter: str | None = None, source: str | None = None):
    conn = get_connection()
    query = "SELECT id, topic, choice, context, outcome, timestamp FROM decisions"
    conditions = []
    params = []
    
    if topic_filter:
        conditions.append("topic LIKE ?")
        params.append(f"%{topic_filter}%")
    
    if source:
        conditions.append("context LIKE ?")
        params.append(f"%{source}%")
    
    if conditions:
        query += " WHERE " + " AND ".join(conditions)
    
    query += f" ORDER BY id DESC LIMIT {limit}"
    
    rows = conn.execute(query, params).fetchall() if params else conn.execute(query).fetchall()
    
    decisions = [
        {
            "id": row[0],
            "topic": row[1],
            "choice": row[2],
            "context": row[3],
            "outcome": row[4],
            "timestamp": row[5],
        }
        for row in rows
    ]
    
    return decisions


def export_decisions_md(limit: int = 50, topic_filter: str | None = None):
    conn = get_connection()
    query = "SELECT topic, choice, context, outcome, timestamp FROM decisions"
    params = []
    
    if topic_filter:
        query += " WHERE topic LIKE ?"
        params.append(f"%{topic_filter}%")
    
    query += f" ORDER BY id DESC LIMIT {limit}"
    
    rows = conn.execute(query, params).fetchall() if params else conn.execute(query).fetchall()
    
    lines = ["# Decisions Export\n", f"Generated: {datetime.now().isoformat()}\n\n"]
    
    for i, row in enumerate(rows):
        lines.append(f"## {i + 1}. {row[0]}\n\n")
        lines.append(f"**Timestamp:** {row[4]}\n\n")
        if row[1]:
            lines.append(f"**Choice:** {row[1]}\n\n")
        if row[2]:
            lines.append(f"**Context:** {row[2]}\n\n")
        if row[3]:
            lines.append(f"**Outcome:** {row[3]}\n\n")
        lines.append("---\n\n")
    
    return "".join(lines)


def export_preferences_csv(limit: int = 100):
    conn = get_connection()
    rows = conn.execute("SELECT key, value, source, timestamp FROM preferences ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
    
    output = []
    for row in rows:
        output.append({"key": row[0], "value": row[1], "source": row[2], "timestamp": row[3]})
    
    return output


def main():
    parser = argparse.ArgumentParser(description="Export decisions/preferences from memory database")
    parser.add_argument("table", choices=["decisions", "preferences"], help="Table to export")
    parser.add_argument("format", choices=["json", "md", "csv"], help="Output format")
    parser.add_argument("--limit", type=int, default=50, help="Maximum rows to export")
    parser.add_argument("--topic", type=str, help="Filter decisions by topic")
    parser.add_argument("--out", type=Path, help="Output file path")
    
    args = parser.parse_args()
    
    EXPORTS_DIR.mkdir(parents=True, exist_ok=True)
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    if args.format == "json":
        if args.table == "decisions":
            data = export_decisions_json(args.limit, args.topic)
        else:
            data = export_preferences_csv(args.limit)
        
        out_path = args.out or EXPORTS_DIR / f"{args.table}-{today}.json"
        with out_path.open("w") as f:
            json.dump(data, f, indent=2)
        print(f"Wrote {len(data)} rows → {out_path}")
    
    elif args.format == "md":
        data = export_decisions_md(args.limit, args.topic)
        out_path = args.out or EXPORTS_DIR / f"decisions-{today}.md"
        with out_path.open("w") as f:
            f.write(data)
        print(f"Wrote decisions markdown → {out_path}")
    
    elif args.format == "csv":
        data = export_preferences_csv(args.limit)
        out_path = args.out or EXPORTS_DIR / f"preferences-{today}.csv"
        with out_path.open("w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["key", "value", "source", "timestamp"])
            writer.writeheader()
            writer.writerows(data)
        print(f"Wrote {len(data)} preferences → {out_path}")


if __name__ == "__main__":
    main()