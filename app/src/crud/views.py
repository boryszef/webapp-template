"""
Sample application views
"""

from rest_framework.viewsets import ModelViewSet

from crud.models import Data
from crud.serializers import DataSerializer


class DataViewSet(ModelViewSet):
    """
    Sample ViewSet class
    """

    queryset = Data.objects.all()
    serializer_class = DataSerializer
