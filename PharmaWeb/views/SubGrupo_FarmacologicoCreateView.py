from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from PharmaWeb.serializers.Subgrupo_FarmacologicoSerializer import Subgrupo_FarmacologicoSerializer


from rest_framework.decorators import api_view
from PharmaWeb.models import Subgrupo_Farmacologico
@api_view(['GET', 'POST'])
def Subgrupo_Farmacologico_api_view(request):
    if request.method == 'GET':
        entidades = Subgrupo_Farmacologico.objects.all()
        entidades_serializer = Subgrupo_FarmacologicoSerializer(entidades, many=True)
        return Response(entidades_serializer.data)
    elif request.method == 'POST':
        entidades_serializer = Subgrupo_FarmacologicoSerializer(data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)


@api_view(['GET', 'PUT', 'DELETE'])
def Subgrupo_Farmacologico_detalle_api_view(request, pk=None):
    if request.method == 'GET':
        entidades = Subgrupo_Farmacologico.objects.filter(id_SubgrupoFarmacologico = pk).first()
        entidades_serializer = Subgrupo_FarmacologicoSerializer(entidades)
        return Response(entidades_serializer.data)
    elif request.method == 'PUT':
        entidades = Subgrupo_Farmacologico.objects.filter(id_SubgrupoFarmacologico = pk).first()
        entidades_serializer = Subgrupo_FarmacologicoSerializer(
            entidades, data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)
    elif request.method == 'DELETE':
        entidades = Subgrupo_Farmacologico.objects.filter(id_SubgrupoFarmacologico = pk).first()
        entidades.delete()
        return Response('Eliminacion Exitosa')