from django.contrib import admin

# Register your models here.
from banco_dados.models import Universo, Habilidade, Categoria, Heroi

admin.site.register(Universo)
admin.site.register(Habilidade)
admin.site.register(Categoria)
admin.site.register(Heroi)