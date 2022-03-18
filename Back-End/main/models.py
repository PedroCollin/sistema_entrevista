from enum import auto
from platform import release
from black import mask_cell
from django.db import models
from users.models import User
from uuid import uuid4
from cpf_field.models import CPFField

class Curso(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(max_length=255)
    data_inicio = models.DateField(auto_now_add=False)
    data_termino = models.DateField(auto_now_add=False)

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
    descicao = models.TextField(max_length=255)
    duracao = models.TimeField(blank=True)

class Candidato(models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    rg = models.CharField(max_length=10)
    cpf = CPFField('Cpf')
    cidade = models.ForeignKey(Cidade, related_name="fk_id_cidade", on_delete=models.CASCADE)
    observacao = models.TextField(max_length=255)

class AprovacaoDinamica(models.Model):
    Usuario = models.ForeignKey(Usuario, related_name="fk_id_usuario", on_delete=models.CASCADE)
    Candidato = models.ForeignKey(Candidato, related_name="fk_id_candidato", on_delete=models.CASCADE)


class Entrevista(models.Model):
    Candidato = models.ForeignKey(Candidato, related_name="fk_id_candidato", on_delete=models.CASCADE)
    Date = models.DateField(auto_now_add=False)
    observacao = models.TextField(max_length=255)
    entrevista = models.ForeignKey(StatusEntrevista, related_name="fk_status_entrevista", on_delete=models.CASCADE)

class StatusEntrevista(models.Model):
    entrevista = models.ForeignKey(Entrevista, related_name="fk_id_entrevista", on_delete=models.CASCADE)
    dataAprovacao = models.DateField(auto_now_add=False)

class Vaga(models.Model):
    Curso = models.ForeignKey(Curso, related_name="fk_id_curso", on_delete=models.CASCADE)
    StatusVaga = models.ForeignKey(StatusVaga, related_name="fk_id_status", on_delete=models.CASCADE)
    QuantidadeVaga = models.IntegerField(blank=True)
    DataAbertura = models.DateField(auto_now_add=False)
    DataFechamento = models.DateField(auto_now_add=False)

class VagaDinamica(models.Model):
    Vaga = models.ForeignKey(Vaga, related_name="fk_id_vaga", on_delete=models.CASCADE)
    Dinamica = models.ForeignKey(Dinamica, related_name="fk_id_dinamica", on_delete=models.CASCADE)
    Status = models.CharField(max_length=30)

class RespostaDinamica(models.Model):
    VagaDinamica = models.ForeignKey(VagaDinamica, related_name="fk_id_vagaDinamica", on_delete=models.CASCADE)
    Usuario = models.ForeignKey(Usuario, related_name="fk_id_usuario", on_delete=models.CASCADE)
    Candidato = models.ForeignKey(Candidato, related_name="fk_id_candidato", on_delete=models.CASCADE)
    AvaliacaoDinamica = models.ForeignKey(AvaliacaoDinamica, related_name="fk_id_avaliacaoDinamica", on_delete=models.CASCADE)
    Candidato = models.ForeignKey(Candidato, related_name="fk_candidato", on_delete=models.CASCADE)
    Nota = models.IntegerField(blank=True)

class ListaDinamica(models.Model):
    idDinamica = models.ForeignKey(RespostaDinamica, related_name="fk_id_respostaDinamica", on_delete=models.CASCADE)
    Candidato = models.ForeignKey(Candidato, related_name="fk_id_candidato", on_delete=models.CASCADE)
    criterio = models.CharField(max_length=255)
    notaCriterio = models.IntegerField()
    

class AvaliacaoDinamica(models.Model):
    Dinamica = models.ForeignKey(Dinamica, related_name="fk_id_dinamica", on_delete=models.CASCADE)
    Criterio = models.CharField(max_length=20)

    
    