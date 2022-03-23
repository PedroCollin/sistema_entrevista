from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
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
            _dinamica = Dinamica.objects.all()
            serializer = DinamicaSerializer(_dinamica, many=True)
            return Response(serializer.data)
        else:
            _dinamica = Dinamica.objects.get(id=pk)
            serializer = DinamicaSerializer(_dinamica)
            _avaliacoes = AvaliacaoDinamica.objects.filter(dinamica=_dinamica.id)

            data = serializer.data
            dict_avaiacoes = {}

            for avaliacao in _avaliacoes:
                dict_avaiacoes[avaliacao.criterio] = avaliacao.peso

                print(dict_avaiacoes)
                # print(type(serializer.data))

            data["lista_criterios"] = dict_avaiacoes
            return Response(data)

    def post(self, request):
        serializer = DinamicaSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        dict_data = request.data[0]['lista_criterios']
        _dinamica = Dinamica.objects.latest('id')

        print(len(dict_data))
        if len(dict_data) >= 5:
            for criterio in dict_data:
                dict_criterio = [{
                    "dinamica": _dinamica.id,
                    "criterio": criterio,
                    "peso": dict_data[criterio]
                }]

                serializer = AvaliacaoDinamicaSerializer(data=dict_criterio, many=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        else:
            raise ValueError('Criterios insuficientes!!!')

        return Response({"msg": "Inserido com sucesso"})
        # return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        _dinamica = Dinamica.objects.get(id=pk)
        serializer = DinamicaSerializer(_dinamica, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        dict_data = request.data['lista_criterios']

        print(len(dict_data))
        if len(dict_data) >= 5:
            for criterio in dict_data:
                dict_criterio = {
                    "dinamica": _dinamica.id,
                    "criterio": criterio,
                    "peso": dict_data[criterio]
                }

                _avaliacao = AvaliacaoDinamica.objects.get(dinamica=_dinamica.id, criterio=criterio)
                serializer = AvaliacaoDinamicaSerializer(_avaliacao, data=dict_criterio)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        else:
            raise ValueError('Criterios insuficientes!!!')

        return Response(serializer.data)

    def delete(self, request, pk=''):
        _dinamica = Dinamica.objects.get(id=pk)
        _dinamica.delete()
        return Response({"msg": "Apagado com sucesso"})

class AvaliacaoDinamica_API(APIView):
    """
    API Cargos
    """

    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        print(pk)
        if pk == '':
            _avaliacao = AvaliacaoDinamica.objects.all()
            print(_avaliacao)
            serializer = AvaliacaoDinamicaSerializer(_avaliacao, many=True)
            print(serializer)
            return Response(serializer.data)
        else:
            _avaliacao = AvaliacaoDinamica.objects.get(id=pk)
            serializer = AvaliacaoDinamicaSerializer(_avaliacao)
            return Response(serializer.data)


