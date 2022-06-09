from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Program)
class ProgramAdmin(admin.ModelAdmin):
    """Admin View for Program"""

    pass


@admin.register(models.Lecture)
class ProgramAdmin(admin.ModelAdmin):
    """Admin View for Program"""

    pass
