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
  # - MySQL
  # - PostgreSQL
  # - MariaDB
---



# Funciones de Agregacion

Las funciones de agregación combinan los valores que tiene el campo de tabla especificado.
Estas funciones son afectadas por la cláusula `#!sql WHERE()`,
por cuanto esta implementa el filtrado de registros 
y por tanto afecta qué valores quedan en el campo.

## COUNT() 

`#!sql COUNT()` cuenta todos los valores disponibles del campo elegido:

```sql title="conteo"
-- Conteo de empleados
SELECT COUNT(FirstName) FROM Employees;
```
Resultado:

|COUNT(FirstName)|
|---|
|10|


```sql title="conteo y asignacion de alias"
-- Conteo de empleados
SELECT COUNT(FirstName) AS cantidad_empleados FROM Employees;
```

Resultado:

|cantidad_empleados|
|---|
|10|


## SUM()


`#!sql SUM()` suma todos los valores disponibles del campo elegido:

```sql title="Sumatoria de valores"
-- Sumatoria de precios
SELECT ProductName, SUM(Price) FROM Products; 
```
Resultado:

|SUM(Price)|
|---|
|2222.71|


## AVG()

`#!sql AVG()` calcula la media aritmética (*average*) del campo seleccionado.

```sql title="promedio (average)"
-- media de precios de productos
SELECT AVG(Price) FROM Products; 
```
Resultado:

|AVG(Price)|
|---|
|28.8663636363636|






## MIN()

La función `#!sql MIN()` elige el registro cuyo valor de campo sea el menor.

```sql title="valor minimo"
-- producto con menor precio
SELECT ProductID, ProductName, MIN(Price) FROM Products; 
```
Resultado:

|ProductID|ProductName|MIN(Price)|
|---|---|---|
|33|Geitost|2.5|

Para prevenir lecturas erróneas por valores no configurados se filtran los valores nulos:

```sql title="valor minimo - valores nulos descartados"
-- Minimo precio, con nombre e ID de producto 
SELECT ProductID, ProductName, MIN(Price) FROM Products
-- descarte de campos nulos
WHERE  ProductName IS NOT NULL AND Price IS NOT NULL;
```
En este caso el resultado es el obtenido previamente




## MAX()

La función `#!sql MAX()` elige el registro cuyo valor de campo sea el mayor.

```sql title="valor máximo - valores nulos descartados"
-- Maximo precio, con nombre e ID de producto 
SELECT ProductID, ProductName, MAX(Price) FROM Products
-- descarte de campos nulos
WHERE  ProductName IS NOT NULL AND Price IS NOT NULL;
```

Resultado:

|ProductID|	ProductName|	MAX(Price)|
|---|---|---|
|38	|Côte de Blaye|	263.5|


## Funciones numéricas

Con el fin de manipular valores numéricos se dispone de las funciones `#!sql ROUND()`, `#!sql FLOOR()`y `#!sql CEIL()` : 

- `#!sql FLOOR()` elimina los decimales dejando el valor entero inmediatamente inferior;
- `#!sql CEIL()` empuja hacia el valor entero inmediatamente superior;
- `#!sql ROUND()` redondea al número de decimales indicado. Por defecto redonea al valor entero más cercano.

Ejemplo:
<!-- 
```sql title="promedio con redondeo"
-- media (average) con redondeo - cero decimales
SELECT ROUND(AVG(Price)) FROM Products; 
-- redondeo con dos decimales
SELECT ROUND(AVG(Price), 2) FROM Products; 
```
 -->

```sql title="comparativa de redondeos"
SELECT AVG(Price) AS media,
	  FLOOR(AVG(Price)) AS piso,
    ROUND(AVG(Price), 2) AS redondeo2,
	  ROUND(AVG(Price)) AS redondeo, 
	  CEIL(AVG(Price)) AS techo
FROM Products; 
```

|media|	piso|	redondeo2|	redondeo|	techo|
|---|---|---|---|---|
|28.8663636363636	|28.0	|28.87	|29.0	|29.0|


!!! info "No son de agregación"

    Estas funciones no son de agregación,
    porque **no combinan ni leen múltiples valores** de campo
    sino que manipula un único valor de entrada

