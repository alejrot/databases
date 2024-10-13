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

# Agrupar


## GROUP BY 


```sql
SELECT SupplierID, ROUND(AVG(Price),2) as promedio FROM Products 
-- WHERE filtra por registros
WHERE SupplierID IS NOT NULL
GROUP BY SupplierID
ORDER BY promedio
```

## HAVING

HAVING habilita filtrar en base a grupos. 

```sql
SELECT SupplierID, ROUND(AVG(Price),2) AS promedio FROM Products 
-- WHERE filtra por registros
WHERE ProductName IS NOT NULL
-- HAVING filtra por grupos
GROUP BY SupplierID
HAVING promedio >40
```

El HAVING debe ir **siempre después** del GROUP BY.

```sql
-- Total de operaciones de venta registradas
SELECT ProductID, Quantity FROM OrderDetails
```
```sql
-- Ventas totales por producto
SELECT ProductID, SUM(Quantity) as Total FROM OrderDetails
GROUP BY ProductID
ORDER BY TOTAL
```

```sql
-- Productos con ventas por encima de un umbral
SELECT ProductID, SUM(Quantity) as Total FROM OrderDetails
GROUP BY ProductID
HAVING TOTAL > 250
ORDER BY TOTAL
```

```sql
-- Producto más vendido
SELECT ProductID, SUM(Quantity) as Total FROM OrderDetails
GROUP BY ProductID
ORDER BY TOTAL DESC
LIMIT 1
```

Importante: no se puede concatenar funciones de agregaciones.
Ejemplo: 
```sql
MAX(SUM( campo ) )
```
Ejemplo:
```sql
-- ERROR: concatenado de funciones de agregación
SELECT ProductID, SUM(Quantity) as Total FROM OrderDetails
GROUP BY ProductID
HAVING MAX(TOTAL) 
ORDER BY TOTAL
```


```sql
-- Orden de operaciones
SELECT ... FROM ....
WHERE ...
GROUP BY ...
HAVING ...
ORDER By ...
LIMIT ...
```