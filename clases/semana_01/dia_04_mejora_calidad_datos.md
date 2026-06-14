# Dia 04 - Mejorar Reglas De Calidad

## Que Mejoramos

El proyecto ya tenia validaciones basicas. Hoy agregamos reglas mas completas para acercarlo a un pipeline real.

## Reglas Nuevas

- `market_cap_usd_positive`: la capitalizacion de mercado debe ser mayor a 0.
- `volume_24h_usd_not_negative`: el volumen 24h no debe ser negativo.
- `extracted_at_utc_not_null`: todo registro debe tener fecha de extraccion.

## Por Que Importa

Un pipeline puede ejecutarse sin fallar y aun asi guardar datos malos.

Ejemplo:

```text
coin_id = bitcoin
price_usd = 0
market_cap_usd = vacio
extracted_at_utc = vacio
```

El codigo podria correr, pero el dato no seria confiable.

## Regla Importante

`change_24h_pct` puede ser negativo.

Eso no es error, porque una criptomoneda puede bajar de precio.

## Explicacion Para Entrevista

```text
Agregue validaciones de calidad para asegurar que las columnas criticas no esten vacias, que las metricas financieras principales tengan valores validos y que no existan duplicados por criptomoneda y snapshot de extraccion.
```

## Mini Reto

Explica en tus palabras:

```text
1. Por que volume_24h_usd puede ser 0, pero no negativo?
2. Por que change_24h_pct si puede ser negativo?
3. Que problema causa un extracted_at_utc vacio?
```

