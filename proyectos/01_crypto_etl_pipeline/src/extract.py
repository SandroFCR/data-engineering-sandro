"""Extract crypto prices from CoinGecko and save the raw JSON response."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


API_URL = "https://api.coingecko.com/api/v3/simple/price"
COIN_IDS = ["bitcoin", "ethereum", "solana", "cardano", "ripple", "dogecoin"]
VS_CURRENCY = "usd"


def build_url() -> str:
    params = {
        "ids": ",".join(COIN_IDS),
        "vs_currencies": VS_CURRENCY,
        "include_24hr_change": "true",
        "include_24hr_vol": "true",
        "include_market_cap": "true",
        "include_last_updated_at": "true",
    }
    return f"{API_URL}?{urlencode(params)}"


def fetch_prices() -> dict:
    request = Request(
        build_url(),
        headers={
            "Accept": "application/json",
            "User-Agent": "data-engineering-sandro/0.1",
        },
    )

    with urlopen(request, timeout=30) as response:
        if response.status != 200:
            raise RuntimeError(f"API error: status {response.status}")
        return json.loads(response.read().decode("utf-8"))


def save_raw_json(data: dict, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    extracted_at = datetime.now(timezone.utc)
    output_path = output_dir / f"coingecko_prices_{extracted_at.strftime('%Y%m%d_%H%M%S')}.json"

    payload = {
        "source": "coingecko",
        "endpoint": API_URL,
        "extracted_at_utc": extracted_at.isoformat(),
        "data": data,
    }

    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return output_path


def main() -> Path:
    project_dir = Path(__file__).resolve().parents[1]
    raw_dir = project_dir / "data" / "raw"

    data = fetch_prices()
    output_path = save_raw_json(data, raw_dir)
    print(f"Raw data saved: {output_path}")
    return output_path


if __name__ == "__main__":
    main()
