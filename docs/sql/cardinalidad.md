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
  # - SQLite
#   - SQLAlchemy
  # - MySQL
  # - PostgreSQL
  # - MariaDB
---


## Cardinalidad


- 1:1 uno a uno
- 1:n uno a muchos
- n:1 muchos a uno
- n:m muchos a muchos

Para manejar relaciones n:m se crean tablas intermedias.
La tabla intermedia se relacionará n:1 con la primera tabla y 1:n con la segunda tabla.


## VER ESQUEMA MARTIN


Esta notación permite indicar la cardinalidad entre tablas con una línea con terminación especial:

Opciones:

- One
- Many
- One (and only one)
- Zero or one
- One or many
- Zero or many