docker run = crea un contenedor
docker run --name nombre_actual nombre_nuevo = crea el contenedor y le cambia el nombre
docker ps = lista los contenedores
docker ps -a = lista contenedores a detalles
docker ps -aq = lista solo los ID de los contenedores (la q significa quiet, tranquilo o silencioso)
docker inspect id_contenedor = detalles internos del contenedor
docker inspect nombre_contenedor = lo mismo que el anterior
docker inspect -f {{}} nombre_contenedor = filtra una variable especifico del contenedor
docker rm nombre_contenedor = elimina un contenedor
docker rm \ $(ps -aq) = borra TODOS los contenedores
docker rm -f $(docker ps -aq) = 

//////
docker run -it ubuntu = entra a la consola de ubuntu
uname -a = identificar sistema

cat /etc/lsb-release = ver distribución de linux

docker exec -it nombre_contenedor bash = abre la terminal del SO de una imagen que este corriendo

ver todas las sesiones = ps -fea

docker kill nombre_contenedor = mata el proceso del contenedor
dokcer rm -f nombre_contenedor = Fuerza el borrado del contenedor
docker run -d --name server -p 8090:80 nginx = descarga ngix, lo corre sin importar el proceso , le agrega nombre y lo publica, el puerto de la izquierda es el puerto local, y el de la derecha es del docker
////
docker run -d --name db mongo = instalar mongo
docker run --name db -d -v /directory/mogodata:/data/db mongo = Crear un sistema de archivos aparte del contenedor, tener en cuenta el -v de volumen

<!-- VOLUMENES -->

docker volume ls = ver los volumenes
docker volume prune = Borra todos los volumenes
docker volume create dbdata = Crea un volumen

$ docker run -d --name db --mount src=dbdata,dst=data/db mongo= Crea una base de datos con nombre db , monta el volumen dbdata en la ruta data/db
$ docker run -d --name db -v dbdata:/data/db mongo = Mismo de arriba pero en windows 10

<!-- Imagenes -->
$ docker image ls = listar imagenes
$ docker build -t ubuntu:platzi path(.) = Corre la imagen del Dockerfile
$ docker tag ubuntu:platzi luisc/ubuntu:platzi = agrega un usuario a la imagen
$ docker push zohan/ubuntu:platzi = enviar la imagen al repositorio de docker
$ docker history ubuntu:platzi = Ver el historial de una imagen
docker image rmi nombre_imagen --force = eilimina forzadamente una imagen
<!-- Imagenes personalizadas -->
docker-compose -f stack-billing.yml build = Constuir imagen personalizada

<!-- docker para aplicaciones -->
$ docker build -t nombre_container .
$ docker run --rm -p 3000:3000 platziapp = corre la aplicacion en el puerto 3mil, borra el repositorio
$ docker network ls = ver las redes de docker
$ docker network create --attachable nombre_red = crear una red con docker
$ docker network connect nombre_red nombre_container
$ docker network inspect nombre_red = ver redes conectadas a la red nombre_red
$ docker run -d --name app -p 3000:3000 --env MONGO_URL=mongodb://db:27017/test nombre_imagen = --name -> agrega un nuevo nombre a la union; --env MONGO_URL_mongodb://db:27017/test -> genera una valirable de entorno junto con la ruta y puerto de la base de datos; -> nombre_container = es el container con el cual se va a conectar la base de datos


<!-- Docker Compose -->
$ docker-compose up = levantar los servicios
$ docker-compose up -d = correr sin el output
$ docker-compose logs app = Ver logs de una aplicación
$ docker-compose exec app bash = entrar a la aplicación
$ docker-compose down = tumba los estados de docker
$ docker-compose build = construye la imagen
$ docker-compose scale app=4 = Crear un balanceador de la misma aplicación(tener pendiente el rango de puertos)
/////
docker-compose pull = ejecuta el archivo docker-compose.yml
docker-compose -f nombre.yml pull = ejecuta el archivo nombre.yml
docker-compose up --scale nombre_repositorio=3 -d --force-recreate = Escala un repositorio a 3 y fuerza la recreación de los contenedores


<!-- Avanzado -->
Docker tiene un dockerignore
$ docker build -t platziapp -f build/development.Dockerfile . = -f es file, teniendo otro archivo Dockerfile se corre con las directivas run install de desarrollo y pro
#docker in docker
$ docker run -it --rm -v /var/run/docker.sock:/var/run/docker.sock docker:18.06.1-ce : se monta para que escuche el deamon de docker

<!-- Docker Hub -->
docker tag billingapp:prod zohan/sales-java:0.0.1 = crear un tag 0.0.1 para el repo sales-java de la imagen billingapp:prod 

<!-- Instlar mysql en php --> docker-php-ext-install mysqli

<!-- Adicionales -->

docker system prune = Eliminar todos los contenedores detenidos

Eliminar todas las imágenes

docker rmi $(docker images -a -q)

Listar los volumenes

docker volume ls 

Eliminar todos los volumenes

docker volume prune

Construir las imagenes definidas en la orquestación

docker-compose -f stack-billing.yml build

Inicializar los contenedores de los servicios de la orquestación

docker-compose -f stack-billing.yml up -d

Detener todos los servicios de la orquestación

docker-compose -f stack-billing.yml stop

Escalar un servicio al iniciar la orquestación

docker-compose -f stack-billing.yml up --scale  billingapp-front=3 -d --force-recreate
Detener todos los contenedores

docker stop $(docker ps -a -q)

Listar las redes virtuales

docker network ls

Eliminar las redes virtuales

docker network prune

reconstruir las imagenes

docker-compose -f stack-billing.yml build --no-cache

reconstruir los contenedores d ela orquestación

docker-compose -f stack-billing.yml up -d --force-recreate