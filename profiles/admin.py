from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Profile)
class ProAdmin(admin.ModelAdmin):
    pass
