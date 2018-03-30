#!/bin/bash

python3 manage.py loaddata countries
python3 manage.py loaddata states
python3 manage.py loaddata materialtype
python3 manage.py loaddata jobstatus
