"""
Sample app
"""

from django.apps import AppConfig


class CrudConfig(AppConfig):
    """
    Sample app config
    """

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'crud'

    def ready(self):
        """
        Do stuff when the app is loaded
        """
        import crud.listeners  # pylint: disable=import-outside-toplevel,unused-import
