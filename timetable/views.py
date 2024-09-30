from rest_framework import viewsets
from .models import Sala, Professor, Disciplina, Horario, Alocacao
from .serializers import SalaSerializer, ProfessorSerializer, DisciplinaSerializer, HorarioSerializer, AlocacaoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services.scheduling import agendar_tabela

class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class AlocacaoViewSet(viewsets.ModelViewSet):
    queryset = Alocacao.objects.all()
    serializer_class = AlocacaoSerializer



@api_view(['POST'])
def iniciar_agendamento(request):
    sucesso = agendar_tabela()
    if sucesso:
        return Response({'status': 'Agendamento realizado com sucesso.'})
    else:
        return Response({'status': 'Não foi possível realizar o agendamento.'}, status=400)
