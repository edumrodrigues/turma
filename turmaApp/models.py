from django.db import models


class Turma(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Aluno(models.Model):
	turma = models.ForeignKey(Turma)
	nome = models.CharField(max_length = 50)


	def __str__(self):
		return self.nome

class Professor(models.Model):
	turma = models.ManyToManyField(Turma)
	nome = models.CharField(max_length = 50)
	disciplina = models.CharField(max_length = 30)

	def __str__(self):
		return self.nome
	
