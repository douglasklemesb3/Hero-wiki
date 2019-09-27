from rest_framework import routers, serializers, viewsets

from banco_dados.models import Heroi, Habilidade, Universo, Categoria


class UniversoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Universo
        fields = ('id','nome')


class HabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidade
        fields = ('id', 'nome')

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('__all__')

class HabilidadeDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)


class UniversoDTOSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(read_only=True)



class CategoriaDTOSerializer(serializers.Serializer):
    id= serializers.IntegerField()
    nome = serializers.CharField(read_only=True)


class HeroiSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nome = serializers.CharField(max_length=255)
    fraqueza = serializers.CharField(max_length=255)
    idade = serializers.IntegerField()
    universo = UniversoDTOSerializer
    habilidade = HabilidadeDTOSerializer(many=True)
    categoria = CategoriaDTOSerializer()

    def create(self,validated_data):
        habilidade_data = validated_data.pop('habilidade')
        habilidade = Habilidade.objects.get(id=habilidade_data['id'])
        heroi = Heroi.objects.create(habilidade=habilidade, **validated_data)
        return heroi


    def update(self,instance,validated_data):
        instance.nome = validated_data.get('nome')
        instance.idade = validated_data.get('idade')
        instance.fraqueza = validated_data.get('fraqueza')
        instance.universo = validated_data.get('universo')
        HabilidadE = validated_data.pop('habilidade')
        habilidade =Habilidade.objects.get(id=HabilidadE['id'])
        instance.HabilidadE = habilidade
        instance.categoria = validated_data.get('categoria')
        instance.save()
        return instance
