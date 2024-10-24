---
tags:
#   - HTML5
  # - JavaScript
  # - CSS
#   - YAML
#   - MkDocs
#   - Python
#   - Docker
#   - Podman
  # - MarkDown
#   - TypeScript
  # - CSV
#   - Bash
#   - Express
#   - ReactJS
#   - NodeJS
#   - NPM
#   - PNPM
#   - ViteJS
  - SQLite
#   - SQLAlchemy
  - MySQL
  - PostgreSQL
  - MariaDB
---




# Tabla

La tabla es el formato usado por las bases de datos relacionales para alojar y organizar los datos internos.
Los datos se reparten en *campos* y *registros*:

- **Campo** es una columna de la tabla;
- **Registro** es una fila de la tabla.



- **tipos de datos**:

|Tipo| Descripción |
|:----|:-----|
|`INT`| números enteros|
|`TEXT`|campos de texto|
|`BLOB`|datos binarios: archivos, imágenes, etc. |
|`REAL`|Números flotantes - uso general|
|`NUMERIC`| Números flotantes - alta precisión|


`REAL` usa 8 bytes,
`NUMERIC` es un tipo de datos compuesto,
permite manejar nñumeros mucho más grandes y de mayor precisión 
pero es más lento de procesar.


!!! tip "Tipado dinamico"

    A diferencia de otros gestores, SQLite permite tipos de datos dinámico. 
    Sin embargo esto es considerado una mala práctica.

- **Valores por defecto**
- **Primary key**




