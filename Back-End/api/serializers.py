from rest_framework import serializers
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