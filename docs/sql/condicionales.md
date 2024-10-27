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

# Cláusulas Condicionales



Las cláusulas condicionales se utilizan con ayuda de la cláusula `WHERE`. 
Pueden afectar a la lectura de datos (`SELECT`), 
a la actualización (`UPDATE`) 
y a la eliminación (`DELETE`).



## Cláusula WHERE


WHERE permite filtrar resultados en base a distintos criterios:

### SELECT

- por coincidencia numérica
```sql
SELECT * FROM Products WHERE ProductID = 24;
```
 - por texto:
```sql
SELECT * FROM Products WHERE ProductName = "Tofu";
```
- por rango numérico:
```sql
SELECT * FROM Products WHERE Price <= 40; --menor o igual a
```

### DELETE

```sql
DELETE FROM turnos_medicos 
WHERE id_turno = 2 ;
```

### UPDATE

```sql
UPDATE turnos_medicos SET horario = "13:00" 
WHERE id_turno = 1 ; 
```


## Operadores Lógicos: AND, OR, NOT

AND
```sql
SELECT * FROM Customers
WHERE CustomerID >= 50 AND CustomerID < 55 ;
```
OR
```sql
SELECT * FROM Employees
WHERE FirstName ="Janet" OR FirstName = "Adam" ;
```
Combinados con paréntesis
```sql
SELECT * FROM Products
WHERE (Price < 20  OR CategoryID = 6) AND SupplierID = 7 ;
```
NOT
```sql
SELECT * FROM Customers
WHERE NOT Country = "USA" ;
```

### LIMIT 
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

### DISTINCT

```sql
SELECT * FROM Customers
WHERE  Country != "USA" ;
```

El operador DISTINCT (!=) es un operador de comparación.
NO cuenta como operador lógico.


### BETWEEN

El operador BETWEEN facilita elegir campos en un rango de valores.

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
    Los valores límite de `BETWEEN` están incluidos. Además estos deben cumplir:

    - estar ordenados de menor a mayor;
    - ser de tipo compatible 
    (hay que evitar mezcla de criterios).


### LIKE


La cláusula LIKE se porta como un operador igualdad:

```sql
SELECT * FROM Employees
WHERE LastName LIKE "Fuller" ;
```
La ventaja es el potencial de usar *caracteres comodín*
para implementar la búsqueda de patrones.


#### Comodin `%`

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

#### Comodin `_`

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
#### Comodines combinados

```sql
-- Apellidos que coinciden con el patrón
SELECT * FROM Employees
-- 1 espacio al inicio, 1 "U", al menos 5 letras
WHERE LastName LIKE "_U___%" ; 
```


### IS NULL & IS NOT NULL
```sql
-- Registros nulos
SELECT * FROM Products
WHERE ProductName IS NULL;
```
```sql
-- Registros  no nulos
SELECT * FROM Products
WHERE ProductName IS NOT NULL;
```


### IN

El operador IN sirve para aquellos casos en que se necesita seleccionar muchos valores particulares de un parámetro.

Por ejemplo: valores 3,4,5,9,14
```sql
SELECT * FROM Products
WHERE SupplierID = 3
OR SupplierID = 4
OR SupplierID = 5 
OR SupplierID = 9 
OR SupplierID = 14 ;
```

Con el operador `IN` se reduce a:

```sql
SELECT * FROM Products
WHERE SupplierID IN (3, 4, 5, 9, 14) ;
```
Los valores de interés se agrupan por paréntesis y se separan con comas.

`IN` es considerado un **operador lógico** por sustituir la batería de operadores `OR` que aglomeraban los condicionales de relación para cada valor.



Los valores buscados pueden ser textos:
```sql
SELECT * FROM Employees
WHERE LastName IN ("King","Fuller") ;
```
Con el operador NOT se puede invertir el resultado, excluyendo los casos elegidos:
```sql
SELECT * FROM Employees
WHERE LastName NOT IN ("King","Fuller") ;
```

