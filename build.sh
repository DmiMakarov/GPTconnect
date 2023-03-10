#!/usr/bin/env bash
# exit on error
set -o errexit


pip install -r requirements.txt

python manage.py makemigrations table
python manage.py migrate
python manage.py runscript load
python manage.py shell < create_user.py