from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from PharmaWeb.serializers.PresentacionSerializer import PresentacionSerializer

from rest_framework.decorators import api_view
from PharmaWeb.models import Presentacion
@api_view(['GET', 'POST'])
def Presentacion_api_view(request):
    if request.method == 'GET':
        entidades = Presentacion.objects.all()
        entidades_serializer = PresentacionSerializer(entidades, many=True)
        return Response(entidades_serializer.data)
    elif request.method == 'POST':
        entidades_serializer = PresentacionSerializer(data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)


@api_view(['GET', 'PUT', 'DELETE'])
def Presentacion_detalle_api_view(request, pk=None):
    if request.method == 'GET':
        entidades = Presentacion.objects.filter(id_Presentacion = pk).first()
        entidades_serializer = PresentacionSerializer(entidades)
        return Response(entidades_serializer.data)
    elif request.method == 'PUT':
        entidades = Presentacion.objects.filter(id_Presentacion = pk).first()
        entidades_serializer = PresentacionSerializer(
            entidades, data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)
    elif request.method == 'DELETE':
        entidades = Presentacion.objects.filter(id_Presentacion = pk).first()
        entidades.delete()
        return Response('Eliminacion Exitosa')
