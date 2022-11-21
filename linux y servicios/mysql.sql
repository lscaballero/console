-- exportar 
mysqldump -u root -p --opt ambito > /storage/ambito.sql
mysqldump -u user -p exampledb > respaldo_exampledb.sql -- forma natural

-- importar base de datos a docker
docker exec -i my-mysql-drupal8 mysql -u root --password=admin transacciones < transacciones.sql

source db.sql -- estando en la base de datos y la copia en el misma ruta

-- structure
mysqldump -u root --no-data -p ambito > /storage/structureambito.sql

# Iniciar servicio Ubuntu
service mysql start

-- Crear vase de datos
create database drupaldb_localhost;

-- Crear usuario
create user drupaluser@localhost identified by 'drupaluser@';

-- Dar todos los privilegios a un usuario
GRANT ALL PRIVILEGES ON * . * TO 'zohan'@'localhost';

-- Dar privilegios a un usuario('drupaluser'@'localhost') a una base de datos especifica(drupaldb_localhost.*)
grant all privileges on drupaldb_localhost.* to 'drupaluser'@'localhost';