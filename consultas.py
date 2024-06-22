import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

ruta_archivo = "Northwind.db"

# conexion con  base de datos en archivo
conector = sqlite3.connect(ruta_archivo)


cubo = lambda n : n*n*n
# Funcion de usuario:
# argumentos: 
# - nombre de la "funcion de usuario"
# - numero de argumentos
# - funcion de python a ejecutar
conector.create_function("cube",1, cubo)

# Cursor 
cursor = conector.cursor()
# inicio de transacción (BEGIN implícito)
cursor.execute(
    # Consulta SQL
    '''
    UPDATE Products SET ProductName = "Chais" WHERE ProductName = "El Pollo" ;
    '''
)


# inicio de transacción (BEGIN implícito)
cursor.execute(
    # Rutina SQL
    'SELECT ProductName, Price FROM Products;'
)


cursor.execute(
    # Rutina SQL con funcion de usuario y redondeo a dos cifras
    '''
    SELECT ProductName, Price, round( cube(Price) , 2) AS CubicPrice FROM Products;
    '''
)


#respuesta de la base de datos
resultados = cursor.fetchall()
# print("Respuesta: ", results)
#conversion de datos a tabla
dataframe = pd.DataFrame(resultados)
# print(resultados)
# print("-----")
print(dataframe)



consulta =  '''
    SELECT ProductName, Price FROM Products;
    '''
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


#guardado definitivo de cambios
# conector.commit()
# Reestablecimiento de datos
conector.rollback()

# cierre
cursor.close()
conector.close()
# la alternativa al cierre manual es abrir con la directiva 'with'









