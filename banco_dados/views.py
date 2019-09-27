from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from banco_dados.models import Heroi, Universo, Habilidade, Categoria
from banco_dados.serializers import HeroiSerializer, UniversoSerializer, HabilidadeSerializer, CategoriaSerializer


class UniversoViewSet(viewsets.ModelViewSet):
    queryset = Universo.objects.all()
    serializer_class = UniversoSerializer


class HabilidadeViewSet(viewsets.ModelViewSet):
    queryset = Habilidade.objects.all()
    serializer_class = HabilidadeSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class HeroiViewSet(viewsets.ModelViewSet):
    queryset = Heroi.objects.all()
    serializer_class = HeroiSerializer

