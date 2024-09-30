from django.urls import include, path
from rest_framework import routers
from .views import (
    SalaViewSet,
    ProfessorViewSet,
    DisciplinaViewSet,
    HorarioViewSet,
    AlocacaoViewSet,
    iniciar_agendamento,
)

router = routers.DefaultRouter()
router.register(r'salas', SalaViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'disciplinas', DisciplinaViewSet)
router.register(r'horarios', HorarioViewSet)
router.register(r'alocacoes', AlocacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('agendar/', iniciar_agendamento, name='agendar'),
]