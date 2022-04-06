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


class StatusEntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusEntrevista
        fields = '__all__'

class VagaSerializerLER(serializers.ModelSerializer):
    curso = CursoSerializer(read_only=True)
    statusVaga = StatusVagaSerializer(read_only=True)
    class Meta:
        model = Vaga
        fields = '__all__'


class VagaSerializerSALVAR(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = '__all__'


class VagaDinamicaSerializerLER(serializers.ModelSerializer):
    dinamica = DinamicaSerializer(read_only=True)
    vaga = VagaSerializerLER(read_only=True)
    class Meta:
        model = VagaDinamica
        fields = '__all__'

class VagaDinamicaSerializerSALVAR(serializers.ModelSerializer):

    class Meta:
        model = VagaDinamica
        fields = '__all__'


class AvaliacaoDinamicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliacaoDinamica
        fields = '__all__'


class CandidatoSerializerLER(serializers.ModelSerializer):
    cidade = CidadeSerializer(read_only=True)
    vaga = VagaSerializerLER(read_only=True)
    class Meta:
        model = Candidato
        fields = '__all__'

class CandidatoSerializerSALVAR(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = '__all__'

class AprovacaoDinamicaSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    candidato = CandidatoSerializerLER(read_only=True)
    class Meta:
        model = AprovacaoDinamica
        fields = '__all__'

class EntrevistaSerializer(serializers.ModelSerializer):
    usuario = UserSerializer(read_only=True)
    candidato = CandidatoSerializerLER(read_only=True)
    class Meta:
        model = Entrevista
        fields = '__all__'

class RespostaDinamicaSerializerSALVAR(serializers.ModelSerializer):
    class Meta:
        model = RespostaDinamica
        fields = '__all__'

class RespostaDinamicaSerializerLER(serializers.ModelSerializer):
    print('teste')
    print(serializers.ModelSerializer)
    usuario = UserSerializer(read_only=True)
    candidato = CandidatoSerializerLER(read_only=True)
    class Meta:
        model = RespostaDinamica
        fields = '__all__'