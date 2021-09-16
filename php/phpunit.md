- Correr pruebas en un grupo
Forma 1 = ../vendor/bin/phpunit --group nombre_grupo --filter nombre_funcion
Forma 2 = php ../vendor/phpunit/phpunit/phpunit --group nombre_grupo --filter nombre_funcion

- Ver la linea donde ocurrio el error y poder colocar un var_dump()
../vendor/bin/phpunit --group nombre_grupo --filter nombre_funcion --verbose --debug
php ../vendor/phpunit/phpunit/phpunit --group nombre_grupo --filter nombre_funcion --verbose --debug