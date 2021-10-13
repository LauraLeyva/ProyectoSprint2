from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from PharmaWeb.serializers.ProfesionalesSerializer import ProfesionalesSerializer

from rest_framework.decorators import api_view
from PharmaWeb.models import Profesionales
@api_view(['GET', 'POST'])
def Profesionales_api_view(request):
    if request.method == 'GET':
        entidades = Profesionales.objects.all()
        entidades_serializer = ProfesionalesSerializer(entidades, many=True)
        return Response(entidades_serializer.data)
    elif request.method == 'POST':
        entidades_serializer = ProfesionalesSerializer(data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)


@api_view(['GET', 'PUT', 'DELETE'])
def Profesionales_detalle_api_view(request, pk=None):
    if request.method == 'GET':
        entidades = Profesionales.objects.filter(Registro_Medico = pk).first()
        entidades_serializer = ProfesionalesSerializer(entidades)
        return Response(entidades_serializer.data)
    elif request.method == 'PUT':
        entidades = Profesionales.objects.filter(Registro_Medico = pk).first()
        entidades_serializer = ProfesionalesSerializer(
            entidades, data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)
    elif request.method == 'DELETE':
        entidades = Profesionales.objects.filter(Registro_Medico = pk).first()
        entidades.delete()
        return Response('Eliminacion Exitosa')