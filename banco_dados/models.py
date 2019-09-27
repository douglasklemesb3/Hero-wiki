from django.db import models

# Create your models here.

class Universo(models.Model):
    nome = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.nome


class Habilidade(models.Model):
    nome = models.CharField(
        max_length=255,
    )
    nivel_habilidade = models.IntegerField()

    def __str__(self):
        return self.nome


class Categoria(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name='nome',
    )
    def __str__(self):
        return self.nome



class Heroi(models.Model):
    nome = models.CharField(
         max_length= 255,
         verbose_name= 'nome'
    )
    idade= models.IntegerField()

    fraqueza = models.CharField(
         max_length=255,
         verbose_name= 'fraqueza'
     )
    universo= models.ForeignKey(Universo, on_delete=models.CASCADE)
    habilidade=models.ManyToManyField(Habilidade,related_name='heroi')
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    def __str__(self):
        return self.nome

