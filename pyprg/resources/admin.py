from django.contrib import admin
from pyprg.resources.models import Resource


@admin.register(Resource)
class AdminResource(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'work_time', 'age_min')
