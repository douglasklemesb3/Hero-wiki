"""hero_wiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework.authtoken.views import obtain_auth_token

from banco_dados.views import UniversoViewSet, HabilidadeViewSet, CategoriaViewSet, HeroiViewSet

router = routers.DefaultRouter()
router.register(r'univesos', UniversoViewSet)
router.register(r'habilidade', HabilidadeViewSet)
router.register(r'catergoria', CategoriaViewSet)
router.register(r'heroi', HeroiViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth-api/', obtain_auth_token)

]

