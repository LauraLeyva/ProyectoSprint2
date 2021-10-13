from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from PharmaWeb.serializers.PacientesSerializer import PacientesSerializer

from rest_framework.decorators import api_view
from PharmaWeb.models import Pacientes
@api_view(['GET', 'POST'])
def Pacientes_api_view(request):
    if request.method == 'GET':
        entidades = Pacientes.objects.all()
        entidades_serializer = PacientesSerializer(entidades, many=True)
        return Response(entidades_serializer.data)
    elif request.method == 'POST':
        entidades_serializer = PacientesSerializer(data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)


@api_view(['GET', 'PUT', 'DELETE'])
def Pacientes_detalle_api_view(request, pk=None):
    if request.method == 'GET':
        entidades = Pacientes.objects.filter(Cod_Paciente = pk).first()
        entidades_serializer = PacientesSerializer(entidades)
        return Response(entidades_serializer.data)
    elif request.method == 'PUT':
        entidades = Pacientes.objects.filter(Cod_Paciente = pk).first()
        entidades_serializer = PacientesSerializer(
            entidades, data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)
    elif request.method == 'DELETE':
        entidades = Pacientes.objects.filter(Cod_Paciente = pk).first()
        entidades.delete()
        return Response('Eliminacion Exitosa')
