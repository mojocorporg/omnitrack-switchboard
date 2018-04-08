Swtichboard Django project
=======================

This project template creates a Django 2.0 project with
a base set of applications

Requirements
---------

* docker
* docker-compose

How to run project:
--------------
* `docker-compose up -d`
* `./init.sh`

Using API's:
----------
* Create a user with admin.
* Create a token with that user either by api or using admin.
* Api can be consumed by basic auth(username and password) or by token.
* `curl -X GET http://localhost:8000/appname/api/model_name/ -H 'Authorization: Token 1789bb6ddcf255a3c342f487ed79e4866b55828d'`

Using Swagger:
----------
* You can simply use swagger for the api documentation.
* You need to login with the superuser privileges. Only, then you can see all swagger api's
