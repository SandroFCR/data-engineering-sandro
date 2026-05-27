# Proyecto 01 - Pipeline ETL Desde API Publica

## Objetivo

Construir un pipeline real de principio a fin:

```text
API -> JSON raw -> transformacion -> base de datos -> consultas SQL -> reporte
```

## Resultado Esperado

Al terminar, este proyecto debe demostrar que puedes:

- Consumir datos desde una API.
- Guardar datos raw.
- Limpiar y transformar datos con Python.
- Cargar datos a SQLite o PostgreSQL.
- Escribir consultas SQL utiles.
- Documentar un pipeline como portafolio.

## Opciones De Dataset

Elige una para empezar:

1. Criptomonedas: precios historicos y variacion.
2. Clima: temperatura por ciudad y dia.
3. Futbol: partidos, equipos y resultados.
4. Peliculas: rankings, generos y popularidad.
5. Ventas simuladas: clientes, productos y pedidos.

## Arquitectura

```text
src/
  extract.py      -> obtiene datos desde API
  transform.py    -> limpia y estructura datos
  load.py         -> carga datos a base de datos
  main.py         -> ejecuta el pipeline completo
data/
  raw/            -> datos originales
  processed/      -> datos limpios
database/
  warehouse.db    -> base SQLite inicial
sql/
  analysis.sql    -> consultas de analisis
```

## Preguntas Que Debe Responder

- Que datos llegaron?
- Hay datos nulos o duplicados?
- Cual es el valor maximo, minimo y promedio?
- Como cambia el dato en el tiempo?
- Que insight puede servir para tomar una decision?

## Primera Mision

Elegir la fuente de datos y escribir una explicacion corta:

```text
Voy a trabajar con datos de ______ porque quiero analizar ______.
```

Respuesta:

```text
Voy a trabajar con datos de criptomonedas porque quiero analizar precios, volumen, capitalizacion de mercado y variacion de 24 horas.
```

## Como Ejecutar El Pipeline

Desde la carpeta del proyecto:

```powershell
cd "C:\Users\Sandro\Documents\New project\proyectos\01_api_pipeline"
python src\main.py
```

## Como Ver Los Resultados

Opcion 1: con el script de consola:

```powershell
python src\view_results.py
```

Opcion 2: ejecutar las consultas SQL de analisis:

```powershell
python src\run_analysis.py
```

Opcion 3: ejecutar validaciones de calidad:

```powershell
python src\validate.py
```

Opcion 4: abrir la base con una app compatible con SQLite:

```text
database/warehouse.db
```

Nota: MySQL Workbench no abre bases SQLite directamente. MySQL y SQLite usan SQL, pero son motores diferentes.

## API Elegida

Usaremos CoinGecko `simple/price`, porque permite consultar varias criptomonedas por ID y pedir campos utiles como precio, market cap, volumen 24h, cambio 24h y fecha de actualizacion.

Criptomonedas iniciales:

- bitcoin
- ethereum
- solana
- cardano
- ripple

## Mini Clase

En este pipeline:

- `extract.py` trae datos desde internet y guarda el JSON original.
- `transform.py` convierte el JSON en una tabla CSV.
- `load.py` carga la tabla a SQLite.
- `main.py` ejecuta todo en orden.

Regla importante: en Ingenieria de Datos casi siempre guardamos primero el dato raw. Asi podemos auditar, reprocesar y corregir transformaciones sin volver a pedir los datos.

## Reto Para Sandro

Despues de ejecutar el pipeline, abre `sql/analysis.sql` y responde:

```text
1. Cual cripto tiene mayor market cap?
2. Cual tuvo mayor cambio positivo en 24h?
3. Que columna representa el momento en que extrajimos los datos?
```
