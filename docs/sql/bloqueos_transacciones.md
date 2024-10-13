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



# Bloqueos y Transacciones

Los **bloqueos** son un mecanismo preventivo de las bases de datos que impiden múltiples consultas simultáneas. Esto permite asegurar la integridad de los datos y prevenir tanto errores de lectura como de escritura.

SQLite utiliza bloqueo completo	mientras se realiza una operacion de escritura, en tanto que permite lecturas concurrentes.

Tipos de bloqueos:

- Bloqueos compartidos (shared locks)
Mientras se lee se permiten lecturas pero no escrituras

- Bloqueos reservados (reserved locks) 
Mientras se escribe se permiten lecturas pero no escrituras

- Bloqueos exclusivos (exclusive locks)
Mientras se escribe se impiden tanto lecturas como escrituras


Las **transacciones** son cambios volátiles que se pueden asentar permanentemente (*commit*) o deshacer (*rollback*). 

La transacción siempre comienza con el comando BEGIN:

```sql
-- Comienza una transaccion
BEGIN;
-- Se propone un cambio en ciertos registros. El cambio es temporal
UPDATE Products SET ProductName = "El Pollo" WHERE ProductName = "Chais" ;
```

Si se detecta algún error o inconsistencia en los cambios realizados se puede ordenar el paso atrás con el comando ROLLBACK:

```sql
-- Deshace los cambios
ROLLBACK
```

Si en cambio se busca guardar los cambios de forma definitiva se utiliza el comando COMMIT:

```sql
-- Asienta los cambios en la base de datos
COMMIT
```
Las transacciones son indispensables para trabajar sobre las bases de datos desde programas externos.








