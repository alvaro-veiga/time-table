from django.contrib import admin
from .models import Sala, Professor, Disciplina, Horario, Alocacao

admin.site.register(Sala)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Horario)
admin.site.register(Alocacao)
