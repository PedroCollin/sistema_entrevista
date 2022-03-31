from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from django.forms.models import model_to_dict


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
                _dinamica = Dinamica_API.get(self, request, pk=dinamica.dinamica.id).data
                try:
                    # print('try')
                    # print(_vaga.id)
                    _respDinamica = RespostaDinamica.objects.filter(vagaDinamica=dinamica.id)
                    print(_respDinamica)
                    _candidato = Candidato.objects.filter(vaga=_vaga.id)
                    # cont = 0
                    # for resp_certa in _respDinamica:
                    #     if resp_certa.vagaDinamica =

                    print('if KKKK')
                    # print(_vaga.id)
                    din_vaga_dinamica = VagaDinamica.objects.get(vaga=_vaga.id, dinamica=_dinamica['id'])
                    print(f"STATUS: {din_vaga_dinamica.status}")
                    print(f"NEW STATUS: {din_vaga_dinamica.status}")
                    temp_vagaDinamica = din_vaga_dinamica

                    print(len(_respDinamica))
                    if len(_respDinamica) == len(_candidato):
                        temp_vagaDinamica.status = 'Finalizada'
                    elif len(_respDinamica) == 0:
                        temp_vagaDinamica.status = 'Não iniciada'
                    else:
                        temp_vagaDinamica.status = 'Iniciada'

                    # print(dinamica.status)
                    din_serializer = VagaDinamicaSerializer(din_vaga_dinamica, data=model_to_dict(temp_vagaDinamica))
                    din_serializer.is_valid(raise_exception=True)
                    din_serializer.save()
                except:
                    pass
                din_vaga_dinamica = VagaDinamica.objects.get(vaga=_vaga.id, dinamica=_dinamica['id'])
                _dinamica['status'] = din_vaga_dinamica.status
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


class Resposta_Dinamica_API(APIView):
    def get(self, request, pk=''):
        if pk == '':

            sort = request.GET.get('sort')
            _respDinamica = RespostaDinamica.objects.all()

            if sort == 'desc':
                print('desc')
                print(_respDinamica[0].candidato.nome)
                _respDinamica = _respDinamica.order_by('-candidato_id')

            serializer = RespostaDinamicaSerializer(_respDinamica, many=True)
            return Response(serializer.data)
        else:

            sort = request.GET.get('sort')
            _respDinamica = RespostaDinamica.objects.filter(vagaDinamica=pk)

            if sort == 'desc':
                print('desc')
                print(_respDinamica[0].candidato.nome)
                _respDinamica = _respDinamica.order_by('-candidato_id')

            serializer = RespostaDinamicaSerializer(_respDinamica, many=True)
            return Response(serializer.data)

    def post(self, request):

        dict_resposta = request.data
        print(dict_resposta)
        _vagaDinamica = VagaDinamica.objects.get(id=dict_resposta[0]['vagaDinamica'])

        _avaDinamicas = AvaliacaoDinamica.objects.filter(dinamica=_vagaDinamica.dinamica)

        print(_avaDinamicas)
        list_cri = [ava.criterio for ava in _avaDinamicas]
        list_peso = [ava.peso for ava in _avaDinamicas]
        dict_ava = {}
        for i, j in enumerate(list_cri):
            dict_ava[j] = list_peso[i]

        print(dict_ava)
        temp = 0
        for key, value in dict_resposta[0]['list_criterios'].items():
            if key in list_cri:
                print("TESTE: ", key)
                print('NOTA: ', value*dict_ava[key])
                temp += value*dict_ava[key]
        temp = temp/len(list_cri)
        print('tam : ', len(list_cri))
        print("Nota: ", temp)
        dict_resposta[0]['nota'] = temp
        print(dict_resposta)

        serializer = RespostaDinamicaSerializer(data=dict_resposta, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"msg": "Inserido com sucesso"})
        #return Response({"id": serializer.data['id']})

    def put(self, request, pk=''):
        _resDinamica = RespostaDinamica.objects.get(id=pk)
        serializer = RespostaDinamicaSerializer(_resDinamica, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        _resDinamica = RespostaDinamica.objects.get(id=pk)
        _resDinamica.delete()
        return Response({"msg": "Apagado com sucesso"})


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
