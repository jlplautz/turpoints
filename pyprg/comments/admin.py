from django.contrib import admin
from pyprg.comments.models import Comment


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ('id', 'user', 'comment', 'date')
