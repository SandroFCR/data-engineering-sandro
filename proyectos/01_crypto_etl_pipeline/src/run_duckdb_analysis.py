"""Run analytical SQL queries directly over processed Parquet files with DuckDB."""

from __future__ import annotations

from pathlib import Path

import duckdb


def find_latest_parquet_file(processed_dir: Path) -> Path:
    files = sorted(processed_dir.glob("crypto_prices_*.parquet"))
    if not files:
        raise FileNotFoundError(
            f"No Parquet files found in {processed_dir}. Run src/main.py first."
        )
    return files[-1]


def print_rows(headers: list[str], rows: list[tuple]) -> None:
    if not rows:
        print("(no rows)")
        return

    widths = [
        max(len(str(header)), *(len(str(row[index])) for row in rows))
        for index, header in enumerate(headers)
    ]

    print(" | ".join(str(header).ljust(widths[index]) for index, header in enumerate(headers)))
    print("-+-".join("-" * width for width in widths))

    for row in rows:
        print(" | ".join(str(value).ljust(widths[index]) for index, value in enumerate(row)))


def main() -> None:
    project_dir = Path(__file__).resolve().parents[1]
    processed_dir = project_dir / "data" / "processed"
    parquet_path = find_latest_parquet_file(processed_dir)

    queries = [
        (
            "Latest Parquet snapshot",
            """
            SELECT
                coin_id,
                ROUND(price_usd, 2) AS price_usd,
                ROUND(change_24h_pct, 2) AS change_24h_pct,
                ROUND(volume_24h_usd, 2) AS volume_24h_usd
            FROM read_parquet(?)
            ORDER BY market_cap_usd DESC;
            """,
        ),
        (
            "Highest 24h change",
            """
            SELECT
                coin_id,
                ROUND(change_24h_pct, 2) AS change_24h_pct
            FROM read_parquet(?)
            ORDER BY change_24h_pct DESC
            LIMIT 1;
            """,
        ),
        (
            "Lowest 24h change",
            """
            SELECT
                coin_id,
                ROUND(change_24h_pct, 2) AS change_24h_pct
            FROM read_parquet(?)
            ORDER BY change_24h_pct ASC
            LIMIT 1;
            """,
        ),
    ]

    print(f"Using Parquet file: {parquet_path}")

    with duckdb.connect() as connection:
        for title, sql in queries:
            cursor = connection.execute(sql, [str(parquet_path)])
            rows = cursor.fetchall()
            headers = [description[0] for description in cursor.description]

            print(f"\n{title}")
            print("=" * 72)
            print_rows(headers, rows)


if __name__ == "__main__":
    main()

