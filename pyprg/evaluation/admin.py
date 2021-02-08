from django.contrib import admin
from pyprg.evaluation.models import Evaluation


@admin.register(Evaluation)
class AdminEvaluation(admin.ModelAdmin):
    list_display = ('id', 'user', 'comment', 'note')
