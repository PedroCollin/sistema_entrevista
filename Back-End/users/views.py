from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime

from rest_framework.permissions import IsAuthenticated


# Create your views here.
class signUp(APIView):

    def post(self, request):
        token = request.headers['Authorization']
        print(token)
        if not token:
            raise AuthenticationFailed('Deslogado!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
            user = User.objects.filter(id=payload['id']).first()
            print(payload)
            print(user)
            if not user:
                print("erro")
                raise AuthenticationFailed('usuario não encontrado!!')

            else:
                serializer = UserSerializer(data=request.data)
                print(request.data)
                print(serializer)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Deslogado!')

class signIn(APIView):
    def post(self, request):
        email = request.data['email']
        senha = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('Usuario não encontrado!')
        if not user.check_password(senha):
            raise AuthenticationFailed('Senha Incorreta!')


        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = ({
            'jwt': token
        })
        print(response)
        print(response.data)


        return response

class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Deslogado!')
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Deslogado!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message':'success'
        }
        return response