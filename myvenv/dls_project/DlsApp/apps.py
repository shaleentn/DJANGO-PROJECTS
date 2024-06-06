from django.apps import AppConfig


class DlsappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DlsApp'
    
    def ready(self):
        import  DlsApp.signals