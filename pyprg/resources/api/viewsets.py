from rest_framework.viewsets import ModelViewSet
from pyprg.resources.models import Resource
from pyprg.resources.api.serializers import ResourceSerializer


class ResourcesViewSet(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
