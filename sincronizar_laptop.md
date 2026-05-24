# Sincronizar Este Proyecto Con La Laptop

Este proyecto vive en archivos. Los chats pueden no sincronizarse, pero el aprendizaje si queda guardado si usamos GitHub.

## Paso 1 - Crear Repo En GitHub

En la computadora actual:

1. Entra a GitHub.
2. Crea un repositorio nuevo.
3. Nombre sugerido: `data-engineering-sandro`.
4. No marques README, `.gitignore` ni licencia, porque este proyecto ya los tiene.

## Paso 2 - Conectar Este Proyecto

En PowerShell, dentro de:

```powershell
C:\Users\Sandro\Documents\New project
```

ejecuta:

```powershell
git remote add origin https://github.com/TU_USUARIO/data-engineering-sandro.git
git branch -M main
git push -u origin main
```

Cambia `TU_USUARIO` por tu usuario real de GitHub.

## Paso 3 - Descargar En La Laptop

En la laptop:

```powershell
git clone https://github.com/TU_USUARIO/data-engineering-sandro.git
cd data-engineering-sandro
```

## Paso 4 - Rutina Normal

Antes de estudiar:

```powershell
git pull
```

Despues de avanzar:

```powershell
git add .
git commit -m "avance de estudio"
git push
```

## Paso 5 - Continuar Con Codex En La Laptop

Abre la carpeta clonada con Codex y escribe:

```text
Lee contexto_codex.md, ruta_aprendizaje.md y bitacora.md. Continuemos desde ahi.
```

