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

# Consultas

## Query

Las queries (consultas) son **todas** las operaciones que afectan a la base de datos.

## Comentarios


Los comentarios y la anulación de líneas de código SQL se realizan con doble guión (`#!sql --`) al inicio de la línea:


```sql title="Comentarios"
-- texto del commentario
```

## CRUD

El acrónimo CRUD representa las operaciones básicas sobre las bases de datos:

- crear (*create*);
- leer (*read*);
- modificar (*update*);
- eliminar (*delete*).


## Comandos CRUD

### Crear (*create*)


Las tablas se crean con el comando `#!sql CREATE` 
y en la declaración se enumera el nombre de tabla como también el nombre y tipo de cada campo a incluir en la misma.

Por ejemplo, la creación de una tabla llamada *usuarios* que incluya como atributos el nombre, apellido y la edad de cada usario se puede hacer así:

```sql title="Create"
-- declaración
CREATE TABLE "usuarios" (
    -- atributos
	"nombre"	TEXT,
	"apellido"	TEXT,
	"edad"	INTEGER
);
```


!!! info "Fin de instrucción"

    El punto y coma (`;`) indica el final de cada intrucción.


### Actualizar (*update*)

Los datos se actualizan con el comando `#!sql INSERT`.

Ejemplo: cargar datos de un usuario (un *registro*):

```sql title="Update - un registro"
-- eleccion de tabla
INSERT INTO usuarios (nombre, apellido, edad)
-- valores de registro a incluir
VALUES ('Aitor','Tilla', 47) ;
```

Para delimitar los valores de texto se pueden usar comillas simples (`'`) o dobles (`"`). Se recomienda el uso de las comillas simples.

Cargar datos de multiples registros:

```sql title="Update - multiples registros"
-- eleccion de tabla
INSERT INTO usuarios (nombre, apellido, edad)
-- valores de registros a incluir
VALUES 	('Aitor','Tilla', 47),
		('Aquiles','Brinco', 25),
		('Helen', 'Chufe', 31),
		('Susana', 'Torio', 55);
```

Prestar atencion al uso de comas para separar registros.

!!! warning "Datos repetidos"
    Los registros que se repitan serán guardados múltiples veces.


### Leer (*read*)


La lectura de campos y de tablas se realizan con el comando `#!sql SELECT`.

Siguiendo el ejemplo previo, si se necesita leer todo el contenido de la tabla:

```sql title="Read - tabla completa"
-- lectura todos los campos (*)
SELECT * FROM usuarios;
```


|id_usuario|nombre|apellido|edad|
|---|---|---|---|
|1|Aitor	|Tilla|47|
|2|Aquiles|Brinco|25|
|3|Helen	|Chufe|31|
|4|Susana	|Torio|55|


Si en cambio se busca leer algunos campos particulares de una tabla:

```sql title="Read - campos específicos"
-- lectura de campos específicos desde tabla
SELECT nombre, edad FROM usuarios ;
```

|nombre|edad|
|---|----|
|Aitor|47|
|Aquiles|25|
|Helen|31|
|Susana|55|

Los campos elegidos se separan con comas.


### Eliminar (*delete*)

Las tablas se eliminan con el comando `#!sql DELETE`.

Por ejemplo, para eliminar una tabla de usuarios:

```sql title="Delete - tabla completa"
-- Eliminar tabla
DELETE FROM usuarios ;
```

