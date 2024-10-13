

# SQL


<!-- 

## Notacion de Chen

### Entidad
Es una representacion de algo
Normalmente se almacena como tabla.
En esta notacion las entidades se representan como una palabra dentro de un rectangulo.


### Atributos
Una entidad tiene multiples atributos. Los atributos se representan gráficamente con óvalos.
Los atributos comunes pueden ser **simples o compuestos**. Estos ultimos éstán formados por otros atributos. Los atibutos simples se representan con óvalos vacíos ("huecos"), en tanto que los atributos compuestos se representan con ovalos rellenos.

Tambien existen los atributos **multivalor**, los cuales tienen multiples valores asignados. Los atributos multivalor se representan con un óvalo doble.

Los atributos **derivados** se pueden obtener a partir de otros atributos. Se representan con óvalos punteados.

### Key (clave)

Las keys son atributos únicos e irrepetibles. Se marcan con un subrayado.
 -->


<!-- 

## Instalacion

gestor de base de datos (gdb)


**Recomendado:** SQLite y su browser


[Instalacion en Fedora:](https://developer.fedoraproject.org/tech/database/sqlite/about.html)
```bash
sudo dnf install sqlite # gestor base datos
sudo dnf install sqlitebrowser # interfaz grafica
sudo dnf install sqlite-doc
``` -->



<!-- 


## Tabla

Una tabla es una estructura de datos se organiza en filas y columnas.

## Campos y Registros

**Campo** es una columna 
**Registro** es una fila



## Query

Las queries (consultas) son **todas** las operaciones que afectan a la base de datos, conocidas con el acrónimo CRUD: crear (*create*), leer (*read*), modificar (*update*) y eliminar (*delete*)



## Comandos

Crear tabla con atributos y tipos llamada *usuarios*
```sql
CREATE TABLE "usuarios" (
	"nombre"	TEXT,
	"apellido"	TEXT,
	"edad"	INTEGER
);
```
El punto y coma (;) indica el final de una intrucción.


Cargar datos de un usuario (un registro):
```sql
INSERT INTO usuarios (nombre, apellido, edad)
VALUES ('Aitor','Tilla', 47) ;
```

Para delimitar los valores de texto se pueden usar comillas simples o dobles. Se recomienda el uso de las simples.

Cargar datos de multiples registros (multiples registros)
Prestar atencion al uso de comas:
```sql
INSERT INTO usuarios (nombre, apellido, edad)
VALUES 	('Aitor','Tilla', 47),
		('Aquiles','Brinco', 25),
		('Helen', 'Chufe', 31),
		('Susana', 'Torio', 55)  ;
```
**Cuidado**: los campos que se repitan serán guardados múltiples veces.


Leer todo el contenido de la tabla:
```sql
SELECT * FROM usuarios  ;
```

Leer algunos campos particulares de una tabla:
```sql
SELECT nombre, edad FROM usuarios ;
```
Los campos elegidos se separan con comas.

Eliminar la tabla de usuarios:
```sql
DELETE FROM usuarios ;
```



<!--  -->



<!-- 
## Identificadores

### primary key

Se rehace la tablas incluyendo una *primary key*, una clave primaria. Ésta es una clave única e irrepetible,típicamente un numero entero. La claves primaria sirve como un alias de los registros de la tabla.

```sql
CREATE TABLE "usuarios" (
	"id_usuario"	INTEGER,
	"nombre"	TEXT,
	"apellido"	TEXT,
	"edad"	INTEGER,
	PRIMARY KEY("id_usuario" AUTOINCREMENT)
);
```

Lo habitual es definir las claves primarias como autoincrementales, de modo que su valor se asigne automáticamente.   

Se crea una segunda tabla con sus propios campos y su propia clave primaria, esta vez para registrar los turnos médicos de los usuarios:

```sql
CREATE TABLE "turnos_medicos" (
	"id_turno"	INTEGER,
	"profesional"	TEXT,
	"id_usuario"	INTEGER,
	"motivo"	TEXT,
	"horario"	TEXT,
	PRIMARY KEY("id_turno" AUTOINCREMENT)
);
```


```sql
INSERT INTO turnos_medicos(profesional, id_usuario, motivo, horario)
VALUES 	('Dr Hernandez', 1, 'dolor panza', '13:30')  ,	
		('Dr Hernandez', 3, 'dolor cabeza', '14:30') ;	
		
SELECT * FROM turnos_medicos ;
```

### foreign keys

Las tablas se pueden superponer para mostrarlas. Esto se hace separando por comas los nombres de tablas a mezclarse:

```sql
SELECT * FROM turnos_medicos , usuarios;
```
En este ejemplo, el campo *id_turno* sigue siendo clave primaria, pero dentro de la tabla se carga el campo *id_usuario* el cual apunta a la otra tabla. Entonces *id_usuario* es en la tabla compuesta una clave foránea (*foreign key*)

Resumiendo:

- Las *primary keys* son campos que identifican registros de una tabla;
- Las *foreign keys* son campos que apuntan a las *primary keys* de otras tablas.



Recomendado: [base de datos Northwind para SQLite](https://en.wikiversity.org/wiki/Database_Examples/Northwind/SQLite)


### alias

Alias para los campos:
```sql
SELECT LastName AS Apellido FROM Employees;
```

```sql
SELECT LastName AS apellido, FirstName AS nombre FROM Employees;
```

Usar alias facilita leer campos afectados por funciones.
Ejemplo, leer precios y su doble de la tabla 'Products':
```sql
SELECT Price as precio ,Price*2 as precio_doble FROM Products;
```

<!--  -->




<!-- 

### ORDER BY

Ordenar un campo en orden ascendente:
```sql
SELECT * FROM Products
ORDER BY price;
```
o:
```sql
SELECT * FROM Products
ORDER BY price ASC;
```
Ordenar en orden desdendente:
```sql

SELECT * FROM Products
ORDER BY price DESC;
```
El ordenamiento se puede aplicar tambien a campos de texto, en tal caso el ordenamiento es el alfabético

Orden de jerarquías en el ordenamiento:

1. Null
2. Números
3. Caracteres especiales
4. Letras


El ordenamiento se puede afecta. 

Ejemplo: ordenar de forma ascendente pero colocando los *Null* al final:
```sql
SELECT * FROM Products
ORDER BY ProductName ASC NULLS LAST
```
Ejemplo: ordenar de forma descendente pero colocando los *Null* al comienzo:
```sql
SELECT * FROM Products
ORDER BY ProductName DESC NULLS FIRST
```
Ordenamiento aleatorio:
```sql
SELECT * FROM Products
ORDER BY Random();
```
Ordenamiento por dos campos:
```sql
SELECT * FROM Products
ORDER BY ProductName, SupplierID;
```
### DISTINCT
Seleccionar campos no repetidos
```sql
SELECT DISTINCT SupplierID FROM Products;
```
 -->



<!-- 
## Clausula WHERE

WHERE permite filtrar resultados en basea distintos criterios:

por coincidencia numérica
```sql
SELECT * FROM Products WHERE ProductID = 24;
```
por texto:
```sql
SELECT * FROM Products WHERE ProductName = "Tofu";
```
por rango numérico:
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
``` -->


<!-- 

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

El operador DISTINCT (!=) es un operador relacional

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

**Importante:** los valores límite están incluidos. Y éstos deben estar ordenados de menor a mayor.

### LIKE


La cláusula LIKE se porta como un operador igualdad:

```sql
SELECT * FROM Employees
WHERE LastName LIKE "Fuller" ;
```
La ventaja es el potencial de usar *comodines*
#### Comodin '\%'

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

#### Comodin '\_'

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

Con el operador IN se reduce a:

```sql
SELECT * FROM Products
WHERE SupplierID IN (3, 4, 5, 9, 14) ;
```
Los valores de interés se agrupan por paréntesis y se separan con comas.

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
 -->

<!--  

## Funciones de Agregacion

### count() :
```sql
-- conteo
SELECT count(FirstName) from Employees;
-- Conteo y asignacion de alias
SELECT count(FirstName) AS cantidad_empleados from Employees;
```

### sum():
```sql
SELECT Price FROM Products;

-- Suma
SELECT sum(Price) FROM Products; 
```
### AVG():
```sql
-- media (average)
SELECT AVG(Price) FROM Products; 
-- media (average) con redondeo
SELECT ROUND(AVG(Price)) FROM Products; 

-- redondeo con dos digitos
SELECT ROUND(AVG(Price), 2) FROM Products; 

```
### MIN():
```sql
SELECT MIN(Price) FROM Products; 
SELECT ProductName, MIN(Price) FROM Products; 

-- Minimo precio con nombre de producto 
SELECT ProductName, MIN(Price) FROM Products
-- descarte de campos nulos
WHERE ProductName IS NOT NULL;
```

### MAX():
```sql
SELECT  MAX(Price) FROM Products;

-- Maximo precio con nombre de producto 
SELECT ProductName, MAX(Price) FROM Products
-- descarte de campos nulos
WHERE ProductName IS NOT NULL;
```

**Comentario:** la funcion ROUND  **no es** de agregacion.


<!--  -->

<!-- 

## GROUP BY 


```sql
SELECT SupplierID, ROUND(AVG(Price),2) as promedio FROM Products 
-- WHERE filtra por registros
WHERE SupplierID IS NOT NULL
GROUP BY SupplierID
ORDER BY promedio
```

## HAVING

HAVING habilita filtrar en base a grupos. 

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

Importante: no se puede concatenar funciones de agregaciones.
Ejemplo: 
```sql
MAX(SUM( campo ) )
```
Ejemplo:
```sql
-- ERROR: concatenado de funciones de agregación
SELECT ProductID, SUM(Quantity) as Total FROM OrderDetails
GROUP BY ProductID
HAVING MAX(TOTAL) 
ORDER BY TOTAL
```


```sql
-- Orden de operaciones
SELECT ... FROM ....
WHERE ...
GROUP BY ...
HAVING ...
ORDER By ...
LIMIT ...
```

 -->





<!-- 

## Subconsultas (Subqueries)

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
 -->





<!-- 
## Uniones (*joins*)

Los joins permiten combinar los datos de dos o más tablas y devolverlos en una sola.
Tipos:
- Inner join
- Left join
- Right join
- Full join
- Cross join


### Inner join

Ejemplo implícito:
```sql
-- Inner join implicito
SELECT * FROM Employees e, orders o
WHERE e.EmployeeID = o.EmployeeID 
```
Ejemplo explícito:
```sql
-- Inner join explicito
SELECT * FROM Employees e
INNER JOIN Orders o
ON e.EmployeeID = o.EmployeeID 
```
El inner join es la opcion por defecto. Si sólo se indica 'JOIN' se asume que es del tipo INNER.



### Cross join

El cross join combina todos elementos de una tabla con todos los elementos de la otra. Si una tabla tiene n registros y la otra tiene m registros entonces la tabla final tendrá n*m registros en total.
Ejemplo explícito:
```sql
-- Cross join
SELECT * FROM Employees e
CROSS JOIN Orders o
```
El cross join rara vez es usado.


### Left join
El elft join muestra la tabla izquierda en su totalidad pero le agrega los datos comunes con la segunda tabla. A los registros no coincidentes los rellena con Null

```sql
-- Left join
SELECT * FROM Employees e
LEFT JOIN Orders o
ON e.EmployeeID = o.EmployeeID 
```

### Right Join

Es el contrario de left join: muestra en su totalidad la segunda tabla y le añade los elementos coindicentes con la primera.

**Importante:** SQLite no permite crear la right join directamente. Sin embargo se puede implementar invirtiendo el orden de llamado de las tablas:

```sql
-- 'Right join' simulado
SELECT * FROM Orders o
LEFT JOIN Employees e
ON o.EmployeeID = e.EmployeeID 
```


### Full join

La full join equivale a la superposición de la left join con la right join.

**Importante:** SQLite no permite crear la full join directamente. Sin embargo se puede implementar con el comando UNION :



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
El comando UNION muestra la unión lógica de las tablas sin repetir elementos. Para mostrar también los registros repetidos usar UNION ALL.


Para que la **unión** funcione correctamente, las dos tablas deben tener los mismos campos; de otra manera se puede dar lugar a resultados impredecibles.



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
-- inner join: empleados premiados ,recompensa y mes entrega
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
 -->





<!-- 
## Cardinalidad


- 1:1 uno a uno
- 1:n uno a muchos
- n:1 muchos a uno
- n:m muchos a muchos

Para manejar relaciones n:m se crean tablas intermedias.
La tabla intermedia se relacionará n:1 con la primera tabla y 1:n con la segunda tabla.


## VER ESQUEMA MARTIN
 -->





<!-- 

## Normalizacion
https://youtu.be/DFg1V-rO6Pg?t=20343

La normalizacion  de la base de datos sirve para prevenir anomalias, mejorar el rendimiento y poder hacer consultas más efectivas.

Hay cinco formas normales, cada una con sus características. Cada nueva forma introduce requisitos adicionales a la forma anterior.

### 1º Forma Normal (1NF)
Cada celda debe tener un unico contenido atómico. Se evita cargar la misma celda con múltiples datos o datos compuestos; en cambio se crean varios campos acordes.
Cada atributo debe tener un valor único para cada registro.

Ejemplo tabla mal implementada:

| **ID_usuario**| **datos_usuario**| 
| ----------- | ----------- |
| 1		| 	aqui37, Aquiles, Brinco, 37  |
| 2		| 	helchu45, Helen, Chufe , 45	|

Ejemplo aplicando primera forma normal:

| **ID_usuario**| **alias** | **nombre** | **apellido** | **edad**| 
| --- | --- | --- | --- | --- |
| 1		| 	aqui37	| Aquiles| Brinco | 37  |
| 2		| 	helchu45| Helen| Chufe  | 45	|


### 2º Forma Normal (2NF)
El valor de cada celda debe dependér unicamente de la clave primaria. (No puede haber celdas con varias claves afectando su contenido). Se previene la dependencia *parcial*.

Ejemplo tabla mal implementada:
| **ID_pedido** | **ID_usuario** | **ID_producto** | **producto** | **precio** | **cantidad** |
|---|---|---|---|---|---|
| 1 | 34| 22| galletas | 1 | 15|

En este caso hay dos claves afectando el contenido del registro, que son *ID_pedido* e *ID_producto*.

Una forma acorde a la segunda forma de implementar la tabla es:

| **ID_pedido** | **ID_usuario** | **ID_producto** |**cantidad** |
|---|---|---|---|
| 1 | 34|  22 | 15|

| **ID_producto** | **producto** | **precio** | 
|---|---|---|
| 22| galletas | 1 |

REVISAR

### 3º Forma Normal (3NF)
Se busca eliminar la dependencia transitiva. Se trata de no repetir relaciones entre campos. Por ejemplo: en una tabla de datos de usuarios donde se indica la ciudad de su domicilio y su provincia (provincia/estado/departamento/etc) :


| ID_usuario| nombre_usuario| ciudad	| provincia	|
| ----------- | ----------- |-------|-------|
| 1        | Alberto       	| La Plata|	Provincia de Buenos Aires|
| 2        | Claudia       	| Córdoba  |	Córdoba		|


Hay una redundancia: una misma ciudad sólo puede estar ubicada en una única provincia. La solución es crear una tabla aparte con los datos de las ciudades, cada una con su ID y ser referenciadas por la tabla de usuarios.  

| ID_usuario| nombre_usuario| ID_ciudad	|
| ----------- | ----------- |-------|
| 1        | Alberto       	| 7 |	
| 2        | Claudia       	| 21  |	

| ID_ciudad| | ciudad	| provincia	|
| ----------- | ----------- |-------|-------|
| 7   | La Plata|	Provincia de Buenos Aires|
| 21   | Córdoba  |	Córdoba		|

De esta forma se previene evitar la repetición de datos de ubicación en distintas tablas.


### 4º Forma Normal (4NF)

- multiples valores para una misma tabla
- valores dependientes de múltiples valores de la misma tabla.

*dependencia muiltivaluada*
*clave foranea compuesta*

### 5º Forma Normal (5NF)

Se previenen las *dependencias de union* entre atributos

Para diseñar bases de datos pequeñas utilizar la tercera forma normal suele ser suficiente. En cambio para bases de datos muy grandes y con necesidad de escalamiento es recomendable implementar la cuarta o la quinta forma normal.


 -->





<!-- 

## Indices

Los índices son una herramienta auxiliar que permite mejorar los tiempos de consulta para ciertos campos de interés. Los índices se crean con la sintaxis: 
```sql
CREATE INDEX <alias> ON <tabla> (<campo>)
```

Ejemplo: índice para los nombres de producto

```sql
-- Indice "nombre" apuntando al campo "ProductName" en tabla "Products"
CREATE INDEX nombre ON Products (ProductName)
```

La consulta de campos se realiza normalmente. No se requiere usar el alias. Ejemplos:

```sql
SELECT * FROM Products
SELECT * FROM Products WHERE  ProductName = "Chais"
```

Los índices sirven también como indicadores únicos para ciertos campos de interés, sirviendo como alternativa ante 
```sql
-- Indice unico compuesto para empleados (nombres o apellidos podrían estar repetidos)
-- Crear este índice impedirá la repetición de pares nombre - apellido
CREATE UNIQUE INDEX name ON Employees (FirstName, LastName)
```

Los indices consumen mucho espacio en disco. Esto se agrava cuando se necesita actualizar datos indexados. Por ello hay que ser prudente a la hora de crear índices. 

Las foreign keys son campos recomendados para indexar.


Los indices se eliminan con la orden DROP:

```sql
DROP INDEX <alias>
```

Para ponerle nombre a los indices es habitual usar la nomenclatura:
```
idx_<nombre_tabla>_<nombre_campo>
```

Ejemplo:

```sql
-- Consulta con unión interna
SELECT * FROM OrderDetails od
INNER JOIN Orders o
WHERE OrderDate > "1996-07-04"
AND od.Quantity > 10

-- Crear indices
CREATE INDEX cantidad ON OrderDetails (Quantity);
CREATE INDEX fecha	  ON Orders (OrderDate);

-- eliminar indices
DROP INDEX cantidad ;
DROP INDEX fecha	;
```
 -->



<!-- 

# Vistas

Las vistas son tablas auxiliares que hacen referencia a las tablas de datos. Sirven para facilitar la visualización de datos recolectados de otras tablas.

Creación de la vista:
```sql
CREATE VIEW Productos_simplificados AS 

SELECT ProductID, ProductName, Price FROM Products
WHERE ProductID > 20
ORDER BY ProductID DESC  
```
Lectura de la vista:
```sql
SELECT * FROM  Productos_simplificados
```

Eliminación de vistas:
```sql
DROP VIEW IF EXISTS Productos_simplificados
```
La condición 'IF EXISTS' es recomendable para evitar posibles errores en caso que la tabla ya haya sido eliminada.
 -->



<!-- 

## Bloqueos y Transacciones

Los **bloqueos** son un mecanismo preventivo de las bases de datos que impiden múltiples consultas simultáneas. Esto permite asegurar la integridad de los datos y prevenir tanto errores de lectura como de escritura.

SQLite utiliza bloqueo completo	mientras se realiza una operacion de escritura, en tanto que permite lecturas concurrentes.

Tipos de bloqueos:

- Bloqueos compartidos (shared locks)
Mientras se lee se permiten lecturas pero no escrituras

- Bloqueos reservados (reserved locks) 
Mientras se escribe se permiten lecturas pero no escrituras

- Bloqueos exclusivos (exclusive locks)
Mientras se escribe se impiden tanto lecturas como escrituras


Las **transacciones** son cambios volátiles que se pueden asentar permanentemente (*commit*) o deshacer (*rollback*). 

La transacción siempre comienza con el comando BEGIN:

```sql
-- Comienza una transaccion
BEGIN;
-- Se propone un cambio en ciertos registros. El cambio es temporal
UPDATE Products SET ProductName = "El Pollo" WHERE ProductName = "Chais" ;
```

Si se detecta algún error o inconsistencia en los cambios realizados se puede ordenar el paso atrás con el comando ROLLBACK:

```sql
-- Deshace los cambios
ROLLBACK
```

Si en cambio se busca guardar los cambios de forma definitiva se utiliza el comando COMMIT:

```sql
-- Asienta los cambios en la base de datos
COMMIT
```
Las transacciones son indispensables para trabajar sobre las bases de datos desde programas externos.

 -->




<!-- 

## Procedimientos almacenados (Stored Procedures)

Los procedimientos almacenados son consultas prearmadas que se pueden utilizar repetidas veces. Son el equivalente a las funciones de los lenguajes de programacion

SQLite **no soporta** procedimientos almacenados debido a su tipo de armado, a diferencia de otras bases de datos como PostgreSQL, MySQL, etc. Sin embargo esta limitación puede saltearse implementando las *queries* prearmadas en el programa 'cliente' de la base de datos.


## User Defined Functions (UDF)

Las funciones definidas por el usuario son funciones que se diseñan en el lenguaje anfitrión del programa cliente y se transmiten al gestor de la base de datos. Es entonces el gestor el encargado de ejecutar la función indicada por el programa cliente y devolver el resultado en caso de ser requerido.
 -->




<!--  

## Uso en Python


### Importación

Python puede conectarse con SQLite mediante el conector *sqlite3*, el cual debe importarse:

```python
import sqlite3
```

### Conectores y cursores

Se crea un conector que abre el archivo que almacena la base de datos:

```python
# ejemplo: archivo de base de datos aledaño al ejecutable
ruta_archivo = "Northwind.db"

# conexion con  base de datos en archivo
conector = sqlite3.connect(ruta_archivo)
```

El siguiente paso es crear un *cursor* para manejar pedidos y respuestas de SQLite:

```python
# Cursor 
cursor = conector.cursor()
```

### Consultas y transacciones

Para hacer las consultas se usa el método *execute()*, el cual **siempre** crea una transacción. Las instrucciones de SQL se ingresan com argumento en formato texto.

```python
# inicio de transacción (BEGIN implícito)
cursor.execute(
    # Rutina SQL, 1 renglon
    'SELECT ProductName, Price FROM Products;'
)
```
La respuesta del gestor se recibe con el método *.fetchall()*:
```python
#respuesta de la base de datos
resultados = cursor.fetchall()
print(resultados)
```
La respuesta viene dada como una lista de tuplas que contienen los registros. 


### pandas y mathplotlib 

Una opción para darle formato de tablas a la información en consola es usar la biblioteca *pandas*:
```python
import pandas as pd
# ...
dataframe = pd.DataFrame(resultados)
print(dataframe)
```
En este caso se mostrará el contenido tabulado en consola emulando una tabla.


La biblioteca ***mathplotlib*** permite graficar las tablas formateadas con *pandas* con la función *pyplot*. Debe importarse:
```python
import matplotlib.pyplot as plt
```

*pandas* incluye integrado su propio manejador para realizar consultas y gestionar el resultado ya formateado:

```python
# Query para el gestor SQL en formato 'string'
consulta =  '''
    SELECT ProductName, Price FROM Products;
    '''
# Envío consulta y recepción de respuesta
dataframe = pd.read_sql_query(consulta, conector)
```
Con el método *plot()* se configuran los parámetros de interés de
la gráfica y ésta se muestra con la función *show()*:
```python
# parámetros de la gráfica
dataframe.plot(
    x="ProductName",
    y="Price",
    kind="bar",
    figsize=(10, 5), 
    legend = False
    )

# Gráfica de Barras
plt.title("Precios")
plt.xlabel("Producto")
plt.ylabel("Valor")
plt.xticks(rotation = 90)   # etiquetas en vertical
plt.show()
```

Ejemplo rutina completa:
```python
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

ruta_archivo = "Northwind.db"

# conexion con  base de datos en archivo
conector = sqlite3.connect(ruta_archivo)

# Query para el gestor SQL en formato 'string'
consulta =  '''
    SELECT ProductName, Price FROM Products;
    '''
# Envío consulta y recepción de respuesta
dataframe = pd.read_sql_query(consulta, conector)

# parámetros de la gráfica
dataframe.plot(
    x="ProductName",
    y="Price",
    kind="bar",
    figsize=(10, 5), 
    legend = False
    )

# Gráfica de Barras
plt.title("Precios")
plt.xlabel("Producto")
plt.ylabel("Valor")
plt.xticks(rotation = 90)   # etiquetas en vertical
plt.show()
```



### modificar datos

Si se busca modificar los datos también se usa el método *.execute()*. Recordar que este método implícitamente inicia una transacción y por tanto los cambios producidos serán temporales:
```python
# inicio de transacción (BEGIN implícito)
cursor.execute(
    # Consulta SQL: actualización de un nombre de producto
    '''
    UPDATE Products SET ProductName = "Chais" WHERE ProductName = "El Pollo" ;
    '''
)
```
La validación de los cambios introducidos se realiza con el método *.commit()* en tanto que el descarte de los mismos se realiza con el método *.rollback()*:

```python
#guardado definitivo de cambios
conector.commit()
# Reestablecimiento de datos
conector.rollback()
```
Una posibilidad del uso de éstos métodos es repartirlos entre las rutinas de excepciones ( **try - except** ). De esta forma se validan los cambios sólo si no se produjeron excepciones y en caso contrario se ordena el reestablecimiento de los datos originales.

### funciones de usuario

Las funciones de usuario se crean con el método *.create_function()*. En él debe pasarse como argumento un nombre para la función, el número de argumentos que usará y la función lambda que define su funcionamiento interno.

```python
# función lambda  de interés 
cubo = lambda n : n*n*n

# Funcion de usuario:
# argumentos: 
# 1 - nombre de la "funcion de usuario"
# 2 - numero de argumentos
# 3 - funcion lambda a ejecutar
conector.create_function("cube",1, cubo)
```

La *función de usuario* así creada se usa normalmente dentro de la rutina SQL de la consulta:

```python
# inicio de transacción (BEGIN implícito)
cursor.execute(
    # Rutina SQL, consulta de campos con funcion usuario
    '''
    SELECT ProductName, Price, round( cube(Price) , 2) AS CubicPrice FROM Products;
    '''
)

# respuesta de la base de datos
resultados = cursor.fetchall()
```
### cierre

El cierre manual de la base de datos se realiza cerrando tanto el cursor como el conector con el método *.close()*:

```python
# cierre
cursor.close()
conector.close()
```

Una opcion es abrir creando un contexto con la *cláusula **with***, de la misma manera en que suelen abrirse los archivos. En tal caso el cierre de la base de datos se hace automáticaticamente al salir del contexto creado, el cual es marcado por indentación.

https://youtu.be/DFg1V-rO6Pg?t=24731

-->





<!-- 

## Diferencias entre gestores


### Características

**SQLite**
- Es un gestor embebido
- Trabaja con archivo único
- Es ideal para aplicaciones embebidas y prototipos
- No sirve para aplicaciones de gran escala o de alto rendimiento

**MySQL**
- Es un gestor basado en servidor
- Puede trabajar con múltiples archivos
- Es ideal para aplicaciones de gran escala o de alto rendimiento

**PostgreSQL**
- Es un gestor basado en servidor
- Puede trabajar con múltiples archivos
- Es ideal para aplicaciones de gran escala o de alto rendimiento
- Tiene extensiones propias

**SQLServer**
- Es de pago
- Es un gestor basado en servidor
- Puede trabajar con múltiples archivos
- Es ideal para aplicaciones de gran escala o de alto rendimiento
- Tiene extensiones propias





## Migracion entre gestores

1 - Se adaptan las consultas para crear el formato de tablas en el nuevo gestor de base de datos;
2 - Para migrar los datos se recomienda exportar cada tabla de la base de datos en archivos CSV e importarlos con el nuevo gestor.

 -->