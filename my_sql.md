
[Curso de SQL y BASES DE DATOS Desde Cero para PRINCIPIANTES](https://www.youtube.com/watch?v=OuJerKzV5T0&t=186s)

[NorthWind para MySQL](https://en.wikiversity.org/wiki/Database_Examples/Northwind/MySQL)

[NorthWind para PosgreSQL](https://en.wikiversity.org/wiki/Database_Examples/Northwind/PostgreSQL)

[NorthWind para SQL Server](https://en.wikiversity.org/wiki/Database_Examples/Northwind/SQL_Server)

# MySQL



## PENDIENTES:

- Gestion de permisos para usuarios normales
- Paradigma declarativo
- Conectores Python para MySQL/MariaDB, PostgreSQL, etc




### PAntUML

[render PlantUML - online](https://www.plantuml.com/)

[PUML para MkDocs](https://github.com/MikhailKravets/mkdocs_puml)




## Clientes multiplataforma

[DB Visualizer](https://www.dbvis.com)

[phpMyAdmin](https://www.phpmyadmin.net)

[DbForge](https://www.devart.com/dbforge/)


[SqlPro Studio](https://www.sqlprostudio.com)

[TablePlus](https://tableplus.com)


## Instalar (Windows)

[MySQL Installer](https://dev.mysql.com/downloads/installer/)

[MySQL WorkBench](https://dev.mysql.com/downloads/workbench/)





## Servidor


MySQL trabaja creando servidores,
los cuales son administrados por un usuario administrador (*root*)
y que pueden ser accedidos por usuarios internos.
Estos usuarios internos son creados por *root* y tienen permisos recortados.


## Conexión

MySQL y MaríaDB se conectan a sus bases de datos con el protocolo TCP/IP
y usan de manera predeterminada el puerto 3306.
Si la base de datos se ubica en el mismo equipo entonces la IP de conexión sera `localhost`:;


```http
http:\\localhost:3306
http:\\127.0.0.1:3306
```


## Schemas

Cada servidor puede soportar varias bases de datos en simultáneo.
Estas son llamadas *schemas*.
Cada servidor crea algunas bases de datos internas automáticamente:
- `sys` ;
- `world`;
- `sakila`

 Pueden crearse de manera gráfica
o ejecutarse desde la terminal de MySQL:

```sql
CREATE DATABASE hello_mysql;
```
```sql
DROP DATABASE hello_mysql;
```

## Conexiones

Un *'schema'* puede ser accedido por múltiples conexiones distintas.
Cada conexión se puede crear manualmente en MySQL Workbench,
asignando un nombre de conexion, y configurando los  parámetros de conexión, el "esquema" elegido, el usuario y contraseña, etc.



## Guia de Estilos SQL

Hay varios estilos de escritura para nombrar los campos (columnas) de SQL: camelcase,  todo en mayusculas, etc.
Uno muy habitual es escribir las palabras del nombre totalmente en minúsculas y unirlas con guiones bajos.


## Tablas

base de datos -> Click derecho -> 'Create table'
Se permite dar nombre a la nueva tabla,
dar nombre al nuevo campo, elegir tipo, seleccionar como clave primaria, etc

Aspectos interesantes:
- las tablas pueden ser **modificadas** tras su creación;
- El gestor gráfico informa el **código equivalente** de la operación.

**TIP:** el Nº de la clave primaria,
al autoincrementarse,
toma siempre como referencia la clave asignada más grande.
Esto le permite evitar errores por repetición de clave.



### Eliminar

```sql
DROP TABLE new_tabledfcfd ;
```




### UPDATE

Agregar edades a la tabla `users`:
``` sql
UPDATE `hello_mysql`.`users` SET `age` = '27' WHERE (`id` = '1');
UPDATE `hello_mysql`.`users` SET `age` = '36' WHERE (`id` = '2');
UPDATE `hello_mysql`.`users` SET `age` = '45' WHERE (`id` = '4');
UPDATE `hello_mysql`.`users` SET `age` = '7' WHERE (`id` = '7');
UPDATE `hello_mysql`.`users` SET `age` = '13' WHERE (`id` = '6');
UPDATE `hello_mysql`.`users` SET `age` = '64' WHERE (`id` = '8');
```



## WARNING:  Comillas dobles vs Comillas simples

https://stackovercoder.es/programming/1992314/what-is-the-difference-between-single-and-double-quotes-in-sql

>En **ANSI SQL**, las comillas dobles citan nombres de objetos (por ejemplo, tablas) que les permite contener caracteres no permitidos de otra manera, o ser lo mismo que palabras reservadas (evítelo, en realidad).
>
>Las comillas simples son para cadenas.
>
>Sin embargo,**MySQL es ajeno al estándar** (a menos que se cambie su SQL_MODE) y permite que se usen de manera intercambiable para cadenas.
>
>Además, Sybase y Microsoft también usan corchetes para las citas de identificadores.
>
>Por lo tanto, es un poco específico del proveedor.
>
>Otras bases de datos como Postgres e IBM se adhieren al estándar ansi :)



### DISTINCT

```sql
SELECT DISTINCT *  FROM new_table;
```

```sql
SELECT DISTINCT age FROM new_table;
```


### LIKE

LIKE se puede usar con comodines (`%`) para detectar aptornes

Usuarios que usan e-mail de Google:

```sql
SELECT * FROM users WHERE email like '%@gmail.com';
```

Usuarios con e-mail que comienzan con `sara`

```sql
SELECT * FROM users WHERE email like 'sara%';
```


### COUNT



La funcion `COUNT()` ignora en el conteo los registros vacíos (`NULL`).
Ejemplo: si la tabla `users` tiene 6 registros pero sólo 4 tienen indicada la edad
entonces `COUNT(age)` sólo contará 4.


```sql
SELECT COUNT(*) FROM users;      -- 6 personas
SELECT COUNT(age) FROM users;    -- 4 tienen edad
```


### SUM, AVG

Las funciones `SUM()`, `AVG()` ignoran los valores nulos al computar los resultados:

```sql
SELECT SUM(age) FROM users;    -- NULLs ignorados
SELECT AVG(age) FROM users;    -- NULLs ignorados
```

### IN

```sql
SELECT * FROM new_table WHERE name IN ("Susana", "aquiles","matias");
```


### BETWEEN

```sql
SELECT * FROM new_table WHERE age BETWEEN 20 AND 30;
```


### CONCAT()

Concatena valores de campo

```sql
SELECT CONCAT(name, surname) FROM new_table;
SELECT CONCAT('Nombre: ',name,'; Apellido: ', surname) FROM new_table;


SELECT CONCAT(name, date) FROM new_table;
SELECT CONCAT('Nombre: ',name,'; Fecha: ', date) FROM new_table;

```

## CASE


Salida de texto
```sql
SELECT *,
CASE
    WHEN age >17 THEN 'Es mayor'
    ELSE 'Es menor'
END AS '¿Es mayor de edad?'
FROM users;
```


```sql
SELECT *,
CASE
    WHEN age >18 THEN 'Es mayor'
    WHEN age =18 THEN 'Acaba de cumplir 18'
    ELSE 'Es menor'
END AS '¿Es mayor de edad?'
FROM users;
```

Salida booleana

```sql
SELECT *,
CASE
    WHEN age >17 THEN True
    ELSE False
END AS '¿Es mayor de edad?'
FROM users;
```

### IFNULL()

Esta función reemplaza los vacíos ( `NULL`) del campo indicado por el valor que se especifique

```sql
SELECT name, IFNULL(age, 0) AS age FROM users;
```


### Otras funciones

MySQL incorpora una gran variedad de funciones adicionales no estandarizadas.



## UPDATE


MySQL trae activado de forma predefinida el ***'safe update mode'***.
Éste previene la modificación accidental de la tabal de datos,
obligando a especificar con la cláusula `WHERE` las condiciones de modificación.

```sql
-- MAL
UPDATE users SET age=21;
```

```sql
-- BIEN
UPDATE users SET age=21 WHERE id=4;
UPDATE users SET age=20, date='2021-11-07' WHERE id=4;
```

La base de datos puede convertir los tipos de datos de entrada de manera automática:

```sql
-- Conversión automática - de string a entero
UPDATE users SET age='24' WHERE id=4;
```

### DELETE

```sql
-- eliminar campo
DELETE FROM users WHERE id=8;
```


## ADMINISTRAR DBs

La base de datos (*database* o *schema*) es el contenedor para las tablas de datos.

En este contexto ``DATABASE` y `SCHEMA` son sinónimos

Crear:
```sql
CREATE SCHEMA   nueva_db;
CREATE DATABASE nueva_db;
```

Eliminar:

```sql
DROP SCHEMA   nueva_db;
DROP DATABASE nueva_db;
```




## Tablas





```sql
CREATE TABLE persona2 (
id int NOT NULL,
name varchar(100) NOT NULL,
age int,
email varchar(50),
created date
);
```

```sql
CREATE TABLE persona3 (
id int NOT NULL,
name varchar(100) NOT NULL,
age int,
email varchar(50),
created datetime,
UNIQUE(ID)
);

```
### CHECK , DEFAULT



```sql
CREATE TABLE persona4 (
id int NOT NULL,
name varchar(100) NOT NULL,
age int,
email varchar(50),
created datetime DEFAULT  CURRENT_TIMESTAMP()  ,
UNIQUE(ID),
PRIMARY KEY(id) ,
CHECK (age >= 18)
);
```


### AUTO_INCREMENT


```sql
CREATE TABLE persona5 (
id int NOT NULL AUTO_INCREMENT,
name varchar(100) NOT NULL,
age int,
email varchar(50),
created datetime DEFAULT  CURRENT_TIMESTAMP()  ,
UNIQUE(ID),
PRIMARY KEY(id) ,
CHECK (age >= 18)
);
```





## ALTER

Este comando permite agregar campos, modificar tipos y quitar campos


Agregar campo a tabla:

``` sql
ALTER TABLE `hello_mysql`.`users`
ADD COLUMN `age` INT NULL AFTER `date`;
```

o:

``` sql
ALTER TABLE persona5
-- campo de texto, 150 caracteres
ADD surname varchar(150) ;
```

Modificar nombre de campo:

``` sql
ALTER TABLE persona5
RENAME COLUMN surname TO apellido;
```

Modificar tipo - longitud de campo:
``` sql
ALTER TABLE persona5
-- campo de texto, 250 caracteres
MODIFY COLUMN apellido varchar(250);
```

Eliminar campo:
``` sql
ALTER TABLE persona5
DROP COLUMN apellido;
```




## Relaciones


1:n, n:n, etc

### Autoreferencia

Un registro puede tener clave foránea
que se apunte a su propia clave primaria
(se referencia a sí mismo)

Ej: tabla de una organización.
Cada miembro tiene un jefe asignado (un *superior*) mediante FK.
El jefe de la organizacion
puede tener  en el campo *superior* `NULL`
o ponerse como jefe de sí mismo


Ejemplo:


tabla de empleados
```sql
CREATE TABLE dni(
	dni_id INT AUTO_INCREMENT PRIMARY KEY,
    dni_number INT NOT NULL,
    user_id INT,
    UNIQUE (dni_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

## Enlazando tablas con claves foráneas

```sql
CREATE TABLE companies(
	company_id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(100)
);

-- agregado de campo
ALTER TABLE users
ADD company_id INT;

ALTER TABLE users
ADD CONSTRAINT fk_companies
FOREIGN KEY (company_id) REFERENCES companies(company_id);
```



## INDEX

Los índices optimizan la lectura de datos
a costa de penalizar la escritura
y el espacio de almacenamiento

Crear indice:

```sql
CREATE INDEX idx_name ON users(name);
```

Crear índice con múltiples claves:

```sql
CREATE INDEX idx_name_age ON users(name , age);
```


Eliminar indice:
```sql
DROP INDEX idx_name ON users;
```


### Unique index

Los índices únicos refuerzan la unicidad (exclusividad)
de los datos internos de los campos apuntados.
En este sentido son una alternativa a las claves primarias
a la hora de forzar la no repetición de datos.


[MySQL Tutorial - MySQL UNIQUE Index](https://www.mysqltutorial.org/mysql-index/mysql-unique-index/)


Crear índice único:

```sql
CREATE UNIQUE INDEX idx_name ON users(name);
```

## Triggers


Son instrucciones que se 'disparan' automáticamente cuando ocurren eventos en ciertas tablas.


Ejemplo: un backup de emails de usuario


Tabla de backups:
```
CREATE TABLE `hello_mysql`.`email_history` (
  `email_history_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `email` VARCHAR(100) NULL,
  PRIMARY KEY (`email_history_id`),
  UNIQUE INDEX `id_UNIQUE` (`email_history_id` ASC) VISIBLE);
```


Definicion del trigger

```sql
delimiter |

CREATE TRIGGER tg_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
	IF OLD.email <> NEW.email THEN
		INSERT INTO email_history(user_id, email)
        VALUES (OLD.user_id, OLD.email);
	END IF;
END;
|
delimiter ;
```

(el delimitador es necesario para crear el trigger)



Evento de disparo: actualización de emails en tabla `users`:

```sql
UPDATE users SET email='yo@miserver.com'   WHERE user_id=4 ;
UPDATE users SET email='jti@miserver.com'   WHERE user_id=4 ;
UPDATE users SET email='jti@miserver.org'   WHERE user_id=4 ;
```

Consulta de cambios:
```sql
-- Nuevo email asignado
SELECT * FROM users	;
-- Viejos emails resguardados
SELECT * FROM email_history	;
```

Eliminar trigger

```sql
DROP TRIGGER tg_email;
```


## COMENTARIOS



```sql
-- comentario simple
```


```sql
/*
Comentario
en varias
lineas
*/
SELECT * FROM users;
```



## VIEWS

Las vistas (*views*) son una representación virtual de una o más tablas.
Son el resultado de una consulta mostrada en formato tabla.

Creación:

```sql
CREATE VIEW v_adult_users AS
SELECT name, age
FROM users
WHERE age>=18;
```

Uso
```sql
SELECT * FROM v_adult_users;
```


Eliminacion

```sql
DROP VIEW v_adult_users;
```


## Procedimientos almacenados


Crear procedimiento (básico)

```sql
DELIMITER //
CREATE PROCEDURE p_all_users()
BEGIN
	-- Rutina interna
	SELECT * FROM users
    WHERE date IS NOT NULL;
END//
```

Ejecutar:

```sql
CALL p_all_users;
```

Eliminar procedimiento

```sql
DROP PROCEDURE  p_all_users;
```

Crear procedimiento - con argumentos
```sql
DELIMITER //
CREATE PROCEDURE p_age_users(IN age_param INT)
BEGIN
	-- Rutina interna
	SELECT * FROM users
    WHERE age=age_param;
END//
```

```sql
CALL p_age_users(36);  -- Existe --> se devuelve
CALL p_age_users(89);  -- No existe --> sin resultados
```

Eliminar procedimiento
```sql
DROP PROCEDURE p_age_users;
```


## Transacciones

Es algo que se ejecuta en bloque
y cuyos cambios se consolidan sólo si se considera que los cambios son correctos.
Esto permite implementar tests junto a las consultas que permitan minimizar el riesgo de errores.


```sql
-- Cambios temporales
START TRANSACTION

-- Confirmación de cambios
COMMIT

-- Descarte de cambios
ROLLBACK
```

## Concurrencia

Los gestores de bases de datos permiten configurar la concurrencia,
la cual se produce cuando múltiples usuarios acceden a la base de datos en simultáneo
y es fuente de errores.



**interbloqueo** *deadlock*:
si hay múltiples cambios en simultáneo el gestor sólo habilita uno de los cambios.


**lecturas sucias** : aquellas lecturas que se producen mientras los datos están siendo modificados.


**Aislamiento de transacciones**


## Conectores


Los conectores permiten conectar software escrito en un lenguaje de programación (Python, Java, etc)
con la base de datos.



Ejemplo para Python: paquete [mysql-connector-python](https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html)

```bash
pip install mysql-connector-python
```


```py
import mysql.connector as connector


# Conexion - con diccionario de datos
config = {
    "host"      : "127.0.0.1",
    "port"      : "3306",
    "database"  : "hello_mysql",
    "user"      : "root",
    "password"  : "root123"
}

connection = connector.connect(**config)
cursor = connection.cursor()

# Consulta
query = "SELECT * FROM users"
cursor.execute(query)
result = cursor.fetchall()

# muestra de datos en pantalla
for row in result:
    print(row)

# cierre de recursos
cursor.close()
connection.close()
```


## SQL injection


## PostgreSQL


## Despliegue


[Vercel](https://vercel.com/home)

para PostgreSQL : [Supabase](https://supabase.com)

[Raiola Networks](https://raiolanetworks.com)



MySQL: [PlanetScale](https://planetscale.com)

MySQL y PostgreSQL[Clever Cloud](https://www.clever-cloud.com)


## Proximos pasos

### Diseño de bases de datos

### Seguridad


### Ventajas comparativas entre gestores


### CURSORES

[HdLeon - Qué diablos son los cursores](https://www.youtube.com/watch?v=4C1cMA-00ag)
