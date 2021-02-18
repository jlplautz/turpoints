from rest_framework.viewsets import ModelViewSet
from pyprg.core.models import TurPoint
from pyprg.core.api.serializers import TurPointsSerializer


class TurPointsViewSet(ModelViewSet):
    """
    A simple Viewset for viewing abd editing accounts
    """
    # queryset = TurPoint.objects.filter(available=True)
    serializer_class = TurPointsSerializer
    # http_method_names = ['COPY', ]

    def get_queryset(self):
        return TurPoint.objects.filter(available=True)

    # procedimento para sobre-escrever o metodo GET()
    # def list(self, request, *args, **kwargs):
    #     return Response({'Teste': 12345})

    # procediemento para sobre-escrever o metodo POST()
    # def create(self, request, *args, **kwargs):
    #     return Response({"Hello": request.data['name']})

    # procediemento para sobre-escrever o metodo DELETE()
    # def destroy(self, request, *args, **kwargs):
    #     pass

    # procediemento para sobre-escrever o metodo PARCIAL_UPDATE()
    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # procediemento para sobre-escrever o metodo PARCIAL_UPDATE()
    # def update(self, request, *args, **kwargs):
    #     pass
