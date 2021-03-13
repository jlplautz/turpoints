# turpoints
This project is based on Udemy DRF Course

# Conceitos:
  - API -> Application Programming Interface
    -  E um conjunto de rotinas e padroes estabelecidos por uma aplicação qualquer,
    que permite que outras aplicaçoes consigam utilizar as funcionalidades desta 
    sem precisar conhecer detalhes da impĺementação do SW.
  - REST -> Representational State Transfer
    - é um estilo arquitetural que consiste em principios/regars/constraints
      que permitem a comunicação entre aplicaçoes
    - REST: conjunto de principios da arquitetura
    - RESTful : capacidade de determinado sistema aplicar os principios ERST
    
  - Verbos HTTP
    - GET recuperar um recurso
    - POST criar um novo recurso
    - PUT atualizar o estado de um recurso
    - PATCH atualizar o parte de um recurso
    - DELETE remover um recurso existente
    - outros 
      - Option
      - Connect
      - Head
    
  - Presentação dos dados
    - JSON -> Javascript Object Notation
      - Formato amigavel a humanos
      - chave-valor
    - YAML
    - XML
    
##  Como criar as rotas np DRF
    - No file urls.py 
      - from rest_framework import routers
      - from pyprg.core.api.viewsets import TurPointsViewSet
      - router = routers.DefaultRouter()
      - router.register(r'turpoints', TurPointsViewSet)
    
    - file api/viewsets.py
      - from rest_framework.viewsets import ModelViewSet 
      - from pyprg.evaluation.models import Evaluation
      - from pyprg.evaluation.api.serializers import EvaluationSerializer
        
      - class TurPointsViewSet(ModelViewSet):
      -    """ A simple Viewset for viewing abd editing accounts """
      -    queryset = TurPoint.objects.all()
      -    serializer_class = TurPointsSerializer
    - file api/serializers.py
      - from rest_framework.serializers import ModelSerializer
      - from pyprg.core.models import TurPoint

      - class TurPointsSerializer(ModelSerializer):
      -    class Meta:
      -    model = TurPoint
      -    fields = ['id', 'name', 'description', 'available', 'resources', 'location']

##  Como implementar filtros na viewsets.py
    - mais simples
       -  queryset = TurPoint.objects.all() -->  queryset = TurPoint.objects.filter(approuved=True)
  
    - outra possibilidade e atraves do metodo get_queryset()
       -     def get_queryset(self):
       -         return TurPoint.objects.filter(available=True)
       - file urls.py inserir o basename
       - >> router.register(r'turpoints', TurPointsViewSet, basename='Turpoints')

##  Procedimento para sobre-escrever metodo GET na viewsets.py
    -     def list(self, request, *args, **kwargs):
    -        return Response({'Teste': 12345})

##  Procedimento para sobre-escrever metodo POST na viewsets.py
    -     def create(self, request, *args, **kwargs):
    -       return Response({"Hello": request.data['name']})

##  Procedimento para sobre-escrever metodo Delete na viewsets.py
    -     def destroy(self, request, *args, **kwargs):
    -        pass

##  Procedimento para sobre-escrever metodo UPDATE na viewsets.py
    -     def retrieve(self, request, *args, **kwargs):
    -        pass

##  Procedimento para denunciar um ponto turistico
    -     def retrieve(self, request, *args, **kwargs):
    -        pass

##  Procedimento para filtro de um ponto turistico via querystring na url
    - via querystring -> qdo passamos um string na url
       - ex: localhost/turpoints/?id=8&name=Bar Batel  -> onde & é para concatenar mais de um objeto

##  Procedimento para filtro de um ponto turistico via DjangoFilterBackend
   - poetry add django-filter
   - settings.py
      - INSTALLED_APPS ->  'django_filters',
      - REST_FRAMEWORK = {'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)}
   - no file viwset
      - inserir -> filter_fields = ('id', 'name', 'description') 
    
## Procedimento para fazer -> search via url
   - inserir -> class TurPointsViewSet(ModelViewSet):
      - filter_backends = (SearchFilter,)
      - search_fields = ('name', 'description', 'location__line') -> chave extrangeira location__line1

## Procedimento para fazer -> search pelo lookup_field
   - normalmente temos o ID como lookup_field dentro do bando de dados.
     mas podemos alterar este atraves to parametro look_file -> apontando para outro campo
   - na class TurPointsViewSet(ModelViewSet):
      -  lookup_field = 'name'
      - na url -> http://localhost:8000/turpoints/Bar2/
      - https://www.django-rest-framework.org/api-guide/filtering/



# Poetry comandos
  - poetry new meuprojeto
  - cd meuprojeto
  - poetry env use 3.8  # criar a virtual env
  - poetry shell   # para ativar a virtual env
  - poetru add django@latest   # instalar a ultima versão do django
  - arquivo poetry.lock tem todos as dependencia do projeto com os respestivo hashss
  - poetry install   # para atualisar as dependencias e se tiver o arquivo poetry.lock será atualizado
  - git init         # para fazer um projeto git 
  - git add meuprojeto
  - poetry build   # para gerar um arquivo tar.gz (um distribuição simples) e outro arquivo whl (compilada)
    Uma pasta dist é criada na raiz do projeto
  - poetry export -f requirements.txt -o requirements.txt  # para exportar no formato requirement
  - poetry publish    # para publicar o projeto 
  - pip install --require-hashes -r requirements.txt  # para install o projeto com pip
  - poetry search django   

# Library installed
  - poetry add flake8  --dev
  - poetry add django@latest
  - poetry add djangorestframework
  - poetry add gunicorn
  - poetry add python-decouple
  - poetry add dj-database-url
  - poetry add psycopg2-binary

## Django project
  - django-admin startproject pontos_turisticos .
  - (.venv) tpoints $ mng startapp core
    - models.py -> Class PontoTuristico(): nome, descricao, disponivel
    - admin.py  -> @admin.register(PontoTuristico) ...
    - INSTALLED_APPS  -> 'core',
  - mng startapp atracoes
    - models.py -> Class Atracao(): nome, descricao, horario_func, idade_min
    - admin.py  -> @admin.register(Atracao) ...
    - INSTALLED_APPS  -> 'atracoes',
    

### heroku Deployment
  - ALLOWED_HOSTS = []=> ALLOWED_HOSTS = ['*']
  - file Procfile -> web: gunicorn turpoints.wsgi --log-file -
  - heroku apps:create turisticspoints
  - poetry export -o requirements.txt --without-hashes
  - git add -A
  - git commit -m "teste"
  - git push heroku 7:master -f



