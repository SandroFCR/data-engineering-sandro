-- Total rows loaded
SELECT COUNT(*) AS total_rows
FROM crypto_prices;

-- Total extraction snapshots
SELECT COUNT(DISTINCT extracted_at_utc) AS total_snapshots
FROM crypto_prices;

-- Latest snapshot by extraction time
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

-- Biggest 24h winner in the latest snapshot
SELECT
    coin_id,
    ROUND(change_24h_pct, 2) AS change_24h_pct
FROM crypto_prices
WHERE extracted_at_utc = (
    SELECT MAX(extracted_at_utc)
    FROM crypto_prices
)
ORDER BY change_24h_pct DESC
LIMIT 1;
