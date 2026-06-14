"""Run the complete crypto ETL pipeline."""

from __future__ import annotations

from extract import main as extract
from load import main as load
from transform import main as transform


def main() -> None:
    raw_path = extract()
    processed_path = transform(raw_path)
    load(processed_path)


if __name__ == "__main__":
    main()

