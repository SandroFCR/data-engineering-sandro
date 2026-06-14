"""Transform raw CoinGecko JSON into a tabular CSV file."""

from __future__ import annotations

import csv
import json
from datetime import datetime, timezone
from pathlib import Path


FIELDNAMES = [
    "coin_id",
    "price_usd",
    "market_cap_usd",
    "volume_24h_usd",
    "change_24h_pct",
    "price_last_updated_at_utc",
    "extracted_at_utc",
]


def find_latest_raw_file(raw_dir: Path) -> Path:
    files = sorted(raw_dir.glob("coingecko_prices_*.json"))
    if not files:
        raise FileNotFoundError(f"No raw files found in {raw_dir}")
    return files[-1]


def unix_to_utc(timestamp: int | None) -> str:
    if timestamp is None:
        return ""
    return datetime.fromtimestamp(timestamp, tz=timezone.utc).isoformat()


def transform_payload(raw_path: Path) -> list[dict]:
    payload = json.loads(raw_path.read_text(encoding="utf-8"))
    extracted_at = payload["extracted_at_utc"]
    data = payload["data"]

    rows = []
    for coin_id, metrics in data.items():
        rows.append(
            {
                "coin_id": coin_id,
                "price_usd": metrics.get("usd"),
                "market_cap_usd": metrics.get("usd_market_cap"),
                "volume_24h_usd": metrics.get("usd_24h_vol"),
                "change_24h_pct": metrics.get("usd_24h_change"),
                "price_last_updated_at_utc": unix_to_utc(metrics.get("last_updated_at")),
                "extracted_at_utc": extracted_at,
            }
        )

    return sorted(rows, key=lambda row: row["coin_id"])


def save_processed_csv(rows: list[dict], output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    extracted_at = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    output_path = output_dir / f"crypto_prices_{extracted_at}.csv"

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)

    return output_path


def main(raw_path: Path | None = None) -> Path:
    project_dir = Path(__file__).resolve().parents[1]
    raw_dir = project_dir / "data" / "raw"
    processed_dir = project_dir / "data" / "processed"

    selected_raw_path = raw_path or find_latest_raw_file(raw_dir)
    rows = transform_payload(selected_raw_path)
    output_path = save_processed_csv(rows, processed_dir)
    print(f"Processed data saved: {output_path}")
    return output_path


if __name__ == "__main__":
    main()

