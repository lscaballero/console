# Ver versión
apachectl -v

# Iniciar servicio Ubuntu
service apache2 start

# Activar configuración de  dominio
 a2ensite drupal9.localhost.conf

# Desactivar configuración de dominio
a2dissite 000-default.conf





























# Configuración dominio

<VirtualHost *:80>
                ServerName www.drupal9.localhost
                DocumentRoot /var/www/html/drupal9.localhost/web

                # Redirect http to https
                RedirectMatch 301 (.*) https://www.drupal9.localhost$1
        </VirtualHost>

        <VirtualHost _default_:443>

                # Server Info
                ServerName www.drupal9.localhost
                ServerAlias drupal9.localhost
                ServerAdmin admin@drupal9.localhost

                # Web root
                DocumentRoot /var/www/html/drupal9.localhost/web

                # Log configuration
                ErrorLog ${APACHE_LOG_DIR}/drupal9.localhost-error.log
                CustomLog ${APACHE_LOG_DIR}/drupal9.localhost-access.log combined

                #   Enable/Disable SSL for this virtual host.
                SSLEngine on

                # Self signed SSL Certificate file
                SSLCertificateFile      /etc/ssl/drupal9.localhost.crt
                SSLCertificateKeyFile /etc/ssl/drupal9.localhost.key

                <Directory "/var/www/html/drupal9.localhost/web">
                        Options FollowSymLinks
                        AllowOverride All
                        Require all granted
                </Directory>

                <FilesMatch "\.(cgi|shtml|phtml|php)$">
                                SSLOptions +StdEnvVars
                </FilesMatch>
                <Directory /usr/lib/cgi-bin>
                                SSLOptions +StdEnvVars
                </Directory>

                BrowserMatch "MSIE [2-6]" \
                                nokeepalive ssl-unclean-shutdown \
                                downgrade-1.0 force-response-1.0
                # MSIE 7 and newer should be able to use keepalive
                BrowserMatch "MSIE [17-9]" ssl-unclean-shutdown

        </VirtualHost>

# Revisar sintaxis de la configuración de apache
apachectl configtest
