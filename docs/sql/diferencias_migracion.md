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



# Diferencias entre gestores - Migración



## Características de los gestores

### SQLite
- Es un gestor embebido
- Trabaja con archivo único
- Es ideal para aplicaciones embebidas y prototipos
- No sirve para aplicaciones de gran escala o de alto rendimiento

### MySQL
- Es un gestor basado en servidor
- Puede trabajar con múltiples archivos
- Es ideal para aplicaciones de gran escala o de alto rendimiento

### PostgreSQL
- Es un gestor basado en servidor
- Puede trabajar con múltiples archivos
- Es ideal para aplicaciones de gran escala o de alto rendimiento
- Tiene extensiones propias

### SQLServer
- Es de pago
- Es un gestor basado en servidor
- Puede trabajar con múltiples archivos
- Es ideal para aplicaciones de gran escala o de alto rendimiento
- Tiene extensiones propias





## Migracion entre gestores

1 - Se adaptan las consultas para crear el formato de tablas en el nuevo gestor de base de datos;
2 - Para migrar los datos se recomienda exportar cada tabla de la base de datos en archivos CSV e importarlos con el nuevo gestor.