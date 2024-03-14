"""
Sample app url config
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from crud.views import DataViewSet


router = DefaultRouter()
router.register(r'data', DataViewSet, basename='data')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
