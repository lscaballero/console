//////////////----v-5 ---///////////////
- INSTALACION
composer create-project symfony/website-skeleton nombre_carpeta
- Apache pack
composer require symfony/apache-pack

//////////////--- v-4 --- ///////////////
- Crear controlador
php bin/console make:controller HomeController
- Crear una extension de twig
php bin/console make:twig-extension MIFiltro
- Listar rutas
php bin/console debug:router

//Database
-----
- Crear base de datos del proyecto
php bin/console doctrine:database:create
- Conectar base de datos con tablas ¡ya existentes!
php bin/console doctrine:mapping:convert --from-database yml ./src/Entity
- Importar modelos de BD
-- con Yalm
php bin/console doctrine:mapping:import App\\Entity yml --path=src/Entity  
-- con Anotation (recomendado)
php bin/console doctrine:mapping:import App\\Entity annotation --path=src/Entity
- Generar getter y setter
php bin/console make:entity --regenerate App
- Añadir getter y setter con nombre de entidad
php bin/console make:entity --regenerate App\\Entity\\Animales
- Ejecucuón de query

//Entidades
-----
- Crear Entidad desde cero
php bin/console make:entity Nombre_Entidad
- Crear tablas con los esquemas creados
php bin/console doctrine:schema:create
- Crear tablas en una migración con las entidades creadas en make:entity
php bin/console doctrine:migrations:diff
- Ejecutar la migración
php bin/console doctrine:migrations:migrate
----
Consultas SQL en consola
php bin/console doctrine:query:sql "SELECT * FROM animales"

//Cache
------------
- Borrar cache
php bin/console cache:clear --env=prod

//Rutas
---------------
- ver rutas
php bin/console debug:router
- información especifica de las rutas
php bin/console debug:router nombre_ruta

//Formularios
--------------
- Crear formulario
php bin/console make:form NombreFormulario

-- Validaciones
- Crear Validación
php bin/console make:validator

//Autenticación
----------------
- Crear clase usuario
php bin/console make:user
- Crear autenticación
php bin/console make:auth
- Crear contraseña encriptada
php bin/console security:encode-password ||  php bin/console security:hash-password (symfony 6.0.0)
- SQL que se crea con el comando php bin/console doctrine:migrations:migrate
php bin/console doctrine:migrations:migrate
- Crear Formulario de registro


//Migraciones
--------------
- Crear la migracion despues de crear la entidad
php bin/console make:migration
- Realizar la migración
php bin/console doctrine:migrations:migrate
- Crear clase y controlador de autenticación
- SQL que se crea con el comando php bin/console doctrine:migrations:migrate
php bin/console doctrine:migrations:migrate --write-sql --dry-run

//Servicios
--------------
- Listar servicios
php bin/console debug:autowiring
- Ver detalle del servicio
php bin/console debug:autowiring nombre_servicio

//Creación de comandos
--------------
- crear la clase del comando
php binb/console make:command
- Listar comandos creados
php bin/console list app

//Traducciones
---------------
- crear archivo de traducciones en formato yaml
php bin/console translation:update --force es_CO --output-format=yaml