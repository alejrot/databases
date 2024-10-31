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



# Diferencias entre gestores - Migración



## Características de los gestores

### SQLite
- Es un gestor embebido
- Trabaja con archivo único
- Es ideal para aplicaciones embebidas y prototipos
- No sirve para aplicaciones de gran escala o de alto rendimiento

### MySQL
- Es un gestor basado en servidor
- Puede trabajar con múltiples archivos
- Es ideal para aplicaciones de gran escala o de alto rendimiento

### PostgreSQL
- Es un gestor basado en servidor
- Puede trabajar con múltiples archivos
- Es ideal para aplicaciones de gran escala o de alto rendimiento
- Tiene extensiones propias

### SQLServer
- Es de pago
- Es un gestor basado en servidor
- Puede trabajar con múltiples archivos
- Es ideal para aplicaciones de gran escala o de alto rendimiento
- Tiene extensiones propias





## Migracion entre gestores

Estructura:

- Exportar la base de datos en formato SQL;
- Abrir y modificar las consultas para adaptarla al nuevo gestor;
- Importar la base de datos modificada para crear la estructura de tablas;

Datos:

- Exportar cada tabla, preferiblemente en formato CSV (*Comma Separated Values*);
- Importar cada tabla en el nuevo gestor.

1. Se adaptan las consultas para crear el formato de tablas en el nuevo gestor de base de datos;
2. Para migrar los datos se recomienda exportar cada tabla de la base de datos en archivos CSV e importarlos con el nuevo gestor.





## Comandos 


### CREATE

=== "SQLite"
    
    ```sql
    CREATE TABLE nombre_tabla(columna1 tipo1, columna2 tipo2, ...);
    ```

=== "MySQL"

    ```sql
    CREATE TABLE nombre_tabla(columna1 tipo1, columna2 tipo2, ...) ENGINE = InnoDB;
    ```

=== "SQLServer"

    ```sql
    CREATE TABLE nombre_tabla(columna1 tipo1, columna2 tipo2, ...);
    ```

=== "PosgreSQL"

    ```sql
    CREATE TABLE nombre_tabla(columna1 tipo1, columna2 tipo2, ...);
    ```

MySQL requiere que se indique el `#!sql ENGINE`.


### CREATE (con clave primaria)


=== "SQLite"
    
    ```sql
    CREATE TABLE ejemplo (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre VARCHAR(50) NOT NULL, 
        apellido VARCHAR(50) NOT NULL
    )
    ```

=== "MySQL"

    ```sql
    CREATE TABLE ejemplo(
        id INT NOT NULL AUTO_INCREMENT,
        nombre VARCHAR(50) NOT NULL,
        apellido VARCHAR(50) NOT NULL,
        PRIMARY KEY (id)
    )
    ```

=== "SQLServer"

    ```sql
    CREATE TABLE ejemplo(
        id INT IDENTITY(1,1) PRIMARY KEY, 
        nombre VARCHAR(50) NOT NULL,
        apellido VARCHAR(50) NOT NULL,
    )
    ```

=== "PosgreSQL"

    ```sql
    CREATE TABLE nombre_tCREATE TABLE ejemplo(
        id SERIAL PRIMARY KEY ,
        nombre VARCHAR(50) NOT NULL,
        apellido VARCHAR(50) NOT NULL
    )
    ```

### RIGHT JOIN


=== "SQLite"
    
    ```sql
    SELECT * FROM tabla2 LEFT JOIN tabla1
    ON tabla2.columna = tabla1.columna;
    ```

=== "MySQL"

    ```sql
    SELECT * FROM tabla1 RIGHT JOIN tabla2
    ON tabla1.columna = tabla2.columna;
    ```

=== "SQLServer"

    ```sql
    SELECT * FROM tabla1 RIGHT JOIN tabla2
    ON tabla1.columna = tabla2.columna;
    ```

=== "PosgreSQL"

    ```sql
    SELECT * FROM tabla1 RIGHT JOIN tabla2
    ON tabla1.columna = tabla2.columna;
    ```

El `#!sql RIGHT JOIN` no está implementado en SQLite. 
Para los otros gestores el código es igual.


### Full JOIN



=== "SQLite"
    
    ```sql
    -- LEFT JOIN
    SELECT * FROM tabla1 LEFT JOIN tabla2
    ON tabla1.columna = tabla2.columna;

    UNION

    -- LEFT JOIN INVERSO
    SELECT * FROM tabla2 LEFT JOIN tabla1
    ON tabla2.columna = tabla1.columna;
    ```

=== "MySQL"

    ```sql    
    -- LEFT JOIN
    SELECT * FROM tabla1 LEFT JOIN tabla2
    ON tabla1.columna = tabla2.columna;

    UNION
    
    -- RIGHT JOIN
    SELECT * FROM tabla1 RIGHT JOIN tabla2
    ON tabla1.columna = tabla2.columna;
    ```

=== "SQLServer"

    ```sql
    SELECT * FROM tabla1 FULL OUTER JOIN tabla2
    ON tabla1.columna = tabla2.columna;
    ```

=== "PosgreSQL"

    ```sql
    SELECT * FROM tabla1 FULL OUTER JOIN tabla2
    ON tabla1.columna = tabla2.columna;
    ```



### Funcion NOW()

Esta función lee la hora actual del sistema con formato

=== "SQLite"
    
    ```sql
    -- REVISAR
    SELECT NOW()
    ```

=== "MySQL"

    ```sql
    SELECT NOW()
    ```

=== "SQLServer"

    ```sql
    SELECT GETDATE()
    ```

=== "PosgreSQL"

    ```sql
    SELECT NOW()
    ```


### CEIL() y CEILING(), FLOOR(), ROUND()

=== "SQLite"
    
    ```sql
    -- REVISAR
    CEIL(numero)
    ```

=== "MySQL"

    ```sql
    CEILING(numero)
    ```

=== "SQLServer"

    ```sql
    CEILING(numero)
    ```

=== "PosgreSQL"

    ```sql
    CEIL(numero)
    ```


### LIMIT
<!-- ### `LIMIT` -->

=== "SQLite"
    
    ```sql
    SELECT * FROM tabla LIMIT n;
    ```

=== "MySQL"

    ```sql
    SELECT * FROM tabla LIMIT n;
    ```

=== "SQLServer"

    ```sql
    SELECT TOP n * FROM tabla;
    ```

=== "PosgreSQL"

    ```sql
    SELECT * FROM tabla LIMIT n;
    ```


### LIMIT con OFFSET

=== "SQLite"
    
    ```sql
    SELECT * FROM tabla LIMIT cantidad OFFSET inicio;
    ```

=== "MySQL"

    ```sql
    SELECT * FROM tabla LIMIT cantidad OFFSET inicio;
    ```

=== "SQLServer"

    ```sql
    SELECT * FROM (
        SELECT *, ROW_NUMBER() OVER (ORDER BY (SELECT ALL)) AS RowNum
        FROM tabla 
    ) AS Resultado
    WHERE Resultado.RowNum BETWEEN inicio + 1 AND inicio + cantidad;
    ```

=== "PosgreSQL"

    ```sql
    SELECT * FROM tabla LIMIT cantidad OFFSET inicio;
    ```




### LIKE y ELIKE

`#!sql LIKE` no distingue mayúsculas de minúsculas.
`#!sql LIKE` funciona igual para todos.
`#!sql ELIKE` distingue mayúsculas de minúsculas. 
Sólo disponible con PosgreSQL.




