# instalar:
# pip install mysql-connector-python

# import mysql.connector
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


# Conexion - con 'kargs'
# connection = connector.connect(
#     host     = "127.0.0.1",
#     port     = "3306",
#     database = "hello_mysql",
#     user     = "root",
#     password = "root123"
#     )

cursor = connection.cursor()

query = "SELECT * FROM users"
cursor.execute(query)
result = cursor.fetchall()

for row in result:
    print(row)

cursor.close()
connection.close()
