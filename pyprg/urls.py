"""turpoints URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pyprg.core.api.viewsets import TurPointsViewSet
from pyprg.resources.api.viewsets import ResourcesViewSet
from pyprg.location.api.viewsets import LocationViewSet
from pyprg.evaluation.api.viewsets import EvaluationViewSet
from pyprg.comments.api.viewsets import CommentsViewSet

router = routers.DefaultRouter()
router.register(r'turpoints', TurPointsViewSet, basename='Turpoints')
router.register(r'comments', CommentsViewSet)
router.register(r'evaluation', EvaluationViewSet)
router.register(r'location', LocationViewSet)
router.register(r'resources', ResourcesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

]
