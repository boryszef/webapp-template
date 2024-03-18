"""
Sample serializer of the model
"""

from rest_framework.serializers import ModelSerializer

from crud.models import Data


class DataSerializer(ModelSerializer):
    """
    Sample (and simple) serializer
    """

    class Meta:
        fields = '__all__'
        model = Data
        read_only_fields = ('weight', )
