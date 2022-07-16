from django.apps import AppConfig

print('now in apps.py page')

class Test1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test1'
