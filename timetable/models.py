from django.db import models

class Sala(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()
    recursos = models.TextField(blank=True)

    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    disciplinas = models.ManyToManyField('Disciplina', related_name='professores')
    disponibilidade = models.JSONField(default=dict)

    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()

    def __str__(self):
        return self.nome

class Horario(models.Model):
    dia = models.CharField(max_length=10)
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()

    def __str__(self):
        return f"{self.dia} {self.hora_inicio} - {self.hora_fim}"

class Alocacao(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.disciplina.nome} - {self.professor.nome} - {self.sala.nome} - {self.horario}"