from django.contrib import admin
from .models import Ensino, Serie, Organizacao, Componente, Instituicao

# Register your models here.


admin.site.register(Ensino)
admin.site.register(Serie)
admin.site.register(Organizacao)
admin.site.register(Componente)
admin.site.register(Instituicao)