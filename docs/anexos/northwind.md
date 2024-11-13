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



# Anexo - NorthWind 


Para mayor comodidad de uso se adjunta la base de datos Northwind adaptada para los gestores de base de datos más populares.


<!-- Links de descarga: -->


=== "SQLite"

    [Ver código online desde Wikiversity](https://en.wikiversity.org/wiki/Database_Examples/Northwind/SQLite)

    [Descargar script (.sql)](northwind_sqlite.sql){ .md-button .md-button--primary }


=== "MySQL / MariaDB"

    [Ver código online desde Wikiversity](https://en.wikiversity.org/wiki/Database_Examples/Northwind/MySQL)

    [Descargar script (.sql)](northwind_mysql.sql){ .md-button .md-button--primary }


=== "PostgreSQL"

    [Ver código online desde Wikiversity](https://en.wikiversity.org/wiki/Database_Examples/Northwind/PostgreSQL)

    [Descargar script (.sql)](northwind_postgresql.sql){ .md-button .md-button--primary }

=== "SQL Server"

    [Ver código online desde Wikiversity](https://en.wikiversity.org/wiki/Database_Examples/Northwind/SQL_Server)

    [Descargar script (.sql)](northwind_sqlserver.sql){ .md-button .md-button--primary }


Código extraído de [Wikiversity](https://en.wikiversity.org/wiki/Database_Examples/Northwind) con [licencia Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)




**Diagrama Entidad-Estado (ER):**

```mermaid 
erDiagram

    Customers ||--|{ Orders : CustomerID	
    Employees ||--|{ Orders : EmployeeID	
    Shippers  ||--|{ Orders : ShipperID	

    Orders ||--|{ OrderDetails : OrderID	

    OrderDetails }|--|| Products: ProductID

    Products }|--|| Categories: CategoryID	
    Products }|--|| Suppliers: SupplierID

    Orders{
        INT OrderID	
        INT CustomerID	
        INT EmployeeID	
        DATETIME OrderDate	
        INT ShipperID
    }
    OrderDetails{
        INT OrderDetailID	
        INT OrderID	
        INT ProductID	
        INT Quantity
    }
    Products{
        INT ProductID
        TEXT ProductName	
        INT SupplierID	
        INT CategoryID	
        TEXT Unit	
        NUMERIC Price
    }
    Employees{
        INT EmployeeID
        TEXT LastName
        TEXT FirstName
        DATE BirthDate
        TEXT Photo
        TEXT Notes
    }
    Categories{
        INT CategoryID
        TEXT CategoryName
        TEXT Description
    }
    Customers{
        INT CustomerID	
        TEXT CustomerName	
        TEXT ContactName	
        TEXT Address	
        TEXT City	
        TEXT PostalCode	
        TEXT Country
    }
    Shippers{
        INT ShipperID
        TEXT ShipperName	
        TEXT Phone
    }
    Suppliers{
        INT SupplierID
        TEXT SupplierName
        TEXT ContactName
        TEXT Address
        TEXT City
        TEXT PostalCode
        TEXT Country
        TEXT Phone
    }
```


