Swtichboard Django project
=======================

This project template creates a Django 2.0 project with
a base set of applications

Requirements
---------

* Django 2.0+
* Postgres

How to run project:
--------------
* `pip install -r requirements.txt`
* `cp secrets.json.default secrets.json`
* Update secrets.json according to the requirements.
* `python manage.py makemigrations`
* `python manage.py migrate`
* `python manage.py runserver`
