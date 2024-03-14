"""
Django signals that will fire on model instance changes
"""

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from crud.models import Data
from crud.tasks import recompute_weights

from loguru import logger


@receiver(post_save, sender=Data)
def trigger_on_save(sender, instance, created, **kwargs):  # pylint: disable=unused-argument
    """
    Recompute weights when Data instance is saved
    """
    logger.info(f'on_save triggered on {instance}')
    recompute_weights.delay()


@receiver(post_delete, sender=Data)
def trigger_on_delete(sender, instance, **kwargs):  # pylint: disable=unused-argument
    """
    Recompute weights when Data instance is deleted
    """
    logger.info(f'on_delete triggered on {instance}')
    recompute_weights.delay()
