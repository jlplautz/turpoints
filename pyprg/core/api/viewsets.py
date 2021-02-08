from rest_framework.viewsets import ModelViewSet
from pyprg.core.models import TurPoint
from pyprg.core.api.serializers import TurPointsSerializer


class TurPointsViewSet(ModelViewSet):
    """
    A simple Viewset for viewing abd editing accounts
    """
    queryset = TurPoint.objects.all()
    serializer_class = TurPointsSerializer
