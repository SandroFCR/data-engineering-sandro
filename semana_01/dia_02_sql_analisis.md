# Dia 02 - Analisis Con SQL

## Que Hacemos Hoy

Ya tenemos datos cargados en SQLite. Ahora toca hacer preguntas.

Un Data Engineer no solo mueve datos. Tambien debe validar que los datos sirven para responder algo.

## Preguntas Iniciales

Con los datos de criptomonedas queremos responder:

```text
1. Cuantas filas se cargaron?
2. Cual es el ultimo snapshot?
3. Que criptomoneda tiene mayor market cap?
4. Que criptomoneda tuvo mayor subida en 24h?
```

## Archivo Principal

Las consultas viven en:

```text
proyectos/01_api_pipeline/sql/analysis.sql
```

## Ejecutar Analisis

Desde `proyectos/01_api_pipeline`:

```powershell
python src\run_analysis.py
```

## Concepto Clave

Una tabla puede tener muchos snapshots.

Por eso usamos:

```sql
WHERE extracted_at_utc = (
    SELECT MAX(extracted_at_utc)
    FROM crypto_prices
)
```

Eso significa:

```text
Dame solo los datos de la ejecucion mas reciente.
```

## Reto Para Sandro

Agrega una consulta nueva a `analysis.sql` que muestre la criptomoneda con menor cambio porcentual en 24 horas.

Pista:

```sql
ORDER BY change_24h_pct ASC
LIMIT 1;
```

