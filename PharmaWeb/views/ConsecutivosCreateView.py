from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from PharmaWeb.serializers.consecutivosSerializer import ConsecutivosSerializer
from rest_framework.decorators import api_view
from PharmaWeb.models import Consecutivos
@api_view(['GET', 'POST'])
def consecutivo_api_view(request):
    if request.method == 'GET':
        entidades = Consecutivos.objects.all()
        entidades_serializer = ConsecutivosSerializer(entidades, many=True)
        return Response(entidades_serializer.data)
    elif request.method == 'POST':
        entidades_serializer = ConsecutivosSerializer(data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)


@api_view(['GET', 'PUT', 'DELETE'])
def consecutivo_detalle_api_view(request, pk=None):
    if request.method == 'GET':
        entidades = Consecutivos.objects.filter(id_Consecutivo=pk).first()
        entidades_serializer = ConsecutivosSerializer(entidades)
        return Response(entidades_serializer.data)
    elif request.method == 'PUT':
        entidades = Consecutivos.objects.filter(id_Consecutivo=pk).first()
        entidades_serializer = ConsecutivosSerializer( entidades, data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)
    elif request.method == 'DELETE':
        entidades = Consecutivos.objects.filter(id_Consecutivo = pk).first()
        entidades.delete()
        return Response('Eliminacion Exitosa')

