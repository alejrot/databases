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

# Ordenar campos



### ORDER BY

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
El ordenamiento se puede aplicar tambien a campos de texto, en tal caso el ordenamiento es el alfabético

Orden de jerarquías en el ordenamiento:

1. Null
2. Números
3. Caracteres especiales
4. Letras


El ordenamiento se puede afecta. 

Ejemplo: ordenar de forma ascendente pero colocando los *Null* al final:
```sql
SELECT * FROM Products
ORDER BY ProductName ASC NULLS LAST
```
Ejemplo: ordenar de forma descendente pero colocando los *Null* al comienzo:
```sql
SELECT * FROM Products
ORDER BY ProductName DESC NULLS FIRST
```
Ordenamiento aleatorio:
```sql
SELECT * FROM Products
ORDER BY Random();
```
Ordenamiento por dos campos:
```sql
SELECT * FROM Products
ORDER BY ProductName, SupplierID;
```
### DISTINCT
Seleccionar campos no repetidos
```sql
SELECT DISTINCT SupplierID FROM Products;
```



