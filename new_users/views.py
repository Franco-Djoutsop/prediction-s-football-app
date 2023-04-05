from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.contrib.auth import login

from .models import Bettor
from .serializers import *

#|______________________________________________________________________________|
#|  classe qui permet d'afficher les informations selon l'enpoint choisie       |
#|______________________________________________________________________________|


# Class based view to Get User Details using Token Authentication
class UserDetailApi(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    
    def get(self, request, *args, **kwargs):
        user = Bettor.objects.get(id = request.user.id)
        serializer = BettorSerializer(user)
        return Response(serializer.data)
    
#Class based view to register user
class SignUpApiView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer
    
    
#class based view to login user

class LoginEmailView(APIView):
    permission_classes = (AllowAny,)
    
    def post(self, request, format = None):
        serializer = LoginEmailSerializer(data=self.request.data,
                                     context={'request' : self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response("connection successfully", status=status.HTTP_202_ACCEPTED)
    
    
class LoginNumberView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format = None):
        serializer = LoginNumberSerializer(data = self.request.data)
        serializer.is_valid(raise_exception= True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response("connexion successfully", status = status.HTTP_202_ACCEPTED)