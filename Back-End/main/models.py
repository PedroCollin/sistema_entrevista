import datetime
from enum import auto
from platform import release

import jsonfield
from black import mask_cell
from django.db import models
from users.models import User
from uuid import uuid4
from cpf_field.models import CPFField

class Curso(models.Model):
    titulo = models.CharField(max_length=255, blank=True)
    descricao = models.TextField(max_length=255, blank=True)
    data_inicio = models.DateField(auto_now_add=False, default=datetime.datetime.now())
    data_termino = models.DateField(auto_now_add=False, default=datetime.datetime.now())

class StatusVaga(models.Model):
    status = models.CharField(max_length=30)

class Usuario(models.Model):
    nome = models.CharField(max_length=30)
    edv = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    senha = models.CharField(max_length=50)

class Cidade(models.Model):
    nome = models.CharField(max_length=30)

class Dinamica(models.Model):
    titulo = models.CharField(max_length=255)
    descicao = models.TextField(max_length=255, blank=True)
    duracao = models.TimeField(blank=True)

class Candidato(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    rg = models.CharField(max_length=10)
    cpf = CPFField('Cpf', blank=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)


class AprovacaoDinamica(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)

class StatusEntrevista(models.Model):
    status = models.CharField(max_length=255)

class Entrevista(models.Model):
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=False)
    observacao = models.TextField(max_length=255)
    status = models.ForeignKey(StatusEntrevista, on_delete=models.CASCADE)

class Vaga(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    statusVaga = models.ForeignKey(StatusVaga, on_delete=models.CASCADE)
    quantidadeVaga = models.IntegerField(blank=True)
    dataAbertura = models.DateField(auto_now_add=False)
    dataFechamento = models.DateField(auto_now_add=False)

class VagaDinamica(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)
    dinamica = models.ForeignKey(Dinamica, on_delete=models.CASCADE)

class AvaliacaoDinamica(models.Model):
    dinamica = models.ForeignKey(Dinamica, on_delete=models.CASCADE)
    criterio = models.CharField(max_length=50, blank=True)
    peso = models.IntegerField(blank=True)

class RespostaDinamica(models.Model):
    vagaDinamica = models.ForeignKey(VagaDinamica, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    list_criterios = jsonfield.JSONField(blank=True)
    nota = models.IntegerField(blank=True)
    observacao = models.TextField(blank=True)


