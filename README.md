
# Prueba Talataa π₯οΈ



## Informacion General βΉοΈ
- Proyecto creado como requisito tecnico para avanzar en la aplicacion al cargo de Ingeniero de Desarrollo en Python :bowtie:
- Lenguaje utilizado: Python π―
- API almacenada en Google Cloud βοΈ
    π https://danielserver-ougocrmvpq-uc.a.run.app/

## Tecnologias πΎ
- Docker
- Flask
- Google Cloud βοΈ
- Git Hub
- Gunicorn π¦
- MySQL
- SQL Lite

## Requerimientos para ejecucion βοΈ
- Entorno virtual
- Interprete de Python 3 
- Docker

## Guia de instalacion para desarrollo local π
 1. Clonar el repositorio localizado en GitHub
 3. Instalar las librerias a utilizar listadas en el archivo **requirements.txt** dentro de un entorno virtual
 4. Interprete de Python 3

## Guia de instalacion Docker π
 1. Clonar el repositorio localizado en GitHub
 3. Abrir el archivo Dockerfile π
      - Tiene un contenedor de Python 3οΈβ£
      - Instala las dependencias requeridas
      - Ejecuta el servicor en Gunicorn π¦
 5. Ejecutar dokerfile πββοΈ

## EjecucionποΈ
 1. Utilizar el interprete de Python 3οΈβ£
 2. π Ejecutar el archivo **main.py**


## Funcionalidades del proyecto π
`````````
**Endpoints** βοΈ **usuarios**
- β‘οΈ /user 
  - Recibe peticion **get** 
  - Lista todos los usuarios en la base de datos
- β‘οΈ /user/register
  - Recibe peticion **get**
  - Retorna Json con el formato de registro a diligenciar
  - π« Registrar el mismo correo mas de una vez por usuario
- β‘οΈ /user/orders
   - Recibe peticion **get** 
   - Retorna todas las ordenes de todos los usuarios
- β‘οΈ /user/orders/{email del usuario}
    - Recibe peticion **get**
    - Retorna la lista de ordenes por usuario
- β‘οΈ /user/createorder
    - Recibe peticion **post** para registrar la orden
    - βοΈ Usuario debe estar registrado
    - βοΈ Debe existir almenos un conductor registrado
    - βοΈ Respetar el formato de entrada que se obtiene con peticion **get**
    - π« Delivery date no puede ser anterior a la fecha de creacion de la orden
   
**Endpoints** βοΈ **conductores**   
 - β‘οΈ /driver 
  - Recibe peticion **get** 
  - Lista todos los conductores en la base de datos
 - β‘οΈ /driver/register
  - Recibe peticion **get**
  - Retorna Json con el formato de registro a diligenciar
  - π« Registrar el mismo correo mas de una vez por usuario
 - β‘οΈ /driver/orders
   - Recibe peticion **get** 
   - Retorna todas las ordenes de todos los conductores
 - β‘οΈ /driver/orders/{email}
    - Recibe peticion **get**
    - Retorna la lista de ordenes por conductor
 - β‘οΈ /user/{email}/{date}
    - Recibe peticion **get**
    - Retorna la lista de ordenes por conductor por fecha
````````````

## Autor π§ββοΈ
  Daniel Rubiano
  
## Limitacion de responsabilidades y propiedad intelectual π§ 
Codigo desarrollado unicamente por el autor atentiendo los requerimientos de la prueba enviada por email. Prohibida su ejecucion y aplicacion en ambientes         laborales o educativos sin la aprobacion expresa del autor, aprobacion que debe ser otorgada de manera escrita. 
En caso de identificarse que la propiedad intelectual del codigo se esta ejecutando sin aprobacion, se acarrearan las medidas legales correspondientes de acuerdo con la gravedad de la situacion y el territorio donde se infrinja la ley de derechos de autor.


