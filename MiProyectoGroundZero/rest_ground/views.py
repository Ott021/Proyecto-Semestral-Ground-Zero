from django.views.decorators import csrf
from rest_ground.serializers import UsuarioSerializer
from rest_framework.serializers import Serializer
from core.models import Usuario
from django.views.decorators.csrf import csrf_exempt
from rest_ground.serializers import UsuarioSerializer
from django.shortcuts import render
from core.models import Usuario
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status


@csrf_exempt
@api_view(['GET','POST'])

def lista_usuarios(request):
    if request.method == 'GET':
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    