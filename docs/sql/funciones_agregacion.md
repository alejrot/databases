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



# Funciones de Agregacion

## COUNT() 

```sql
-- conteo
SELECT COUNT(FirstName) FROM Employees;
-- Conteo y asignacion de alias
SELECT COUNT(FirstName) AS cantidad_empleados FROM Employees;
```

## SUM()

```sql
SELECT Price FROM Products;

-- Suma
SELECT SUM(Price) FROM Products; 
```

## AVG()

```sql
-- media (average)
SELECT AVG(Price) FROM Products; 
-- media (average) con redondeo
SELECT ROUND(AVG(Price)) FROM Products; 

-- redondeo con dos digitos
SELECT ROUND(AVG(Price), 2) FROM Products; 
```

## MIN()

```sql
SELECT MIN(Price) FROM Products; 
SELECT ProductName, MIN(Price) FROM Products; 

-- Minimo precio con nombre de producto 
SELECT ProductName, MIN(Price) FROM Products
-- descarte de campos nulos
WHERE ProductName IS NOT NULL;
```

## MAX()

```sql
SELECT  MAX(Price) FROM Products;

-- Maximo precio con nombre de producto 
SELECT ProductName, MAX(Price) FROM Products
-- descarte de campos nulos
WHERE ProductName IS NOT NULL;
```

**Comentario:** la funcion `ROUND()`  **no es** de agregacion.
