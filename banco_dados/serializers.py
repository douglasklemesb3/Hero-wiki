from rest_framework import routers, serializers, viewsets

from banco_dados.models import Heroi, Habilidade, Universo, Categoria


class UniversoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universo
        fields = ('id','nome')


class HabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidade
        fields = ('id', 'nome','nivel_habilidade')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')

class HeroiSerializer(serializers.ModelSerializer):
    habilidade = HabilidadeSerializer(many=True)
    class Meta:
        model = Heroi
        fields = ('nome','fraqueza','universo', 'idade', 'habilidade', 'categoria')

