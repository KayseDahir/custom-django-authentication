from django.contrib import admin
from . import models

# Register your models here.


class NotesAdmin(admin.ModelAdmin):
    list_display = ('title',)


# function used to register models with the django admin interface
admin.site.register(models.Notes, NotesAdmin)
