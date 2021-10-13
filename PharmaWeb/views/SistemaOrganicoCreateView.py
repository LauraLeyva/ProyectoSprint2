from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from PharmaWeb.serializers.Sistema_OrganicoSerializer import Sistema_OrganicoSerializer


from rest_framework.decorators import api_view
from PharmaWeb.models import Sistema_Organico
@api_view(['GET', 'POST'])
def Sistema_Organico_api_view(request):
    if request.method == 'GET':
        entidades = Sistema_Organico.objects.all()
        entidades_serializer = Sistema_OrganicoSerializer(entidades, many=True)
        return Response(entidades_serializer.data)
    elif request.method == 'POST':
        entidades_serializer = Sistema_OrganicoSerializer(data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)


@api_view(['GET', 'PUT', 'DELETE'])
def Sistema_Organico_detalle_api_view(request, pk=None):
    if request.method == 'GET':
        entidades = Sistema_Organico.objects.filter(id_Sistema_Organico = pk).first()
        entidades_serializer = Sistema_OrganicoSerializer(entidades)
        return Response(entidades_serializer.data)
    elif request.method == 'PUT':
        entidades = Sistema_Organico.objects.filter(id_Sistema_Organico = pk).first()
        entidades_serializer = Sistema_OrganicoSerializer(
            entidades, data=request.data)
        if entidades_serializer.is_valid():
            entidades_serializer.save()
            return Response(entidades_serializer.data)
        return Response(entidades_serializer.error_messages)
    elif request.method == 'DELETE':
        entidades = Sistema_Organico.objects.filter(id_Sistema_Organico = pk).first()
        entidades.delete()
        return Response('Eliminacion Exitosa')