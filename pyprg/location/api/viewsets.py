from rest_framework.viewsets import ModelViewSet
from pyprg.location.models import Location
from pyprg.location.api.serializers import LocationSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
