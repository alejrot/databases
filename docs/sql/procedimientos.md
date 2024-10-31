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
  - SQLAlchemy
  - MySQL
  - PostgreSQL
  - MariaDB
---


<!-- 
# Procedimientos y Funciones -->


# Procedimientos almacenados (Stored Procedures)

Los procedimientos almacenados son consultas prearmadas que se pueden utilizar repetidas veces. 
Son el equivalente a las funciones de los lenguajes de programación.

SQLite **no soporta** procedimientos almacenados debido a su tipo de armado, a diferencia de otras bases de datos como PostgreSQL, MySQL, etc. 
Sin embargo esta limitación puede saltearse implementando las *queries* prearmadas en el programa 'cliente' de la base de datos.
Estas son las *user defined functions*, las cuales se explican más adelante.


