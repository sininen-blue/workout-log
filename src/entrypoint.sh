#!/usr/bin/env bash

touch /app/db/db.sqlite3

python manage.py collectstatic --noinput
python manage.py migrate --noinput
python -m gunicorn --bind 0.0.0.0:8000 --workers 3 WorkoutLog.wsgi:application
