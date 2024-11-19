


# Tuto Mouredev


DBMS: DataBase Management System

RDBMS: Relational DataBase Management System

- Oracle DB
- IBM db2
- SQLite
- MariaDB
- SQL Server
- PostgreSQL
- MySQL



[Instalar MariaDB en Fedora](https://mariadb.org/download/?t=repo-config&d=Fedora+Linux&v=11+Rolling&r_m=insacom)


[Imagen MariaDB - DockerHub](https://hub.docker.com/_/mariadb)

[Instalar MariadB - Mysql en Fedora](https://docs.fedoraproject.org/en-US/quick-docs/installing-mysql-mariadb/)


## Tipos de Datos

No todas las bases de datos tienen implementados los mismos tipos de datos. 


MySQL:

- CHAR: texto - maximo 255 caracteres
- VARCHAR: texto - maximo 65536 caracteres



## Configurar admin

'root' / root_password


## MySQL / MariaDB requieren ser inicializados

- dar la orden de arranque manual
- ver la orden de arranque al inicio




## Terminal - CLI

En caso de necesitarse el uso de la DB por terminal hay que instalar una CLI (*Command Line Interface*)



## MARIADB Container
CREAR:
```bash
podman run --detach --name mariadb-test --env MARIADB_USER=dev --env MARIADB_PASSWORD=123 --env MARIADB_DATABASE=ejemplo-db --env MARIADB_ROOT_PASSWORD=my-secret-pw  mariadb:latest
```


INFO:
```bash
podman ps -a | grep mariadb-test
```


Entrar con Bash:
```bash
podman exec -it mariadb-test bash
```

### Operar como root

Logearse:
```bash
mariadb -u root -p
(ingresar_contraseña_'root')
```

Consultar bases de datos internas:

```
show databases;
```
esto muestra todas las DB internas

crear base de datos interna:
```
create database ejemplificador;
```


Salir:
```
exit
```

### Operar como user


Logearse:
```bash
mariadb -u dev -p
(ingresar_contraseña_'dev')
```

Consultar bases de datos internas:

```
show databases;
```
ahora sólo se muestran las DB con acceso del developer


Salir:
```
exit
```

(FALTAN LOS PUERTOS EXTERNOS)


CREAR CON PUERTO: 
```bash
podman run --detach --name mariadb-test --env MARIADB_USER=dev -p30000:3306 --env MARIADB_PASSWORD=123 --env MARIADB_DATABASE=ejemplo-db --env MARIADB_ROOT_PASSWORD=my-secret-pw --replace  mariadb:latest  
```




```bash
# export USER='devel'
# export PASS=
export MARIADB_ROOT_PASSWORD=1234
export MARIADB_DATABASE=mi-db

podman run --detach --name mariadb-test -p30001:3306 --env MARIADB_DATABASE=$MARIADB_DATABASE --env MARIADB_ROOT_PASSWORD=$MARIADB_ROOT_PASSWORD --replace  mariadb:latest  
```




BIEN: `-v`
```bash
# export USER='devel'
# export PASS=
export MARIADB_ROOT_PASSWORD=1234
export MARIADB_DATABASE=mi-db

# podman run --detach --name mariadb-test -p30001:3306 \
podman create --name mariadb-test -p30001:3306 \
-e MARIADB_DATABASE=$MARIADB_DATABASE \
-e MARIADB_ROOT_PASSWORD=$MARIADB_ROOT_PASSWORD \
-v mariadb-persistente:/var/lib/mysql \
--replace  mariadb:latest  
```


MAL:`--mount`

```bash
# export USER='devel'
# export PASS=
export MARIADB_ROOT_PASSWORD=1234
export MARIADB_DATABASE=mi-db

# podman run --detach --name mariadb-test -p30001:3306 \
podman create --name mariadb-test -p30001:3306 \
--env MARIADB_DATABASE=$MARIADB_DATABASE \
--env MARIADB_ROOT_PASSWORD=$MARIADB_ROOT_PASSWORD \
--mount source=mariadb-persistente,target=/var/lib/mysql \
--replace  mariadb:latest  
```




https://www.youtube.com/watch?v=DsCdbugBF8A



1:14:00





