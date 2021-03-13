from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from pyprg.core.models import TurPoint
from pyprg.core.api.serializers import TurPointsSerializer


class TurPointsViewSet(ModelViewSet):
    """
    A simple Viewset for viewing the Turistics Points
    """
    serializer_class = TurPointsSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'description', 'location__line1')
    lookup_field = 'id'

    # metodo para fazer queryset
    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        queryset = TurPoint.objects.all()
        if id:
            queryset = TurPoint.objects.filter(pk=id)
        if name:
            # parametro __iexact -> ignore se a letra é maiuscula ou não
            queryset = queryset.filter(name__iexact=name)
        if description:
            queryset = queryset.objects.filter(description__iexact=description)

        return queryset

    # procedimento para sobre-escrever o metodo GET()
    # def list(self, request, *args, **kwargs):
    #     return Response({'Teste': 12345})

    # procedimento para sobre-escrever o metodo POST()
    # def create(self, request, *args, **kwargs):
    #     return Response({"Hello": request.data['name']})
    # procedimento para sobre-escrever o metodo POST()
    # def create(self, request, *args, **kwargs):
    #     return Super(TurPointsViewSet, self).create(request, *args, **kwargs)

    # procedicemento para sobre-escrever o metodo DELETE()
    # def destroy(self, request, *args, **kwargs):
    #     pass

    # procedicemento para sobre-escrever o metodo PARCIAL_UPDATE()
    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # procedicemento para sobre-escrever o metodo PARCIAL_UPDATE()
    # def update(self, request, *args, **kwargs):
    #     pass

    # procedimento pra denciar um Ponto Tyuristico
    @action(methods=['post', 'get'], detail=True)
    def denunciar(self, request, pk=None):
        pass
