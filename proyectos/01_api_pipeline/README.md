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

