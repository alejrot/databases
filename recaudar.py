import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# ejemplo: archivo de base de datos aledaño al ejecutable
ruta_archivo = "Northwind.db"



recaudacion_productos = True

recaudacion_empleados = True

###############  VISTAS   #################


# 1º vista: 'OrderDetailsExtended'
with sqlite3.connect(ruta_archivo) as conector:

    # Cursor 
    cursor = conector.cursor()
    
    print("Vista 'OrderDetailsExtended'")

    try:
        # inicio de transacción (BEGIN implícito)
        cursor.execute(
            """
            CREATE VIEW OrderDetailsExtended AS 
            SELECT  OrderDetailID, 
                OrderID, 
                P.ProductID, 
                Quantity, 
                Price ,
                Quantity * Price AS ProductOrderRevenue 
            FROM OrderDetails OD, Products P
            WHERE OD.ProductID=P.ProductID
            """
            )

    except:
        # excepción producida: reestablecimiento de datos
        conector.rollback()
        print("Error: creacion fallida")

    else:
        # respuesta normal: guardado definitivo de cambios
        conector.commit()
        print("Creacion correcta")


# 2º vista: 'ProductsRevenue'
with sqlite3.connect(ruta_archivo) as conector:

    # Cursor 
    cursor = conector.cursor()
    
    print("Vista 'ProductsRevenue'")

    try:
        # inicio de transacción (BEGIN implícito)
        cursor.execute(
            """
            CREATE VIEW ProductsRevenue AS
            SELECT 
                P.ProductID, 
                ProductName, 
                SUM(ProductOrderRevenue) AS ProductRevenue
            FROM Products P
            LEFT JOIN OrderDetailsExtended ODE
            ON P.ProductID=ODE.ProductID
            GROUP BY P.ProductID
            """
            )

    except:
        # excepción producida: reestablecimiento de datos
        conector.rollback()
        print("Error: creacion fallida")

    else:
        # respuesta normal: guardado definitivo de cambios
        conector.commit()
        print("Creacion correcta")


# 3º vista: 'EmployeesSales'
with sqlite3.connect(ruta_archivo) as conector:

    # Cursor 
    cursor = conector.cursor()

    print("Vista 'EmployeesSales'")

    try:
        # inicio de transacción (BEGIN implícito)
        cursor.execute(
            """
            CREATE VIEW EmployeesSales AS 
            SELECT    
                EmployeeID,
                SUM(ProductOrderRevenue) AS EmployeeSales
                FROM OrderDetailsExtended ODE, Orders O
            WHERE ODE.OrderID=O.OrderID
            GROUP BY EmployeeID
            ORDER BY EmployeeID
            """
            )

    except:
        # excepción producida: reestablecimiento de datos
        conector.rollback()
        print("Error: creacion fallida")

    else:
        # respuesta normal: guardado definitivo de cambios
        conector.commit()
        print("Creacion correcta")


# 4º vista: 'EmployeesRevenue'
with sqlite3.connect(ruta_archivo) as conector:

    # Cursor 
    cursor = conector.cursor()

    print("Vista 'EmployeesRevenue'")

    try:
        # inicio de transacción (BEGIN implícito)
        cursor.execute(
            """
            CREATE VIEW EmployeesRevenue AS 
            SELECT 
                E.EmployeeID,
                FirstName ||" "||LastName AS Employee,
                EmployeeSales 
            FROM  Employees E
            LEFT JOIN EmployeesSales  S 
            ON S.EmployeeID=E.EmployeeID
            ORDER BY E.EmployeeID
            """
            )

    except:
        # excepción producida: reestablecimiento de datos
        conector.rollback()
        print("Error: creacion fallida")

    else:
        # respuesta normal: guardado definitivo de cambios
        conector.commit()
        print("Creacion correcta")


####################### LECTURAS #####################



if recaudacion_productos:

    with sqlite3.connect(ruta_archivo) as conector:

        print("PRODUCTOS")

        consulta ="""
            SELECT * FROM ProductsRevenue 
            ORDER BY ProductRevenue
            LIMIT 10
            """

        productos = pd.read_sql_query(consulta, conector)


        # parámetros de la gráfica
        productos.plot(
            x="ProductName",
            y="ProductRevenue",
            kind="bar",
            figsize=(10, 5), 
            legend = False
            )

        # Gráfica de Barras
        plt.title("10 Productos más rentables")
        plt.xlabel("Productos")
        plt.ylabel("Retorno")
        plt.xticks(rotation = -45)   # etiquetas en vertical
        
        plt.grid(True)
        plt.show()
        # plt.savefig("productos_top.png")




if recaudacion_empleados:

    with sqlite3.connect(ruta_archivo) as conector:

        print("EMPLEADOS")


        consulta = """
        SELECT * FROM EmployeesRevenue 
        ORDER BY EmployeeID
        """

        empleados = pd.read_sql_query(consulta, conector)

        # parámetros de la gráfica
        empleados.plot(
            x="Employee",
            y="EmployeeSales",
            kind="bar",
            figsize=(10, 5), 
            legend = False
            )

        # Gráfica de Barras
        plt.title("Top 10 Empleados ")
        plt.xlabel("Empleados")
        plt.ylabel("Nº ventas")
        plt.xticks(rotation = -45)   # etiquetas a 45º



        plt.grid(True)
        plt.show()
        # plt.savefig("empleados_top.png")


