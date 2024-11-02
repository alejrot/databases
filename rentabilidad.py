
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# pip install matplotlib

conector = sqlite3.connect("Northwind.db")

ej1 = False
ej2 = False
ej3 = True

if ej1:

    # Consulta: 10 productos más rentables

    consulta = '''
        SELECT ProductName, SUM(Price * Quantity) AS Revenue
        FROM OrderDetails od
        JOIN Products p ON p.ProductID = od.ProductID
        GROUP BY od.ProductID
        ORDER BY Revenue DESC
        LIMIT 10
    '''

    productos_top = pd.read_sql_query(consulta, conector)

    # tabla en pantalla - texto simple
    # print(productos_top)


    # parámetros de la gráfica
    productos_top.plot(
        x="ProductName",
        y="Revenue",
        kind="bar",
        figsize=(10, 5), 
        legend = False
        )

    # Gráfica de Barras
    plt.title("10 Productos más rentables")
    plt.xlabel("Productos")
    plt.ylabel("Retorno")
    plt.xticks(rotation = 45)   # etiquetas en vertical
    plt.show()


if ej2:

    #  10 EMPLEADOS CON MÁS VENTAS (CANTIDAD)
    # Consulta 
    consulta2 = '''
        SELECT FirstName ||" "|| LastName AS Employee, COUNT(*) as Total
        FROM Orders o
        JOIN Employees e 
        ON o.EmployeeID = e.EmployeeID
        GROUP BY o.EmployeeID
        ORDER BY Total DESC
        LIMIT 10
    '''

    empleados_top_cantidad = pd.read_sql_query(consulta2, conector)

    # tabla en pantalla - texto simple
    # print(empleados_top)


    # parámetros de la gráfica
    empleados_top_cantidad.plot(
        x="Employee",
        y="Total",
        kind="bar",
        figsize=(10, 5), 
        legend = False
        )

    # Gráfica de Barras
    plt.title("Top 10 Empleados ")
    plt.xlabel("Empleados")
    plt.ylabel("Nº ventas")
    plt.xticks(rotation = 45)   # etiquetas a 45º
    plt.show()


if ej3:

    #  10 EMPLEADOS CON MÁS VENTAS (CANTIDAD)
    # Consulta 
    consulta3 = '''
        SELECT FirstName ||" "|| LastName AS Employee, SUM(ProductPrice) as Total
        FROM Orders o
        JOIN Employees e 
        ON o.EmployeeID = e.EmployeeID
        GROUP BY o.EmployeeID
        ORDER BY Total DESC
        LIMIT 10
    '''

    empleados_top_montos = pd.read_sql_query(consulta3, conector)

    # parámetros de la gráfica
    empleados_top_montos.plot(
        x="Employee",
        y="Total",
        kind="bar",
        figsize=(10, 5), 
        legend = False
        )

    # Gráfica de Barras
    plt.title("Top 10 Empleados ")
    plt.xlabel("Empleados")
    plt.ylabel("Montos")
    plt.xticks(rotation = 45)   # etiquetas a 45º
    plt.show()
