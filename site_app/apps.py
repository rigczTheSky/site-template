from django.apps import AppConfig
from django.db.models.signals import post_migrate

def create_default_categories(sender, **kwargs):
    from .models import Category
    default_categories = ['Domestic', 'World', 'About']
    for name in default_categories:
        Category.objects.get_or_create(name=name)

class SiteAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'site_app'

    def ready(self):
        post_migrate.connect(create_default_categories, sender=self)
