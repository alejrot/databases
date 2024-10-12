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




# Uso en Python


## Importación

Python puede conectarse con SQLite mediante el conector *sqlite3*, el cual debe importarse:

```python
import sqlite3
```

## Conectores y cursores

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

## Consultas y transacciones

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


## pandas y mathplotlib 

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



## modificar datos

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

## funciones de usuario

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
## cierre

El cierre manual de la base de datos se realiza cerrando tanto el cursor como el conector con el método *.close()*:

```python
# cierre
cursor.close()
conector.close()
```

Una opcion es abrir creando un contexto con la *cláusula **with***, de la misma manera en que suelen abrirse los archivos. En tal caso el cierre de la base de datos se hace automáticaticamente al salir del contexto creado, el cual es marcado por indentación.




## Referencias

[Soy Dalto - Curso de SQL desde CERO (Completo)](https://youtu.be/DFg1V-rO6Pg?t=24731)
