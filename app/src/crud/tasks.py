"""
Asynchronous celery tasks
"""

from celery import shared_task
from django.db.models import F, Value, FloatField
from django.db.models.functions import Cast
from loguru import logger

from crud.models import Data


@shared_task
def recompute_weights():
    """
    When values change, recompute all the weights across the table.
    """
    total = sum(Data.objects.values_list('value', flat=True))
    logger.info(f'Total = {total}')
    count = Data.objects.update(
        weight=Cast(F('value'), output_field=FloatField()) / Value(total)
    )
    logger.info(f'Updated {count} records')
