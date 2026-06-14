# Crypto ETL Pipeline

Pipeline ETL de criptomonedas construido como primer proyecto de portafolio en Ingenieria de Datos.

## Objetivo

Construir un flujo de datos end-to-end:

```text
CoinGecko API -> JSON raw -> CSV procesado -> SQLite -> consultas SQL -> validaciones de calidad
```

Este proyecto demuestra fundamentos importantes para un rol trainee/junior de Data Engineering:

- consumo de APIs REST;
- almacenamiento de datos raw para auditoria y reproceso;
- transformacion de JSON a estructura tabular;
- carga en base de datos SQLite;
- consultas SQL para analisis;
- validaciones basicas de calidad de datos;
- documentacion tecnica y organizacion en GitHub.

## Stack

- Python
- SQL
- SQLite
- CoinGecko API
- JSON / CSV
- Git y GitHub

## Arquitectura

Flujo del pipeline:

```text
CoinGecko API
    |
    v
extract.py
    |
    v
data/raw/*.json
    |
    v
transform.py
    |
    v
data/processed/*.csv
    |
    v
load.py
    |
    v
database/warehouse.db
    |
    +--> run_analysis.py
    |
    +--> validate.py
    |
    +--> view_results.py
```

Estructura del proyecto:

```text
src/
  extract.py       -> obtiene datos desde CoinGecko API y guarda JSON raw
  transform.py     -> transforma JSON raw a CSV tabular
  load.py          -> carga CSV procesado en SQLite
  main.py          -> ejecuta el pipeline completo
  run_analysis.py  -> ejecuta consultas SQL de analisis
  validate.py      -> ejecuta reglas de calidad de datos
  view_results.py  -> muestra resultados desde consola

data/
  raw/             -> datos originales de la API
  processed/       -> datos procesados en CSV

database/
  warehouse.db     -> base SQLite local

sql/
  analysis.sql     -> consultas SQL del proyecto
```

## Decisiones Tecnicas

### Guardar datos raw

Primero se guarda la respuesta original de la API en `data/raw/`. Esto permite auditar los datos recibidos y reprocesarlos si una transformacion necesita corregirse.

### Separar extract, transform y load

Cada archivo tiene una responsabilidad clara:

- `extract.py`: extraer datos;
- `transform.py`: dar forma tabular;
- `load.py`: cargar a base de datos.

Esto facilita mantenimiento, pruebas y debugging.

### Usar SQLite al inicio

SQLite permite practicar SQL y carga de datos sin configurar un servidor. Es una buena primera base antes de migrar a PostgreSQL.

### Validar antes de confiar

El pipeline incluye reglas de calidad para detectar datos vacios, metricas invalidas o duplicados antes de usar los resultados para analisis.

## Datos

Fuente: CoinGecko `simple/price`.

Criptomonedas iniciales:

- bitcoin
- ethereum
- solana
- cardano
- ripple
- dogecoin

Metricas usadas:

- precio en USD;
- market cap;
- volumen 24h;
- variacion 24h;
- fecha de actualizacion del precio;
- fecha de extraccion del pipeline.

## Como ejecutar

Desde esta carpeta:

```powershell
python src\main.py
```

Para ver resultados:

```powershell
python src\view_results.py
```

Para ejecutar analisis SQL:

```powershell
python src\run_analysis.py
```

Para ejecutar validaciones de calidad:

```powershell
python src\validate.py
```

## Consultas incluidas

El archivo [`sql/analysis.sql`](sql/analysis.sql) responde preguntas como:

- cuantas filas fueron cargadas;
- cuantos snapshots existen;
- ranking de criptomonedas por market cap;
- mayor variacion positiva en 24h;
- mayor variacion negativa en 24h.

## Reglas de calidad de datos

El script `src/validate.py` valida:

- la tabla principal tiene filas;
- `coin_id` no esta vacio;
- `price_usd` es positivo;
- `market_cap_usd` es positivo;
- `volume_24h_usd` no es negativo;
- `extracted_at_utc` no esta vacio;
- no existen duplicados por `coin_id` y `extracted_at_utc`.

## Como Explicarlo En Entrevista

```text
Construí un pipeline ETL modular para datos de criptomonedas. El pipeline extrae precios desde la API de CoinGecko, guarda la respuesta raw en JSON, transforma los datos a un CSV tabular y los carga en SQLite. Luego ejecuta consultas SQL de análisis y validaciones de calidad para revisar nulos, métricas inválidas y duplicados por snapshot.
```

Preguntas que este proyecto ayuda a responder:

- Como consumes datos desde una API?
- Por que guardarias datos raw?
- Como conviertes JSON en una estructura tabular?
- Como cargas datos a una base?
- Como evitas duplicados?
- Como validas calidad de datos?
- Como organizas un pipeline ETL por modulos?

## Aprendizajes principales

- En Ingenieria de Datos conviene guardar primero el dato raw para auditoria y reproceso.
- Separar extraccion, transformacion y carga mejora mantenimiento y lectura del pipeline.
- SQL sigue siendo clave para validar y entender los datos despues de cargarlos.
- Las reglas de calidad ayudan a detectar errores antes de confiar en los resultados.

## Proximas Mejoras

- Migrar la carga de SQLite a PostgreSQL.
- Agregar Docker para levantar la base de datos.
- Agregar variables de entorno para configuracion.
- Agregar logs estructurados.
- Crear modelos analiticos con dbt.
- Construir una version Lakehouse con Databricks, PySpark y Delta Lake.
