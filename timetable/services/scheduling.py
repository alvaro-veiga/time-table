from ortools.sat.python import cp_model
from ..models import Disciplina, Professor, Sala, Horario, Alocacao

def agendar_tabela():
    # Obter dados do banco
    disciplinas = list(Disciplina.objects.all())
    professores = list(Professor.objects.prefetch_related('disciplinas').all())
    salas = list(Sala.objects.all())
    horarios = list(Horario.objects.all())

    # Criar índices para facilitar o acesso
    disciplina_indices = {disciplina.id: idx for idx, disciplina in enumerate(disciplinas)}
    professor_indices = {professor.id: idx for idx, professor in enumerate(professores)}
    sala_indices = {sala.id: idx for idx, sala in enumerate(salas)}
    horario_indices = {horario.id: idx for idx, horario in enumerate(horarios)}

    num_disciplinas = len(disciplinas)
    num_professores = len(professores)
    num_salas = len(salas)
    num_horarios = len(horarios)

    model = cp_model.CpModel()

    # Variáveis: para cada disciplina, professor, sala e horário
    x = {}
    for d in range(num_disciplinas):
        for p in range(num_professores):
            for s in range(num_salas):
                for h in range(num_horarios):
                    x[(d, p, s, h)] = model.NewBoolVar(f'x_d{d}_p{p}_s{s}_h{h}')

    # Restrições

    # Cada disciplina deve ser alocada exatamente uma vez
    for d in range(num_disciplinas):
        model.Add(sum(x[(d, p, s, h)] for p in range(num_professores)
                                  for s in range(num_salas)
                                  for h in range(num_horarios)) == 1)

    # Um professor não pode estar em mais de uma disciplina ao mesmo tempo
    for p in range(num_professores):
        for h in range(num_horarios):
            model.Add(sum(x[(d, p, s, h)] for d in range(num_disciplinas)
                                     for s in range(num_salas)) <= 1)

    # Uma sala não pode ser usada por mais de uma disciplina ao mesmo tempo
    for s in range(num_salas):
        for h in range(num_horarios):
            model.Add(sum(x[(d, p, s, h)] for d in range(num_disciplinas)
                                     for p in range(num_professores)) <= 1)

    # Um professor deve estar disponível no horário
    for d, disciplina in enumerate(disciplinas):
        for p, professor in enumerate(professores):
            if disciplina not in professor.disciplinas.all():
                # Professor não leciona esta disciplina
                for s in range(num_salas):
                    for h in range(num_horarios):
                        model.Add(x[(d, p, s, h)] == 0)
            else:
                # Respeitar a disponibilidade
                disponibilidade = professor.disponibilidade  # Ex: {"segunda": ["08:00-12:00"], ...}
                for h, horario in enumerate(horarios):
                    dia = horario.dia.lower()
                    if dia not in disponibilidade or not any(
                        horario.hora_inicio >= parse_time(interval.split('-')[0]) and
                        horario.hora_fim <= parse_time(interval.split('-')[1])
                        for interval in disponibilidade[dia]
                    ):
                        for s in range(num_salas):
                            model.Add(x[(d, p, s, h)] == 0)

    # Função Objetivo: Minimizar o uso de salas ou balancear a carga horária
    # Aqui, por simplicidade, não estamos definindo uma função objetivo específica
    model.Maximize(1)  # Apenas satisfazer as restrições

    # Resolver o modelo
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        # Limpar alocações existentes
        Alocacao.objects.all().delete()

        # Criar novas alocações
        for d in range(num_disciplinas):
            for p in range(num_professores):
                for s in range(num_salas):
                    for h in range(num_horarios):
                        if solver.Value(x[(d, p, s, h)]) == 1:
                            Alocacao.objects.create(
                                disciplina=disciplinas[d],
                                professor=professores[p],
                                sala=salas[s],
                                horario=horarios[h]
                            )
        return True
    else:
        return False

def parse_time(time_str):
    """Converte string de tempo 'HH:MM' para objeto time"""
    from datetime import datetime
    return datetime.strptime(time_str, '%H:%M').time()
