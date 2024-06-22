
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# pip install matplotlib

conector = sqlite3.connect("Northwind.db")


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
plt.xticks(rotation = 90)   # etiquetas en vertical
plt.show()

#  10 EMPLEADOS CON MÁS VENTAS
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

empleados_top = pd.read_sql_query(consulta2, conector)

# tabla en pantalla - texto simple
# print(empleados_top)


# parámetros de la gráfica
empleados_top.plot(
    x="Employee",
    y="Total",
    kind="bar",
    figsize=(10, 5), 
    legend = False
    )

# Gráfica de Barras
plt.title("Top 10 Empleados")
plt.xlabel("Empleados")
plt.ylabel("Monto ventas")
plt.xticks(rotation = 45)   # etiquetas a 45º
plt.show()



