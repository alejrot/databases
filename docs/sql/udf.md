---
tags:
#   - HTML5
  # - JavaScript
  # - CSS
#   - YAML
#   - MkDocs
  - Python
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

<!-- # User Defined Functions (UDF) -->
# Funciones Definidas por el Usuario (UDF)

Las *User Defined Functions* son funciones que se diseñan en el lenguaje anfitrión del programa cliente y se transmiten al gestor de la base de datos. 
Es entonces el gestor el encargado de ejecutar la función indicada por el programa cliente y devolver el resultado en caso de ser requerido.


## Uso en Python

<!-- 

Las funciones definidas por el usuario se crean con  -->


El conector *sqlite3* incorpora
el método `create_function()`
para crear las UDF.
En él debe pasarse como argumento un nombre para la función, 
el número de argumentos que usará 
y la función lambda que define su funcionamiento interno.

```python title="UDF - definición"
# función lambda  de interés 
cubo = lambda n : n*n*n

# Funcion de usuario:
# argumentos: 
# 1 - nombre de la "funcion de usuario"
# 2 - numero de argumentos
# 3 - funcion lambda a ejecutar
conector.create_function("cube",1, cubo)
```

La *función de usuario* así creada se usa normalmente **dentro** de la rutina SQL de la consulta:

```python title="UDF - uso" hl_lines="7"
# inicio de transacción (BEGIN implícito)
cursor.execute(
    # Rutina SQL, consulta de campos con funcion usuario
    '''
    SELECT ProductName, 
        Price, 
        round( cube(Price) , 2) AS CubicPrice 
    FROM Products;
    '''
    )

# respuesta de la base de datos
resultados = cursor.fetchall()
```

