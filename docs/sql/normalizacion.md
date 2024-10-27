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


# Normalizacion


La normalizacion  de la base de datos sirve para prevenir anomalias, mejorar el rendimiento y poder hacer consultas más efectivas.

Hay cinco formas normales, cada una con sus características. Cada nueva forma introduce requisitos adicionales a la forma anterior.

## 1º Forma Normal (1NF)
Cada celda debe tener un unico contenido atómico. Se evita cargar la misma celda con múltiples datos o datos compuestos; en cambio se crean varios campos acordes.
Cada atributo debe tener un valor único para cada registro.

Ejemplo tabla mal implementada:

| **ID_usuario**| **datos_usuario**| 
| ----------- | ----------- |
| 1		| 	aqui37, Aquiles, Brinco, 37  |
| 2		| 	helchu45, Helen, Chufe , 45	|

Ejemplo aplicando primera forma normal:

| **ID_usuario**| **alias** | **nombre** | **apellido** | **edad**| 
| --- | --- | --- | --- | --- |
| 1		| 	aqui37	| Aquiles| Brinco | 37  |
| 2		| 	helchu45| Helen| Chufe  | 45	|


## 2º Forma Normal (2NF)
El valor de cada celda debe dependér unicamente de la clave primaria.
(No puede haber celdas con varias claves afectando su contenido). 
Se previene la *dependencia parcial*.

Ejemplo tabla mal implementada:

| **ID_pedido** | **ID_usuario** | **ID_producto** | **producto** | **precio** | **cantidad** |
|---|---|---|---|---|---|
| 1 | 34| 22| galletas | 1 | 15|

En este caso hay dos claves afectando el contenido del registro, que son *ID_pedido* e *ID_producto*.

Una forma acorde a la segunda forma de implementar la tabla es:

| **ID_pedido** | **ID_usuario** | **ID_producto** |**cantidad** |
|---|---|---|---|
| 1 | 34|  22 | 15|

| **ID_producto** | **producto** | **precio** | 
|---|---|---|
| 22| galletas | 1 |

REVISAR

## 3º Forma Normal (3NF)
Se busca eliminar la *dependencia transitiva*. 
Se trata de no repetir relaciones entre campos. 
Por ejemplo: en una tabla de datos de usuarios donde se indica la ciudad de su domicilio y su provincia (provincia/estado/departamento/etc) :


| ID_usuario| nombre_usuario| ciudad	| provincia	|
| ----------- | ----------- |-------|-------|
| 1        | Alberto       	| La Plata|	Provincia de Buenos Aires|
| 2        | Claudia       	| Córdoba  |	Córdoba		|


Hay una redundancia: una misma ciudad sólo puede estar ubicada en una única provincia. La solución es crear una tabla aparte con los datos de las ciudades, cada una con su ID y ser referenciadas por la tabla de usuarios.  

| ID_usuario| nombre_usuario| ID_ciudad	|
| ----------- | ----------- |-------|
| 1        | Alberto       	| 7 |	
| 2        | Claudia       	| 21  |	

| ID_ciudad| | ciudad	| provincia	|
| ----------- | ----------- |-------|-------|
| 7   | La Plata|	Provincia de Buenos Aires|
| 21   | Córdoba  |	Córdoba		|

De esta forma se previene evitar la repetición de datos de ubicación en distintas tablas.


## 4º Forma Normal (4NF)

Evita la redundancia de datos:

- multiples valores para una misma tabla
- valores dependientes de múltiples valores de la misma tabla 
(*dependencia muiltivaluada*)

*clave foranea compuesta*

## 5º Forma Normal (5NF)

Se previenen las *dependencias de union* entre atributos


Si un atributo requiere unir atributos de varias tablas entonces debe ser movido a otra tabla.



!!! tip "Criterios de Normalización"

    Para diseñar bases de datos pequeñas utilizar la tercera forma normal suele ser suficiente. En cambio para bases de datos muy grandes y con necesidad de escalamiento es recomendable implementar la cuarta o la quinta forma normal.


## Referencias





[Soy Dalto - Curso de SQL desde CERO (Completo)](https://youtu.be/DFg1V-rO6Pg?t=20343)