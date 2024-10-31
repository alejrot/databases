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

Los `#!sql INNER JOIN` devuelven las coincidencias entre tablas.

<div class="grid" markdown>

<!-- Ejemplo implícito: -->
```sql title="INNER JOIN - implícito"
-- Tabla de empleados y tabla de órdenes de compra
SELECT * FROM Employees e, orders o
-- (Inner join implicito)
-- Condición de unión
WHERE e.EmployeeID = o.EmployeeID 
```


<!-- Ejemplo explícito: -->
```sql title="INNER JOIN - explícito"
-- Tabla de empleados y tabla de órdenes de compra
SELECT * FROM Employees e
-- Inner join explicito
INNER JOIN Orders o
-- Condición de unión
ON e.EmployeeID = o.EmployeeID 
```

</div>

!!! info "Unión predefinida"
    
    El `#!sql INNER JOIN` es la opcion por defecto. 
    Si sólo se indica `#!sql JOIN` se asume que es del tipo `#!sql INNER`.



## Cross join

El `#!sql CROSS JOIN` combina todos elementos de una tabla con todos los elementos de la otra. 
Si una tabla tiene `n` registros y la otra tiene `m` registros 
entonces la tabla final tendrá `n x m` registros en total.


<div class="grid" markdown>

```sql title="CROSS JOIN - implícito"
-- Cross join
SELECT * FROM Employees e, Orders o
```

```sql title="CROSS JOIN - explícito"
-- Cross join
SELECT * FROM Employees e
CROSS JOIN Orders o
```


</div>
El `#!sql CROSS JOIN` rara vez es usado.


## Left join

El `#!sql LEFT JOIN` muestra la tabla izquierda en su totalidad pero le agrega los datos comunes con la segunda tabla. 
A los registros no coincidentes los rellena con `Null`.

```sql title="LEFT JOIN"
-- Left join
SELECT * FROM Employees e
LEFT JOIN Orders o
ON e.EmployeeID = o.EmployeeID 
```

## Right Join

Es el contrario de `#!sql LEFT JOIN`: 
muestra en su totalidad la segunda tabla 
y le añade los elementos coincidentes con la primera.

SQLite no permite crear la `#!sql RIGHT JOIN` directamente. 
Sin embargo se puede implementar invirtiendo el orden de llamado de las tablas:

```sql title="RIGHT JOIN"
-- 'Right join' simulado
SELECT * FROM Orders o
LEFT JOIN Employees e
ON o.EmployeeID = e.EmployeeID 
```


## Full join

La `#!sql FULL JOIN` equivale a la superposición de la `#!sql LEFT JOIN` con la `#!sql RIGHT JOIN`.

SQLite no permite crear la `#!sql FULL JOIN` directamente. 
Sin embargo se puede implementar con el comando `UNION`:

```sql title="FULL JOIN"
-- FULL JOIN SIMULADO:

-- 1 - Left join
SELECT * FROM Employees e
LEFT JOIN Orders o
ON e.EmployeeID = o.EmployeeID 

-- 3 - union de joints
UNION

-- 2 - 'Right join' simulado
SELECT * FROM Orders o
LEFT JOIN Employees e
ON o.EmployeeID = e.EmployeeID 
```
El comando `UNION` muestra la unión lógica de las tablas sin repetir elementos. 
Para mostrar también los registros repetidos usar `UNION ALL`.


Para que la **unión** funcione correctamente, las dos tablas deben tener los **mismos campos**; 
de otra manera se puede dar lugar a resultados impredecibles.


## Ejemplo aplicado


### Preparando data

Imagínese que se otorgan
premios mensuales para los empleados.
Estos se guardan en una nueva tabla llamada `Rewards`:

```sql title="Tabla de premios"
-- Tabla de premios para los empleados
CREATE TABLE "Rewards"(
	"RewardID" INTEGER,
	"EmployeeID" INTEGER,
	"Reward" INTEGER,
	"Month" TEXT,
	PRIMARY KEY ("RewardID" AUTOINCREMENT)
);
```

Los registros de los premios se cargan en la nueva tabla:

```sql title="Registro de premios"
-- Registro de premios: uno por mes
INSERT INTO Rewards (EmployeeID, Reward, Month) VALUES
(3, 200, "Juanuary"),
(2, 180, "February"),
(5, 250, "March"),
(1, 280, "April"),
(8, 160,"May"),
(null, null, "June");	-- premio no asignado
```

El resultado se consulta 

```sql title="Ver premios"
-- ver resultado
SELECT * FROM Rewards;
```
Esta es la tabla creada:

|RewardID|	EmployeeID|	Reward|	Month|
|---|---|---|---|
|1|	3|	200|	Juanuary|
|2|	2|	180|	February|
|3|	5|	250|	March|
|4|	1|	280|	April|
|5|	8|	160|	May|
|6|	|	|	June|

<!-- 
Los resultados se pueden consultar con las siguientes rutinas: 
-->
El último premio no fue entregado, por ello el monto y el ID de empleado aparecen vacíos.

Con la tabla ya configurada 
y usando uniones se puede consultar la data relacionada con los premios.
En este ejemplo se tomo como tabla izquierda la tabla de empleados (`Employees`) 
y como tabla derecha la tabla de premios (`Rewards`).


### Inner join

Esta unión muestra solamente a aquellos empleados premiados y la información de su premio.

```sql title="Empleados premiados"
-- inner join: empleados premiados, recompensa y mes entrega
SELECT e.EmployeeID, FirstName , Reward, Month FROM Employees e
INNER JOIN Rewards r
ON r.EmployeeID = e.EmployeeID
```

|EmployeeID	|FirstName|	Reward|	Month|
|---|---|---|---|
|3|	Janet	|200	|Juanuary|
|2|	Andrew|	180|	February|
|5|	Steven|	250|	March|
|1|	Nancy	|280	|April|
|8|	Laura	|160	|May|


Nótese la necesidad de indicar una de las tablas de origen para poder mostrar el campo `EmployeeID`.
Esto se debe a que aparece en ambas tablas y entonces SQLite arroja un error por ambiguedad de columna
( *'ambiguous column name'*).

### Left join


Esta unión muestra a todos los empleados y la información de sus premios, 
si es que recibieron algo.

```sql title="Todos los empleados"
-- left join: todos los empleados y qué premio recibió cada uno, si recibió algo
SELECT e.EmployeeID, FirstName , Reward, Month FROM Employees e
LEFT JOIN Rewards r
ON r.EmployeeID = e.EmployeeID
```

|EmployeeID	|FirstName	|Reward|	Month|
|---|---|---|---|
|1	|Nancy	|280	|April|
|2	|Andrew	|180	|February|
|3	|Janet	|200	|Juanuary|
|4	|Margaret	|	||
|5	|Steven	|250|	March|
|6	|Michael	|||	
|7	|Robert	|	||
|8	|Laura|	160	|May|
|9	|Anne	||	
|10|	Adam||		


### Right join

Con esta unión se muestran todos los premios y a quién le fueron asignados.

```sql title="Todos los premios"
-- 'right join': todos los premios y qué empleados fueron beneficiados
SELECT e.EmployeeID, FirstName , Reward, Month FROM Rewards r
LEFT JOIN Employees e 
ON e.EmployeeID = r.EmployeeID
```


|EmployeeID|	FirstName|	Reward|	Month|
|----|----|---|---|
|3	|Janet	|200|	Juanuary|
|2	|Andrew	|180|	February|
|5	|Steven	|250|	March|
|1	|Nancy	|280|	April|
|8	|Laura	|160|	May|
|	|| |		June|

### Full join

Esta unión muestra a todos los empleados y a todos los premios vinculados entre sí.


```sql title="Todos los empleados, todos los premios"
-- left join: todos los empleados y qué premio recibió cada uno, si recibió algo
SELECT e.EmployeeID, FirstName , Reward, Month FROM Employees e
LEFT JOIN Rewards r
ON r.EmployeeID = e.EmployeeID

-- full join (l + r) : todos los empleados, todos los premios
UNION

-- 'right join': todos los premios y qué empleados fueron beneficiados
SELECT e.EmployeeID, FirstName , Reward, Month FROM Rewards r
LEFT JOIN Employees e 
ON e.EmployeeID = r.EmployeeID
```


|EmployeeID|	FirstName|	Reward|	Month|
|---|---|----|---|
|	 | ||	June|
|1 | Nancy	|280|	April|
|2 | Andrew	|180|	February|
|3 | Janet	|200|	Juanuary|
|4 | Margaret	||	|
|5 | Steven	|250|	March|
|6 | Michael	||	|
|7 | Robert	||	|
|8 | Laura	|160|	May|
|9 | Anne	||	|
|10|	Adam	||	|


Aparecen tanto los empleados sin premios como el premio sin asignar.

