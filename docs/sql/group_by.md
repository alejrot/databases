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


`#!sql GROUP BY` permite "repartir" (agrupar) los registros leídos de una tabla en base a los valores de un campo elegido.
Como analogía, es como si este comando creara varias tablas paralelas que se reparten las filas entre sí.
Una vez reordenadas las filas se aplica la función de agregación elegida de manera paralela para cada grupo, 
obteniéndose un resultado separado para cada grupo.

### Uso básico

Supóngase el ejemplo de la tabla `Products`, 
la cual tiene 77 productos distintos.
Si se buscara calcular el precio promedio de los productos según su proveedor:

```sql title="Agrupado"
-- ordena los promedios de precios por proveedor
SELECT SupplierID, ROUND(AVG(Price),2) AS promedio FROM Products 
-- GROUP BY clasifica los registros
GROUP BY SupplierID
```

entonces la función `AVG()` usada calculará un promedio independiente para cada uno de los 29 proveedores disponibles:

|SupplierID|	promedio|
|---|---|
|1|15.67|
|2|20.35|
|3|31.67|
|...|...|
|28|	44.5|
|29|	38.9|


### Filtrado y ordenado

El orden general de operaciones indicado es:

1. se filtran los registros de la tabla (`#!sql WHERE`); 
2. se agrupan los registros en grupos `#!sql GROUP BY`;
3. se ordena el resultado (`#!sql ORDER BY`);
4. limitar el número de registros de salida (`#!sql LIMIT`).



Supóngase que además se necesita filtrar los datos anómalos de la tabla.
En tal caso se usa la cláusula `#!sql WHERE`,
la cual siempre va antes de `#!sql GROUP BY`:


```sql title="Agrupado - con filtrado y ordenado"
SELECT SupplierID, ROUND(AVG(Price),2) as promedio FROM Products 
-- WHERE filtra por registros
WHERE SupplierID IS NOT NULL
-- GROUP BY clasifica los registros
GROUP BY SupplierID
-- ORDER BY ordena los resultados de la funcion de agregación
ORDER BY promedio
```

En este caso se obtienen los precios promedio de los 29 proveedores pero ordenados de menor a mayor:

|SupplierID|	promedio|
|---|---|
|10|	4.5|
|21|	10.75|
|...|...|
|4|	46.0|
|18|	140.75|




!!! example "Ejemplo adicional: top 3 de ventas"

    Supóngase que se desea conocer a los 3 productos más vendidos. 
    Entonces al agrupado y al ordenamiento se agrega la limitación de resultados con el operador `#!sql LIMIT`:

    ```sql
    -- Lectura de la tabla de ventas
    SELECT ProductID, SUM(Quantity) as Ventas FROM OrderDetails
    -- WHERE filtra por registros
    WHERE ProductID IS NOT NULL
    -- Agrupado por producto
    GROUP BY ProductID
    -- Ordenado de manera descendente - los más vendidos primero
    ORDER BY Ventas DESC
    -- seleccion de los primeros 3 registros
    LIMIT 3
    ``` 

    Resultado:

    |ProductID|Ventas|
    |---|---|
    |31|458|
    |60|430|
    |35|369|




## HAVING



`#!sql HAVING` habilita filtrar registros en base a operaciones realizadas **sobre grupos**. 
Por este motivo, el `#!sql HAVING` debe ir **siempre después** del `#!sql GROUP BY`.

Por ejemplo, imagínese que se necesita calcular el total de ventas de una lista de productos.
La tabla `OrderDetails` registra un total de 518 pedidos,
donde cada pedido consta de un único producto y su cantidad deseada por cada cliente y en cada compra:

```sql title="conteo de registros"
-- Total de operaciones de venta registradas
SELECT COUNT(OrderID) FROM OrderDetails
```

El total de ventas de cada producto se obtiene por agregación:

```sql title="suma total por grupo" hl_lines="3"
-- Ventas totales por producto
SELECT ProductID, SUM(Quantity) as Ventas FROM OrderDetails
GROUP BY ProductID
```

Donde se observa que hay 77 totales de ventas, uno por producto:


|ProductID	|Ventas|
|---|---|
|1|	159|
|2|	341|
|3|	80|
|...|...|
|76|198|
|77|108|


Si además se necesita mostrar solamente aquellos productos que superen un umbral de ventas se recurre a la cláusula `#!sql HAVING`, a la cual se le puede agregar un ordenamiento: 

```sql title="Umbral de grupos"  hl_lines="4-5"
-- Productos con ventas por encima de un umbral
SELECT ProductID, SUM(Quantity) as Ventas FROM OrderDetails
GROUP BY ProductID
HAVING Ventas > 350
ORDER BY Ventas 
```
En este caso sólo pasaron tres productos:

|ProductID|	Ventas |
|---|---|
|35	|369|
|60	|430|
|31	|458|



## `#!sql HAVING` vs `#!sql WHERE`

`#!sql WHERE` filtra sobre campos,
en tanto que 
`#!sql HAVING` filtra sobre el resultado de las funciones de agregación.

<div class="grid" markdown>

!!! failure "`#!sql WHERE`"

    `#!sql WHERE` no permite trabajar con la salida de las funciones de agregación:

    ```sql hl_lines="4"
    SELECT SupplierID, 
        AVG(Price) AS promedio 
        FROM Products 
    WHERE promedio > 40    -- MAL
    GROUP BY SupplierID
    ```
!!! success "`#!sql HAVING`"

    `#!sql HAVING` está pensado para trabajar con la salida de las funciones de agregación:

    ```sql hl_lines="5"
    SELECT SupplierID, 
        AVG(Price) AS promedio 
        FROM Products 
    GROUP BY SupplierID
    HAVING promedio > 40    -- BIEN
    ```
</div>

!!! warning "Concatenar agregaciones"

    No se puede concatenar funciones de agregación.
    
    Ejemplo: 

    ```sql
    MAX(SUM( campo ) ) -- ERROR
    ```

    Ejemplo:

    ```sql
    -- ERROR: concatenado de funciones de agregación
    SELECT ProductID, SUM(Quantity) as Ventas FROM OrderDetails
    GROUP BY ProductID
    HAVING MAX(TOTAL) -- ERROR
    ORDER BY TOTAL
    ```

    Para evitar este problema existen las subconsultas (*subqueries*).



## Orden de cláusulas

El orden general para poder especificar los distintos operadores y cláusulas cuando hay agregación es el siguiente:

```sql title="Orden de operaciones"
-- Orden de operaciones
SELECT ... FROM ....
WHERE ...
GROUP BY ...
HAVING ...
ORDER By ...
LIMIT ...
```

Nótese de los ejemplos previos que muchas de estas cláusulas son de uso opcional.
Sin embargo, sí es necesario respetar el orden de uso de cada una para evitar errores.