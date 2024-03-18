"""
Celery configuration
"""

import os

from celery import Celery
from celery.signals import setup_logging


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings_production')

app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

@setup_logging.connect
def config_loggers(*args, **kwargs):
    """
    Configure logging
    """
    # pylint: disable=import-outside-toplevel
    from logging.config import dictConfig
    from django.conf import settings
    dictConfig(settings.LOGGING)
