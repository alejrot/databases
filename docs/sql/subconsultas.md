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





# Subconsultas (Subqueries)

Las subconsultas son consultas del tipo SELECT cuyo resultado servirá para hacer una consulta de mayor jerarquía

```sql
SELECT (SELECT ...) ...
INSERT INTO (SELECT) ...
UPDATE (SELECT ...) ...
-- (etc)
```

El **orden de la subconsulta** es la cantidad de subconsultas anidadas. Si hay una es orden 1, si hay dos es orden dos, etc. Cada gestor de bases de datos impone su propio límite al orden de las subconsultas admisibles.

```sql
-- Consulta a tabla
SELECT ProductID,
		Quantity, 
		(SELECT ProductName FROM Products AS Prod
		-- Subconsulta (subquery) a otra tabla
		WHERE Od.ProductID = ProductID) AS Nombre 
FROM OrderDetails AS Od	-- Alias de tabla
```

Alias de tablas
```sql
-- ...
-- FROM OrderDetails AS Od -- Alias de tabla
FROM [OrderDetails]  Od -- Alias de tabla
```

Doble subconsulta:
```sql
-- Consulta a tabla
SELECT ProductID,
		Quantity, 
		-- Subconsulta (subquery) a otra tabla: nombre producto
		(SELECT ProductName FROM Products 
		WHERE Od.ProductID = ProductID) AS Producto,
		-- Subconsulta (subquery) a otra tabla: precio
		(SELECT Price FROM Products
		WHERE Od.ProductID = ProductID) AS Precio 
FROM OrderDetails AS Od
```

Recaudacion por producto ordenada: 
```sql
SELECT ProductID, SUM(Quantity) as total_vendido,
	(SELECT Price FROM Products WHERE ProductID =  OD.ProductID) AS Precio,
	SUM(Quantity)*(SELECT Price FROM Products WHERE ProductID =  OD.ProductID) as Total_Recaudado
	FROM OrderDetails AS OD
GROUP BY ProductID
ORDER BY Total_Recaudado DESC
```

Seleccion de empleados con más unidades vendidas:
```sql
-- Cálculo de media de ventas 
HAVING unidades_totales > (SELECT avg(unidades_totales) FROM (
	-- Recreacion de tabla 'unidades_totales'
	SELECT (
		SELECT SUM(od.Quantity) FROM [orders] o,[OrderDetails] od
		WHERE o.EmployeeID =  e2.EmployeeID AND od.OrderID = o.OrderID
	) AS unidades_totales FROM [Employees] e2
	GROUP BY e2.EmployeeID
))
```






