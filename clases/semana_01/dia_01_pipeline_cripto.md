# Dia 01 - Primer Pipeline Cripto

## Que Construimos

Creamos un pipeline ETL simple:

```text
CoinGecko API -> JSON raw -> CSV procesado -> SQLite -> SQL
```

## Conceptos Clave

### API

Una API es una puerta para pedir datos a otro sistema. En este proyecto pedimos precios de criptomonedas a CoinGecko.

### JSON Raw

El dato raw es el dato original, tal como llega desde la fuente.

Guardar raw es importante porque permite:

- auditar que llego desde la API;
- reprocesar si nuestra transformacion estaba mal;
- comparar cambios entre ejecuciones.

### Transformacion

Transformar significa convertir datos en una forma mas util. Aqui pasamos de JSON anidado a una tabla CSV.

### Carga

Cargar significa guardar los datos transformados en una base. Aqui usamos SQLite porque no requiere servidor y es perfecto para empezar.

## Archivos Creados

- `src/extract.py`: obtiene datos desde CoinGecko.
- `src/transform.py`: convierte JSON raw en CSV.
- `src/load.py`: carga CSV a SQLite.
- `src/main.py`: ejecuta todo el pipeline.
- `sql/analysis.sql`: consultas iniciales.

## Comando Principal

Desde `proyectos/01_api_pipeline`:

```powershell
python src\main.py
```

Si `python` no existe en tu laptop, instala Python 3.12 o superior y marca la opcion "Add Python to PATH".

## Resultado De La Primera Ejecucion

Se cargaron 5 criptomonedas:

- bitcoin
- ethereum
- ripple
- solana
- cardano

## Mini Reto

Explica con tus palabras:

```text
1. Por que guardamos primero JSON raw?
2. Que problema resuelve transform.py?
3. Por que SQLite es buena opcion para comenzar?
```

## Reto De Codigo

Agrega una criptomoneda nueva a `COIN_IDS` en `src/extract.py`, ejecuta el pipeline otra vez y verifica si aparece en SQLite.

