from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Osoba, Druzyna
from .serializers import OsobaSerializer, DruzynaSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
def osoba_list(request):
    if request.method == 'GET':
        osoby = Osoba.objects.all()
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def osoba_detail(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        osoba = Osoba.objects.get(pk=pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['PUT'])
def osoba_edit(request, pk):
    try:

        osoba = Osoba.objects.get(pk=pk)

    except Osoba.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':

        serializer = OsobaSerializer(osoba, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['DELETE'])
def osoba_delete(request, pk):
    try:

        osoba = Osoba.objects.get(pk=pk)

    except Osoba.DoesNotExist:

        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        osoba.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def osoba_znak(request, znak):
    if request.method == 'GET':
        osoba = Osoba.objects.all().filter(imie__icontains=znak)
        serializer = OsobaSerializer(osoba, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def druzyna_list(request):
    if request.method == 'GET':
        druzyny = Druzyna.objects.all()
        serializer = DruzynaSerializer(druzyny, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def druzyna_detail(request, pk):
    try:
        druzyna = Druzyna.objects.get(pk=pk)
    except Druzyna.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        druzyna = Druzyna.objects.get(pk=pk)
        serializer = DruzynaSerializer(druzyna)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DruzynaSerializer(druzyna, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        druzyna.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def druzyna_czlonkowie(request, pk):
    if request.method == 'GET':
        druzyna = Druzyna.objects.get(pk=pk)
        osoba = Osoba.objects.filter(kraj=druzyna)
        serializer = OsobaSerializer(osoba, many=True)
        return Response(serializer.data)