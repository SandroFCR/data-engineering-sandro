"""Run SQL analysis queries against the SQLite warehouse."""

from __future__ import annotations

import sqlite3
from pathlib import Path


def read_sql_statements(sql_path: Path) -> list[str]:
    content = sql_path.read_text(encoding="utf-8")
    statements = []

    for chunk in content.split(";"):
        statement = chunk.strip()
        if statement:
            statements.append(statement)

    return statements


def print_rows(headers: list[str], rows: list[tuple]) -> None:
    if not rows:
        print("(no rows)")
        return

    widths = [
        max(len(str(header)), *(len(str(row[index])) for row in rows))
        for index, header in enumerate(headers)
    ]

    header_line = " | ".join(str(header).ljust(widths[index]) for index, header in enumerate(headers))
    separator = "-+-".join("-" * width for width in widths)
    print(header_line)
    print(separator)

    for row in rows:
        print(" | ".join(str(value).ljust(widths[index]) for index, value in enumerate(row)))


def main() -> None:
    project_dir = Path(__file__).resolve().parents[1]
    database_path = project_dir / "database" / "warehouse.db"
    sql_path = project_dir / "sql" / "analysis.sql"

    if not database_path.exists():
        raise FileNotFoundError(
            f"Database not found: {database_path}. Run src/main.py first."
        )

    statements = read_sql_statements(sql_path)

    with sqlite3.connect(database_path) as connection:
        for number, statement in enumerate(statements, start=1):
            cursor = connection.execute(statement)
            rows = cursor.fetchall()
            headers = [description[0] for description in cursor.description or []]

            print(f"\nQuery {number}")
            print("=" * 72)
            print_rows(headers, rows)


if __name__ == "__main__":
    main()

