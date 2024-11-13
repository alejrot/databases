

# Ejercicio Integrador - Recaudación 

A modo de integración se propone crear las consultas necesarias para calcular los montos de recaudación descritos en la [base de datos NorthWind](../anexos/northwind.md).

Se eligen los siguientes criterios:

- Por recaudación según cada producto.
- Por recaudación según cada empleado de la tienda.


## 1. Tablas relevantes

Se describen las tablas de la base de datos que tienen información importante para los ejercicios y se enumeran los campos de interés de cada una.


### `Orders`

Hay 196 órdenes de compra en total,
las cuales pueden agrupar distintos productos (no especificados aquí) 
y cada una es manejada por un empleado particular.


```yaml
Orders:
    - OrderID	
    - EmployeeID	
```


### `OrderDetails`

Las órdenes se desglosan en 518 *"detalles de orden"*. Cada uno consiste en un producto elegido para comprar y su cantidad pedida. 

```yaml 
OrderDetails:
    - OrderDetailID	
    - OrderID	
    - ProductID	
    - Quantity
```

### `Products`

El catálogo de productos (77 en total) tiene su propia tabla, donde se incluye el nombre y precios de cada uno. 

```yaml  
Products:
    - ProductID
    - ProductName
    - Price
```

### `Employees`

Los datos de todos los empleados son condensados en esta tabla. Son 10 personas contratadas.

```yaml 
Employees:
    - EmployeeID
    - LastName
    - FirstName
```

## 2. Agrupar detalles de órdenes 


Se extiende la tabla `OrderDetails` 
agregando los precios de cada producto elegido mediante una unión `#!sql INNER JOIN`
y se crea una vista de dicha consulta, 
llamándola `OrderDetailsExtended` :


```sql 
-- Creación de vista
CREATE VIEW IF NOT EXISTS OrderDetailsExtended AS 
-- inner join implicita
SELECT  OrderDetailID, 
    OrderID, 
    P.ProductID, 
    Quantity, 
    Price ,
    Quantity * Price AS ProductOrderRevenue 
FROM OrderDetails OD, Products P
WHERE OD.ProductID=P.ProductID
```

Esta vista puede consultarse como una tabla cualquiera:

```sql
SELECT * FROM OrderDetailsExtended
```


|OrderDetailID|	OrderID|	ProductID|	Quantity|	Price|	ProductOrderRevenue|
|---|---|---|---|---|---|
|1|10248|11|12|	21	|252|
|2|10248|42|10|	14	|140|
|3|10248|72|5	|34.8|	174.0|
|...|...|...|...|...|...|
|517	|10443|	11|	6|	21|	126|
|518	|10443|	28|	12|	45.6|	547.2|



## 3. Recaudación por producto


Con una consulta se calcula el total de dinero recaudado con cada producto en venta
y se le asigna la lista `ProductsRevenue`.
Usa los datos de la vista `OrderDetailsExtended` 
y le agrega el nombre de cada producto mediante una  unión `#!sql LEFT JOIN`


```sql
CREATE VIEW IF NOT EXISTS ProductsRevenue AS

SELECT 
	P.ProductID, 
	ProductName, 
	SUM(ProductOrderRevenue) AS ProductRevenue
FROM Products P
LEFT JOIN OrderDetailsExtended ODE
ON P.ProductID=ODE.ProductID
GROUP BY P.ProductID
```


```sql
SELECT * FROM ProductsRevenue
```

|ProductID|	ProductName|	ProductRevenue|
|---|---|---|
|1|	Chais	|2862|
|2|	Chang	|6479|
|3|	Aniseed Syrup|	800|
|4|	Chef Anton's Cajun Seasoning	|2354|
|...|...|...|
|76|	Lakkalikööri|	3564|
|77|	Original Frankfurter grüne Soße|	1404|


## 4. Recaudación por empleado


La vista `OrderDetailsExtended` se une con la tabla `Orders`. 
Esto permitirá agregar la información de los empleados
y se usa la agregación para calcular los totales de ingresos correspondientes a cada empleado,
creando la vista `EmployeesSales`:

```sql
-- Creación de vista
CREATE VIEW IF NOT EXISTS EmployeesSales AS 

SELECT    
    -- ID de cada empleado con ingresos
	EmployeeID,
    -- suma por ventas de cada empleado
    SUM(ProductOrderRevenue) AS EmployeeSales
    -- inner join implicita
    FROM OrderDetailsExtended ODE, Orders O
WHERE ODE.OrderID=O.OrderID
-- agregacion por ID de empleado empleado
GROUP BY EmployeeID
ORDER BY EmployeeID
```
De esta forma se muestran todas las recaudaciones y a qué empleado le corresponde cada una:

```sql
SELECT * FROM EmployeesSales 
```


|EmployeeID|	EmployeeSales|
|---|---|
|1|57690.39|
|2|32503.16|
|3|42838.35|
|4|105696.5|
|5|27480.8|
|6|25399.25|
|7|39772.3|
|8|39309.38|
|9|15734.1|


Con una `#!sql LEFT JOIN` se puede forzar la visualización de todos los empleados 
y a cada uno se le asigna el valor de ventas conseguido:

```sql
-- Creación de vista
CREATE VIEW IF NOT EXISTS EmployeesRevenue AS 

SELECT 
    E.EmployeeID,
	FirstName ||" "||LastName AS Employee,
	EmployeeSales 
FROM  Employees E
-- se muestra a todos los empleados
LEFT JOIN EmployeesSales  S 
ON S.EmployeeID=E.EmployeeID
ORDER BY E.EmployeeID
```

La vista creada se llamó `EmployeesRevenue` y se consulta para ver el resultado

```sql
SELECT * FROM EmployeesRevenue 
```
Este es el resultado final:

|EmployeeID|	Employee|	EmployeeSales|
|---|---|---|
|1	|Nancy Davolio|	57690.39|
|2	|Andrew Fuller|	32503.16|
|3	|Janet Leverling|	42838.35|
|4	|Margaret Peacock|	105696.5|
|5	|Steven Buchanan|	27480.8|
|6	|Michael Suyama|	25399.25|
|7	|Robert King|	39772.3|
|8	|Laura Callahan	|39309.38|
|9	|Anne Dodsworth|	15734.1|
|10|	Adam West||	



## 5. Conexion con Python




[Descarga de rutina Python "recaudar.py" ](../anexos/recaudar.py){ .md-button .md-button--primary }


??? abstract "Ver código de rutina Python"

    ```sql title="recaudar.py" linenums="1" 
    --8<- "docs/anexos/recaudar.py"
    ```
    { data-search-exclude }