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
  - SQLAlchemy
  - MySQL
  - PostgreSQL
  - MariaDB
---

# Indices

Los índices son una herramienta auxiliar que permite mejorar los tiempos de consulta para ciertos campos de interés. 

Los índices pueden ser:

- ordinarios
- primarios: establecen unicidad de la fila;
- únicos: aseguran que el valor del campo no se repita en otros registros;
- compuestos: previenen la repetición de combinaciones de valores.


## Creación

Los índices se crean con la sintaxis: 

```sql
CREATE INDEX <alias> ON <tabla> (<campo>)
```

Ejemplo: índice para los nombres de producto

```sql
-- Indice "nombre" apuntando al campo "ProductName" en tabla "Products"
CREATE INDEX nombre ON Products (ProductName)
```

La consulta de campos se realiza normalmente. No se requiere usar el alias. 

Ejemplos:

```sql
SELECT * FROM Products
SELECT * FROM Products WHERE  ProductName = "Chais"
```




!!! warning "Espacio en disco"
    
    Los indices consumen mucho espacio en disco. 
    Esto se agrava cuando se necesita actualizar datos indexados. 
    Por ello hay que ser prudente a la hora de crear índices. 

!!! warning "Procesamiento"

    El uso de indices exige procesamiento adicional cada vez que se actualizan las tablas. 
    En caso de abusarse del uso de índices,
    este procesamiento extra puede anular la mejora de rendimiento.


Se recomienda crear índices para campos:

- frecuentemente accedidos;
- con alta cardinalidad. 



!!! tip "Claves foráenas"
    
    Las *foreign keys* son campos recomendados para indexar.


## Índices únicos

Los índices sirven también como indicadores únicos para ciertos campos de interés, 
previniento la repetición de valores o de combinaciones de valores.
<!-- sirviendo como alternativa ante  -->



```sql title="Indice único"
-- Indice unico compuesto para empleados (nombres o apellidos podrían estar repetidos)
-- Crear este índice impedirá la repetición de pares nombre - apellido
CREATE UNIQUE INDEX name ON Employees (FirstName, LastName)
```




## Eliminar índices

Los indices se eliminan con la orden `DROP`:

```sql
DROP INDEX <alias>
```

## Nomenclatura de índices

Para ponerle nombre a los indices es habitual usar la nomenclatura:

```sql
idx_<nombre_tabla>_<nombre_campo>
```

## Ejemplo

```sql
-- Consulta con unión interna
SELECT * FROM OrderDetails od
INNER JOIN Orders o
WHERE OrderDate > "1996-07-04"
AND od.Quantity > 10

-- Crear indices
CREATE INDEX cantidad ON OrderDetails (Quantity);
CREATE INDEX fecha	  ON Orders (OrderDate);

-- eliminar indices
DROP INDEX cantidad ;
DROP INDEX fecha	;
```

