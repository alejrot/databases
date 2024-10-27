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

```python title="SQLite3 - importación"
import sqlite3
```

## Conectores y cursores

Se crea un conector que abre el archivo que almacena la base de datos:

```python title="SQLite3 - conector"
# ejemplo: archivo de base de datos aledaño al ejecutable
ruta_archivo = "Northwind.db"

# conexion con  base de datos en archivo
conector = sqlite3.connect(ruta_archivo)
```

El siguiente paso es crear un *cursor* para manejar pedidos y respuestas de SQLite:

```python title="SQLite3 - cursor"
# Cursor 
cursor = conector.cursor()
```

## Consultas y transacciones

Para hacer las consultas se usa el método `execute()`, 
el cual **siempre** crea una transacción. 
Las instrucciones de SQL se ingresan como argumento en formato texto.

### Lectura


```python title="SQlite3 - consultar"
# inicio de transacción (BEGIN implícito)
cursor.execute(
    # Rutina SQL, 1 renglon
    'SELECT ProductName, Price FROM Products;'
    )
```
La respuesta del gestor se recibe con el método `fetchall()`:
```python title="SQlite3 - leer respuesta"
#respuesta de la base de datos
resultados = cursor.fetchall()
print(resultados)
```
La respuesta viene dada como una lista de tuplas que contienen los registros. 

### Modificar datos


Si se busca leer modificar los datos también se usa el método `execute()`. 
Recordar que este método implícitamente inicia una transacción 
y por tanto los cambios producidos serán temporales:

```python title="SQLite - Iniciar transacción"
# inicio de transacción (BEGIN implícito)
cursor.execute(
    # Consulta SQL: actualización de un nombre de producto
    '''
    UPDATE Products SET ProductName = "Chais" WHERE ProductName = "El Pollo" ;
    '''
)
```
### Validación y descarte

La validación de los cambios introducidos se realiza con el método `commit()` en tanto que el descarte de los mismos se realiza con el método `rollback()`:

 <div class="grid" markdown>

```python title="SQLite - Confirmación de cambios"
# guardado definitivo de cambios
conector.commit()
```

```python title="SQLite - Descarte de cambios"
# reestablecimiento de datos
conector.rollback()
```
 </div>

Una posibilidad del uso de éstos métodos es repartirlos entre las rutinas de excepciones ( `#!py try` - `#!py except` ). 
De esta forma se validan los cambios sólo si no se produjeron excepciones 
y en caso contrario se ordena el reestablecimiento de los datos originales.


```py title="SQLite - Transacción con excepciones Python"
try:
    # inicio de transacción (BEGIN implícito)
    cursor.execute(
        # Consulta SQL: actualización de un nombre de producto
        '''
        UPDATE Products SET ProductName = "Chais" WHERE ProductName = "El Pollo" ;
        '''
        )

except:
    # excepción producida: reestablecimiento de datos
    conector.rollback()
    print("datos reestablecidos")

else:
    # respuesta normal: guardado definitivo de cambios
    conector.commit()
    print("cambios confirmados")
```



## Funciones de usuario (*UDF*)

Las funciones definidas por el usuario (*UDF*) se crean con el método `create_function()`.
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





## Cierre

### Cierre manual

El cierre manual de la base de datos se realiza cerrando tanto el cursor como el conector con el método `close()`:

```python title="SQLite3 - cierre manual"
# cierre
cursor.close()
conector.close()
```

### Cierre automático

Una alternativa es abrir creando un contexto con la cláusula `#!py with`, 
de la misma manera en que suelen abrirse los archivos. 
En tal caso el cierre de la base de datos se hace automáticaticamente al salir del contexto creado, 
el cual es marcado por indentación.


```python title="SQLite3 - cláusula with"
with sqlite3.connect(ruta_archivo) as conector:
    # Cursor 
    cursor = conector.cursor()
    # rutina
    # .....

# cierre automático
```






## Extra: Pandas y Mathplotlib 

### Pandas    

Una opción para darle formato de tablas a la información en consola es usar la biblioteca ***pandas***.
El paquete se instala vía PIP:

``` bash title="Pandas - instalación"    
pip install pandas
```    

El paquete se importa para su uso:

```python title="Pandas - importación"   
import pandas as pd
```

Finalmente el paquete ayuda a dar formato a la data de la consulta 
con ayuda de la función `DataFrame()`:

``` py title="Pandas - formateo de datos"   
dataframe = pd.DataFrame(resultados)
print(dataframe)
```
En este caso se mostrará el contenido tabulado en consola emulando una tabla.



### Matplotlib


La biblioteca ***Mathplotlib*** permite graficar las tablas formateadas con *Pandas* con la función `pyplot()`.
Debe instalarse:

``` bash title="Matplotlib - instalación"    
pip install matplotlib
```    

El paquete requiere importación:

```python title="Matplotlib - importación"   
import matplotlib.pyplot as plt
```


### Combinando paquetes



*Pandas* incluye integrado su propio manejador para realizar consultas y gestionar el resultado ya formateado:

```python title="Handler de Pandas"
# Query para el gestor SQL en formato 'string'
consulta =  '''
    SELECT ProductName, Price FROM Products;
    '''
# Envío consulta y recepción de respuesta
dataframe = pd.read_sql_query(consulta, conector)
```


Con el método `plot()` de *Pandas* se configuran los parámetros de interés de
la gráfica.
Ésta se muestra con la función `show()` de *Matplotlib*:

```python title="Gráfica de barras"
# Pandas - parámetros de la gráfica
dataframe.plot(
    x="ProductName",
    y="Price",
    kind="bar",
    figsize=(10, 5), 
    legend = False
    )

# Matplotlib - Gráfica de Barras
plt.title("Precios")
plt.xlabel("Producto")
plt.ylabel("Valor")
plt.xticks(rotation = 90)   # etiquetas en vertical
plt.show()
```






## Ejemplos

!!! example "Ejemplo Nº1: consulta de precios - por consola"

    ```py title="Northwind - Cierre manual"
    import sqlite3

    # ejemplo: archivo de base de datos aledaño al ejecutable
    ruta_archivo = "Northwind.db"

    # conexion con  base de datos en archivo
    conector = sqlite3.connect(ruta_archivo)
    # Cursor
    cursor = conector.cursor()
    # inicio de transacción (BEGIN implícito)
    cursor.execute(
        # Rutina SQL, 1 renglon
        'SELECT ProductName, Price FROM Products;'
        )

    #respuesta de la base de datos
    resultados = cursor.fetchall()
    print(resultados)
    # cierre de conexión
    cursor.close()
    conector.close()
    ```

    ```py title="Northwind - cierre automático"
    import sqlite3

    # ejemplo: archivo de base de datos aledaño al ejecutable
    ruta_archivo = "Northwind.db"

    with sqlite3.connect(ruta_archivo) as conector:
        # Cursor 
        cursor = conector.cursor()
        # inicio de transacción (BEGIN implícito)
        cursor.execute(
            # Rutina SQL, 1 renglon
            'SELECT ProductName, Price FROM Products;'
            )

        #respuesta de la base de datos
        resultados = cursor.fetchall()
        print(resultados)
    ```



!!! example "Ejemplo Nº2: consulta de precios - con gráficas"

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


!!! example "Ejemplo Nº3: Actualización de datos - con excepciones"

    ```python
    import sqlite3

    # ejemplo: archivo de base de datos aledaño al ejecutable
    ruta_archivo = "Northwind.db"

    # conexion con  base de datos en archivo
    with sqlite3.connect(ruta_archivo) as conector:
        # Cursor 
        cursor = conector.cursor()
      
        try:
            # inicio de transacción (BEGIN implícito)
            cursor.execute(
                # Modificación de campo
                '''
                UPDATE Products SET ProductName = "Chais" WHERE ProductName = "El Pollo" ;
                '''
                )
        except:
            # reestablecimiento de datos
            conector.rollback()
            print("datos reestablecidos")

        else:
            # guardado definitivo de cambios
            conector.commit()
            print("cambios confirmados")
    ```



## Referencias

[Soy Dalto - Curso de SQL desde CERO (Completo)](https://youtu.be/DFg1V-rO6Pg?t=24731)
