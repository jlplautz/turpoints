from rest_framework.serializers import ModelSerializer
from pyprg.resources.models import Resource


class ResourceSerializer(ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name', 'description', 'work_time', 'age_min']
