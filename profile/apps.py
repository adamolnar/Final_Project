from django.apps import AppConfig


class ProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile'

class ProfileConfig(AppConfig):
    name = 'profile'

    def ready(self):
        from . import signals
