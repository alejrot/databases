


# Anexo - NorthWind 


Para mayor comodidad de uso se adjunta la base de datos Northwind adaptada para SQLite.
Código extraído de [Wikiversity](https://en.wikiversity.org/wiki/Database_Examples/Northwind/SQLite) con [licencia Creative Commons BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)


[Descarga de archivo "northwind.sql" (para SQLite)](../anexos/northwind_sqlite.sql){ .md-button .md-button--primary }


??? abstract "Ver código de Northwind (SQLite)"

    ```sql title="Northwind para SQLite" linenums="1" 
    --8<- "docs/anexos/northwind_sqlite.sql"
    ```
    { data-search-exclude }


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


