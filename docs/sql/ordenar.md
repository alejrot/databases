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

# Ordenado y filtrado



## ORDER BY

El ordenamiento de datos se realiza durante la consulta con el comando `#!sql ORDER BY`.
Este comando indica el campo en base al cual se hará el ordenamiento.


### ASC y DESC

La opción `#!sql ASC` permite elegir el orden ascendente,
en tanto que la opción `#!sql DESC` elige el orden descendente.
El ordenamiento será con orden ascendente salvo indicación contraria.


Por ejemplo, para ordenar una tabla de precios de productos en orden ascendente:
```sql title="ordenamiento ascendente"
SELECT * FROM Products
ORDER BY price;
```
o:
```sql title="ordenamiento ascendente explícito"
SELECT * FROM Products
ORDER BY price ASC;
```

|ProductID|	ProductName|	SupplierID|	CategoryID|	Unit|	Price|
|---|---|---|---|---|---|
|33|	Geitost|	15	|4|	500 g	|2.5|
|24|	Guaraná Fantástica|	10|1	|12 - 355 ml cans	|4.5|
|13|	Konbu	|6	|8	|2 kg box|	6|
|...|



Si en cambio se necesita ordenar en orden descendente:
```sql title="ordenamiento descendente"
SELECT * FROM Products
ORDER BY price DESC;
```

|ProductID|	ProductName|	SupplierID|	CategoryID|	Unit|	Price|
|---|---|---|---|---|---|
|38	|Côte de Blaye|	18|	1|	12 - 75 cl bottles|	263.5|
|29	|Thüringer Rostbratwurst|	12|	6|	50 bags x 30 sausgs. |	123.79
|9	|Mishi Kobe Niku|	4|	6|	18 - 500 g pkgs.|	97|
|...|


El ordenamiento se puede aplicar tambien a campos de texto, en tal caso el ordenamiento predefinido es el alfabético.


### Jerarquías de ordenamiento

Hay un orden de jerarquías predefinido en el ordenamiento según el tipo de datos:

1. Null
2. Números
3. Caracteres especiales
4. Letras


La jerarquía de ordenamiento se puede afectar con las cláusulas `#!sql FIRST` y `#!sql LAST`. 

Ejemplo: ordenar de forma descendente pero colocando los *Null* al comienzo:
```sql title="ordenamiento descendente - Nulls al comienzo"
SELECT * FROM Products
ORDER BY ProductName DESC NULLS FIRST
```

Ejemplo: ordenar de forma ascendente pero colocando los *Null* al final:
```sql title="ordenamiento ascendente - Nulls al final"
SELECT * FROM Products
ORDER BY ProductName ASC NULLS LAST
```


### Ordenamiento aleatorio

El ordenamiento aleatorio se logra con ayuda de la función `#!sql RANDOM()`:

```sql title="ordenamiento aleatorio"
SELECT * FROM Products
ORDER BY RANDOM();
```

### Ordenamiento sucesivo

El ordenamiento por varios campos (ordenamiento sucesivo) se realiza indicando los campos uno tras otro: 
```sql title="ordenamiento sucesivo"
SELECT * FROM Products
ORDER BY ProductName, SupplierID;
```



## DISTINCT

El filtrado de los valores repetidos se realiza durante la consulta con la cláusula `#!sql DISTINCT`.


En el ejemplo, se enumeran los IDs de todos los proveedores de una tabla de poductos:
```sql title="campos no repetidos"
SELECT DISTINCT SupplierID FROM Products;
```

|SupplierID|
|----|
|1|
|2|
|3|
|4|
|...|

Todos los IDs repetidos se ocultan.