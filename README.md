# sifos [![Build Status](https://travis-ci.org/jmencisom/sifos.svg?branch=master)](https://travis-ci.org/jmencisom/sifos) [![Coverage Status](https://coveralls.io/repos/github/jmencisom/sifos/badge.svg?branch=master)](https://coveralls.io/github/jmencisom/sifos?branch=master)
Sistema de Gestión Forestal Sostenible

## Documentation

### Requirements

[Requirements](https://drive.google.com/open?id=1oiQh0QQZMWD-ptlE9fQ2_5NQgC7TS5BWRZcsKb-Hp2k)

### Mockups

[Mockups](https://drive.google.com/open?id=1flKTkbqYR01N30gm7wugDByb4mloGO7i)

### Class diagram

[Class diagram](https://drive.google.com/open?id=1mZY2_OF6Fe3bRvz97R9OUrwiKV6pyqTZ)

## Requirements specification document, mockups and class diagram.

 [Especificación de Requisitos de Software del Sistema de Gestión Forestal sostenible - SIFO](https://drive.google.com/open?id=1NP-dPYXarNpQv6mZu3DLxRIvlqEU1YBk)

## ¿Cómo contribuir?

### Descargar repositorio

Para descargar el repositorio siga los siguientes pasos:

1. Inicie sesión en Github con su nombre de usuario y contraseña.

2. Para copiar el proyecto:

   a. Ingrese al repositorio del proyecto

   https://github.com/jmencisom/sifos
  
   b. Haga clic en el botón Fork.

   ![Paso3b](https://i.imgur.com/2mwODzD.jpg)
  
   c. Seleccione su cuenta.
 
4. Para inicializar el repositorio:
   
   a. Cree la carpeta sifos del proyecto en una partición del disco duro del PC diferente a la del sistema operativo.
   
   b. Ejecute Git extensión y cree un nuevo repositorio.
 
   ![Paso4b](http://i.imgur.com/Dbt2crn.jpg)

5. Para crear la rama o branch:
   
   a. En el Git extensión haga clic en el botón Git bash
 
   ![Paso5a](http://i.imgur.com/5hjEyYS.jpg)

   b. En la consola escriba el siguiente comando para cambiarse a la nueva rama:
      
      _$ git checkout –b dev

6. Para configurar el repositorio Origin:
   
   a. Diríjase a su copia del proyecto almacenado en Github 
   
   b. Haga clic en el botón para copiar la URL del repositorio
 
   ![Paso6b](http://i.imgur.com/dmRtEGB.jpg)

   c. En la consola escriba el siguiente comando:
      
   _$ git remote add origin_ 

   d. Seguido del comando pegue la URL de la copia del proyecto y oprima la tecla ENTER. Debe quedar de la siguiente manera: 

   _$ git remote add origin https://github.com/Nombredelrepositorio/sifos.git_

7. Para configurar el repositorio master:

   a. Diríjase al proyecto principal jmencisom/sifos almacenado en Github.

   b. Haga clic en el botón para copiar la URL del repositorio

   ![Paso7b](http://i.imgur.com/dmRtEGB.jpg)

   c. En la consola escriba el siguiente comandos:

      _$ git remote add upstream_

   d. Seguido del último comando pegue la URL del proyecto y oprima la tecla ENTER. Debe quedar de la siguiente manera: 
 
   ![Paso7d](https://i.imgur.com/aGurPz5.jpg)

   e. Para ver los repositorios configurados en la consola escriba el siguiente comando:
      
      _$ git remote -v_
 
   ![Paso7e](https://i.imgur.com/C3ps6V4.jpg)

   f. En la consola escriba el siguiente comando:

      _$ git pull upstream dev_

   g. Ingrese sus credenciales de usuario (User name y password) y haga clic en el botón OK

   ![Paso7g](http://i.imgur.com/MOwMpe0.jpg)

   Si los pasos se han realizado correctamente se inicia la descarga del proyecto.
   
   h. En la consola escriba el siguiente comando para crear una nueva rama personal para realizar los cambios (push) y no modificar la rama develop-t2.

      _$ git checkout –b nombrerama dev_
      
### Ramas del repositorio

El desarrollo de éste proyecto se está manejando con 2 ramas.

1. master
   
   La rama master es utilizada para las versión final del proyecto. Cada vez que se requiera una nueva versión de la aplicación se hace un merge entre la rama dev y la rama master.
   
2. dev
   
   La rama dev es utilizada para el desarrollo de la aplicación.
   
### Pull request con las modificaciones realizadas

Los desarrolladores deben realizar el pull request desde su origin al upstream de la rama dev. A continuación los pasos para contribuir con el repositorio.

1. Realizar las modificaciones al código necesarias.

![Paso1](https://i.imgur.com/PkDJqHB.jpg)

2. Realizar commit con un mensaje claro de las modificaciones realizadas.

![Paso2](https://i.imgur.com/klVycJ8.jpg)

3. Actualizar repositorio para mantenerlo actualizado.

![Paso3](https://i.imgur.com/lUQbqfN.jpg)

4. Realizar push a origin.

![Paso4](https://i.imgur.com/H9hwgPk.jpg)

5. Creación del pull request

   a. Diríjase al proyecto principal jmencisom/sifos almacenado en Github.
   
   https://github.com/jmencisom/sifos
   
   b. Haga clic en el botón New pull request
   
   ![Paso5b](https://i.imgur.com/dz9rLKH.jpg)
   
   c. Haga clic en el link compare across forks
   
   ![Paso5c](https://i.imgur.com/jyIM7Pw.jpg)
   
   d. Seleccione su repositorio en la sección _head fork_ y la rama a la que envío push origin en la sección _compare_ y en la sección _base fork_ seleccione la rama dev
   
   ![Paso5d](https://i.imgur.com/8nBO0XY.jpg)
   
   e. Haga clic en create pull request
   
   ![Paso5e](https://i.imgur.com/3G2d4zW.jpg)


## Docker

### Requirements

Docker - Container Framework
### Run local environments Docker

docker-compose up -d && docker restart web_web_1
### Restart and run migrations

docker restart web_web_1
### View Docker logs

docker logs --tail=100 -f web_web_1
### Install requirements

Modify requirements.txt
docker stop web_web_1
docker rm web_we
docker rmi web_web
docker-compose up -d
### Run Prod

docker build -t web_web .
docker run -d -p 80:8001 --name sifos_prod -e DATABASE_NAME=sifos -e DATABASE_USER=sifos -e DATABASE_PASSWORD=A12345678 -e DATABASE_HOST=localhost -e DATABASE_PORT=5432 web_web sh start.sh

## Wiki

[Entra a la wiki](https://github.com/jmencisom/sifos/wiki)


