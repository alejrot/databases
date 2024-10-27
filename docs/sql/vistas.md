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

Las vistas son tablas auxiliares que hacen referencia a las tablas de datos. 
Sirven para facilitar la visualización de datos recolectados de otras tablas.

## Creación

Creación de la vista:
```sql
-- Creación de vista
CREATE VIEW Productos_simplificados AS 
-- Consulta equivalente
SELECT ProductID, ProductName, Price FROM Products
WHERE ProductID > 20
ORDER BY ProductID DESC  
```
# Lectura

Lectura de la vista:
```sql
SELECT * FROM  Productos_simplificados
```


!!! warning "Visibilidad"

    Si se crea una vista con igual nombre que una tabla,
    la vista tendrá prioridad de consulta respecto a la tabla.



## Eliminación

Eliminación de vistas:

```sql
DROP VIEW IF EXISTS Productos_simplificados
```
La condición `IF EXISTS` es recomendable para evitar posibles errores en caso que la vista ya haya sido eliminada.




!!! warning "Abuso de vistas"

    Las vistas son consultas y como tales exigen capacidad de procesamiento.
    No abusar de su uso.

