Crear imagen docker (solo la primera vez): 
sudo docker build -t m-u .

levantar ambiente de desarrollo: 
sudo docker-compose -f ./docker-compose.yml up -d

Descargamos la siguiente versión de moodle:
https://download.moodle.org/download.php/direct/stable38/moodle-latest-38.zip
copiamos el config.php en nuestro moodle    
        cp docker/compartida/config.php moodle/sitio/

Nos conectamos a nuestro contenedor de moodle:    
        docker exec -it servidormd bash

importar bk de base de datos:
docker exec -it serverdb bash
cd /compartida
mysql -u root -pNuevo123* udemycurso < udemycursov1.sql

Instalmos laravel:
docker exec -it servidorlr composer global require laravel/installer
Crearmo el proyecto:
docker exec -it servidorlr composer create-project --prefer-dist laravel/laravel udemy

docker exec -it servidorlr bash

nos movemos de directorio:
cd /var/www/html/udemy/ 

damos permisos a la carpetas de laralvel, para su ejecución:
chmod -R 777 ./

En caso de querer generara una nueva llave (ubicarse en la carpeta principal):
php artisan key:generate
ponemos el archivo de configuracion en cache (si lo modificamos, lo tenemos que correr), con el fin de hacer mas rapido su acceso de lectura:
php artisan config:cache

Generamos la autenticación basica de Laravel:
primero instalamos laravel/ui
composer require laravel/ui --dev
Instalamos NPM:

apt install npm

segundo bootstrap como ambiente ui:
php artisan ui bootstrap
chmod -R 777 ./
npm install   

Luego instalamos el tipo de autenticación
php artisan ui bootstrap --auth
chmod -R 777 ./
npm install 
npm run dev

solucionar problema con babel: 
npm install --save-dev gulp-babel @babel/core @babel/preset-env
npm run dev

Antes vamos a nuestro phpmyadmin a crear nuestra base de datos
php artisan migrate:refresh --seed

Autenticación:
https://medium.com/@cvallejo/roles-usuarios-laravel-2e1c6123ad

Docker:
https://cerebro-digital.com/panel/knowledgebase/63/Comandos-frecuentes-de-Docker.html

https://github.com/guzzle/guzzle

http://dev-web.refineddata.com/api/ (de interes para muchos que quieran integrarse con moodle)

token: 18c1d7c41dcb8be04fe229254d97d714

http://127.0.0.1:8082/webservice/rest/server.php?wstoken=18c1d7c41dcb8be04fe229254d97d714&wsfunction=core_course_get_courses&moodlewsrestformat=json
http://127.0.0.1:8082/user/editadvanced.php?id=-1


core_course_get_categories
core_course_get_courses
core_course_get_courses_by_field
core_course_get_enrolled_users_by_cmid
core_enrol_get_enrolled_users
core_enrol_get_users_courses
core_group_add_group_members
core_user_update_users
enrol_manual_unenrol_users

core_group_get_course_groups
core_role_assign_roles
core_role_unassign_roles
core_user_create_users
core_user_get_course_user_profiles
core_user_get_users
core_user_get_users_by_field
enrol_manual_enrol_users

instalar ping:
        apt-get update && apt-get install -y iputils-ping

php artisan make:model Matricular -m

php artisan make:seeder MatricularTableSeeder

php artisan migrate:refresh --seed

php artisan make:model Paisesmoodle -m

php artisan make:seeder PaisesmoodleTableSeeder

php artisan make:controller MatriculaController






//npm set audit false
pico .npmrc
fund=false

hacer bk de base de datos mysql (opcional):
cd /compartida
mysqldump -u root -pNuevo123* udemycurso > udemycursov1.sql


