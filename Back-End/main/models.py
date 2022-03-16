from black import mask_cell
from django.db import models
from users.models import User
from uuid import uuid4

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
    