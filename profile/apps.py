from django.apps import AppConfig
from django.apps import apps


class ProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile'

    def ready(self):
        # Import and register signals
        import profile.signals
