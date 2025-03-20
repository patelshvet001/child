from django.apps import AppConfig


class ChildvcConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'childvc'
    def ready(self):
        import childvc.signals
