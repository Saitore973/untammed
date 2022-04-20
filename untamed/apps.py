from django.apps import AppConfig


class UntamedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'untamed'
    
    def ready(self):
        import untamed.signals
