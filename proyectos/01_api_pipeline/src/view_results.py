"""Show the latest crypto prices loaded in SQLite."""

from __future__ import annotations

import sqlite3
from pathlib import Path


def main() -> None:
    project_dir = Path(__file__).resolve().parents[1]
    database_path = project_dir / "database" / "warehouse.db"

    if not database_path.exists():
        raise FileNotFoundError(
            f"Database not found: {database_path}. Run src/main.py first."
        )

    query = """
    SELECT
        coin_id,
        ROUND(price_usd, 2) AS price_usd,
        ROUND(change_24h_pct, 2) AS change_24h_pct,
        ROUND(volume_24h_usd, 2) AS volume_24h_usd,
        extracted_at_utc
    FROM crypto_prices
    WHERE extracted_at_utc = (
        SELECT MAX(extracted_at_utc)
        FROM crypto_prices
    )
    ORDER BY market_cap_usd DESC;
    """

    with sqlite3.connect(database_path) as connection:
        rows = connection.execute(query).fetchall()

    print("coin_id   | price_usd | change_24h_pct | volume_24h_usd | extracted_at_utc")
    print("-" * 86)
    for coin_id, price, change, volume, extracted_at in rows:
        print(f"{coin_id:<9} | {price:>9} | {change:>14} | {volume:>14} | {extracted_at}")


if __name__ == "__main__":
    main()

