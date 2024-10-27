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


# Uniones (*joins*)





Los *joins* permiten combinar los datos de dos o más tablas y devolverlos en una sola.


Trabajan mediante índices y son una alternativa más eficiente a las subconsultas.



Tipos de uniones:

- Inner join
- Left join
- Right join
- Full join
- Cross join


## Inner join

Los inner join devuelven las coincidencias entre tablas.


Ejemplo implícito:
```sql
-- Tabla de empleados y tabla de órdenes de compra
SELECT * FROM Employees e, orders o
-- Inner join implicito
WHERE e.EmployeeID = o.EmployeeID 
```


Ejemplo explícito:
```sql
-- Tabla de empleados y tabla de órdenes de compra
SELECT * FROM Employees e
-- Inner join explicito
INNER JOIN Orders o
-- Condición de unión
ON e.EmployeeID = o.EmployeeID 
```
El *inner join* es la opcion por defecto. 
Si sólo se indica 'JOIN' se asume que es del tipo INNER.



## Cross join

El *cross join* combina todos elementos de una tabla con todos los elementos de la otra. 
Si una tabla tiene `n` registros y la otra tiene `m` registros 
entonces la tabla final tendrá `n x m` registros en total.


Ejemplo implícito:
```sql
-- Cross join
SELECT * FROM Employees e, Orders o
```

Ejemplo explícito:
```sql
-- Cross join
SELECT * FROM Employees e
CROSS JOIN Orders o
```
El *cross join* rara vez es usado.


## Left join

El *left join* muestra la tabla izquierda en su totalidad pero le agrega los datos comunes con la segunda tabla. 
A los registros no coincidentes los rellena con `Null`

```sql
-- Left join
SELECT * FROM Employees e
LEFT JOIN Orders o
ON e.EmployeeID = o.EmployeeID 
```

## Right Join

Es el contrario de *left join*: muestra en su totalidad la segunda tabla y le añade los elementos coindicentes con la primera.

**Importante:** SQLite no permite crear la *right join* directamente. Sin embargo se puede implementar invirtiendo el orden de llamado de las tablas:

```sql
-- 'Right join' simulado
SELECT * FROM Orders o
LEFT JOIN Employees e
ON o.EmployeeID = e.EmployeeID 
```


## Full join

La full join equivale a la superposición de la *left join* con la *right join*.

**Importante:** SQLite no permite crear la full join directamente. 
Sin embargo se puede implementar con el comando `UNION`:



```sql
-- FULL JOIN SIMULADO:

-- 1 - Left join
SELECT * FROM Employees e
LEFT JOIN Orders o
ON e.EmployeeID = o.EmployeeID 

-- 3 - union de joints
UNION

-- 2- 'Right join' simulado
SELECT * FROM Orders o
LEFT JOIN Employees e
ON o.EmployeeID = e.EmployeeID 
```
El comando `UNION` muestra la unión lógica de las tablas sin repetir elementos. 
Para mostrar también los registros repetidos usar `UNION ALL`.


Para que la **unión** funcione correctamente, las dos tablas deben tener los **mismos campos**; 
de otra manera se puede dar lugar a resultados impredecibles.


## Ejemplo aplicado
Ejemplo aplicado: premios mensuales para los empleados
```sql
-- Tabla de premios para los empleados
CREATE TABLE "Rewards"(
	"RewardID" INTEGER,
	"EmployeeID" INTEGER,
	"Reward" INTEGER,
	"Month" TEXT,
	PRIMARY KEY ("RewardID" AUTOINCREMENT)
)
-- Registro de premios: uno por mes
INSERT INTO Rewards (EmployeeID, Reward, Month) VALUES
(3, 200, "Juanuary"),
(2, 180, "February"),
(5, 250, "March"),
(1, 280, "April"),
(8, 160,"May"),
(null, null, "June")	-- premio no asignado
-- ver resultado
SELECT * FROM Rewards
```
Los resultados se pueden consultar con las siguientes rutinas:
```sql
-- inner join: empleados premiados, recompensa y mes entrega
SELECT FirstName , Reward, Month FROM Employees e
INNER JOIN Rewards r
ON r.EmployeeID = e.EmployeeID

-- left join: todos los empleados y qué premio recibió cada uno, si recibió algo
SELECT FirstName , Reward, Month FROM Employees e
LEFT JOIN Rewards r
ON r.EmployeeID = e.EmployeeID

-- full join (l + r) : todos los empleados, todos los premios
UNION

-- 'right join': todos los premios y empleados beneficiados, si el premio fue entregado
SELECT FirstName , Reward, Month FROM Rewards r
LEFT JOIN Employees e 
ON e.EmployeeID = r.EmployeeID
```

