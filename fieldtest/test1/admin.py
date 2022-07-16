from django.contrib import admin

from . import models

# Register your models here.


print('now in admin.py page')

admin.site.register(models.User)
admin.site.register(models.Data)
admin.site.register(models.Question)
admin.site.register(models.Choice)
