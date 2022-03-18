from rest_framework import serializers
from soupsieve import select
from main import models

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Usuario
        fields = '__all__'

class StatusVagaSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.StatusVaga
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Curso
        fields = '__all__'

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Cidade
        fields = '__all__'

class DinamicaSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Dinamica
        fields = '__all__'

class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Candidato
        fields = '__all__'

class AprovacaoDinamicaSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.AprovacaoDinamica
        fields = '__all__'

class ObservacaoGeralSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.ObservacaoGeral
        fields = '__all__'

class EntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Entrevista
        fields = '__all__'

class StatusEntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.StatusEntrevista
        fields = '__all__'

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Vaga
        fields = '__all__'

class VagaDinamicaSerializer(serializers.ModelSerializer):

    class Meta:
        models = models.VagaDinamica
        fields = '__all__'


class AvaliacaoDinamicaSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.AvaliacaoDinamica
        fields = '__all__'

class ListaDinamicaSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.ListaDinamica
        fields = '__all__'


class RespostaDinamicaSerializer(serializers.ModelSerializer):
    criterio = ListaDinamicaSerializer(read_only=True) 
    notaCriterio = ListaDinamicaSerializer(read_only=True) 

    class Meta:
        models = models.RespostaDinamica
        fields = '__all__'