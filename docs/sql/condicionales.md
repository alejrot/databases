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
  # - MySQL
  # - PostgreSQL
  # - MariaDB
---

# Cláusulas Condicionales



Las cláusulas condicionales se utilizan con ayuda de la cláusula `#!sql WHERE`,
la cual permite seleccionar registros de las tablas en base a criterios específicos.
Pueden afectar a la lectura de datos (`#!sql SELECT`), 
a la actualización (`#!sql UPDATE`) 
y a la eliminación (`#!sql DELETE`).



<!-- ## Cláusula WHERE -->

<!-- 
La cláusula `#!sql WHERE` 
afecta a los comandos CRUD de SQL 
y permite **filtrar registros** en base a distintos criterios: 
-->

## SELECT

### por coincidencia numérica

```sql
SELECT * FROM Products 
WHERE ProductID = 24;
```

Resultado: el producto con ID 24

|ProductID |ProductName	|SupplierID	|CategoryID|	Unit|Price|
|---|---|---|---|---|---|
|24|	Guaraná Fantástica|	10	|1	|12 - 355 ml cans	|4.5|




### por texto

```sql
SELECT * FROM Products 
WHERE ProductName = "Tofu";
```

Resultado: el único tofu encontrado

|ProductID |ProductName	|SupplierID	|CategoryID|	Unit|Price|
|---|---|---|---|---|---|
|14|	Tofu|	6	|7	|40 - 100 g pkgs.	|23.25|

### por rango numérico

```sql
SELECT * FROM Products 
WHERE Price <= 40; --menor o igual a 4
```
Resultado: 77 registros con precio unitario menor a 40

|ProductID |ProductName	|SupplierID	|CategoryID|	Unit|Price|
|---|---|---|---|---|---|
|1|	Chais	|1	|1|	10 boxes x 20 bags	|18|
|2|	Chang	|1	|1|	24 - 12 oz bottles	|19|
|3|	Aniseed Syrup	|1|	2|	12 - 550 ml bottles	|10|
|...|
|76|	Lakkalikööri|	23|	1|	500 ml	|18|
|77|	Original Frankfurter grüne Soße|	12|	2|	12 boxes|	13|

## DELETE

```sql
DELETE FROM turnos_medicos 
WHERE id_turno = 2 ;
```

## UPDATE

```sql
UPDATE turnos_medicos SET horario = "13:00" 
WHERE id_turno = 1 ; 
```


## Operadores Lógicos

### AND

```sql
SELECT * FROM Customers
WHERE CustomerID >= 50 AND CustomerID < 55 ;
```

### OR

```sql
SELECT * FROM Employees
WHERE FirstName ="Janet" OR FirstName = "Adam" ;
```

### NOT

```sql
SELECT * FROM Customers
WHERE NOT Country = "USA" ;
```

### Combinados con paréntesis

```sql
SELECT * FROM Products
WHERE (Price < 20  OR CategoryID = 6) AND SupplierID = 7 ;
```



## LIMIT 
Con la cláusula LIMIT se puede poner tope al numero de resultados:
```sql
SELECT * FROM Customers
WHERE CustomerID >=50
LIMIT 5 ;
```

Ejemplo: cláusulas combinadas
```sql
SELECT * FROM Products
WHERE NOT CategoryID = 6 
AND NOT SupplierID = 1
AND Price <= 30
ORDER BY RANDOM()
LIMIT 5 ;
```

## DISTINCT

```sql
SELECT * FROM Customers
WHERE  Country != "USA" ;
```

El operador `#!sql DISTINCT` (`!=`) es un operador de comparación.
NO cuenta como operador lógico.


## BETWEEN

El operador `#!sql BETWEEN` facilita elegir campos en un rango de valores.

```sql
SELECT * FROM Products 
WHERE Price BETWEEN 20 AND 40 ;
```

```sql
SELECT * FROM Products 
WHERE Price BETWEEN 20 AND 40
AND CategoryID = 6 ;
```

Este operador es práctico para seleccionar entre fechas

```sql
SELECT * FROM Employees
WHERE BirthDate BETWEEN "1960-0-1" AND "1970-01" ;
```


!!! warning "Valores límite"
    Los valores límite de `#!sql BETWEEN` están incluidos. 
    Además estos deben cumplir:

    - estar ordenados de menor a mayor;
    - ser de tipo compatible 
    (hay que evitar mezcla de criterios).


## LIKE


La cláusula `#!sql LIKE` se porta como un operador igualdad:

```sql
SELECT * FROM Employees
WHERE LastName LIKE "Fuller" ;
```
La ventaja es el potencial de usar *caracteres comodín*
para implementar la búsqueda de patrones.


### Comodin `%`

```sql
-- Apellidos que empiezan con "D"
SELECT * FROM Employees
WHERE LastName LIKE "D%" ;
```

```sql
-- Apellidos que terminan con "G"
SELECT * FROM Employees
WHERE LastName LIKE "%G" ;
```

```sql
-- Apellidos que incluyen la "A"
SELECT * FROM Employees
WHERE LastName LIKE "%A%" ;
```

### Comodin `_`

```sql
-- Apellidos que coinciden con el patrón
SELECT * FROM Employees
-- Empieza con "F", 4 espacios en medio, termina en "R"
WHERE LastName LIKE "F____R" ; 
```

```sql
-- Apellidos que coinciden con el patrón
SELECT * FROM Employees
-- 1 espacio al inicio, 1 "U", 4 espacios al final
WHERE LastName LIKE "_U____" ;
```
### Comodines combinados

```sql
-- Apellidos que coinciden con el patrón
SELECT * FROM Employees
-- 1 espacio al inicio, 1 "U", al menos 5 letras
WHERE LastName LIKE "_U___%" ; 
```


## IS 

Con el operador `#!sql IS` se puede filtrar tanto a los registros con valor nulos como a los no nulos.


```sql title="nulos"
-- Registros con valor nulo
SELECT * FROM Products
WHERE ProductName IS NULL;
```
```sql title="no nulos"
-- Registros con valores no nulos
SELECT * FROM Products
WHERE ProductName IS NOT NULL;
```


## IN

El operador `#!sql IN` sirve para aquellos casos en que se necesita seleccionar muchos valores particulares de un parámetro.

Por ejemplo: valores 3,4,9
```sql
SELECT * FROM Products
WHERE SupplierID = 3
OR SupplierID = 4
OR SupplierID = 9;
```

Con el operador `#!sql IN` se reduce a:

```sql
SELECT * FROM Products
WHERE SupplierID IN (3, 4, 9);
```

<!-- 
|ProductID|	ProductName|	SupplierID|	CategoryID|	Unit|	Price|
|---|---|---|---|---|---|
|6|	Grandma's Boysenberry Spread|	3|	2|	12 - 8 oz jars|25|
|7|	Uncle Bob's Organic Dried Pears|	3	|7|	12 - 1 lb pkgs.	|30|
|8|	Northwoods Cranberry Sauce|	3	|2	|12 - 12 oz jars	|40|
|9|	Mishi Kobe Niku|	4|6	|18 - 500 g pkgs.	|97|
|10|	Ikura|	4|	8|	12 - 200 ml jars	|31|
|22|	Gustaf's Knäckebröd|	9	|5	|24 - 500 g pkgs.	|21|
|23|	Tunnbröd	|9|	5|	12 - 250 g pkgs.|	9|
|74|	Longlife Tofu|	4|	7|	5 kg pkg.|	10|
-->


Los valores de interés se agrupan por paréntesis y se separan con comas.

`#!sql IN` es considerado un **operador lógico** por sustituir la batería de operadores `#!sql OR` que aglomeraban los condicionales de relación para cada valor.



Los valores buscados pueden ser textos:
```sql
SELECT * FROM Employees
WHERE LastName IN ("King","Fuller") ;
```
Con el operador `#!sql NOT` se puede invertir el resultado, 
excluyendo los casos elegidos:
```sql
SELECT * FROM Employees
WHERE LastName NOT IN ("King","Fuller") ;
```

