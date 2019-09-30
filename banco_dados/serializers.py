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
    id = serializers.IntegerField(required=False)
    nome = serializers.CharField(max_length=255)
    fraqueza = serializers.CharField(max_length=255)
    idade = serializers.IntegerField()
    universo = UniversoDTOSerializer()
    habilidade = HabilidadeDTOSerializer(many=True)
    categoria = CategoriaDTOSerializer()

    def create(self, validated_data):
        universo_data = validated_data.pop('universo')
        universo = Universo.objects.get(id=universo_data['id'])
        categoria_data = validated_data.pop('categoria')
        categoria = Categoria.objects.get(id=categoria_data['id'])
        heroi = Heroi.objects.create(universo=universo, categoria=categoria,
                                     nome=validated_data.get('nome'),
                                     idade=validated_data.get('idade'),
                                     fraqueza=validated_data.get('fraqueza')
                                     )

        habilidade_data = validated_data.pop('habilidade')
        habilidades = []

        for hab in habilidade_data:
            habilidades.append(Habilidade.objects.get(id=hab['id']))

        heroi.habilidade.set(habilidades)
        return heroi


    def update(self, instance,validated_data):
        universo_data = validated_data.pop('universo')
        universo = Universo.objects.get(id=universo_data['id'])
        instance.universo = universo
        categoria_data =validated_data.pop('categoria')
        categoria = Categoria.objects.get(id=categoria_data['id'])
        instance.categoria = categoria
        habilidade_data = validated_data.pop('habilidade')
        habilidades = []

        for hab in habilidade_data:
            habilidades.append(Habilidade.objects.get(id=hab['id']))

        instance.habilidade.set(habilidades)
        instance.save()
        return instance
