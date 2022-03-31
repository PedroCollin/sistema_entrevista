from rest_framework import serializers
from .models import *
from .models import Dinamica
from users.serializers import UserSerializer


class StatusVagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusVaga
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = '__all__'

class DinamicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dinamica
        fields = '__all__'

class AprovacaoDinamicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AprovacaoDinamica
        fields = '__all__'

class EntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrevista
        fields = '__all__'

class StatusEntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusEntrevista
        fields = '__all__'

class VagaSerializer(serializers.ModelSerializer):
    curso = CursoSerializer(read_only=True)
    statusVaga = StatusVagaSerializer(read_only=True)
    class Meta:
        model = Vaga
        fields = '__all__'

class VagaDinamicaSerializer(serializers.ModelSerializer):
    dinamica = DinamicaSerializer(read_only=True)
    vaga = VagaSerializer(read_only=True)
    class Meta:
        model = VagaDinamica
        fields = '__all__'


class AvaliacaoDinamicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliacaoDinamica
        fields = '__all__'


class CandidatoSerializer(serializers.ModelSerializer):
    cidade = CidadeSerializer(read_only=True)
    vaga = VagaSerializer(read_only=True)
    class Meta:
        model = Candidato
        fields = '__all__'

class RespostaDinamicaSerializer(serializers.ModelSerializer):

    usuario = UserSerializer(read_only=True)
    candidato = CandidatoSerializer(read_only=True)
    class Meta:
        model = RespostaDinamica
        fields = '__all__'