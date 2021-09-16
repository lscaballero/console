<!-- Comandos basicos -->
$minikube start = iniciar minikube
$minikube status = Ver estado de  minikube
$minikube stop = detener  minikube
$minikube dashboard = abrir interfaz grafica de minikube
$minikube ip = ver ip del clouster

<!-- PODS -->
kubectl run nombre_pod --image=sotobotero/udemy-devops:0.0.1 --port=80 80 = run nombre_pod imgagen y puerto
kubectl get pods = ver pods
kubectl describe pod nombre_pod = Muestra las características del pod
kubectl expose pod nombre_pod --type=LoadBalancer --port=8080 --target-port=80 = Exponer a la web un pod en el puerto 8080

<!-- Servicios -->
kubectl get services = ver servicios
kubectl get describe services nombre_service = describe el servicio seleccionado
minikube service nombre_servicio = lanza el servicio de forma externa
kubectl delete service nombre_servicio = Borra un servicio

<!-- Comandos alternativos -->
kubectl api-versions = ver versiones de la api
echo -n "clave" | base64 = codifica la palabara clave a base 64
echo Y2xhdmU= | base64 -d = decodifica

<!-- Uso de kubectl -->
kubectl apply -f secret-dev.yaml = crea servicios individuales con base en un achivo en este caso secret-dev.yml
kubectl get all = ver un resumen en consola lo que muestra el dashboard
kubectl get pods = ver estado de los pods
kubectl delete -f ./ = eliminar todas las definiciones creadas
kubectl apply -f ./ = crear todas las configuraciones

<!-- minikube avanzado -->
minikube docker-env = generar variables de entorno de minikube
eval $(minikube -p minikube docker-env) = aplica la configuración listada