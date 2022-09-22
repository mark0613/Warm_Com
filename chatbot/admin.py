from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Counselor)
admin.site.register(models.Target)
admin.site.register(models.Article)
admin.site.register(models.Reply)