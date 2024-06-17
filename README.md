# Microservicio para Consultas en Datamart
Este proyecto es parte de la prueba técnica para Desarrollador Python en Celes. El objetivo es desarrollar un microservicio en Python que interactúe con un Datamart, proporcionando una interfaz para consultas y operaciones específicas.

## Configuración del Proyecto
### Clonar el Repositorio
Para empezar, clona este repositorio en tu máquina local:
```sh
git clone https://github.com/91-julian-sanchez/celes.git
```

Abre directorio del proyecto:
```sh
cd celes
```

### Descargar Datamart
Descarga el archivo .zip del Datamart en este [enlace](https://drive.google.com/file/d/1s0irIrngQVeRDXY8F5gizkttG9Rqshg0/view) y descomprimalo en la carpeta del proyecto

## Ejecución del Proyecto
Puedes ejecutar la aplicación utilizando el Makefile o Docker Compose.

### Makefile
Para ejecutar la aplicación, simplemente ejecuta:

```sh 
make up
```

Para detener la aplicación, ejecuta:
``` sh 
make down
```

### Docker Compose
Para ejecutar la aplicación, ejecuta:

```sh 
make up
```

Para detener la aplicación, ejecuta:
``` sh 
make down
```

## Endpoints Existentes
El microservicio expone los siguientes endpoints para consultar el Datamart:

### Obtener Token de Acceso
Para obtener un token de acceso, haz una solicitud POST al endpoint /token con un formulario que incluya el nombre de usuario y la contraseña.

```sh
curl --location 'http://localhost:8000/token' \
--form 'username="johndoe"' \
--form 'password="pass"'
```

### Obtener Datos de Ventas
Puedes obtener datos de ventas por empleado, producto o tienda haciendo solicitudes GET a los siguientes endpoints, incluyendo el token de acceso en el encabezado de autorización.

* Ventas por empleado:
```sh
    curl --location 'http://localhost:8000/sales/employee/1%7C10250?start_date=2023-01-01&end_date=2023-12-31' \
    --header 'Authorization: Bearer {tu_access_token}'
```
* Ventas por producto:
```sh
  curl --location 'http://localhost:8000/sales/product/1%7C42872?start_date=2023-01-01&end_date=2023-12-31' \
--header 'Authorization: Bearer {tu_access_token}'
```
* Ventas por tienda:
```sh 
 curl --location 'http://localhost:8000/sales/store/1%7C007?start_date=2023-01-01&end_date=2023-12-31' \
--header 'Authorization: Bearer {tu_access_token}'
```

Vea la documentacion completa en [http://localhost:8000/docs](http://localhost:8000/docs)
## Ejecución de Pruebas
Para ejecutar las pruebas unitarias, puedes utilizar el siguiente comando:
```
python -m unittest tests.test_main
```