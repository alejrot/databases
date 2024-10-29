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

# Ordenado y filtrado

El ordenamiento de datos se realiza durante la consulta con el comando `ORDER BY`.
Este comando indica el campo en base al cual se hará el ordenamiento.

El filtrado de los valores repetidos se realiza durante la consulta con la cláusula `DISTINCT`.


## ORDER BY

Ordenar un campo en orden ascendente:
```sql
SELECT * FROM Products
ORDER BY price;
```
o:
```sql
SELECT * FROM Products
ORDER BY price ASC;
```
Ordenar en orden desdendente:
```sql

SELECT * FROM Products
ORDER BY price DESC;
```
El ordenamiento se puede aplicar tambien a campos de texto, en tal caso el ordenamiento predefinido es el alfabético.

Orden de jerarquías en el ordenamiento según el tipo de datos:

1. Null
2. Números
3. Caracteres especiales
4. Letras


El ordenamiento se puede afectar con las cláusulas `FIRST` y `LAST` 

Ejemplo: ordenar de forma descendente pero colocando los *Null* al comienzo:
```sql
SELECT * FROM Products
ORDER BY ProductName DESC NULLS FIRST
```

Ejemplo: ordenar de forma ascendente pero colocando los *Null* al final:
```sql
SELECT * FROM Products
ORDER BY ProductName ASC NULLS LAST
```
Ordenamiento aleatorio:
```sql
SELECT * FROM Products
ORDER BY RANDOM();
```
Ordenamiento por dos campos (ordenamiento sucesivo):
```sql
SELECT * FROM Products
ORDER BY ProductName, SupplierID;
```



## DISTINCT


Seleccionar campos no repetidos
```sql
SELECT DISTINCT SupplierID FROM Products;
```



