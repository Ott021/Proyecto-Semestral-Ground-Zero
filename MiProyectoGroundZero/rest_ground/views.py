from django.views.decorators import csrf
from rest_ground.serializers import ObraSerializer, UsuarioSerializer
from rest_framework.serializers import Serializer
from django.views.decorators.csrf import csrf_exempt
from rest_ground.serializers import UsuarioSerializer
from django.shortcuts import render
from core.models import Usuario,Producto
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
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

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_usuario(request, id):
    try:
        usuario = Usuario.objects.get(rut=id)              
    except Usuario.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)    

    if request.method == 'GET':
        serializer = UsuarioSerializer(usuario)
        return Response(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(usuario,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        usuario.delete()
        return Response(status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_obras(request):
    if request.method == 'GET':
        obras = Producto.objects.all()
        serializer = ObraSerializer(obras,many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ObraSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_obra(request, id):
    try:
        obra = Producto.objects.get(rut=id)              
    except Producto.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)    

    if request.method == 'GET':
        serializer = ObraSerializer(obra)
        return Response(serializer.data)

    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ObraSerializer(obra,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        obra.delete()
        return Response(status.HTTP_204_NO_CONTENT)