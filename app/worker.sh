#!/bin/sh

export PYTHONPATH="/app:$PYTHONPATH"
/app/venv/bin/celery -A app worker --loglevel=INFO