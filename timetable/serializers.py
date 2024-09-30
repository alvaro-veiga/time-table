from rest_framework import serializers
from .models import Sala, Professor, Disciplina, Horario, Alocacao

class SalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    disciplinas = serializers.PrimaryKeyRelatedField(many=True, queryset=Disciplina.objects.all())

    class Meta:
        model = Professor
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

class AlocacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alocacao
        fields = '__all__'