from rest_framework.viewsets import ModelViewSet
from core.models import TurPoint
from .serializers import TurPointSerializer


class TurPointsViewSet(ModelViewSet):
    """
    A simple Viewset for viewing abd editing accounts
    """
    queryset = TurPoint.objects.all()
    serializer_class = TurPointSerializer
