<!-- Crear proyecto --> composer create-project --prefer-dist blog laravel/laravel 
<!-- Crear proyecto y sellecionar versión --> composer create-project --prefer-dist blog laravel/laravel "7.1.*" 

<!-- Crear modelo --> 
php artisan make:model nombre_modelo = crea modelo
php artisan make:model Post -m -f  = crea modelo post con la migration y factory
php artisan migrate = para renderizar la carpeta migrations
php artisan make:model Post -fm = Crea el model con el factory y la migración

<!-- Controladores -->
php artisan make.controller Api/PostContoller --api --model=Post == crea un controlador y lo conecta al modelo Post

<!-- Generar autenticacón -->
<!-- libreria ui --> composer require laravel/ui
<!-- vue autenticación --> php artisan ui vue --auth
<!-- bootstrap autenticación --> php artisan ui bootstrap --auth
<!-- Instalar Bootstrap para mejorar visualización --> php artisan ui bootstrap
<!-- Mejorar la vista  -->npm install && npm run dev

<!-- Crear controlador --> php artisan make:controller NombreControlador

<!-- crea tablas iniciales -->php artisan migrate

<!-- Crear usuarios masivos -->php artisan tinker
<!-- Crea 12 usuarios --> factory(App\User::class, 12)->create()  

<!-- Crear controlador con recursos --> php artisan make:controller PageController --resource --model=Page

<!-- tinker -->
php artisan tinker = es como devel de drupal
factory(App\Post::class, 30)->create() = Crea 30 elementos de clase post

<!-- Migrates -->
php artisan migrate  = crea migraciones en la base de datos
php artisan migrate:refresh  = refresca las migraciones si no hay nada que crear
php artisan migrate:refresh --seed = mismo que lo anterior pero usa la configuración en seeds y factories

<!-- Test -->
php artisan make:test UserTest = Craer clase de test en feature
php artisan make:test UserTest --unit = Crear clase de test en Unit
ejecutar el test = .\vendor\bin\phpunit