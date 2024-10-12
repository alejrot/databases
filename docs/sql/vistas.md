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


# Vistas

Las vistas son tablas auxiliares que hacen referencia a las tablas de datos. Sirven para facilitar la visualización de datos recolectados de otras tablas.

Creación de la vista:
```sql
CREATE VIEW Productos_simplificados AS 

SELECT ProductID, ProductName, Price FROM Products
WHERE ProductID > 20
ORDER BY ProductID DESC  
```
Lectura de la vista:
```sql
SELECT * FROM  Productos_simplificados
```

Eliminación de vistas:
```sql
DROP VIEW IF EXISTS Productos_simplificados
```
La condición 'IF EXISTS' es recomendable para evitar posibles errores en caso que la tabla ya haya sido eliminada.




