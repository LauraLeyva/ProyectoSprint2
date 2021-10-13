from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from PharmaWeb.serializers.genericosSerializer import GenericosSerializer



from rest_framework.decorators import api_view
from PharmaWeb.models import Genericos
@api_view(['GET', 'POST'])
def Genericos_api_view(request):
    if request.method == 'GET':
        entidades = Genericos.objects.all()
        entidades_serializer = GenericosSerializer(entidades, many=True)
        return Response(entidades_serializer.data)
    elif request.method == 'POST':
        entidades_serializer = GenericosSerializer(data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)


@api_view(['GET', 'PUT', 'DELETE'])
def Genericos_detalle_api_view(request, pk=None):
    if request.method == 'GET':
        entidades = Genericos.objects.filter(id_Generico = pk).first()
        entidades_serializer = GenericosSerializer(entidades)
        return Response(entidades_serializer.data)
    elif request.method == 'PUT':
        entidades = Genericos.objects.filter(id_Generico = pk).first()
        entidades_serializer = GenericosSerializer(
            entidades, data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)
    elif request.method == 'DELETE':
        entidades = Genericos.objects.filter(id_Generico = pk).first()
        entidades.delete()
        return Response('Eliminacion Exitosa')
