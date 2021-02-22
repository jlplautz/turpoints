from rest_framework.serializers import ModelSerializer
from pyprg.core.models import TurPoint


class TurPointsSerializer(ModelSerializer):
    class Meta:
        model = TurPoint
        fields = ['id', 'name', 'description', 'available', 'resources', 'location', 'foto']
