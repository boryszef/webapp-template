"""
Sample serializer of the model
"""

from rest_framework.serializers import ModelSerializer, FloatField

from crud.models import Data


class DataSerializer(ModelSerializer):
    """
    Sample (and simple) serializer
    """

    weight = FloatField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Data
