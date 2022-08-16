# Instalar certificados a un nombre de dominio
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/drupal9.localhost.key -out /etc/ssl/drupaldb.localhost.crt