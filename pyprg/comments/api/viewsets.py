from rest_framework.viewsets import ModelViewSet
from pyprg.comments.models import Comment
from pyprg.comments.api.serializers import CommentSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
