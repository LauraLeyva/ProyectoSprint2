from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from PharmaWeb.serializers.GrupoFarmacologicoSerializer import Grupo_FarmacologicoSerializer

from rest_framework.decorators import api_view
from PharmaWeb.models import Grupo_Farmacologico
@api_view(['GET', 'POST'])
def Grupo_Farmacologico_api_view(request):
    if request.method == 'GET':
        entidades = Grupo_Farmacologico.objects.all()
        entidades_serializer = Grupo_FarmacologicoSerializer(entidades, many=True)
        return Response(entidades_serializer.data)
    elif request.method == 'POST':
        entidades_serializer = Grupo_FarmacologicoSerializer(data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)


@api_view(['GET', 'PUT', 'DELETE'])
def Grupo_Farmacologico_detalle_api_view(request, pk=None):
    if request.method == 'GET':
        entidades = Grupo_Farmacologico.objects.filter(id_Grupo_Farmacologico = pk).first()
        entidades_serializer = Grupo_FarmacologicoSerializer(entidades)
        return Response(entidades_serializer.data)
    elif request.method == 'PUT':
        entidades = Grupo_Farmacologico.objects.filter(id_Grupo_Farmacologico = pk).first()
        entidades_serializer = Grupo_FarmacologicoSerializer(
            entidades, data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)
    elif request.method == 'DELETE':
        entidades = Grupo_Farmacologico.objects.filter(id_Grupo_Farmacologico = pk).first()
        entidades.delete()
        return Response('Eliminacion Exitosa')
