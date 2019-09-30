from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from banco_dados.models import Heroi, Universo, Habilidade, Categoria
from banco_dados.serializers import HeroiSerializer, UniversoSerializer, HabilidadeSerializer, CategoriaSerializer


class UniversoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    queryset = Universo.objects.all()
    serializer_class = UniversoSerializer


class HabilidadeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class HeroiViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    queryset = Heroi.objects.all()
    serializer_class = HeroiSerializer

