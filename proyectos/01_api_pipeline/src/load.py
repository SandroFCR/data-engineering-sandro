"""Load processed crypto prices into a SQLite database."""

from __future__ import annotations

import csv
import sqlite3
from pathlib import Path


CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS crypto_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    coin_id TEXT NOT NULL,
    price_usd REAL,
    market_cap_usd REAL,
    volume_24h_usd REAL,
    change_24h_pct REAL,
    price_last_updated_at_utc TEXT,
    extracted_at_utc TEXT NOT NULL,
    loaded_at_utc TEXT DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (coin_id, extracted_at_utc)
);
"""


INSERT_SQL = """
INSERT OR IGNORE INTO crypto_prices (
    coin_id,
    price_usd,
    market_cap_usd,
    volume_24h_usd,
    change_24h_pct,
    price_last_updated_at_utc,
    extracted_at_utc
) VALUES (?, ?, ?, ?, ?, ?, ?);
"""


def find_latest_processed_file(processed_dir: Path) -> Path:
    files = sorted(processed_dir.glob("crypto_prices_*.csv"))
    if not files:
        raise FileNotFoundError(f"No processed files found in {processed_dir}")
    return files[-1]


def to_float(value: str) -> float | None:
    if value == "" or value is None:
        return None
    return float(value)


def load_csv_to_sqlite(csv_path: Path, database_path: Path) -> int:
    database_path.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(database_path) as connection:
        connection.execute(CREATE_TABLE_SQL)

        with csv_path.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            rows = [
                (
                    row["coin_id"],
                    to_float(row["price_usd"]),
                    to_float(row["market_cap_usd"]),
                    to_float(row["volume_24h_usd"]),
                    to_float(row["change_24h_pct"]),
                    row["price_last_updated_at_utc"],
                    row["extracted_at_utc"],
                )
                for row in reader
            ]

        before = connection.total_changes
        connection.executemany(INSERT_SQL, rows)
        connection.commit()
        return connection.total_changes - before


def main(csv_path: Path | None = None) -> Path:
    project_dir = Path(__file__).resolve().parents[1]
    processed_dir = project_dir / "data" / "processed"
    database_path = project_dir / "database" / "warehouse.db"

    selected_csv_path = csv_path or find_latest_processed_file(processed_dir)
    inserted_rows = load_csv_to_sqlite(selected_csv_path, database_path)
    print(f"Rows inserted: {inserted_rows}")
    print(f"Database ready: {database_path}")
    return database_path


if __name__ == "__main__":
    main()

