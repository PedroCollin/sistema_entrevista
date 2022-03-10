import django
from django.db import models
import datetime
from users.models import User


class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    desc = models.CharField(max_length=255, null=True, blank=True)
    duracao = models.CharField(max_length=50)

    def __str__(self):
        return self.id

class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    rg = models.IntegerField()
    cff = models.IntegerField()
    cidade = models.CharField(max_length=100)
    status = models.CharField(max_length=15, default='1',
                               choices=(('1', 'Dinâmica'),
                                        ('2', 'Entrevista'),
                                        ('3', 'Pré-Aprovado')))

    def __str__(self):
        return self.id

class Dinamica(models.Model):
    titulo = models.CharField(max_length=100)
    desc = models.EmailField(max_length=255)
    duracao = models.TimeField()

    def __str__(self):
        return self.id

class Avaliacao_Dinamica(models.Model):
    fk_id_dinamica = models.ForeignKey(Dinamica, on_delete=models.CASCADE, null=True)
    item_de_avaliacao = models.CharField(max_length=255)


    def __str__(self):
        return self.id

class Vaga(models.Model):
    fk_id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
    quant_vaga = models.IntegerField()
    dataInicio = models.DateTimeField(default=datetime.datetime.now())
    dataFechamento = models.DateTimeField(null=True, default=datetime.datetime.now())

    def __str__(self):
        return self.id

class Vaga_Dinamica(models.Model):
    fk_id_vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, null=True)
    fk_id_dinamica = models.ForeignKey(Dinamica, on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.id

class Resposta_Dinamica(models.Model):
    fk_id_vaga_dinamica = models.ForeignKey(Vaga_Dinamica, on_delete=models.CASCADE, null=True)
    fk_id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fk_id_avaliacao_dinamica = models.ForeignKey(Avaliacao_Dinamica, on_delete=models.CASCADE, null=True)
    fk_id_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, null=True)
    resposta = models.CharField(max_length=255)


    def __str__(self):
        return self.id

class Observacao_Geral(models.Model):
    fk_id_vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, null=True)
    fk_id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fk_id_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, null=True)
    observacao = models.TextField()


    def __str__(self):
        return self.id

class Aprovacao(models.Model):
    fk_id_vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, null=True)
    fk_id_usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fk_id_candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.id