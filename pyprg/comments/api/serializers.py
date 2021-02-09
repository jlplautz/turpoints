from rest_framework.serializers import ModelSerializer
from pyprg.core.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'comment', 'date', 'accept']
