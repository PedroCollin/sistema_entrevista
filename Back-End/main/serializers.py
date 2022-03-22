from rest_framework import serializers
from .models import *
from main import models

class StatusVagaSerializer(serializers.ModelSerializer):
    class Meta:
        models = StatusVaga
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Curso
        fields = '__all__'

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        models = Cidade
        fields = '__all__'

class DinamicaSerializer(serializers.ModelSerializer):

    class Meta:
        models = Dinamica
        fields = (
            'id',
            'titulo',
            'descricao',
            'duracao',
        )

class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Candidato
        fields = '__all__'

class AprovacaoDinamicaSerializer(serializers.ModelSerializer):
    class Meta:
        models = AprovacaoDinamica
        fields = '__all__'

class EntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        models = Entrevista
        fields = '__all__'

class StatusEntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        models = StatusEntrevista
        fields = '__all__'

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        models = Vaga
        fields = '__all__'

class VagaDinamicaSerializer(serializers.ModelSerializer):

    class Meta:
        models = VagaDinamica
        fields = '__all__'


class AvaliacaoDinamicaSerializer(serializers.ModelSerializer):
    class Meta:
        models = AvaliacaoDinamica
        fields = '__all__'

class RespostaDinamicaSerializer(serializers.ModelSerializer):
    class Meta:
        models = RespostaDinamica
        fields = '__all__'