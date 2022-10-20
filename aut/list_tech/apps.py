from tabnanny import verbose
from django.apps import AppConfig


class ListTechConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'list_tech'
    verbose_name = 'Cписки'