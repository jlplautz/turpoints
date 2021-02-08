from rest_framework.serializers import ModelSerializer
from core.models import TurPoint


class TurPointSerializer(ModelSerializer):
    class Meta:
        model = TurPoint
        fields = ['id', 'name', 'description', 'available']
