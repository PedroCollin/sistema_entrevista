from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class Dinamica_API(APIView):
    """
    API Cargos
    """

    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if pk == '':
            dinamica = Dinamica.objects.all()
            print(dinamica)
            serializer = DinamicaSerializer(dinamica, many=True)
            print(serializer)
            return Response(serializer.data)
        else:
            _dinamica = Dinamica.objects.get(fiap=pk)
            serializer = DinamicaSerializer(_dinamica)
            return Response(serializer.data)

    def post(self, request):
        print(request.data)
        serializer = DinamicaSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
        # return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        _dinamica = Dinamica.objects.get(id=pk)
        serializer = DinamicaSerializer(_dinamica, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        _dinamica = Dinamica.objects.get(id=pk)
        _dinamica.delete()
        return Response({"msg": "Apagado com sucesso"})

