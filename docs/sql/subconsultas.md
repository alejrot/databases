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

Las subconsultas son consultas auxiliares
cuyo resultado servirá para hacer una consulta de mayor jerarquía:

```sql
SELECT (SELECT ...) ...
INSERT INTO (SELECT) ...
UPDATE (SELECT ...) ...
-- (etc)
```

Las subconsultas son de sólo lectura (comando `#!sql SELECT`), 
por ello no pueden modificar los datos guardados por sí mismas.


## Orden 

El **orden de la subconsulta** es la cantidad de subconsultas anidadas. 
Si hay una es orden 1, si hay dos es orden dos, etc. 
Cada gestor de bases de datos impone su propio límite al orden de las subconsultas admisibles.

EL estándar SQL impone un máximo de 16 subconsultas, 
pero hay gestores que soportan muchas más.


## Tipos

Las *subqueries* pueden clasificarse por tipos según resultado buscado:

- subconsultas de valor unico
- subconsultas de fila
- subconsultas de tabla

También pueden clasificarse según su correlacion con la tabla principal:


- correlacionales
- no correlacionales

Sin embargo, en el lenguaje coloquial rara vez se especifica qué tipo de subconsulta se usó en cada caso.




## Uso




Se consultan los productos y cantidades de la tabla de pedidos,
llamada `OrderDetails`...

```sql
-- 518 órdenes, un producto por orden
SELECT ProductID,Quantity AS Cantidad FROM OrderDetails 
```

... pero se devuelven los IDs de los productos, no su nombre:

|ProductID|Cantidad|
|---|---|
|11|12|
|42|10|
|72|5 |
|...|...|

Éste se encuentra en otra tabla llamada `Products`.

```sql
-- 77 productos en el catálogo
SELECT ProductID, ProductName AS Nombre FROM Products 
```

|ProductID|	Nombre|
|---|---|
|1 | Chais|
|2 | Chang|
|3 | Aniseed Syrup|
|4 | Chef Anton's Cajun Seasoning|
|...|...|



La última instrucción se agrega adentro de la primera como *subconsulta*:

```sql hl_lines="5"
SELECT 
	ProductID,
	Quantity, 
	-- Subconsulta a la tabla 'Products'
	(SELECT ProductName FROM Products) AS Nombre  	-- MAL: nombre producto erróneo 
FROM OrderDetails;
```
... pero a todos los productos les asigna el nombre *'Chais'*, 
que es el nombre del primer producto.
Se agrega a la subconsulta la condición para acoplar los registros de ambas tablas,
que es la coincidencia entre ambas tablas del valor del campo `ProductID`: 

```sql title="Subconsulta" hl_lines="5-6"
-- Consulta a la tabla 'OrderDetails'
SELECT ProductID as pID,
	Quantity as Cantidad, 
	-- Subconsulta a la tabla 'Products'- con condición de acoplamiento
	(SELECT ProductName FROM Products 
	WHERE OrderDetails.ProductID = ProductID) AS Producto
FROM OrderDetails;
```
dando por resultado la combinación correcta de cantidades y nombres para cada pedido registrado:

|pID|Cantidad|Producto|
|---|---|---|
|11	|12	|Queso Cabrales|
|42	|10	|Singaporean Hokkien Fried Mee|
|72	|5	|Mozzarella di Giovanni|
|...|...|...|





## Alias de tabla


Las tablas obtenidas pueden tener un alias, 
un nombre alternativo para poder consultarlas.
Este alias se crea con ayuda del operador `#!sql AS` o con el uso de corchetes:

<div class="grid" markdown>
```sql title="Alias - operador AS"
-- (operaciones previas)
FROM OrderDetails AS Od -- operador 'AS'
```

```sql title="Alias - con corchetes"
-- (operaciones previas)
-- ...
FROM [OrderDetails]  Od -- corchetes
```
</div>

En el ejemplo se repite la subconsulta previa implementando un alias para la tabla de salida:

```sql title="Subconsulta - Alias de tabla" hl_lines="7"
-- Consulta a la tabla 'OrderDetails'
SELECT ProductID,
		Quantity, 
		-- Subconsulta a la tabla 'Products'
		(SELECT ProductName FROM Products AS Prod
		WHERE Od.ProductID = ProductID) AS Nombre 
FROM OrderDetails AS Od	-- 'Od': alias de tabla
```


## Múltiples subconsultas

Una misma consulta puede incluir varias subconsultas internas.

En el ejemplo se consultan el nombre de cada producto y precio por separado:

```sql title="Doble subconsulta - producto y precio"
-- Consulta a tabla
SELECT ProductID,
		Quantity AS Cantidad, 
		-- Subconsulta Nº1 a la tabla 'Products': nombre producto
		(SELECT ProductName FROM Products 
		WHERE Od.ProductID = ProductID) AS Producto,
		-- Subconsulta Nº2 a la tabla 'Products': precio
		(SELECT Price FROM Products
		WHERE Od.ProductID = ProductID) AS Precio 
FROM OrderDetails AS Od
```

Este es el resultado:

|ProductID|	Cantidad|	Producto|	Precio|
|---|---|---|---|
|11|12|	Queso Cabrales|	21|
|42|10|	Singaporean Hokkien Fried Mee|	14|
|72|5	|Mozzarella di Giovanni|34.8|
|14|9	|Tofu	|23.25|
|...|...|...|...|
<!-- 
Recaudacion por producto ordenada:  
-->
## Subconsultas de orden superior

Las subconsultas de orden superior se consiguen anidando subconsultas.

En este ejemplo, se consulta el precio de los productos para poder calcular el dinero recaudado por producto (`cantidad * precio`)

```sql title="subconsulta orden superior - recaudacion por producto"
SELECT ProductID, 
	SUM(Quantity) as Cantidad,
	--  subconsulta de primer orden: precio
	(SELECT Price FROM Products 
	WHERE ProductID =  OD.ProductID) AS Precio,
	--  subconsulta de segundo orden: total recaudado por ventas
	SUM(Quantity)*(
		-- sub-subconsulta: precios de cada producto
		SELECT Price FROM Products 
			WHERE ProductID =  OD.ProductID
			) AS Total_Recaudado
	FROM OrderDetails AS OD
GROUP BY ProductID
ORDER BY Total_Recaudado DESC
```

Resultado:

|ProductID|	Cantidad|Precio|Total_Recaudado|
|---|----|---|---|
|38| 239|263.5|	62976.5|
|29| 168|123.79|20796.72|
|59| 346|55|	19030|
|...|...|...|...|


Si al ejemplo previo se le agrega una nueva subconsulta se puede adjuntar también el nombre de cada producto: 


```sql title="ejemplo integrador - producto, precio y recaudación"
SELECT ProductID, 
	-- Subconsulta Nº1 a la tabla 'Products': nombre producto
	(SELECT ProductName FROM Products WHERE ProductID = OD.ProductID) as Producto,
	-- Subconsulta Nº2 a la tabla 'Products': precio
	(SELECT Price FROM Products WHERE ProductID = OD.ProductID) as Precio,
	SUM(Quantity) AS Cantidad,
	--  Subconsulta Nº3 a la tabla 'Products' (segundo orden): total recaudado por ventas
	(SUM(Quantity) * (
		-- sub-subconsulta: precios de cada producto
		SELECT Price FROM Products WHERE ProductID = OD.ProductID)
		) AS Total_Recaudado
FROM [OrderDetails] OD
GROUP BY ProductID	
ORDER BY total_recaudado DESC;
```

Resultado:

|ProductID|	Producto|	Precio|	Cantidad|	Total_Recaudado|
|---|---|----|---|---|
|38|Côte de Blaye|	263.5|	239|	62976.5|
|29|Thüringer Rostbratwurst	|123.79|	168|	20796.72|
|59|Raclette Courdavault|	55|	346	|19030|
|...|...|...|...|...|




## Ejemplos adicionales

??? example "Ordenado de empleados por Nº de ventas"

	Esta consulta cuenta el total de objetos vendidos por cada empleado.

	```sql
	SELECT FirstName,LastName,
	(
		SELECT SUM(od.Quantity) FROM [orders] o, [OrderDetails]  od
		WHERE o.EmployeeID = e.EmployeeID AND od.OrderID=o.orderID
	) AS unidades_totales
	FROM [Employees] e
	```

	Hay 10 empleados en la tienda:

	|FirstName|LastName	|unidades_totales|
	|---|---|---|
	|Nancy	|Davolio	|1924|
	|Andrew|	Fuller	|1315|
	|Janet	|Leverling	|1725|
	|Margaret	|Peacock	|3232|
	|Steven	|Buchanan|	778|
	|Michael|	Suyama|	1094|
	|Robert|	King|	733|
	|Laura|	Callahan|	1293|
	|Anne|	Dodsworth|	649|
	|Adam|	West	|*Null*|

	(el último no tiene ninguna venta registrada a su nombre) 



??? example "Empleados que vendieron más de la media"

	```sql
	SELECT FirstName, LastName, (
			-- subquerie: ventas por empleado
			SELECT SUM(od.Quantity) FROM [orders] o, [OrderDetails]  od
			WHERE o.EmployeeID = e.EmployeeID AND od.OrderID=o.orderID
		) AS unidades_totales
	FROM [Employees] e
	-- sección filtrado --> media sobre tabla virtual
	WHERE unidades_totales < ( 
		-- cálculo de la media de ventas por empleado
		SELECT AVG(unidades_totales) FROM (
			SELECT (
				-- subquerie: ventas por empleado
				SELECT SUM(od.Quantity) FROM [orders] o, [OrderDetails] od
				WHERE o.EmployeeID=e2.EmployeeID AND  od.orderID=o.orderID
				) AS unidades_totales
			FROM  [Employees] e2
			GROUP BY e2.EmployeeID
			)
		)
	```

	Hay 6 empleados cuya cantidad de ventas supera la media:

	|FirstName	|LastName	|unidades_totales|
	|---|---|---|
	|Andrew	|Fuller	|1315|
	|Steven	|Buchanan|	778|
	|Michael|Suyama	|1094|
	|Robert	|King|	733|
	|Laura	|Callahan	|1293|
	|Anne	|Dodsworth|	649|



	Nótese que la subconsulta del ejemplo previo debió repetirse dos veces para obtener el resultado final.
	Una alternativa superadora a las subqueries son las *uniones* o *joins*, que se explican más adelante.


