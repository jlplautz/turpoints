from rest_framework.viewsets import ModelViewSet
from pyprg.evaluation.models import Evaluation
from pyprg.evaluation.api.serializers import EvaluationSerializer


class EvaluationViewSet(ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
