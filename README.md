# TestApi_Django

## Introducción

Este proyecto de Django existe con el propósito de crear servicios API REST para una aplicación móvil desarrollada en Ionic.
La aplicación para dispositivos móviles se llama TeLlevoApp y corresponde al trabajo semestral de la asignatura "Programación de Aplicaciones Móviles", de la carrera Ingeniería en Informática, del Instituto Profesional Duoc UC.
</br>

**Alumnos**
<ul>
 <li>Martín Orellana</li>
 <li>Pablo Maldonado</li>
</ul>

Repositorio del proyecto de Ionic "TeLlevoApp": https://github.com/CybeR-LuduS/pApp 

## Instrucciones

### 1.1. Instalaciones previas: Programas
**Python** (lenguaje de programación interpretado)
 * Página oficial: https://www.python.org/
</br>

**MongoDB** (motor de base de datos no relacional)
 * Página oficial de descarga: https://www.mongodb.com/try/download/community
</br>

**MongoDB Compass** (interfaz gráfica para MongoDB) 

== En el caso de no incluirse la opción en el instalador de MongoDB ==
 * Página oficial de descarga: https://www.mongodb.com/try/download/compass
</br>

### 1.2. Instalaciones previas: Framework
**Django** (framework en base a Python)
 * Ejectuar como comando CLI: _pip install django_
</br>


### 1.3. Instalaciones previas: Librerías
Para el correcto funcionamiento del proyecto de Django, es necesario tener instaladas algunas dependencias:
</br>

**Django REST framework** (framework para construir APIs REST en Django)
 * Ejectuar como comando CLI: _pip install djangorestframework_
</br>

**Djongo** (conector MongoDB para Django)
 * Ejectuar como comando CLI: _pip install djongo_
</br>

**django-cors-headers** (para permitir solicitudes en el navegador a la aplicación Django desde otros orígenes)
 * Ejectuar como comando CLI: _pip install django-cors-headers_
</br>

**Pymongo 3.12.3** (contiene herramientas para interactuar con la base de datos MongoDB desde Python) 

== Las nuevas versiones de pymongo no son compatibles con Djongo ==
 * Ejectuar como comando CLI: _pip install pymongo==3.12.3_
</br>


### 2. Ejecución
**Ejecución y conexión a base de datos**
  * Iniciar programa MongoDBCompass y establecer conexión con el servidor local
</br>

**Ejecución del servidor de Django**
  * Ejectuar como comando CLI en la carpeta del proyecto Django: _python manage.py runserver_
