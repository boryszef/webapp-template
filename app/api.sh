#!/bin/sh

export PYTHONPATH="/app:$PYTHONPATH"
python /app/manage.py migrate --settings=app.settings_production
python /app/manage.py collectstatic --settings=app.settings_production --no-input
/app/venv/bin/uwsgi --http :9005 --wsgi-file /app/app/wsgi.py