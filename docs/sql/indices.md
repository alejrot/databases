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

# Indices

Los índices son una herramienta auxiliar que permite mejorar los tiempos de consulta para ciertos campos de interés. Los índices se crean con la sintaxis: 
```sql
CREATE INDEX <alias> ON <tabla> (<campo>)
```

Ejemplo: índice para los nombres de producto

```sql
-- Indice "nombre" apuntando al campo "ProductName" en tabla "Products"
CREATE INDEX nombre ON Products (ProductName)
```

La consulta de campos se realiza normalmente. No se requiere usar el alias. 

Ejemplos:

```sql
SELECT * FROM Products
SELECT * FROM Products WHERE  ProductName = "Chais"
```

Los índices sirven también como indicadores únicos para ciertos campos de interés, sirviendo como alternativa ante 
```sql
-- Indice unico compuesto para empleados (nombres o apellidos podrían estar repetidos)
-- Crear este índice impedirá la repetición de pares nombre - apellido
CREATE UNIQUE INDEX name ON Employees (FirstName, LastName)
```

Los indices consumen mucho espacio en disco. Esto se agrava cuando se necesita actualizar datos indexados. Por ello hay que ser prudente a la hora de crear índices. 

Las foreign keys son campos recomendados para indexar.


Los indices se eliminan con la orden DROP:

```sql
DROP INDEX <alias>
```

Para ponerle nombre a los indices es habitual usar la nomenclatura:
```
idx_<nombre_tabla>_<nombre_campo>
```

Ejemplo:

```sql
-- Consulta con unión interna
SELECT * FROM OrderDetails od
INNER JOIN Orders o
WHERE OrderDate > "1996-07-04"
AND od.Quantity > 10

-- Crear indices
CREATE INDEX cantidad ON OrderDetails (Quantity);
CREATE INDEX fecha	  ON Orders (OrderDate);

-- eliminar indices
DROP INDEX cantidad ;
DROP INDEX fecha	;
```

