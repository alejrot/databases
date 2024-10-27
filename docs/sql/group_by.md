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
-- ordena los promedios de precios por proveedor
SELECT SupplierID, ROUND(AVG(Price),2) as promedio FROM Products 
GROUP BY SupplierID
```

Pasos:
- lee la tabla de productos;
- agrupa todos los productos incluidos en listas, en base al proveedor de cada uno;
- les calcula el precio promedio de cada lista.






```sql
SELECT SupplierID, ROUND(AVG(Price),2) as promedio FROM Products 
-- WHERE filtra por registros
WHERE SupplierID IS NOT NULL
GROUP BY SupplierID
ORDER BY promedio
```

`WHERE` siempre va antes de `GROUP BY`.
Primero se filtran los registros 
y luego se agrupa el resultado.


## HAVING

<!-- HAVING habilita filtrar en base a grupos.  -->


!!! danger "MAL"

    `WHERE` no permite hacer referencia a la funcion de agregación

    ```sql
    SELECT SupplierID, ROUND(AVG(Price),2) AS promedio FROM Products 
    WHERE promedio >40    -- MAL
    GROUP BY SupplierID
    ```

    ```sql
    SELECT SupplierID, ROUND(AVG(Price),2) AS promedio FROM Products 
    GROUP BY SupplierID
    HAVING promedio >40    -- BIEN
    ```


!!! info "`HAVING` vs `WHERE`"

    `WHERE` filtra sobre campos,
    en tanto que 
    `HAVING` filtra sobre grupos.


HAVING habilita filtrar en base a operaciones realizadas sobre grupos. 

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

!!! warning "Concatenar agregaciones"

    No se puede concatenar funciones de agregaciones.
    
    Ejemplo: 
    ```sql
    MAX(SUM( campo ) )
    ```

    Ejemplo:
    ```sql
    -- ERROR: concatenado de funciones de agregación
    SELECT ProductID, SUM(Quantity) as TOTAL FROM OrderDetails
    GROUP BY ProductID
    HAVING MAX(TOTAL) -- ERROR
    ORDER BY TOTAL
    ```

    Para evitar este problema existen las subconsultas (*subqueries*)



## Orden de cláusulas

```sql
-- Orden de operaciones
SELECT ... FROM ....
WHERE ...
GROUP BY ...
HAVING ...
ORDER By ...
LIMIT ...
```