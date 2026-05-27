# Dia 03 - Calidad De Datos

## Que Aprendemos

Un pipeline no solo debe correr. Debe correr con datos confiables.

Calidad de datos significa revisar reglas como:

- La tabla no esta vacia.
- Las columnas importantes no tienen nulos.
- Los precios no son negativos.
- No hay duplicados en la misma ejecucion.

## Archivo Principal

```text
proyectos/01_api_pipeline/src/validate.py
```

## Ejecutar Validaciones

Desde `proyectos/01_api_pipeline`:

```powershell
python src\validate.py
```

## Checks Creados

- `table_has_rows`: la tabla tiene filas.
- `coin_id_not_null`: ninguna cripto tiene nombre vacio.
- `price_usd_positive`: el precio debe ser mayor a cero.
- `no_duplicate_coin_snapshot`: una cripto no debe repetirse dentro del mismo snapshot.

## Concepto Clave

Una validacion convierte una suposicion en una regla comprobable.

Ejemplo:

```text
"El precio siempre deberia ser positivo"
```

se convierte en:

```sql
SELECT COUNT(*)
FROM crypto_prices
WHERE price_usd IS NULL OR price_usd <= 0;
```

Si el resultado es `0`, la regla pasa.

## Reto Para Sandro

Explica con tus palabras:

```text
1. Por que un pipeline que corre no siempre es un pipeline correcto?
2. Que significa detectar duplicados por coin_id y extracted_at_utc?
3. Que otra regla de calidad agregarias?
```

