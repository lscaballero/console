Ordena los archivos por fecha de modificación: ls -t

Ordena elementos primero por nombre y después por extensión: ls -x

Ordena los elementos primero por extensión y luego por nombre: ls -X

Muestra la misma información que ls -l pero con las unidades de tamaño en KB, MB: ls -lh

Muestra el contenido de todos los subdirectorios de forma recursiva: ls -R

Ordena los resultados por tamaño de archivo: ls -S

crea un usuario en el home : sueradd -m usuarionuevo

<!-- busquedas con grep -->

grep hanks dump1.sql = [comando][expresión regular][archivo]
Para buscar sin importar si esta en mayuscula o miniscula:
grep -i hanks dump1.sql
\_Tambien podemos buscar una expresión de una frase que termine con la misma palabra que estemos buscando:
grep -i “hanks’),\$” .

<!-- sed -->

sed ‘s/hanks/selleck/g’ dump1.sql = [comando][subcomando- sustitución][expresión original][nueva expresión][modificador-(/g de global, indica que tiene que hacerse a lo largo de todo el flujo)][indicar cual es el flujo a utilizar (archivo de texto)]

SED no modifica el archivo, lo que hace es crear un nuevo flujo con la modificación
Para eliminar la ultima linea podemos utilizar:

2. sed ‘$d’ nuevasPelis.csv = [Comando][’$sub-comando’][archivo]
   awk: Trataminento de texto delimitado, este comando sirve para trabajar con archivos de textos delimitados por comas.

<!-- awk -->

awk -F ‘;’ ‘{ print \$1}’ nuevasPelis.csv

<!-- Procesos que se ejecutan en Background -->

CTRL + Z: Envía un proceso para que se ejecute por siempre en Background.
fg: Flag- Terminal devuelve dicho proceso al flag.

¿Cuales son los procesos que están en ejecución?
Para estos tenemos dos herramientas:

ps: Simplemente al ejecutarlo me dicen los procesos que he ejecutado. ps ax: los procesos que corren del sistema.

top: Es una utilidad interactiva, que me indica los recursos que utiliza el equipo e inclusive finalizar procesos del sistema.
al presionar ‘q’ salimos de allí.

¿Como detener un proceso?

Si el proceso no esta en background (&) con CTRL+C se puede finalizar.

Pero: si esta en background, primero hay que identificar el numero de ID que diferencia nuestro proceso a cortar; a través del comando ps ax

Segundo: se puede utilizar alguno de los siguientes comandos:
kill: Se utiliza colocando [comando][-9][el número de ID del proceso]
killall: Hace lo mismo pero no se le coloca el ID; sino el nombre del proceso.

<!-- Comprimir archivos y carpetas -->

Archivos .gz:
Comprimir: gzip archivo.txt
Descomprimir: gzip -d archivo.txt.gz

Archivos .tar:
Empaquetar: tar cf paquete.tar /carpeta/a/empaquetar/
Ver contenido del paquete: tar tf paquete.tar
Empaquetar y ver contenido empaquetado: tar -cvf paquete.tar /carpeta/a/empaquetar/
Desempaquetar: tar xf paquete.tar

Archivos .tar.gz:
Empaquetar y Comprimir: tar czf empaquetado.tar.gz /carpeta/a/empaquetar/y/comprimir
Descomprimir: tar xzf archivo.tar.gz

<!-- busqueda de archivos -->

find [ruta][expresión_de_búsqueda][acción]

#Ruta
#Si no se indica una ruta se toma en cuenta entonces el directorio donde se este actualmente, es decir el directorio de trabajo actual, que es lo mismo que indicar con un #punto “.”.

#Es posible asignar mas de una ruta de búsqueda también como por ejemplo

find /etc /usr /var -groupadmin

#Búsquedas básicas 👍
#Algunas banderas que podemos utilizar para buscar:
-name = Busca nombre de un archivo
-iname = Igual que name pero este no toma en consideración si tiene alguna mayúscula
-user = El usuario propietario
-group = El grupo propietario
-type = tipo de archivo, f para directorios

#Búsquedas a través del tiempo ⏰
-mmin = Tiempo en minutos
-mtime = Periodos de 24 horas
-exec; El poder aumenta 👊
-exec Permite ejecutar acciones sobre el resultado de cada línea o archivo devuelto por find, ejemplo:
find . type -f mtime +7 -exec cp {} ./backup/ \;

<!-- peticiones HTTP -->

$curl direccionweb.com
$curl -v direccionweb.com > /dev/null = solo trae los encabezados hhtp
\$wget https://www.php.net/distributions/php-7.3.10.tar.bz2 = Es mas compleja, Realiza descargas también desde el servidores http

<!-- Mailing -->

echo "Asunto" | mail -s "Mensaje a enviar" correo@correo.com = Enviar mensaje

<!-- Variables de Entorno -->

echo \$PATH = se encuentran todos los comandos ejecutables

Asignación de las variables de entorno
export: Este comando se utiliza para asignar a toda la sesión
Ejemplo: export MI_VAR = mauro, si luego escribimos echo \$MI_VAR se mostrará mauro en la terminal. (Este permanecerá miestras dure mi sesión)
.
var: Este comando solo asigna el valor para el proximo proceso que se va a ejecutar. este no es muy usual.
Ejemplo: MI_VAR=/home php env.php

<!-- cron at -->

Ojo que debemos levantar los servicios
sudo service atd start
sudo service cron start

at now +2 minutes
echo “HOLA…!!” > /home/paul/development/learning/prog_bash_shell/hola.txt

CRON
crontab -e

Y lo que demos insertar va en este orden:
1.- Minuto a ejecutarse Numero=0 a 59
2.- Hora a ejecutarse Hora=0 a 23
3.- Dia del mes o Todos Dia = 1 - 31 / Todos = _
4.- En que mes o Todos Meses = 1 - 12 / Todos = _
5.- Dia de la semana o Todos Dia = 0 (Sunday) / Todos = \*

Ej:
45 12 \* \* \* <Rutadelarchivo>/archivo.extension

# PHP
## Escoger versión de php por defecto
sudo update-alternatives --set php /usr/bin/php7.4

### Desactivar y Activar php para Apache
 - sudo a2dismod php7.1
 - sudo a2enmod php7.4

## Instalar extensiones php.4
sudo apt install -y php7.4-{bcmath,bz2,intl,gd,mbstring,mysql,zip,common}
