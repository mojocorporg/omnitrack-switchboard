#!/bin/bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py loaddata countries
docker-compose exec web python manage.py loaddata states
docker-compose exec web python manage.py loaddata materialtype
docker-compose exec web python manage.py loaddata jobstatus
