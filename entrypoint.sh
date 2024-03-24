#!/bin/bash
cd /app/src
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py csu
gunicorn --bind=0.0.0.0:8000 config.wsgi:application
