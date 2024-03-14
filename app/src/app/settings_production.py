"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

from loguru import logger

from app.settings_common import *  # pylint: disable=wildcard-import,unused-wildcard-import

logger.remove()
logger.add('/applogs/django.log', format="{message}", serialize=True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.environ["POSTGRES_USER"],
        "PASSWORD": os.environ["POSTGRES_PASSWORD"],
        "HOST": "db"
    }
}

broker_user = os.environ["RABBITMQ_DEFAULT_USER"]
broker_pass = os.environ["RABBITMQ_DEFAULT_PASS"]

CELERY_BROKER_URL = f"amqp://{broker_user}:{broker_pass}@broker:5672/"
