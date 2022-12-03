
# Prueba Talataa 🖥️



## Informacion General ℹ️
- Proyecto creado como requisito tecnico para avanzar en la aplicacion al cargo de Ingeniero de Desarrollo en Python :bowtie:
- Lenguaje utilizado: Python 💯
- API almacenada en Google Cloud ☁️
    🔗 

## Tecnologias 💾
- Docker
- Flask
- Google Cloud ☁️
- Git Hub
- Gunicorn 🦄
- MySQL
- SQL Lite

## Requerimientos para ejecucion ✔️
- Entorno virtual
- Interprete de Python 3 
- Docker

## Guia de instalacion para desarrollo local 📖
 1. Clonar el repositorio localizado en GitHub
 3. Instalar las librerias a utilizar listadas en el archivo **requirements.txt** dentro de un entorno virtual
 4. Interprete de Python 3

## Guia de instalacion Docker 📖
 1. Clonar el repositorio localizado en GitHub
 3. Abrir el archivo Dockerfile 📂
      - Tiene un contenedor de Python 3️⃣
      - Instala las dependencias requeridas
      - Ejecuta el servicor en Gunicorn 🦄
 5. Ejecutar dokerfile 🏃‍♀️

## Ejecucion🖊️
 1. Utilizar el interprete de Python 3️⃣
 2. 🏃 Ejecutar el archivo **main.py**


## Funcionalidades del proyecto 📝
`````````
**Endpoints** ☝️ **usuarios**
- ➡️ /user 
  - Recibe peticion **get** 
  - Lista todos los usuarios en la base de datos
- ➡️ /user/register
  - Recibe peticion **get**
  - Retorna Json con el formato de registro a diligenciar
  - 🚫 Registrar el mismo correo mas de una vez por usuario
- ➡️ /user/orders
   - Recibe peticion **get** 
   - Retorna todas las ordenes de todos los usuarios
- ➡️ /user/orders/{email del usuario}
    - Recibe peticion **get**
    - Retorna la lista de ordenes por usuario
- ➡️ /user/createorder
    - Recibe peticion **post** para registrar la orden
    - ☑️ Usuario debe estar registrado
    - ☑️ Debe existir almenos un conductor registrado
    - ☑️ Respetar el formato de entrada que se obtiene con peticion **get**
    - 🚫 Delivery date no puede ser anterior a la fecha de creacion de la orden
   
**Endpoints** ☝️ **conductores**   
 - ➡️ /driver 
  - Recibe peticion **get** 
  - Lista todos los conductores en la base de datos
 - ➡️ /driver/register
  - Recibe peticion **get**
  - Retorna Json con el formato de registro a diligenciar
  - 🚫 Registrar el mismo correo mas de una vez por usuario
 - ➡️ /driver/orders
   - Recibe peticion **get** 
   - Retorna todas las ordenes de todos los conductores
 - ➡️ /driver/orders/{email}
    - Recibe peticion **get**
    - Retorna la lista de ordenes por conductor
 - ➡️ /user/{email}/{date}
    - Recibe peticion **get**
    - Retorna la lista de ordenes por conductor por fecha
````````````

## Autor 🧞‍♂️
  Daniel Rubiano
  
## Limitacion de responsabilidades y propiedad intelectual 🧠
Codigo desarrollado unicamente por el autor atentiendo los requerimientos de la prueba enviada por email. Prohibida su ejecucion y aplicacion en ambientes         laborales o educativos sin la aprobacion expresa del autor, aprobacion que debe ser otorgada de manera escrita. 
En caso de identificarse que la propiedad intelectual del codigo se esta ejecutando sin aprobacion, se acarrearan las medidas legales correspondientes de acuerdo con la gravedad de la situacion y el territorio donde se infrinja la ley de derechos de autor.


