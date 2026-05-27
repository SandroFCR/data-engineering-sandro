"""Run basic data quality checks on the SQLite warehouse."""

from __future__ import annotations

import sqlite3
from pathlib import Path


CHECKS = [
    {
        "name": "table_has_rows",
        "sql": "SELECT COUNT(*) FROM crypto_prices;",
        "passes": lambda value: value > 0,
        "message": "The table must have at least one row.",
    },
    {
        "name": "coin_id_not_null",
        "sql": "SELECT COUNT(*) FROM crypto_prices WHERE coin_id IS NULL OR coin_id = '';",
        "passes": lambda value: value == 0,
        "message": "coin_id cannot be empty.",
    },
    {
        "name": "price_usd_positive",
        "sql": "SELECT COUNT(*) FROM crypto_prices WHERE price_usd IS NULL OR price_usd <= 0;",
        "passes": lambda value: value == 0,
        "message": "price_usd must be positive.",
    },
    {
        "name": "no_duplicate_coin_snapshot",
        "sql": """
            SELECT COUNT(*)
            FROM (
                SELECT coin_id, extracted_at_utc, COUNT(*) AS total
                FROM crypto_prices
                GROUP BY coin_id, extracted_at_utc
                HAVING COUNT(*) > 1
            );
        """,
        "passes": lambda value: value == 0,
        "message": "Each coin can appear only once per extraction snapshot.",
    },
]


def main() -> None:
    project_dir = Path(__file__).resolve().parents[1]
    database_path = project_dir / "database" / "warehouse.db"

    if not database_path.exists():
        raise FileNotFoundError(
            f"Database not found: {database_path}. Run src/main.py first."
        )

    failed_checks = []

    with sqlite3.connect(database_path) as connection:
        for check in CHECKS:
            value = connection.execute(check["sql"]).fetchone()[0]
            passed = check["passes"](value)
            status = "PASS" if passed else "FAIL"
            print(f"{status} | {check['name']} | value={value} | {check['message']}")

            if not passed:
                failed_checks.append(check["name"])

    if failed_checks:
        raise SystemExit(f"Data quality failed: {', '.join(failed_checks)}")

    print("All data quality checks passed.")


if __name__ == "__main__":
    main()

