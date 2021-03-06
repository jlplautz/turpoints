from django.contrib import admin
from pyprg.core.models import TurPoint


@admin.register(TurPoint)
class AdminCore(admin.ModelAdmin):
    list_display = ('name', 'description', 'available', 'foto')
