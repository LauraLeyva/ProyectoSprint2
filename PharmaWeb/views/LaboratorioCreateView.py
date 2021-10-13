from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from PharmaWeb.serializers.LaboratoriosSerializer import LaboratoriosSerializer

from rest_framework.decorators import api_view
from PharmaWeb.models import Laboratorios
@api_view(['GET', 'POST'])
def Laboratorios_api_view(request):
    if request.method == 'GET':
        entidades = Laboratorios.objects.all()
        entidades_serializer = LaboratoriosSerializer(entidades, many=True)
        return Response(entidades_serializer.data)
    elif request.method == 'POST':
        entidades_serializer = LaboratoriosSerializer(data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)


@api_view(['GET', 'PUT', 'DELETE'])
def Laboratorios_detalle_api_view(request, pk=None):
    if request.method == 'GET':
        entidades = Laboratorios.objects.filter(id_Laboratorio = pk).first()
        entidades_serializer = LaboratoriosSerializer(entidades)
        return Response(entidades_serializer.data)
    elif request.method == 'PUT':
        entidades = Laboratorios.objects.filter(id_Laboratorio = pk).first()
        entidades_serializer = LaboratoriosSerializer(
            entidades, data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)
    elif request.method == 'DELETE':
        entidades = Laboratorios.objects.filter(id_Laboratorio = pk).first()
        entidades.delete()
        return Response('Eliminacion Exitosa')
