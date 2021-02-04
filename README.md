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
    
# Poetry comandos
  - poetry new meuprojeto
  - cd meuprojeto
  - poetry env use 3.8  # criar a virtual env
  - poetry shell   # para ativar a virtual env
  - poetru add django@latest   # instalar a ultima versão do django
  - arquivo poetry.lock tem todos as dependencia do projeto com os respestivo hashss
  - poetry install   # para atualisar as dependencias e se tiver o arquivo poetry.lock será atualizado
  - git init       # para fazer um projeto git 
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


