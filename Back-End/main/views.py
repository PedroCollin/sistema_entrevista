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


class Vaga_Dinamica_API(APIView):
    """
    API Cargos
    """

    # permission_classes = (IsAuthenticated,)

    def get(self, request, pk=''):
        if pk == '':
            print('teste')
            # _vagaDinamica = VagaDinamica.objects.all()
            # dict_vagaDinamica = {}
            # for vagaDinamica in _vagaDinamica:
            #     _vaga = Vaga.objects.get(id=vagaDinamica.vaga.id)
            #     serializer = VagaSerializer(_vaga)
            #     _data = {}
            #     _data = serializer.data
            #     _vagaDinamica = VagaDinamica.objects.filter(vaga=_vaga.id)
            #
            #     print(_vagaDinamica)
            #     dict_dinamicas = {}
            #     for dinamica in _vagaDinamica:
            #         print(dinamica)
            #         _dinamica = Dinamica_API.get(self, request, pk=dinamica.id).data
            #         print('DINAMICA: ' + str(_dinamica))
            #         dict_dinamicas[_dinamica['id']] = _dinamica
            #
            #     _data['dinamica'] = dict_dinamicas
            #     dict_vagaDinamica[vagaDinamica.id] = _data
            # return Response(dict_vagaDinamica)
        else:
            _vaga = Vaga.objects.get(id=pk)
            serializer = VagaSerializer(_vaga)
            _data = {}
            _data = serializer.data
            _vagaDinamica = VagaDinamica.objects.filter(vaga=_vaga.id)

            # print(_vagaDinamica)
            dict_dinamicas = {}
            for dinamica in _vagaDinamica:
                # print(dinamica)
                _dinamica = Dinamica_API.get(self, request, pk=dinamica.id).data
                # print('DINAMICA: '+str(_dinamica))

                try:
                    print('teste')
                    _respDinamica = RespostaDinamica.objects.filter(vagaDinamica=dinamica.id)
                    print(len(_respDinamica))
                    # for resp in _respDinamica:
                    #     print(resp.list_criterios)

                    _candidato = Candidato.objects.filter(vaga=_vaga.id)
                    print(len(_candidato))

                    if len(_respDinamica) == len(_candidato)-1:
                        din_vaga_dinamica = VagaDinamica.objects.filter(vaga=_vaga.id, dinamica=dinamica.id)
                        print(din_vaga_dinamica)
                        dinamica.status = 'AOA'
                        din_serializer = VagaDinamicaSerializer(din_vaga_dinamica, data=dinamica)
                        din_serializer.is_valid(raise_exception=True)
                        din_serializer.save()
                        print('salvou')

                except:
                    pass

                _dinamica['status'] = dinamica.status
                dict_dinamicas[_dinamica['id']] = _dinamica

            _data['dinamica'] = dict_dinamicas


            return Response(_data)

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
        _vagaDinamica = Dinamica.objects.get(id=pk)
        serializer = DinamicaSerializer(_vagaDinamica, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        dict_data = request.data['lista_criterios']

        print(len(dict_data))
        if len(dict_data) >= 5:
            for criterio in dict_data:
                dict_criterio = {
                    "dinamica": _vagaDinamica.id,
                    "criterio": criterio,
                    "peso": dict_data[criterio]
                }

                _avaliacao = AvaliacaoDinamica.objects.get(dinamica=_vagaDinamica.id, criterio=criterio)
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


class Vaga_API(APIView):
    def get(self, request, pk=''):
        if pk == '':
            _vaga = Vaga.objects.all()
            serializer = VagaSerializer(_vaga, many=True)
            return Response(serializer.data)
        else:
            _vaga = Vaga.objects.get(id=pk)
            serializer = VagaSerializer(_vaga)
            return Response(serializer.data)

    def post(self, request):
        serializer = VagaSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        vaga = Vaga.objects.get(id=pk)
        serializer = VagaSerializer(vaga, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        vaga = Vaga.objects.get(id=pk)
        vaga.delete()
        return Response({"msg": "Apagado com sucesso"})


class Candidato_API(APIView):
    def get(self, request, pk=''):
        if pk == '':
            _candidato = Candidato.objects.all()
            serializer = CandidatoSerializer(_candidato, many=True)
            return Response(serializer.data)
        else:
            _candidato = Candidato.objects.get(id=pk)
            serializer = CandidatoSerializer(_candidato)
            return Response(serializer.data)

    def post(self, request):
        serializer = CandidatoSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        candidato = Candidato.objects.get(id=pk)
        serializer = CandidatoSerializer(candidato, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        candidato = Candidato.objects.get(id=pk)
        candidato.delete()
        return Response({"msg": "Apagado com sucesso"})
