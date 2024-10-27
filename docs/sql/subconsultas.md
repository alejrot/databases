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

Las subconsultas son consultas del tipo SELECT cuyo resultado servirá para hacer una consulta de mayor jerarquía.
Las subconsultas no pueden modificar los datos guardados.

```sql
SELECT (SELECT ...) ...
INSERT INTO (SELECT) ...
UPDATE (SELECT ...) ...
-- (etc)
```

El **orden de la subconsulta** es la cantidad de subconsultas anidadas. Si hay una es orden 1, si hay dos es orden dos, etc. 

Cada gestor de bases de datos impone su propio límite al orden de las subconsultas admisibles.

EL estándar SQL impone un máximo de 16 subconsultas, pero hay gestores que soportan muchas más.


!!! info  "SELECT"

	Las subconsultas siempre son el comando SELECT, 
	es decir son de sólo lectura. 
	Sólo la consulta principal puede ser de otro tipo.


Tipos según resultado

- subconsultas de valor unico
- subconsultas de fila
- subconsultas de tabla

Según correlacion con tabla principal 


- correlacionales
- no correlacionales





ejemplo:

Se consultan  productos y cantidades de la tabla de pedidos...

```sql
SELECT ProductID,Quantity FROM OrderDetails
```

... pero se devuelven los IDs de los productos, no su nombre. 
Éste se encuentra en otra tabla.
```sql
SELECT ProductName FROM Products AS nombre
```
La última instruccion se agrega a la primera como subconsulta:

```sql
SELECT 
	ProductID,
	Quantity, 
	-- MAL
	(SELECT ProductName FROM Products) AS nombre
FROM OrderDetails;
```



```sql title="Subconsulta"
-- Consulta a la tabla 'OrderDetails'
SELECT ProductID as pID,
	Quantity, 
	-- Subconsulta a la tabla 'Products'
	(SELECT ProductName FROM Products WHERE OrderDetails.ProductID = ProductID) AS Nombre
FROM OrderDetails;
```






```sql title="Subconsulta - Alias de tabla"
-- Consulta a la tabla 'OrderDetails'
SELECT ProductID,
		Quantity, 
		-- Subconsulta a la tabla 'Products'
		(SELECT ProductName FROM Products AS Prod
		WHERE Od.ProductID = ProductID) AS Nombre 
FROM OrderDetails AS Od	-- Alias de tabla
```

Alias de tablas
```sql title="Sintaxis de Alias"
-- ...
FROM OrderDetails AS Od -- AS
FROM [OrderDetails]  Od -- corchetes
```

Doble subconsulta:
```sql title="Doble Subconsulta"
-- Consulta a tabla
SELECT ProductID,
		Quantity, 
		-- Subconsulta (subquery) a la tabla 'Products': nombre producto
		(SELECT ProductName FROM Products 
		WHERE Od.ProductID = ProductID) AS Producto,
		-- Subconsulta (subquery) a la tabla 'Products': precio
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


```sql
SELECT ProductID, 
	(SELECT ProductName FROM Products WHERE ProductID = OD.ProductID) as Nombre,
	(SELECT Price FROM Products WHERE ProductID = OD.ProductID) as Price,
	SUM(Quantity) AS total_vendido,
	(SUM(Quantity) * (SELECT Price FROM Products WHERE ProductID = OD.ProductID)) as total_recaudado
FROM [OrderDetails] OD
GROUP BY ProductID	
ORDER BY total_recaudado DESC;
```






Seleccion de empleados con más unidades vendidas:

***MAL***
```sql
-- MAL
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




## Ejercicio subconsultas

Ordenado de empleados por Nº de ventas:
```sql
-- 
SELECT FirstName,LastName,
(
	SELECT SUM(od.Quantity) FROM [orders] o, [OrderDetails]  od
	WHERE o.EmployeeID = e.EmployeeID AND od.OrderID=o.orderID
) AS unidades_totales
FROM [Employees] e
```


Empleados que vendieron más de la media:

```sql
SELECT FirstName,LastName,
(
	SELECT SUM(od.Quantity) FROM [orders] o, [OrderDetails]  od
	WHERE o.EmployeeID = e.EmployeeID AND od.OrderID=o.orderID
) AS unidades_totales
FROM [Employees] e
-- sección ordenado --> media sobre tabla virtual
WHERE unidades_totales < (SELECT AVG(unidades_totales) FROM (
	SELECT (SELECT SUM(od.Quantity) FROM [orders] o, [OrderDetails] od
	WHERE o.EmployeeID=e2.EmployeeID AND  od.orderID=o.orderID) as unidades_totales
	FROM  [Employees] e2
	GROUP BY e2.EmployeeID
))
```









