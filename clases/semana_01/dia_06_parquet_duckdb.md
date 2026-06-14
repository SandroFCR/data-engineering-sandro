# Dia 06 - Parquet Y DuckDB

## Que Agregamos

El pipeline ahora genera dos salidas procesadas:

```text
CSV
Parquet
```

Tambien agregamos DuckDB para consultar archivos Parquet directamente con SQL.

## Por Que Parquet

CSV es facil de leer, pero no es el formato mas eficiente para analitica.

Parquet es un formato columnar. Eso significa que guarda los datos pensando en columnas, no solo en filas.

Es muy usado en:

- data lakes;
- lakehouses;
- Databricks;
- Spark;
- pipelines analiticos modernos.

## Por Que DuckDB

DuckDB permite hacer SQL sobre archivos locales como CSV o Parquet sin levantar un servidor.

En este proyecto:

```text
Parquet + DuckDB = analisis moderno local
```

## Nuevo Flujo

```text
API -> JSON raw -> CSV + Parquet -> SQLite + DuckDB SQL
```

## Comando Nuevo

Desde `proyectos/01_crypto_etl_pipeline`:

```powershell
python src\run_duckdb_analysis.py
```

## Conexion Con Databricks

Databricks tambien trabaja mucho con formatos columnares y arquitectura Lakehouse.

Aprender Parquet ahora facilita entender despues:

```text
bronze -> silver -> gold
Delta Lake
Spark SQL
Databricks Workflows
```

## Mini Reto

Responde en tus palabras:

```text
1. Por que CSV es facil para aprender pero Parquet es mejor para analitica?
2. Que ventaja tiene consultar Parquet con DuckDB?
3. Como conecta esto con Databricks?
```

