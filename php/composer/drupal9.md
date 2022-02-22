<!-- Conexion forcontu-->

ssh -p2220 luiscabg@ssh.training.forcontu.com

<!-- Instalación -->

\$ composer create-project drupal/recommended-project:9.0.0 sb1

<!-- Cuando falla el composer -->

composer update zaporylie/composer-drupal-optimizations --no-plugins && composer update --lock

/////////////////////
Actualizar Drupal 9

// Ver modulos a actualizar
ddev composer outdated drupal/*

//Actualizar core con dependencias
$ ddev composer update drupal/core-recommended --with-dependencies

//Actualizar base de datos
ddev drush updb

---------------Exportar/Importar

- Exportar configuracion
drush cex

- Importar Configuracion
drush cim






