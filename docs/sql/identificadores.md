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





# Identificadores

## Primary key (PK)

La clave primaria o *primary key* es una clave única e irrepetible, típicamente un numero entero. 
Ésta sirve como un alias de los registros de la tabla.
La clave primaria se define durante la creación de la tabla apuntando a uno de sus atributos internos.

Por ejemplo, para incorporar una clave primaria a la tabla de usuarios previa:

```sql title="Tabla usuarios - con clave primaria" hl_lines="2 6"
CREATE TABLE "usuarios" (
	"id_usuario"	INTEGER,    -- atributo elegido
	"nombre"	TEXT,
	"apellido"	TEXT,
	"edad"	INTEGER,
	PRIMARY KEY("id_usuario" AUTOINCREMENT) -- declaracion como 'primary key'
);
```

Lo habitual es definir las claves primarias como enteros autoincrementales, de modo que su valor se asigne automáticamente y previniendo su repetición.   


Continuando con el ejemplo se crea una segunda tabla, con sus propios campos y su propia clave primaria, esta vez para registrar los turnos médicos de los usuarios:

```sql title="Tabla turnos - con clave primaria" hl_lines="2 7"
CREATE TABLE "turnos_medicos" (
	"id_turno"	INTEGER,                    -- atributo PK
	"profesional"	TEXT,
	"id_usuario"	INTEGER,
	"motivo"	TEXT,
	"horario"	TEXT,
	PRIMARY KEY("id_turno" AUTOINCREMENT)   -- declaracion PK
);
```

Los registros se cargan sin incluir un valor para la clave primaria porque éste es asignado automáticamente por el gestor de la base de datos:

```sql title="Carga de datos - primary "
INSERT INTO turnos_medicos(profesional, id_usuario, motivo, horario)
-- el valor de la PK NO se incluye 
VALUES 	('Dr Gero', 1, 'dolor panza', '13:30')  ,	
		('Dr Manhattan', 3, 'dolor cabeza', '14:30') ;	
		
SELECT * FROM turnos_medicos ;
```

El resultado es la tabla siguiente:

|id_turno|profesional|id_usuario|motivo|horario|
|:---|:---|:----|:---|:---|
|1|	Dr Gero|1|dolor panza|13:30|
|2|	Dr Manhattan|3|dolor cabeza|14:30|


## Foreign key (FK)

Las claves foráneas son claves de una tabla que sirven para *referenciar* (apuntar) a los registros de otras tablas. 



Supóngase quese necesita superponer dos tablas para mostrarlas juntas.
Esto se hace separando por comas los nombres de tablas a mezclarse:

```sql title="Claves primarias y foráneas"
SELECT * FROM turnos_medicos , usuarios;
```
En este ejemplo, el campo *id_turno* sigue siendo clave primaria, 
pero dentro de la tabla se carga el campo *id_usuario* el cual apunta a la otra tabla. 
Entonces *id_usuario* es en la tabla compuesta una clave foránea (*foreign key*).

Lo habitual es elegir siempre como claves foráneas a las claves primarias de otras tablas.
Esto permite una referencia segura de unas tablas a otras, 
porque las claves primarias son inmutables 
y con ellas se evitan errores en caso de modificar los registros.

## Alias

Los alias funcionan como nombres alternativos para los campos de una tabla.
El alias se crea en la lectura con la cláusula `AS`.

Supóngase por ejemplo [base de datos Northwind para SQLite](northwind.md). Si se desea llamar 
`Apellido` al campo `LastName` se hace:


```sql title="Alias - campo único"
SELECT LastName AS Apellido FROM Employees;
```


|Apellido|
|---|
|Davolio|
|Fuller|
|Leverling|
|...|





En este ejemplo `Apellido` es un alias para `LastName`.

Múltiples alias pueden ser asignados en una misma lectura de datos:


```sql title="Alias - múltiples campos"
SELECT LastName AS apellido, FirstName AS nombre FROM Employees;
```

|apellido	|nombre|
|---|---|
|Davolio	|Nancy|
|Fuller	|Andrew|
|Leverling	|Janet|
|...|




Usar alias facilita leer campos afectados por funciones.

Por ejemplo, para leer los precios y su doble de la tabla `Products`:
```sql title="Alias para funciones"
SELECT Price AS precio, Price*2 AS precio_doble FROM Products;
```

En este caso la columna del campo `Price` se mostrará bajo el alias `precio` y su réplica ya multiplicada por dos se mostrará bajo el alias `precio_doble`:

|precio | precio_doble|
|---|---|
|18	| 36 |
|19	| 38 |
|10	| 20 |
|...|


## Resumen

- Las *primary keys* son campos que **identifican registros** de una tabla;
- Las *foreign keys* son campos que **apuntan** a las *primary keys* de otras tablas;
- Los *alias* son **apodos temporales** para ciertos *campos específicos* de la tabla.


