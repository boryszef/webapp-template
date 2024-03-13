"""
Sample app models
"""

from django.db import models


class Data(models.Model):
    """
    Sample model with basic fields
    """

    name = models.TextField()
    value = models.IntegerField()
    weight = models.FloatField(default=-1.0)
