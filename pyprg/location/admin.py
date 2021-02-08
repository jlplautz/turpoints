from django.contrib import admin
from pyprg.location.models import Location


@admin.register(Location)
class AdminLocation(admin.ModelAdmin):
    list_display = ('id', 'line1', 'line2', 'city')
