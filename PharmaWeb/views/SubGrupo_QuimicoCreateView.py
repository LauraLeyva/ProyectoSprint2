from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from PharmaWeb.serializers.SubGrupo_QuimicoSerializer import Subgrupo_QuimicoSerializer


from rest_framework.decorators import api_view
from PharmaWeb.models import Subgrupo_Quimico
@api_view(['GET', 'POST'])
def Subgrupo_Quimico_api_view(request):
    if request.method == 'GET':
        entidades = Subgrupo_Quimico.objects.all()
        entidades_serializer = Subgrupo_QuimicoSerializer(entidades, many=True)
        return Response(entidades_serializer.data)
    elif request.method == 'POST':
        entidades_serializer = Subgrupo_QuimicoSerializer(data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)


@api_view(['GET', 'PUT', 'DELETE'])
def Subgrupo_Quimico_detalle_api_view(request, pk=None):
    if request.method == 'GET':
        entidades = Subgrupo_Quimico.objects.filter(id_SubgrupoFarmacologico = pk).first()
        entidades_serializer = Subgrupo_QuimicoSerializer(entidades)
        return Response(entidades_serializer.data)
    elif request.method == 'PUT':
        entidades = Subgrupo_Quimico.objects.filter(id_SubgrupoFarmacologico = pk).first()
        entidades_serializer = Subgrupo_QuimicoSerializer(
            entidades, data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)
    elif request.method == 'DELETE':
        entidades = Subgrupo_Quimico.objects.filter(id_SubgrupoFarmacologico = pk).first()
        entidades.delete()
        return Response('Eliminacion Exitosa')